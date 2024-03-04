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
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import TestUTF8
import TestTime
import TestComputeSetToOrderedSequenceCharLess
import Sets
import TestHexStrings
import FloatCompareTest
import TestCallMany
import GetOptTest

# Module: TestUUID

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFromBytesSuccess():
        d_173_fromBytes_: _dafny.Seq
        d_174_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_174_valueOrError0_ = UUID.default__.FromByteArray(default__.byteUuid)
        if not(not((d_174_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(23,18): " + _dafny.string_of(d_174_valueOrError0_))
        d_173_fromBytes_ = (d_174_valueOrError0_).Extract()
        if not((d_173_fromBytes_) == (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(24,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestFromBytesFailure():
        d_175_fromBytes_: _dafny.Seq
        d_176_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_176_valueOrError0_ = UUID.default__.FromByteArray(default__.wrongByteUuid)
        if not(not((d_176_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(28,18): " + _dafny.string_of(d_176_valueOrError0_))
        d_175_fromBytes_ = (d_176_valueOrError0_).Extract()
        if not((d_175_fromBytes_) != (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesSuccess():
        d_177_toBytes_: _dafny.Seq
        d_178_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_178_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_178_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(33,16): " + _dafny.string_of(d_178_valueOrError0_))
        d_177_toBytes_ = (d_178_valueOrError0_).Extract()
        if not((d_177_toBytes_) == (default__.byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesFailure():
        d_179_toBytes_: _dafny.Seq
        d_180_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_180_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_180_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(38,16): " + _dafny.string_of(d_180_valueOrError0_))
        d_179_toBytes_ = (d_180_valueOrError0_).Extract()
        if not((d_179_toBytes_) != (default__.wrongByteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripStringConversion():
        d_181_stringToBytes_: _dafny.Seq
        d_182_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_182_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_182_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(43,22): " + _dafny.string_of(d_182_valueOrError0_))
        d_181_stringToBytes_ = (d_182_valueOrError0_).Extract()
        if not((len(d_181_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_183_bytesToString_: _dafny.Seq
        d_184_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_184_valueOrError1_ = UUID.default__.FromByteArray(d_181_stringToBytes_)
        if not(not((d_184_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(45,22): " + _dafny.string_of(d_184_valueOrError1_))
        d_183_bytesToString_ = (d_184_valueOrError1_).Extract()
        if not((d_183_bytesToString_) == (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripByteConversion():
        d_185_bytesToString_: _dafny.Seq
        d_186_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_186_valueOrError0_ = UUID.default__.FromByteArray(default__.byteUuid)
        if not(not((d_186_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(50,22): " + _dafny.string_of(d_186_valueOrError0_))
        d_185_bytesToString_ = (d_186_valueOrError0_).Extract()
        d_187_stringToBytes_: _dafny.Seq
        d_188_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_188_valueOrError1_ = UUID.default__.ToByteArray(d_185_bytesToString_)
        if not(not((d_188_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(51,22): " + _dafny.string_of(d_188_valueOrError1_))
        d_187_stringToBytes_ = (d_188_valueOrError1_).Extract()
        if not((len(d_187_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(52,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_187_stringToBytes_) == (default__.byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGenerateAndConversion():
        d_189_uuidString_: _dafny.Seq
        d_190_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out11_: Wrappers.Result
        out11_ = UUID.default__.GenerateUUID()
        d_190_valueOrError0_ = out11_
        if not(not((d_190_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(57,19): " + _dafny.string_of(d_190_valueOrError0_))
        d_189_uuidString_ = (d_190_valueOrError0_).Extract()
        d_191_uuidBytes_: _dafny.Seq
        d_192_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_192_valueOrError1_ = UUID.default__.ToByteArray(d_189_uuidString_)
        if not(not((d_192_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(58,18): " + _dafny.string_of(d_192_valueOrError1_))
        d_191_uuidBytes_ = (d_192_valueOrError1_).Extract()
        d_193_bytesToString_: _dafny.Seq
        d_194_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_194_valueOrError2_ = UUID.default__.FromByteArray(d_191_uuidBytes_)
        if not(not((d_194_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(60,22): " + _dafny.string_of(d_194_valueOrError2_))
        d_193_bytesToString_ = (d_194_valueOrError2_).Extract()
        d_195_stringToBytes_: _dafny.Seq
        d_196_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_196_valueOrError3_ = UUID.default__.ToByteArray(d_193_bytesToString_)
        if not(not((d_196_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(61,22): " + _dafny.string_of(d_196_valueOrError3_))
        d_195_stringToBytes_ = (d_196_valueOrError3_).Extract()
        if not((len(d_195_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_195_stringToBytes_) == (d_191_uuidBytes_)):
            raise _dafny.HaltException("test/UUID.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_197_uuidStringToBytes_: _dafny.Seq
        d_198_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_198_valueOrError4_ = UUID.default__.ToByteArray(d_189_uuidString_)
        if not(not((d_198_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(65,26): " + _dafny.string_of(d_198_valueOrError4_))
        d_197_uuidStringToBytes_ = (d_198_valueOrError4_).Extract()
        if not((len(d_197_uuidStringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_199_uuidBytesToString_: _dafny.Seq
        d_200_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_200_valueOrError5_ = UUID.default__.FromByteArray(d_197_uuidStringToBytes_)
        if not(not((d_200_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(67,26): " + _dafny.string_of(d_200_valueOrError5_))
        d_199_uuidBytesToString_ = (d_200_valueOrError5_).Extract()
        if not((d_199_uuidBytesToString_) == (d_189_uuidString_)):
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
