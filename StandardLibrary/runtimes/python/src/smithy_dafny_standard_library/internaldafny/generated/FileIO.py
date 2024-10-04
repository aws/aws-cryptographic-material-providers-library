import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings

# Module: FileIO

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ReadBytesFromFile(path):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_isError_: bool
        d_1_bytesRead_: _dafny.Seq
        d_2_errorMsg_: _dafny.Seq
        out0_: bool
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out0_, out1_, out2_ = DafnyLibraries.FileIO.INTERNAL_ReadBytesFromFile(path)
        d_0_isError_ = out0_
        d_1_bytesRead_ = out1_
        d_2_errorMsg_ = out2_
        if d_0_isError_:
            res = Wrappers.Result_Failure(d_2_errorMsg_)
        elif True:
            res = Wrappers.Result_Success(d_1_bytesRead_)
        return res
        return res

    @staticmethod
    def WriteBytesToFile(path, bytes):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_0_isError_: bool
        d_1_errorMsg_: _dafny.Seq
        out0_: bool
        out1_: _dafny.Seq
        out0_, out1_ = DafnyLibraries.FileIO.INTERNAL_WriteBytesToFile(path, bytes)
        d_0_isError_ = out0_
        d_1_errorMsg_ = out1_
        if d_0_isError_:
            res = Wrappers.Result_Failure(d_1_errorMsg_)
        elif True:
            res = Wrappers.Result_Success(())
        return res
        return res

