#!/bin/bash

# Simple wrapper script to run fuzz tests from the main project directory

echo "Running fuzz tests from the main directory..."

# Check for required tools
if ! command -v tox &> /dev/null; then
  echo "Error: tox is not installed. Please install it with 'pip install tox'."
  exit 1
fi

if ! command -v python3 &> /dev/null; then
  echo "Error: python3 is not installed. Please install Python 3."
  exit 1
fi

# Check for virtual environment
if [ -d "fuzz-env" ]; then
  echo "Found virtual environment. Activating..."
  source fuzz-env/bin/activate || {
    echo "Warning: Failed to activate virtual environment. Continuing without it..."
  }
fi

# Ensure the scripts are executable
chmod +x TestVectorsAwsCryptographicMaterialProviders/runtimes/python/test/run_fuzz_tests.sh
chmod +x TestVectorsAwsCryptographicMaterialProviders/runtimes/python/test/generate_fuzz_vectors.py

# Ensure hypothesis is installed
pip install --quiet hypothesis

# Command line args
ARGS="$@"
if [ -z "$ARGS" ]; then
  ARGS="--runtime python --num-vectors 100"
fi

# Change to the test directory and run the fuzzing script
cd TestVectorsAwsCryptographicMaterialProviders/runtimes/python/test
./run_fuzz_tests.sh $ARGS
