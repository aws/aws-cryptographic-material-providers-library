# Changelog

## [releases/go/mpl/v0.2.1] - 2025-08-06

### Fixes

- *(all languages)* Bump Dafny libraries for JSON fix (#1517)

### Maintenance

- *(all languages)* Update ddb model (#1357)
- *(all languages)* Don't recalculate RSA key on every decrypt (#1448)
- *(all languages)* Store privateKey in RawRSAKeyring because some Java code needs it (#1450)
- *(go)* Remove print statements from testLotsOfAdding (#1468)
- *(all languages)* Support for memory size constraints (#1481)
- *(all languages)* Update UInt and MemoryMath as needed for DB-ESDK (#1488)
- *(all languages)* More using uint64 instead of nat (#1490)
- *(go)* Implement missing MutableMap::content() (#1519)
- *(all languages)* BK fix to extract encryption context for branch key materials (#1523)
- *(all languages)* Make HasSubString generic (#1549)
- *(all languages)* Update makefile to only use prettier 3.5.3  (#1577)
- *(all languages)* Remove negative test for codebuild runner (#1603)
- *(go)* Automate changelog for Go release  (#1607)
- *(all languages)* Append our user agent in KMS client (#1564)
- *(all languages)* Add Rust and Go to supported languages  (#1492)
- *(go)* Update go test matrix and clean up setup  (#1625)
- *(all languages)* Add search and replace methods (#1649)
- *(go)* Update Go release script for ESDK and DB-ESDK (#1653)
- *(go)* Release smithy-dafny-standard-library Go module 0.2.1  (#1666)

### Miscellaneous

- *(all languages)* Restore static test branch key id (#1404)
- *(all languages)* Add tests for multiple utf8 ec entries (#1424)
# [0.2.0] (2025-03-18)

- Breaks compatibility with v0.1.0 when using chars with unicode codepoints > 65535
- utf8-utf16 encoding fix
- support for utf16 surrogate pairs / chars with unicode codepoints > 65535
- fix for replacement char U+FFFD
- empty byte fix to allow custom keyring wrapping
- other operational improvements

# [0.1.0] (2025-01-15)

Semantic version upgrade from v0.0.1 to v0.1.0

# [0.0.1] (2025-01-13)

Initial release for Go based on MPL [1.8.0](../../../CHANGELOG.md)
