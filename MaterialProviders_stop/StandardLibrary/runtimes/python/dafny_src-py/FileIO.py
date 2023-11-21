import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings

assert "FileIO" == __name__
FileIO = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ReadBytesFromFile(path):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_164_isError_: bool
        d_165_bytesRead_: _dafny.Seq
        d_166_errorMsg_: _dafny.Seq
        out1_: bool
        out2_: _dafny.Seq
        out3_: _dafny.Seq
        out1_, out2_, out3_ = DafnyLibraries.FileIO.INTERNAL_ReadBytesFromFile(path)
        d_164_isError_ = out1_
        d_165_bytesRead_ = out2_
        d_166_errorMsg_ = out3_
        res = (Wrappers.Result_Failure(d_166_errorMsg_) if d_164_isError_ else Wrappers.Result_Success(d_165_bytesRead_))
        return res
        return res

    @staticmethod
    def WriteBytesToFile(path, bytes):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_167_isError_: bool
        d_168_errorMsg_: _dafny.Seq
        out4_: bool
        out5_: _dafny.Seq
        out4_, out5_ = DafnyLibraries.FileIO.INTERNAL_WriteBytesToFile(path, bytes)
        d_167_isError_ = out4_
        d_168_errorMsg_ = out5_
        res = (Wrappers.Result_Failure(d_168_errorMsg_) if d_167_isError_ else Wrappers.Result_Success(()))
        return res
        return res

