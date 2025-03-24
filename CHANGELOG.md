# Changelog

## [1.10.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.9.0...v1.10.0) (2025-03-24)

This release is available in the following languages:

- Python

### Miscellaneous -- Python

* **deps:** extend supported version of pytz library ([#1333](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1333)) ([6f6876a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6f6876aea8be186555e6430e039f4a6c6883c5d5))

### Miscellaneous

* clarify InFlightTTLExceeded exception ([#1169](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1169)) ([d1c42a6](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d1c42a6840a7846934b6e9124b170ef710cf2aba))
* fix typos in documentation ([#1326](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1326)) ([7f59a7e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7f59a7e073f2abe9effa89f7818ceb50bea9df26))
* let fileio deal in uint8 instead of bv8 ([#1347](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1347)) ([80e28f3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/80e28f3f7816e99ed22120cca6a81628a3ae4892))

# [1.9.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.8.0...v1.9.0) (2025-02-03)

This release is available in the following languages:

- Java

### Bug Fixes

- CI ([d9e2a1e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d9e2a1e673a5a81ff030b45b6a66ead35040484f))
- DafnyLibraries.FileIO extern ([b150c48](https://github.com/aws/aws-cryptographic-material-providers-library/commit/b150c48a0570407dc0462c6e91929ff18a92897c))
- ECDH ValidatePublicKey err msg ([34a48fc](https://github.com/aws/aws-cryptographic-material-providers-library/commit/34a48fcde591a5aef53ec29a44e11885efcea8ea))
- for test vectors, use SetToSequenceSorted ([#1034](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1034)) ([21ad206](https://github.com/aws/aws-cryptographic-material-providers-library/commit/21ad206c54de90276ff4c8a23311731e66ab2a73))
- **GHW:** check-files apply to PR, not to diff b/w HEAD and branch ([#1075](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1075)) ([1f53a92](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1f53a92481e89ae7656acb5240919ed161abe74d))
- improve golang externs ([#1133](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1133)) ([b6ee16e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/b6ee16e47ae44d5af140dd5b934870f21565aa18))
- **Java:** Improve Collection of Errors string ([#1056](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1056)) ([9e195a1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/9e195a1960fa18e1dc6efd0c9057c2ec6aed8e11))
- line breaks ([21536c7](https://github.com/aws/aws-cryptographic-material-providers-library/commit/21536c79fba4c31671bf02fd0cd56dad7e2d624e))
- PR comments ([798214b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/798214b474edbecca6907054d3635f6f9903f6d6))
- PR comments ([a21c0b3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/a21c0b38b7ac184697b98524e9fe93ac974c9a3a))
- PR comments ([7dd95bc](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7dd95bc8656f51d70529253691036ee10cc6b53a))
- PR comments ([eed0d87](https://github.com/aws/aws-cryptographic-material-providers-library/commit/eed0d87ec161af904f57f229436bd731f465795d))
- PR comments ([435515e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/435515eba9fbd3e457520aebfc1a26a968ab7a57))
- re-enable aes_gcm_192 ([#1143](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1143)) ([23650a9](https://github.com/aws/aws-cryptographic-material-providers-library/commit/23650a9c6e1c897455e2d59d15b7d7a2c5a07cdd))
- region ([5930ae4](https://github.com/aws/aws-cryptographic-material-providers-library/commit/5930ae44e17014e660132298ffd37528b711e3be))
- region ([e3454b5](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e3454b5a7fbf3c462ed56507133521a362ff89b1))
- remove [@sensitive](https://github.com/sensitive) from smithy models ([#1123](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1123)) ([c939f3a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c939f3a6608aea60d1d3c2d6aa64ceef969457c2))
- repo rename ([#1218](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1218)) ([c2f003c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c2f003cb679b9282981b539bbe50102e0952cb97))
- revert pyproject.toml drop ([b5dbb5c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/b5dbb5c83d0cc1c13676694c721dc160087e2ba9))
- rust code used for testing must be allowed dead code ([#1148](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1148)) ([5997919](https://github.com/aws/aws-cryptographic-material-providers-library/commit/59979192a51ef5b1864ac36d57925d55eb562fa2))
- SetToSequence should be a method, not a function ([#1035](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1035)) ([1169bc8](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1169bc8ef34ebfe3937ea3be8acf7a187ef1517a))
- smithy-dafny ([#1136](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1136)) ([6005777](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6005777e8157a1273a4293ac3b1c135d25140a47))

### Features

- Adds CI ([511ed35](https://github.com/aws/aws-cryptographic-material-providers-library/commit/511ed358751c846fca46e111001841f7dd7f3bf6))
- check in polymorph go generated code ([#1137](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1137)) ([d0fefbf](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d0fefbf2a6a363a7aa6940ce7a45eb8e395654f0))
- Check-in polymorph generated code ([bfc7cb9](https://github.com/aws/aws-cryptographic-material-providers-library/commit/bfc7cb9f5645544d956a1c500a686c133196eb02))
- ddb Go externs ([1e3737b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1e3737b2f6294e9399f19ac9fd7377f8b0e526f7))
- **ddb:** Go release v0.0.1 ([#1201](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1201)) ([5293bfd](https://github.com/aws/aws-cryptographic-material-providers-library/commit/5293bfd755952b243a57c9cb7e6718d807e09d9a))
- **ddb:** Go release v0.0.3 ([#1210](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1210)) ([983f553](https://github.com/aws/aws-cryptographic-material-providers-library/commit/983f553337954a97db43e2c8cfb8bfa3378db345))
- **Go:** Go module rename ([#1196](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1196)) ([b0876ac](https://github.com/aws/aws-cryptographic-material-providers-library/commit/b0876ace8d4882dbee77887712469f799015e9dc))
- kms externs for Go ([2d1f6d1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/2d1f6d1da826433c566c4ce4d5ff53d7f7ab1bdc))
- **kms:** Go release v0.0.1 ([#1199](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1199)) ([9c80544](https://github.com/aws/aws-cryptographic-material-providers-library/commit/9c80544bbfeac5547915aa93795f9b79eac7db6b))
- mpl externs ([#1105](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1105)) ([29bc52e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/29bc52eccca8dcb5cbce8c90563b8461b9ba0454))
- **mpl:** Go release v0.0.1 ([#1211](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1211)) ([4508ab8](https://github.com/aws/aws-cryptographic-material-providers-library/commit/4508ab84bd6017e7db6f353d2195b93ac30761c9))
- Primitives CI ([ce6e942](https://github.com/aws/aws-cryptographic-material-providers-library/commit/ce6e9421a0632beae2fe554f258d0243ec4b99c3))
- Primitives for Go ([8066826](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8066826b3b17b2355af4d8bf94dab54325932ae6))
- **primitives:** Go release v0.0.1 ([#1203](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1203)) ([6bf0bbe](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6bf0bbe25650da820c4133e1d1b1bce813d33a9e))
- StandardLibrary for Go ([587b57e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/587b57ee5ec341c9961e0d1689dfb26b1a271055))
- StandardLibrary for Go ([94b4fd0](https://github.com/aws/aws-cryptographic-material-providers-library/commit/94b4fd0e9f8a491103c5b9ca0b0c8ab892dd580e))
- StandardLibrary for Go ([6ce1ce3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6ce1ce32f65955fea922eb9237ee813fa5536eb8))
- **StdLib:** Go v0.0.1 release ([#1195](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1195)) ([95e54bf](https://github.com/aws/aws-cryptographic-material-providers-library/commit/95e54bf5ab4a5881f04f11a00aae074c7810add3))

# [1.8.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.7.4...v1.8.0) (2024-11-19)

This release is available in the following languages:

- Java

### Bug Fixes

- Drop SelectOpt from MutableMap ([bdb6509](https://github.com/aws/aws-cryptographic-material-providers-library/commit/bdb65098881245dfed0f2251bd654313e31b1b89))
- Externs ([0bc1f96](https://github.com/aws/aws-cryptographic-material-providers-library/commit/0bc1f961462dd9e3821fea438e3067d543adab9c))
- formatting ([b608ab8](https://github.com/aws/aws-cryptographic-material-providers-library/commit/b608ab88e155bdb23e21f8b3f0f75116b58b182d))
- **Python-Release:** Run validate tests from release commit ([41c0c94](https://github.com/aws/aws-cryptographic-material-providers-library/commit/41c0c94aac165addcef6e75bc7bad5c1dffa16ac))
- **Python:** CMCs release lock for unhandled runtime exceptions ([#979](https://github.com/aws/aws-cryptographic-material-providers-library/issues/979)) ([1510b77](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1510b772550646b6e1f26df5b0e6e96b3e48a6e3))
- **Python:** return error on interrupted sleep ([#1003](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1003)) ([405cf37](https://github.com/aws/aws-cryptographic-material-providers-library/commit/405cf37a20ffe8c36f49eccc95a7482ee97d3f7b))
- remove input and output traits on DynamoDB operations ([#1012](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1012)) ([8377acf](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8377acfbd505236ca9bb58f21f95cfc5122d1cf9))
- return error on interrupted sleep ([#993](https://github.com/aws/aws-cryptographic-material-providers-library/issues/993)) ([f49460a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f49460a569ea03778db3d1856a54b7d9b53fb9e6))
- rust CI ([42e39cc](https://github.com/aws/aws-cryptographic-material-providers-library/commit/42e39cc8e64b18387b738746457924bcf5dd47e9))

### Features

- **Rust:** Interop test vectors; bump Dafny to 4.9.0 ([#1004](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1004)) ([a505a30](https://github.com/aws/aws-cryptographic-material-providers-library/commit/a505a304f7cf7ed2490498af85c703dc85faf7ab))
- Storm cache supports millisecond resolution ([#1011](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1011)) ([6f09d5d](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6f09d5d23ecd76658e6d90b23e15ce5daade5bd2))

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
