# Changelog

## [1.11.3](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.11.2-python...v1.11.3-python) (2026-08-31)

### ⚠ BREAKING CHANGES

* **.net:** add a separate releaserc file to keep track of net releases (#1814)

* **.net:** add a separate releaserc file to keep track of net releases ([#1814](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1814)) ([c13c58f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c13c58fc72ebd8e90e338a73c4f617362f1883a9))

### Features -- All Languages

* **ci:** Add workflow to auto-sync mutations/mutations with main ([#1858](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1858)) ([7f758c0](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7f758c0d5f607e4859ccd8790fe58e2a27748ac9))

### Fixes -- All Languages

* **ci:** Prevent script injection in GitHub Actions workflows ([#1917](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1917)) ([189b87b](https://github.com/aws/aws-cryptographic-material-providers-library/commit/189b87bb25c19e410bf9b4ec9e26e39ad73399a8))

### Fixes -- Python

* **python:** convert sleepMilli to seconds for time.sleep in python stormtracking cache ([#1941](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1941)) ([2872cb0](https://github.com/aws/aws-cryptographic-material-providers-library/commit/2872cb042399ccb30ea0874b3aeed70ee315bd70))
* **python:** skip missing interpreters in tox so CI matrix jobs pass ([#1919](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1919)) ([9f72026](https://github.com/aws/aws-cryptographic-material-providers-library/commit/9f7202691b5022e0213fde41c38720d4180b103b))

### Miscellaneous

* add special-characters-workaround to avoid sigv4 failure ([#1874](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1874)) ([e2d01b9](https://github.com/aws/aws-cryptographic-material-providers-library/commit/e2d01b93140905cdf19931369268fe1c01c08505))
* **ci:** add a date timestamp to reduce daily ci flakiness ([#1875](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1875)) ([da42f3e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/da42f3e5e8594f7a7c7207c85e6816ec517c612c))
* **ci:** add concurrency control  ([#1873](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1873)) ([aa1f539](https://github.com/aws/aws-cryptographic-material-providers-library/commit/aa1f5399928a629d3bf6f10c4a82032e592b906e))
* **CI:** reduce flakiness of install_smithy_dafny_codegen_dependencies ([#1824](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1824)) ([cd9dec3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cd9dec30f7a0fa34abc7a3bec6ee3e5fe1b59ba3))
* **CI:** split up build from tests to reduce throttling ([#1872](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1872)) ([3e7170e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/3e7170e33283d96d3dfb408fd6e06515b3fd016e))
* **ci:** update install smithy-dafny deps action to work upstream and add retries ([#1855](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1855)) ([f4beb38](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f4beb3803744c588b9f868401901a8180e01a717))
* **dependabot:** modernize config with full ecosystem coverage ([#1897](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1897)) ([1b529ba](https://github.com/aws/aws-cryptographic-material-providers-library/commit/1b529ba0fef59bfb0c5ccc5e4d80d52360cf0d85))
* **deps:** bump cryptography upper bound to <51 ([#1939](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1939)) ([47a1577](https://github.com/aws/aws-cryptographic-material-providers-library/commit/47a15777a60e6580df22fc69e9a33e6798a19a29))
* **deps:** bump cryptography upperbound to <49 to allow patching GH… ([#1918](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1918)) ([cdd05b1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/cdd05b14f02a2dd2b0ba8a0d1dbebf0b8d74b003))
* **deps:** bump slackapi/slack-github-action from 2.1.1 to 3.0.1 in /.github/workflows ([#1818](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1818)) ([eb856f5](https://github.com/aws/aws-cryptographic-material-providers-library/commit/eb856f56d96270ec49d2037161c15fb06274614c))
* **deps:** bump slackapi/slack-github-action from 3.0.1 to 3.0.3 in /.github/workflows ([#1866](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1866)) ([478fb6d](https://github.com/aws/aws-cryptographic-material-providers-library/commit/478fb6dce1b9a3985f015fbed6bda7fcd8e5b9b6))
* Golang release staging branch mpl 0.4.0 ([#1864](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1864)) ([c589db3](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c589db3bc162a3c37e82f8510233ba869e1a6ff4))
* Golang release staging branch primitives 0.4.0 ([#1861](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1861)) ([9b98890](https://github.com/aws/aws-cryptographic-material-providers-library/commit/9b98890ce9c666185a06d6e44135b69841e6f32a))
* Golang release staging branch/dynamodb/0.4.0 ([#1863](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1863)) ([8d7671e](https://github.com/aws/aws-cryptographic-material-providers-library/commit/8d7671ea7b4ff27e325810cf4298ff5f681a39b4))
* Golang release staging branch/kms/0.4.0 ([#1860](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1860)) ([0724017](https://github.com/aws/aws-cryptographic-material-providers-library/commit/07240175b12f1b5ab63fe87f0e85233be0fdf996))
* update changelog and version number for 1.11.1 release in Java ([#1852](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1852)) ([d592385](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d5923859cefdc0f363b667633bdf0f3d37bf42a1))
* update GitHub Actions to latest major versions ([#1821](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1821)) ([c16d163](https://github.com/aws/aws-cryptographic-material-providers-library/commit/c16d1630a8aadeff282c517436da54486aced429))
* update semantic release to differentiate between runtimes  ([#1844](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1844)) ([60c08fa](https://github.com/aws/aws-cryptographic-material-providers-library/commit/60c08fa412b20d815d3c0ad74ecd2570721929d9))
* upgrade dafny runtime go v4.11.3 ([#1849](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1849)) ([7b1f859](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7b1f8594e3101508ac9db09b395522cf1ee7305c))
* upgrade go version to 1.24 ([#1856](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1856)) ([50d285f](https://github.com/aws/aws-cryptographic-material-providers-library/commit/50d285f1797e44f2485bc864de43856b6d416764))
* use local builds ([#1804](https://github.com/aws/aws-cryptographic-material-providers-library/issues/1804)) ([006061a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/006061a43b2bb367f189cdf0cbfbb17341e6cbb8))
