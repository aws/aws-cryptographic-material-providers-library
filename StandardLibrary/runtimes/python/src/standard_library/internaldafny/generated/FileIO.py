import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries

# Module: FileIO

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ReadBytesFromFile(path):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_177_isError_: bool
        d_178_bytesRead_: _dafny.Seq
        d_179_errorMsg_: _dafny.Seq
        out1_: bool
        out2_: _dafny.Seq
        out3_: _dafny.Seq
        out1_, out2_, out3_ = DafnyLibraries.FileIO.INTERNAL_ReadBytesFromFile(path)
        d_177_isError_ = out1_
        d_178_bytesRead_ = out2_
        d_179_errorMsg_ = out3_
        res = (Wrappers.Result_Failure(d_179_errorMsg_) if d_177_isError_ else Wrappers.Result_Success(d_178_bytesRead_))
        return res
        return res

    @staticmethod
    def WriteBytesToFile(path, bytes):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_180_isError_: bool
        d_181_errorMsg_: _dafny.Seq
        out4_: bool
        out5_: _dafny.Seq
        out4_, out5_ = DafnyLibraries.FileIO.INTERNAL_WriteBytesToFile(path, bytes)
        d_180_isError_ = out4_
        d_181_errorMsg_ = out5_
        res = (Wrappers.Result_Failure(d_181_errorMsg_) if d_180_isError_ else Wrappers.Result_Success(()))
        return res
        return res

