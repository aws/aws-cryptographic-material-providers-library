"""
Extern UTF8 encode and decode methods.

Note:
Python's `.encode()`/`.decode()` handle surrogates with 'surrogatepass'.
However, the results of 'surrogatepass' does not comply with Dafny's expectations.
Dafny expects a strict interpretation of Python's Unicode handling.
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

However, the `.decode()` method with 'surrogatepass' leaves '\ud808\udc00' as '𒀀',
which does not match Dafny's expectation of the literal interpretation of this field.
To correct this, the Decode extern implementation
re-encodes any characters outside the BMP,
then decodes them under the expected decoding.
"""
import _dafny
import struct

import standard_library.internaldafny.generated.UTF8
from standard_library.internaldafny.generated.UTF8 import *


# Extend the Dafny-generated class with our extern methods
class default__(standard_library.internaldafny.generated.UTF8.default__):

  @staticmethod
  def Encode(dafny_string):
    try:
      utf16_bytes = b''.join([ord(unit).to_bytes(2, byteorder='big') for unit in dafny_string.VerbatimString(False)])
      return Wrappers.Result_Success(_dafny.Seq(
        utf16_bytes.decode('utf-16-be').encode('utf-8')
      ))
    # Catch both UnicodeEncodeError and UnicodeDecodeError.
    # The `try` block involves both encoding and decoding.
    # OverflowError is possibly raised at `_strict_tostring`'s `ord(c).to_bytes`
    # if the char `c` is not valid.
    except (UnicodeDecodeError, UnicodeEncodeError, OverflowError):
      return Wrappers.Result_Failure(_dafny.Seq("Could not encode input to Dafny Bytes."))
    
  @staticmethod
  def Decode(dafny_utf8):
    print(f"{dafny_utf8.Elements=}")
    try:
      utf16_bytes = bytes(dafny_utf8).decode('utf-8').encode('utf-16-be')
      # decoded = bytes(s).decode('utf-8').encode('utf-16')
      return Wrappers.Result_Success(_dafny.Seq(
        [chr(int.from_bytes(utf16_bytes[i:i+2])) for i in range(0, len(utf16_bytes), 2)]
      ))
    except (UnicodeDecodeError, UnicodeEncodeError, ValueError, TypeError, struct.error):
      return Wrappers.Result_Failure(_dafny.Seq("Could not decode input from Dafny Bytes."))


# Export externs
standard_library.internaldafny.generated.UTF8.default__ = default__