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

# Module: GetOptTest

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestEmpty():
        d_207_MyOptions_: GetOpt.Options
        d_207_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_208_x_: GetOpt.Parsed
        d_209_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_209_valueOrError0_ = GetOpt.default__.GetOptions(d_207_MyOptions_, _dafny.Seq([_dafny.Seq("cmd")]))
        if not(not((d_209_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(20,10): " + _dafny.string_of(d_209_valueOrError0_))
        d_208_x_ = (d_209_valueOrError0_).Extract()
        if not(((d_208_x_).params) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(21,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_208_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(22,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestShort():
        d_210_MyOptions_: GetOpt.Options
        d_210_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_211_x_: GetOpt.Parsed
        d_212_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_212_valueOrError0_ = GetOpt.default__.GetOptions(d_210_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("-svsttt"), _dafny.Seq("-t"), _dafny.Seq("stuff"), _dafny.Seq("-v")]))
        if not(not((d_212_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(34,10): " + _dafny.string_of(d_212_valueOrError0_))
        d_211_x_ = (d_212_valueOrError0_).Extract()
        if not(((d_211_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("six"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("six"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("tt"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_211_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(37,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestLong():
        d_213_MyOptions_: GetOpt.Options
        d_213_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_214_x_: GetOpt.Parsed
        d_215_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_215_valueOrError0_ = GetOpt.default__.GetOptions(d_213_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("file1"), _dafny.Seq("--bar"), _dafny.Seq("bar1"), _dafny.Seq("-"), _dafny.Seq("--bar=bar2=bar3"), _dafny.Seq("file3"), _dafny.Seq("--"), _dafny.Seq("--this"), _dafny.Seq("-that")]))
        if not(not((d_215_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(49,10): " + _dafny.string_of(d_215_valueOrError0_))
        d_214_x_ = (d_215_valueOrError0_).Extract()
        if not(((d_214_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar1"))), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar2=bar3")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(50,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_214_x_).files) == (_dafny.Seq([_dafny.Seq("file1"), _dafny.Seq("-"), _dafny.Seq("file3"), _dafny.Seq("--this"), _dafny.Seq("-that")]))):
            raise _dafny.HaltException("test/GetOpt.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRequired():
        d_216_MyOptions_: GetOpt.Options
        d_216_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_Required(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_217_x_: GetOpt.Parsed
        d_218_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_218_valueOrError0_ = GetOpt.default__.GetOptions(d_216_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("file1"), _dafny.Seq("--bar"), _dafny.Seq("bar1"), _dafny.Seq("-"), _dafny.Seq("--bar=bar2=bar3"), _dafny.Seq("file3"), _dafny.Seq("--"), _dafny.Seq("--this"), _dafny.Seq("-that")]))
        if not(not((d_218_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(63,10): " + _dafny.string_of(d_218_valueOrError0_))
        d_217_x_ = (d_218_valueOrError0_).Extract()
        if not(((d_217_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar1"))), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("bar2=bar3")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_217_x_).files) == (_dafny.Seq([_dafny.Seq("file1"), _dafny.Seq("-"), _dafny.Seq("file3"), _dafny.Seq("--this"), _dafny.Seq("-that")]))):
            raise _dafny.HaltException("test/GetOpt.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_219_y_: Wrappers.Result
        d_219_y_ = GetOpt.default__.GetOptions(d_216_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("file1"), _dafny.Seq("file3"), _dafny.Seq("--"), _dafny.Seq("--this"), _dafny.Seq("-that")]))
        if not((d_219_y_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(68,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_219_y_).error) == (_dafny.Seq("Option 'bar' is required, but was not used."))):
            raise _dafny.HaltException("test/GetOpt.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDeprecated():
        d_220_MyOptions_: GetOpt.Options
        d_220_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_221_x_: GetOpt.Parsed
        d_222_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_222_valueOrError0_ = GetOpt.default__.GetOptions(d_220_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("--bar=baz"), _dafny.Seq("-svtstuff")]))
        if not(not((d_222_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(81,10): " + _dafny.string_of(d_222_valueOrError0_))
        d_221_x_ = (d_222_valueOrError0_).Extract()
        if not(((d_221_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("stuff")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(82,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_221_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(83,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestAlias():
        d_223_MyOptions_: GetOpt.Options
        d_223_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq("abc"), _dafny.Seq([_dafny.Seq("def"), _dafny.Seq("ghi")])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Deprecated(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_224_x_: GetOpt.Parsed
        d_225_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_225_valueOrError0_ = GetOpt.default__.GetOptions(d_223_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("-abc"), _dafny.Seq("--def"), _dafny.Seq("--ghi")]))
        if not(not((d_225_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(95,10): " + _dafny.string_of(d_225_valueOrError0_))
        d_224_x_ = (d_225_valueOrError0_).Extract()
        if not(((d_224_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(96,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_224_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(97,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPositionalFail():
        d_226_MyOptions_: GetOpt.Options
        d_226_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Maybe()), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Yes())]))
        d_227_x_: Wrappers.Result
        d_227_x_ = GetOpt.default__.GetOptions(d_226_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("-123"), _dafny.Seq("--foo")]))
        if not((d_227_x_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_227_x_).error) == (_dafny.Seq("Required positional argument 'bar' follows optional positional argument 'two'."))):
            raise _dafny.HaltException("test/GetOpt.dfy(109,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPositional():
        d_228_MyOptions_: GetOpt.Options
        d_228_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Yes()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_Maybe())]))
        d_229_x_: GetOpt.Parsed
        d_230_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_230_valueOrError0_ = GetOpt.default__.GetOptions(d_228_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("-123"), _dafny.Seq("--foo")]))
        if not(not((d_230_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(119,10): " + _dafny.string_of(d_230_valueOrError0_))
        d_229_x_ = (d_230_valueOrError0_).Extract()
        if not(((d_229_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("-123"))), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(120,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_229_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(121,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_231_valueOrError1_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_231_valueOrError1_ = GetOpt.default__.GetOptions(d_228_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("--two=-123"), _dafny.Seq("--foo")]))
        if not(not((d_231_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(123,6): " + _dafny.string_of(d_231_valueOrError1_))
        d_229_x_ = (d_231_valueOrError1_).Extract()
        if not(((d_229_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("-123"))), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_229_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(125,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_232_valueOrError2_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_232_valueOrError2_ = GetOpt.default__.GetOptions(d_228_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff"), _dafny.Seq("--two=-123"), _dafny.Seq("--foo"), _dafny.Seq("--bar"), _dafny.Seq("more-stuff")]))
        if not(not((d_232_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(127,6): " + _dafny.string_of(d_232_valueOrError2_))
        d_229_x_ = (d_232_valueOrError2_).Extract()
        if not(((d_229_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff"))), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("-123"))), GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("more-stuff")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_229_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_233_valueOrError3_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_233_valueOrError3_ = GetOpt.default__.GetOptions(d_228_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("stuff")]))
        if not(not((d_233_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(131,6): " + _dafny.string_of(d_233_valueOrError3_))
        d_229_x_ = (d_233_valueOrError3_).Extract()
        if not(((d_229_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("bar"), Wrappers.Option_Some(_dafny.Seq("stuff")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(132,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_229_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(133,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_234_y_: Wrappers.Result
        d_234_y_ = GetOpt.default__.GetOptions(d_228_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--two=-123"), _dafny.Seq("--foo"), _dafny.Seq("--bar"), _dafny.Seq("more-stuff")]))
        if not((d_234_y_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_234_y_).error) == (_dafny.Seq("Positional arg bar matched with invalid positional value '--two=-123'."))):
            raise _dafny.HaltException("test/GetOpt.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_234_y_ = GetOpt.default__.GetOptions(d_228_MyOptions_, _dafny.Seq([_dafny.Seq("cmd")]))
        if not((d_234_y_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(140,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_234_y_).error) == (_dafny.Seq("Positional arg 'bar' is required, but we've run out of arguments."))):
            raise _dafny.HaltException("test/GetOpt.dfy(141,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestHelp():
        d_235_MyOptions_: GetOpt.Options
        d_235_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_236_x_: GetOpt.Parsed
        d_237_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_237_valueOrError0_ = GetOpt.default__.GetOptions(d_235_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--help")]))
        if not(not((d_237_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(153,10): " + _dafny.string_of(d_237_valueOrError0_))
        d_236_x_ = (d_237_valueOrError0_).Extract()
        d_238_y_: _dafny.Seq
        d_239_valueOrError1_: Wrappers.Option = Wrappers.Option.default()()
        d_239_valueOrError1_ = GetOpt.default__.NeedsHelp(d_235_MyOptions_, d_236_x_, _dafny.Seq(""))
        if not(not((d_239_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(154,10): " + _dafny.string_of(d_239_valueOrError1_))
        d_238_y_ = (d_239_valueOrError1_).Extract()
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(d_238_y_))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))

    @staticmethod
    def TestHelpFail():
        d_240_MyOptions_: GetOpt.Options
        d_240_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("helpText"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("bar"), _dafny.Seq("helpText"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("helpText"), _dafny.Seq("arg"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("helpText"), 's', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Flag(_dafny.Seq("seven"), _dafny.Seq("helpText"), 'v', False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))
        d_241_x_: Wrappers.Result
        d_241_x_ = GetOpt.default__.GetOptions(d_240_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--help"), _dafny.Seq("--foo")]))
        if not((d_241_x_).is_Failure):
            raise _dafny.HaltException("test/GetOpt.dfy(168,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_241_x_).error) == (_dafny.Seq("Option 'help' used with other stuff, but must only be used alone."))):
            raise _dafny.HaltException("test/GetOpt.dfy(169,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestNested():
        d_242_MyOptions_: GetOpt.Options
        d_242_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("command"), _dafny.Seq("Does command stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("five"), _dafny.Seq("Does five things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("Does six things"), GetOpt.default__.NullChar, False, True, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("other"), _dafny.Seq("Does other stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("seven"), _dafny.Seq("Does seven things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("eight"), _dafny.Seq("Does eight things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))])))]))
        d_243_x_: GetOpt.Parsed
        d_244_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_244_valueOrError0_ = GetOpt.default__.GetOptions(d_242_MyOptions_, _dafny.Seq([_dafny.Seq("MyProg"), _dafny.Seq("--foo"), _dafny.Seq("other"), _dafny.Seq("--seven=siete"), _dafny.Seq("--eight")]))
        if not(not((d_244_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(186,10): " + _dafny.string_of(d_244_valueOrError0_))
        d_243_x_ = (d_244_valueOrError0_).Extract()
        if not(((d_243_x_).command) == (_dafny.Seq("MyProg"))):
            raise _dafny.HaltException("test/GetOpt.dfy(187,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_243_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(188,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_243_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(189,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_243_x_).subcommand).is_Some):
            raise _dafny.HaltException("test/GetOpt.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_245_sub_: GetOpt.Parsed
        d_245_sub_ = ((d_243_x_).subcommand).value
        if not(((d_245_sub_).command) == (_dafny.Seq("other"))):
            raise _dafny.HaltException("test/GetOpt.dfy(192,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_245_sub_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_Some(_dafny.Seq("siete"))), GetOpt.OneArg_OneArg(_dafny.Seq("eight"), Wrappers.Option_None())]))):
            raise _dafny.HaltException("test/GetOpt.dfy(193,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_245_sub_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(194,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_245_sub_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(195,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_246_valueOrError1_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_246_valueOrError1_ = GetOpt.default__.GetOptions(d_242_MyOptions_, _dafny.Seq([_dafny.Seq("MyProg"), _dafny.Seq("--help")]))
        if not(not((d_246_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(197,6): " + _dafny.string_of(d_246_valueOrError1_))
        d_243_x_ = (d_246_valueOrError1_).Extract()
        d_247_y_: _dafny.Seq
        d_248_valueOrError2_: Wrappers.Option = Wrappers.Option.default()()
        d_248_valueOrError2_ = GetOpt.default__.NeedsHelp(d_242_MyOptions_, d_243_x_, _dafny.Seq(""))
        if not(not((d_248_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(198,10): " + _dafny.string_of(d_248_valueOrError2_))
        d_247_y_ = (d_248_valueOrError2_).Extract()
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(d_247_y_))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        d_249_valueOrError3_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_249_valueOrError3_ = GetOpt.default__.GetOptions(d_242_MyOptions_, _dafny.Seq([_dafny.Seq("MyProg"), _dafny.Seq("command"), _dafny.Seq("--help")]))
        if not(not((d_249_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(201,6): " + _dafny.string_of(d_249_valueOrError3_))
        d_243_x_ = (d_249_valueOrError3_).Extract()
        d_250_valueOrError4_: Wrappers.Option = Wrappers.Option.default()()
        d_250_valueOrError4_ = GetOpt.default__.NeedsHelp(d_242_MyOptions_, d_243_x_, _dafny.Seq(""))
        if not(not((d_250_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(202,6): " + _dafny.string_of(d_250_valueOrError4_))
        d_247_y_ = (d_250_valueOrError4_).Extract()
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(d_247_y_))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))

    @staticmethod
    def TestDefault():
        d_251_MyOptions_: GetOpt.Options
        d_251_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("MyProg"), _dafny.Seq("does stuff"), _dafny.Seq([GetOpt.Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), GetOpt.Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', GetOpt.Unused_Default(_dafny.Seq("two_dflt")), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("command"), _dafny.Seq("Does command stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("five"), _dafny.Seq("Does five things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_Default(_dafny.Seq("five_dflt")), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("six"), _dafny.Seq("Does six things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("other"), _dafny.Seq("Does other stuff"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("seven"), _dafny.Seq("Does seven things to thingy"), _dafny.Seq("thingy"), 'h', GetOpt.Unused_Default(_dafny.Seq("seven_dflt")), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Flag(_dafny.Seq("eight"), _dafny.Seq("Does eight things"), GetOpt.default__.NullChar, False, False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))])))]))
        d_252_x_: GetOpt.Parsed
        d_253_valueOrError0_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_253_valueOrError0_ = GetOpt.default__.GetOptions(d_251_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("other"), _dafny.Seq("--eight")]))
        if not(not((d_253_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(227,10): " + _dafny.string_of(d_253_valueOrError0_))
        d_252_x_ = (d_253_valueOrError0_).Extract()
        if not(((d_252_x_).command) == (_dafny.Seq("cmd"))):
            raise _dafny.HaltException("test/GetOpt.dfy(228,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("two_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(229,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(230,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).subcommand).is_Some):
            raise _dafny.HaltException("test/GetOpt.dfy(231,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_254_sub_: GetOpt.Parsed
        d_254_sub_ = ((d_252_x_).subcommand).value
        if not(((d_254_sub_).command) == (_dafny.Seq("other"))):
            raise _dafny.HaltException("test/GetOpt.dfy(233,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_254_sub_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("eight"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("seven"), Wrappers.Option_Some(_dafny.Seq("seven_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(234,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_254_sub_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(235,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_254_sub_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(236,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_255_valueOrError1_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_255_valueOrError1_ = GetOpt.default__.GetOptions(d_251_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo"), _dafny.Seq("command"), _dafny.Seq("--six")]))
        if not(not((d_255_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(238,6): " + _dafny.string_of(d_255_valueOrError1_))
        d_252_x_ = (d_255_valueOrError1_).Extract()
        if not(((d_252_x_).command) == (_dafny.Seq("cmd"))):
            raise _dafny.HaltException("test/GetOpt.dfy(239,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("two_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(240,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(241,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).subcommand).is_Some):
            raise _dafny.HaltException("test/GetOpt.dfy(242,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_254_sub_ = ((d_252_x_).subcommand).value
        if not(((d_254_sub_).command) == (_dafny.Seq("command"))):
            raise _dafny.HaltException("test/GetOpt.dfy(244,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_254_sub_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("six"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("five"), Wrappers.Option_Some(_dafny.Seq("five_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(245,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_254_sub_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(246,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_254_sub_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(247,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_256_valueOrError2_: Wrappers.Result = Wrappers.Result.default(GetOpt.Parsed.default())()
        d_256_valueOrError2_ = GetOpt.default__.GetOptions(d_251_MyOptions_, _dafny.Seq([_dafny.Seq("cmd"), _dafny.Seq("--foo")]))
        if not(not((d_256_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/GetOpt.dfy(249,6): " + _dafny.string_of(d_256_valueOrError2_))
        d_252_x_ = (d_256_valueOrError2_).Extract()
        if not(((d_252_x_).command) == (_dafny.Seq("cmd"))):
            raise _dafny.HaltException("test/GetOpt.dfy(250,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).params) == (_dafny.Seq([GetOpt.OneArg_OneArg(_dafny.Seq("foo"), Wrappers.Option_None()), GetOpt.OneArg_OneArg(_dafny.Seq("two"), Wrappers.Option_Some(_dafny.Seq("two_dflt")))]))):
            raise _dafny.HaltException("test/GetOpt.dfy(251,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).files) == (_dafny.Seq([]))):
            raise _dafny.HaltException("test/GetOpt.dfy(252,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_252_x_).subcommand).is_None):
            raise _dafny.HaltException("test/GetOpt.dfy(253,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDdbec():
        d_257_MyOptions_: GetOpt.Options
        d_257_MyOptions_ = GetOpt.Options_Options(_dafny.Seq("ddbec"), _dafny.Seq("Test the ddbec"), _dafny.Seq([GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("encrypt"), _dafny.Seq("Encrypts record"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("output"), _dafny.Seq("Write encrypted records to fileName."), _dafny.Seq("fileName"), 'o', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No())]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("decrypt"), _dafny.Seq("Decrypts Records"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("expected"), _dafny.Seq("fileName contains expected plaintext records."), _dafny.Seq("fileName"), 'e', GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No())])))]))

