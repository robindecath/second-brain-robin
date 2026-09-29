#!/usr/bin/env python3
"""
Parse benchmark YAML configs and extract required environment variables.
Helps auto-discover env var requirements without manual setup.
"""

import yaml
import re
import sys
from pathlib import Path

def extract_env_vars_from_comments(yaml_file):
    """Extract env var export commands from YAML comments."""
    env_vars = {}
    
    with open(yaml_file) as f:
        content = f.read()
    
    # Look for lines like: #   export TECH_RADAR_PATH=/path/to/...
    pattern = r'#\s+export\s+(\w+)=([^\n]+)'
    matches = re.findall(pattern, content)
    
    for var_name, var_path in matches:
        env_vars[var_name] = var_path.strip()
    
    return env_vars

def get_agent_name_from_config(yaml_file):
    """Extract agent name from benchmark config."""
    with open(yaml_file) as f:
        data = yaml.safe_load(f)
    
    return data.get('project', 'unknown')

def get_all_benchmarks(repo_root):
    """Find all benchmark YAML files in the repository."""
    benchmarks = []
    repo_path = Path(repo_root)
    
    # Look for *-benchmark.yml files
    for benchmark_file in repo_path.glob('**/bmad-*-benchmark.yml'):
        agent_name = get_agent_name_from_config(benchmark_file)
        env_vars = extract_env_vars_from_comments(benchmark_file)
        
        benchmarks.append({
            'path': str(benchmark_file),
            'agent': agent_name,
            'env_vars': env_vars,
            'relative_path': str(benchmark_file.relative_to(repo_path))
        })
    
    return sorted(benchmarks, key=lambda x: x['agent'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        repo_root = sys.argv[1]
    else:
        repo_root = '.'
    
    benchmarks = get_all_benchmarks(repo_root)
    
    if not benchmarks:
        print("No benchmarks found", file=sys.stderr)
        sys.exit(1)
    
    # Output as shell-friendly format
    for b in benchmarks:
        print(f"AGENT={b['agent']}")
        print(f"CONFIG={b['relative_path']}")
        for var, path in b['env_vars'].items():
            print(f"  {var}={path}")
        print()
