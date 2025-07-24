# Changelog

## [1.7.6](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.7.5...v1.7.6) (2025-07-23)


### Bug Fixes

* **dotnet:** resolve AWS SDK Dependency to less than v4 ([#1629](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1629)) ([60e46cd](https://github.com/aws/aws-cryptographic-material-providers-library/commit/60e46cde52b17c803b406324a1bc1cd1335c2b6b))

## [1.7.5](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.7.4...v1.7.5) (2025-01-30)

This release is available in the following languages:

- .NET

### Fixes

- **.NET:** CollectionOfErrors; list as string ([#1247](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1247)) ([6126ddb](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6126ddb8b9792524ab0fd4d86cbc8258bc6289e6))

### Maintenance

- **CI:** Allow local testing ([#961](https://github.com/aws/aws-cryptographic-material-providers-library/issues/961)) ([898cb43](https://github.com/aws/aws-cryptographic-material-providers-library/commit/898cb4360144ebc73a7abca295f216dd672b9133))

# [1.7.4](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.7.3...v1.7.4) (2024-11-06)

This release is available in the following languages:

- Python

### Bug Fixes

- **Python:** Support Python 3.13 ([#953](https://github.com/aws/aws-cryptographic-material-providers-library/issues/953)) ([000baed](https://github.com/aws/aws-cryptographic-material-providers-library/commit/000baedfab341670952449837541c88ea5cf1dba))

## [1.7.3](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.7.2...v1.7.3) (2024-10-31)

This release is available in the following languages:

- Python

### Bug Fixes

- python time externs should return integers ([#898](https://github.com/aws/aws-cryptographic-material-providers-library/issues/898)) ([56b9b67](https://github.com/aws/aws-cryptographic-material-providers-library/commit/56b9b6745eee5782bcec3f3e51f5b27a5ffe223e))

## [1.7.2](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.7.1...v1.7.2) (2024-10-22)

This release is available in the following languages:

- Python

### Bug Fixes

- Move Java helper methods out of extern class ([#855](https://github.com/aws/aws-cryptographic-material-providers-library/issues/855)) ([61fddf8](https://github.com/aws/aws-cryptographic-material-providers-library/commit/61fddf8359749e9fd7f5c3151cfaf1c6c0bca747))
- Smithy-Dafny update for separated classes and unions ([#806](https://github.com/aws/aws-cryptographic-material-providers-library/issues/806)) ([4b7cc5f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/4b7cc5f368e6a878d5e003484e88a33a0f2bb6d3))
- variable name collision fix for Go ([ceaec06](https://github.com/aws/aws-cryptographic-material-providers-library/commit/ceaec06cd4a670659e8329d879558081a2401e2d))

# [1.7.1](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.7.0...v1.7.1) (2024-10-11)

This release is available in the following languages:

- Python

This is the first release for the Python implementation of the AWS Cryptographic Material Providers Library. ([#805](https://github.com/aws/aws-cryptographic-material-providers-library/issues/805)) ([cfb2f7e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cfb2f7e06c406b3f3ddb506a6356382737b53746))

### Bug Fixes

- **H-Keyring:** if getCache returns Error not EntryDoesNotExist, raise error ([#846](https://github.com/aws/aws-cryptographic-material-providers-library/issues/846)) ([3413fcb](https://github.com/aws/aws-cryptographic-material-providers-library/commit/3413fcbc889e2c31fb753ff3eca852c1d5db1140))
- **H-Keyring:** if putCache throws EntryAlreadyExists, swallow ([#856](https://github.com/aws/aws-cryptographic-material-providers-library/issues/856)) ([d01a182
  ](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d01a182b5e62010f44616dacd6730aa873dec4c7))

# [1.7.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.6.0...v1.7.0) (2024-09-23)

### Features

- **HierarchyKeyring; CMC:** Shared cache across Hierarchy Keyrings ([#747](https://github.com/aws/aws-cryptographic-material-providers-library/issues/747)) ([d4709e9](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d4709e91fe05180ea13712cf657373515493a3f1))

# [1.6.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.5.1...v1.6.0) (2024-09-10)

### Bug Fixes

- add ECDH error message for Rust ([#574](https://github.com/aws/aws-cryptographic-material-providers-library/issues/574)) ([473a34a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/473a34abe688629e1a5b8abe8bc859e1128ea40b))
- **DDB-Model:** DDB Supports 100 actions per Transaction ([#692](https://github.com/aws/aws-cryptographic-material-providers-library/issues/692)) ([8a67843](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8a6784372ff635828aa15b9edd7a1c7a37a95286))
- GetCurrentTimeStamp returns ISO8601 format ([#575](https://github.com/aws/aws-cryptographic-material-providers-library/issues/575)) ([c07a51f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c07a51fc29ff70411f7573bca96d2a091db8c1ed))
- maintain order in test vectors for languages with parallel tests ([#641](https://github.com/aws/aws-cryptographic-material-providers-library/issues/641)) ([8c8a38f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8c8a38ff3534b8e4f0dca020e65effc454ef330a))
- Remove 4.4 DDB and KMS patches, abstract test to work on later Dafny versions ([#611](https://github.com/aws/aws-cryptographic-material-providers-library/issues/611)) ([d51d648](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d51d6482e3d8ca668111a4695d1adc0c67c3f0a3))
- Remove uses of `:|` ([#618](https://github.com/aws/aws-cryptographic-material-providers-library/issues/618)) ([f12fe5b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f12fe5b4a96a9873eb1b73cee8ae74737f3d2375))
- test vector help text ([#657](https://github.com/aws/aws-cryptographic-material-providers-library/issues/657)) ([0fedaf1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/0fedaf1466d1e0915faa6b6a533b88a40fb0ee91))
- **post-release:** Change back to 1.5.1-SNAPSHOT ([09cd9a4](https://github.com/aws/aws-cryptographic-material-providers-library/commit/09cd9a432aeeb7e88da5932f335cd82f95d264b3))

### Features

- bump dafny verification and code gen to dafny 4.8.0 ([#520](https://github.com/aws/aws-cryptographic-material-providers-library/issues/520)) ([e16539e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e16539e98d4b0f60098693fdbaec12dc49c34c9b))

## [1.5.1](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.5.0...v1.5.1) (2024-07-08)

### Fixes

- **SDK-Java:** Generic SDK Error to Opaque & Back ([#466](https://github.com/aws/aws-cryptographic-material-providers-library/issues/466)) ([f832ad1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f832ad106cea3a86c536197dae15a335b4676d42))

# [1.5.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.4.0...v1.5.0) (2024-06-17)

### Features

- **MPL:** Add Raw ECDH and AWS KMS ECDH Keyrings ([#419](https://github.com/aws/aws-cryptographic-material-providers-library/issues/419)) ([0946a7e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/0946a7ed801a6269565651cfe2ef17831d89d99c))

# [1.4.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.3.0...v1.4.0) (2024-05-20)

### Features

- **Keystore:** Introduce additional KMSConfiguration options ([#316](https://github.com/aws/aws-cryptographic-material-providers-library/issues/316)) ([f3a0a52](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f3a0a5269e611afd254425226d32eaaed1f3d99b))

The Hierarchical Keyring's Keystore now supports four (4) `KMSConfigurations`:

- kmsKeyArn
- kmsMRKeyArn
- discovery
- mrDiscovery

See our [JavaDocs](https://aws.github.io/aws-cryptographic-material-providers-library/index.html?software/amazon/cryptography/keystore/model/KMSConfiguration.html) for details
on how these options effect the relationship between
a Keystore and KMS.

### Maintenance

- .NET : Bump dependency [BouncyCastle.Cryptography](https://github.com/bcgit/bc-csharp) from 2.2.1 to 2.3.1. ([#329](https://github.com/aws/aws-cryptographic-material-providers-library/pull/329))
- .NET : Bump dependency [AWSSDK.Core](https://github.com/aws/aws-sdk-net) from 3.7.300.2 to 3.7.304.2. ([#329](https://github.com/aws/aws-cryptographic-material-providers-library/pull/329))
- Java : Move InternalResult into StandardLibrary(Internal) ([#325](https://github.com/aws/aws-cryptographic-material-providers-library/pull/325))

# [1.3.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.2.0...v1.3.0) (2024-04-24)

### Bug Fixes

- **dafny:** Local Service Constructors MUST return concrete ([64f72c1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/64f72c121fef31a83bcf3a5346d7efc1e84ab25f))
- Improvements to the Java Release process ([#162](https://github.com/aws/aws-cryptographic-material-providers-library/issues/162)) ([d92c06a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d92c06a2fd355290f27df669c866157e14da9793))
- Increase try-block scope when calling MPL components ([#267](https://github.com/aws/aws-cryptographic-material-providers-library/issues/267)) ([7661bf4](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7661bf4b0f23e810f825fd884ecdc036b5e472d5))

### Features

- Multi-Region Key Logic in the Keystore ([#285](https://github.com/aws/aws-cryptographic-material-providers-library/issues/285)) ([d924395](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d924395e7895187aee59279f7ba1f4dcdf1f893e))
- .NET : Enforce User input Constraints at Type Conversion ([#281](https://github.com/aws/aws-cryptographic-material-providers-library/issues/281)) ([04102d7](https://github.com/aws/aws-cryptographic-material-providers-library/commit/04102d7e30c04167df9fb76de86d2aeb0508536e))
- Update error message to include expected values when no Encrypted Data Keys found to match ([#275](https://github.com/aws/aws-cryptographic-material-providers-library/issues/275)) ([da95f9a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/da95f9a66f863016f8172df9aa19d1086b9bdd78))

## 1.2.0 (2024-01-08)

### Features

    * add command line parser (#131)

### Bug Fixes

    * resolve awssdk:core dependency in TestVectors build.gradle.kts (#177)
    * add more tests to ComputeSetToOrderedSequence (#111)
    * Empty string defers to SDK default region (#127)
    * update mpl .csproj to use project references (#134)
    * newest polymorph for newest shims. Catch all exceptions. DDB only (#135)
    * update README for repo rename update (#147)
    * rerun latest polymorph. (#128)
    * typo lead to two verification, no format (#130)
    * Improve compatibility with Dafny 4.4 (#129)

### Maintenance

    * A variety of fixes to the libraries CI and testing

## 1.0.2 (2023-10-18)

### Bug Fixes

    * CmpError must return custom error message (#118) (86abacc)
    * Deafult entryPruningTailSize (#93) (0344e9f)
    * Fix brittle concurrent test (#105) (#60) (c043162)
    * fix typo in encryption materials validation (cd6b0aa), closes #84
    * fix typo in encryption materials validation (89a234c)
    * Forward the underlying error (#90) (bc21551)

## 1.0.1 2023-07-26

### Fix

- Fixes a runtime check in `VersionKey` Key Store API that no longer checks for the CipherText length
  on the output of a KMS ReEncrypt API call.

## 1.0.0 2023-07-21

### Features

- Introduces Thread Safe Cryptographic Materials Caches (CMCs):
  - Storm Tracking Cache  
    Safe for use in a multi threaded environment,  
    tries to prevent redundant or overly parallel backend calls.  
    See [Spec changes](https://github.com/awslabs/aws-encryption-sdk-specification/blob/ce9a4062124edc5085c66a4f10742e15aa039b34/changes/2023-06-19_thread_safe_cache/change.md) for details.
  - Multi Threaded Cache  
    Safe for use in a multi threaded environment,  
    but no extra functionality

### BREAKING CHANGES

- CMCs:
  - Original Cryptographic Materials Cache has been renamed to Single Threaded Cache
  - `CreateCryptographicMaterialsCacheInput` now ONLY accepts `CacheType`,  
    which determines which, if any, of the three implemented CMCs will be returned.
  - The `DefaultCache` is `StormTrackingCache`
- `CreateAwsKmsHierarchicalKeyringInput`:
  - no longer has a `maxCacheSize` field
  - now has an optional `cache` field for a `CacheType`
- Hierarchical Keyring's Key Store:
  - The Hierarchical Keyring's Key Store's Data Structure has changed.  
    As such, entries persisted in the Key Store with prior versions of this library are NOT compatibale.  
    Instead, we recommend Creating a new DynamoDB Table for this version of the Key Store.
  - The Key Store's `CreateKeyInput` now takes:
    - An Optional `String branchKeyIdentifier`
    - An Optional `EncryptionContext encryptionContext`
      - This `encryptionContext` will be added to the Encryption Context sent to KMS prefixed with `aws-crypto-ec:`
  - Creating a Key now also calls KMS:ReEncrypt
  - `CreateKeyStore` no longer creates a GSI
  - The Encryption Context used with KMS' `GenerateDataKeyWithoutPlaintext` no longer include's the discarded GSI's `status`.
  - More details about the Key Store's changes are avaible in our Specification:
    - [2023-07-12 Update Key Store](https://github.com/awslabs/aws-encryption-sdk-specification/tree/master/changes/2023_7_12_update-keystore-structure)
    - [KeyStore Specification](https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/branch-key-store.md)

### Maintenance

- A variety of fixes to the libraries CI and testing

### Fix

- Fixes Required Encryption Context CMM and UpdateUsageMetadata names in smithy model

## 1.0.0-preview-3 2023-06-22

### Fix

- Fixes PutCacheEntry
  - PutCacheEntry will now update an entry.
    This simplifies using the cache in concurrent situations.
    Rather than having the caller implement some retry logic
    the cache will now update the entry.
- Fixes pom.xml to include runtime version of BouncyCastle and removes bundling of BC in the jar.

## 1.0.0-preview-2 2023-06-19

### Fix

- Fixes build file to correctly generate pom file with correct dependencies during release.

## 1.0.0-preview-1 2023-06-07

### Features

- Initial release of the AWS Cryptographic Material Providers Library.
  This release is considered a [developer preview](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle)
  and is not intended for production use cases.
