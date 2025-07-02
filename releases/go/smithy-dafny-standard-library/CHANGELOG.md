# Changelog

## [releases/go/mpl/v0.2.1] - 2025-07-02

### Fixes

- *(dafny)* Bump Dafny libraries for JSON fix (#1517)

### Maintenance

- *(dafny)* Update ddb model (#1357)
- *(dafny)* Don't recalculate RSA key on every decrypt (#1448)
- *(dafny)* Store privateKey in RawRSAKeyring because some Java code needs it (#1450)
- *(go)* Remove print statements from testLotsOfAdding (#1468)
- *(dafny)* Support for memory size constraints (#1481)
- *(dafny)* Update UInt and MemoryMath as needed for DB-ESDK (#1488)
- *(dafny)* More using uint64 instead of nat (#1490)
- *(go)* Implement missing MutableMap::content() (#1519)
- *(dafny)* BK fix to extract encryption context for branch key materials (#1523)
- *(dafny)* Make HasSubString generic (#1549)
- *(dafny)* Update makefile to only use prettier 3.5.3  (#1577)
- *(dafny)* Remove negative test for codebuild runner (#1603)

### Miscellaneous

- *(dafny)* Restore static test branch key id (#1404)
- *(dafny)* Add tests for multiple utf8 ec entries (#1424)

# [0.2.0] (2025-03-17)

- Breaks compatibility with v0.1.0 when using chars with unicode codepoints > 65535
- utf8-utf16 encoding fix
- support for utf16 surrogate pairs / chars with unicode codepoints > 65535
- fix for replacement char U+FFFD
- empty byte fix to allow custom keyring wrapping
- other operational improvements

# [0.1.0] (2025-01-15)

Semantic version upgrade from v0.0.1 to v0.1.0

# [0.0.1] (2025-01-10)

Initial release for Go based on MPL [1.8.0](../../../CHANGELOG.md)
