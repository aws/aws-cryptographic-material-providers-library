# Changelog

## [releases/go/mpl/v0.2.1] - 2025-08-08

## [releases/go/mpl/v0.2.1] - 2025-08-06

### Fixes

- _(all languages)_ Bump Dafny libraries for JSON fix (#1517)

### Maintenance

- _(all languages)_ Update ddb model (#1357)
- _(all languages)_ Don't recalculate RSA key on every decrypt (#1448)
- _(all languages)_ Store privateKey in RawRSAKeyring because some Java code needs it (#1450)
- _(go)_ Remove print statements from testLotsOfAdding (#1468)
- _(all languages)_ Support for memory size constraints (#1481)
- _(all languages)_ Update UInt and MemoryMath as needed for DB-ESDK (#1488)
- _(all languages)_ More using uint64 instead of nat (#1490)
- _(go)_ Implement missing MutableMap::content() (#1519)
- _(all languages)_ BK fix to extract encryption context for branch key materials (#1523)
- _(all languages)_ Make HasSubString generic (#1549)
- _(all languages)_ Update makefile to only use prettier 3.5.3 (#1577)
- _(all languages)_ Remove negative test for codebuild runner (#1603)
- _(go)_ Automate changelog for Go release (#1607)
- _(all languages)_ Append our user agent in KMS client (#1564)
- _(all languages)_ Add Rust and Go to supported languages (#1492)
- _(go)_ Update go test matrix and clean up setup (#1625)
- _(all languages)_ Add search and replace methods (#1649)
- _(go)_ Update Go release script for ESDK and DB-ESDK (#1653)
- _(go)_ Release smithy-dafny-standard-library Go module 0.2.1 (#1666)
- _(go)_ Release kms Go module 0.2.1 (#1667)
- _(go)_ Release primitives Go module 0.2.1 (#1669)
- _(go)_ Release dynamodb Go module 0.2.1 (#1671)

### Miscellaneous

- _(all languages)_ Restore static test branch key id (#1404)
- _(all languages)_ Add tests for multiple utf8 ec entries (#1424)

# [0.2.0] (2025-03-18)

- Breaks compatibility with v0.1.0 when using chars with unicode codepoints > 65535
- utf8-utf16 encoding fix
- support for utf16 surrogate pairs / chars with unicode codepoints > 65535
- fix for replacement char U+FFFD
- empty byte fix to allow custom keyring wrapping
- other operational improvements

# [0.1.0] (2025-01-15)

Semantic version upgrade from v0.0.1 to v0.1.0

# [0.0.1] (2025-01-14)

Initial release for Go based on MPL [1.8.0](../../../CHANGELOG.md)
