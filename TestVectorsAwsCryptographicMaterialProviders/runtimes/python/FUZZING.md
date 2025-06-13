# Fuzz Testing for AWS Cryptographic Material Providers Library

This document describes the fuzz testing approach for the AWS Cryptographic Material Providers Library (MPL).

## Overview

Fuzz testing is an automated software testing technique that involves providing random, unexpected, or invalid data as inputs to a program. The goal is to identify potential vulnerabilities, edge cases, or bugs that might not be caught by traditional testing methods.

For the MPL library, we've implemented property-based fuzz testing using the [Hypothesis](https://hypothesis.readthedocs.io/) framework, which allows us to:

1. Generate a wide range of random inputs
2. Run tests with these inputs
3. Automatically shrink failures to minimal reproducible examples
4. Ensure consistent test coverage across different environments

## What We Test

The fuzz testing framework focuses on these key areas:

### 1. Encryption Context Handling
- Testing edge cases in key-value pairs
- Testing with empty, very long, or special character keys and values
- Validating context integrity during encryption/decryption cycles

### 2. Algorithm Suite Variations
- Testing different algorithms and their parameters
- Ensuring consistent behavior across algorithm implementations

### 3. Keyring Configurations
- Testing different keyring setups (Raw AES, Multi-keyring, KMS)
- Verifying correct materials handling under different configurations

### 4. Error Handling
- Ensuring proper error behavior under unusual inputs
- Validating that expected validation errors are raised correctly
- Testing tampered contexts and invalid inputs

## Running the Tests Locally

### Prerequisites
- Python 3.9+ installed
- MPL library and dependencies installed

### Setup
```bash
# Install dependencies
pip install pytest hypothesis boto3

# Install MPL in development mode
pip install -e path/to/AwsCryptographicMaterialProviders/runtimes/python/
pip install -e path/to/TestVectorsAwsCryptographicMaterialProviders/runtimes/python/
```

### Running Basic Tests
```bash
# Run from TestVectorsAwsCryptographicMaterialProviders/runtimes/python directory
python -m pytest -xvs test/test_fuzz_encryption.py
```

### Extended Testing
For more thorough testing with larger sample sizes:
```bash
# Set environment variable to increase test examples
export HYPOTHESIS_MAX_EXAMPLES=1000

# Run the tests with increased timeout
python -m pytest -xvs test/test_fuzz_encryption.py
```

### KMS Testing
To test with AWS KMS, you need valid AWS credentials:
```bash
# Source credentials (if using assume-ci-role.sh)
source ./assume-ci-role.sh

# Run only the KMS test
python -m pytest -xvs test/test_fuzz_encryption.py::test_kms_keyring_if_available
```

## CI Integration

This repository includes a GitHub Actions workflow that runs the fuzz tests automatically:
- On pushes to the main branch
- On pull requests targeting the main branch
- Via manual triggering with customizable duration

The workflow is defined in `.github/workflows/fuzz-testing.yml` and includes:

- Tests with multiple Python versions
- Basic and extended testing modes
- Support for KMS testing when credentials are available
- Configurable test duration for manual runs

## Extending the Tests

To add new fuzz tests:

1. Add new strategy generators for any new input types
2. Create new test functions with the `@given` decorator
3. Implement property checks that verify invariants
4. Add error classification for expected validation errors

Example of adding a new test:
```python
@given(
    new_parameter=new_parameter_strategy()
)
def test_new_feature(new_parameter):
    # Setup
    # ...
    
    # Action
    result = perform_action(new_parameter)
    
    # Assert invariants
    assert invariant_holds(result)
```

## Analyzing Results

When fuzzing finds an issue:

1. Hypothesis will automatically shrink the failing input to a minimal reproducible example
2. The test will fail with detailed output showing the exact inputs that caused the failure
3. For expected validation errors, the test framework will classify them and continue
4. For unexpected errors, the test will fail and provide detailed information

This makes it straightforward to identify and fix issues found by fuzz testing.
