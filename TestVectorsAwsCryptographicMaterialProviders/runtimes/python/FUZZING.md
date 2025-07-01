# Property-Based Fuzzing for MPL

This document provides a guide to using the property-based fuzzing system for the AWS Cryptographic Material Providers Library (MPL).

## Overview

The fuzzing system is designed to generate diverse test inputs for encryption and decryption operations, helping to detect cross-runtime compatibility issues like the UTF-8 vulnerability. It uses Hypothesis, a Python property-based testing framework, to generate a wide range of inputs.

## What Are We Fuzzing?

The system focuses on fuzzing three key components:

1. **Encryption Contexts**:
   - Dictionary sizes (0-20 key-value pairs)
   - Key types (normal strings, empty strings, long strings, special characters, Unicode, numeric)
   - Value types (similar variations)
   - Unicode edge cases (zero-width characters, combining marks, normalization forms)

2. **Plaintexts**:
   - Various sizes (empty to 1KB)
   - Different patterns (empty, random, repeating, zeros)

3. **Algorithm Suites**:
   - All supported MPL algorithm variants

## How It Works

The approach is straightforward:

1. **Generate Fuzzed Inputs**: The `generate_fuzz_vectors.py` script uses Hypothesis to generate diverse test vectors and produces a JSON manifest file.

2. **Run Encryption**: The existing test commands (`test_encrypt_vectors_*`) are used to process the generated manifest and encrypt all test vectors.

3. **Verify Decryption**: The decryption commands (`test_decrypt_encrypt_vectors_*`) verify that all encrypted data can be correctly decrypted.

## Running the Tests

The `run_fuzz_tests.sh` script automates the entire process:

```bash
# Basic usage
./run_fuzz_tests.sh --runtime python --num-vectors 1000

# With different runtime
./run_fuzz_tests.sh --runtime java --num-vectors 500
```

Available options:
- `--runtime`: The runtime to test (python, java, net, rust, go)
- `--num-vectors`: Number of test vectors to generate
- `--output-dir`: Directory to write test vectors to
- `--verbose`: Enable verbose output

## CI Integration

The fuzzing tests are integrated into CI through GitHub Actions:

- **Basic testing** runs on every PR and push to main
- **Extended testing** runs on a weekly schedule and can be manually triggered

See the workflow file at `.github/workflows/fuzz-testing.yml` for details.

## Interpreting Results

The fuzz testing produces two main artifacts:

1. `fuzz_manifest.json`: Contains all the generated test vectors
2. `fuzz_failures.log`: Created if any failures are detected

When failures are found, the log contains details about the specific test vectors that failed, making it easy to reproduce and debug the issue.

## Customizing the Fuzzing

To customize what gets fuzzed, you can modify the strategies in `generate_fuzz_vectors.py`:

- Adjust the range of dictionary sizes for encryption contexts
- Add new types of keys and values
- Include additional Unicode edge cases
- Modify plaintext generation patterns
- Add or remove algorithm suites

## Comparison with Previous Approaches

This fuzzing approach offers several advantages over static test vectors:

1. **Vastly more test cases**: Generates thousands of diverse test vectors rather than a small set of hand-crafted examples.

2. **Automation**: Automatically explores edge cases that might be missed in manual testing.

3. **Focus on problematic areas**: Special attention to Unicode edge cases that have caused issues in the past.

4. **Integration with existing tools**: Uses the standard encryption/decryption commands rather than creating separate testing paths.

5. **Reproducibility**: Failing test vectors can be easily reproduced for debugging.

## Best Practices

1. **Start small**: Begin with a small number of vectors (100-500) for quick tests.

2. **Test all runtimes**: Run tests against all supported runtimes to catch cross-runtime inconsistencies.

3. **Save failing vectors**: When failures are found, save the vectors as permanent regression tests.

4. **Periodically increase coverage**: Run larger tests (10,000+ vectors) periodically to explore more edge cases.

5. **Focus on specific areas**: When making changes to encryption context handling or adding new algorithms, customize the fuzzing to focus on those areas.

## Future Work

Planned enhancements to the fuzzing system:

1. **Cross-runtime verification**: Encrypt in one runtime, decrypt in another.

2. **Coverage-guided fuzzing**: Focus testing on less-explored code paths.

3. **Mutation-based fuzzing**: Apply mutations to known-good inputs to find edge cases.

4. **Automatic export of failures**: Add failing test vectors to the permanent test suite automatically.
