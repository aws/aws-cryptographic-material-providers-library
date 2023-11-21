from standard_library.internal_generated_dafny.UTF8 import *
import standard_library.internal_generated_dafny.UTF8
import _dafny

# Extend the Dafny-generated class with our extern method
class default__(standard_library.internal_generated_dafny.UTF8.default__):

  @staticmethod
  def Encode(s):
    return Wrappers.Result_Success(_dafny.Seq(b''.join(bytes(e, encoding="utf-8") for e in s.Elements)))

standard_library.internal_generated_dafny.UTF8.default__ = default__