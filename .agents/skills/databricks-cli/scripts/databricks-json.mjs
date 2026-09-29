import { readFileSync } from 'node:fs';

const states = new Set(['PENDING', 'RUNNING', 'SUCCEEDED', 'FAILED', 'CANCELED', 'CLOSED']);

function parseResponse() {
  let response;
  try {
    response = JSON.parse(readFileSync(0, 'utf8'));
  } catch {
    throw new Error('Databricks returned invalid JSON; no result can be reported.');
  }
  if (
    !response || typeof response !== 'object' ||
    typeof response.statement_id !== 'string' ||
    !/^[a-zA-Z0-9_-]+$/.test(response.statement_id) ||
    !states.has(response.status?.state)
  ) {
    throw new Error('Databricks response is missing a valid statement_id or status.state.');
  }
  return response;
}

try {
  const [mode, warehouseId, statement, catalog, schema] = process.argv.slice(2);
  if (mode === 'request') {
    if (!warehouseId || !statement) throw new Error('warehouse_id and statement are required.');
    const body = { warehouse_id: warehouseId, statement, wait_timeout: '30s' };
    if (catalog) body.catalog = catalog;
    if (schema) body.schema = schema;
    console.log(JSON.stringify(body));
  } else if (mode === 'status') {
    const response = parseResponse();
    console.log(`${response.statement_id} ${response.status.state}`);
  } else if (mode === 'result') {
    const response = parseResponse();
    if (response.status.state !== 'SUCCEEDED') throw new Error('Statement has not succeeded.');
    const { manifest, result } = response;
    const partial = manifest?.truncated === true ||
      manifest?.total_chunk_count > 1 ||
      result?.next_chunk_index != null ||
      Boolean(result?.next_chunk_internal_link) ||
      Boolean(result?.external_links?.length) ||
      (manifest?.total_row_count > 0 &&
        (!Array.isArray(result?.data_array) || result.data_array.length < manifest.total_row_count));
    console.log(JSON.stringify(response));
    if (partial) {
      console.error(
        'INCOMPLETE RESULTS: the JSON contains only part of the result or links to data. ' +
        'Do not report these rows as the complete answer. Follow result.next_chunk_internal_link ' +
        'with the same profile to retrieve further chunks; if manifest.truncated is true, ' +
        'use a narrower query or an explicitly chosen export strategy.'
      );
      process.exitCode = 3;
    }
  } else {
    throw new Error('Expected request, status, or result mode.');
  }
} catch (error) {
  console.error(error instanceof Error ? error.message : 'Failed to process Databricks JSON.');
  process.exitCode = 1;
}
