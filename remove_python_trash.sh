#!bin/bash
find . -name "*.pyc" -exec git rm -f "{}" \;
find . -name "*.py.bak" -exec git rm -f "{}" \;
find . -name "__pycache__" -exec rm -r "{}" \;
