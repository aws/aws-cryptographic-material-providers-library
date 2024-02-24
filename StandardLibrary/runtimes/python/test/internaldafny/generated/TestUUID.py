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
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import TestUTF8
import TestTime
import TestComputeSetToOrderedSequenceCharLess
import Sets
import TestHexStrings
import FloatCompareTest
import TestCallMany
import GetOpt
import GetOptTest

# Module: TestUUID

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFromBytesSuccess():
        d_258_fromBytes_: _dafny.Seq
        d_259_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_259_valueOrError0_ = UUID.default__.FromByteArray(default__.byteUuid)
        if not(not((d_259_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(23,18): " + _dafny.string_of(d_259_valueOrError0_))
        d_258_fromBytes_ = (d_259_valueOrError0_).Extract()
        if not((d_258_fromBytes_) == (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(24,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestFromBytesFailure():
        d_260_fromBytes_: _dafny.Seq
        d_261_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_261_valueOrError0_ = UUID.default__.FromByteArray(default__.wrongByteUuid)
        if not(not((d_261_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(28,18): " + _dafny.string_of(d_261_valueOrError0_))
        d_260_fromBytes_ = (d_261_valueOrError0_).Extract()
        if not((d_260_fromBytes_) != (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesSuccess():
        d_262_toBytes_: _dafny.Seq
        d_263_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_263_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_263_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(33,16): " + _dafny.string_of(d_263_valueOrError0_))
        d_262_toBytes_ = (d_263_valueOrError0_).Extract()
        if not((d_262_toBytes_) == (default__.byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesFailure():
        d_264_toBytes_: _dafny.Seq
        d_265_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_265_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_265_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(38,16): " + _dafny.string_of(d_265_valueOrError0_))
        d_264_toBytes_ = (d_265_valueOrError0_).Extract()
        if not((d_264_toBytes_) != (default__.wrongByteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripStringConversion():
        d_266_stringToBytes_: _dafny.Seq
        d_267_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_267_valueOrError0_ = UUID.default__.ToByteArray(default__.uuid)
        if not(not((d_267_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(43,22): " + _dafny.string_of(d_267_valueOrError0_))
        d_266_stringToBytes_ = (d_267_valueOrError0_).Extract()
        if not((len(d_266_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_268_bytesToString_: _dafny.Seq
        d_269_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_269_valueOrError1_ = UUID.default__.FromByteArray(d_266_stringToBytes_)
        if not(not((d_269_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(45,22): " + _dafny.string_of(d_269_valueOrError1_))
        d_268_bytesToString_ = (d_269_valueOrError1_).Extract()
        if not((d_268_bytesToString_) == (default__.uuid)):
            raise _dafny.HaltException("test/UUID.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripByteConversion():
        d_270_bytesToString_: _dafny.Seq
        d_271_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_271_valueOrError0_ = UUID.default__.FromByteArray(default__.byteUuid)
        if not(not((d_271_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(50,22): " + _dafny.string_of(d_271_valueOrError0_))
        d_270_bytesToString_ = (d_271_valueOrError0_).Extract()
        d_272_stringToBytes_: _dafny.Seq
        d_273_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_273_valueOrError1_ = UUID.default__.ToByteArray(d_270_bytesToString_)
        if not(not((d_273_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(51,22): " + _dafny.string_of(d_273_valueOrError1_))
        d_272_stringToBytes_ = (d_273_valueOrError1_).Extract()
        if not((len(d_272_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(52,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_272_stringToBytes_) == (default__.byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGenerateAndConversion():
        d_274_uuidString_: _dafny.Seq
        d_275_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out11_: Wrappers.Result
        out11_ = UUID.default__.GenerateUUID()
        d_275_valueOrError0_ = out11_
        if not(not((d_275_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(57,19): " + _dafny.string_of(d_275_valueOrError0_))
        d_274_uuidString_ = (d_275_valueOrError0_).Extract()
        d_276_uuidBytes_: _dafny.Seq
        d_277_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_277_valueOrError1_ = UUID.default__.ToByteArray(d_274_uuidString_)
        if not(not((d_277_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(58,18): " + _dafny.string_of(d_277_valueOrError1_))
        d_276_uuidBytes_ = (d_277_valueOrError1_).Extract()
        d_278_bytesToString_: _dafny.Seq
        d_279_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_279_valueOrError2_ = UUID.default__.FromByteArray(d_276_uuidBytes_)
        if not(not((d_279_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(60,22): " + _dafny.string_of(d_279_valueOrError2_))
        d_278_bytesToString_ = (d_279_valueOrError2_).Extract()
        d_280_stringToBytes_: _dafny.Seq
        d_281_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_281_valueOrError3_ = UUID.default__.ToByteArray(d_278_bytesToString_)
        if not(not((d_281_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(61,22): " + _dafny.string_of(d_281_valueOrError3_))
        d_280_stringToBytes_ = (d_281_valueOrError3_).Extract()
        if not((len(d_280_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_280_stringToBytes_) == (d_276_uuidBytes_)):
            raise _dafny.HaltException("test/UUID.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_282_uuidStringToBytes_: _dafny.Seq
        d_283_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_283_valueOrError4_ = UUID.default__.ToByteArray(d_274_uuidString_)
        if not(not((d_283_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(65,26): " + _dafny.string_of(d_283_valueOrError4_))
        d_282_uuidStringToBytes_ = (d_283_valueOrError4_).Extract()
        if not((len(d_282_uuidStringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_284_uuidBytesToString_: _dafny.Seq
        d_285_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_285_valueOrError5_ = UUID.default__.FromByteArray(d_282_uuidStringToBytes_)
        if not(not((d_285_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(67,26): " + _dafny.string_of(d_285_valueOrError5_))
        d_284_uuidBytesToString_ = (d_285_valueOrError5_).Extract()
        if not((d_284_uuidBytesToString_) == (d_274_uuidString_)):
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
