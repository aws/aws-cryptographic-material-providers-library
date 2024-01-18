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

# Module: GetOpt

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Example(args):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_122_MyOptions_: _dafny.Seq
        d_122_MyOptions_ = _dafny.Seq([Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), default__.NullChar, False, False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', Unused_UnusedOk(), False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), Tri_No()), Param_Command(Options_Options(_dafny.Seq("command"), _dafny.Seq("Does command stuff"), _dafny.Seq([Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', Unused_UnusedOk(), False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), Tri_No()), Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), default__.NullChar, False, False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))])))])
        d_123_opts_: Options
        d_123_opts_ = Options_Options(_dafny.Seq("myProg"), _dafny.Seq("does prog stuff"), d_122_MyOptions_)
        d_124_x_: Parsed
        d_125_valueOrError0_: Wrappers.Result = Wrappers.Result.default(Parsed.default())()
        d_125_valueOrError0_ = default__.GetOptions(d_123_opts_, args)
        if (d_125_valueOrError0_).IsFailure():
            output = (d_125_valueOrError0_).PropagateFailure()
            return output
        d_124_x_ = (d_125_valueOrError0_).Extract()
        d_126_h_: Wrappers.Option
        d_126_h_ = default__.NeedsHelp(d_123_opts_, d_124_x_, _dafny.Seq(""))
        if (d_126_h_).is_Some:
            _dafny.print(_dafny.string_of((d_126_h_).value))
            output = Wrappers.Result_Success(True)
            return output
        output = Wrappers.Result_Success(True)
        return output
        return output

    @staticmethod
    def Filter(f, xs):
        d_127___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_127___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_127___accumulator_ = (d_127___accumulator_) + ((_dafny.Seq([(xs)[0]]) if f((xs)[0]) else _dafny.Seq([])))
                    in2_ = f
                    in3_ = _dafny.Seq((xs)[1::])
                    f = in2_
                    xs = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def NeedsHelp(opts, args, prefix):
        while True:
            with _dafny.label():
                if ((len((args).params)) != (0)) and (((((args).params)[0]).name) == (default__.HELP__STR)):
                    return Wrappers.Option_Some(default__.GetHelp(opts, prefix))
                elif ((args).subcommand).is_Some:
                    d_128_valueOrError0_ = default__.GetSubOptions((opts).params, (((args).subcommand).value).command, 0)
                    if (d_128_valueOrError0_).IsFailure():
                        return (d_128_valueOrError0_).PropagateFailure()
                    elif True:
                        d_129_pos_ = (d_128_valueOrError0_).Extract()
                        in4_ = (((opts).params)[d_129_pos_]).options
                        in5_ = ((args).subcommand).value
                        in6_ = ((prefix) + ((args).command)) + (_dafny.Seq(" "))
                        opts = in4_
                        args = in5_
                        prefix = in6_
                        raise _dafny.TailCall()
                elif True:
                    return Wrappers.Option_None()
                break

    @staticmethod
    def GetHelp(opts, prefix):
        d_130_newOpts_ = ((opts).params) + (_dafny.Seq([default__.HELP__PARAM]))
        d_131_longLen_ = default__.GetLongLen(d_130_newOpts_, 6)
        d_132_commandLen_ = default__.GetCommandLen(d_130_newOpts_, 0)
        if (d_132_commandLen_) == (0):
            return ((((((_dafny.Seq("USAGE : ")) + (prefix)) + ((opts).name)) + (_dafny.Seq(" [args...]\n"))) + ((opts).help)) + (_dafny.Seq("\n"))) + (default__.GetHelp2(d_130_newOpts_, d_131_longLen_))
        elif True:
            return ((((((((_dafny.Seq("USAGE : ")) + ((opts).name)) + (_dafny.Seq(" [args...] command [args...]\n"))) + ((opts).help)) + (_dafny.Seq("\n"))) + (_dafny.Seq("\nAvailable Commands:\n"))) + (default__.GetCmdHelp(d_130_newOpts_, d_132_commandLen_))) + (_dafny.Seq("\nAvailable Options:\n"))) + (default__.GetHelp2(d_130_newOpts_, d_131_longLen_))

    @staticmethod
    def OptValue(args, arg):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return Wrappers.Option_None()
                elif (((args)[0]).name) == (arg):
                    return ((args)[0]).value
                elif True:
                    in7_ = _dafny.Seq((args)[1::])
                    in8_ = arg
                    args = in7_
                    arg = in8_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagCount(args, arg):
        d_133___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return (0) + (d_133___accumulator_)
                elif (((args)[0]).name) == (arg):
                    d_133___accumulator_ = (d_133___accumulator_) + (1)
                    in9_ = _dafny.Seq((args)[1::])
                    in10_ = arg
                    args = in9_
                    arg = in10_
                    raise _dafny.TailCall()
                elif True:
                    in11_ = _dafny.Seq((args)[1::])
                    in12_ = arg
                    args = in11_
                    arg = in12_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OptMapLast(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theMap
                elif (((args)[0]).value).is_Some:
                    in13_ = _dafny.Seq((args)[1::])
                    in14_ = (theMap).set(((args)[0]).name, (((args)[0]).value).value)
                    args = in13_
                    theMap = in14_
                    raise _dafny.TailCall()
                elif True:
                    in15_ = _dafny.Seq((args)[1::])
                    in16_ = theMap
                    args = in15_
                    theMap = in16_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagsSet(args, theSet):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theSet
                elif (((args)[0]).value).is_Some:
                    in17_ = _dafny.Seq((args)[1::])
                    in18_ = theSet
                    args = in17_
                    theSet = in18_
                    raise _dafny.TailCall()
                elif True:
                    in19_ = _dafny.Seq((args)[1::])
                    in20_ = (theSet) | (_dafny.Set({((args)[0]).name}))
                    args = in19_
                    theSet = in20_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OptMapList(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theMap
                elif (((args)[0]).value).is_Some:
                    if (((args)[0]).name) in (theMap):
                        in21_ = _dafny.Seq((args)[1::])
                        in22_ = (theMap).set(((args)[0]).name, ((theMap)[((args)[0]).name]) + (_dafny.Seq([(((args)[0]).value).value])))
                        args = in21_
                        theMap = in22_
                        raise _dafny.TailCall()
                    elif True:
                        in23_ = _dafny.Seq((args)[1::])
                        in24_ = (theMap).set(((args)[0]).name, _dafny.Seq([(((args)[0]).value).value]))
                        args = in23_
                        theMap = in24_
                        raise _dafny.TailCall()
                elif True:
                    in25_ = _dafny.Seq((args)[1::])
                    in26_ = theMap
                    args = in25_
                    theMap = in26_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagMapCount(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theMap
                elif (((args)[0]).value).is_Some:
                    in27_ = _dafny.Seq((args)[1::])
                    in28_ = theMap
                    args = in27_
                    theMap = in28_
                    raise _dafny.TailCall()
                elif (((args)[0]).name) in (theMap):
                    in29_ = _dafny.Seq((args)[1::])
                    in30_ = (theMap).set(((args)[0]).name, ((theMap)[((args)[0]).name]) + (1))
                    args = in29_
                    theMap = in30_
                    raise _dafny.TailCall()
                elif True:
                    in31_ = _dafny.Seq((args)[1::])
                    in32_ = (theMap).set(((args)[0]).name, 1)
                    args = in31_
                    theMap = in32_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagSetCheck(args, theSet):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return Wrappers.Result_Success(theSet)
                elif (((args)[0]).value).is_Some:
                    if (((args)[0]).name) in (theSet):
                        return Wrappers.Result_Failure((_dafny.Seq("Duplicate arg : ")) + (((args)[0]).name))
                    elif True:
                        in33_ = _dafny.Seq((args)[1::])
                        in34_ = (theSet) | (_dafny.Set({((args)[0]).name}))
                        args = in33_
                        theSet = in34_
                        raise _dafny.TailCall()
                elif True:
                    in35_ = _dafny.Seq((args)[1::])
                    in36_ = theSet
                    args = in35_
                    theSet = in36_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OptMapCheck(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return Wrappers.Result_Success(theMap)
                elif (((args)[0]).value).is_Some:
                    if (((args)[0]).name) in (theMap):
                        return Wrappers.Result_Failure((_dafny.Seq("Duplicate arg : ")) + (((args)[0]).name))
                    elif True:
                        in37_ = _dafny.Seq((args)[1::])
                        in38_ = (theMap).set(((args)[0]).name, (((args)[0]).value).value)
                        args = in37_
                        theMap = in38_
                        raise _dafny.TailCall()
                elif True:
                    in39_ = _dafny.Seq((args)[1::])
                    in40_ = theMap
                    args = in39_
                    theMap = in40_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetHelpHelp(opt):
        if (opt).is_Command:
            return _dafny.Seq("")
        elif (opt).is_Flag:
            return (opt).help
        elif True:
            return ((opt).help) + ((_dafny.Seq(" (required)") if (opt).Required() else (((_dafny.Seq(" (default : ")) + (((opt).unused).val)) + (_dafny.Seq(")")) if (opt).HasDefault() else _dafny.Seq(""))))

    @staticmethod
    def OneHelp(opt, longLen):
        if ((opt).is_Command) or (not((opt).ShowHelp())):
            return _dafny.Seq("")
        elif True:
            return (((((default__.GetShortHelp(opt)) + (_dafny.Seq("  "))) + (default__.GetLongHelp(opt, longLen))) + (_dafny.Seq("  "))) + (default__.GetHelpHelp(opt))) + (_dafny.Seq("\n"))

    @staticmethod
    def GetCommandHelp(opt, commandLen):
        d_134_name_ = ((((opt).options).name) + (_dafny.Seq([' ' for d_135_i_ in range((commandLen) - (len(((opt).options).name)))])) if (len(((opt).options).name)) < (commandLen) else ((opt).options).name)
        return (((d_134_name_) + (_dafny.Seq("  "))) + (((opt).options).help)) + (_dafny.Seq("\n"))

    @staticmethod
    def GetShortHelp(opt):
        if ((opt).is_Opt) or ((opt).is_Flag):
            if ((opt).short) != (default__.NullChar):
                return (_dafny.Seq("-")) + (_dafny.Seq([(opt).short]))
            elif True:
                return _dafny.Seq("  ")
        elif True:
            return _dafny.Seq("")

    @staticmethod
    def GetLongHelp(opt, longLen):
        if ((opt).is_Opt) or ((opt).is_Flag):
            d_136_tmp_ = ((_dafny.Seq("--")) + ((opt).name)) + (((_dafny.Seq("=")) + ((opt).argName) if (opt).is_Opt else _dafny.Seq("")))
            if (len(d_136_tmp_)) < (longLen):
                return (d_136_tmp_) + (_dafny.Seq([' ' for d_137_i_ in range((longLen) - (len(d_136_tmp_)))]))
            elif True:
                return d_136_tmp_
        elif True:
            return _dafny.Seq("")

    @staticmethod
    def GetHelp2(opts, longLen):
        d_138___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return (d_138___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_139_x_ = default__.OneHelp((opts)[0], longLen)
                    d_138___accumulator_ = (d_138___accumulator_) + (d_139_x_)
                    in41_ = _dafny.Seq((opts)[1::])
                    in42_ = longLen
                    opts = in41_
                    longLen = in42_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetCmdHelp(opts, commandLen):
        d_140___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return (d_140___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_141_x_ = (default__.GetCommandHelp((opts)[0], commandLen) if ((opts)[0]).is_Command else _dafny.Seq(""))
                    d_140___accumulator_ = (d_140___accumulator_) + (d_141_x_)
                    in43_ = _dafny.Seq((opts)[1::])
                    in44_ = commandLen
                    opts = in43_
                    commandLen = in44_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetLongLen(opts, max):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return max
                elif True:
                    d_142_x_ = len(default__.GetLongHelp((opts)[0], 0))
                    d_143_newMax_ = (d_142_x_ if (d_142_x_) > (max) else max)
                    in45_ = _dafny.Seq((opts)[1::])
                    in46_ = d_143_newMax_
                    opts = in45_
                    max = in46_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetCommandLen(opts, max):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return max
                elif True:
                    d_144_x_ = (len((((opts)[0]).options).name) if ((opts)[0]).is_Command else 0)
                    d_145_newMax_ = (d_144_x_ if (d_144_x_) > (max) else max)
                    in47_ = _dafny.Seq((opts)[1::])
                    in48_ = d_145_newMax_
                    opts = in47_
                    max = in48_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AddShortAlias(aliases, shortMap, name):
        while True:
            with _dafny.label():
                if (len(aliases)) == (0):
                    return Wrappers.Result_Success(shortMap)
                elif ((aliases)[0]) in (shortMap):
                    return Wrappers.Result_Failure(((((_dafny.Seq("Short alias '")) + (_dafny.Seq((aliases)[0:1:]))) + (_dafny.Seq("' for '"))) + (name)) + (_dafny.Seq("' already in use as a short option.")))
                elif True:
                    in49_ = _dafny.Seq((aliases)[1::])
                    in50_ = (shortMap).set((aliases)[0], name)
                    in51_ = name
                    aliases = in49_
                    shortMap = in50_
                    name = in51_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AddLongAlias(aliases, longMap, opt):
        while True:
            with _dafny.label():
                if (len(aliases)) == (0):
                    return Wrappers.Result_Success(longMap)
                elif ((aliases)[0]) in (longMap):
                    return Wrappers.Result_Failure(((_dafny.Seq("Long alias '")) + ((aliases)[0])) + (_dafny.Seq("' already in use as a long option.")))
                elif True:
                    in52_ = _dafny.Seq((aliases)[1::])
                    in53_ = (longMap).set((aliases)[0], opt)
                    in54_ = opt
                    aliases = in52_
                    longMap = in53_
                    opt = in54_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetMaps(opts, longMap, shortMap, commandMap):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return Wrappers.Result_Success((longMap, shortMap, commandMap))
                elif True:
                    d_146_opt_ = (opts)[0]
                    if (d_146_opt_).is_Command:
                        d_147_valueOrError0_ = Wrappers.default__.Need((((d_146_opt_).options).name) not in (commandMap), (_dafny.Seq("Duplicate command in options : ")) + (((d_146_opt_).options).name))
                        if (d_147_valueOrError0_).IsFailure():
                            return (d_147_valueOrError0_).PropagateFailure()
                        elif True:
                            in55_ = _dafny.Seq((opts)[1::])
                            in56_ = longMap
                            in57_ = shortMap
                            in58_ = (commandMap).set(((d_146_opt_).options).name, (d_146_opt_).options)
                            opts = in55_
                            longMap = in56_
                            shortMap = in57_
                            commandMap = in58_
                            raise _dafny.TailCall()
                    elif True:
                        d_148_valueOrError1_ = Wrappers.default__.Need(((d_146_opt_).name) not in (longMap), (_dafny.Seq("Duplicate long name in options : ")) + ((d_146_opt_).name))
                        if (d_148_valueOrError1_).IsFailure():
                            return (d_148_valueOrError1_).PropagateFailure()
                        elif True:
                            d_149_longMap_ = (longMap).set((d_146_opt_).name, d_146_opt_)
                            d_150_valueOrError2_ = default__.AddShortAlias((d_146_opt_).ShortAlias(), shortMap, (d_146_opt_).name)
                            if (d_150_valueOrError2_).IsFailure():
                                return (d_150_valueOrError2_).PropagateFailure()
                            elif True:
                                d_151_shortMap_ = (d_150_valueOrError2_).Extract()
                                d_152_valueOrError3_ = default__.AddLongAlias((d_146_opt_).LongAlias(), d_149_longMap_, d_146_opt_)
                                if (d_152_valueOrError3_).IsFailure():
                                    return (d_152_valueOrError3_).PropagateFailure()
                                elif True:
                                    d_153_longMap_ = (d_152_valueOrError3_).Extract()
                                    if ((d_146_opt_).short) != (default__.NullChar):
                                        d_154_short_ = (d_146_opt_).short
                                        if (d_154_short_) in (d_151_shortMap_):
                                            return Wrappers.Result_Failure((((((_dafny.Seq("Duplicate short char in options : '")) + (_dafny.Seq([d_154_short_]))) + (_dafny.Seq("' for "))) + ((d_146_opt_).name)) + (_dafny.Seq(" and "))) + ((d_151_shortMap_)[d_154_short_]))
                                        elif True:
                                            in59_ = _dafny.Seq((opts)[1::])
                                            in60_ = (d_153_longMap_).set((d_146_opt_).name, d_146_opt_)
                                            in61_ = (d_151_shortMap_).set(d_154_short_, (d_146_opt_).name)
                                            in62_ = commandMap
                                            opts = in59_
                                            longMap = in60_
                                            shortMap = in61_
                                            commandMap = in62_
                                            raise _dafny.TailCall()
                                    elif True:
                                        in63_ = _dafny.Seq((opts)[1::])
                                        in64_ = (d_153_longMap_).set((d_146_opt_).name, d_146_opt_)
                                        in65_ = d_151_shortMap_
                                        in66_ = commandMap
                                        opts = in63_
                                        longMap = in64_
                                        shortMap = in65_
                                        commandMap = in66_
                                        raise _dafny.TailCall()
                break

    @staticmethod
    def Print(x):
        hresult_: Wrappers.Outcome = Wrappers.Outcome.default()()
        _dafny.print(_dafny.string_of(x))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = Wrappers.Outcome_Pass()
        return hresult_
        return hresult_

    @staticmethod
    def ArgExists(args, name):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return False
                elif (((args)[0]).name) == (name):
                    return True
                elif True:
                    in67_ = _dafny.Seq((args)[1::])
                    in68_ = name
                    args = in67_
                    name = in68_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def PostProcess2(opts, args, newArgs):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return Wrappers.Result_Success(newArgs)
                elif ((((opts)[0]).is_Opt) and (((opts)[0]).Required())) and (not(default__.ArgExists(args, ((opts)[0]).name))):
                    return Wrappers.Result_Failure(((_dafny.Seq("Option '")) + (((opts)[0]).name)) + (_dafny.Seq("' is required, but was not used.")))
                elif ((((opts)[0]).is_Opt) and (((opts)[0]).HasDefault())) and (not(default__.ArgExists(args, ((opts)[0]).name))):
                    in69_ = _dafny.Seq((opts)[1::])
                    in70_ = args
                    in71_ = (newArgs) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((((opts)[0]).unused).val))]))
                    opts = in69_
                    args = in70_
                    newArgs = in71_
                    raise _dafny.TailCall()
                elif True:
                    in72_ = _dafny.Seq((opts)[1::])
                    in73_ = args
                    in74_ = newArgs
                    opts = in72_
                    args = in73_
                    newArgs = in74_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetSubOptions(opts, name, pos):
        while True:
            with _dafny.label():
                if (len(opts)) == (pos):
                    return Wrappers.Option_None()
                elif (((opts)[pos]).is_Command) and (((((opts)[pos]).options).name) == (name)):
                    return Wrappers.Option_Some(pos)
                elif True:
                    in75_ = opts
                    in76_ = name
                    in77_ = (pos) + (1)
                    opts = in75_
                    name = in76_
                    pos = in77_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def PostProcess(opts, args):
        pat_let_tv0_ = args
        pat_let_tv1_ = args
        d_155_valueOrError0_ = default__.PostProcess2((opts).params, (args).params, _dafny.Seq([]))
        if (d_155_valueOrError0_).IsFailure():
            return (d_155_valueOrError0_).PropagateFailure()
        elif True:
            d_156_newParams_ = (d_155_valueOrError0_).Extract()
            if ((args).subcommand).is_Some:
                d_157_optPos_ = default__.GetSubOptions((opts).params, (((args).subcommand).value).command, 0)
                if (d_157_optPos_).is_Some:
                    d_158_valueOrError1_ = default__.PostProcess((((opts).params)[(d_157_optPos_).value]).options, ((args).subcommand).value)
                    if (d_158_valueOrError1_).IsFailure():
                        return (d_158_valueOrError1_).PropagateFailure()
                    elif True:
                        d_159_sub_ = (d_158_valueOrError1_).Extract()
                        def iife3_(_pat_let1_0):
                            def iife4_(d_160_dt__update__tmp_h0_):
                                def iife5_(_pat_let2_0):
                                    def iife6_(d_161_dt__update_hsubcommand_h0_):
                                        def iife7_(_pat_let3_0):
                                            def iife8_(d_162_dt__update_hparams_h0_):
                                                return Parsed_Parsed((d_160_dt__update__tmp_h0_).command, d_162_dt__update_hparams_h0_, (d_160_dt__update__tmp_h0_).files, d_161_dt__update_hsubcommand_h0_)
                                            return iife8_(_pat_let3_0)
                                        return iife7_(((pat_let_tv0_).params) + (d_156_newParams_))
                                    return iife6_(_pat_let2_0)
                                return iife5_(Wrappers.Option_Some(d_159_sub_))
                            return iife4_(_pat_let1_0)
                        return Wrappers.Result_Success(iife3_(args))
                elif True:
                    return Wrappers.Result_Failure(_dafny.Seq("Internal error in GetOpt::PostProcess"))
            elif True:
                def iife9_(_pat_let4_0):
                    def iife10_(d_163_dt__update__tmp_h1_):
                        def iife11_(_pat_let5_0):
                            def iife12_(d_164_dt__update_hparams_h1_):
                                return Parsed_Parsed((d_163_dt__update__tmp_h1_).command, d_164_dt__update_hparams_h1_, (d_163_dt__update__tmp_h1_).files, (d_163_dt__update__tmp_h1_).subcommand)
                            return iife12_(_pat_let5_0)
                        return iife11_(((pat_let_tv1_).params) + (d_156_newParams_))
                    return iife10_(_pat_let4_0)
                return Wrappers.Result_Success(iife9_(args))

    @staticmethod
    def AllDigits(s):
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return True
                elif (('0') <= ((s)[0])) and (((s)[0]) <= ('9')):
                    in78_ = _dafny.Seq((s)[1::])
                    s = in78_
                    raise _dafny.TailCall()
                elif True:
                    return False
                break

    @staticmethod
    def ValidPositional(s):
        if (len(s)) == (0):
            return True
        elif ((s)[0]) != ('-'):
            return True
        elif True:
            return default__.AllDigits(_dafny.Seq((s)[1::]))

    @staticmethod
    def TestPositionals(opts, optional):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return Wrappers.Outcome_Pass()
                elif not(((opts)[0]).is_Opt):
                    in79_ = _dafny.Seq((opts)[1::])
                    in80_ = optional
                    opts = in79_
                    optional = in80_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_No()):
                    in81_ = _dafny.Seq((opts)[1::])
                    in82_ = optional
                    opts = in81_
                    optional = in82_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_Maybe()):
                    in83_ = _dafny.Seq((opts)[1::])
                    in84_ = Wrappers.Option_Some(((opts)[0]).name)
                    opts = in83_
                    optional = in84_
                    raise _dafny.TailCall()
                elif (optional).is_None:
                    in85_ = _dafny.Seq((opts)[1::])
                    in86_ = optional
                    opts = in85_
                    optional = in86_
                    raise _dafny.TailCall()
                elif True:
                    return Wrappers.Outcome_Fail(((((_dafny.Seq("Required positional argument '")) + (((opts)[0]).name)) + (_dafny.Seq("' follows optional positional argument '"))) + ((optional).value)) + (_dafny.Seq("'.")))
                break

    @staticmethod
    def GetPositionals(opts, args, params):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return Wrappers.Result_Success((args, params))
                elif not(((opts)[0]).is_Opt):
                    in87_ = _dafny.Seq((opts)[1::])
                    in88_ = args
                    in89_ = params
                    opts = in87_
                    args = in88_
                    params = in89_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_No()):
                    in90_ = _dafny.Seq((opts)[1::])
                    in91_ = args
                    in92_ = params
                    opts = in90_
                    args = in91_
                    params = in92_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_Yes()):
                    if (len(args)) == (0):
                        return Wrappers.Result_Failure(((_dafny.Seq("Positional arg '")) + (((opts)[0]).name)) + (_dafny.Seq("' is required, but we've run out of arguments.")))
                    elif default__.ValidPositional((args)[0]):
                        in93_ = _dafny.Seq((opts)[1::])
                        in94_ = _dafny.Seq((args)[1::])
                        in95_ = (params) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((args)[0]))]))
                        opts = in93_
                        args = in94_
                        params = in95_
                        raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Failure(((((_dafny.Seq("Positional arg ")) + (((opts)[0]).name)) + (_dafny.Seq(" matched with invalid positional value '"))) + ((args)[0])) + (_dafny.Seq("'.")))
                elif True:
                    if (len(args)) == (0):
                        return Wrappers.Result_Success((args, params))
                    elif default__.ValidPositional((args)[0]):
                        in96_ = _dafny.Seq((opts)[1::])
                        in97_ = _dafny.Seq((args)[1::])
                        in98_ = (params) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((args)[0]))]))
                        opts = in96_
                        args = in97_
                        params = in98_
                        raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Success((args, params))
                break

    @staticmethod
    def GetOptions(opts, args):
        d_165_newOpts_ = ((opts).params) + (_dafny.Seq([default__.HELP__PARAM]))
        def lambda0_(d_167_o_):
            return (d_167_o_).Inherits()

        d_166_inherits_ = default__.Filter(lambda0_, d_165_newOpts_)
        d_168_valueOrError0_ = default__.TestPositionals(d_165_newOpts_, Wrappers.Option_None())
        if (d_168_valueOrError0_).IsFailure():
            return (d_168_valueOrError0_).PropagateFailure()
        elif True:
            d_169_valueOrError1_ = default__.GetPositionals(d_165_newOpts_, _dafny.Seq((args)[1::]), _dafny.Seq([]))
            if (d_169_valueOrError1_).IsFailure():
                return (d_169_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs0_ = (d_169_valueOrError1_).Extract()
                d_170_newArgs_ = let_tmp_rhs0_[0]
                d_171_params_ = let_tmp_rhs0_[1]
                d_172_valueOrError2_ = default__.GetMaps(d_165_newOpts_, _dafny.Map({}), _dafny.Map({}), _dafny.Map({}))
                if (d_172_valueOrError2_).IsFailure():
                    return (d_172_valueOrError2_).PropagateFailure()
                elif True:
                    let_tmp_rhs1_ = (d_172_valueOrError2_).Extract()
                    d_173_longMap_ = let_tmp_rhs1_[0]
                    d_174_shortMap_ = let_tmp_rhs1_[1]
                    d_175_commandMap_ = let_tmp_rhs1_[2]
                    d_176_context_ = Context_Context(d_173_longMap_, d_174_shortMap_, d_166_inherits_, d_175_commandMap_, (args)[0])
                    d_177_valueOrError3_ = default__.GetOptions2(d_170_newArgs_, d_176_context_, d_171_params_, _dafny.Seq([]))
                    if (d_177_valueOrError3_).IsFailure():
                        return (d_177_valueOrError3_).PropagateFailure()
                    elif True:
                        d_178_result_ = (d_177_valueOrError3_).Extract()
                        return default__.PostProcess(opts, d_178_result_)

    @staticmethod
    def IndexOf(xs, v):
        d_179___accumulator_ = 0
        while True:
            with _dafny.label():
                if ((xs)[0]) == (v):
                    return (0) + (d_179___accumulator_)
                elif True:
                    d_179___accumulator_ = (d_179___accumulator_) + (1)
                    in99_ = _dafny.Seq((xs)[1::])
                    in100_ = v
                    xs = in99_
                    v = in100_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SplitOnce(s, delim):
        d_180_i_ = default__.IndexOf(s, delim)
        return (_dafny.Seq((s)[:d_180_i_:]), _dafny.Seq((s)[(d_180_i_) + (1)::]))

    @staticmethod
    def GetOptions2(args, context, parms, files):
        if (len(args)) == (0):
            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, files, Wrappers.Option_None()))
        elif ((args)[0]) in ((context).commands):
            def lambda1_(d_182_o_):
                return (d_182_o_).Inherits()

            d_181_inherits_ = default__.Filter(lambda1_, (((context).commands)[(args)[0]]).params)
            d_183_newOpts_ = ((((context).commands)[(args)[0]]).params) + ((context).inherits)
            d_184_valueOrError0_ = default__.TestPositionals(d_183_newOpts_, Wrappers.Option_None())
            if (d_184_valueOrError0_).IsFailure():
                return (d_184_valueOrError0_).PropagateFailure()
            elif True:
                d_185_valueOrError1_ = default__.GetPositionals(d_183_newOpts_, _dafny.Seq((args)[1::]), _dafny.Seq([]))
                if (d_185_valueOrError1_).IsFailure():
                    return (d_185_valueOrError1_).PropagateFailure()
                elif True:
                    let_tmp_rhs2_ = (d_185_valueOrError1_).Extract()
                    d_186_newArgs_ = let_tmp_rhs2_[0]
                    d_187_params_ = let_tmp_rhs2_[1]
                    d_188_valueOrError2_ = default__.GetMaps(d_183_newOpts_, _dafny.Map({}), _dafny.Map({}), _dafny.Map({}))
                    if (d_188_valueOrError2_).IsFailure():
                        return (d_188_valueOrError2_).PropagateFailure()
                    elif True:
                        let_tmp_rhs3_ = (d_188_valueOrError2_).Extract()
                        d_189_longMap_ = let_tmp_rhs3_[0]
                        d_190_shortMap_ = let_tmp_rhs3_[1]
                        d_191_commandSet_ = let_tmp_rhs3_[2]
                        d_192_newContext_ = Context_Context(d_189_longMap_, d_190_shortMap_, ((context).inherits) + (d_181_inherits_), d_191_commandSet_, (args)[0])
                        d_193_lostArgs_ = (len(args)) - (len(d_186_newArgs_))
                        d_194_valueOrError3_ = default__.GetOptions2(_dafny.Seq((args)[d_193_lostArgs_::]), d_192_newContext_, d_187_params_, _dafny.Seq([]))
                        if (d_194_valueOrError3_).IsFailure():
                            return (d_194_valueOrError3_).PropagateFailure()
                        elif True:
                            d_195_result_ = (d_194_valueOrError3_).Extract()
                            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, files, Wrappers.Option_Some(d_195_result_)))
        elif ((args)[0]) == (_dafny.Seq("--")):
            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, (files) + (_dafny.Seq((args)[1::])), Wrappers.Option_None()))
        elif (_dafny.Seq("--")) < ((args)[0]):
            d_196_longOpt_ = _dafny.Seq(((args)[0])[2::])
            if ('=') in (d_196_longOpt_):
                let_tmp_rhs4_ = default__.SplitOnce(d_196_longOpt_, '=')
                d_197_opt_ = let_tmp_rhs4_[0]
                d_198_arg_ = let_tmp_rhs4_[1]
                if (d_197_opt_) in ((context).longMap):
                    if (((context).longMap)[d_197_opt_]).NeedsArg():
                        return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + ((((context).longMap)[d_197_opt_]).MakeArg(Wrappers.Option_Some(d_198_arg_))), files)
                    elif True:
                        return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_197_opt_)) + (_dafny.Seq(" does not take an argument, but it got one.")))
                elif True:
                    return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_197_opt_)) + (_dafny.Seq(" not recognized.")))
            elif (d_196_longOpt_) in ((context).longMap):
                d_199_opt_ = ((context).longMap)[d_196_longOpt_]
                if (d_199_opt_).NeedsArg():
                    if (len(args)) < (2):
                        return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_196_longOpt_)) + (_dafny.Seq(" requires an argument, but didn't get one.")))
                    elif True:
                        return default__.GetOptions2(_dafny.Seq((args)[2::]), context, (parms) + ((d_199_opt_).MakeArg(Wrappers.Option_Some((args)[1]))), files)
                elif (((d_199_opt_).is_Flag) and ((d_199_opt_).solo)) and ((((len(args)) != (1)) or ((len(parms)) != (0))) or ((len(files)) != (0))):
                    return Wrappers.Result_Failure(((_dafny.Seq("Option '")) + (d_196_longOpt_)) + (_dafny.Seq("' used with other stuff, but must only be used alone.")))
                elif True:
                    return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + ((d_199_opt_).MakeArg(Wrappers.Option_None())), files)
            elif True:
                return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_196_longOpt_)) + (_dafny.Seq(" not recognized.")))
        elif (_dafny.Seq("-")) == ((args)[0]):
            return default__.GetOptions2(_dafny.Seq((args)[1::]), context, parms, (files) + (_dafny.Seq([(args)[0]])))
        elif (_dafny.Seq("-")) < ((args)[0]):
            d_200_valueOrError4_ = default__.GetShort(_dafny.Seq(((args)[0])[1::]), (context).longMap, (context).shortMap, _dafny.Seq([]))
            if (d_200_valueOrError4_).IsFailure():
                return (d_200_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs5_ = (d_200_valueOrError4_).Extract()
                d_201_newParms_ = let_tmp_rhs5_[0]
                d_202_nextParm_ = let_tmp_rhs5_[1]
                if (d_202_nextParm_).is_None:
                    return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + (d_201_newParms_), files)
                elif (len(args)) == (1):
                    return Wrappers.Result_Failure(((_dafny.Seq("Short option ")) + (_dafny.Seq([(d_202_nextParm_).value]))) + (_dafny.Seq(" requires argument but didn't get one.")))
                elif True:
                    d_203_longOpt_ = ((context).shortMap)[(d_202_nextParm_).value]
                    d_204_opt_ = ((context).longMap)[d_203_longOpt_]
                    return default__.GetOptions2(_dafny.Seq((args)[2::]), context, ((parms) + (d_201_newParms_)) + ((d_204_opt_).MakeArg(Wrappers.Option_Some((args)[1]))), files)
        elif (len((context).commands)) == (0):
            return default__.GetOptions2(_dafny.Seq((args)[1::]), context, parms, (files) + (_dafny.Seq([(args)[0]])))
        elif True:
            return Wrappers.Result_Failure(((((((_dafny.Seq("Unrecognized command ")) + ((args)[0])) + (_dafny.Seq(" for "))) + ((context).command)) + (_dafny.Seq("\nRun '"))) + ((context).command)) + (_dafny.Seq(" --help' for usage.")))

    @staticmethod
    def GetShort(arg, longMap, shortMap, parms):
        while True:
            with _dafny.label():
                if (len(arg)) == (0):
                    return Wrappers.Result_Success((parms, Wrappers.Option_None()))
                elif True:
                    d_205_ch_ = (arg)[0]
                    if (d_205_ch_) in (shortMap):
                        d_206_opt_ = (shortMap)[d_205_ch_]
                        if ((longMap)[d_206_opt_]).NeedsArg():
                            if (len(arg)) == (1):
                                return Wrappers.Result_Success((parms, Wrappers.Option_Some(d_205_ch_)))
                            elif True:
                                return Wrappers.Result_Success(((parms) + (((longMap)[d_206_opt_]).MakeArg(Wrappers.Option_Some(_dafny.Seq((arg)[1::])))), Wrappers.Option_None()))
                        elif True:
                            in101_ = _dafny.Seq((arg)[1::])
                            in102_ = longMap
                            in103_ = shortMap
                            in104_ = (parms) + (((longMap)[d_206_opt_]).MakeArg(Wrappers.Option_None()))
                            arg = in101_
                            longMap = in102_
                            shortMap = in103_
                            parms = in104_
                            raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Failure(((_dafny.Seq("Short option '")) + (_dafny.Seq([d_205_ch_]))) + (_dafny.Seq("' not recognized.")))
                break

    @_dafny.classproperty
    def NullChar(instance):
        return chr(0)
    @_dafny.classproperty
    def HELP__STR(instance):
        return _dafny.Seq("help")
    @_dafny.classproperty
    def HELP__PARAM(instance):
        return Param_Flag(default__.HELP__STR, _dafny.Seq("This help text."), default__.NullChar, True, True, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))

class Tri:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [Tri_Yes(), Tri_No(), Tri_Maybe()]
    @classmethod
    def default(cls, ):
        return lambda: Tri_Yes()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Yes(self) -> bool:
        return isinstance(self, Tri_Yes)
    @property
    def is_No(self) -> bool:
        return isinstance(self, Tri_No)
    @property
    def is_Maybe(self) -> bool:
        return isinstance(self, Tri_Maybe)

class Tri_Yes(Tri, NamedTuple('Yes', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Tri.Yes'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Tri_Yes)
    def __hash__(self) -> int:
        return super().__hash__()

class Tri_No(Tri, NamedTuple('No', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Tri.No'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Tri_No)
    def __hash__(self) -> int:
        return super().__hash__()

class Tri_Maybe(Tri, NamedTuple('Maybe', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Tri.Maybe'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Tri_Maybe)
    def __hash__(self) -> int:
        return super().__hash__()


class Visibility:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [Visibility_Normal(), Visibility_Hidden(), Visibility_Deprecated()]
    @classmethod
    def default(cls, ):
        return lambda: Visibility_Normal()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Normal(self) -> bool:
        return isinstance(self, Visibility_Normal)
    @property
    def is_Hidden(self) -> bool:
        return isinstance(self, Visibility_Hidden)
    @property
    def is_Deprecated(self) -> bool:
        return isinstance(self, Visibility_Deprecated)

class Visibility_Normal(Visibility, NamedTuple('Normal', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Visibility.Normal'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Visibility_Normal)
    def __hash__(self) -> int:
        return super().__hash__()

class Visibility_Hidden(Visibility, NamedTuple('Hidden', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Visibility.Hidden'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Visibility_Hidden)
    def __hash__(self) -> int:
        return super().__hash__()

class Visibility_Deprecated(Visibility, NamedTuple('Deprecated', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Visibility.Deprecated'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Visibility_Deprecated)
    def __hash__(self) -> int:
        return super().__hash__()


class Options:
    @classmethod
    def default(cls, ):
        return lambda: Options_Options(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Options(self) -> bool:
        return isinstance(self, Options_Options)

class Options_Options(Options, NamedTuple('Options', [('name', Any), ('help', Any), ('params', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Options.Options({_dafny.string_of(self.name)}, {_dafny.string_of(self.help)}, {_dafny.string_of(self.params)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Options_Options) and self.name == __o.name and self.help == __o.help and self.params == __o.params
    def __hash__(self) -> int:
        return super().__hash__()


class Unused:
    @classmethod
    def default(cls, ):
        return lambda: Unused_UnusedOk()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnusedOk(self) -> bool:
        return isinstance(self, Unused_UnusedOk)
    @property
    def is_Required(self) -> bool:
        return isinstance(self, Unused_Required)
    @property
    def is_Default(self) -> bool:
        return isinstance(self, Unused_Default)

class Unused_UnusedOk(Unused, NamedTuple('UnusedOk', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Unused.UnusedOk'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Unused_UnusedOk)
    def __hash__(self) -> int:
        return super().__hash__()

class Unused_Required(Unused, NamedTuple('Required', [])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Unused.Required'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Unused_Required)
    def __hash__(self) -> int:
        return super().__hash__()

class Unused_Default(Unused, NamedTuple('Default', [('val', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Unused.Default({_dafny.string_of(self.val)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Unused_Default) and self.val == __o.val
    def __hash__(self) -> int:
        return super().__hash__()


class Param:
    @classmethod
    def default(cls, ):
        return lambda: Param_Opt(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), 'D', Unused.default()(), False, Visibility.default()(), _dafny.Seq({}), _dafny.Seq({}), Tri.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Opt(self) -> bool:
        return isinstance(self, Param_Opt)
    @property
    def is_Flag(self) -> bool:
        return isinstance(self, Param_Flag)
    @property
    def is_Command(self) -> bool:
        return isinstance(self, Param_Command)
    def NeedsArg(self):
        return (self).is_Opt

    def Inherits(self):
        return (((self).is_Opt) or ((self).is_Flag)) and ((self).inherit)

    def ShowHelp(self):
        return ((self).is_Command) or (((self).vis) == (Visibility_Normal()))

    def KeepResult(self):
        return ((self).is_Command) or (((self).vis) != (Visibility_Deprecated()))

    def Name(self):
        if (self).is_Command:
            return ((self).options).name
        elif True:
            return (self).name

    def MakeArg(self, value):
        if (self).KeepResult():
            return _dafny.Seq([OneArg_OneArg((self).Name(), value)])
        elif True:
            return _dafny.Seq([])

    def ShortAlias(self):
        if (self).is_Command:
            return _dafny.Seq([])
        elif True:
            return (self).shortAlias

    def LongAlias(self):
        if (self).is_Command:
            return _dafny.Seq([])
        elif True:
            return (self).longAlias

    def Required(self):
        return ((self).is_Opt) and (((self).unused).is_Required)

    def HasDefault(self):
        return ((self).is_Opt) and (((self).unused).is_Default)


class Param_Opt(Param, NamedTuple('Opt', [('name', Any), ('help', Any), ('argName', Any), ('short', Any), ('unused', Any), ('inherit', Any), ('vis', Any), ('shortAlias', Any), ('longAlias', Any), ('positional', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Param.Opt({_dafny.string_of(self.name)}, {_dafny.string_of(self.help)}, {_dafny.string_of(self.argName)}, {_dafny.string_of(self.short)}, {_dafny.string_of(self.unused)}, {_dafny.string_of(self.inherit)}, {_dafny.string_of(self.vis)}, {_dafny.string_of(self.shortAlias)}, {_dafny.string_of(self.longAlias)}, {_dafny.string_of(self.positional)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Param_Opt) and self.name == __o.name and self.help == __o.help and self.argName == __o.argName and self.short == __o.short and self.unused == __o.unused and self.inherit == __o.inherit and self.vis == __o.vis and self.shortAlias == __o.shortAlias and self.longAlias == __o.longAlias and self.positional == __o.positional
    def __hash__(self) -> int:
        return super().__hash__()

class Param_Flag(Param, NamedTuple('Flag', [('name', Any), ('help', Any), ('short', Any), ('solo', Any), ('inherit', Any), ('vis', Any), ('shortAlias', Any), ('longAlias', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Param.Flag({_dafny.string_of(self.name)}, {_dafny.string_of(self.help)}, {_dafny.string_of(self.short)}, {_dafny.string_of(self.solo)}, {_dafny.string_of(self.inherit)}, {_dafny.string_of(self.vis)}, {_dafny.string_of(self.shortAlias)}, {_dafny.string_of(self.longAlias)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Param_Flag) and self.name == __o.name and self.help == __o.help and self.short == __o.short and self.solo == __o.solo and self.inherit == __o.inherit and self.vis == __o.vis and self.shortAlias == __o.shortAlias and self.longAlias == __o.longAlias
    def __hash__(self) -> int:
        return super().__hash__()

class Param_Command(Param, NamedTuple('Command', [('options', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Param.Command({_dafny.string_of(self.options)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Param_Command) and self.options == __o.options
    def __hash__(self) -> int:
        return super().__hash__()


class OneArg:
    @classmethod
    def default(cls, ):
        return lambda: OneArg_OneArg(_dafny.Seq({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OneArg(self) -> bool:
        return isinstance(self, OneArg_OneArg)

class OneArg_OneArg(OneArg, NamedTuple('OneArg', [('name', Any), ('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.OneArg.OneArg({_dafny.string_of(self.name)}, {_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OneArg_OneArg) and self.name == __o.name and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()


class Parsed:
    @classmethod
    def default(cls, ):
        return lambda: Parsed_Parsed(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Parsed(self) -> bool:
        return isinstance(self, Parsed_Parsed)

class Parsed_Parsed(Parsed, NamedTuple('Parsed', [('command', Any), ('params', Any), ('files', Any), ('subcommand', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Parsed.Parsed({_dafny.string_of(self.command)}, {_dafny.string_of(self.params)}, {_dafny.string_of(self.files)}, {_dafny.string_of(self.subcommand)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Parsed_Parsed) and self.command == __o.command and self.params == __o.params and self.files == __o.files and self.subcommand == __o.subcommand
    def __hash__(self) -> int:
        return super().__hash__()


class CommandMap:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})

class Context:
    @classmethod
    def default(cls, ):
        return lambda: Context_Context(_dafny.Map({}), _dafny.Map({}), _dafny.Seq({}), _dafny.Map({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Context(self) -> bool:
        return isinstance(self, Context_Context)

class Context_Context(Context, NamedTuple('Context', [('longMap', Any), ('shortMap', Any), ('inherits', Any), ('commands', Any), ('command', Any)])):
    def __dafnystr__(self) -> str:
        return f'GetOpt.Context.Context({_dafny.string_of(self.longMap)}, {_dafny.string_of(self.shortMap)}, {_dafny.string_of(self.inherits)}, {_dafny.string_of(self.commands)}, {_dafny.string_of(self.command)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Context_Context) and self.longMap == __o.longMap and self.shortMap == __o.shortMap and self.inherits == __o.inherits and self.commands == __o.commands and self.command == __o.command
    def __hash__(self) -> int:
        return super().__hash__()

