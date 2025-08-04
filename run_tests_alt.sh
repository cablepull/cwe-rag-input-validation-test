#!/bin/bash
set -e
mkdir -p test_outputs
PYTHONPATH=app python -m unittest test_cases_alt | tee test_outputs/logs_alt.txt
PYTHONPATH=app python -m unittest test_multi_ingest_alt | tee test_outputs/multi_ingest_alt_logs.txt
