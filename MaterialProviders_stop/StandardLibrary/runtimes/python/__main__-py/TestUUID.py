import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import StandardLibrary
import UTF8
import TestUTF8
import Time
import TestTime
import HexStrings
import TestHexStrings
import Relations
import Seq_mMergeSort
import Math
import Seq
import SortedSets
import TestSeqReaderReadElements
import Functions
import Sets
import FloatCompare
import FloatCompareTest
import ConcurrentCall
import TestCallMany
import UUID

assert "TestUUID" == __name__
TestUUID = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFromBytesSuccess():
        d_242_fromBytes_: _dafny.Seq
        d_243_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_243_valueOrError0_ = UUID.default__.FromByteArray((TestUUID.default__).byteUuid)
        if not(not((d_243_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(23,18): " + _dafny.string_of(d_243_valueOrError0_))
        d_242_fromBytes_ = (d_243_valueOrError0_).Extract()
        if not((d_242_fromBytes_) == ((TestUUID.default__).uuid)):
            raise _dafny.HaltException("test/UUID.dfy(24,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestFromBytesFailure():
        d_244_fromBytes_: _dafny.Seq
        d_245_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_245_valueOrError0_ = UUID.default__.FromByteArray((TestUUID.default__).wrongByteUuid)
        if not(not((d_245_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(28,18): " + _dafny.string_of(d_245_valueOrError0_))
        d_244_fromBytes_ = (d_245_valueOrError0_).Extract()
        if not((d_244_fromBytes_) != ((TestUUID.default__).uuid)):
            raise _dafny.HaltException("test/UUID.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesSuccess():
        d_246_toBytes_: _dafny.Seq
        d_247_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_247_valueOrError0_ = UUID.default__.ToByteArray((TestUUID.default__).uuid)
        if not(not((d_247_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(33,16): " + _dafny.string_of(d_247_valueOrError0_))
        d_246_toBytes_ = (d_247_valueOrError0_).Extract()
        if not((d_246_toBytes_) == ((TestUUID.default__).byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesFailure():
        d_248_toBytes_: _dafny.Seq
        d_249_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_249_valueOrError0_ = UUID.default__.ToByteArray((TestUUID.default__).uuid)
        if not(not((d_249_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(38,16): " + _dafny.string_of(d_249_valueOrError0_))
        d_248_toBytes_ = (d_249_valueOrError0_).Extract()
        if not((d_248_toBytes_) != ((TestUUID.default__).wrongByteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripStringConversion():
        d_250_stringToBytes_: _dafny.Seq
        d_251_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_251_valueOrError0_ = UUID.default__.ToByteArray((TestUUID.default__).uuid)
        if not(not((d_251_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(43,22): " + _dafny.string_of(d_251_valueOrError0_))
        d_250_stringToBytes_ = (d_251_valueOrError0_).Extract()
        if not((len(d_250_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_252_bytesToString_: _dafny.Seq
        d_253_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_253_valueOrError1_ = UUID.default__.FromByteArray(d_250_stringToBytes_)
        if not(not((d_253_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(45,22): " + _dafny.string_of(d_253_valueOrError1_))
        d_252_bytesToString_ = (d_253_valueOrError1_).Extract()
        if not((d_252_bytesToString_) == ((TestUUID.default__).uuid)):
            raise _dafny.HaltException("test/UUID.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripByteConversion():
        d_254_bytesToString_: _dafny.Seq
        d_255_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_255_valueOrError0_ = UUID.default__.FromByteArray((TestUUID.default__).byteUuid)
        if not(not((d_255_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(50,22): " + _dafny.string_of(d_255_valueOrError0_))
        d_254_bytesToString_ = (d_255_valueOrError0_).Extract()
        d_256_stringToBytes_: _dafny.Seq
        d_257_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_257_valueOrError1_ = UUID.default__.ToByteArray(d_254_bytesToString_)
        if not(not((d_257_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(51,22): " + _dafny.string_of(d_257_valueOrError1_))
        d_256_stringToBytes_ = (d_257_valueOrError1_).Extract()
        if not((len(d_256_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(52,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_256_stringToBytes_) == ((TestUUID.default__).byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGenerateAndConversion():
        d_258_uuidString_: _dafny.Seq
        d_259_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out12_: Wrappers.Result
        out12_ = UUID.default__.GenerateUUID()
        d_259_valueOrError0_ = out12_
        if not(not((d_259_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(57,19): " + _dafny.string_of(d_259_valueOrError0_))
        d_258_uuidString_ = (d_259_valueOrError0_).Extract()
        d_260_uuidBytes_: _dafny.Seq
        d_261_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_261_valueOrError1_ = UUID.default__.ToByteArray(d_258_uuidString_)
        if not(not((d_261_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(58,18): " + _dafny.string_of(d_261_valueOrError1_))
        d_260_uuidBytes_ = (d_261_valueOrError1_).Extract()
        d_262_bytesToString_: _dafny.Seq
        d_263_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_263_valueOrError2_ = UUID.default__.FromByteArray(d_260_uuidBytes_)
        if not(not((d_263_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(60,22): " + _dafny.string_of(d_263_valueOrError2_))
        d_262_bytesToString_ = (d_263_valueOrError2_).Extract()
        d_264_stringToBytes_: _dafny.Seq
        d_265_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_265_valueOrError3_ = UUID.default__.ToByteArray(d_262_bytesToString_)
        if not(not((d_265_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(61,22): " + _dafny.string_of(d_265_valueOrError3_))
        d_264_stringToBytes_ = (d_265_valueOrError3_).Extract()
        if not((len(d_264_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_264_stringToBytes_) == (d_260_uuidBytes_)):
            raise _dafny.HaltException("test/UUID.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_266_uuidStringToBytes_: _dafny.Seq
        d_267_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_267_valueOrError4_ = UUID.default__.ToByteArray(d_258_uuidString_)
        if not(not((d_267_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(65,26): " + _dafny.string_of(d_267_valueOrError4_))
        d_266_uuidStringToBytes_ = (d_267_valueOrError4_).Extract()
        if not((len(d_266_uuidStringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_268_uuidBytesToString_: _dafny.Seq
        d_269_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_269_valueOrError5_ = UUID.default__.FromByteArray(d_266_uuidStringToBytes_)
        if not(not((d_269_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(67,26): " + _dafny.string_of(d_269_valueOrError5_))
        d_268_uuidBytesToString_ = (d_269_valueOrError5_).Extract()
        if not((d_268_uuidBytesToString_) == (d_258_uuidString_)):
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
