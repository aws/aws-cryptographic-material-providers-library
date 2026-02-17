# Changelog

## [1.11.2](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.11.1...v1.11.2) (2026-02-02)

This release is available in the following languages:

- DotNet
- Python

### NOTE

This Library is **NOT** impacted by CVE-2026-26007.

### Fixes -- DotNet

- **dotnet:** build from main ([#1781](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1781)) ([b2d6075](https://github.com/aws/aws-cryptographic-material-providers-library/commit/b2d6075ff4e009df32e22da05d79c52216607572))

### Maintenance -- All Languages

- **dafny:** add fuzz testing to MPL ([#1622](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1622)) ([14fad38](https://github.com/aws/aws-cryptographic-material-providers-library/commit/14fad380f4350b3b32e478feb5fab03dabd7b14b))
- **dafny:** add new SearchAndReplaceWhole and friends ([#1680](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1680)) ([74e98c1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/74e98c10184c27bc57ba5b77386872466213f91f))
- **dafny:** optimize mutation map for O(1) performance in Go ([#1687](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1687)) ([68cd7cb](https://github.com/aws/aws-cryptographic-material-providers-library/commit/68cd7cb768ab2ffc85052959e46122af1e1c1dcf))

### Maintenance -- Python

- **python:** add user agent suffix to kms requests ([#1686](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1686)) ([b69aaf2](https://github.com/aws/aws-cryptographic-material-providers-library/commit/b69aaf25d5f63ce833a07b852f4a0df3a82c477b))
- **python:** exclude generated tests from project distribution ([#1627](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1627)) ([505eee0](https://github.com/aws/aws-cryptographic-material-providers-library/commit/505eee0072d6390e23d855fa303dde9eeb031706))
- **python:** tests for OpaqueWithText ([#1656](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1656)) ([25e1219](https://github.com/aws/aws-cryptographic-material-providers-library/commit/25e121974106cab8386058be29a1072cb50bb193))
- **python**: bump cryptography upperbound to <47 due to CVE-2026-26007 ([#1800](https://github.com/aws/aws-cryptographic-material-providers-library/pull/1800))

### Maintenance -- Go

- **go:** put back content() in mutable maps extern ([#1694](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1694)) ([bb0ec0c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/bb0ec0cb959e6982cf2c154458c39865db083e84))
- **go:** Release dynamodb Go module 0.2.1 ([#1671](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1671)) ([c82e136](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c82e136380e00a3a300f24df805d5a66d4a52a4e))
- **go:** Release dynamodb Go module 0.2.2 ([#1698](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1698)) ([76846e1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/76846e16598492f5bff36d811b7edf064d949b13))
- **go:** Release kms Go module 0.2.1 ([#1667](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1667)) ([dd8cdf1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/dd8cdf15dce8d918478cdeb8c81431318ef6eafd))
- **go:** Release kms Go module 0.2.2 ([#1697](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1697)) ([79c0531](https://github.com/aws/aws-cryptographic-material-providers-library/commit/79c053174e8da98f2d0fdd527c1817cf43c394c8))
- **go:** Release kms Go module 0.3.0 ([#1746](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1746)) ([1e438f3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1e438f320ebfe0c0ac8a29ccb123b0360a66c272))
- **go:** Release mpl Go module 0.2.1 ([#1672](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1672)) ([9bc43c0](https://github.com/aws/aws-cryptographic-material-providers-library/commit/9bc43c059fa820c298d8269b8fa316704c39703e))
- **go:** Release mpl Go module 0.2.2 ([#1704](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1704)) ([5f2aa33](https://github.com/aws/aws-cryptographic-material-providers-library/commit/5f2aa3338e6577d23b73c5fa9b699bf22ece1315))
- **go:** Release mpl Go module 0.3.0 ([#1751](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1751)) ([1ac31b6](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1ac31b6ed320cff83cb9374230d4613651423e2a))
- **go:** Release primitives Go module 0.2.1 ([#1669](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1669)) ([dca265f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/dca265fbb3ad8818f53fe66af91bde496fe7c29b))
- **go:** Release primitives Go module 0.2.2 ([#1699](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1699)) ([d4c3a20](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d4c3a20ec8561b1159964221c51906cab2b9a821))
- **go:** Release primitives Go module 0.3.0 ([#1748](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1748)) ([541e04a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/541e04afc3fcaa11828e83312ba40f4dbef0b8d8))
- **go:** Release smithy-dafny-standard-library Go module 0.2.1 ([#1666](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1666)) ([fa3f98b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/fa3f98b84cdd56be61d348c72d1b8701a17109a8))
- **go:** Release smithy-dafny-standard-library Go module 0.2.2 ([#1696](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1696)) ([4312195](https://github.com/aws/aws-cryptographic-material-providers-library/commit/4312195d21f0d13719a4b869ebd1e8335dd136ba))
- **go:** remove create pull request step in go release workflow ([#1681](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1681)) ([7eafe88](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7eafe8890ef7626adc04c591a3359c80d7097d47))
- **go:** test with go 1.23 ([#1737](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1737)) ([987ac0f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/987ac0fdc9b1177b43c761b810fdfb0e9f33afe8))

### Maintenance -- Rust

- **rust:** bump dafny version for rust to 4.10 ([#1725](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1725)) ([f41b3c4](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f41b3c45c786a119952f0b35b311dbfad5fd3aa6))
- **rust:** clean up kms module ([#1752](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1752)) ([6878377](https://github.com/aws/aws-cryptographic-material-providers-library/commit/687837704534fccf7764767b7057a7b83a3f1a17))
- **rust:** fix clippy warning. Bump test dependencies ([#1715](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1715)) ([7b8d6ac](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7b8d6ac580a3b386e764cf975c063f3e3a2722c2))
- **rust:** more compatible blocking ([#1780](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1780)) ([3ea1161](https://github.com/aws/aws-cryptographic-material-providers-library/commit/3ea116182a442607720330c102f086ebf3c6975f))
- **rust:** note unused parameter ([#1693](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1693)) ([49759c9](https://github.com/aws/aws-cryptographic-material-providers-library/commit/49759c9f320895a2dfc4c8b06092a5871c73dd7a))
- **rust:** prepare for initial Rust crate publication ([#1755](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1755)) ([1e28a61](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1e28a61361edf51ba45b50bca91672f85c679862))
- **rust:** provide fips feature flag ([#1703](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1703)) ([f6bdd23](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f6bdd23d4ef83e3513554abb41d0ddbd3d89e8b8))
- **rust:** release 0.2.0 ([#1782](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1782)) ([03c999c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/03c999c72426158b06988cc31155454808d6baa1))
- **rust:** remove warnings ([#1724](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1724)) ([453359a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/453359a4e0390904152854ffa39db460e63a36dd))

### Miscellaneous

- Add UserAgent string to KMS client ([#1716](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1716)) ([09b2cda](https://github.com/aws/aws-cryptographic-material-providers-library/commit/09b2cdab5bd2e711e5487db747ff3380a393c48a))
- **deps:** update deps across the repo ([#1773](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1773)) ([edcc64c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/edcc64c96760e23e948afa7d23f796045e3546d8))
- update check-files ([#1785](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1785)) ([14af920](https://github.com/aws/aws-cryptographic-material-providers-library/commit/14af9201be58aa20760e3e1c453de28418865100))
- update kms externs correctly ([#1717](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1717)) ([e11ba53](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e11ba531f3f12610ded9df7acb49b41f908b7b22))

## [1.11.1](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.11.0...v1.11.1) (2025-07-29)

This release is available in the following languages:

- Python

### Maintenance -- All Languages

- **dafny:** add Rust and Go to supported languages ([#1492](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1492)) ([87ab402](https://github.com/aws/aws-cryptographic-material-providers-library/commit/87ab40233096739f2aa709fdcd948ce7452c7d04))
- **dafny:** append our user agent in KMS client ([#1564](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1564)) ([03d03ac](https://github.com/aws/aws-cryptographic-material-providers-library/commit/03d03ac1f3591885bcc583efb988602ed129c3c5))
- **dafny:** remove negative test for codebuild runner ([#1603](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1603)) ([8b45e40](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8b45e40e9fa081e277837946e53836b308429ee8))

### Maintenance -- Python

- **python:** Updated pytz version range to include 2025 releases ([#1603](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1641)) ([1aced27](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1aced27699de7aebcb6d4513a9e72c604c7ce855))

### Maintenance -- Go

- **go:** automate changelog for Go release ([#1607](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1607)) ([f9eb8e0](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f9eb8e0169139946ca46a7a4f0e30abdff7f976e))
- **go:** update go test matrix and clean up setup ([#1625](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1625)) ([6baa15c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6baa15ca499603dc4fe5501542d6f45b80d2c244))

### Maintenance -- Rust

- **rust:** update for new version of clippy ([#1606](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1606)) ([ec013f6](https://github.com/aws/aws-cryptographic-material-providers-library/commit/ec013f6ba85d62ab41db48fec92baca85625e4b9))

### Miscellaneous

- 5 instead of 25 interop decrypt processes ([#1620](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1620)) ([d82696b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d82696b520681eaabd8f9a6c76bd9a208de4d6ac))
- allow local testing for python ([#1598](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1598)) ([cbfa209](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cbfa209c0b9453fe633a3047e3dcd5db0e7fa728))
- bump credentials to 2 hours, for python ([#1621](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1621)) ([69991da](https://github.com/aws/aws-cryptographic-material-providers-library/commit/69991da9a26e4422dfdeb8fc95a87a46b0bb3ccc))
- **cfn:** add trusted policy for optools mpl-python roles ([#1602](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1602)) ([436d939](https://github.com/aws/aws-cryptographic-material-providers-library/commit/436d93951038e4107b36bf1f4cb3a0a5fb870577))
- **CI:** fix daily CI and add slack notification to it ([#1647](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1647)) ([c546646](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c546646a719b54f880a8aeccc6a6489fcf332070))
- **CI:** send slack message on new GHI ([#1632](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1632)) ([e80b7ae](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e80b7aeaf691e956b6177aa24633681dcfe7a7ba))
- **CI:** Test Rust on Dafny prerelease in nightly build ([#1623](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1623)) ([92070bc](https://github.com/aws/aws-cryptographic-material-providers-library/commit/92070bc128da94a24cfb84cc1fdd50f8ce5623f7))
- **CI:** update to not trigger workflow on PR comments ([#1640](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1640)) ([c62e8cf](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c62e8cf0bf6b3efa0ae479a57b08ca91ef0306b6))
- **deps:** bump slackapi/slack-github-action from 2.1.0 to 2.1.1 in /.github/workflows ([#1638](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1638)) ([40b643f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/40b643f9b95e325131a99c7ac5227d0851927980))
- **Go:** Add Go release script and workflow to run it ([#1562](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1562)) ([1c563bd](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1c563bdf8985f4c79b376929faa61496964dc69c))

## [1.11.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.10.1...v1.11.0) (2025-06-17)

This release is available in the following languages:

- Java
- Python

### Fixes -- All Languages

- **dafny:** bump Dafny libraries for JSON fix ([#1517](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1517)) ([d8679e5](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d8679e517ae3bc3b074325f849b5cb6c252c8f18))

### Maintenance -- All Languages

- **dafny:** BK fix to extract encryption context for branch key materials ([#1523](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1523)) ([95856ac](https://github.com/aws/aws-cryptographic-material-providers-library/commit/95856acd01ad26460a09eb171f2793a3109bfdbd))
- **dafny:** don't recalculate RSA key on every decrypt ([#1448](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1448)) ([f318912](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f318912eb419140c8e1cb4694b9bf69c3e239967))
- **dafny:** Make HasSubString generic ([#1549](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1549)) ([6a1017f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6a1017f5f87f39bb8eace9e92704bb2b64b16e65))
- **dafny:** more using uint64 instead of nat ([#1490](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1490)) ([571e3c5](https://github.com/aws/aws-cryptographic-material-providers-library/commit/571e3c564f1989e3c3df1fd765f4939326bc0893))
- **dafny:** store privateKey in RawRSAKeyring because some Java code needs it ([#1450](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1450)) ([1c29322](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1c293223efb2bc9643a45e482daf37a87eeae197))
- **dafny:** support for memory size constraints ([#1481](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1481)) ([8d2c2b5](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8d2c2b5d4e20f89d7bfad75fcd4d149894d390f3))
- **dafny:** update UInt and MemoryMath as needed for DB-ESDK ([#1488](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1488)) ([49e596b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/49e596b1cd8ce446d0b82074ff48ba0406aa8995))

### Maintenance -- Java

- **java:** migrate to Nexus Central for Maven publishing ([#1553](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1553)) ([7d2fcd3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7d2fcd392eb31f023669e309ab9fc557394e932b))

### Maintenance -- Go

- **go:** implement missing MutableMap::content() ([#1519](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1519)) ([f033b91](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f033b915701eaa53d97019af61b96a51fed43483))
- **go:** remove print statements from testLotsOfAdding ([#1468](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1468)) ([594383c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/594383c6fa1ed9bb286290a0b67814953c88eef0))

### Maintenance -- Rust

- **rust:** remove print statements from testLotsOfAdding ([#1469](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1469)) ([9cf1dce](https://github.com/aws/aws-cryptographic-material-providers-library/commit/9cf1dce985d86d83d393e46b7e78697ebda85d90))
- **rust:** update smithy-dafny, use small-int feature ([#1437](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1437)) ([515995e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/515995e68400e56fc720412fe355e6965715136e))

### Miscellaneous

- add MemoryMath to Index.dfy ([#1484](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1484)) ([3196e7d](https://github.com/aws/aws-cryptographic-material-providers-library/commit/3196e7d1e51fd6f1f31fca6d90c1c01d437ae830))
- add MPL CI to principal of KmsKeyForRobbieOnly ([#1528](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1528)) ([527f69d](https://github.com/aws/aws-cryptographic-material-providers-library/commit/527f69d7c0eb2070406051047dcefbabadc374e4))
- bump smithy-dafny to latest ([#1375](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1375)) ([d3e7916](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d3e79168a23381973fab90e0c11e5ec0fb8a37fd))
- CFN for Restricted EC ([#1522](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1522)) ([391fa4c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/391fa4c1163b6722752169181219408660cc9e09))
- CFN for two new roles to prove prefixing/defixing behavior ([#1538](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1538)) ([e810e7d](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e810e7da19c5242435eb8b9c2a922c56d3a6a966))
- CFN KMS GDK for HV-2 ([#1464](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1464)) ([cfbaa58](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cfbaa58f8976c5d7ff5351c4957b9539fcac7e54))
- **CI:** Allow local testing ([#1371](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1371)) ([fe18948](https://github.com/aws/aws-cryptographic-material-providers-library/commit/fe189489ee0e21b3d12944673a9a1de756ee0bc9))
- **CI:** Fix nightly build (mostly) ([#1540](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1540)) ([362ffc1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/362ffc1c8b5adb84af58e783dc5ef696ca103643))
- **CI:** Fix nightly build workflow ([#1541](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1541)) ([48d69eb](https://github.com/aws/aws-cryptographic-material-providers-library/commit/48d69ebeda1e5167f26ebe8f87a51addab3d9afb))
- Create KMS keys for HV1 & HV2 branch keys ([#1419](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1419)) ([2f0696d](https://github.com/aws/aws-cryptographic-material-providers-library/commit/2f0696dbd06e471f4b0bedea7239ec86ff39a79e))
- Create Static Key Store table for storing static branch keys ([#1456](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1456)) ([96b8058](https://github.com/aws/aws-cryptographic-material-providers-library/commit/96b80589406a71503d2e87d2cff8968ac95abd71))
- **dafny:** add tests for multiple utf8 ec entries ([#1424](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1424)) ([131ae58](https://github.com/aws/aws-cryptographic-material-providers-library/commit/131ae583de02cb8352f8a96d69a9e1c84fea7338))
- **dafny:** restore static test branch key id ([#1404](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1404)) ([377de79](https://github.com/aws/aws-cryptographic-material-providers-library/commit/377de796f001ae21f69ac0e10f57709d0e6fa1ef))
- **deps:** Extend supported pyca version range ([#1556](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1556)) ([89f47aa](https://github.com/aws/aws-cryptographic-material-providers-library/commit/89f47aa50a98e211a1cb669f8d7294e340f07723))
- improve performance ([#1286](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1286)) ([d808fd8](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d808fd88df92acf64fb9ca0e7c652d72e05fa50a))
- install polymorph dependencies in github workflows ([#1514](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1514)) ([eb68525](https://github.com/aws/aws-cryptographic-material-providers-library/commit/eb68525d9430ea4dcc355e7f17bef7bafe069035))
- **Python:** bump pyca to 44.0 ([#1555](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1555)) ([4f4cd87](https://github.com/aws/aws-cryptographic-material-providers-library/commit/4f4cd87c5bea38d523aac00947d6678b5ea2b3a0))
- resolve rust warning ([#1394](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1394)) ([e2fe1a4](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e2fe1a4fc79d62c434bdbf72f8713b18ce74071a))
- specify language in commits ([#1382](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1382)) ([ccd56cf](https://github.com/aws/aws-cryptographic-material-providers-library/commit/ccd56cfae7c784e3c852d1f4bcc0b7127525f7d8))

## [1.10.1](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.10.0...v1.10.1) (2025-03-27)

This release is available in the following languages:

- Java

### Maintenance -- All Languages

- **dafny:** update ddb model ([#1357](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1357)) ([8f68a3e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8f68a3ec0e07dfdad9d25376412617dc4932aa0a))

### Maintenance -- Java

- **java:** harden LocalCMCTests.java ([#1365](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1365)) ([c0deb24](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c0deb245a2c8562c8adc6f6fce66e42c8bee8118))

### Miscellaneous

- add proper sleep handling in StormTracker for Python and .NET ([#1369](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1369)) ([77fd007](https://github.com/aws/aws-cryptographic-material-providers-library/commit/77fd007ecac4347087340fd74d56805ae57d3704))
- **CI:** Allow local testing ([#1358](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1358)) ([5ecb410](https://github.com/aws/aws-cryptographic-material-providers-library/commit/5ecb410c3e79d5e986a98281a952bdd3807412a2))

## [1.10.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.9.0...v1.10.0) (2025-03-24)

This release is available in the following languages:

- Python

### Miscellaneous -- Python

- **deps:** extend supported version of pytz library ([#1333](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1333)) ([6f6876a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/6f6876aea8be186555e6430e039f4a6c6883c5d5))

### Miscellaneous

- clarify InFlightTTLExceeded exception ([#1169](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1169)) ([d1c42a6](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d1c42a6840a7846934b6e9124b170ef710cf2aba))
- fix typos in documentation ([#1326](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1326)) ([7f59a7e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7f59a7e073f2abe9effa89f7818ceb50bea9df26))
- let fileio deal in uint8 instead of bv8 ([#1347](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1347)) ([80e28f3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/80e28f3f7816e99ed22120cca6a81628a3ae4892))

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
