import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings

# Module: GetOpt

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Example(args):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_0_MyOptions_: _dafny.Seq
        d_0_MyOptions_ = _dafny.Seq([Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), default__.NullChar, False, False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', Unused_UnusedOk(), False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), Tri_No()), Param_Command(Options_Options(_dafny.Seq("command"), _dafny.Seq("Does command stuff"), _dafny.Seq([Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', Unused_UnusedOk(), False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), Tri_No()), Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), default__.NullChar, False, False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))])))])
        d_1_opts_: Options
        d_1_opts_ = Options_Options(_dafny.Seq("myProg"), _dafny.Seq("does prog stuff"), d_0_MyOptions_)
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(Parsed.default())()
        d_2_valueOrError0_ = default__.GetOptions(d_1_opts_, args)
        if (d_2_valueOrError0_).IsFailure():
            output = (d_2_valueOrError0_).PropagateFailure()
            return output
        d_3_x_: Parsed
        d_3_x_ = (d_2_valueOrError0_).Extract()
        d_4_h_: Wrappers.Option
        d_4_h_ = default__.NeedsHelp(d_1_opts_, d_3_x_, _dafny.Seq(""))
        if (d_4_h_).is_Some:
            _dafny.print(_dafny.string_of((d_4_h_).value))
            output = Wrappers.Result_Success(True)
            return output
        output = Wrappers.Result_Success(True)
        return output
        return output

    @staticmethod
    def Filter(f, xs):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((_dafny.Seq([(xs)[0]]) if f((xs)[0]) else _dafny.Seq([])))
                    in0_ = f
                    in1_ = _dafny.Seq((xs)[1::])
                    f = in0_
                    xs = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IsHelp(args):
        return ((len((args).params)) != (0)) and (((((args).params)[0]).name) == (default__.HELP__STR))

    @staticmethod
    def NeedsHelp(opts, args, prefix):
        while True:
            with _dafny.label():
                if default__.IsHelp(args):
                    return Wrappers.Option_Some(default__.GetHelp(opts, prefix))
                elif ((args).subcommand).is_Some:
                    d_0_valueOrError0_ = default__.GetSubOptions((opts).params, (((args).subcommand).value).command, 0)
                    if (d_0_valueOrError0_).IsFailure():
                        return (d_0_valueOrError0_).PropagateFailure()
                    elif True:
                        d_1_pos_ = (d_0_valueOrError0_).Extract()
                        in0_ = (((opts).params)[d_1_pos_]).options
                        in1_ = ((args).subcommand).value
                        in2_ = ((prefix) + ((args).command)) + (_dafny.Seq(" "))
                        opts = in0_
                        args = in1_
                        prefix = in2_
                        raise _dafny.TailCall()
                elif True:
                    return Wrappers.Option_None()
                break

    @staticmethod
    def GetHelp(opts, prefix):
        d_0_newOpts_ = ((opts).params) + (_dafny.Seq([default__.HELP__PARAM]))
        d_1_longLen_ = default__.GetLongLen(d_0_newOpts_, 6)
        d_2_commandLen_ = default__.GetCommandLen(d_0_newOpts_, 0)
        if (d_2_commandLen_) == (0):
            return ((((((_dafny.Seq("USAGE : ")) + (prefix)) + ((opts).name)) + (_dafny.Seq(" [args...]\n"))) + ((opts).help)) + (_dafny.Seq("\n"))) + (default__.GetHelp2(d_0_newOpts_, d_1_longLen_))
        elif True:
            return ((((((((_dafny.Seq("USAGE : ")) + ((opts).name)) + (_dafny.Seq(" [args...] command [args...]\n"))) + ((opts).help)) + (_dafny.Seq("\n"))) + (_dafny.Seq("\nAvailable Commands:\n"))) + (default__.GetCmdHelp(d_0_newOpts_, d_2_commandLen_))) + (_dafny.Seq("\nAvailable Options:\n"))) + (default__.GetHelp2(d_0_newOpts_, d_1_longLen_))

    @staticmethod
    def OptValue(args, arg):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return Wrappers.Option_None()
                elif (((args)[0]).name) == (arg):
                    return ((args)[0]).value
                elif True:
                    in0_ = _dafny.Seq((args)[1::])
                    in1_ = arg
                    args = in0_
                    arg = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagCount(args, arg):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return (0) + (d_0___accumulator_)
                elif (((args)[0]).name) == (arg):
                    d_0___accumulator_ = (d_0___accumulator_) + (1)
                    in0_ = _dafny.Seq((args)[1::])
                    in1_ = arg
                    args = in0_
                    arg = in1_
                    raise _dafny.TailCall()
                elif True:
                    in2_ = _dafny.Seq((args)[1::])
                    in3_ = arg
                    args = in2_
                    arg = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OptMapLast(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theMap
                elif (((args)[0]).value).is_Some:
                    in0_ = _dafny.Seq((args)[1::])
                    in1_ = (theMap).set(((args)[0]).name, (((args)[0]).value).value)
                    args = in0_
                    theMap = in1_
                    raise _dafny.TailCall()
                elif True:
                    in2_ = _dafny.Seq((args)[1::])
                    in3_ = theMap
                    args = in2_
                    theMap = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagsSet(args, theSet):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theSet
                elif (((args)[0]).value).is_Some:
                    in0_ = _dafny.Seq((args)[1::])
                    in1_ = theSet
                    args = in0_
                    theSet = in1_
                    raise _dafny.TailCall()
                elif True:
                    in2_ = _dafny.Seq((args)[1::])
                    in3_ = (theSet) | (_dafny.Set({((args)[0]).name}))
                    args = in2_
                    theSet = in3_
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
                        in0_ = _dafny.Seq((args)[1::])
                        in1_ = (theMap).set(((args)[0]).name, ((theMap)[((args)[0]).name]) + (_dafny.Seq([(((args)[0]).value).value])))
                        args = in0_
                        theMap = in1_
                        raise _dafny.TailCall()
                    elif True:
                        in2_ = _dafny.Seq((args)[1::])
                        in3_ = (theMap).set(((args)[0]).name, _dafny.Seq([(((args)[0]).value).value]))
                        args = in2_
                        theMap = in3_
                        raise _dafny.TailCall()
                elif True:
                    in4_ = _dafny.Seq((args)[1::])
                    in5_ = theMap
                    args = in4_
                    theMap = in5_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagMapCount(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theMap
                elif (((args)[0]).value).is_Some:
                    in0_ = _dafny.Seq((args)[1::])
                    in1_ = theMap
                    args = in0_
                    theMap = in1_
                    raise _dafny.TailCall()
                elif (((args)[0]).name) in (theMap):
                    in2_ = _dafny.Seq((args)[1::])
                    in3_ = (theMap).set(((args)[0]).name, ((theMap)[((args)[0]).name]) + (1))
                    args = in2_
                    theMap = in3_
                    raise _dafny.TailCall()
                elif True:
                    in4_ = _dafny.Seq((args)[1::])
                    in5_ = (theMap).set(((args)[0]).name, 1)
                    args = in4_
                    theMap = in5_
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
                        in0_ = _dafny.Seq((args)[1::])
                        in1_ = (theSet) | (_dafny.Set({((args)[0]).name}))
                        args = in0_
                        theSet = in1_
                        raise _dafny.TailCall()
                elif True:
                    in2_ = _dafny.Seq((args)[1::])
                    in3_ = theSet
                    args = in2_
                    theSet = in3_
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
                        in0_ = _dafny.Seq((args)[1::])
                        in1_ = (theMap).set(((args)[0]).name, (((args)[0]).value).value)
                        args = in0_
                        theMap = in1_
                        raise _dafny.TailCall()
                elif True:
                    in2_ = _dafny.Seq((args)[1::])
                    in3_ = theMap
                    args = in2_
                    theMap = in3_
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
        d_0_name_ = ((((opt).options).name) + (_dafny.Seq([' ' for d_1_i_ in range((commandLen) - (len(((opt).options).name)))])) if (len(((opt).options).name)) < (commandLen) else ((opt).options).name)
        return (((d_0_name_) + (_dafny.Seq("  "))) + (((opt).options).help)) + (_dafny.Seq("\n"))

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
            d_0_tmp_ = ((_dafny.Seq("--")) + ((opt).name)) + (((_dafny.Seq("=")) + ((opt).argName) if (opt).is_Opt else _dafny.Seq("")))
            if (len(d_0_tmp_)) < (longLen):
                return (d_0_tmp_) + (_dafny.Seq([' ' for d_1_i_ in range((longLen) - (len(d_0_tmp_)))]))
            elif True:
                return d_0_tmp_
        elif True:
            return _dafny.Seq("")

    @staticmethod
    def GetHelp2(opts, longLen):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_1_x_ = default__.OneHelp((opts)[0], longLen)
                    d_0___accumulator_ = (d_0___accumulator_) + (d_1_x_)
                    in0_ = _dafny.Seq((opts)[1::])
                    in1_ = longLen
                    opts = in0_
                    longLen = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetCmdHelp(opts, commandLen):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_1_x_ = (default__.GetCommandHelp((opts)[0], commandLen) if ((opts)[0]).is_Command else _dafny.Seq(""))
                    d_0___accumulator_ = (d_0___accumulator_) + (d_1_x_)
                    in0_ = _dafny.Seq((opts)[1::])
                    in1_ = commandLen
                    opts = in0_
                    commandLen = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetLongLen(opts, max):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return max
                elif True:
                    d_0_x_ = len(default__.GetLongHelp((opts)[0], 0))
                    d_1_newMax_ = (d_0_x_ if (d_0_x_) > (max) else max)
                    in0_ = _dafny.Seq((opts)[1::])
                    in1_ = d_1_newMax_
                    opts = in0_
                    max = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetCommandLen(opts, max):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return max
                elif True:
                    d_0_x_ = (len((((opts)[0]).options).name) if ((opts)[0]).is_Command else 0)
                    d_1_newMax_ = (d_0_x_ if (d_0_x_) > (max) else max)
                    in0_ = _dafny.Seq((opts)[1::])
                    in1_ = d_1_newMax_
                    opts = in0_
                    max = in1_
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
                    in0_ = _dafny.Seq((aliases)[1::])
                    in1_ = (shortMap).set((aliases)[0], name)
                    in2_ = name
                    aliases = in0_
                    shortMap = in1_
                    name = in2_
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
                    in0_ = _dafny.Seq((aliases)[1::])
                    in1_ = (longMap).set((aliases)[0], opt)
                    in2_ = opt
                    aliases = in0_
                    longMap = in1_
                    opt = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetMaps(opts, longMap, shortMap, commandMap):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return Wrappers.Result_Success((longMap, shortMap, commandMap))
                elif True:
                    d_0_opt_ = (opts)[0]
                    if (d_0_opt_).is_Command:
                        d_1_valueOrError0_ = Wrappers.default__.Need((((d_0_opt_).options).name) not in (commandMap), (_dafny.Seq("Duplicate command in options : ")) + (((d_0_opt_).options).name))
                        if (d_1_valueOrError0_).IsFailure():
                            return (d_1_valueOrError0_).PropagateFailure()
                        elif True:
                            in0_ = _dafny.Seq((opts)[1::])
                            in1_ = longMap
                            in2_ = shortMap
                            in3_ = (commandMap).set(((d_0_opt_).options).name, (d_0_opt_).options)
                            opts = in0_
                            longMap = in1_
                            shortMap = in2_
                            commandMap = in3_
                            raise _dafny.TailCall()
                    elif True:
                        d_2_valueOrError1_ = Wrappers.default__.Need(((d_0_opt_).name) not in (longMap), (_dafny.Seq("Duplicate long name in options : ")) + ((d_0_opt_).name))
                        if (d_2_valueOrError1_).IsFailure():
                            return (d_2_valueOrError1_).PropagateFailure()
                        elif True:
                            d_3_newLongMap_ = (longMap).set((d_0_opt_).name, d_0_opt_)
                            d_4_valueOrError2_ = default__.AddShortAlias((d_0_opt_).ShortAlias(), shortMap, (d_0_opt_).name)
                            if (d_4_valueOrError2_).IsFailure():
                                return (d_4_valueOrError2_).PropagateFailure()
                            elif True:
                                d_5_newShortMap_ = (d_4_valueOrError2_).Extract()
                                d_6_valueOrError3_ = default__.AddLongAlias((d_0_opt_).LongAlias(), d_3_newLongMap_, d_0_opt_)
                                if (d_6_valueOrError3_).IsFailure():
                                    return (d_6_valueOrError3_).PropagateFailure()
                                elif True:
                                    d_7_newLongMap_ = (d_6_valueOrError3_).Extract()
                                    if ((d_0_opt_).short) != (default__.NullChar):
                                        d_8_short_ = (d_0_opt_).short
                                        if (d_8_short_) in (d_5_newShortMap_):
                                            return Wrappers.Result_Failure((((((_dafny.Seq("Duplicate short char in options : '")) + (_dafny.Seq([d_8_short_]))) + (_dafny.Seq("' for "))) + ((d_0_opt_).name)) + (_dafny.Seq(" and "))) + ((d_5_newShortMap_)[d_8_short_]))
                                        elif True:
                                            in4_ = _dafny.Seq((opts)[1::])
                                            in5_ = (d_7_newLongMap_).set((d_0_opt_).name, d_0_opt_)
                                            in6_ = (d_5_newShortMap_).set(d_8_short_, (d_0_opt_).name)
                                            in7_ = commandMap
                                            opts = in4_
                                            longMap = in5_
                                            shortMap = in6_
                                            commandMap = in7_
                                            raise _dafny.TailCall()
                                    elif True:
                                        in8_ = _dafny.Seq((opts)[1::])
                                        in9_ = (d_7_newLongMap_).set((d_0_opt_).name, d_0_opt_)
                                        in10_ = d_5_newShortMap_
                                        in11_ = commandMap
                                        opts = in8_
                                        longMap = in9_
                                        shortMap = in10_
                                        commandMap = in11_
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
                    in0_ = _dafny.Seq((args)[1::])
                    in1_ = name
                    args = in0_
                    name = in1_
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
                    in0_ = _dafny.Seq((opts)[1::])
                    in1_ = args
                    in2_ = (newArgs) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((((opts)[0]).unused).val))]))
                    opts = in0_
                    args = in1_
                    newArgs = in2_
                    raise _dafny.TailCall()
                elif True:
                    in3_ = _dafny.Seq((opts)[1::])
                    in4_ = args
                    in5_ = newArgs
                    opts = in3_
                    args = in4_
                    newArgs = in5_
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
                    in0_ = opts
                    in1_ = name
                    in2_ = (pos) + (1)
                    opts = in0_
                    name = in1_
                    pos = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def PostProcess(opts, args):
        pat_let_tv0_ = args
        pat_let_tv1_ = args
        if default__.IsHelp(args):
            return Wrappers.Result_Success(args)
        elif True:
            d_0_valueOrError0_ = default__.PostProcess2((opts).params, (args).params, _dafny.Seq([]))
            if (d_0_valueOrError0_).IsFailure():
                return (d_0_valueOrError0_).PropagateFailure()
            elif True:
                d_1_newParams_ = (d_0_valueOrError0_).Extract()
                if ((args).subcommand).is_Some:
                    d_2_optPos_ = default__.GetSubOptions((opts).params, (((args).subcommand).value).command, 0)
                    if (d_2_optPos_).is_Some:
                        d_3_valueOrError1_ = default__.PostProcess((((opts).params)[(d_2_optPos_).value]).options, ((args).subcommand).value)
                        if (d_3_valueOrError1_).IsFailure():
                            return (d_3_valueOrError1_).PropagateFailure()
                        elif True:
                            d_4_sub_ = (d_3_valueOrError1_).Extract()
                            def iife0_(_pat_let1_0):
                                def iife1_(d_5_dt__update__tmp_h0_):
                                    def iife2_(_pat_let2_0):
                                        def iife3_(d_6_dt__update_hsubcommand_h0_):
                                            def iife4_(_pat_let3_0):
                                                def iife5_(d_7_dt__update_hparams_h0_):
                                                    return Parsed_Parsed((d_5_dt__update__tmp_h0_).command, d_7_dt__update_hparams_h0_, (d_5_dt__update__tmp_h0_).files, d_6_dt__update_hsubcommand_h0_)
                                                return iife5_(_pat_let3_0)
                                            return iife4_(((pat_let_tv0_).params) + (d_1_newParams_))
                                        return iife3_(_pat_let2_0)
                                    return iife2_(Wrappers.Option_Some(d_4_sub_))
                                return iife1_(_pat_let1_0)
                            return Wrappers.Result_Success(iife0_(args))
                    elif True:
                        return Wrappers.Result_Failure(_dafny.Seq("Internal error in GetOpt::PostProcess"))
                elif True:
                    def iife6_(_pat_let4_0):
                        def iife7_(d_8_dt__update__tmp_h1_):
                            def iife8_(_pat_let5_0):
                                def iife9_(d_9_dt__update_hparams_h1_):
                                    return Parsed_Parsed((d_8_dt__update__tmp_h1_).command, d_9_dt__update_hparams_h1_, (d_8_dt__update__tmp_h1_).files, (d_8_dt__update__tmp_h1_).subcommand)
                                return iife9_(_pat_let5_0)
                            return iife8_(((pat_let_tv1_).params) + (d_1_newParams_))
                        return iife7_(_pat_let4_0)
                    return Wrappers.Result_Success(iife6_(args))

    @staticmethod
    def AllDigits(s):
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return True
                elif (('0') <= ((s)[0])) and (((s)[0]) <= ('9')):
                    in0_ = _dafny.Seq((s)[1::])
                    s = in0_
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
                    in0_ = _dafny.Seq((opts)[1::])
                    in1_ = optional
                    opts = in0_
                    optional = in1_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_No()):
                    in2_ = _dafny.Seq((opts)[1::])
                    in3_ = optional
                    opts = in2_
                    optional = in3_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_Maybe()):
                    in4_ = _dafny.Seq((opts)[1::])
                    in5_ = Wrappers.Option_Some(((opts)[0]).name)
                    opts = in4_
                    optional = in5_
                    raise _dafny.TailCall()
                elif (optional).is_None:
                    in6_ = _dafny.Seq((opts)[1::])
                    in7_ = optional
                    opts = in6_
                    optional = in7_
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
                    in0_ = _dafny.Seq((opts)[1::])
                    in1_ = args
                    in2_ = params
                    opts = in0_
                    args = in1_
                    params = in2_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_No()):
                    in3_ = _dafny.Seq((opts)[1::])
                    in4_ = args
                    in5_ = params
                    opts = in3_
                    args = in4_
                    params = in5_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_Yes()):
                    if (len(args)) == (0):
                        return Wrappers.Result_Failure(((_dafny.Seq("Positional arg '")) + (((opts)[0]).name)) + (_dafny.Seq("' is required, but we've run out of arguments.")))
                    elif default__.ValidPositional((args)[0]):
                        in6_ = _dafny.Seq((opts)[1::])
                        in7_ = _dafny.Seq((args)[1::])
                        in8_ = (params) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((args)[0]))]))
                        opts = in6_
                        args = in7_
                        params = in8_
                        raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Failure(((((_dafny.Seq("Positional arg ")) + (((opts)[0]).name)) + (_dafny.Seq(" matched with invalid positional value '"))) + ((args)[0])) + (_dafny.Seq("'.")))
                elif True:
                    if (len(args)) == (0):
                        return Wrappers.Result_Success((args, params))
                    elif default__.ValidPositional((args)[0]):
                        in9_ = _dafny.Seq((opts)[1::])
                        in10_ = _dafny.Seq((args)[1::])
                        in11_ = (params) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((args)[0]))]))
                        opts = in9_
                        args = in10_
                        params = in11_
                        raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Success((args, params))
                break

    @staticmethod
    def GetOptions(opts, args):
        d_0_newOpts_ = ((opts).params) + (_dafny.Seq([default__.HELP__PARAM]))
        def lambda0_(d_2_o_):
            return (d_2_o_).Inherits()

        d_1_inherits_ = default__.Filter(lambda0_, d_0_newOpts_)
        d_3_valueOrError0_ = default__.TestPositionals(d_0_newOpts_, Wrappers.Option_None())
        if (d_3_valueOrError0_).IsFailure():
            return (d_3_valueOrError0_).PropagateFailure()
        elif True:
            d_4_valueOrError1_ = default__.GetPositionals(d_0_newOpts_, _dafny.Seq((args)[1::]), _dafny.Seq([]))
            if (d_4_valueOrError1_).IsFailure():
                return (d_4_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs0_ = (d_4_valueOrError1_).Extract()
                d_5_newArgs_ = let_tmp_rhs0_[0]
                d_6_params_ = let_tmp_rhs0_[1]
                d_7_valueOrError2_ = default__.GetMaps(d_0_newOpts_, _dafny.Map({}), _dafny.Map({}), _dafny.Map({}))
                if (d_7_valueOrError2_).IsFailure():
                    return (d_7_valueOrError2_).PropagateFailure()
                elif True:
                    let_tmp_rhs1_ = (d_7_valueOrError2_).Extract()
                    d_8_longMap_ = let_tmp_rhs1_[0]
                    d_9_shortMap_ = let_tmp_rhs1_[1]
                    d_10_commandMap_ = let_tmp_rhs1_[2]
                    d_11_context_ = Context_Context(d_8_longMap_, d_9_shortMap_, d_1_inherits_, d_10_commandMap_, (args)[0])
                    d_12_valueOrError3_ = default__.GetOptions2(d_5_newArgs_, d_11_context_, d_6_params_, _dafny.Seq([]))
                    if (d_12_valueOrError3_).IsFailure():
                        return (d_12_valueOrError3_).PropagateFailure()
                    elif True:
                        d_13_result_ = (d_12_valueOrError3_).Extract()
                        return default__.PostProcess(opts, d_13_result_)

    @staticmethod
    def IndexOf(xs, v):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if ((xs)[0]) == (v):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (1)
                    in0_ = _dafny.Seq((xs)[1::])
                    in1_ = v
                    xs = in0_
                    v = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SplitOnce(s, delim):
        d_0_i_ = default__.IndexOf(s, delim)
        return (_dafny.Seq((s)[:d_0_i_:]), _dafny.Seq((s)[(d_0_i_) + (1)::]))

    @staticmethod
    def GetOptions2(args, context, parms, files):
        if (len(args)) == (0):
            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, files, Wrappers.Option_None()))
        elif ((args)[0]) in ((context).commands):
            def lambda0_(d_1_o_):
                return (d_1_o_).Inherits()

            d_0_inherits_ = default__.Filter(lambda0_, (((context).commands)[(args)[0]]).params)
            d_2_newOpts_ = ((((context).commands)[(args)[0]]).params) + ((context).inherits)
            d_3_valueOrError0_ = default__.TestPositionals(d_2_newOpts_, Wrappers.Option_None())
            if (d_3_valueOrError0_).IsFailure():
                return (d_3_valueOrError0_).PropagateFailure()
            elif True:
                d_4_valueOrError1_ = default__.GetPositionals(d_2_newOpts_, _dafny.Seq((args)[1::]), _dafny.Seq([]))
                if (d_4_valueOrError1_).IsFailure():
                    return (d_4_valueOrError1_).PropagateFailure()
                elif True:
                    let_tmp_rhs0_ = (d_4_valueOrError1_).Extract()
                    d_5_newArgs_ = let_tmp_rhs0_[0]
                    d_6_params_ = let_tmp_rhs0_[1]
                    d_7_valueOrError2_ = default__.GetMaps(d_2_newOpts_, _dafny.Map({}), _dafny.Map({}), _dafny.Map({}))
                    if (d_7_valueOrError2_).IsFailure():
                        return (d_7_valueOrError2_).PropagateFailure()
                    elif True:
                        let_tmp_rhs1_ = (d_7_valueOrError2_).Extract()
                        d_8_longMap_ = let_tmp_rhs1_[0]
                        d_9_shortMap_ = let_tmp_rhs1_[1]
                        d_10_commandSet_ = let_tmp_rhs1_[2]
                        d_11_newContext_ = Context_Context(d_8_longMap_, d_9_shortMap_, ((context).inherits) + (d_0_inherits_), d_10_commandSet_, (args)[0])
                        d_12_lostArgs_ = (len(args)) - (len(d_5_newArgs_))
                        d_13_valueOrError3_ = default__.GetOptions2(_dafny.Seq((args)[d_12_lostArgs_::]), d_11_newContext_, d_6_params_, _dafny.Seq([]))
                        if (d_13_valueOrError3_).IsFailure():
                            return (d_13_valueOrError3_).PropagateFailure()
                        elif True:
                            d_14_result_ = (d_13_valueOrError3_).Extract()
                            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, files, Wrappers.Option_Some(d_14_result_)))
        elif ((args)[0]) == (_dafny.Seq("--")):
            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, (files) + (_dafny.Seq((args)[1::])), Wrappers.Option_None()))
        elif (_dafny.Seq("--")) < ((args)[0]):
            d_15_longOpt_ = _dafny.Seq(((args)[0])[2::])
            if ('=') in (d_15_longOpt_):
                let_tmp_rhs2_ = default__.SplitOnce(d_15_longOpt_, '=')
                d_16_opt_ = let_tmp_rhs2_[0]
                d_17_arg_ = let_tmp_rhs2_[1]
                if (d_16_opt_) in ((context).longMap):
                    if (((context).longMap)[d_16_opt_]).NeedsArg():
                        return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + ((((context).longMap)[d_16_opt_]).MakeArg(Wrappers.Option_Some(d_17_arg_))), files)
                    elif True:
                        return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_16_opt_)) + (_dafny.Seq(" does not take an argument, but it got one.")))
                elif True:
                    return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_16_opt_)) + (_dafny.Seq(" not recognized.")))
            elif (d_15_longOpt_) in ((context).longMap):
                d_18_opt_ = ((context).longMap)[d_15_longOpt_]
                if (d_18_opt_).NeedsArg():
                    if (len(args)) < (2):
                        return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_15_longOpt_)) + (_dafny.Seq(" requires an argument, but didn't get one.")))
                    elif True:
                        return default__.GetOptions2(_dafny.Seq((args)[2::]), context, (parms) + ((d_18_opt_).MakeArg(Wrappers.Option_Some((args)[1]))), files)
                elif (((d_18_opt_).is_Flag) and ((d_18_opt_).solo)) and ((((len(args)) != (1)) or ((len(parms)) != (0))) or ((len(files)) != (0))):
                    return Wrappers.Result_Failure(((_dafny.Seq("Option '")) + (d_15_longOpt_)) + (_dafny.Seq("' used with other stuff, but must only be used alone.")))
                elif True:
                    return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + ((d_18_opt_).MakeArg(Wrappers.Option_None())), files)
            elif True:
                return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_15_longOpt_)) + (_dafny.Seq(" not recognized.")))
        elif (_dafny.Seq("-")) == ((args)[0]):
            return default__.GetOptions2(_dafny.Seq((args)[1::]), context, parms, (files) + (_dafny.Seq([(args)[0]])))
        elif (_dafny.Seq("-")) < ((args)[0]):
            d_19_valueOrError4_ = default__.GetShort(_dafny.Seq(((args)[0])[1::]), (context).longMap, (context).shortMap, _dafny.Seq([]))
            if (d_19_valueOrError4_).IsFailure():
                return (d_19_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs3_ = (d_19_valueOrError4_).Extract()
                d_20_newParms_ = let_tmp_rhs3_[0]
                d_21_nextParm_ = let_tmp_rhs3_[1]
                if (d_21_nextParm_).is_None:
                    return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + (d_20_newParms_), files)
                elif (len(args)) == (1):
                    return Wrappers.Result_Failure(((_dafny.Seq("Short option ")) + (_dafny.Seq([(d_21_nextParm_).value]))) + (_dafny.Seq(" requires argument but didn't get one.")))
                elif True:
                    d_22_longOpt_ = ((context).shortMap)[(d_21_nextParm_).value]
                    d_23_opt_ = ((context).longMap)[d_22_longOpt_]
                    return default__.GetOptions2(_dafny.Seq((args)[2::]), context, ((parms) + (d_20_newParms_)) + ((d_23_opt_).MakeArg(Wrappers.Option_Some((args)[1]))), files)
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
                    d_0_ch_ = (arg)[0]
                    if (d_0_ch_) in (shortMap):
                        d_1_opt_ = (shortMap)[d_0_ch_]
                        if ((longMap)[d_1_opt_]).NeedsArg():
                            if (len(arg)) == (1):
                                return Wrappers.Result_Success((parms, Wrappers.Option_Some(d_0_ch_)))
                            elif True:
                                return Wrappers.Result_Success(((parms) + (((longMap)[d_1_opt_]).MakeArg(Wrappers.Option_Some(_dafny.Seq((arg)[1::])))), Wrappers.Option_None()))
                        elif True:
                            in0_ = _dafny.Seq((arg)[1::])
                            in1_ = longMap
                            in2_ = shortMap
                            in3_ = (parms) + (((longMap)[d_1_opt_]).MakeArg(Wrappers.Option_None()))
                            arg = in0_
                            longMap = in1_
                            shortMap = in2_
                            parms = in3_
                            raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Failure(((_dafny.Seq("Short option '")) + (_dafny.Seq([d_0_ch_]))) + (_dafny.Seq("' not recognized.")))
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
        return lambda: Options_Options(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq({}))
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
        return lambda: Param_Opt(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), 'D', Unused.default()(), False, Visibility.default()(), _dafny.Seq(""), _dafny.Seq({}), Tri.default()())
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
        return lambda: OneArg_OneArg(_dafny.Seq(""), Wrappers.Option.default()())
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
        return lambda: Parsed_Parsed(_dafny.Seq(""), _dafny.Seq({}), _dafny.Seq({}), Wrappers.Option.default()())
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
    def _Is(source__):
        d_0_x_: _dafny.Map = source__
        def lambda0_(forall_var_0_):
            d_1_k_: _dafny.Seq = forall_var_0_
            return not ((d_1_k_) in (d_0_x_)) or ((((d_0_x_)[d_1_k_]).name) == (d_1_k_))

        return _dafny.quantifier((d_0_x_).keys.Elements, True, lambda0_)

class Context:
    @classmethod
    def default(cls, ):
        return lambda: Context_Context(_dafny.Map({}), _dafny.Map({}), _dafny.Seq({}), _dafny.Map({}), _dafny.Seq(""))
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

