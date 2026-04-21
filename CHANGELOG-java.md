# Changelog

## [1.11.1](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.11.0-java...v1.11.1-java) (2026-04-21)

### ⚠ BREAKING CHANGES

* **.net:** add a separate releaserc file to keep track of net releases (#1814)

* **.net:** add a separate releaserc file to keep track of net releases ([#1814](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1814)) ([c13c58f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c13c58fc72ebd8e90e338a73c4f617362f1883a9))

### Fixes -- All Languages

* **Go:** Improve Go performance ([#1729](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1729)) ([cc30ecc](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cc30ecc512fa6ac02a1011cf81b0b00bbd5d600d))
* Updated pytz version range to include 2025 releases ([#1644](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1644)) ([1aced27](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1aced27699de7aebcb6d4513a9e72c604c7ce855))

### Maintenance -- All Languages

* 1.11.1 [skip ci] ([#1650](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1650)) ([51db080](https://github.com/aws/aws-cryptographic-material-providers-library/commit/51db0806a00c19c3be5dcbfb7d0bec72004af448))
* 5 instead of 25 interop decrypt processes ([#1620](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1620)) ([d82696b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d82696b520681eaabd8f9a6c76bd9a208de4d6ac))
* add managed policy to cfn template ([#1758](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1758)) ([81cc558](https://github.com/aws/aws-cryptographic-material-providers-library/commit/81cc5588a7402d319a2caa32d69c50553bb1a47d))
* add setup smithy dafny dependencies to net releases ([#1791](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1791)) ([734c1a3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/734c1a31fc4521dc0653433565d5d6171e61d1ac))
* Add UserAgent string to KMS client ([#1716](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1716)) ([09b2cda](https://github.com/aws/aws-cryptographic-material-providers-library/commit/09b2cdab5bd2e711e5487db747ff3380a393c48a))
* allow local testing ([#1790](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1790)) ([f2a04e7](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f2a04e7bdda613626c256f91ab7e4498c6dbdd8d))
* allow local testing for python ([#1598](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1598)) ([cbfa209](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cbfa209c0b9453fe633a3047e3dcd5db0e7fa728))
* bump CI to macos-14 ([#1734](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1734)) ([1413b88](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1413b8815e34d5745f39773b82425b928cc88261))
* bump credentials to 2 hours, for python ([#1621](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1621)) ([69991da](https://github.com/aws/aws-cryptographic-material-providers-library/commit/69991da9a26e4422dfdeb8fc95a87a46b0bb3ccc))
* bump smithy-dafny ([#1657](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1657)) ([e2fb76c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e2fb76cfaf5201dab2fcfc145b46a688d27b2f14))
* bump smithy-dafny ([#1706](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1706)) ([dc1678a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/dc1678ab78948bee223f029df36b9f5d2cb0276d))
* **cfn:** add trusted policy for optools mpl-python roles ([#1602](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1602)) ([436d939](https://github.com/aws/aws-cryptographic-material-providers-library/commit/436d93951038e4107b36bf1f4cb3a0a5fb870577))
* **CI:** ci action to upload performance logs to cloudwatch ([#1754](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1754)) ([c5b3ac6](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c5b3ac65e98535e4771e4cdbbb48c5fc0a54509f))
* **CI:** fix daily CI and add slack notification to it ([#1647](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1647)) ([c546646](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c546646a719b54f880a8aeccc6a6489fcf332070))
* **ci:** Install Go/goimports as codegen dependencies ([#1713](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1713)) ([7a6fd63](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7a6fd6313143d7940dba7971b8193f3d0ba51de7))
* **CI:** reduce flakiness of install_smithy_dafny_codegen_dependencies ([#1824](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1824)) ([cd9dec3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cd9dec30f7a0fa34abc7a3bec6ee3e5fe1b59ba3))
* **CI:** send slack message on new GHI  ([#1632](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1632)) ([e80b7ae](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e80b7aeaf691e956b6177aa24633681dcfe7a7ba))
* **CI:** test DB-ESDK java examples from MPL  ([#1692](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1692)) ([4e06e37](https://github.com/aws/aws-cryptographic-material-providers-library/commit/4e06e375317f354a280d2fad4401725786641f38))
* **CI:** Test Rust on Dafny prerelease in nightly build ([#1623](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1623)) ([92070bc](https://github.com/aws/aws-cryptographic-material-providers-library/commit/92070bc128da94a24cfb84cc1fdd50f8ce5623f7))
* **CI:** update slack notification to include link of GHA run  ([#1659](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1659)) ([c6e2c20](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c6e2c203ec976c5488e08c79e378bc4b34da4b4e))
* **CI:** update to not trigger workflow on PR comments ([#1640](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1640)) ([c62e8cf](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c62e8cf0bf6b3efa0ae479a57b08ca91ef0306b6))
* clean up submodule URL to remove embedded username ([#1757](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1757)) ([df1ec90](https://github.com/aws/aws-cryptographic-material-providers-library/commit/df1ec90a2d40f81a642d30c1222c41989c1d787d))
* **dafny:** add fuzz testing to MPL ([#1622](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1622)) ([14fad38](https://github.com/aws/aws-cryptographic-material-providers-library/commit/14fad380f4350b3b32e478feb5fab03dabd7b14b))
* **dafny:** add new SearchAndReplaceWhole and friends ([#1680](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1680)) ([74e98c1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/74e98c10184c27bc57ba5b77386872466213f91f))
* **dafny:** add Rust and Go to supported languages  ([#1492](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1492)) ([87ab402](https://github.com/aws/aws-cryptographic-material-providers-library/commit/87ab40233096739f2aa709fdcd948ce7452c7d04))
* **dafny:** add search and replace methods ([#1649](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1649)) ([c86be0d](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c86be0dc7bb7609facad17adb6fc303478865f60))
* **dafny:** append our user agent in KMS client ([#1564](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1564)) ([03d03ac](https://github.com/aws/aws-cryptographic-material-providers-library/commit/03d03ac1f3591885bcc583efb988602ed129c3c5))
* **dafny:** bump setup_dafny ([#1712](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1712)) ([2c57523](https://github.com/aws/aws-cryptographic-material-providers-library/commit/2c575232dd97fedcbb84232c8fb75e82e8483734))
* **dafny:** optimize mutation map for O(1) performance in Go  ([#1687](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1687)) ([68cd7cb](https://github.com/aws/aws-cryptographic-material-providers-library/commit/68cd7cb768ab2ffc85052959e46122af1e1c1dcf))
* **dafny:** remove negative test for codebuild runner ([#1603](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1603)) ([8b45e40](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8b45e40e9fa081e277837946e53836b308429ee8))
* **deps:** bump actions/download-artifact from 4 to 6 in /.github/workflows ([#1747](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1747)) ([2a767e7](https://github.com/aws/aws-cryptographic-material-providers-library/commit/2a767e74e71efbe03c1a2beef16cc7d2e3e33fae))
* **deps:** bump cryptography upperbound to <47 due to CVE-2026-26007 ([#1800](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1800)) ([aaf70a5](https://github.com/aws/aws-cryptographic-material-providers-library/commit/aaf70a580d19494ee28736e46439d8ab4f5ccf78))
* **deps:** bump slackapi/slack-github-action from 2.1.0 to 2.1.1 in /.github/workflows ([#1638](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1638)) ([40b643f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/40b643f9b95e325131a99c7ac5227d0851927980))
* **deps:** bump slackapi/slack-github-action from 2.1.1 to 3.0.1 in /.github/workflows ([#1818](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1818)) ([eb856f5](https://github.com/aws/aws-cryptographic-material-providers-library/commit/eb856f56d96270ec49d2037161c15fb06274614c))
* **deps:** update deps across the repo ([#1773](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1773)) ([edcc64c](https://github.com/aws/aws-cryptographic-material-providers-library/commit/edcc64c96760e23e948afa7d23f796045e3546d8))
* fix daily ci ([#1787](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1787)) ([7758fee](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7758feebd2dddf750aa60666cfb850f691c0c637))
* **Go:** Add Go release script and workflow to run it  ([#1562](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1562)) ([1c563bd](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1c563bdf8985f4c79b376929faa61496964dc69c))
* prep python 1.11.2 release ([#1802](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1802)) ([ce27052](https://github.com/aws/aws-cryptographic-material-providers-library/commit/ce27052072aa8f0fd60fd5161f17c2fef100261b))
* **release:** 1.11.2 ([#1788](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1788)) ([48ec90a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/48ec90a9b4dec24cb18c6b01e0b9a17edebc893c))
* update check-files ([#1785](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1785)) ([14af920](https://github.com/aws/aws-cryptographic-material-providers-library/commit/14af9201be58aa20760e3e1c453de28418865100))
* update GitHub Actions to latest major versions ([#1821](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1821)) ([c16d163](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c16d1630a8aadeff282c517436da54486aced429))
* update kms externs correctly ([#1717](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1717)) ([e11ba53](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e11ba531f3f12610ded9df7acb49b41f908b7b22))
* Update workflow permissions ([#1783](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1783)) ([37f416e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/37f416ec8865795ebe443ebf0b7978d9d70a21a8))
* use local builds ([#1804](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1804)) ([006061a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/006061a43b2bb367f189cdf0cbfbb17341e6cbb8))

### Maintenance -- Java

* **java:** update changelog for Java ([4f4f033](https://github.com/aws/aws-cryptographic-material-providers-library/commit/4f4f033a3aea109b43a574ebfba32034be24a2c5))
