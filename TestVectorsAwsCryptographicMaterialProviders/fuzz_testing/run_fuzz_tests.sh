#!/bin/bash

# Fuzz Testing Script for AWS Cryptographic Material Providers Library
# This script runs the complete fuzz testing workflow

set -e  # Exit on any error

echo "=== AWS Cryptographic Material Providers Fuzz Testing ==="
echo "Starting fuzz testing workflow..."

# Check if we're in the right directory
if [ ! -d "fuzz_testing" ]; then
    echo "Error: fuzz_testing directory not found."
    echo "Please run this script from the TestVectorsAwsCryptographicMaterialProviders directory."
    exit 1
fi

# Check if Python and required packages are available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required but not installed."
    exit 1
fi

# Check if hypothesis is installed
if ! python3 -c "import hypothesis" &> /dev/null; then
    echo "Installing required packages..."
    pip3 install hypothesis
fi

# Step 1: Generate fuzzed test vectors
echo ""
echo "Step 1: Generating fuzzed test vectors..."
cd fuzz_testing
python3 fuzz_generator.py

# Step 2: Run the fuzz tests
echo ""
echo "Step 2: Running fuzz tests..."
python3 fuzz_runner.py

# Step 3: Show results
echo ""
echo "=== Fuzz Testing Complete ==="
echo "Check the following files for results:"
echo "  - fuzz_failures.log: Summary of any failures"
echo "  - fuzz_detailed_failures.json: Detailed failure information"
echo "  - fuzz_test.json: Generated test vectors"
echo "  - fuzz_keys.json: Keys used for testing"

# Check if there were any failures
if [ -f "fuzz_failures.log" ]; then
    if grep -q "FAILURE" fuzz_failures.log; then
        echo ""
        echo "❌ Failures detected! Check fuzz_failures.log for details."
        exit 1
    else
        echo ""
        echo "🎉 All fuzz tests passed successfully!"
    fi
fi

echo ""
echo "Fuzz testing workflow completed." 