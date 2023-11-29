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
import TestUUID
import ConcurrentCall
import TestCallMany
import FloatCompare
import FloatCompareTest
import Relations
import Seq_mMergeSort
import Math
import Seq
import SortedSets
import TestSeqReaderReadElements
import HexStrings
import TestHexStrings
import Time
import TestTime
import UTF8

# assert "TestUTF8" == __name__
TestUTF8 = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestEncodeHappyCase():
        d_82_unicodeString_: _dafny.Seq
        d_82_unicodeString_ = _dafny.Seq("abc\u0306\u01FD\u03B2")
        d_83_expectedBytes_: _dafny.Seq
        d_83_expectedBytes_ = _dafny.Seq([97, 98, 99, 204, 134, 199, 189, 206, 178])
        d_84_encoded_: _dafny.Seq
        d_85_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_85_valueOrError0_ = UTF8.default__.Encode(d_82_unicodeString_)
        if not(not((d_85_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(14,16): " + _dafny.string_of(d_85_valueOrError0_))
        d_84_encoded_ = (d_85_valueOrError0_).Extract()
        if not((d_83_expectedBytes_) == (d_84_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(15,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestEncodeInvalidUnicode():
        d_86_invalidUnicode_: _dafny.Seq
        d_86_invalidUnicode_ = _dafny.Seq("abc\uD800")
        d_87_encoded_: Wrappers.Result
        d_87_encoded_ = UTF8.default__.Encode(d_86_invalidUnicode_)
        if not((d_87_encoded_).is_Failure):
            raise _dafny.HaltException("test/UTF8.dfy(22,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDecodeHappyCase():
        d_88_unicodeBytes_: _dafny.Seq
        d_88_unicodeBytes_ = _dafny.Seq([97, 98, 99, 204, 134, 199, 189, 206, 178])
        d_89_expectedString_: _dafny.Seq
        d_89_expectedString_ = _dafny.Seq("abc\u0306\u01FD\u03B2")
        d_90_decoded_: _dafny.Seq
        d_91_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_91_valueOrError0_ = UTF8.default__.Decode(d_88_unicodeBytes_)
        if not(not((d_91_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(32,16): " + _dafny.string_of(d_91_valueOrError0_))
        d_90_decoded_ = (d_91_valueOrError0_).Extract()
        if not((d_89_expectedString_) == (d_90_decoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDecodeInvalidUnicode():
        d_92_invalidUnicode_: _dafny.Seq
        d_92_invalidUnicode_ = _dafny.Seq([97, 98, 99, 237, 160, 128])
        if not(not(UTF8.default__.ValidUTF8Seq(d_92_invalidUnicode_))):
            raise _dafny.HaltException("test/UTF8.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((UTF8.default__.Decode(d_92_invalidUnicode_)).is_Failure):
            raise _dafny.HaltException("test/UTF8.dfy(40,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test1Byte():
        d_93_decoded_: _dafny.Seq
        d_93_decoded_ = _dafny.Seq("\u0000")
        d_94_encoded_: _dafny.Seq
        d_95_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_95_valueOrError0_ = UTF8.default__.Encode(d_93_decoded_)
        if not(not((d_95_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(46,16): " + _dafny.string_of(d_95_valueOrError0_))
        d_94_encoded_ = (d_95_valueOrError0_).Extract()
        if not((_dafny.Seq([0])) == (d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_96_redecoded_: _dafny.Seq
        d_97_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_97_valueOrError1_ = UTF8.default__.Decode(d_94_encoded_)
        if not(not((d_97_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(49,18): " + _dafny.string_of(d_97_valueOrError1_))
        d_96_redecoded_ = (d_97_valueOrError1_).Extract()
        if not((d_93_decoded_) == (d_96_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(50,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_93_decoded_ = _dafny.Seq("\u0020")
        d_98_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_98_valueOrError2_ = UTF8.default__.Encode(d_93_decoded_)
        if not(not((d_98_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(54,12): " + _dafny.string_of(d_98_valueOrError2_))
        d_94_encoded_ = (d_98_valueOrError2_).Extract()
        if not((_dafny.Seq([32])) == (d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(55,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_99_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_99_valueOrError3_ = UTF8.default__.Decode(d_94_encoded_)
        if not(not((d_99_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(57,14): " + _dafny.string_of(d_99_valueOrError3_))
        d_96_redecoded_ = (d_99_valueOrError3_).Extract()
        if not((d_93_decoded_) == (d_96_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_93_decoded_ = _dafny.Seq("$")
        d_100_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_100_valueOrError4_ = UTF8.default__.Encode(d_93_decoded_)
        if not(not((d_100_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(61,12): " + _dafny.string_of(d_100_valueOrError4_))
        d_94_encoded_ = (d_100_valueOrError4_).Extract()
        if not((_dafny.Seq([36])) == (d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_101_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_101_valueOrError5_ = UTF8.default__.Decode(d_94_encoded_)
        if not(not((d_101_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(64,14): " + _dafny.string_of(d_101_valueOrError5_))
        d_96_redecoded_ = (d_101_valueOrError5_).Extract()
        if not((d_93_decoded_) == (d_96_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_93_decoded_ = _dafny.Seq("0")
        d_102_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_102_valueOrError6_ = UTF8.default__.Encode(d_93_decoded_)
        if not(not((d_102_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(68,12): " + _dafny.string_of(d_102_valueOrError6_))
        d_94_encoded_ = (d_102_valueOrError6_).Extract()
        if not((_dafny.Seq([48])) == (d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_103_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_103_valueOrError7_ = UTF8.default__.Decode(d_94_encoded_)
        if not(not((d_103_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(71,14): " + _dafny.string_of(d_103_valueOrError7_))
        d_96_redecoded_ = (d_103_valueOrError7_).Extract()
        if not((d_93_decoded_) == (d_96_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_93_decoded_ = _dafny.Seq("A")
        d_104_valueOrError8_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_104_valueOrError8_ = UTF8.default__.Encode(d_93_decoded_)
        if not(not((d_104_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(75,12): " + _dafny.string_of(d_104_valueOrError8_))
        d_94_encoded_ = (d_104_valueOrError8_).Extract()
        if not((_dafny.Seq([65])) == (d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(77,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_105_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_105_valueOrError9_ = UTF8.default__.Decode(d_94_encoded_)
        if not(not((d_105_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(78,14): " + _dafny.string_of(d_105_valueOrError9_))
        d_96_redecoded_ = (d_105_valueOrError9_).Extract()
        if not((d_93_decoded_) == (d_96_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(79,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_93_decoded_ = _dafny.Seq("a")
        d_106_valueOrError10_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_106_valueOrError10_ = UTF8.default__.Encode(d_93_decoded_)
        if not(not((d_106_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(82,12): " + _dafny.string_of(d_106_valueOrError10_))
        d_94_encoded_ = (d_106_valueOrError10_).Extract()
        if not((_dafny.Seq([97])) == (d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(83,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_94_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(84,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_107_valueOrError11_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_107_valueOrError11_ = UTF8.default__.Decode(d_94_encoded_)
        if not(not((d_107_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(85,14): " + _dafny.string_of(d_107_valueOrError11_))
        d_96_redecoded_ = (d_107_valueOrError11_).Extract()
        if not((d_93_decoded_) == (d_96_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test2Bytes():
        d_108_decoded_: _dafny.Seq
        d_108_decoded_ = _dafny.Seq("\u00A3")
        d_109_encoded_: _dafny.Seq
        d_110_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_110_valueOrError0_ = UTF8.default__.Encode(d_108_decoded_)
        if not(not((d_110_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(92,16): " + _dafny.string_of(d_110_valueOrError0_))
        d_109_encoded_ = (d_110_valueOrError0_).Extract()
        if not((_dafny.Seq([194, 163])) == (d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(93,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(94,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_111_redecoded_: _dafny.Seq
        d_112_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_112_valueOrError1_ = UTF8.default__.Decode(d_109_encoded_)
        if not(not((d_112_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(95,18): " + _dafny.string_of(d_112_valueOrError1_))
        d_111_redecoded_ = (d_112_valueOrError1_).Extract()
        if not((d_108_decoded_) == (d_111_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(96,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_108_decoded_ = _dafny.Seq("\u00A9")
        d_113_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_113_valueOrError2_ = UTF8.default__.Encode(d_108_decoded_)
        if not(not((d_113_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(100,12): " + _dafny.string_of(d_113_valueOrError2_))
        d_109_encoded_ = (d_113_valueOrError2_).Extract()
        if not((_dafny.Seq([194, 169])) == (d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_114_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_114_valueOrError3_ = UTF8.default__.Decode(d_109_encoded_)
        if not(not((d_114_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(103,14): " + _dafny.string_of(d_114_valueOrError3_))
        d_111_redecoded_ = (d_114_valueOrError3_).Extract()
        if not((d_108_decoded_) == (d_111_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_108_decoded_ = _dafny.Seq("\u00AE")
        d_115_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_115_valueOrError4_ = UTF8.default__.Encode(d_108_decoded_)
        if not(not((d_115_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(108,12): " + _dafny.string_of(d_115_valueOrError4_))
        d_109_encoded_ = (d_115_valueOrError4_).Extract()
        if not((_dafny.Seq([194, 174])) == (d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(109,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_116_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_116_valueOrError5_ = UTF8.default__.Decode(d_109_encoded_)
        if not(not((d_116_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(111,14): " + _dafny.string_of(d_116_valueOrError5_))
        d_111_redecoded_ = (d_116_valueOrError5_).Extract()
        if not((d_108_decoded_) == (d_111_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_108_decoded_ = _dafny.Seq("\u03C0")
        d_117_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_117_valueOrError6_ = UTF8.default__.Encode(d_108_decoded_)
        if not(not((d_117_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(116,12): " + _dafny.string_of(d_117_valueOrError6_))
        d_109_encoded_ = (d_117_valueOrError6_).Extract()
        if not((_dafny.Seq([207, 128])) == (d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(117,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_109_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_118_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_118_valueOrError7_ = UTF8.default__.Decode(d_109_encoded_)
        if not(not((d_118_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(119,14): " + _dafny.string_of(d_118_valueOrError7_))
        d_111_redecoded_ = (d_118_valueOrError7_).Extract()
        if not((d_108_decoded_) == (d_111_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(120,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test3Bytes():
        d_119_decoded_: _dafny.Seq
        d_119_decoded_ = _dafny.Seq("\u2386")
        d_120_encoded_: _dafny.Seq
        d_121_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_121_valueOrError0_ = UTF8.default__.Encode(d_119_decoded_)
        if not(not((d_121_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(126,16): " + _dafny.string_of(d_121_valueOrError0_))
        d_120_encoded_ = (d_121_valueOrError0_).Extract()
        if not((_dafny.Seq([226, 142, 134])) == (d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(127,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_122_redecoded_: _dafny.Seq
        d_123_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_123_valueOrError1_ = UTF8.default__.Decode(d_120_encoded_)
        if not(not((d_123_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(129,18): " + _dafny.string_of(d_123_valueOrError1_))
        d_122_redecoded_ = (d_123_valueOrError1_).Extract()
        if not((d_119_decoded_) == (d_122_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_119_decoded_ = _dafny.Seq("\u2387")
        d_124_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_124_valueOrError2_ = UTF8.default__.Encode(d_119_decoded_)
        if not(not((d_124_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(134,12): " + _dafny.string_of(d_124_valueOrError2_))
        d_120_encoded_ = (d_124_valueOrError2_).Extract()
        if not((_dafny.Seq([226, 142, 135])) == (d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(135,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_125_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_125_valueOrError3_ = UTF8.default__.Decode(d_120_encoded_)
        if not(not((d_125_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(137,14): " + _dafny.string_of(d_125_valueOrError3_))
        d_122_redecoded_ = (d_125_valueOrError3_).Extract()
        if not((d_119_decoded_) == (d_122_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_119_decoded_ = _dafny.Seq("\u231B")
        d_126_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_126_valueOrError4_ = UTF8.default__.Encode(d_119_decoded_)
        if not(not((d_126_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(142,12): " + _dafny.string_of(d_126_valueOrError4_))
        d_120_encoded_ = (d_126_valueOrError4_).Extract()
        if not((_dafny.Seq([226, 140, 155])) == (d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(143,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(144,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_127_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_127_valueOrError5_ = UTF8.default__.Decode(d_120_encoded_)
        if not(not((d_127_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(145,14): " + _dafny.string_of(d_127_valueOrError5_))
        d_122_redecoded_ = (d_127_valueOrError5_).Extract()
        if not((d_119_decoded_) == (d_122_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_119_decoded_ = _dafny.Seq("\u1D78")
        d_128_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_128_valueOrError6_ = UTF8.default__.Encode(d_119_decoded_)
        if not(not((d_128_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(150,12): " + _dafny.string_of(d_128_valueOrError6_))
        d_120_encoded_ = (d_128_valueOrError6_).Extract()
        if not((_dafny.Seq([225, 181, 184])) == (d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(151,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_129_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_129_valueOrError7_ = UTF8.default__.Decode(d_120_encoded_)
        if not(not((d_129_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(153,14): " + _dafny.string_of(d_129_valueOrError7_))
        d_122_redecoded_ = (d_129_valueOrError7_).Extract()
        if not((d_119_decoded_) == (d_122_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(154,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_119_decoded_ = _dafny.Seq("\u732B")
        d_130_valueOrError8_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_130_valueOrError8_ = UTF8.default__.Encode(d_119_decoded_)
        if not(not((d_130_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(158,12): " + _dafny.string_of(d_130_valueOrError8_))
        d_120_encoded_ = (d_130_valueOrError8_).Extract()
        if not((_dafny.Seq([231, 140, 171])) == (d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(159,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_120_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_131_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_131_valueOrError9_ = UTF8.default__.Decode(d_120_encoded_)
        if not(not((d_131_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(161,14): " + _dafny.string_of(d_131_valueOrError9_))
        d_122_redecoded_ = (d_131_valueOrError9_).Extract()
        if not((d_119_decoded_) == (d_122_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(162,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test4Bytes():
        d_132_decoded_: _dafny.Seq
        d_132_decoded_ = _dafny.Seq("\uD808\uDC00")
        d_133_encoded_: _dafny.Seq
        d_134_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_134_valueOrError0_ = UTF8.default__.Encode(d_132_decoded_)
        if not(not((d_134_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(168,16): " + _dafny.string_of(d_134_valueOrError0_))
        d_133_encoded_ = (d_134_valueOrError0_).Extract()
        if not((_dafny.Seq([240, 146, 128, 128])) == (d_133_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(169,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses4Bytes(d_133_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(170,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_135_redecoded_: _dafny.Seq
        d_136_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_136_valueOrError1_ = UTF8.default__.Decode(d_133_encoded_)
        if not(not((d_136_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(171,18): " + _dafny.string_of(d_136_valueOrError1_))
        d_135_redecoded_ = (d_136_valueOrError1_).Extract()
        if not((d_132_decoded_) == (d_135_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_132_decoded_ = _dafny.Seq("\uD835\uDFC1")
        d_137_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_137_valueOrError2_ = UTF8.default__.Encode(d_132_decoded_)
        if not(not((d_137_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(176,12): " + _dafny.string_of(d_137_valueOrError2_))
        d_133_encoded_ = (d_137_valueOrError2_).Extract()
        if not((_dafny.Seq([240, 157, 159, 129])) == (d_133_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses4Bytes(d_133_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(178,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_138_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_138_valueOrError3_ = UTF8.default__.Decode(d_133_encoded_)
        if not(not((d_138_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(179,14): " + _dafny.string_of(d_138_valueOrError3_))
        d_135_redecoded_ = (d_138_valueOrError3_).Extract()
        if not((d_132_decoded_) == (d_135_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(180,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

