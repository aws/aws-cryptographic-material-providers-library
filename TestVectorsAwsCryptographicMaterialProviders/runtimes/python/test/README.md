# Fuzzing Tests for AWS Cryptographic Material Providers Library

## Overview

This directory contains property-based fuzzing tests for the AWS Cryptographic Material Providers Library. These tests use [Hypothesis](https://hypothesis.readthedocs.io/) to generate diverse inputs for testing encryption and decryption operations.

## Files

- `test_fuzz_ci.py` - Simplified tests that verify our fuzzing strategies generate valid inputs. These tests run in CI and don't require actual crypto implementations.
- `test_fuzz_encryption.py` - Full tests that verify the actual crypto functionality. These require a complete build environment and are intended to run locally.
- `fuzz_strategies.py` - Contains shared fuzzing strategies used by both test files.

## CI Testing

The CI workflow runs only the tests in `test_fuzz_ci.py`, which:
1. Generate diverse encryption contexts, plaintexts, and algorithm IDs
2. Verify these inputs have the correct structure and properties
3. Skip tests that require actual crypto implementations

This approach allows us to:
- Continuously verify that our fuzzing strategies generate valid inputs
- Demonstrate the structure of our tests without requiring complex dependencies
- Run quickly in CI environments

## Local Testing

For full testing, run `pytest -xvs test/test_fuzz_encryption.py` in a properly configured local environment. This will:
1. Generate diverse test inputs using the same strategies
2. Pass these inputs to the actual crypto functions
3. Verify that encryption and decryption operations work correctly with all input variations

## Benefits Over Static JSON Tests

This fuzzing approach has several advantages over static JSON test vectors:
1. **Coverage**: Hypothesis generates thousands of test cases, exploring far more edge cases than would be practical with hand-written tests
2. **Dynamic Adaptation**: Strategies adapt to find interesting edge cases automatically
3. **Shrinking**: When a test fails, Hypothesis automatically finds the simplest failing example
4. **Extensibility**: Easy to add new input types or adjust parameters

## Running the Tests

### CI Environment
```bash
# Run basic tests (automatically skips crypto-dependent tests)
python -m pytest -xvs test/test_fuzz_ci.py
```

### Local Development
```bash
# Run full crypto-dependent tests
python -m pytest -xvs test/test_fuzz_encryption.py
```
