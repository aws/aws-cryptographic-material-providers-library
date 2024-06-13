import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings

# Module: GetOpt

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Example(args):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_266_MyOptions_: _dafny.Seq
        d_266_MyOptions_ = _dafny.Seq([Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), default__.NullChar, False, False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([])), Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', Unused_UnusedOk(), False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), Tri_No()), Param_Command(Options_Options(_dafny.Seq("command"), _dafny.Seq("Does command stuff"), _dafny.Seq([Param_Opt(_dafny.Seq("two"), _dafny.Seq("Does bar things to thingy"), _dafny.Seq("thingy"), 't', Unused_UnusedOk(), False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), Tri_No()), Param_Flag(_dafny.Seq("foo"), _dafny.Seq("Does foo things"), default__.NullChar, False, False, Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]))])))])
        d_267_opts_: Options
        d_267_opts_ = Options_Options(_dafny.Seq("myProg"), _dafny.Seq("does prog stuff"), d_266_MyOptions_)
        d_268_x_: Parsed
        d_269_valueOrError0_: Wrappers.Result = Wrappers.Result.default(Parsed.default())()
        d_269_valueOrError0_ = default__.GetOptions(d_267_opts_, args)
        if (d_269_valueOrError0_).IsFailure():
            output = (d_269_valueOrError0_).PropagateFailure()
            return output
        d_268_x_ = (d_269_valueOrError0_).Extract()
        d_270_h_: Wrappers.Option
        d_270_h_ = default__.NeedsHelp(d_267_opts_, d_268_x_, _dafny.Seq(""))
        if (d_270_h_).is_Some:
            _dafny.print(_dafny.string_of((d_270_h_).value))
            output = Wrappers.Result_Success(True)
            return output
        output = Wrappers.Result_Success(True)
        return output
        return output

    @staticmethod
    def Filter(f, xs):
        d_271___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_271___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_271___accumulator_ = (d_271___accumulator_) + ((_dafny.Seq([(xs)[0]]) if f((xs)[0]) else _dafny.Seq([])))
                    in69_ = f
                    in70_ = _dafny.Seq((xs)[1::])
                    f = in69_
                    xs = in70_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def NeedsHelp(opts, args, prefix):
        while True:
            with _dafny.label():
                if ((len((args).params)) != (0)) and (((((args).params)[0]).name) == (default__.HELP__STR)):
                    return Wrappers.Option_Some(default__.GetHelp(opts, prefix))
                elif ((args).subcommand).is_Some:
                    d_272_valueOrError0_ = default__.GetSubOptions((opts).params, (((args).subcommand).value).command, 0)
                    if (d_272_valueOrError0_).IsFailure():
                        return (d_272_valueOrError0_).PropagateFailure()
                    elif True:
                        d_273_pos_ = (d_272_valueOrError0_).Extract()
                        in71_ = (((opts).params)[d_273_pos_]).options
                        in72_ = ((args).subcommand).value
                        in73_ = ((prefix) + ((args).command)) + (_dafny.Seq(" "))
                        opts = in71_
                        args = in72_
                        prefix = in73_
                        raise _dafny.TailCall()
                elif True:
                    return Wrappers.Option_None()
                break

    @staticmethod
    def GetHelp(opts, prefix):
        d_274_newOpts_ = ((opts).params) + (_dafny.Seq([default__.HELP__PARAM]))
        d_275_longLen_ = default__.GetLongLen(d_274_newOpts_, 6)
        d_276_commandLen_ = default__.GetCommandLen(d_274_newOpts_, 0)
        if (d_276_commandLen_) == (0):
            return ((((((_dafny.Seq("USAGE : ")) + (prefix)) + ((opts).name)) + (_dafny.Seq(" [args...]\n"))) + ((opts).help)) + (_dafny.Seq("\n"))) + (default__.GetHelp2(d_274_newOpts_, d_275_longLen_))
        elif True:
            return ((((((((_dafny.Seq("USAGE : ")) + ((opts).name)) + (_dafny.Seq(" [args...] command [args...]\n"))) + ((opts).help)) + (_dafny.Seq("\n"))) + (_dafny.Seq("\nAvailable Commands:\n"))) + (default__.GetCmdHelp(d_274_newOpts_, d_276_commandLen_))) + (_dafny.Seq("\nAvailable Options:\n"))) + (default__.GetHelp2(d_274_newOpts_, d_275_longLen_))

    @staticmethod
    def OptValue(args, arg):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return Wrappers.Option_None()
                elif (((args)[0]).name) == (arg):
                    return ((args)[0]).value
                elif True:
                    in74_ = _dafny.Seq((args)[1::])
                    in75_ = arg
                    args = in74_
                    arg = in75_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagCount(args, arg):
        d_277___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return (0) + (d_277___accumulator_)
                elif (((args)[0]).name) == (arg):
                    d_277___accumulator_ = (d_277___accumulator_) + (1)
                    in76_ = _dafny.Seq((args)[1::])
                    in77_ = arg
                    args = in76_
                    arg = in77_
                    raise _dafny.TailCall()
                elif True:
                    in78_ = _dafny.Seq((args)[1::])
                    in79_ = arg
                    args = in78_
                    arg = in79_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OptMapLast(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theMap
                elif (((args)[0]).value).is_Some:
                    in80_ = _dafny.Seq((args)[1::])
                    in81_ = (theMap).set(((args)[0]).name, (((args)[0]).value).value)
                    args = in80_
                    theMap = in81_
                    raise _dafny.TailCall()
                elif True:
                    in82_ = _dafny.Seq((args)[1::])
                    in83_ = theMap
                    args = in82_
                    theMap = in83_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagsSet(args, theSet):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theSet
                elif (((args)[0]).value).is_Some:
                    in84_ = _dafny.Seq((args)[1::])
                    in85_ = theSet
                    args = in84_
                    theSet = in85_
                    raise _dafny.TailCall()
                elif True:
                    in86_ = _dafny.Seq((args)[1::])
                    in87_ = (theSet) | (_dafny.Set({((args)[0]).name}))
                    args = in86_
                    theSet = in87_
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
                        in88_ = _dafny.Seq((args)[1::])
                        in89_ = (theMap).set(((args)[0]).name, ((theMap)[((args)[0]).name]) + (_dafny.Seq([(((args)[0]).value).value])))
                        args = in88_
                        theMap = in89_
                        raise _dafny.TailCall()
                    elif True:
                        in90_ = _dafny.Seq((args)[1::])
                        in91_ = (theMap).set(((args)[0]).name, _dafny.Seq([(((args)[0]).value).value]))
                        args = in90_
                        theMap = in91_
                        raise _dafny.TailCall()
                elif True:
                    in92_ = _dafny.Seq((args)[1::])
                    in93_ = theMap
                    args = in92_
                    theMap = in93_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlagMapCount(args, theMap):
        while True:
            with _dafny.label():
                if (len(args)) == (0):
                    return theMap
                elif (((args)[0]).value).is_Some:
                    in94_ = _dafny.Seq((args)[1::])
                    in95_ = theMap
                    args = in94_
                    theMap = in95_
                    raise _dafny.TailCall()
                elif (((args)[0]).name) in (theMap):
                    in96_ = _dafny.Seq((args)[1::])
                    in97_ = (theMap).set(((args)[0]).name, ((theMap)[((args)[0]).name]) + (1))
                    args = in96_
                    theMap = in97_
                    raise _dafny.TailCall()
                elif True:
                    in98_ = _dafny.Seq((args)[1::])
                    in99_ = (theMap).set(((args)[0]).name, 1)
                    args = in98_
                    theMap = in99_
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
                        in100_ = _dafny.Seq((args)[1::])
                        in101_ = (theSet) | (_dafny.Set({((args)[0]).name}))
                        args = in100_
                        theSet = in101_
                        raise _dafny.TailCall()
                elif True:
                    in102_ = _dafny.Seq((args)[1::])
                    in103_ = theSet
                    args = in102_
                    theSet = in103_
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
                        in104_ = _dafny.Seq((args)[1::])
                        in105_ = (theMap).set(((args)[0]).name, (((args)[0]).value).value)
                        args = in104_
                        theMap = in105_
                        raise _dafny.TailCall()
                elif True:
                    in106_ = _dafny.Seq((args)[1::])
                    in107_ = theMap
                    args = in106_
                    theMap = in107_
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
        d_278_name_ = ((((opt).options).name) + (_dafny.Seq([' ' for d_279_i_ in range((commandLen) - (len(((opt).options).name)))])) if (len(((opt).options).name)) < (commandLen) else ((opt).options).name)
        return (((d_278_name_) + (_dafny.Seq("  "))) + (((opt).options).help)) + (_dafny.Seq("\n"))

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
            d_280_tmp_ = ((_dafny.Seq("--")) + ((opt).name)) + (((_dafny.Seq("=")) + ((opt).argName) if (opt).is_Opt else _dafny.Seq("")))
            if (len(d_280_tmp_)) < (longLen):
                return (d_280_tmp_) + (_dafny.Seq([' ' for d_281_i_ in range((longLen) - (len(d_280_tmp_)))]))
            elif True:
                return d_280_tmp_
        elif True:
            return _dafny.Seq("")

    @staticmethod
    def GetHelp2(opts, longLen):
        d_282___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return (d_282___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_283_x_ = default__.OneHelp((opts)[0], longLen)
                    d_282___accumulator_ = (d_282___accumulator_) + (d_283_x_)
                    in108_ = _dafny.Seq((opts)[1::])
                    in109_ = longLen
                    opts = in108_
                    longLen = in109_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetCmdHelp(opts, commandLen):
        d_284___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return (d_284___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_285_x_ = (default__.GetCommandHelp((opts)[0], commandLen) if ((opts)[0]).is_Command else _dafny.Seq(""))
                    d_284___accumulator_ = (d_284___accumulator_) + (d_285_x_)
                    in110_ = _dafny.Seq((opts)[1::])
                    in111_ = commandLen
                    opts = in110_
                    commandLen = in111_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetLongLen(opts, max):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return max
                elif True:
                    d_286_x_ = len(default__.GetLongHelp((opts)[0], 0))
                    d_287_newMax_ = (d_286_x_ if (d_286_x_) > (max) else max)
                    in112_ = _dafny.Seq((opts)[1::])
                    in113_ = d_287_newMax_
                    opts = in112_
                    max = in113_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetCommandLen(opts, max):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return max
                elif True:
                    d_288_x_ = (len((((opts)[0]).options).name) if ((opts)[0]).is_Command else 0)
                    d_289_newMax_ = (d_288_x_ if (d_288_x_) > (max) else max)
                    in114_ = _dafny.Seq((opts)[1::])
                    in115_ = d_289_newMax_
                    opts = in114_
                    max = in115_
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
                    in116_ = _dafny.Seq((aliases)[1::])
                    in117_ = (shortMap).set((aliases)[0], name)
                    in118_ = name
                    aliases = in116_
                    shortMap = in117_
                    name = in118_
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
                    in119_ = _dafny.Seq((aliases)[1::])
                    in120_ = (longMap).set((aliases)[0], opt)
                    in121_ = opt
                    aliases = in119_
                    longMap = in120_
                    opt = in121_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetMaps(opts, longMap, shortMap, commandMap):
        while True:
            with _dafny.label():
                if (len(opts)) == (0):
                    return Wrappers.Result_Success((longMap, shortMap, commandMap))
                elif True:
                    d_290_opt_ = (opts)[0]
                    if (d_290_opt_).is_Command:
                        d_291_valueOrError0_ = Wrappers.default__.Need((((d_290_opt_).options).name) not in (commandMap), (_dafny.Seq("Duplicate command in options : ")) + (((d_290_opt_).options).name))
                        if (d_291_valueOrError0_).IsFailure():
                            return (d_291_valueOrError0_).PropagateFailure()
                        elif True:
                            in122_ = _dafny.Seq((opts)[1::])
                            in123_ = longMap
                            in124_ = shortMap
                            in125_ = (commandMap).set(((d_290_opt_).options).name, (d_290_opt_).options)
                            opts = in122_
                            longMap = in123_
                            shortMap = in124_
                            commandMap = in125_
                            raise _dafny.TailCall()
                    elif True:
                        d_292_valueOrError1_ = Wrappers.default__.Need(((d_290_opt_).name) not in (longMap), (_dafny.Seq("Duplicate long name in options : ")) + ((d_290_opt_).name))
                        if (d_292_valueOrError1_).IsFailure():
                            return (d_292_valueOrError1_).PropagateFailure()
                        elif True:
                            d_293_longMap_ = (longMap).set((d_290_opt_).name, d_290_opt_)
                            d_294_valueOrError2_ = default__.AddShortAlias((d_290_opt_).ShortAlias(), shortMap, (d_290_opt_).name)
                            if (d_294_valueOrError2_).IsFailure():
                                return (d_294_valueOrError2_).PropagateFailure()
                            elif True:
                                d_295_shortMap_ = (d_294_valueOrError2_).Extract()
                                d_296_valueOrError3_ = default__.AddLongAlias((d_290_opt_).LongAlias(), d_293_longMap_, d_290_opt_)
                                if (d_296_valueOrError3_).IsFailure():
                                    return (d_296_valueOrError3_).PropagateFailure()
                                elif True:
                                    d_297_longMap_ = (d_296_valueOrError3_).Extract()
                                    if ((d_290_opt_).short) != (default__.NullChar):
                                        d_298_short_ = (d_290_opt_).short
                                        if (d_298_short_) in (d_295_shortMap_):
                                            return Wrappers.Result_Failure((((((_dafny.Seq("Duplicate short char in options : '")) + (_dafny.Seq([d_298_short_]))) + (_dafny.Seq("' for "))) + ((d_290_opt_).name)) + (_dafny.Seq(" and "))) + ((d_295_shortMap_)[d_298_short_]))
                                        elif True:
                                            in126_ = _dafny.Seq((opts)[1::])
                                            in127_ = (d_297_longMap_).set((d_290_opt_).name, d_290_opt_)
                                            in128_ = (d_295_shortMap_).set(d_298_short_, (d_290_opt_).name)
                                            in129_ = commandMap
                                            opts = in126_
                                            longMap = in127_
                                            shortMap = in128_
                                            commandMap = in129_
                                            raise _dafny.TailCall()
                                    elif True:
                                        in130_ = _dafny.Seq((opts)[1::])
                                        in131_ = (d_297_longMap_).set((d_290_opt_).name, d_290_opt_)
                                        in132_ = d_295_shortMap_
                                        in133_ = commandMap
                                        opts = in130_
                                        longMap = in131_
                                        shortMap = in132_
                                        commandMap = in133_
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
                    in134_ = _dafny.Seq((args)[1::])
                    in135_ = name
                    args = in134_
                    name = in135_
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
                    in136_ = _dafny.Seq((opts)[1::])
                    in137_ = args
                    in138_ = (newArgs) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((((opts)[0]).unused).val))]))
                    opts = in136_
                    args = in137_
                    newArgs = in138_
                    raise _dafny.TailCall()
                elif True:
                    in139_ = _dafny.Seq((opts)[1::])
                    in140_ = args
                    in141_ = newArgs
                    opts = in139_
                    args = in140_
                    newArgs = in141_
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
                    in142_ = opts
                    in143_ = name
                    in144_ = (pos) + (1)
                    opts = in142_
                    name = in143_
                    pos = in144_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def PostProcess(opts, args):
        pat_let_tv6_ = args
        pat_let_tv7_ = args
        d_299_valueOrError0_ = default__.PostProcess2((opts).params, (args).params, _dafny.Seq([]))
        if (d_299_valueOrError0_).IsFailure():
            return (d_299_valueOrError0_).PropagateFailure()
        elif True:
            d_300_newParams_ = (d_299_valueOrError0_).Extract()
            if ((args).subcommand).is_Some:
                d_301_optPos_ = default__.GetSubOptions((opts).params, (((args).subcommand).value).command, 0)
                if (d_301_optPos_).is_Some:
                    d_302_valueOrError1_ = default__.PostProcess((((opts).params)[(d_301_optPos_).value]).options, ((args).subcommand).value)
                    if (d_302_valueOrError1_).IsFailure():
                        return (d_302_valueOrError1_).PropagateFailure()
                    elif True:
                        d_303_sub_ = (d_302_valueOrError1_).Extract()
                        def iife2_(_pat_let1_0):
                            def iife3_(d_304_dt__update__tmp_h0_):
                                def iife4_(_pat_let2_0):
                                    def iife5_(d_305_dt__update_hsubcommand_h0_):
                                        def iife6_(_pat_let3_0):
                                            def iife7_(d_306_dt__update_hparams_h0_):
                                                return Parsed_Parsed((d_304_dt__update__tmp_h0_).command, d_306_dt__update_hparams_h0_, (d_304_dt__update__tmp_h0_).files, d_305_dt__update_hsubcommand_h0_)
                                            return iife7_(_pat_let3_0)
                                        return iife6_(((pat_let_tv6_).params) + (d_300_newParams_))
                                    return iife5_(_pat_let2_0)
                                return iife4_(Wrappers.Option_Some(d_303_sub_))
                            return iife3_(_pat_let1_0)
                        return Wrappers.Result_Success(iife2_(args))
                elif True:
                    return Wrappers.Result_Failure(_dafny.Seq("Internal error in GetOpt::PostProcess"))
            elif True:
                def iife8_(_pat_let4_0):
                    def iife9_(d_307_dt__update__tmp_h1_):
                        def iife10_(_pat_let5_0):
                            def iife11_(d_308_dt__update_hparams_h1_):
                                return Parsed_Parsed((d_307_dt__update__tmp_h1_).command, d_308_dt__update_hparams_h1_, (d_307_dt__update__tmp_h1_).files, (d_307_dt__update__tmp_h1_).subcommand)
                            return iife11_(_pat_let5_0)
                        return iife10_(((pat_let_tv7_).params) + (d_300_newParams_))
                    return iife9_(_pat_let4_0)
                return Wrappers.Result_Success(iife8_(args))

    @staticmethod
    def AllDigits(s):
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return True
                elif (('0') <= ((s)[0])) and (((s)[0]) <= ('9')):
                    in145_ = _dafny.Seq((s)[1::])
                    s = in145_
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
                    in146_ = _dafny.Seq((opts)[1::])
                    in147_ = optional
                    opts = in146_
                    optional = in147_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_No()):
                    in148_ = _dafny.Seq((opts)[1::])
                    in149_ = optional
                    opts = in148_
                    optional = in149_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_Maybe()):
                    in150_ = _dafny.Seq((opts)[1::])
                    in151_ = Wrappers.Option_Some(((opts)[0]).name)
                    opts = in150_
                    optional = in151_
                    raise _dafny.TailCall()
                elif (optional).is_None:
                    in152_ = _dafny.Seq((opts)[1::])
                    in153_ = optional
                    opts = in152_
                    optional = in153_
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
                    in154_ = _dafny.Seq((opts)[1::])
                    in155_ = args
                    in156_ = params
                    opts = in154_
                    args = in155_
                    params = in156_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_No()):
                    in157_ = _dafny.Seq((opts)[1::])
                    in158_ = args
                    in159_ = params
                    opts = in157_
                    args = in158_
                    params = in159_
                    raise _dafny.TailCall()
                elif (((opts)[0]).positional) == (Tri_Yes()):
                    if (len(args)) == (0):
                        return Wrappers.Result_Failure(((_dafny.Seq("Positional arg '")) + (((opts)[0]).name)) + (_dafny.Seq("' is required, but we've run out of arguments.")))
                    elif default__.ValidPositional((args)[0]):
                        in160_ = _dafny.Seq((opts)[1::])
                        in161_ = _dafny.Seq((args)[1::])
                        in162_ = (params) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((args)[0]))]))
                        opts = in160_
                        args = in161_
                        params = in162_
                        raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Failure(((((_dafny.Seq("Positional arg ")) + (((opts)[0]).name)) + (_dafny.Seq(" matched with invalid positional value '"))) + ((args)[0])) + (_dafny.Seq("'.")))
                elif True:
                    if (len(args)) == (0):
                        return Wrappers.Result_Success((args, params))
                    elif default__.ValidPositional((args)[0]):
                        in163_ = _dafny.Seq((opts)[1::])
                        in164_ = _dafny.Seq((args)[1::])
                        in165_ = (params) + (_dafny.Seq([OneArg_OneArg(((opts)[0]).name, Wrappers.Option_Some((args)[0]))]))
                        opts = in163_
                        args = in164_
                        params = in165_
                        raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Success((args, params))
                break

    @staticmethod
    def GetOptions(opts, args):
        d_309_newOpts_ = ((opts).params) + (_dafny.Seq([default__.HELP__PARAM]))
        def lambda23_(d_311_o_):
            return (d_311_o_).Inherits()

        d_310_inherits_ = default__.Filter(lambda23_, d_309_newOpts_)
        d_312_valueOrError0_ = default__.TestPositionals(d_309_newOpts_, Wrappers.Option_None())
        if (d_312_valueOrError0_).IsFailure():
            return (d_312_valueOrError0_).PropagateFailure()
        elif True:
            d_313_valueOrError1_ = default__.GetPositionals(d_309_newOpts_, _dafny.Seq((args)[1::]), _dafny.Seq([]))
            if (d_313_valueOrError1_).IsFailure():
                return (d_313_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs1_ = (d_313_valueOrError1_).Extract()
                d_314_newArgs_ = let_tmp_rhs1_[0]
                d_315_params_ = let_tmp_rhs1_[1]
                d_316_valueOrError2_ = default__.GetMaps(d_309_newOpts_, _dafny.Map({}), _dafny.Map({}), _dafny.Map({}))
                if (d_316_valueOrError2_).IsFailure():
                    return (d_316_valueOrError2_).PropagateFailure()
                elif True:
                    let_tmp_rhs2_ = (d_316_valueOrError2_).Extract()
                    d_317_longMap_ = let_tmp_rhs2_[0]
                    d_318_shortMap_ = let_tmp_rhs2_[1]
                    d_319_commandMap_ = let_tmp_rhs2_[2]
                    d_320_context_ = Context_Context(d_317_longMap_, d_318_shortMap_, d_310_inherits_, d_319_commandMap_, (args)[0])
                    d_321_valueOrError3_ = default__.GetOptions2(d_314_newArgs_, d_320_context_, d_315_params_, _dafny.Seq([]))
                    if (d_321_valueOrError3_).IsFailure():
                        return (d_321_valueOrError3_).PropagateFailure()
                    elif True:
                        d_322_result_ = (d_321_valueOrError3_).Extract()
                        return default__.PostProcess(opts, d_322_result_)

    @staticmethod
    def IndexOf(xs, v):
        d_323___accumulator_ = 0
        while True:
            with _dafny.label():
                if ((xs)[0]) == (v):
                    return (0) + (d_323___accumulator_)
                elif True:
                    d_323___accumulator_ = (d_323___accumulator_) + (1)
                    in166_ = _dafny.Seq((xs)[1::])
                    in167_ = v
                    xs = in166_
                    v = in167_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SplitOnce(s, delim):
        d_324_i_ = default__.IndexOf(s, delim)
        return (_dafny.Seq((s)[:d_324_i_:]), _dafny.Seq((s)[(d_324_i_) + (1)::]))

    @staticmethod
    def GetOptions2(args, context, parms, files):
        if (len(args)) == (0):
            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, files, Wrappers.Option_None()))
        elif ((args)[0]) in ((context).commands):
            def lambda24_(d_326_o_):
                return (d_326_o_).Inherits()

            d_325_inherits_ = default__.Filter(lambda24_, (((context).commands)[(args)[0]]).params)
            d_327_newOpts_ = ((((context).commands)[(args)[0]]).params) + ((context).inherits)
            d_328_valueOrError0_ = default__.TestPositionals(d_327_newOpts_, Wrappers.Option_None())
            if (d_328_valueOrError0_).IsFailure():
                return (d_328_valueOrError0_).PropagateFailure()
            elif True:
                d_329_valueOrError1_ = default__.GetPositionals(d_327_newOpts_, _dafny.Seq((args)[1::]), _dafny.Seq([]))
                if (d_329_valueOrError1_).IsFailure():
                    return (d_329_valueOrError1_).PropagateFailure()
                elif True:
                    let_tmp_rhs3_ = (d_329_valueOrError1_).Extract()
                    d_330_newArgs_ = let_tmp_rhs3_[0]
                    d_331_params_ = let_tmp_rhs3_[1]
                    d_332_valueOrError2_ = default__.GetMaps(d_327_newOpts_, _dafny.Map({}), _dafny.Map({}), _dafny.Map({}))
                    if (d_332_valueOrError2_).IsFailure():
                        return (d_332_valueOrError2_).PropagateFailure()
                    elif True:
                        let_tmp_rhs4_ = (d_332_valueOrError2_).Extract()
                        d_333_longMap_ = let_tmp_rhs4_[0]
                        d_334_shortMap_ = let_tmp_rhs4_[1]
                        d_335_commandSet_ = let_tmp_rhs4_[2]
                        d_336_newContext_ = Context_Context(d_333_longMap_, d_334_shortMap_, ((context).inherits) + (d_325_inherits_), d_335_commandSet_, (args)[0])
                        d_337_lostArgs_ = (len(args)) - (len(d_330_newArgs_))
                        d_338_valueOrError3_ = default__.GetOptions2(_dafny.Seq((args)[d_337_lostArgs_::]), d_336_newContext_, d_331_params_, _dafny.Seq([]))
                        if (d_338_valueOrError3_).IsFailure():
                            return (d_338_valueOrError3_).PropagateFailure()
                        elif True:
                            d_339_result_ = (d_338_valueOrError3_).Extract()
                            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, files, Wrappers.Option_Some(d_339_result_)))
        elif ((args)[0]) == (_dafny.Seq("--")):
            return Wrappers.Result_Success(Parsed_Parsed((context).command, parms, (files) + (_dafny.Seq((args)[1::])), Wrappers.Option_None()))
        elif (_dafny.Seq("--")) < ((args)[0]):
            d_340_longOpt_ = _dafny.Seq(((args)[0])[2::])
            if ('=') in (d_340_longOpt_):
                let_tmp_rhs5_ = default__.SplitOnce(d_340_longOpt_, '=')
                d_341_opt_ = let_tmp_rhs5_[0]
                d_342_arg_ = let_tmp_rhs5_[1]
                if (d_341_opt_) in ((context).longMap):
                    if (((context).longMap)[d_341_opt_]).NeedsArg():
                        return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + ((((context).longMap)[d_341_opt_]).MakeArg(Wrappers.Option_Some(d_342_arg_))), files)
                    elif True:
                        return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_341_opt_)) + (_dafny.Seq(" does not take an argument, but it got one.")))
                elif True:
                    return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_341_opt_)) + (_dafny.Seq(" not recognized.")))
            elif (d_340_longOpt_) in ((context).longMap):
                d_343_opt_ = ((context).longMap)[d_340_longOpt_]
                if (d_343_opt_).NeedsArg():
                    if (len(args)) < (2):
                        return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_340_longOpt_)) + (_dafny.Seq(" requires an argument, but didn't get one.")))
                    elif True:
                        return default__.GetOptions2(_dafny.Seq((args)[2::]), context, (parms) + ((d_343_opt_).MakeArg(Wrappers.Option_Some((args)[1]))), files)
                elif (((d_343_opt_).is_Flag) and ((d_343_opt_).solo)) and ((((len(args)) != (1)) or ((len(parms)) != (0))) or ((len(files)) != (0))):
                    return Wrappers.Result_Failure(((_dafny.Seq("Option '")) + (d_340_longOpt_)) + (_dafny.Seq("' used with other stuff, but must only be used alone.")))
                elif True:
                    return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + ((d_343_opt_).MakeArg(Wrappers.Option_None())), files)
            elif True:
                return Wrappers.Result_Failure(((_dafny.Seq("Option ")) + (d_340_longOpt_)) + (_dafny.Seq(" not recognized.")))
        elif (_dafny.Seq("-")) == ((args)[0]):
            return default__.GetOptions2(_dafny.Seq((args)[1::]), context, parms, (files) + (_dafny.Seq([(args)[0]])))
        elif (_dafny.Seq("-")) < ((args)[0]):
            d_344_valueOrError4_ = default__.GetShort(_dafny.Seq(((args)[0])[1::]), (context).longMap, (context).shortMap, _dafny.Seq([]))
            if (d_344_valueOrError4_).IsFailure():
                return (d_344_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs6_ = (d_344_valueOrError4_).Extract()
                d_345_newParms_ = let_tmp_rhs6_[0]
                d_346_nextParm_ = let_tmp_rhs6_[1]
                if (d_346_nextParm_).is_None:
                    return default__.GetOptions2(_dafny.Seq((args)[1::]), context, (parms) + (d_345_newParms_), files)
                elif (len(args)) == (1):
                    return Wrappers.Result_Failure(((_dafny.Seq("Short option ")) + (_dafny.Seq([(d_346_nextParm_).value]))) + (_dafny.Seq(" requires argument but didn't get one.")))
                elif True:
                    d_347_longOpt_ = ((context).shortMap)[(d_346_nextParm_).value]
                    d_348_opt_ = ((context).longMap)[d_347_longOpt_]
                    return default__.GetOptions2(_dafny.Seq((args)[2::]), context, ((parms) + (d_345_newParms_)) + ((d_348_opt_).MakeArg(Wrappers.Option_Some((args)[1]))), files)
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
                    d_349_ch_ = (arg)[0]
                    if (d_349_ch_) in (shortMap):
                        d_350_opt_ = (shortMap)[d_349_ch_]
                        if ((longMap)[d_350_opt_]).NeedsArg():
                            if (len(arg)) == (1):
                                return Wrappers.Result_Success((parms, Wrappers.Option_Some(d_349_ch_)))
                            elif True:
                                return Wrappers.Result_Success(((parms) + (((longMap)[d_350_opt_]).MakeArg(Wrappers.Option_Some(_dafny.Seq((arg)[1::])))), Wrappers.Option_None()))
                        elif True:
                            in168_ = _dafny.Seq((arg)[1::])
                            in169_ = longMap
                            in170_ = shortMap
                            in171_ = (parms) + (((longMap)[d_350_opt_]).MakeArg(Wrappers.Option_None()))
                            arg = in168_
                            longMap = in169_
                            shortMap = in170_
                            parms = in171_
                            raise _dafny.TailCall()
                    elif True:
                        return Wrappers.Result_Failure(((_dafny.Seq("Short option '")) + (_dafny.Seq([d_349_ch_]))) + (_dafny.Seq("' not recognized.")))
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
        d_351_x_: _dafny.Map = source__
        def lambda25_(forall_var_5_):
            d_352_k_: _dafny.Seq = forall_var_5_
            return not ((d_352_k_) in (d_351_x_)) or ((((d_351_x_)[d_352_k_]).name) == (d_352_k_))

        return _dafny.quantifier((d_351_x_).keys.Elements, True, lambda25_)

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

