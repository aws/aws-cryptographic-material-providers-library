"""
Extern UTF8 encode and decode methods.

Note:
Python represents Unicode-escaped characters based on their presence in the Basic Multilingual Plane (BMP).
The BMP includes characters from U+0000 to U+FFFF (or, 0 <= ord(chr) < 65535; or, 0x0 <= hex(chr) < 0xFFFF).
Note that this is the range of characters that can fit into a single UTF-16 code unit (2 bytes).

If a Unicode-escaped character is inside the BMP, Python internally represents it
as a single UTF-16-encoded code unit.
ex.
"\u2386" == '⎆' --> ord('⎆') == 9094 --> 9094 < 65535 --> in BMP
Since "\u2386" is in the BMP, Python internally represents it as '⎆':

```
>>> s = "\u2386"
>>> s
'⎆'
```

However, if a Unicode-escaped character is outside the BMP, Python internally represents it
as a Unicode-escaped character using surrogate pairs.
ex.
"\uD808\uDC00" == '𒀀' --> ord('𒀀') == 73728 --> 73728 > 65535 --> outside BMP
Since "\uD808\uDC00" is outside the BMP, Python internally represents it as "\uD808\uDC00":

```
>>> s = "\uD808\uDC00"
>>> s
'\ud808\udc00'
```

Dafny expects its strings to be UTF-16 code units.
However, the `.decode()` method with 'surrogatepass' leaves '\ud808\udc00' as '𒀀',
which, if passed directly to Dafny, will be interpreted as a single UTF-32 code unit,
instead of the desired two UTF-16 code units.

To correct this, the extern implementations
convert between Dafny Seqs of UTF-16 code units (handling multi-byte surrogate pairs)
and Dafny Seqs of UTF-8 bytes.
"""
import _dafny
import struct

import smithy_dafny_standard_library.internaldafny.generated.UTF8
from smithy_dafny_standard_library.internaldafny.generated.UTF8 import *


# Extend the Dafny-generated class with our extern methods
class default__(smithy_dafny_standard_library.internaldafny.generated.UTF8.default__):

  @staticmethod
  def Encode(dafny_utf16_code_units):
    try:
      return Wrappers.Result_Success(_dafny.Seq(
          default__._strict_tostring(dafny_utf16_code_units).encode('utf-8')
      ))
    # Catch both UnicodeEncodeError and UnicodeDecodeError.
    # The `try` block involves both encoding and decoding.
    # OverflowError is possibly raised at `_strict_tostring`'s `ord(c).to_bytes`
    #   if the char `c` is not valid.
    except (UnicodeDecodeError, UnicodeEncodeError, OverflowError):
      return Wrappers.Result_Failure(_dafny.Seq("Could not encode input to Dafny Bytes."))
    
  @staticmethod
  def _strict_tostring(dafny_ascii_string):
    """
    Converts a Dafny Seq of UTF-16 code units
    into a string that can be encoded with Python's built-in `.encode('utf-8')`.

    This encoding-decoding allows subsequent UTF8 encodings
    to handle surrogates as expected by Dafny code.

    This is exactly the `_dafny.string_from_utf_16` method from the DafnyRuntime,
    except with two changes
    1)
    `errors = 'strict'` here,
    instead of
    `errors = 'replace'` in the `_dafny.string_from_utf_16` function.
    `strict` will throw an exception for invalid encodings, allowing us
    to detect invalid encodings and raise exceptions,
    while `replace` will fail silently.

    2)
    Using big-endian internally instead of little-endian.
    :param s:
    :return:
    """
    return b''\
      .join([c.to_bytes(2, byteorder="big") \
            if isinstance(c, int) \
            else ord(c).to_bytes(2, byteorder="big") \
            for c in dafny_ascii_string])\
      .decode("utf-16-be", errors = 'strict')
    
  @staticmethod
  def Decode(dafny_utf8):
    try:
      utf8_str = bytes(dafny_utf8).decode('utf-8')
      unicode_escaped_utf8_str = default__._reverse_strict_tostring(utf8_str)
      return Wrappers.Result_Success(unicode_escaped_utf8_str)
    # Catch both UnicodeEncodeError and UnicodeDecodeError.
    # The `try` block involves both encoding and decoding.
    # ValueError and TypeError are possibly raised at `_reverse_strict_tostring`'s `chr()`.
    # struct.error is possibly raised at `struct.unpack`.
    except (UnicodeDecodeError, UnicodeEncodeError, ValueError, TypeError, struct.error):
      return Wrappers.Result_Failure(_dafny.Seq("Could not decode input from Dafny Bytes."))


  @staticmethod
  def _reverse_strict_tostring(utf8_str):
    """
    Converts a string into a Dafny Seq of unicode-escaped ASCII characters.
    This is the inverse of the `_strict_tostring` function in this file.
    :param s:
    :return:
    """
    utf16_bytes = utf8_str.encode("utf-16-be", errors = "strict")
    out = []
    # len(b)/2 is an integer by construction of UTF-16 encoding (2 bytes per encoded character)
    for i in range(int(len(utf16_bytes)/2)):
      # Take two consecutive bytes;
      utf_16_bytepair = utf16_bytes[2*i:2*i+2]
      # Unpack them into an ordinal representation;
      packed_bytes = struct.unpack('>H', utf_16_bytepair)
      # Convert into a character representation;
      char_representation = chr(packed_bytes[0])
      # Append to returned string
      out.append(char_representation)
    return _dafny.Seq(out)

# Export externs
smithy_dafny_standard_library.internaldafny.generated.UTF8.default__ = default__