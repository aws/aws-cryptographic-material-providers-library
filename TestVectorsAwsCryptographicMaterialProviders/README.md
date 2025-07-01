# Test Vectors for AWS Cryptographic Material Providers Library

The TestVectorsAwsCryptographicMaterialProviders is responsible for creating Test Vectors used to test all the combinations of features available in the AWS Cryptographic Material Providers Library.

This project is used as part of AWS Crypto Tools' CI/CD process to test functionality and compatibility across language implementations.

This project does not adhere to semantic versioning; as such it makes no guarantees that functionality will persist across major, minor, or patch versions.
**DO NOT** take a standalone dependency on this library.

[Security issue notifications](./CONTRIBUTING.md#security-issue-notifications)

## Security

If you discover a potential security issue in this project
we ask that you notify AWS/Amazon Security via our
[vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/).
Please **do not** create a public GitHub issue.

## Fuzz Testing

This project now includes property-based fuzz testing capabilities that help identify edge cases, potential vulnerabilities, and unexpected behaviors in the MPL library. The fuzz testing framework:

- Tests encryption context handling with various input types and edge cases
- Evaluates different algorithm suite combinations
- Verifies correct behavior across multiple keyring configurations
- Ensures proper error handling under unusual or malformed inputs

For more information about the fuzz testing approach, how to run the tests locally, and how to extend them, see [FUZZING.md](./runtimes/python/FUZZING.md).

The fuzz tests are automatically run as part of CI/CD via GitHub Actions to ensure continuous validation of the library's robustness.
