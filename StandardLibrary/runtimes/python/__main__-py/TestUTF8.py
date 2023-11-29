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

# Module: TestUTF8

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestEncodeHappyCase():
        d_73_unicodeString_: _dafny.Seq
        d_73_unicodeString_ = _dafny.Seq("abc\u0306\u01FD\u03B2")
        d_74_expectedBytes_: _dafny.Seq
        d_74_expectedBytes_ = _dafny.Seq([97, 98, 99, 204, 134, 199, 189, 206, 178])
        d_75_encoded_: _dafny.Seq
        d_76_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_76_valueOrError0_ = UTF8.default__.Encode(d_73_unicodeString_)
        if not(not((d_76_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(14,16): " + _dafny.string_of(d_76_valueOrError0_))
        d_75_encoded_ = (d_76_valueOrError0_).Extract()
        if not((d_74_expectedBytes_) == (d_75_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(15,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestEncodeInvalidUnicode():
        d_77_invalidUnicode_: _dafny.Seq
        d_77_invalidUnicode_ = _dafny.Seq("abc\uD800")
        d_78_encoded_: Wrappers.Result
        d_78_encoded_ = UTF8.default__.Encode(d_77_invalidUnicode_)
        if not((d_78_encoded_).is_Failure):
            raise _dafny.HaltException("test/UTF8.dfy(22,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDecodeHappyCase():
        d_79_unicodeBytes_: _dafny.Seq
        d_79_unicodeBytes_ = _dafny.Seq([97, 98, 99, 204, 134, 199, 189, 206, 178])
        d_80_expectedString_: _dafny.Seq
        d_80_expectedString_ = _dafny.Seq("abc\u0306\u01FD\u03B2")
        d_81_decoded_: _dafny.Seq
        d_82_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_82_valueOrError0_ = UTF8.default__.Decode(d_79_unicodeBytes_)
        if not(not((d_82_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(32,16): " + _dafny.string_of(d_82_valueOrError0_))
        d_81_decoded_ = (d_82_valueOrError0_).Extract()
        if not((d_80_expectedString_) == (d_81_decoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDecodeInvalidUnicode():
        d_83_invalidUnicode_: _dafny.Seq
        d_83_invalidUnicode_ = _dafny.Seq([97, 98, 99, 237, 160, 128])
        if not(not(UTF8.default__.ValidUTF8Seq(d_83_invalidUnicode_))):
            raise _dafny.HaltException("test/UTF8.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((UTF8.default__.Decode(d_83_invalidUnicode_)).is_Failure):
            raise _dafny.HaltException("test/UTF8.dfy(40,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test1Byte():
        d_84_decoded_: _dafny.Seq
        d_84_decoded_ = _dafny.Seq("\u0000")
        d_85_encoded_: _dafny.Seq
        d_86_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_86_valueOrError0_ = UTF8.default__.Encode(d_84_decoded_)
        if not(not((d_86_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(46,16): " + _dafny.string_of(d_86_valueOrError0_))
        d_85_encoded_ = (d_86_valueOrError0_).Extract()
        if not((_dafny.Seq([0])) == (d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_87_redecoded_: _dafny.Seq
        d_88_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_88_valueOrError1_ = UTF8.default__.Decode(d_85_encoded_)
        if not(not((d_88_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(49,18): " + _dafny.string_of(d_88_valueOrError1_))
        d_87_redecoded_ = (d_88_valueOrError1_).Extract()
        if not((d_84_decoded_) == (d_87_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(50,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_84_decoded_ = _dafny.Seq("\u0020")
        d_89_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_89_valueOrError2_ = UTF8.default__.Encode(d_84_decoded_)
        if not(not((d_89_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(54,12): " + _dafny.string_of(d_89_valueOrError2_))
        d_85_encoded_ = (d_89_valueOrError2_).Extract()
        if not((_dafny.Seq([32])) == (d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(55,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_90_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_90_valueOrError3_ = UTF8.default__.Decode(d_85_encoded_)
        if not(not((d_90_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(57,14): " + _dafny.string_of(d_90_valueOrError3_))
        d_87_redecoded_ = (d_90_valueOrError3_).Extract()
        if not((d_84_decoded_) == (d_87_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_84_decoded_ = _dafny.Seq("$")
        d_91_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_91_valueOrError4_ = UTF8.default__.Encode(d_84_decoded_)
        if not(not((d_91_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(61,12): " + _dafny.string_of(d_91_valueOrError4_))
        d_85_encoded_ = (d_91_valueOrError4_).Extract()
        if not((_dafny.Seq([36])) == (d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_92_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_92_valueOrError5_ = UTF8.default__.Decode(d_85_encoded_)
        if not(not((d_92_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(64,14): " + _dafny.string_of(d_92_valueOrError5_))
        d_87_redecoded_ = (d_92_valueOrError5_).Extract()
        if not((d_84_decoded_) == (d_87_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_84_decoded_ = _dafny.Seq("0")
        d_93_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_93_valueOrError6_ = UTF8.default__.Encode(d_84_decoded_)
        if not(not((d_93_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(68,12): " + _dafny.string_of(d_93_valueOrError6_))
        d_85_encoded_ = (d_93_valueOrError6_).Extract()
        if not((_dafny.Seq([48])) == (d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_94_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_94_valueOrError7_ = UTF8.default__.Decode(d_85_encoded_)
        if not(not((d_94_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(71,14): " + _dafny.string_of(d_94_valueOrError7_))
        d_87_redecoded_ = (d_94_valueOrError7_).Extract()
        if not((d_84_decoded_) == (d_87_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_84_decoded_ = _dafny.Seq("A")
        d_95_valueOrError8_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_95_valueOrError8_ = UTF8.default__.Encode(d_84_decoded_)
        if not(not((d_95_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(75,12): " + _dafny.string_of(d_95_valueOrError8_))
        d_85_encoded_ = (d_95_valueOrError8_).Extract()
        if not((_dafny.Seq([65])) == (d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(77,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_96_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_96_valueOrError9_ = UTF8.default__.Decode(d_85_encoded_)
        if not(not((d_96_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(78,14): " + _dafny.string_of(d_96_valueOrError9_))
        d_87_redecoded_ = (d_96_valueOrError9_).Extract()
        if not((d_84_decoded_) == (d_87_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(79,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_84_decoded_ = _dafny.Seq("a")
        d_97_valueOrError10_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_97_valueOrError10_ = UTF8.default__.Encode(d_84_decoded_)
        if not(not((d_97_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(82,12): " + _dafny.string_of(d_97_valueOrError10_))
        d_85_encoded_ = (d_97_valueOrError10_).Extract()
        if not((_dafny.Seq([97])) == (d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(83,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses1Byte(d_85_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(84,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_98_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_98_valueOrError11_ = UTF8.default__.Decode(d_85_encoded_)
        if not(not((d_98_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(85,14): " + _dafny.string_of(d_98_valueOrError11_))
        d_87_redecoded_ = (d_98_valueOrError11_).Extract()
        if not((d_84_decoded_) == (d_87_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test2Bytes():
        d_99_decoded_: _dafny.Seq
        d_99_decoded_ = _dafny.Seq("\u00A3")
        d_100_encoded_: _dafny.Seq
        d_101_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_101_valueOrError0_ = UTF8.default__.Encode(d_99_decoded_)
        if not(not((d_101_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(92,16): " + _dafny.string_of(d_101_valueOrError0_))
        d_100_encoded_ = (d_101_valueOrError0_).Extract()
        if not((_dafny.Seq([194, 163])) == (d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(93,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(94,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_102_redecoded_: _dafny.Seq
        d_103_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_103_valueOrError1_ = UTF8.default__.Decode(d_100_encoded_)
        if not(not((d_103_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(95,18): " + _dafny.string_of(d_103_valueOrError1_))
        d_102_redecoded_ = (d_103_valueOrError1_).Extract()
        if not((d_99_decoded_) == (d_102_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(96,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_99_decoded_ = _dafny.Seq("\u00A9")
        d_104_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_104_valueOrError2_ = UTF8.default__.Encode(d_99_decoded_)
        if not(not((d_104_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(100,12): " + _dafny.string_of(d_104_valueOrError2_))
        d_100_encoded_ = (d_104_valueOrError2_).Extract()
        if not((_dafny.Seq([194, 169])) == (d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_105_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_105_valueOrError3_ = UTF8.default__.Decode(d_100_encoded_)
        if not(not((d_105_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(103,14): " + _dafny.string_of(d_105_valueOrError3_))
        d_102_redecoded_ = (d_105_valueOrError3_).Extract()
        if not((d_99_decoded_) == (d_102_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_99_decoded_ = _dafny.Seq("\u00AE")
        d_106_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_106_valueOrError4_ = UTF8.default__.Encode(d_99_decoded_)
        if not(not((d_106_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(108,12): " + _dafny.string_of(d_106_valueOrError4_))
        d_100_encoded_ = (d_106_valueOrError4_).Extract()
        if not((_dafny.Seq([194, 174])) == (d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(109,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_107_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_107_valueOrError5_ = UTF8.default__.Decode(d_100_encoded_)
        if not(not((d_107_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(111,14): " + _dafny.string_of(d_107_valueOrError5_))
        d_102_redecoded_ = (d_107_valueOrError5_).Extract()
        if not((d_99_decoded_) == (d_102_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_99_decoded_ = _dafny.Seq("\u03C0")
        d_108_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_108_valueOrError6_ = UTF8.default__.Encode(d_99_decoded_)
        if not(not((d_108_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(116,12): " + _dafny.string_of(d_108_valueOrError6_))
        d_100_encoded_ = (d_108_valueOrError6_).Extract()
        if not((_dafny.Seq([207, 128])) == (d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(117,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses2Bytes(d_100_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_109_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_109_valueOrError7_ = UTF8.default__.Decode(d_100_encoded_)
        if not(not((d_109_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(119,14): " + _dafny.string_of(d_109_valueOrError7_))
        d_102_redecoded_ = (d_109_valueOrError7_).Extract()
        if not((d_99_decoded_) == (d_102_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(120,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test3Bytes():
        d_110_decoded_: _dafny.Seq
        d_110_decoded_ = _dafny.Seq("\u2386")
        d_111_encoded_: _dafny.Seq
        d_112_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_112_valueOrError0_ = UTF8.default__.Encode(d_110_decoded_)
        if not(not((d_112_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(126,16): " + _dafny.string_of(d_112_valueOrError0_))
        d_111_encoded_ = (d_112_valueOrError0_).Extract()
        if not((_dafny.Seq([226, 142, 134])) == (d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(127,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_113_redecoded_: _dafny.Seq
        d_114_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_114_valueOrError1_ = UTF8.default__.Decode(d_111_encoded_)
        if not(not((d_114_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(129,18): " + _dafny.string_of(d_114_valueOrError1_))
        d_113_redecoded_ = (d_114_valueOrError1_).Extract()
        if not((d_110_decoded_) == (d_113_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_110_decoded_ = _dafny.Seq("\u2387")
        d_115_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_115_valueOrError2_ = UTF8.default__.Encode(d_110_decoded_)
        if not(not((d_115_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(134,12): " + _dafny.string_of(d_115_valueOrError2_))
        d_111_encoded_ = (d_115_valueOrError2_).Extract()
        if not((_dafny.Seq([226, 142, 135])) == (d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(135,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_116_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_116_valueOrError3_ = UTF8.default__.Decode(d_111_encoded_)
        if not(not((d_116_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(137,14): " + _dafny.string_of(d_116_valueOrError3_))
        d_113_redecoded_ = (d_116_valueOrError3_).Extract()
        if not((d_110_decoded_) == (d_113_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_110_decoded_ = _dafny.Seq("\u231B")
        d_117_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_117_valueOrError4_ = UTF8.default__.Encode(d_110_decoded_)
        if not(not((d_117_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(142,12): " + _dafny.string_of(d_117_valueOrError4_))
        d_111_encoded_ = (d_117_valueOrError4_).Extract()
        if not((_dafny.Seq([226, 140, 155])) == (d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(143,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(144,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_118_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_118_valueOrError5_ = UTF8.default__.Decode(d_111_encoded_)
        if not(not((d_118_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(145,14): " + _dafny.string_of(d_118_valueOrError5_))
        d_113_redecoded_ = (d_118_valueOrError5_).Extract()
        if not((d_110_decoded_) == (d_113_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_110_decoded_ = _dafny.Seq("\u1D78")
        d_119_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_119_valueOrError6_ = UTF8.default__.Encode(d_110_decoded_)
        if not(not((d_119_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(150,12): " + _dafny.string_of(d_119_valueOrError6_))
        d_111_encoded_ = (d_119_valueOrError6_).Extract()
        if not((_dafny.Seq([225, 181, 184])) == (d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(151,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_120_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_120_valueOrError7_ = UTF8.default__.Decode(d_111_encoded_)
        if not(not((d_120_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(153,14): " + _dafny.string_of(d_120_valueOrError7_))
        d_113_redecoded_ = (d_120_valueOrError7_).Extract()
        if not((d_110_decoded_) == (d_113_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(154,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_110_decoded_ = _dafny.Seq("\u732B")
        d_121_valueOrError8_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_121_valueOrError8_ = UTF8.default__.Encode(d_110_decoded_)
        if not(not((d_121_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(158,12): " + _dafny.string_of(d_121_valueOrError8_))
        d_111_encoded_ = (d_121_valueOrError8_).Extract()
        if not((_dafny.Seq([231, 140, 171])) == (d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(159,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses3Bytes(d_111_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_122_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_122_valueOrError9_ = UTF8.default__.Decode(d_111_encoded_)
        if not(not((d_122_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(161,14): " + _dafny.string_of(d_122_valueOrError9_))
        d_113_redecoded_ = (d_122_valueOrError9_).Extract()
        if not((d_110_decoded_) == (d_113_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(162,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def Test4Bytes():
        d_123_decoded_: _dafny.Seq
        d_123_decoded_ = _dafny.Seq("\uD808\uDC00")
        d_124_encoded_: _dafny.Seq
        d_125_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_125_valueOrError0_ = UTF8.default__.Encode(d_123_decoded_)
        if not(not((d_125_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(168,16): " + _dafny.string_of(d_125_valueOrError0_))
        d_124_encoded_ = (d_125_valueOrError0_).Extract()
        if not((_dafny.Seq([240, 146, 128, 128])) == (d_124_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(169,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses4Bytes(d_124_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(170,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_126_redecoded_: _dafny.Seq
        d_127_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_127_valueOrError1_ = UTF8.default__.Decode(d_124_encoded_)
        if not(not((d_127_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(171,18): " + _dafny.string_of(d_127_valueOrError1_))
        d_126_redecoded_ = (d_127_valueOrError1_).Extract()
        if not((d_123_decoded_) == (d_126_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_123_decoded_ = _dafny.Seq("\uD835\uDFC1")
        d_128_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_128_valueOrError2_ = UTF8.default__.Encode(d_123_decoded_)
        if not(not((d_128_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(176,12): " + _dafny.string_of(d_128_valueOrError2_))
        d_124_encoded_ = (d_128_valueOrError2_).Extract()
        if not((_dafny.Seq([240, 157, 159, 129])) == (d_124_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(UTF8.default__.Uses4Bytes(d_124_encoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(178,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_129_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_129_valueOrError3_ = UTF8.default__.Decode(d_124_encoded_)
        if not(not((d_129_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/UTF8.dfy(179,14): " + _dafny.string_of(d_129_valueOrError3_))
        d_126_redecoded_ = (d_129_valueOrError3_).Extract()
        if not((d_123_decoded_) == (d_126_redecoded_)):
            raise _dafny.HaltException("test/UTF8.dfy(180,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

