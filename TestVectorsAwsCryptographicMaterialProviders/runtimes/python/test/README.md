# Fuzzing Tests for MPL

This directory contains fuzzing tests for the AWS Cryptographic Material Providers Library (MPL) designed to detect cross-runtime compatibility issues like the UTF-8 vulnerability.

## Overview

The fuzzing approach generates random test vectors using Hypothesis strategies, creates a test manifest, and then runs encryption and decryption operations to verify that the cryptographic operations work correctly with these diverse inputs.

### Key Components

- `generate_fuzz_vectors.py`: Generates random test vectors with diverse inputs for encryption contexts, plaintexts, and algorithm suites
- `run_fuzz_tests.sh`: Shell script that orchestrates the complete testing flow (generation, encryption, decryption)

### What We're Fuzzing

The system specifically focuses on fuzzing:

1. **Encryption Contexts**:
   - Dictionary sizes (empty to 20 key-value pairs)
   - Key types (normal, empty, long, special characters, Unicode, numeric)
   - Value types (normal, empty, long, binary, Unicode)
   - Unicode edge cases (zero-width characters, combining marks, normalization forms)

2. **Plaintexts**:
   - Varying sizes (empty to 1KB)
   - Different patterns (empty, random, repeating, all zeros)

3. **Algorithm Suites**:
   - All supported algorithm variants in MPL

## Running the Tests

### Prerequisites

1. Make sure you have Python 3 installed with the required dependencies:
   ```bash
   pip install hypothesis pytest tox
   ```

2. Ensure you're using the virtual environment if applicable:
   ```bash
   source fuzz-env/bin/activate  # If you're using a virtual environment
   ```

### Running from Project Root (Recommended)

The simplest way to run the tests is from the project root directory:

```bash
# Run with default settings (Python runtime, 100 vectors)
./run_fuzz_tests.sh

# Run with specific options
./run_fuzz_tests.sh --runtime python --num-vectors 1000 --verbose
```

### Alternative: Running from Test Directory

You can also run the script directly from the test directory:

```bash
cd TestVectorsAwsCryptographicMaterialProviders/runtimes/python/test
./run_fuzz_tests.sh --runtime python --num-vectors 1000
```

### Available Options

```
--runtime <runtime>     Runtime to test (python, java, net, rust, go)
--num-vectors <n>       Number of test vectors to generate (default: 1000)
--output-dir <dir>      Output directory for test vectors
--verbose               Print verbose output
--help                  Show this help message
```

### Expected Output

When the test runs successfully, you should see output like:

```
===== Running Fuzz Tests =====
Runtime: python
Number of vectors: 100
Output directory: /path/to/TestVectorsAwsCryptographicMaterialProviders/runtimes/python
===============================

Step 1: Generating fuzzed test vectors...
Generating 100 test vectors...
Successfully wrote 120 test vectors to /path/to/TestVectorsAwsCryptographicMaterialProviders/runtimes/python/fuzz_manifest.json

Step 2: Running encryption on generated vectors...
[encryption output]

Step 3: Running decryption to verify...
[decryption output]

Fuzz testing completed successfully!
120 test vectors were processed.

✅ All tests passed!
```

### Cross-Runtime Testing

To test with other runtimes:

```bash
# Test with Java
./run_fuzz_tests.sh --runtime java --num-vectors 500

# Test with .NET
./run_fuzz_tests.sh --runtime net --num-vectors 500

# Test with Rust
./run_fuzz_tests.sh --runtime rust --num-vectors 500

# Test with Go
./run_fuzz_tests.sh --runtime go --num-vectors 500
```

## CI Integration

The fuzzing tests are integrated into CI via GitHub Actions:

- **Basic Test**: On every PR and push to main, runs a small set of fuzz tests (100 vectors) with the Python runtime
- **Extended Test**: On manual trigger or weekly schedule, runs more extensive testing with configurable runtimes and vector counts

To manually trigger extended tests, use the GitHub Actions workflow dispatch with custom parameters.

## Interpreting Results

The test produces two key artifacts:

1. **fuzz_manifest.json**: Contains all the generated test vectors
2. **fuzz_failures.log**: Created only if failures are detected, contains details about failed test cases

When a failure is detected, the script will:
- Log details about the failing test vector
- Exit with a non-zero status code
- Print a summary of the failures

This approach makes it easy to identify and reproduce issues by re-running the specific failing test vector.

## Advantages Over Previous Approach

This fuzzing system offers several advantages:

1. **Simplicity**: Single-flow approach that integrates with existing test commands
2. **Direct Integration**: Uses the actual encryption/decryption commands rather than mocks
3. **Cross-Runtime Testing**: Can test any supported runtime with the same vectors
4. **CI Friendly**: Configurable for both quick PR checks and thorough scheduled testing
5. **Reproducibility**: Clear artifacts that make it easy to reproduce and debug issues

## Future Improvements

Potential enhancements to this system:

1. Automatically export any failing test vectors as permanent regression tests
2. Add coverage-guided fuzzing to focus on less-explored code paths
3. Implement cross-runtime verification (encrypt in one runtime, decrypt in another)
4. Add mutation-based fuzzing for edge cases discovery
