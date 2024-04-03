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

# Module: GetOptTest

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestEmpty():
        d_122_MyOptions_: GetOpt.Options
        d_122_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_123_x_: GetOpt.Parsed
        d_124_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_124_valueOrError0_ = GetOpt.default__.GetOptions(d_122_MyOptions_, _dafny.Seq([_dafny.Seq("cmd")]))
        if not(not((d_124_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(20,13): " + _dafny.string_of(d_124_valueOrError0_))
        d_123_x_ = (d_124_valueOrError0_).Extract()
        if not(((d_123_x_).params) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(21,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_123_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(22,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestShort():
        d_125_MyOptions_: GetOpt.Options
        d_125_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_126_x_: GetOpt.Parsed
        d_127_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_127_valueOrError0_ = GetOpt.default__.GetOptions(d_125_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("-svsttt"), _dafny.Seq("-t"), _dafny.Seq("stuff"), _dafny.Seq("-v")]))
        if not(not((d_127_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(34,13): " + _dafny.string_of(d_127_valueOrError0_))
        d_126_x_ = (d_127_valueOrError0_).Extract()
        if not(((d_126_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("six"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("six"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("tt"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_126_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(37,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestLong():
        d_128_MyOptions_: GetOpt.Options
        d_128_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_129_x_: GetOpt.Parsed
        d_130_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_130_valueOrError0_ = GetOpt.default__.GetOptions(d_128_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("file1"), _dafny.Seq("--bar"), _dafny.Seq("bar1"), _dafny.Seq("-"), _dafny.Seq("--bar=bar2=bar3"), _dafny.Seq("file3"), _dafny.Seq("--"), _dafny.Seq("--this"), _dafny.Seq("-that")]))
        if not(not((d_130_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(49,13): " + _dafny.string_of(d_130_valueOrError0_))
        d_129_x_ = (d_130_valueOrError0_).Extract()
        if not(((d_129_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar1"))), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar2=bar3")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(50,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_129_x_).files) == (_dafny.Seq([_dafny.Seq("file1"), _dafny.Seq("-"), _dafny.Seq("file3"), _dafny.Seq("--this"), _dafny.Seq("-that")]))):
            raise _dafny.HaltException("test/GetOpt.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRequired():
        d_131_MyOptions_: GetOpt.Options
        d_131_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_Required(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_132_x_: GetOpt.Parsed
        d_133_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_133_valueOrError0_ = GetOpt.default__.GetOptions(d_131_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("file1"), _dafny.Seq("--bar"), _dafny.Seq("bar1"), _dafny.Seq("-"), _dafny.Seq("--bar=bar2=bar3"), _dafny.Seq("file3"), _dafny.Seq("--"), _dafny.Seq("--this"), _dafny.Seq("-that")]))
        if not(not((d_133_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(63,13): " + _dafny.string_of(d_133_valueOrError0_))
        d_132_x_ = (d_133_valueOrError0_).Extract()
        if not(((d_132_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar1"))), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar2=bar3")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_132_x_).files) == (_dafny.Seq([_dafny.Seq("file1"), _dafny.Seq("-"), _dafny.Seq("file3"), _dafny.Seq("--this"), _dafny.Seq("-that")]))):
            raise _dafny.HaltException("test/GetOpt.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_134_y_: Wrappers.Result
        d_134_y_ = GetOpt.default__.GetOptions(d_131_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("file1"), _dafny.Seq("file3"), _dafny.Seq("--"), _dafny.Seq("--this"), _dafny.Seq("-that")]))
        if not((d_134_y_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(68,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_134_y_).error) == (_dafny.Seq("Option 'bar' is required, but was not used."))):
            raise _dafny.HaltException("test/GetOpt.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDeprecated():
        d_135_MyOptions_: GetOpt.Options
        d_135_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_136_x_: GetOpt.Parsed
        d_137_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_137_valueOrError0_ = GetOpt.default__.GetOptions(d_135_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("--bar=baz"), _dafny.Seq("-svtstuff")]))
        if not(not((d_137_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(81,13): " + _dafny.string_of(d_137_valueOrError0_))
        d_136_x_ = (d_137_valueOrError0_).Extract()
        if not(((d_136_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("stuff")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(82,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_136_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(83,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestAlias():
        d_138_MyOptions_: GetOpt.Options
        d_138_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq("abc"), _dafny.Seq([_dafny.Seq("def"), _dafny.Seq("ghi")])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_139_x_: GetOpt.Parsed
        d_140_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_140_valueOrError0_ = GetOpt.default__.GetOptions(d_138_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("-abc"), _dafny.Seq("--def"), _dafny.Seq("--ghi")]))
        if not(not((d_140_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(95,13): " + _dafny.string_of(d_140_valueOrError0_))
        d_139_x_ = (d_140_valueOrError0_).Extract()
        if not(((d_139_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(96,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_139_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(97,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPositionalFail():
        d_141_MyOptions_: GetOpt.Options
        d_141_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Maybe()), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Yes())]))
        d_142_x_: Wrappers.Result
        d_142_x_ = GetOpt.default__.GetOptions(d_141_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("-123"), _dafny.Seq("--foo")]))
        if not((d_142_x_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_142_x_).error) == (_dafny.Seq("Required positional argument 'bar' follows optional positional argument 'two'."))):
            raise _dafny.HaltException("test/GetOpt.dfy(109,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPositional():
        d_143_MyOptions_: GetOpt.Options
        d_143_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Yes()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Maybe())]))
        d_144_x_: GetOpt.Parsed
        d_145_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_145_valueOrError0_ = GetOpt.default__.GetOptions(d_143_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("-123"), _dafny.Seq("--foo")]))
        if not(not((d_145_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(119,13): " + _dafny.string_of(d_145_valueOrError0_))
        d_144_x_ = (d_145_valueOrError0_).Extract()
        if not(((d_144_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("-123"))), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(120,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_144_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(121,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_146_valueOrError1_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_146_valueOrError1_ = GetOpt.default__.GetOptions(d_143_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("--two=-123"), _dafny.Seq("--foo")]))
        if not(not((d_146_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(123,9): " + _dafny.string_of(d_146_valueOrError1_))
        d_144_x_ = (d_146_valueOrError1_).Extract()
        if not(((d_144_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("-123"))), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_144_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(125,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_147_valueOrError2_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_147_valueOrError2_ = GetOpt.default__.GetOptions(d_143_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("--two=-123"), _dafny.Seq("--foo"), _dafny.Seq("--bar"), _dafny.Seq("more-stuff")]))
        if not(not((d_147_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(127,9): " + _dafny.string_of(d_147_valueOrError2_))
        d_144_x_ = (d_147_valueOrError2_).Extract()
        if not(((d_144_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("-123"))), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("more-stuff")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_144_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_148_valueOrError3_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_148_valueOrError3_ = GetOpt.default__.GetOptions(d_143_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff")]))
        if not(not((d_148_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(131,9): " + _dafny.string_of(d_148_valueOrError3_))
        d_144_x_ = (d_148_valueOrError3_).Extract()
        if not(((d_144_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(132,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_144_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(133,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_149_y_: Wrappers.Result
        d_149_y_ = GetOpt.default__.GetOptions(d_143_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--two=-123"), _dafny.Seq("--foo"), _dafny.Seq("--bar"), _dafny.Seq("more-stuff")]))
        if not((d_149_y_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_149_y_).error) == (_dafny.Seq("Positional arg bar matched with invalid positional value '--two=-123'."))):
            raise _dafny.HaltException("test/GetOpt.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_149_y_ = GetOpt.default__.GetOptions(d_143_MyOptions_, _dafny.Seq([_dafny.Seq("cmd")]))
        if not((d_149_y_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(140,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_149_y_).error) == (_dafny.Seq("Positional arg 'bar' is required, but we've run out of arguments."))):
            raise _dafny.HaltException("test/GetOpt.dfy(141,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestHelp():
        d_150_MyOptions_: GetOpt.Options
        d_150_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_151_x_: GetOpt.Parsed
        d_152_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_152_valueOrError0_ = GetOpt.default__.GetOptions(d_150_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--help")]))
        if not(not((d_152_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(153,13): " + _dafny.string_of(d_152_valueOrError0_))
        d_151_x_ = (d_152_valueOrError0_).Extract()
        d_153_y_: _dafny.Seq
        d_154_valueOrError1_: Wrappers.Option = Wrappers.Option.default()()
        d_154_valueOrError1_ = GetOpt.default__.NeedsHelp(d_150_MyOptions_, d_151_x_, _dafny.Seq(""))
        if not(not((d_154_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(154,13): " + _dafny.string_of(d_154_valueOrError1_))
        d_153_y_ = (d_154_valueOrError1_).Extract()
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(d_153_y_))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))

    @staticmethod
    def TestHelpFail():
        d_155_MyOptions_: GetOpt.Options
        d_155_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_156_x_: Wrappers.Result
        d_156_x_ = GetOpt.default__.GetOptions(d_155_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--help"), _dafny.Seq("--foo")]))
        if not((d_156_x_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(168,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_156_x_).error) == (_dafny.Seq("Option 'help' used with other stuff, but must only be used alone."))):
            raise _dafny.HaltException("test/GetOpt.dfy(169,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestNested():
        d_157_MyOptions_: GetOpt.Options
        d_157_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("command"), _dafny.Seq("Does command stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("five"), _dafny.Seq("Does five things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("Does six things"), GetOpt.default__.NullChar, False, True, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("other"), _dafny.Seq("Does other stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("seven"), _dafny.Seq("Does seven things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("eight"), _dafny.Seq("Does eight things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))])))]))
        d_158_x_: GetOpt.Parsed
        d_159_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_159_valueOrError0_ = GetOpt.default__.GetOptions(d_157_MyOptions_, _dafny.Seq([_dafny.Seq("MyProg"), _dafny.Seq("--foo"), _dafny.Seq("other"), _dafny.Seq("--seven=siete"), _dafny.Seq("--eight")]))
        if not(not((d_159_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(186,13): " + _dafny.string_of(d_159_valueOrError0_))
        d_158_x_ = (d_159_valueOrError0_).Extract()
        if not(((d_158_x_).command) == (_dafny.Seq("MyProg"))):
            raise _dafny.HaltException("test/GetOpt.dfy(187,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_158_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(188,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_158_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(189,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_158_x_).subcommand).is_Some):
            raise _dafny.HaltException("test/GetOpt.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_160_sub_: GetOpt.Parsed
        d_160_sub_ = ((d_158_x_).subcommand).value
        if not(((d_160_sub_).command) == (_dafny.Seq("other"))):
            raise _dafny.HaltException("test/GetOpt.dfy(192,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_160_sub_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_Some(_dafny.Seq("siete"))), GetOpt.OneArg_OneArg(_dafny.Seq("eight"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(193,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_160_sub_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(194,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_160_sub_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(195,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_161_valueOrError1_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_161_valueOrError1_ = GetOpt.default__.GetOptions(d_157_MyOptions_, _dafny.Seq([_dafny.Seq("MyProg"), _dafny.Seq("--help")]))
        if not(not((d_161_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(197,9): " + _dafny.string_of(d_161_valueOrError1_))
        d_158_x_ = (d_161_valueOrError1_).Extract()
        d_162_y_: _dafny.Seq
        d_163_valueOrError2_: Wrappers.Option = Wrappers.Option.default()()
        d_163_valueOrError2_ = GetOpt.default__.NeedsHelp(d_157_MyOptions_, d_158_x_, _dafny.Seq(""))
        if not(not((d_163_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(198,13): " + _dafny.string_of(d_163_valueOrError2_))
        d_162_y_ = (d_163_valueOrError2_).Extract()
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(d_162_y_))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        d_164_valueOrError3_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_164_valueOrError3_ = GetOpt.default__.GetOptions(d_157_MyOptions_, _dafny.Seq([_dafny.Seq("MyProg"), _dafny.Seq("command"), _dafny.Seq("--help")]))
        if not(not((d_164_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(201,9): " + _dafny.string_of(d_164_valueOrError3_))
        d_158_x_ = (d_164_valueOrError3_).Extract()
        d_165_valueOrError4_: Wrappers.Option = Wrappers.Option.default()()
        d_165_valueOrError4_ = GetOpt.default__.NeedsHelp(d_157_MyOptions_, d_158_x_, _dafny.Seq(""))
        if not(not((d_165_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(202,9): " + _dafny.string_of(d_165_valueOrError4_))
        d_162_y_ = (d_165_valueOrError4_).Extract()
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(d_162_y_))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))

    @staticmethod
    def TestDefault():
        d_166_MyOptions_: GetOpt.Options
        d_166_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', GetOpt.Unused_Default(_dafny.Seq("two_dflt")), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("command"), _dafny.Seq("Does command stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("five"), _dafny.Seq("Does five things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_Default(_dafny.Seq("five_dflt")), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("Does six things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("other"), _dafny.Seq("Does other stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("seven"), _dafny.Seq("Does seven things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_Default(_dafny.Seq("seven_dflt")), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("eight"), _dafny.Seq("Does eight things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))])))]))
        d_167_x_: GetOpt.Parsed
        d_168_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_168_valueOrError0_ = GetOpt.default__.GetOptions(d_166_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("other"), _dafny.Seq("--eight")]))
        if not(not((d_168_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(227,13): " + _dafny.string_of(d_168_valueOrError0_))
        d_167_x_ = (d_168_valueOrError0_).Extract()
        if not(((d_167_x_).command) == (_dafny.Seq("cmd"))):
            raise _dafny.HaltException("test/GetOpt.dfy(228,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("two_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(229,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(230,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).subcommand).is_Some):
            raise _dafny.HaltException("test/GetOpt.dfy(231,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_169_sub_: GetOpt.Parsed
        d_169_sub_ = ((d_167_x_).subcommand).value
        if not(((d_169_sub_).command) == (_dafny.Seq("other"))):
            raise _dafny.HaltException("test/GetOpt.dfy(233,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_169_sub_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("eight"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_Some(_dafny.Seq("seven_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(234,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_169_sub_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(235,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_169_sub_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(236,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_170_valueOrError1_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_170_valueOrError1_ = GetOpt.default__.GetOptions(d_166_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("command"), _dafny.Seq("--six")]))
        if not(not((d_170_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(238,9): " + _dafny.string_of(d_170_valueOrError1_))
        d_167_x_ = (d_170_valueOrError1_).Extract()
        if not(((d_167_x_).command) == (_dafny.Seq("cmd"))):
            raise _dafny.HaltException("test/GetOpt.dfy(239,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("two_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(240,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(241,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).subcommand).is_Some):
            raise _dafny.HaltException("test/GetOpt.dfy(242,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_169_sub_ = ((d_167_x_).subcommand).value
        if not(((d_169_sub_).command) == (_dafny.Seq("command"))):
            raise _dafny.HaltException("test/GetOpt.dfy(244,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_169_sub_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("six"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("five"), Wrappers.Option_Some(_dafny.Seq("five_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(245,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_169_sub_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(246,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_169_sub_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(247,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_171_valueOrError2_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_171_valueOrError2_ = GetOpt.default__.GetOptions(d_166_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo")]))
        if not(not((d_171_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(249,9): " + _dafny.string_of(d_171_valueOrError2_))
        d_167_x_ = (d_171_valueOrError2_).Extract()
        if not(((d_167_x_).command) == (_dafny.Seq("cmd"))):
            raise _dafny.HaltException("test/GetOpt.dfy(250,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("two_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(251,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(252,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_167_x_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(253,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDdbec():
        d_172_MyOptions_: GetOpt.Options
        d_172_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("ddbec"), _dafny.Seq("Test the ddbec"), _dafny.Seq([GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("encrypt"), _dafny.Seq("Encrypts record"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("output"), _dafny.Seq("Write encrypted records to fileName."), _dafny.Seq("fileName"), 'o', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No())]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("decrypt"), _dafny.Seq("Decrypts Records"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("expected"), _dafny.Seq("fileName contains expected plaintext records."), _dafny.Seq("fileName"), 'e', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No())])))]))

