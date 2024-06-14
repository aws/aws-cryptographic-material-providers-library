import datetime
import pytz
import _dafny

import standard_library.internaldafny.generated.Time
import standard_library.internaldafny.generated.Wrappers as Wrappers

class default__:
    def CurrentRelativeTime():
        return datetime.datetime.now(tz = pytz.UTC).timestamp() * 1000

    def GetCurrentTimeStamp():
        try:
            d = datetime.datetime.now(tz = pytz.UTC).strftime("%Y-%m-%d'T'%H:%M:%S:%f'Z'")
            return Wrappers.Result_Success(_dafny.Seq(_dafny.string_of(d)))
        except Exception as e:
            return Wrappers.Result_Failure(_dafny.string_of("Could not generate a timestamp in ISO8601: " + e))
        

# Export externs
standard_library.internaldafny.generated.Time.default__ = default__