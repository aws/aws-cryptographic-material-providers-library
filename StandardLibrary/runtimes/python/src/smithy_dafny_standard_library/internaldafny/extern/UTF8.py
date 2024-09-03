"""
Extern UTF8 encode and decode methods.

Note:
Python's `.encode()`/`.decode()` handle surrogates with 'surrogatepass'.
Python represents Unicode characters based on their presence in the Basic Multilingual Plane (BMP).
The BMP includes characters from U+0000 to U+FFFF (or, 0 <= ord(chr) < 65535).

If a character is inside the BMP, Python internally represents it as a single UTF-16-encoded code unit.
ex.
"\u2386" == '⎆' --> ord('⎆') == 9094 --> 9094 < 65535 --> in BMP
Since "\u2386" is in the BMP, Python internally represents it as '⎆':

```
>>> s = "\u2386"
>>> s
'⎆'
```

In contrast, if a character is outside the BMP, Python internally represents it
as a unicode-escaped string using surrogate pairs.
ex.
"\uD808\uDC00" == '𒀀' --> ord('𒀀') == 73728 --> 73728 > 65535 --> outside BMP
Since "\uD808\uDC00" is outside the BMP, Python internally represents it as "\uD808\uDC00":

```
>>> s = "\uD808\uDC00"
>>> s
'\ud808\udc00'
```
"""
import _dafny

import standard_library.internaldafny.generated.UTF8
from standard_library.internaldafny.generated.UTF8 import *


# Extend the Dafny-generated class with our extern methods
class default__(standard_library.internaldafny.generated.UTF8.default__):

  @staticmethod
  def Encode(s):
    try:
      return Wrappers.Result_Success(_dafny.Seq(
          s.VerbatimString(False).encode('utf-16', 'surrogatepass').decode('utf-16').encode('utf-8')
      ))
    # Catch both UnicodeEncodeError and UnicodeDecodeError.
    # The `try` block involves both encoding and decoding.
    except (UnicodeDecodeError, UnicodeEncodeError):
      return Wrappers.Result_Failure(_dafny.Seq("Could not encode input to Dafny Bytes."))
    
  @staticmethod
  def Decode(s):
    try:
      decoded = bytes(s).decode('utf-8')
      return Wrappers.Result_Success(_dafny.Seq(
        decoded
      ))
    except (UnicodeDecodeError):
      return Wrappers.Result_Failure(_dafny.Seq("Could not decode input from Dafny Bytes."))


# Export externs
standard_library.internaldafny.generated.UTF8.default__ = default__