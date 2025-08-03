#!/bin/bash
set -e
mkdir -p test_outputs
python app/test_cases.py | tee test_outputs/logs.txt
