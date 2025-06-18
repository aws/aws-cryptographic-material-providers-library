# Property-Based Fuzzing for AWS Cryptographic Material Providers Library: Cross-Runtime Vulnerability Detection

## Background

### AWS Cryptographic Material Providers Library (MPL)

The AWS Cryptographic Material Providers Library (MPL) is a foundational component for cryptographic operations in AWS services. MPL abstracts lower-level cryptographic materials management for encryption and decryption operations, implementing cryptographic best practices to protect data keys. Its key features include:

* **Envelope Encryption**: Data is encrypted with data keys, which are in turn encrypted with wrapping keys
* **Key Management**: Integration with AWS KMS for key management
* **Provider Flexibility**: APIs for defining and using wrapping keys from various providers
* **Cross-Language Support**: Written in Dafny and compiled into multiple runtime languages including Python, Java, and .NET

MPL consists of five main customer-facing modules:
1. AwsCryptographicMaterialProviders
2. AwsCryptographyPrimitives 
3. ComAmazonawsDynamodb
4. ComAmazonawsKms
5. StandardLibrary

This design document focuses on enhancing the testing for the TestVectorsAwsCryptographicMaterialProviders module, which is responsible for validating that cryptographic implementations function correctly according to specifications.

### The UTF-8 Vulnerability Case

Recently, a vulnerability was discovered in the Go runtime implementation of MPL related to how UTF-8 characters were handled in encryption contexts. This vulnerability highlighted an edge case in our current testing approach, which relies primarily on test vectors that didn't expose this cross-runtime inconsistency.

### Technical Details of the UTF-8 Vulnerability

The vulnerability emerged when encryption contexts containing certain UTF-8 characters were processed differently across language runtimes. Specifically, in the Go implementation, some Unicode characters in encryption context keys and values were not properly normalized, leading to inconsistent behavior:

1. An encryption operation performed by the Go runtime would create ciphertext with an encryption context containing UTF-8 characters
2. When other runtimes (Python, Java, etc.) attempted to decrypt this Go-encrypted ciphertext, they would fail to properly reconstruct the encryption context
3. This led to authentication failures and decryption errors, despite the underlying encrypted data being valid

This cross-runtime incompatibility was not caught by our existing test vectors because they didn't adequately explore the range of possible character encodings in encryption contexts.

### Current Testing Limitations

Historically, we've relied on test vectors defined in Dafny code that generates JSON files to verify the correctness of cryptographic operations in the library. While these tests serve as good regression tests, they have limitations:

1. **Limited coverage**: The tests only exercise the exact scenarios defined by the test comprehension functions in Dafny.
2. **Fixed inputs**: They don't explore unexpected edge cases or boundary conditions that might occur in production.
3. **Maintenance overhead**: Adding new dimensions to the set comprehension functions requires manual intervention and careful consideration.

The cryptography community has increasingly adopted fuzz testing as a comprehensive approach to finding bugs. Fuzz testing generates many random inputs to find edge cases and validate that invariant properties hold true across all inputs.

For MPL, this kind of testing is particularly valuable because:

1. Cryptographic systems must work correctly across all possible valid inputs.
2. Subtle edge cases in encryption and decryption operations can lead to security vulnerabilities and data loss.
3. Exhaustive manual testing of all input combinations is very arduous.

For more on the complexity of selecting representative test values, see the [AWS Encryption SDK test vector documentation](https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/test-vectors/test-vector-enumeration.md#selecting-a-representative-input-value).

## Variables Being Fuzzed

Our fuzzing approach targets specific inputs to the cryptographic operations that are most likely to reveal bugs, compatibility issues, or security vulnerabilities. Below is a detailed breakdown of each variable being fuzzed:

### 1. Encryption Contexts

Encryption contexts are authenticated but not encrypted additional data associated with encrypted content. These are the primary focus of our fuzzing efforts due to the previously discovered UTF-8 vulnerability.

**Range and Variations:**
- **Dictionary Size**: 0 to 20 key-value pairs, including empty contexts
- **Key Types**:
  - Normal strings (1-20 characters)
  - Empty strings
  - Long strings (50-100 characters)
  - Special characters (`!@#$%^&*()_+-=[]{}|;':\",./<>?`)
  - Unicode characters (covering multiple Unicode categories)
  - Numeric strings
- **Value Types**: Similar variations to keys
- **Unicode Edge Cases**:
  - Zero-width characters (`\u200B`)
  - Combining marks (e.g., combining acute accent `\u0301`)
  - Line/paragraph separators (`\u2028`, `\u2029`)
  - Byte order marks (`\uFEFF`)
  - Emoji sequences including zero-width joiners
  - Normalized vs. denormalized form pairs (NFC/NFD normalization forms)

**Importance:**
- UTF-8 handling bugs were previously found in the Go runtime, causing cross-runtime incompatibilities
- JSON serialization/deserialization issues often occur with special characters
- Key length limits may vary across implementations

### 2. Plaintexts

The actual data being encrypted.

**Range and Variations:**
- **Size**: 0 bytes to 1024 bytes (empty to 1KB)
- **Content Patterns**:
  - Empty data
  - All zeros
  - Repeating patterns (e.g., "abcabc...")
  - Random bytes
  - Binary data with null bytes and control characters

### 3. Algorithm Suites

The cryptographic algorithms used for encryption operations.

**Range and Variations:**
- All algorithm suites supported by MPL
- Focus on algorithm transitions (older to newer)
- Various key lengths and modes

## Requirements

Our fuzzing system for MPL must meet the following requirements:

1. **MUST generate diverse test inputs** that cover the range of possible inputs for encryption/decryption operations, including:
   - Encryption contexts of varying sizes, character types, and Unicode properties
   - Plaintexts of different sizes and patterns (empty, small, large, repeated patterns)
   - Various algorithm suites supported by MPL

2. **MUST verify core cryptographic properties** across all generated inputs, such as:
   - Encryption followed by decryption must yield the original plaintext
   - Changes to encryption context must affect the encryption/decryption process predictably

3. **MUST integrate with CI/CD pipeline** to run tests regularly without manual intervention.

4. **MUST maintain compatibility** with existing test infrastructure and libraries.

5. **SHOULD provide clear, actionable feedback** when failures are detected.

6. **SHOULD scale** to allow for more intensive testing in local environments while keeping CI runs reasonably fast.

7. **SHOULD be extensible** to add new property tests as the library evolves.

## Success Measurements

The success of our fuzzing implementation will be measured by:

1. **Bug detection**: The system should be capable of detecting existing bugs deliberately introduced for testing.

2. **CI reliability**: The tests should run consistently in CI environments without spurious failures.

3. **Developer adoption**: The tests should be easy enough for developers to run locally for testing changes.

4. **Input diversity**: We should be able to demonstrate that the fuzzing system generates a wider variety of test cases than our previous approach.

## Out of Scope

The following aspects are considered out of scope for the initial implementation:

1. Fuzzing of third-party cryptographic libraries that MPL depends on.
2. Performance testing or benchmarking of the MPL library.
3. Testing of integrations with external services like AWS KMS.
4. Creation and addition of test vectors once vulnerabilities are discovered
5. Automated vulnerability assessment based on fuzzing results.

## Issues and Alternatives

### One-Way Doors

Before discussing the options and alternatives, let's identify the one-way door decisions that should be considered carefully:

1. **Using a specific testing framework**: Once we've committed to a specific framework for fuzzing, migrating to a different framework would require significant refactoring.

2. **Separating CI and local tests**: A decision to have separate CI-friendly tests creates a maintenance burden, as changes must be reflected in both test types.

3. **Cross-Runtime Testing Standards**: Implementing standards for handling UTF-8 and other encoding issues across runtimes will require changes in all language implementations of MPL.

### Issue 1: Test Input Generation Strategy

How should we generate test inputs for fuzzing cryptographic operations?

#### Option A: JSON-Based Manifest Generation (RECOMMENDED)
**Description:** Generate a JSON manifest with diverse test vectors that can be used by any runtime, focusing on generating a wide variety of encryption contexts, plaintexts, and algorithm suites.

**Criterion 1: Input diversity**
The JSON approach allows for generating diverse inputs across multiple dimensions, providing excellent coverage of potential edge cases.

**Criterion 2: Cross-runtime compatibility**
By using JSON as a universal format, the same test vectors can be used across all language runtimes, ensuring consistent testing across implementations.

**Criterion 3: Integration with existing infrastructure**
JSON test vectors integrate cleanly with the existing test commands and infrastructure.

#### Option B: Pure Random Generation
**Description:** Generate completely random data for all inputs in each runtime separately.

**Criterion 1: Input diversity**
Random generation provides maximum diversity, potentially finding unexpected edge cases.
However, truly random inputs often waste time testing invalid or meaningless scenarios.

**Criterion 2: Cross-runtime compatibility**
Each runtime would need its own random generation implementation, which might not be consistent across languages.

**Criterion 3: Integration with existing infrastructure**
Would require building new test execution mechanisms instead of using existing test commands.

#### Option C: Extending Existing Dafny-Generated Test Vectors
**Description:** Use existing test vector generation in Dafny and extend the set comprehension functions.

**Criterion 1: Input diversity**
Limited diversity, as the structured approach of Dafny might restrict the range of possible inputs.

**Criterion 2: Cross-runtime compatibility**
Good compatibility since Dafny generates for all runtimes, but would be limited by Dafny's expressiveness.

**Criterion 3: Integration with existing infrastructure**
Excellent integration as it would be an extension of the current approach.

**Recommendation:** We chose Option A (JSON-Based Manifest Generation) because it offers the best balance of input diversity, cross-runtime compatibility, and integration with existing infrastructure. By generating JSON manifests, we can create diverse test vectors that work with all language runtimes while leveraging existing test commands.

### Issue 2: CI Integration Strategy

How should fuzzing tests be integrated into the CI environment?

#### Option A: Run Simplified Tests in CI (RECOMMENDED)
**Description:** Run simplified tests in CI that generate and validate test vectors without requiring full cryptographic operations.

**Criterion 1: Test coverage**
Good coverage of input generation while avoiding lengthy cryptographic operations.

**Criterion 2: Build complexity**
Significantly reduced complexity, as crypto libraries don't need to be fully built.

**Criterion 3: CI execution time**
Faster execution times, limited to around 20 minutes per PR run.

**Criterion 4: Failure diagnosis**
Clearer separation between input generation issues and cryptographic implementation issues.

#### Option B: Run Full Cryptographic Tests in CI
**Description:** Run the same complete cryptographic fuzzing tests in CI as in local development.

**Criterion 1: Test coverage**
Maximum test coverage, as all tests run in both environments.

**Criterion 2: Build complexity**
High complexity, requiring building all dependencies and crypto libraries in CI.

**Criterion 3: CI execution time**
Longer execution times that would significantly slow down the PR process.

**Criterion 4: Failure diagnosis**
More complex failure diagnosis due to potential issues in both test code and cryptographic implementations.

#### Option C: Schedule Long-Running Tests
**Description:** Run simplified tests on PRs, but schedule more thorough cryptographic tests weekly.

**Criterion 1: Test coverage**
Good balance of quick feedback on PRs with thorough testing over time.

**Criterion 2: Build complexity**
Mixed complexity depending on the test type.

**Criterion 3: CI execution time**
Optimized for PR flow while still ensuring thorough testing.

**Criterion 4: Failure diagnosis**
Good separation between immediate PR feedback and deeper testing.

**Recommendation:** We recommend a hybrid approach combining Options A and C:

1. **Option A (Simplified Tests)** runs on every PR and commit:
   - Fast feedback for developers (limited to around 20 minutes)
   - Validates input generation strategies 
   - Ensures CI reliability since it avoids complex crypto build dependencies

2. **Option C (Scheduled Testing)** runs on a weekly basis:
   - More thorough testing with larger numbers of test vectors
   - Validates actual cryptographic implementation across different runtimes
   - Catches deeper bugs that the simplified tests can't detect

This hybrid strategy provides both quick CI feedback during development and thorough cryptographic validation at regular intervals.

### Issue 3: Initial Runtime Selection

Which runtime should we implement first while designing a cross-runtime compatible solution?

#### Option A: Python Implementation First (RECOMMENDED)
**Description:** Implement the fuzzing system first in Python, using a JSON manifest format that can be used by any language.

**Criterion 1: Development speed**
Python offers rapid development capabilities with excellent libraries like Hypothesis.

**Criterion 2: Cross-runtime compatibility**
By focusing on generating JSON manifests that can be consumed by any runtime, we maintain cross-runtime compatibility.

**Criterion 3: Integration with existing test infrastructure**
Python is well-integrated with our existing test infrastructure and CI system.

**Criterion 4: Future extensibility**
The approach can be easily extended to other languages or enhanced with additional test types.

#### Option B: Implement in Multiple Runtimes Simultaneously
**Description:** Develop fuzzing capabilities for multiple language runtimes in parallel.

**Criterion 1: Development speed**
Slower development as multiple implementations would need to be maintained in parallel.

**Criterion 2: Cross-runtime compatibility**
Direct testing of cross-runtime issues, but higher implementation complexity.

**Criterion 3: Integration with existing test infrastructure**
Potentially more complex integration across multiple language-specific test systems.

**Criterion 4: Future extensibility**
More complex to maintain and extend with each new feature needing multiple implementations.

#### Option C: Implement in Dafny
**Description:** Extend the existing Dafny test vector generation with fuzzing capabilities.

**Criterion 1: Development speed**
Slower development due to Dafny's more constrained programming model for test generation.

**Criterion 2: Cross-runtime compatibility**
Excellent cross-runtime compatibility as Dafny generates code for all supported languages.

**Criterion 3: Integration with existing test infrastructure**
Good integration with existing Dafny-based test generation, but limited flexibility.

**Criterion 4: Future extensibility**
More constrained by Dafny's capabilities and expressiveness.

**Recommendation:** We chose Option A (Python Implementation First) because it provides the fastest development path while maintaining cross-runtime compatibility through JSON manifests. This approach allows us to rapidly develop and iterate on the fuzzing system using Python's excellent tooling, while ensuring the test vectors can be used by any runtime through the common JSON format.

## Detailed Design

### Architecture Overview

Our implemented fuzzing system consists of four main components that work together to provide comprehensive testing across runtimes:

1. **Vector Generation**: A Python script using Hypothesis to generate diverse test vectors and create a standard JSON manifest.

2. **JSON Manifest**: The universal format (`fuzz_manifest.json`) that can be consumed by any runtime implementation, making this approach runtime-agnostic.

3. **Test Execution**: Using existing test commands to run the vectors against the actual implementations, eliminating the need to implement custom encryption/decryption logic.

4. **Failure Detection**: A simple mechanism that logs failures to `fuzz_failures.log` when they occur, making it easy to identify and reproduce issues.

This architecture leverages existing MPL test infrastructure while adding the flexibility of property-based input generation through Hypothesis.

### Architecture Diagram

```
+---------------------+          +---------------------+          +---------------------+
|                     |          |                     |          |                     |
| Vector Generation   |  ----->  |  JSON Manifest      |  ----->  |  Test Execution     |
| (Python/Hypothesis) |          |  (Universal Format) |          |  (Any Runtime)      |
|                     |          |                     |          |                     |
+---------------------+          +---------------------+          +---------------------+
                                                                           |
                                                                           v
                                                                  +---------------------+
                                                                  |                     |
                                                                  |  Failure Detection  |
                                                                  |  and Reporting      |
                                                                  |                     |
                                                                  +---------------------+
```

### Key Components

#### Vector Generation

The vector generation component uses Hypothesis to create diverse test inputs:

1. **Encryption Contexts**: Varying sizes, character types, and Unicode properties
2. **Plaintexts**: Different sizes and patterns
3. **Algorithm Suites**: Various supported algorithms

#### JSON Manifest

The JSON manifest follows a standard format compatible with existing test commands:

```json
{
  "type": "awses-decrypt-verify",
  "version": 1,
  "tests": [
    {
      "id": "vector_000001",
      "encryption_context": {"key1": "value1", "key2": "value2"},
      "plaintext": "base64EncodedPlaintext",
      "algorithm_suite": "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256"
    },
    // More test vectors...
  ]
}
```

This format ensures that the test vectors can be used by any runtime implementation, not just Python.

#### Test Execution

The test execution component uses existing test commands to run the vectors:

```bash
# Python example
python -m tox -c runtimes/python -e cli -- encrypt --manifest-path "$MANIFEST_PATH"

# Java example
gradle -p runtimes/java run --args="encrypt --manifest-path $MANIFEST_PATH"
```

#### Failure Detection

When failures occur, they are logged to a failure log file with details about the failed vector.

### CI/CD Integration

Our GitHub workflow is designed to run tests regularly:

1. **Basic Tests on PRs**: Every PR runs a small number of test vectors to ensure the system works.

2. **Weekly Extended Tests**: A scheduled job runs more extensive testing weekly.

3. **Artifacts Collection**: Test artifacts are automatically stored for analysis.

## Implementation Details

### What is Hypothesis?

Hypothesis is a Python library for property-based testing that generates random inputs to test your code. It's particularly well-suited for our needs because:

1. It has built-in strategies for generating complex data structures
2. It automatically simplifies failing examples to minimal counterexamples
3. It supports reproducible random generation through seeds
4. It can generate diverse inputs that cover a wide range of scenarios

### Generating Diverse Inputs

Our implementation uses Hypothesis strategies to generate diverse inputs:

```python
@composite
def encryption_contexts(draw, min_pairs=0, max_pairs=20):
    """Generate random encryption contexts with different characteristics."""
    num_pairs = draw(st.integers(min_value=min_pairs, max_value=max_pairs))
    
    # Define strategies for keys and values
    key_strategies = {
        "normal": st.text(min_size=1, max_size=20),
        "empty": st.just(""),
        "long": st.text(min_size=50, max_size=100),
        "special": st.text(alphabet="!@#$%^&*()_+-=[]{}|;':\",./<>?", min_size=1, max_size=20),
        "unicode": st.text(alphabet=st.characters(categories=('L',)), min_size=1, max_size=10),
        "numeric": st.text(alphabet="0123456789", min_size=1, max_size=10),
    }
    
    # Select and apply strategies to generate encryption contexts
    # ...
    
    return context
```

For our unicode-specific testing, we have dedicated strategies that focus on problematic Unicode characters and normalization issues:

```python
@composite
def unicode_encryption_contexts(draw):
    """Generate encryption contexts specifically focused on Unicode edge cases."""
    # ...
    
    # Characters known to cause normalization issues
    problematic_chars = [
        '\u2028',  # Line separator
        '\u2029',  # Paragraph separator
        '\u200B',  # Zero-width space
        '\u200D',  # Zero-width joiner
        # ...
    ]
    
    # Generate various Unicode edge cases
    # ...
    
    return context
```

### JSON Manifest Creation

The generated inputs are converted to a JSON manifest file with a standardized format that can be consumed by any runtime:

```python
def create_manifest(vectors, output_dir, filename="manifest.json"):
    """Create a manifest file from test vectors."""
    manifest = {
        "type": "awses-decrypt-verify",
        "version": 1,
        "tests": [v.to_json() for v in vectors]
    }
    
    # Write to file
    output_path = os.path.join(output_dir, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    return output_path
```

## Security Considerations

The fuzzing system is designed to improve the security of the MPL library by finding edge cases and vulnerabilities that might not be caught by existing tests. Specific security considerations include:

1. **Edge Case Detection**: The fuzzing system can find edge cases that might lead to security vulnerabilities.

2. **Cross-Runtime Compatibility**: By testing with diverse inputs, we can ensure cross-runtime compatibility, preventing issues like the UTF-8 vulnerability.

3. **Error Handling**: The tests verify that the library handles unexpected inputs gracefully without exposing sensitive information.

## Impact/Other Considerations

Implementing this fuzzing system has several impacts:

1. **Developer Workflow**: Developers can run fuzzing tests locally to validate changes before pushing code.

2. **CI Performance**: The CI pipeline includes additional tests, configured to run within reasonable time limits.

3. **Test Coverage**: The fuzzing system complements existing tests, providing broader coverage of potential inputs.

4. **Bug Detection**: The system is designed to catch subtle bugs that might not be found through manual testing.

## Future Work

While our initial implementation focuses on Python-based fuzzing that generates JSON manifests, future work could include:

1. **Extended Runtime Support**: Implement similar fuzzing capabilities in other language runtimes.

2. **Cross-Runtime Testing**: Develop automated tools for testing encryption in one runtime and decryption in another.

3. **Coverage-Guided Fuzzing**: Extend the system to use coverage information to guide the fuzzing process.

4. **Mutation-Based Fuzzing**: Add mutation-based fuzzing to find additional edge cases.

## Appendix: Timeline

The development timeline for this project is:

- **Weeks 1-2**: AWS onboarding and learning relevant cryptographic tools and materials
- **Weeks 3-9**: Project design and implementation
- **Weeks 10-11**: Project presentation preparation and presentation
- **Week 12**: Off-boarding

## Appendix: Code Examples

### Example JSON Manifest

```json
{
  "type": "awses-decrypt-verify",
  "version": 1,
  "tests": [
    {
      "id": "vector_000000",
      "encryption_context": {
        "key1": "value1",
        "key2": "value2"
      },
      "plaintext": "SGVsbG8sIHdvcmxkIQ==",
      "algorithm_suite": "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256"
    }
  ]
}
```

### Example Unicode Test Strategy

```python
@composite
def unicode_encryption_contexts(draw):
    """Generate encryption contexts specifically focused on Unicode edge cases."""
    num_pairs = draw(st.integers(min_value=1, max_value=10))
    context = {}
    
    # Unicode character categories to test
    categories = [
        ('L',),  # Letters
        ('Mn',), # Non-spacing marks
        ('Zs',), # Spaces
        ('Co',), # Private use
        ('Cf',), # Format characters
    ]
    
    # Characters known to cause normalization issues
    problematic_chars = [
        '\u2028',  # Line separator
        '\u2029',  # Paragraph separator
        '\u200B',  # Zero-width space
        '\u200D',  # Zero-width joiner
        '\u200E',  # Left-to-right mark
        '\u0000',  # Null character
        '\uFEFF',  # Byte order mark
        '\uFFFF',  # Highest BMP code point
        '\U0001F600',  # Emoji (outside BMP)
    ]
    
    for _ in range(num_pairs):
        # Decide what kind of test case to generate
        case_type = draw(st.sampled_from([
            "normal_unicode",
            "problematic_char",
            "normalized_pair",
            "combining_chars",
            "emoji_sequences"
        ]))
        
        # Generate the appropriate test case
        # ...
        
        # Ensure keys don't collide
        unique_key = f"{key}_{_}" if key in context else key
        context[unique_key] = value
        
    return context
```

### Example CI Workflow

```yaml
name: MPL Fuzz Testing

on:
  # Run on main branch changes
  push:
    branches: [ main ]
  
  # Run on PRs
  pull_request:
    branches: [ main ]
  
  # Run scheduled tests (weekly on Sunday)
  schedule:
    - cron: '0 0 * * 0'

jobs:
  basic-fuzz-test:
    name: Basic Fuzz Tests (Python Runtime)
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install hypothesis pytest
      
      - name: Generate and run tests
        run: |
          chmod +x TestVectorsAwsCryptographicMaterialProviders/runtimes/python/test/run_fuzz_tests.sh
          cd TestVectorsAwsCryptographicMaterialProviders/runtimes/python/test
          ./run_fuzz_tests.sh --runtime python --num-vectors 100 --verbose
