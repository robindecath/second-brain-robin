.PHONY: help test-benchmark test-benchmark-setup test-benchmark-run test-benchmark-clean test-all test-all-parallel test-all-seq test test-agent-dev test-agent-pm test-agent-ux test-agent-sre test-build test-sprint-planning test-architecture

help:
	@echo "Benchmark Test Targets:"
	@echo ""
	@echo "Single Agent (bmad-agent-architect):"
	@echo "  make test-benchmark           - Full test cycle (setup → run → clean)"
	@echo "  make test-benchmark-setup     - Create temp BMAD + apply customization"
	@echo "  make test-benchmark-run       - Run benchmark against real setup"
	@echo "  make test-benchmark-clean     - Clean up temp directories"
	@echo ""
	@echo "All Agents (run all benchmarks with zero manual config):"
	@echo "  make test-all                 - Run all benchmarks sequentially (~30-40 min)"
	@echo "  make test-all-parallel        - Run all benchmarks in parallel (~10-15 min)"
	@echo ""
	@echo "Specific Agent:"
	@echo "  make test-agent-dev           - Run bmad-agent-dev benchmark"
	@echo "  make test-agent-pm            - Run bmad-agent-pm benchmark"
	@echo "  make test-agent-ux            - Run bmad-agent-ux-designer benchmark"
	@echo "  make test-agent-sre           - Run bmad-agent-sre benchmark"
	@echo ""
	@echo "Specific Workflow (BMAD-METHOD 6.11.0 layout):"
	@echo "  make test-build               - Run bmad-build benchmark (Phase 4 implementation loop)"
	@echo "  make test-sprint-planning     - Run bmad-sprint-planning benchmark (incl. readiness gate)"
	@echo "  make test-architecture        - Run bmad-architecture benchmark"

# Single agent targets (bmad-agent-architect)
test-benchmark: test-benchmark-setup test-benchmark-run test-benchmark-clean
	@echo "✅ Benchmark test cycle complete"

test-benchmark-setup:
	@scripts/setup-test-env.sh

test-benchmark-run:
	@scripts/run-benchmark-test.sh

test-benchmark-clean:
	@bash -c 'rm -rf /tmp/bmad-test-* && echo "✅ Cleaned up temp directories"'

# Multi-agent test suite
test-all: test-all-seq

test-all-seq:
	@echo "Running all benchmarks sequentially..."
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential

test-all-parallel:
	@echo "Running all benchmarks in parallel..."
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh parallel

# Specific agent targets
test-agent-dev:
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential bmad-agent-dev

test-agent-pm:
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential bmad-agent-pm

test-agent-ux:
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential bmad-agent-ux-designer

test-agent-sre:
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential bmad-agent-sre

# Workflow targets (BMAD-METHOD 6.11.0 skill layout)
test-build:
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential bmad-build

test-sprint-planning:
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential bmad-sprint-planning

test-architecture:
	@chmod +x scripts/run-all-benchmarks.sh
	@bash scripts/run-all-benchmarks.sh sequential bmad-architecture
