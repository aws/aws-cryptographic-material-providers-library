import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
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
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import TestUTF8 as TestUTF8
import TestTime as TestTime
import TestComputeSetToOrderedSequenceCharLess as TestComputeSetToOrderedSequenceCharLess
import Sets as Sets
import TestHexStrings as TestHexStrings
import FloatCompareTest as FloatCompareTest
import TestCallMany as TestCallMany
import GetOptTest as GetOptTest

# Module: TestUUID

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFromBytesSuccess():
        d_175_fromBytes_: _dafny.Seq
        d_176_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_176_valueOrError0_ = UUID.default__.FromByteArray(default__.byteUuid)
        if not(not((d_176_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(23,21): " + _dafny.string_of(d_176_valueOrError0_))
        d_175_fromBytes_ = (d_176_valueOrError0_).Extract()
        if not((d_175_fromBytes_) == (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(24,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestFromBytesFailure():
        d_177_fromBytes_: _dafny.Seq
        d_178_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_178_valueOrError0_ = UUID.default__.FromByteArray(default__.wrongByteUuid)
        if not(not((d_178_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(28,21): " + _dafny.string_of(d_178_valueOrError0_))
        d_177_fromBytes_ = (d_178_valueOrError0_).Extract()
        if not((d_177_fromBytes_) != (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesSuccess():
        d_179_toBytes_: _dafny.Seq
        d_180_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_180_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_180_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(33,19): " + _dafny.string_of(d_180_valueOrError0_))
        d_179_toBytes_ = (d_180_valueOrError0_).Extract()
        if not((d_179_toBytes_) == (default__.byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesFailure():
        d_181_toBytes_: _dafny.Seq
        d_182_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_182_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_182_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(38,19): " + _dafny.string_of(d_182_valueOrError0_))
        d_181_toBytes_ = (d_182_valueOrError0_).Extract()
        if not((d_181_toBytes_) != (default__.wrongByteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripStringConversion():
        d_183_stringToBytes_: _dafny.Seq
        d_184_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_184_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_184_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(43,25): " + _dafny.string_of(d_184_valueOrError0_))
        d_183_stringToBytes_ = (d_184_valueOrError0_).Extract()
        if not((len(d_183_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_185_bytesToString_: _dafny.Seq
        d_186_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_186_valueOrError1_ = UUID.default__.FromByteArray(d_183_stringToBytes_)
        if not(not((d_186_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(45,25): " + _dafny.string_of(d_186_valueOrError1_))
        d_185_bytesToString_ = (d_186_valueOrError1_).Extract()
        if not((d_185_bytesToString_) == (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripByteConversion():
        d_187_bytesToString_: _dafny.Seq
        d_188_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_188_valueOrError0_ = UUID.default__.FromByteArray(default__.byteUuid)
        if not(not((d_188_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(50,25): " + _dafny.string_of(d_188_valueOrError0_))
        d_187_bytesToString_ = (d_188_valueOrError0_).Extract()
        d_189_stringToBytes_: _dafny.Seq
        d_190_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_190_valueOrError1_ = UUID.default__.ToByteArray(d_187_bytesToString_)
        if not(not((d_190_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(51,25): " + _dafny.string_of(d_190_valueOrError1_))
        d_189_stringToBytes_ = (d_190_valueOrError1_).Extract()
        if not((len(d_189_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(52,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_189_stringToBytes_) == (default__.byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGenerateAndConversion():
        d_191_uuidString_: _dafny.Seq
        d_192_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out12_: Wrappers.Result
        out12_ = UUID.default__.GenerateUUID()
        d_192_valueOrError0_ = out12_
        if not(not((d_192_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(57,22): " + _dafny.string_of(d_192_valueOrError0_))
        d_191_uuidString_ = (d_192_valueOrError0_).Extract()
        d_193_uuidBytes_: _dafny.Seq
        d_194_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_194_valueOrError1_ = UUID.default__.ToByteArray(d_191_uuidString_)
        if not(not((d_194_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(58,21): " + _dafny.string_of(d_194_valueOrError1_))
        d_193_uuidBytes_ = (d_194_valueOrError1_).Extract()
        d_195_bytesToString_: _dafny.Seq
        d_196_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_196_valueOrError2_ = UUID.default__.FromByteArray(d_193_uuidBytes_)
        if not(not((d_196_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(60,25): " + _dafny.string_of(d_196_valueOrError2_))
        d_195_bytesToString_ = (d_196_valueOrError2_).Extract()
        d_197_stringToBytes_: _dafny.Seq
        d_198_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_198_valueOrError3_ = UUID.default__.ToByteArray(d_195_bytesToString_)
        if not(not((d_198_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(61,25): " + _dafny.string_of(d_198_valueOrError3_))
        d_197_stringToBytes_ = (d_198_valueOrError3_).Extract()
        if not((len(d_197_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_197_stringToBytes_) == (d_193_uuidBytes_)):
            raise _dafny.HaltException("test/UUID.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_199_uuidStringToBytes_: _dafny.Seq
        d_200_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_200_valueOrError4_ = UUID.default__.ToByteArray(d_191_uuidString_)
        if not(not((d_200_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(65,29): " + _dafny.string_of(d_200_valueOrError4_))
        d_199_uuidStringToBytes_ = (d_200_valueOrError4_).Extract()
        if not((len(d_199_uuidStringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_201_uuidBytesToString_: _dafny.Seq
        d_202_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_202_valueOrError5_ = UUID.default__.FromByteArray(d_199_uuidStringToBytes_)
        if not(not((d_202_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(67,29): " + _dafny.string_of(d_202_valueOrError5_))
        d_201_uuidBytesToString_ = (d_202_valueOrError5_).Extract()
        if not((d_201_uuidBytesToString_) == (d_191_uuidString_)):
            raise _dafny.HaltException("test/UUID.dfy(68,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def byteUuid(instance):
        return _dafny.Seq([146, 56, 38, 88, 183, 160, 77, 151, 156, 73, 206, 228, 230, 114, 163, 179])
    @_dafny.classproperty
    def uuid(instance):
        return _dafny.Seq("92382658-b7a0-4d97-9c49-cee4e672a3b3")
    @_dafny.classproperty
    def wrongByteUuid(instance):
        return _dafny.Seq([146, 56, 38, 88, 183, 160, 77, 151, 156, 73, 206, 228, 230, 114, 163, 178])
