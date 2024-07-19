import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings

# Module: FileIO

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ReadBytesFromFile(path):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_168_isError_: bool
        d_169_bytesRead_: _dafny.Seq
        d_170_errorMsg_: _dafny.Seq
        out1_: bool
        out2_: _dafny.Seq
        out3_: _dafny.Seq
        out1_, out2_, out3_ = DafnyLibraries.FileIO.INTERNAL_ReadBytesFromFile(path)
        d_168_isError_ = out1_
        d_169_bytesRead_ = out2_
        d_170_errorMsg_ = out3_
        if d_168_isError_:
            res = Wrappers.Result_Failure(d_170_errorMsg_)
        elif True:
            res = Wrappers.Result_Success(d_169_bytesRead_)
        return res
        return res

    @staticmethod
    def WriteBytesToFile(path, bytes):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_171_isError_: bool
        d_172_errorMsg_: _dafny.Seq
        out4_: bool
        out5_: _dafny.Seq
        out4_, out5_ = DafnyLibraries.FileIO.INTERNAL_WriteBytesToFile(path, bytes)
        d_171_isError_ = out4_
        d_172_errorMsg_ = out5_
        if d_171_isError_:
            res = Wrappers.Result_Failure(d_172_errorMsg_)
        elif True:
            res = Wrappers.Result_Success(())
        return res
        return res

