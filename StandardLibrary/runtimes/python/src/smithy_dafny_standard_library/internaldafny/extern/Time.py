import datetime
import pytz
import _dafny

import smithy_dafny_standard_library.internaldafny.generated.Time
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers

# Extend generated class with our externs
class default__(smithy_dafny_standard_library.internaldafny.generated.Time.default__):
    def CurrentRelativeTimeMilli():
        return datetime.datetime.now(tz = pytz.UTC).timestamp() * 1000

    def CurrentRelativeTime():
        return datetime.datetime.now(tz = pytz.UTC).timestamp()

    def GetCurrentTimeStamp():
        try:
            d = datetime.datetime.now(tz = pytz.UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            return Wrappers.Result_Success(_dafny.Seq(_dafny.string_of(d)))
        except Exception as e:
            return Wrappers.Result_Failure(_dafny.string_of("Could not generate a timestamp in ISO8601: " + e))
        

# Export externs
smithy_dafny_standard_library.internaldafny.generated.Time.default__ = default__