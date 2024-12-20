import os
import _dafny
import platform
import sys

import smithy_dafny_standard_library.internaldafny.generated.OsLang

# Extend generated class with our externs
class default__(smithy_dafny_standard_library.internaldafny.generated.OsLang.default__):
    def GetOsShort():
        sys = platform.system()
        if sys == "Darwin":
            return _dafny.Seq(_dafny.string_of("MacOS"))
        if sys == "Linux":
            return _dafny.Seq(_dafny.string_of("Unix"))
        return _dafny.Seq(_dafny.string_of(sys))

    def GetOsLong():
        return _dafny.Seq(_dafny.string_of(platform.platform()))

    def GetLanguageShort():
        return _dafny.Seq(_dafny.string_of("Python"))

    def GetLanguageLong():
        return _dafny.Seq(_dafny.string_of("Python " + sys.version))

# Export externs
smithy_dafny_standard_library.internaldafny.generated.OsLang.default__ = default__
