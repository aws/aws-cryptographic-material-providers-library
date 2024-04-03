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

# Module: TestUTF8

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestEncodeHappyCase():
        d_0_unicodeString_: _dafny.Seq
        d_0_unicodeString_ = _dafny.Seq("abc\u0306\u01FD\u03B2")
        d_1_expectedBytes_: _dafny.Seq
        d_1_expectedBytes_ = _dafny.Seq([97, 98, 99, 204, 134, 199, 189, 206, 178])
        d_2_encoded_: _dafny.Seq
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_3_valueOrError0_ = UTF8.default__.Encode(d_0_unicodeString_)
        if not(not((d_3_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(14,19): " + _dafny.string_of(d_3_valueOrError0_))
        d_2_encoded_ = (d_3_valueOrError0_).Extract()
        if not((d_1_expectedBytes_) == (d_2_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(15,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestEncodeInvalidUnicode():
        d_4_invalidUnicode_: _dafny.Seq
        d_4_invalidUnicode_ = _dafny.Seq("abc\uD800")
        d_5_encoded_: Wrappers.Result
        d_5_encoded_ = UTF8.default__.Encode(d_4_invalidUnicode_)
        if not((d_5_encoded_).is_Failure):
            raise _dafny.HaltException("test/UTF8.dfy(22,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDecodeHappyCase():
        d_6_unicodeBytes_: _dafny.Seq
        d_6_unicodeBytes_ = _dafny.Seq([97, 98, 99, 204, 134, 199, 189, 206, 178])
        d_7_expectedString_: _dafny.Seq
        d_7_expectedString_ = _dafny.Seq("abc\u0306\u01FD\u03B2")
        d_8_decoded_: _dafny.Seq
        d_9_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_9_valueOrError0_ = UTF8.default__.Decode(d_6_unicodeBytes_)
        if not(not((d_9_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(32,19): " + _dafny.string_of(d_9_valueOrError0_))
        d_8_decoded_ = (d_9_valueOrError0_).Extract()
        if not((d_7_expectedString_) == (d_8_decoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDecodeInvalidUnicode():
        d_10_invalidUnicode_: _dafny.Seq
        d_10_invalidUnicode_ = _dafny.Seq([97, 98, 99, 237, 160, 128])
        if not(not(UTF8.default__.ValidUTF8Seq(d_10_invalidUnicode_))):
            raise _dafny.HaltException("test/UTF8.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((UTF8.default__.Decode(d_10_invalidUnicode_)).is_Failure):
            raise _dafny.HaltException("test/UTF8.dfy(40,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test1Byte():
        d_11_decoded_: _dafny.Seq
        d_11_decoded_ = _dafny.Seq("\u0000")
        d_12_encoded_: _dafny.Seq
        d_13_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_13_valueOrError0_ = UTF8.default__.Encode(d_11_decoded_)
        if not(not((d_13_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(46,19): " + _dafny.string_of(d_13_valueOrError0_))
        d_12_encoded_ = (d_13_valueOrError0_).Extract()
        if not((_dafny.Seq([0])) == (d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_14_redecoded_: _dafny.Seq
        d_15_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_15_valueOrError1_ = UTF8.default__.Decode(d_12_encoded_)
        if not(not((d_15_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(49,21): " + _dafny.string_of(d_15_valueOrError1_))
        d_14_redecoded_ = (d_15_valueOrError1_).Extract()
        if not((d_11_decoded_) == (d_14_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(50,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_11_decoded_ = _dafny.Seq("\u0020")
        d_16_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_16_valueOrError2_ = UTF8.default__.Encode(d_11_decoded_)
        if not(not((d_16_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(54,15): " + _dafny.string_of(d_16_valueOrError2_))
        d_12_encoded_ = (d_16_valueOrError2_).Extract()
        if not((_dafny.Seq([32])) == (d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(55,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_17_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_17_valueOrError3_ = UTF8.default__.Decode(d_12_encoded_)
        if not(not((d_17_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(57,17): " + _dafny.string_of(d_17_valueOrError3_))
        d_14_redecoded_ = (d_17_valueOrError3_).Extract()
        if not((d_11_decoded_) == (d_14_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_11_decoded_ = _dafny.Seq("$")
        d_18_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_18_valueOrError4_ = UTF8.default__.Encode(d_11_decoded_)
        if not(not((d_18_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(61,15): " + _dafny.string_of(d_18_valueOrError4_))
        d_12_encoded_ = (d_18_valueOrError4_).Extract()
        if not((_dafny.Seq([36])) == (d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_19_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_19_valueOrError5_ = UTF8.default__.Decode(d_12_encoded_)
        if not(not((d_19_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(64,17): " + _dafny.string_of(d_19_valueOrError5_))
        d_14_redecoded_ = (d_19_valueOrError5_).Extract()
        if not((d_11_decoded_) == (d_14_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_11_decoded_ = _dafny.Seq("0")
        d_20_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_20_valueOrError6_ = UTF8.default__.Encode(d_11_decoded_)
        if not(not((d_20_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(68,15): " + _dafny.string_of(d_20_valueOrError6_))
        d_12_encoded_ = (d_20_valueOrError6_).Extract()
        if not((_dafny.Seq([48])) == (d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_21_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_21_valueOrError7_ = UTF8.default__.Decode(d_12_encoded_)
        if not(not((d_21_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(71,17): " + _dafny.string_of(d_21_valueOrError7_))
        d_14_redecoded_ = (d_21_valueOrError7_).Extract()
        if not((d_11_decoded_) == (d_14_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_11_decoded_ = _dafny.Seq("A")
        d_22_valueOrError8_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_22_valueOrError8_ = UTF8.default__.Encode(d_11_decoded_)
        if not(not((d_22_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(75,15): " + _dafny.string_of(d_22_valueOrError8_))
        d_12_encoded_ = (d_22_valueOrError8_).Extract()
        if not((_dafny.Seq([65])) == (d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(77,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_23_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_23_valueOrError9_ = UTF8.default__.Decode(d_12_encoded_)
        if not(not((d_23_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(78,17): " + _dafny.string_of(d_23_valueOrError9_))
        d_14_redecoded_ = (d_23_valueOrError9_).Extract()
        if not((d_11_decoded_) == (d_14_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(79,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_11_decoded_ = _dafny.Seq("a")
        d_24_valueOrError10_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_24_valueOrError10_ = UTF8.default__.Encode(d_11_decoded_)
        if not(not((d_24_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(82,15): " + _dafny.string_of(d_24_valueOrError10_))
        d_12_encoded_ = (d_24_valueOrError10_).Extract()
        if not((_dafny.Seq([97])) == (d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(83,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_12_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(84,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_25_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_25_valueOrError11_ = UTF8.default__.Decode(d_12_encoded_)
        if not(not((d_25_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(85,17): " + _dafny.string_of(d_25_valueOrError11_))
        d_14_redecoded_ = (d_25_valueOrError11_).Extract()
        if not((d_11_decoded_) == (d_14_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test2Bytes():
        d_26_decoded_: _dafny.Seq
        d_26_decoded_ = _dafny.Seq("\u00A3")
        d_27_encoded_: _dafny.Seq
        d_28_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_28_valueOrError0_ = UTF8.default__.Encode(d_26_decoded_)
        if not(not((d_28_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(92,19): " + _dafny.string_of(d_28_valueOrError0_))
        d_27_encoded_ = (d_28_valueOrError0_).Extract()
        if not((_dafny.Seq([194, 163])) == (d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(93,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(94,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_29_redecoded_: _dafny.Seq
        d_30_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_30_valueOrError1_ = UTF8.default__.Decode(d_27_encoded_)
        if not(not((d_30_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(95,21): " + _dafny.string_of(d_30_valueOrError1_))
        d_29_redecoded_ = (d_30_valueOrError1_).Extract()
        if not((d_26_decoded_) == (d_29_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(96,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_26_decoded_ = _dafny.Seq("\u00A9")
        d_31_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_31_valueOrError2_ = UTF8.default__.Encode(d_26_decoded_)
        if not(not((d_31_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(100,15): " + _dafny.string_of(d_31_valueOrError2_))
        d_27_encoded_ = (d_31_valueOrError2_).Extract()
        if not((_dafny.Seq([194, 169])) == (d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_32_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_32_valueOrError3_ = UTF8.default__.Decode(d_27_encoded_)
        if not(not((d_32_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(103,17): " + _dafny.string_of(d_32_valueOrError3_))
        d_29_redecoded_ = (d_32_valueOrError3_).Extract()
        if not((d_26_decoded_) == (d_29_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_26_decoded_ = _dafny.Seq("\u00AE")
        d_33_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_33_valueOrError4_ = UTF8.default__.Encode(d_26_decoded_)
        if not(not((d_33_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(108,15): " + _dafny.string_of(d_33_valueOrError4_))
        d_27_encoded_ = (d_33_valueOrError4_).Extract()
        if not((_dafny.Seq([194, 174])) == (d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(109,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_34_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_34_valueOrError5_ = UTF8.default__.Decode(d_27_encoded_)
        if not(not((d_34_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(111,17): " + _dafny.string_of(d_34_valueOrError5_))
        d_29_redecoded_ = (d_34_valueOrError5_).Extract()
        if not((d_26_decoded_) == (d_29_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_26_decoded_ = _dafny.Seq("\u03C0")
        d_35_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_35_valueOrError6_ = UTF8.default__.Encode(d_26_decoded_)
        if not(not((d_35_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(116,15): " + _dafny.string_of(d_35_valueOrError6_))
        d_27_encoded_ = (d_35_valueOrError6_).Extract()
        if not((_dafny.Seq([207, 128])) == (d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(117,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_27_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_36_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_36_valueOrError7_ = UTF8.default__.Decode(d_27_encoded_)
        if not(not((d_36_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(119,17): " + _dafny.string_of(d_36_valueOrError7_))
        d_29_redecoded_ = (d_36_valueOrError7_).Extract()
        if not((d_26_decoded_) == (d_29_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(120,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test3Bytes():
        d_37_decoded_: _dafny.Seq
        d_37_decoded_ = _dafny.Seq("\u2386")
        d_38_encoded_: _dafny.Seq
        d_39_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_39_valueOrError0_ = UTF8.default__.Encode(d_37_decoded_)
        if not(not((d_39_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(126,19): " + _dafny.string_of(d_39_valueOrError0_))
        d_38_encoded_ = (d_39_valueOrError0_).Extract()
        if not((_dafny.Seq([226, 142, 134])) == (d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(127,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_40_redecoded_: _dafny.Seq
        d_41_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_41_valueOrError1_ = UTF8.default__.Decode(d_38_encoded_)
        if not(not((d_41_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(129,21): " + _dafny.string_of(d_41_valueOrError1_))
        d_40_redecoded_ = (d_41_valueOrError1_).Extract()
        if not((d_37_decoded_) == (d_40_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_37_decoded_ = _dafny.Seq("\u2387")
        d_42_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_42_valueOrError2_ = UTF8.default__.Encode(d_37_decoded_)
        if not(not((d_42_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(134,15): " + _dafny.string_of(d_42_valueOrError2_))
        d_38_encoded_ = (d_42_valueOrError2_).Extract()
        if not((_dafny.Seq([226, 142, 135])) == (d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(135,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_43_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_43_valueOrError3_ = UTF8.default__.Decode(d_38_encoded_)
        if not(not((d_43_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(137,17): " + _dafny.string_of(d_43_valueOrError3_))
        d_40_redecoded_ = (d_43_valueOrError3_).Extract()
        if not((d_37_decoded_) == (d_40_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_37_decoded_ = _dafny.Seq("\u231B")
        d_44_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_44_valueOrError4_ = UTF8.default__.Encode(d_37_decoded_)
        if not(not((d_44_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(142,15): " + _dafny.string_of(d_44_valueOrError4_))
        d_38_encoded_ = (d_44_valueOrError4_).Extract()
        if not((_dafny.Seq([226, 140, 155])) == (d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(143,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(144,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_45_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_45_valueOrError5_ = UTF8.default__.Decode(d_38_encoded_)
        if not(not((d_45_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(145,17): " + _dafny.string_of(d_45_valueOrError5_))
        d_40_redecoded_ = (d_45_valueOrError5_).Extract()
        if not((d_37_decoded_) == (d_40_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_37_decoded_ = _dafny.Seq("\u1D78")
        d_46_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_46_valueOrError6_ = UTF8.default__.Encode(d_37_decoded_)
        if not(not((d_46_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(150,15): " + _dafny.string_of(d_46_valueOrError6_))
        d_38_encoded_ = (d_46_valueOrError6_).Extract()
        if not((_dafny.Seq([225, 181, 184])) == (d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(151,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_47_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_47_valueOrError7_ = UTF8.default__.Decode(d_38_encoded_)
        if not(not((d_47_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(153,17): " + _dafny.string_of(d_47_valueOrError7_))
        d_40_redecoded_ = (d_47_valueOrError7_).Extract()
        if not((d_37_decoded_) == (d_40_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(154,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_37_decoded_ = _dafny.Seq("\u732B")
        d_48_valueOrError8_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_48_valueOrError8_ = UTF8.default__.Encode(d_37_decoded_)
        if not(not((d_48_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(158,15): " + _dafny.string_of(d_48_valueOrError8_))
        d_38_encoded_ = (d_48_valueOrError8_).Extract()
        if not((_dafny.Seq([231, 140, 171])) == (d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(159,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_38_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_49_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_49_valueOrError9_ = UTF8.default__.Decode(d_38_encoded_)
        if not(not((d_49_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(161,17): " + _dafny.string_of(d_49_valueOrError9_))
        d_40_redecoded_ = (d_49_valueOrError9_).Extract()
        if not((d_37_decoded_) == (d_40_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(162,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test4Bytes():
        d_50_decoded_: _dafny.Seq
        d_50_decoded_ = _dafny.Seq("\uD808\uDC00")
        d_51_encoded_: _dafny.Seq
        d_52_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_52_valueOrError0_ = UTF8.default__.Encode(d_50_decoded_)
        if not(not((d_52_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(168,19): " + _dafny.string_of(d_52_valueOrError0_))
        d_51_encoded_ = (d_52_valueOrError0_).Extract()
        if not((_dafny.Seq([240, 146, 128, 128])) == (d_51_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(169,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses4Bytes(d_51_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(170,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_53_redecoded_: _dafny.Seq
        d_54_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_54_valueOrError1_ = UTF8.default__.Decode(d_51_encoded_)
        if not(not((d_54_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(171,21): " + _dafny.string_of(d_54_valueOrError1_))
        d_53_redecoded_ = (d_54_valueOrError1_).Extract()
        if not((d_50_decoded_) == (d_53_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_50_decoded_ = _dafny.Seq("\uD835\uDFC1")
        d_55_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_55_valueOrError2_ = UTF8.default__.Encode(d_50_decoded_)
        if not(not((d_55_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(176,15): " + _dafny.string_of(d_55_valueOrError2_))
        d_51_encoded_ = (d_55_valueOrError2_).Extract()
        if not((_dafny.Seq([240, 157, 159, 129])) == (d_51_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses4Bytes(d_51_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(178,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_56_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_56_valueOrError3_ = UTF8.default__.Decode(d_51_encoded_)
        if not(not((d_56_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(179,17): " + _dafny.string_of(d_56_valueOrError3_))
        d_53_redecoded_ = (d_56_valueOrError3_).Extract()
        if not((d_50_decoded_) == (d_53_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(180,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

