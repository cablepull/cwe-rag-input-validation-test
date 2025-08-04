#!/bin/bash
set -e
mkdir -p test_outputs
python app/test_cases.py | tee test_outputs/logs.txt
python app/test_multi_ingest.py | tee test_outputs/multi_ingest_logs.txt
