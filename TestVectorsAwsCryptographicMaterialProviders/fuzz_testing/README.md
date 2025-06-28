# Fuzz Testing for AWS Cryptographic Material Providers Library

This directory contains a fuzz testing system for the AWS Cryptographic Material Providers Library (MPL). The system generates diverse test vectors and runs them through the existing test infrastructure to detect vulnerabilities and edge cases.

## Overview

The fuzzing system focuses on testing encryption contexts with AWS KMS keyrings, which is where the previously discovered UTF-8 vulnerability was found. It uses Hypothesis for property-based testing to generate diverse inputs.

## Files

- `fuzz_generator.py` - Generates fuzzed test vectors using Hypothesis
- `fuzz_runner.py` - Runs the fuzzed vectors through the test infrastructure
- `run_fuzz_tests.sh` - Complete workflow script
- `README.md` - This file

## Quick Start

### Prerequisites

- Python 3.7+
- Hypothesis library (`pip install hypothesis`)
- Access to the existing test infrastructure

### Running Fuzz Tests

1. **From the TestVectorsAwsCryptographicMaterialProviders directory:**

```bash
# Run the complete workflow
./fuzz_testing/run_fuzz_tests.sh
```

2. **Or run steps individually:**

```bash
# Step 1: Generate fuzzed test vectors
cd fuzz_testing
python3 fuzz_generator.py

# Step 2: Run the tests
python3 fuzz_runner.py
```

## What Gets Fuzzed

### 1. Encryption Contexts (Primary Focus)
- **Normal strings**: ASCII characters, numbers, spaces
- **Unicode characters**: Including problematic UTF-8 sequences
- **Special characters**: Punctuation, symbols, whitespace
- **Size variations**: 0-20 key-value pairs
- **Edge cases**: Empty strings, very long strings, mixed encodings

### 2. Algorithm Suites
- Valid algorithm suites: `0014`, `0214`, `0378`, `0478`
- (Future: Invalid algorithm suites for negative testing)

### 3. AWS KMS Keyrings
- Different KMS key types: MRK, regular, encrypt-only
- Cross-region testing: us-west-2, us-east-1

## Output Files

- `fuzz_test.json` - Generated test vectors
- `fuzz_keys.json` - Keys used for testing (copied from existing keys.json)
- `fuzz_failures.log` - Summary of any failures
- `fuzz_detailed_failures.json` - Detailed failure information

## Understanding the Results

### Success Case
```
🎉 All fuzz tests passed!
```

### Failure Case
```
❌ 2 fuzz test(s) failed!
Check fuzz_failures.log for details.
```

### Example Failure Log
```
2024-01-15 10:30:15 - ERROR - FAILURE: encryption - Encryption tests failed
2024-01-15 10:30:15 - ERROR - Output: Error: Invalid UTF-8 sequence in encryption context
```

## How It Works

1. **Generation Phase**: `fuzz_generator.py` uses Hypothesis to create diverse test vectors
2. **Setup Phase**: `fuzz_runner.py` replaces the existing test files with fuzzed versions
3. **Execution Phase**: Runs the existing Makefile commands:
   - `test_generate_vectors_python` - Creates manifest from test vectors
   - `test_encrypt_vectors_python` - Tests encryption
   - `test_decrypt_encrypt_vectors_python` - Tests decryption
4. **Cleanup Phase**: Restores original test files
5. **Reporting Phase**: Logs any failures and generates reports

## Extending the System

### Adding New Fuzzing Targets

1. **Algorithm Suite Fuzzing**: Add invalid algorithm suite IDs
2. **Keyring Type Fuzzing**: Test different keyring configurations
3. **Plaintext Fuzzing**: Generate diverse plaintext content
4. **Cross-Runtime Testing**: Test encryption in one runtime, decryption in another

### Example: Adding Invalid Algorithm Suites

```python
# In fuzz_generator.py
algorithm_suites = [
    "0014", "0214", "0378", "0478",  # Valid
    "0000", "FFFF", "9999", "ABCD"   # Invalid
]
```

### Example: Adding More Keyring Types

```python
# In fuzz_generator.py
keyring_types = [
    {"type": "aws-kms", "key": "us-west-2-mrk"},
    {"type": "raw", "key": "aes-256"},
    {"type": "multi", "children": [...]}
]
```

## Troubleshooting

### Common Issues

1. **Missing Hypothesis**: `pip install hypothesis`
2. **Permission Denied**: `chmod +x fuzz_testing/*.py`
3. **Test Infrastructure Not Found**: Ensure you're in the correct directory
4. **Timeout Errors**: Increase timeout in `fuzz_runner.py`

### Debug Mode

To see more detailed output, modify the logging level in `fuzz_runner.py`:

```python
logging.basicConfig(level=logging.DEBUG)
```

## Security Considerations

- The fuzzing system only tests metadata (encryption contexts), not cryptographic keys
- All tests run in isolation with proper cleanup
- No sensitive data is exposed in logs
- Failures are logged for analysis but don't expose internal details

## Future Enhancements

1. **Coverage-Guided Fuzzing**: Use HypoFuzz for better input generation
2. **Cross-Runtime Testing**: Test encryption/decryption across different language implementations
3. **Performance Testing**: Measure performance impact of different inputs
4. **CI Integration**: Automated fuzz testing in continuous integration
5. **Mutation-Based Fuzzing**: Mutate existing test vectors to find new edge cases

## Contributing

When adding new fuzzing capabilities:

1. Follow the existing pattern in `fuzz_generator.py`
2. Add appropriate logging in `fuzz_runner.py`
3. Update this README with new features
4. Test thoroughly before committing
5. Document any new failure patterns discovered 