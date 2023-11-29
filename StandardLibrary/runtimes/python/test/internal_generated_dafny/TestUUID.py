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
import String
import StandardLibrary
import UUID

# assert "TestUUID" == __name__
TestUUID = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFromBytesSuccess():
        d_0_fromBytes_: _dafny.Seq
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1_valueOrError0_ = UUID.default__.FromByteArray((TestUUID.default__).byteUuid)
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(23,18): " + _dafny.string_of(d_1_valueOrError0_))
        d_0_fromBytes_ = (d_1_valueOrError0_).Extract()
        if not((d_0_fromBytes_) == ((TestUUID.default__).uuid)):
            raise _dafny.HaltException("test/UUID.dfy(24,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestFromBytesFailure():
        d_2_fromBytes_: _dafny.Seq
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_3_valueOrError0_ = UUID.default__.FromByteArray((TestUUID.default__).wrongByteUuid)
        if not(not((d_3_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(28,18): " + _dafny.string_of(d_3_valueOrError0_))
        d_2_fromBytes_ = (d_3_valueOrError0_).Extract()
        if not((d_2_fromBytes_) != ((TestUUID.default__).uuid)):
            raise _dafny.HaltException("test/UUID.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesSuccess():
        d_4_toBytes_: _dafny.Seq
        d_5_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_5_valueOrError0_ = UUID.default__.ToByteArray((TestUUID.default__).uuid)
        if not(not((d_5_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(33,16): " + _dafny.string_of(d_5_valueOrError0_))
        d_4_toBytes_ = (d_5_valueOrError0_).Extract()
        if not((d_4_toBytes_) == ((TestUUID.default__).byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestToBytesFailure():
        d_6_toBytes_: _dafny.Seq
        d_7_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_7_valueOrError0_ = UUID.default__.ToByteArray((TestUUID.default__).uuid)
        if not(not((d_7_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(38,16): " + _dafny.string_of(d_7_valueOrError0_))
        d_6_toBytes_ = (d_7_valueOrError0_).Extract()
        if not((d_6_toBytes_) != ((TestUUID.default__).wrongByteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripStringConversion():
        d_8_stringToBytes_: _dafny.Seq
        d_9_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_9_valueOrError0_ = UUID.default__.ToByteArray((TestUUID.default__).uuid)
        if not(not((d_9_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(43,22): " + _dafny.string_of(d_9_valueOrError0_))
        d_8_stringToBytes_ = (d_9_valueOrError0_).Extract()
        if not((len(d_8_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_10_bytesToString_: _dafny.Seq
        d_11_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_11_valueOrError1_ = UUID.default__.FromByteArray(d_8_stringToBytes_)
        if not(not((d_11_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(45,22): " + _dafny.string_of(d_11_valueOrError1_))
        d_10_bytesToString_ = (d_11_valueOrError1_).Extract()
        if not((d_10_bytesToString_) == ((TestUUID.default__).uuid)):
            raise _dafny.HaltException("test/UUID.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundTripByteConversion():
        d_12_bytesToString_: _dafny.Seq
        d_13_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_13_valueOrError0_ = UUID.default__.FromByteArray((TestUUID.default__).byteUuid)
        if not(not((d_13_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(50,22): " + _dafny.string_of(d_13_valueOrError0_))
        d_12_bytesToString_ = (d_13_valueOrError0_).Extract()
        d_14_stringToBytes_: _dafny.Seq
        d_15_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_15_valueOrError1_ = UUID.default__.ToByteArray(d_12_bytesToString_)
        if not(not((d_15_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(51,22): " + _dafny.string_of(d_15_valueOrError1_))
        d_14_stringToBytes_ = (d_15_valueOrError1_).Extract()
        if not((len(d_14_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(52,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_14_stringToBytes_) == ((TestUUID.default__).byteUuid)):
            raise _dafny.HaltException("test/UUID.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGenerateAndConversion():
        d_16_uuidString_: _dafny.Seq
        d_17_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = UUID.default__.GenerateUUID()
        d_17_valueOrError0_ = out0_
        if not(not((d_17_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(57,19): " + _dafny.string_of(d_17_valueOrError0_))
        d_16_uuidString_ = (d_17_valueOrError0_).Extract()
        d_18_uuidBytes_: _dafny.Seq
        d_19_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_19_valueOrError1_ = UUID.default__.ToByteArray(d_16_uuidString_)
        if not(not((d_19_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(58,18): " + _dafny.string_of(d_19_valueOrError1_))
        d_18_uuidBytes_ = (d_19_valueOrError1_).Extract()
        d_20_bytesToString_: _dafny.Seq
        d_21_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_21_valueOrError2_ = UUID.default__.FromByteArray(d_18_uuidBytes_)
        if not(not((d_21_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(60,22): " + _dafny.string_of(d_21_valueOrError2_))
        d_20_bytesToString_ = (d_21_valueOrError2_).Extract()
        d_22_stringToBytes_: _dafny.Seq
        d_23_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_23_valueOrError3_ = UUID.default__.ToByteArray(d_20_bytesToString_)
        if not(not((d_23_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(61,22): " + _dafny.string_of(d_23_valueOrError3_))
        d_22_stringToBytes_ = (d_23_valueOrError3_).Extract()
        if not((len(d_22_stringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_22_stringToBytes_) == (d_18_uuidBytes_)):
            raise _dafny.HaltException("test/UUID.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_24_uuidStringToBytes_: _dafny.Seq
        d_25_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_25_valueOrError4_ = UUID.default__.ToByteArray(d_16_uuidString_)
        if not(not((d_25_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(65,26): " + _dafny.string_of(d_25_valueOrError4_))
        d_24_uuidStringToBytes_ = (d_25_valueOrError4_).Extract()
        if not((len(d_24_uuidStringToBytes_)) == (16)):
            raise _dafny.HaltException("test/UUID.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_26_uuidBytesToString_: _dafny.Seq
        d_27_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_27_valueOrError5_ = UUID.default__.FromByteArray(d_24_uuidStringToBytes_)
        if not(not((d_27_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UUID.dfy(67,26): " + _dafny.string_of(d_27_valueOrError5_))
        d_26_uuidBytesToString_ = (d_27_valueOrError5_).Extract()
        if not((d_26_uuidBytesToString_) == (d_16_uuidString_)):
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
