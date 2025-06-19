// Class __default
// Dafny class __default compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<Boolean, dafny.DafnySequence<? extends Character>> Example(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> args)
  {
    Wrappers_Compile.Result<Boolean, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<Boolean, dafny.DafnySequence<? extends Character>>Default(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), false);
    dafny.DafnySequence<? extends Param> _0_MyOptions;
    _0_MyOptions = dafny.DafnySequence.<Param> of(Param._typeDescriptor(), Param.create_Flag(dafny.DafnySequence.asString("foo"), dafny.DafnySequence.asString("Does foo things"), __default.NullChar(), false, false, Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Param.create_Opt(dafny.DafnySequence.asString("two"), dafny.DafnySequence.asString("Does bar things to thingy"), dafny.DafnySequence.asString("thingy"), 't', Unused.create_UnusedOk(), false, Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Tri.create_No()), Param.create_Command(Options.create(dafny.DafnySequence.asString("command"), dafny.DafnySequence.asString("Does command stuff"), dafny.DafnySequence.<Param> of(Param._typeDescriptor(), Param.create_Opt(dafny.DafnySequence.asString("two"), dafny.DafnySequence.asString("Does bar things to thingy"), dafny.DafnySequence.asString("thingy"), 't', Unused.create_UnusedOk(), false, Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Tri.create_No()), Param.create_Flag(dafny.DafnySequence.asString("foo"), dafny.DafnySequence.asString("Does foo things"), __default.NullChar(), false, false, Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))))));
    Options _1_opts;
    _1_opts = Options.create(dafny.DafnySequence.asString("myProg"), dafny.DafnySequence.asString("does prog stuff"), _0_MyOptions);
    Wrappers_Compile.Result<Parsed, dafny.DafnySequence<? extends Character>> _2_valueOrError0 = Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>Default(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed.Default());
    _2_valueOrError0 = __default.GetOptions(_1_opts, args);
    if ((_2_valueOrError0).IsFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      output = (_2_valueOrError0).<Boolean>PropagateFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.TypeDescriptor.BOOLEAN);
      return output;
    }
    Parsed _3_x;
    _3_x = (_2_valueOrError0).Extract(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _4_h;
    _4_h = __default.NeedsHelp(_1_opts, _3_x, dafny.DafnySequence.asString(""));
    if ((_4_h).is_Some()) {
      System.out.print(((_4_h).dtor_value()).verbatimString());
      output = Wrappers_Compile.Result.<Boolean, dafny.DafnySequence<? extends Character>>create_Success(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), true);
      return output;
    }
    output = Wrappers_Compile.Result.<Boolean, dafny.DafnySequence<? extends Character>>create_Success(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), true);
    return output;
  }
  public static <__T> dafny.DafnySequence<? extends __T> Filter(dafny.TypeDescriptor<__T> _td___T, java.util.function.Function<__T, Boolean> f, dafny.DafnySequence<? extends __T> xs)
  {
    dafny.DafnySequence<? extends __T> _0___accumulator = dafny.DafnySequence.<__T> empty(_td___T);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
        return dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> empty(_td___T));
      } else {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(_0___accumulator, ((((boolean)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))) ? (dafny.DafnySequence.<__T> of(_td___T, ((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) : (dafny.DafnySequence.<__T> empty(_td___T))));
        java.util.function.Function<__T, Boolean> _in0 = f;
        dafny.DafnySequence<? extends __T> _in1 = (xs).drop(java.math.BigInteger.ONE);
        f = _in0;
        xs = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static boolean IsHelp(Parsed args) {
    return ((java.math.BigInteger.valueOf(((args).dtor_params()).length())).signum() != 0) && (((((OneArg)(java.lang.Object)(((args).dtor_params()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()).equals(__default.HELP__STR()));
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NeedsHelp(Options opts, Parsed args, dafny.DafnySequence<? extends Character> prefix)
  {
    TAIL_CALL_START: while (true) {
      if (__default.IsHelp(args)) {
        return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.GetHelp(opts, prefix));
      } else if (((args).dtor_subcommand()).is_Some()) {
        Wrappers_Compile.Option<java.math.BigInteger> _0_valueOrError0 = __default.GetSubOptions((opts).dtor_params(), (((args).dtor_subcommand()).dtor_value()).dtor_command(), java.math.BigInteger.ZERO);
        if ((_0_valueOrError0).IsFailure(_System.nat._typeDescriptor())) {
          return (_0_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        } else {
          java.math.BigInteger _1_pos = (_0_valueOrError0).Extract(_System.nat._typeDescriptor());
          Options _in0 = (((Param)(java.lang.Object)(((opts).dtor_params()).select(dafny.Helpers.toInt((_1_pos)))))).dtor_options();
          Parsed _in1 = ((args).dtor_subcommand()).dtor_value();
          dafny.DafnySequence<? extends Character> _in2 = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(prefix, (args).dtor_command()), dafny.DafnySequence.asString(" "));
          opts = _in0;
          args = _in1;
          prefix = _in2;
          continue TAIL_CALL_START;
        }
      } else {
        return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> GetHelp(Options opts, dafny.DafnySequence<? extends Character> prefix)
  {
    dafny.DafnySequence<? extends Param> _0_newOpts = dafny.DafnySequence.<Param>concatenate((opts).dtor_params(), dafny.DafnySequence.<Param> of(Param._typeDescriptor(), __default.HELP__PARAM()));
    java.math.BigInteger _1_longLen = __default.GetLongLen(_0_newOpts, java.math.BigInteger.valueOf(6L));
    java.math.BigInteger _2_commandLen = __default.GetCommandLen(_0_newOpts, java.math.BigInteger.ZERO);
    if ((_2_commandLen).signum() == 0) {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("USAGE : "), prefix), (opts).dtor_name()), dafny.DafnySequence.asString(" [args...]\n")), (opts).dtor_help()), dafny.DafnySequence.asString("\n")), __default.GetHelp2(_0_newOpts, _1_longLen));
    } else {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("USAGE : "), (opts).dtor_name()), dafny.DafnySequence.asString(" [args...] command [args...]\n")), (opts).dtor_help()), dafny.DafnySequence.asString("\n")), dafny.DafnySequence.asString("\nAvailable Commands:\n")), __default.GetCmdHelp(_0_newOpts, _2_commandLen)), dafny.DafnySequence.asString("\nAvailable Options:\n")), __default.GetHelp2(_0_newOpts, _1_longLen));
    }
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> OptValue(dafny.DafnySequence<? extends OneArg> args, dafny.DafnySequence<? extends Character> arg)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()).equals(arg)) {
        return (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value();
      } else {
        dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends Character> _in1 = arg;
        args = _in0;
        arg = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static java.math.BigInteger FlagCount(dafny.DafnySequence<? extends OneArg> args, dafny.DafnySequence<? extends Character> arg)
  {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()).equals(arg)) {
        _0___accumulator = (_0___accumulator).add(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends Character> _in1 = arg;
        args = _in0;
        arg = _in1;
        continue TAIL_CALL_START;
      } else {
        dafny.DafnySequence<? extends OneArg> _in2 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends Character> _in3 = arg;
        args = _in2;
        arg = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> OptMapLast(dafny.DafnySequence<? extends OneArg> args, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> theMap)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return theMap;
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).is_Some()) {
        dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _in1 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>update(theMap, (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), ((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).dtor_value());
        args = _in0;
        theMap = _in1;
        continue TAIL_CALL_START;
      } else {
        dafny.DafnySequence<? extends OneArg> _in2 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _in3 = theMap;
        args = _in2;
        theMap = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> FlagsSet(dafny.DafnySequence<? extends OneArg> args, dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> theSet)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return theSet;
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).is_Some()) {
        dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> _in1 = theSet;
        args = _in0;
        theSet = _in1;
        continue TAIL_CALL_START;
      } else {
        dafny.DafnySequence<? extends OneArg> _in2 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> _in3 = dafny.DafnySet.<dafny.DafnySequence<? extends Character>>union(theSet, dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()));
        args = _in2;
        theSet = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> OptMapList(dafny.DafnySequence<? extends OneArg> args, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> theMap)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return theMap;
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).is_Some()) {
        if ((theMap).<dafny.DafnySequence<? extends Character>>contains((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name())) {
          dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _in1 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>update(theMap, (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>concatenate(((dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>)(java.lang.Object)((theMap).get((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()))), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).dtor_value())));
          args = _in0;
          theMap = _in1;
          continue TAIL_CALL_START;
        } else {
          dafny.DafnySequence<? extends OneArg> _in2 = (args).drop(java.math.BigInteger.ONE);
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _in3 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>update(theMap, (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).dtor_value()));
          args = _in2;
          theMap = _in3;
          continue TAIL_CALL_START;
        }
      } else {
        dafny.DafnySequence<? extends OneArg> _in4 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _in5 = theMap;
        args = _in4;
        theMap = _in5;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends java.math.BigInteger> FlagMapCount(dafny.DafnySequence<? extends OneArg> args, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends java.math.BigInteger> theMap)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return theMap;
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).is_Some()) {
        dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends java.math.BigInteger> _in1 = theMap;
        args = _in0;
        theMap = _in1;
        continue TAIL_CALL_START;
      } else if ((theMap).<dafny.DafnySequence<? extends Character>>contains((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name())) {
        dafny.DafnySequence<? extends OneArg> _in2 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends java.math.BigInteger> _in3 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, java.math.BigInteger>update(theMap, (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), (((java.math.BigInteger)(java.lang.Object)((theMap).get((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name())))).add(java.math.BigInteger.ONE));
        args = _in2;
        theMap = _in3;
        continue TAIL_CALL_START;
      } else {
        dafny.DafnySequence<? extends OneArg> _in4 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends java.math.BigInteger> _in5 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, java.math.BigInteger>update(theMap, (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), java.math.BigInteger.ONE);
        args = _in4;
        theMap = _in5;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> FlagSetCheck(dafny.DafnySequence<? extends OneArg> args, dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> theSet)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySet.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), theSet);
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).is_Some()) {
        if ((theSet).<dafny.DafnySequence<? extends Character>>contains((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name())) {
          return Wrappers_Compile.Result.<dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySet.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Duplicate arg : "), (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()));
        } else {
          dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
          dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> _in1 = dafny.DafnySet.<dafny.DafnySequence<? extends Character>>union(theSet, dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()));
          args = _in0;
          theSet = _in1;
          continue TAIL_CALL_START;
        }
      } else {
        dafny.DafnySequence<? extends OneArg> _in2 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> _in3 = theSet;
        args = _in2;
        theSet = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> OptMapCheck(dafny.DafnySequence<? extends OneArg> args, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> theMap)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), theMap);
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).is_Some()) {
        if ((theMap).<dafny.DafnySequence<? extends Character>>contains((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name())) {
          return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Duplicate arg : "), (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()));
        } else {
          dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _in1 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>update(theMap, (((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), ((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_value()).dtor_value());
          args = _in0;
          theMap = _in1;
          continue TAIL_CALL_START;
        }
      } else {
        dafny.DafnySequence<? extends OneArg> _in2 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _in3 = theMap;
        args = _in2;
        theMap = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> GetHelpHelp(Param opt) {
    if ((opt).is_Command()) {
      return dafny.DafnySequence.asString("");
    } else if ((opt).is_Flag()) {
      return (opt).dtor_help();
    } else {
      return dafny.DafnySequence.<Character>concatenate((opt).dtor_help(), (((opt).Required()) ? (dafny.DafnySequence.asString(" (required)")) : ((((opt).HasDefault()) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString(" (default : "), ((opt).dtor_unused()).dtor_val()), dafny.DafnySequence.asString(")"))) : (dafny.DafnySequence.asString(""))))));
    }
  }
  public static dafny.DafnySequence<? extends Character> OneHelp(Param opt, java.math.BigInteger longLen)
  {
    if (((opt).is_Command()) || (!((opt).ShowHelp()))) {
      return dafny.DafnySequence.asString("");
    } else {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(__default.GetShortHelp(opt), dafny.DafnySequence.asString("  ")), __default.GetLongHelp(opt, longLen)), dafny.DafnySequence.asString("  ")), __default.GetHelpHelp(opt)), dafny.DafnySequence.asString("\n"));
    }
  }
  public static dafny.DafnySequence<? extends Character> GetCommandHelp(Param opt, java.math.BigInteger commandLen)
  {
    dafny.DafnySequence<? extends Character> _0_name = (((java.math.BigInteger.valueOf((((opt).dtor_options()).dtor_name()).length())).compareTo(commandLen) < 0) ? (dafny.DafnySequence.<Character>concatenate(((opt).dtor_options()).dtor_name(), dafny.DafnySequence.Create(dafny.TypeDescriptor.CHAR, (commandLen).subtract(java.math.BigInteger.valueOf((((opt).dtor_options()).dtor_name()).length())), ((java.util.function.Function<java.math.BigInteger, Character>)(_1_i_boxed0) -> {
      java.math.BigInteger _1_i = ((java.math.BigInteger)(java.lang.Object)(_1_i_boxed0));
      return ' ';
    })))) : (((opt).dtor_options()).dtor_name()));
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(_0_name, dafny.DafnySequence.asString("  ")), ((opt).dtor_options()).dtor_help()), dafny.DafnySequence.asString("\n"));
  }
  public static dafny.DafnySequence<? extends Character> GetShortHelp(Param opt) {
    if (((opt).is_Opt()) || ((opt).is_Flag())) {
      if (((opt).dtor_short()) != (__default.NullChar())) {
        return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-"), dafny.DafnySequence.<Character> of((opt).dtor_short()));
      } else {
        return dafny.DafnySequence.asString("  ");
      }
    } else {
      return dafny.DafnySequence.asString("");
    }
  }
  public static dafny.DafnySequence<? extends Character> GetLongHelp(Param opt, java.math.BigInteger longLen)
  {
    if (((opt).is_Opt()) || ((opt).is_Flag())) {
      dafny.DafnySequence<? extends Character> _0_tmp = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("--"), (opt).dtor_name()), (((opt).is_Opt()) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("="), (opt).dtor_argName())) : (dafny.DafnySequence.asString(""))));
      if ((java.math.BigInteger.valueOf((_0_tmp).length())).compareTo(longLen) < 0) {
        return dafny.DafnySequence.<Character>concatenate(_0_tmp, dafny.DafnySequence.Create(dafny.TypeDescriptor.CHAR, (longLen).subtract(java.math.BigInteger.valueOf((_0_tmp).length())), ((java.util.function.Function<java.math.BigInteger, Character>)(_1_i_boxed0) -> {
          java.math.BigInteger _1_i = ((java.math.BigInteger)(java.lang.Object)(_1_i_boxed0));
          return ' ';
        })));
      } else {
        return _0_tmp;
      }
    } else {
      return dafny.DafnySequence.asString("");
    }
  }
  public static dafny.DafnySequence<? extends Character> GetHelp2(dafny.DafnySequence<? extends Param> opts, java.math.BigInteger longLen)
  {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.asString(""));
      } else {
        dafny.DafnySequence<? extends Character> _1_x = __default.OneHelp(((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), longLen);
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, _1_x);
        dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
        java.math.BigInteger _in1 = longLen;
        opts = _in0;
        longLen = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> GetCmdHelp(dafny.DafnySequence<? extends Param> opts, java.math.BigInteger commandLen)
  {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.asString(""));
      } else {
        dafny.DafnySequence<? extends Character> _1_x = (((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_Command()) ? (__default.GetCommandHelp(((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), commandLen)) : (dafny.DafnySequence.asString("")));
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, _1_x);
        dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
        java.math.BigInteger _in1 = commandLen;
        opts = _in0;
        commandLen = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static java.math.BigInteger GetLongLen(dafny.DafnySequence<? extends Param> opts, java.math.BigInteger max)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return max;
      } else {
        java.math.BigInteger _0_x = java.math.BigInteger.valueOf((__default.GetLongHelp(((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), java.math.BigInteger.ZERO)).length());
        java.math.BigInteger _1_newMax = (((_0_x).compareTo(max) > 0) ? (_0_x) : (max));
        dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
        java.math.BigInteger _in1 = _1_newMax;
        opts = _in0;
        max = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static java.math.BigInteger GetCommandLen(dafny.DafnySequence<? extends Param> opts, java.math.BigInteger max)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return max;
      } else {
        java.math.BigInteger _0_x = (((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_Command()) ? (java.math.BigInteger.valueOf((((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_options()).dtor_name()).length())) : (java.math.BigInteger.ZERO));
        java.math.BigInteger _1_newMax = (((_0_x).compareTo(max) > 0) ? (_0_x) : (max));
        dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
        java.math.BigInteger _in1 = _1_newMax;
        opts = _in0;
        max = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> AddShortAlias(dafny.DafnySequence<? extends Character> aliases, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> shortMap, dafny.DafnySequence<? extends Character> name)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((aliases).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), shortMap);
      } else if ((shortMap).<Character>contains(((char)(java.lang.Object)((aliases).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
        return Wrappers_Compile.Result.<dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Short alias '"), (aliases).subsequence(dafny.Helpers.toInt((java.math.BigInteger.ZERO)), dafny.Helpers.toInt((java.math.BigInteger.ONE)))), dafny.DafnySequence.asString("' for '")), name), dafny.DafnySequence.asString("' already in use as a short option.")));
      } else {
        dafny.DafnySequence<? extends Character> _in0 = (aliases).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _in1 = dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>update(shortMap, ((char)(java.lang.Object)((aliases).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), name);
        dafny.DafnySequence<? extends Character> _in2 = name;
        aliases = _in0;
        shortMap = _in1;
        name = _in2;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnySequence<? extends Character>> AddLongAlias(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> aliases, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> longMap, Param opt)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((aliases).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), longMap);
      } else if ((longMap).<dafny.DafnySequence<? extends Character>>contains(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((aliases).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
        return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Long alias '"), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((aliases).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), dafny.DafnySequence.asString("' already in use as a long option.")));
      } else {
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in0 = (aliases).drop(java.math.BigInteger.ONE);
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _in1 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>update(longMap, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((aliases).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), opt);
        Param _in2 = opt;
        aliases = _in0;
        longMap = _in1;
        opt = _in2;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>, dafny.DafnySequence<? extends Character>> GetMaps(dafny.DafnySequence<? extends Param> opts, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> longMap, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> shortMap, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> commandMap)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>create(longMap, shortMap, commandMap));
      } else {
        Param _0_opt = ((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
        if ((_0_opt).is_Command()) {
          Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), !(commandMap).<dafny.DafnySequence<? extends Character>>contains(((_0_opt).dtor_options()).dtor_name()), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Duplicate command in options : "), ((_0_opt).dtor_options()).dtor_name()));
          if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
            return (_1_valueOrError0).<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()));
          } else {
            dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
            dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _in1 = longMap;
            dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _in2 = shortMap;
            dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> _in3 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Options>update(commandMap, ((_0_opt).dtor_options()).dtor_name(), (_0_opt).dtor_options());
            opts = _in0;
            longMap = _in1;
            shortMap = _in2;
            commandMap = _in3;
            continue TAIL_CALL_START;
          }
        } else {
          Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), !(longMap).<dafny.DafnySequence<? extends Character>>contains((_0_opt).dtor_name()), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Duplicate long name in options : "), (_0_opt).dtor_name()));
          if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
            return (_2_valueOrError1).<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()));
          } else {
            dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _3_newLongMap = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>update(longMap, (_0_opt).dtor_name(), _0_opt);
            Wrappers_Compile.Result<dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = __default.AddShortAlias((_0_opt).ShortAlias(), shortMap, (_0_opt).dtor_name());
            if ((_4_valueOrError2).IsFailure(dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
              return (_4_valueOrError2).<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>>PropagateFailure(dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()));
            } else {
              dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _5_newShortMap = (_4_valueOrError2).Extract(dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = __default.AddLongAlias((_0_opt).LongAlias(), _3_newLongMap, _0_opt);
              if ((_6_valueOrError3).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                return (_6_valueOrError3).<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()));
              } else {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _7_newLongMap = (_6_valueOrError3).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                if (((_0_opt).dtor_short()) != (__default.NullChar())) {
                  char _8_short = (_0_opt).dtor_short();
                  if ((_5_newShortMap).<Character>contains(_8_short)) {
                    return Wrappers_Compile.Result.<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Duplicate short char in options : '"), dafny.DafnySequence.<Character> of(_8_short)), dafny.DafnySequence.asString("' for ")), (_0_opt).dtor_name()), dafny.DafnySequence.asString(" and ")), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_newShortMap).get(_8_short)))));
                  } else {
                    dafny.DafnySequence<? extends Param> _in4 = (opts).drop(java.math.BigInteger.ONE);
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _in5 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>update(_7_newLongMap, (_0_opt).dtor_name(), _0_opt);
                    dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _in6 = dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>update(_5_newShortMap, _8_short, (_0_opt).dtor_name());
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> _in7 = commandMap;
                    opts = _in4;
                    longMap = _in5;
                    shortMap = _in6;
                    commandMap = _in7;
                    continue TAIL_CALL_START;
                  }
                } else {
                  dafny.DafnySequence<? extends Param> _in8 = (opts).drop(java.math.BigInteger.ONE);
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _in9 = dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>update(_7_newLongMap, (_0_opt).dtor_name(), _0_opt);
                  dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _in10 = _5_newShortMap;
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> _in11 = commandMap;
                  opts = _in8;
                  longMap = _in9;
                  shortMap = _in10;
                  commandMap = _in11;
                  continue TAIL_CALL_START;
                }
              }
            }
          }
        }
      }
    }
  }
  public static <__T> Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> Print(dafny.TypeDescriptor<__T> _td___T, __T x)
  {
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _hresult = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    System.out.print(java.lang.String.valueOf(x));
    System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
    _hresult = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>create_Pass(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    return _hresult;
  }
  public static boolean ArgExists(dafny.DafnySequence<? extends OneArg> args, dafny.DafnySequence<? extends Character> name)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
        return false;
      } else if (((((OneArg)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()).equals(name)) {
        return true;
      } else {
        dafny.DafnySequence<? extends OneArg> _in0 = (args).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends Character> _in1 = name;
        args = _in0;
        name = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends OneArg>, dafny.DafnySequence<? extends Character>> PostProcess2(dafny.DafnySequence<? extends Param> opts, dafny.DafnySequence<? extends OneArg> args, dafny.DafnySequence<? extends OneArg> newArgs)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends OneArg>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), newArgs);
      } else if ((((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_Opt()) && ((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).Required())) && (!(__default.ArgExists(args, (((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name())))) {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends OneArg>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Option '"), (((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()), dafny.DafnySequence.asString("' is required, but was not used.")));
      } else if ((((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_Opt()) && ((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).HasDefault())) && (!(__default.ArgExists(args, (((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name())))) {
        dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends OneArg> _in1 = args;
        dafny.DafnySequence<? extends OneArg> _in2 = dafny.DafnySequence.<OneArg>concatenate(newArgs, dafny.DafnySequence.<OneArg> of(OneArg._typeDescriptor(), OneArg.create((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_unused()).dtor_val()))));
        opts = _in0;
        args = _in1;
        newArgs = _in2;
        continue TAIL_CALL_START;
      } else {
        dafny.DafnySequence<? extends Param> _in3 = (opts).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends OneArg> _in4 = args;
        dafny.DafnySequence<? extends OneArg> _in5 = newArgs;
        opts = _in3;
        args = _in4;
        newArgs = _in5;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Option<java.math.BigInteger> GetSubOptions(dafny.DafnySequence<? extends Param> opts, dafny.DafnySequence<? extends Character> name, java.math.BigInteger pos)
  {
    TAIL_CALL_START: while (true) {
      if (java.util.Objects.equals(java.math.BigInteger.valueOf((opts).length()), pos)) {
        return Wrappers_Compile.Option.<java.math.BigInteger>create_None(_System.nat._typeDescriptor());
      } else if (((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((pos)))))).is_Command()) && ((((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((pos)))))).dtor_options()).dtor_name()).equals(name))) {
        return Wrappers_Compile.Option.<java.math.BigInteger>create_Some(_System.nat._typeDescriptor(), pos);
      } else {
        dafny.DafnySequence<? extends Param> _in0 = opts;
        dafny.DafnySequence<? extends Character> _in1 = name;
        java.math.BigInteger _in2 = (pos).add(java.math.BigInteger.ONE);
        opts = _in0;
        name = _in1;
        pos = _in2;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<Parsed, dafny.DafnySequence<? extends Character>> PostProcess(Options opts, Parsed args)
  {
    Parsed _pat_let_tv0 = args;
    Parsed _pat_let_tv1 = args;
    if (__default.IsHelp(args)) {
      return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Success(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), args);
    } else {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends OneArg>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.PostProcess2((opts).dtor_params(), (args).dtor_params(), dafny.DafnySequence.<OneArg> empty(OneArg._typeDescriptor()));
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_0_valueOrError0).<Parsed>PropagateFailure(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends OneArg> _1_newParams = (_0_valueOrError0).Extract(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        if (((args).dtor_subcommand()).is_Some()) {
          Wrappers_Compile.Option<java.math.BigInteger> _2_optPos = __default.GetSubOptions((opts).dtor_params(), (((args).dtor_subcommand()).dtor_value()).dtor_command(), java.math.BigInteger.ZERO);
          if ((_2_optPos).is_Some()) {
            Wrappers_Compile.Result<Parsed, dafny.DafnySequence<? extends Character>> _3_valueOrError1 = __default.PostProcess((((Param)(java.lang.Object)(((opts).dtor_params()).select(dafny.Helpers.toInt(((_2_optPos).dtor_value())))))).dtor_options(), ((args).dtor_subcommand()).dtor_value());
            if ((_3_valueOrError1).IsFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
              return (_3_valueOrError1).<Parsed>PropagateFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
            } else {
              Parsed _4_sub = (_3_valueOrError1).Extract(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Success(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((Parsed)(java.lang.Object)(dafny.Helpers.<Parsed, Parsed>Let(args, boxed0 -> {
  Parsed _pat_let0_0 = ((Parsed)(java.lang.Object)(boxed0));
  return ((Parsed)(java.lang.Object)(dafny.Helpers.<Parsed, Parsed>Let(_pat_let0_0, boxed1 -> {
    Parsed _5_dt__update__tmp_h0 = ((Parsed)(java.lang.Object)(boxed1));
    return ((Parsed)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Option<Parsed>, Parsed>Let(Wrappers_Compile.Option.<Parsed>create_Some(Parsed._typeDescriptor(), _4_sub), boxed2 -> {
      Wrappers_Compile.Option<Parsed> _pat_let1_0 = ((Wrappers_Compile.Option<Parsed>)(java.lang.Object)(boxed2));
      return ((Parsed)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Option<Parsed>, Parsed>Let(_pat_let1_0, boxed3 -> {
        Wrappers_Compile.Option<Parsed> _6_dt__update_hsubcommand_h0 = ((Wrappers_Compile.Option<Parsed>)(java.lang.Object)(boxed3));
        return ((Parsed)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends OneArg>, Parsed>Let(dafny.DafnySequence.<OneArg>concatenate((_pat_let_tv0).dtor_params(), _1_newParams), boxed4 -> {
          dafny.DafnySequence<? extends OneArg> _pat_let2_0 = ((dafny.DafnySequence<? extends OneArg>)(java.lang.Object)(boxed4));
          return ((Parsed)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends OneArg>, Parsed>Let(_pat_let2_0, boxed5 -> {
            dafny.DafnySequence<? extends OneArg> _7_dt__update_hparams_h0 = ((dafny.DafnySequence<? extends OneArg>)(java.lang.Object)(boxed5));
            return Parsed.create((_5_dt__update__tmp_h0).dtor_command(), _7_dt__update_hparams_h0, (_5_dt__update__tmp_h0).dtor_files(), _6_dt__update_hsubcommand_h0);
          }
          )));
        }
        )));
      }
      )));
    }
    )));
  }
  )));
}
))));
            }
          } else {
            return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Internal error in GetOpt::PostProcess"));
          }
        } else {
          return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Success(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((Parsed)(java.lang.Object)(dafny.Helpers.<Parsed, Parsed>Let(args, boxed6 -> {
  Parsed _pat_let3_0 = ((Parsed)(java.lang.Object)(boxed6));
  return ((Parsed)(java.lang.Object)(dafny.Helpers.<Parsed, Parsed>Let(_pat_let3_0, boxed7 -> {
    Parsed _8_dt__update__tmp_h1 = ((Parsed)(java.lang.Object)(boxed7));
    return ((Parsed)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends OneArg>, Parsed>Let(dafny.DafnySequence.<OneArg>concatenate((_pat_let_tv1).dtor_params(), _1_newParams), boxed8 -> {
      dafny.DafnySequence<? extends OneArg> _pat_let4_0 = ((dafny.DafnySequence<? extends OneArg>)(java.lang.Object)(boxed8));
      return ((Parsed)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends OneArg>, Parsed>Let(_pat_let4_0, boxed9 -> {
        dafny.DafnySequence<? extends OneArg> _9_dt__update_hparams_h1 = ((dafny.DafnySequence<? extends OneArg>)(java.lang.Object)(boxed9));
        return Parsed.create((_8_dt__update__tmp_h1).dtor_command(), _9_dt__update_hparams_h1, (_8_dt__update__tmp_h1).dtor_files(), (_8_dt__update__tmp_h1).dtor_subcommand());
      }
      )));
    }
    )));
  }
  )));
}
))));
        }
      }
    }
  }
  public static boolean AllDigits(dafny.DafnySequence<? extends Character> s) {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((s).length())).signum() == 0) {
        return true;
      } else if ((('0') <= (((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) && ((((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= ('9'))) {
        dafny.DafnySequence<? extends Character> _in0 = (s).drop(java.math.BigInteger.ONE);
        s = _in0;
        continue TAIL_CALL_START;
      } else {
        return false;
      }
    }
  }
  public static boolean ValidPositional(dafny.DafnySequence<? extends Character> s) {
    if ((java.math.BigInteger.valueOf((s).length())).signum() == 0) {
      return true;
    } else if ((((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) != ('-')) {
      return true;
    } else {
      return __default.AllDigits((s).drop(java.math.BigInteger.ONE));
    }
  }
  public static Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> TestPositionals(dafny.DafnySequence<? extends Param> opts, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> optional)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>create_Pass(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      } else if (!((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_Opt())) {
        dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _in1 = optional;
        opts = _in0;
        optional = _in1;
        continue TAIL_CALL_START;
      } else if (java.util.Objects.equals((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_positional(), Tri.create_No())) {
        dafny.DafnySequence<? extends Param> _in2 = (opts).drop(java.math.BigInteger.ONE);
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _in3 = optional;
        opts = _in2;
        optional = _in3;
        continue TAIL_CALL_START;
      } else if (java.util.Objects.equals((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_positional(), Tri.create_Maybe())) {
        dafny.DafnySequence<? extends Param> _in4 = (opts).drop(java.math.BigInteger.ONE);
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _in5 = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name());
        opts = _in4;
        optional = _in5;
        continue TAIL_CALL_START;
      } else if ((optional).is_None()) {
        dafny.DafnySequence<? extends Param> _in6 = (opts).drop(java.math.BigInteger.ONE);
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _in7 = optional;
        opts = _in6;
        optional = _in7;
        continue TAIL_CALL_START;
      } else {
        return Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>create_Fail(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Required positional argument '"), (((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()), dafny.DafnySequence.asString("' follows optional positional argument '")), (optional).dtor_value()), dafny.DafnySequence.asString("'.")));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>> GetPositionals(dafny.DafnySequence<? extends Param> opts, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> args, dafny.DafnySequence<? extends OneArg> params)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((opts).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>create(args, params));
      } else if (!((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_Opt())) {
        dafny.DafnySequence<? extends Param> _in0 = (opts).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in1 = args;
        dafny.DafnySequence<? extends OneArg> _in2 = params;
        opts = _in0;
        args = _in1;
        params = _in2;
        continue TAIL_CALL_START;
      } else if (java.util.Objects.equals((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_positional(), Tri.create_No())) {
        dafny.DafnySequence<? extends Param> _in3 = (opts).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in4 = args;
        dafny.DafnySequence<? extends OneArg> _in5 = params;
        opts = _in3;
        args = _in4;
        params = _in5;
        continue TAIL_CALL_START;
      } else if (java.util.Objects.equals((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_positional(), Tri.create_Yes())) {
        if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
          return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Positional arg '"), (((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()), dafny.DafnySequence.asString("' is required, but we've run out of arguments.")));
        } else if (__default.ValidPositional(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
          dafny.DafnySequence<? extends Param> _in6 = (opts).drop(java.math.BigInteger.ONE);
          dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in7 = (args).drop(java.math.BigInteger.ONE);
          dafny.DafnySequence<? extends OneArg> _in8 = dafny.DafnySequence.<OneArg>concatenate(params, dafny.DafnySequence.<OneArg> of(OneArg._typeDescriptor(), OneArg.create((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))));
          opts = _in6;
          args = _in7;
          params = _in8;
          continue TAIL_CALL_START;
        } else {
          return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Positional arg "), (((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name()), dafny.DafnySequence.asString(" matched with invalid positional value '")), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), dafny.DafnySequence.asString("'.")));
        }
      } else {
        if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
          return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>create(args, params));
        } else if (__default.ValidPositional(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
          dafny.DafnySequence<? extends Param> _in9 = (opts).drop(java.math.BigInteger.ONE);
          dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in10 = (args).drop(java.math.BigInteger.ONE);
          dafny.DafnySequence<? extends OneArg> _in11 = dafny.DafnySequence.<OneArg>concatenate(params, dafny.DafnySequence.<OneArg> of(OneArg._typeDescriptor(), OneArg.create((((Param)(java.lang.Object)((opts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_name(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))));
          opts = _in9;
          args = _in10;
          params = _in11;
          continue TAIL_CALL_START;
        } else {
          return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>create(args, params));
        }
      }
    }
  }
  public static Wrappers_Compile.Result<Parsed, dafny.DafnySequence<? extends Character>> GetOptions(Options opts, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> args)
  {
    dafny.DafnySequence<? extends Param> _0_newOpts = dafny.DafnySequence.<Param>concatenate((opts).dtor_params(), dafny.DafnySequence.<Param> of(Param._typeDescriptor(), __default.HELP__PARAM()));
    dafny.DafnySequence<? extends Param> _1_inherits = __default.<Param>Filter(Param._typeDescriptor(), ((java.util.function.Function<Param, Boolean>)(_2_o_boxed0) -> {
      Param _2_o = ((Param)(java.lang.Object)(_2_o_boxed0));
      return (_2_o).Inherits();
    }), _0_newOpts);
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError0 = __default.TestPositionals(_0_newOpts, Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_3_valueOrError0).<Parsed>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
    } else {
      Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>> _4_valueOrError1 = __default.GetPositionals(_0_newOpts, (args).drop(java.math.BigInteger.ONE), dafny.DafnySequence.<OneArg> empty(OneArg._typeDescriptor()));
      if ((_4_valueOrError1).IsFailure(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_4_valueOrError1).<Parsed>PropagateFailure(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
      } else {
        dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>> _let_tmp_rhs0 = (_4_valueOrError1).Extract(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _5_newArgs = ((dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>)_let_tmp_rhs0).dtor__0()));
        dafny.DafnySequence<? extends OneArg> _6_params = ((dafny.DafnySequence<? extends OneArg>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>)_let_tmp_rhs0).dtor__1()));
        Wrappers_Compile.Result<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>, dafny.DafnySequence<? extends Character>> _7_valueOrError2 = __default.GetMaps(_0_newOpts, dafny.DafnyMap.fromElements(), dafny.DafnyMap.fromElements(), dafny.DafnyMap.fromElements());
        if ((_7_valueOrError2).IsFailure(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_7_valueOrError2).<Parsed>PropagateFailure(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
        } else {
          dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>> _let_tmp_rhs1 = (_7_valueOrError2).Extract(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _8_longMap = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>)(java.lang.Object)(((dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>)_let_tmp_rhs1).dtor__0()));
          dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _9_shortMap = ((dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>)(java.lang.Object)(((dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>)_let_tmp_rhs1).dtor__1()));
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> _10_commandMap = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>)(java.lang.Object)(((dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>)_let_tmp_rhs1).dtor__2()));
          Context _11_context = Context.create(_8_longMap, _9_shortMap, _1_inherits, _10_commandMap, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
          Wrappers_Compile.Result<Parsed, dafny.DafnySequence<? extends Character>> _12_valueOrError3 = __default.GetOptions2(_5_newArgs, _11_context, _6_params, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
          if ((_12_valueOrError3).IsFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
            return (_12_valueOrError3).<Parsed>PropagateFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
          } else {
            Parsed _13_result = (_12_valueOrError3).Extract(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
            return __default.PostProcess(opts, _13_result);
          }
        }
      }
    }
  }
  public static <__T> java.math.BigInteger IndexOf(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, __T v)
  {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    TAIL_CALL_START: while (true) {
      if (java.util.Objects.equals(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), v)) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else {
        _0___accumulator = (_0___accumulator).add(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends __T> _in0 = (xs).drop(java.math.BigInteger.ONE);
        __T _in1 = v;
        xs = _in0;
        v = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> dafny.Tuple2<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>> SplitOnce(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, __T delim)
  {
    java.math.BigInteger _0_i = __default.<__T>IndexOf(_td___T, s, delim);
    return dafny.Tuple2.<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>create((s).take(_0_i), (s).drop((_0_i).add(java.math.BigInteger.ONE)));
  }
  public static Wrappers_Compile.Result<Parsed, dafny.DafnySequence<? extends Character>> GetOptions2(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> args, Context context, dafny.DafnySequence<? extends OneArg> parms, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> files)
  {
    if ((java.math.BigInteger.valueOf((args).length())).signum() == 0) {
      return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Success(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed.create((context).dtor_command(), parms, files, Wrappers_Compile.Option.<Parsed>create_None(Parsed._typeDescriptor())));
    } else if (((context).dtor_commands()).<dafny.DafnySequence<? extends Character>>contains(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
      dafny.DafnySequence<? extends Param> _0_inherits = __default.<Param>Filter(Param._typeDescriptor(), ((java.util.function.Function<Param, Boolean>)(_1_o_boxed0) -> {
        Param _1_o = ((Param)(java.lang.Object)(_1_o_boxed0));
        return (_1_o).Inherits();
      }), (((Options)(java.lang.Object)(((context).dtor_commands()).get(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))).dtor_params());
      dafny.DafnySequence<? extends Param> _2_newOpts = dafny.DafnySequence.<Param>concatenate((((Options)(java.lang.Object)(((context).dtor_commands()).get(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))).dtor_params(), (context).dtor_inherits());
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError0 = __default.TestPositionals(_2_newOpts, Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_3_valueOrError0).<Parsed>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
      } else {
        Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>, dafny.DafnySequence<? extends Character>> _4_valueOrError1 = __default.GetPositionals(_2_newOpts, (args).drop(java.math.BigInteger.ONE), dafny.DafnySequence.<OneArg> empty(OneArg._typeDescriptor()));
        if ((_4_valueOrError1).IsFailure(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_4_valueOrError1).<Parsed>PropagateFailure(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
        } else {
          dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>> _let_tmp_rhs0 = (_4_valueOrError1).Extract(dafny.Tuple2.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>_typeDescriptor(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _5_newArgs = ((dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>)_let_tmp_rhs0).dtor__0()));
          dafny.DafnySequence<? extends OneArg> _6_params = ((dafny.DafnySequence<? extends OneArg>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends OneArg>>)_let_tmp_rhs0).dtor__1()));
          Wrappers_Compile.Result<dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>, dafny.DafnySequence<? extends Character>> _7_valueOrError2 = __default.GetMaps(_2_newOpts, dafny.DafnyMap.fromElements(), dafny.DafnyMap.fromElements(), dafny.DafnyMap.fromElements());
          if ((_7_valueOrError2).IsFailure(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
            return (_7_valueOrError2).<Parsed>PropagateFailure(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
          } else {
            dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>> _let_tmp_rhs1 = (_7_valueOrError2).Extract(dafny.Tuple3.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Param>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Param._typeDescriptor()), dafny.DafnyMap.<Character, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), CommandMap._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
            dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _8_longMap = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>)(java.lang.Object)(((dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>)_let_tmp_rhs1).dtor__0()));
            dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _9_shortMap = ((dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>)(java.lang.Object)(((dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>)_let_tmp_rhs1).dtor__1()));
            dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> _10_commandSet = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>)(java.lang.Object)(((dafny.Tuple3<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param>, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>)_let_tmp_rhs1).dtor__2()));
            Context _11_newContext = Context.create(_8_longMap, _9_shortMap, dafny.DafnySequence.<Param>concatenate((context).dtor_inherits(), _0_inherits), _10_commandSet, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
            java.math.BigInteger _12_lostArgs = (java.math.BigInteger.valueOf((args).length())).subtract(java.math.BigInteger.valueOf((_5_newArgs).length()));
            Wrappers_Compile.Result<Parsed, dafny.DafnySequence<? extends Character>> _13_valueOrError3 = __default.GetOptions2((args).drop(_12_lostArgs), _11_newContext, _6_params, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
            if ((_13_valueOrError3).IsFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
              return (_13_valueOrError3).<Parsed>PropagateFailure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
            } else {
              Parsed _14_result = (_13_valueOrError3).Extract(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Success(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed.create((context).dtor_command(), parms, files, Wrappers_Compile.Option.<Parsed>create_Some(Parsed._typeDescriptor(), _14_result)));
            }
          }
        }
      }
    } else if ((((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).equals(dafny.DafnySequence.asString("--"))) {
      return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Success(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed.create((context).dtor_command(), parms, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>concatenate(files, (args).drop(java.math.BigInteger.ONE)), Wrappers_Compile.Option.<Parsed>create_None(Parsed._typeDescriptor())));
    } else if ((dafny.DafnySequence.asString("--")).isProperPrefixOf(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
      dafny.DafnySequence<? extends Character> _15_longOpt = (((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).drop(java.math.BigInteger.valueOf(2L));
      if ((_15_longOpt).contains('=')) {
        dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _let_tmp_rhs2 = __default.<Character>SplitOnce(dafny.TypeDescriptor.CHAR, _15_longOpt, '=');
        dafny.DafnySequence<? extends Character> _16_opt = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>)_let_tmp_rhs2).dtor__0()));
        dafny.DafnySequence<? extends Character> _17_arg = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>)_let_tmp_rhs2).dtor__1()));
        if (((context).dtor_longMap()).<dafny.DafnySequence<? extends Character>>contains(_16_opt)) {
          if ((((Param)(java.lang.Object)(((context).dtor_longMap()).get(_16_opt)))).NeedsArg()) {
            return __default.GetOptions2((args).drop(java.math.BigInteger.ONE), context, dafny.DafnySequence.<OneArg>concatenate(parms, (((Param)(java.lang.Object)(((context).dtor_longMap()).get(_16_opt)))).MakeArg(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _17_arg))), files);
          } else {
            return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Option "), _16_opt), dafny.DafnySequence.asString(" does not take an argument, but it got one.")));
          }
        } else {
          return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Option "), _16_opt), dafny.DafnySequence.asString(" not recognized.")));
        }
      } else if (((context).dtor_longMap()).<dafny.DafnySequence<? extends Character>>contains(_15_longOpt)) {
        Param _18_opt = ((Param)(java.lang.Object)(((context).dtor_longMap()).get(_15_longOpt)));
        if ((_18_opt).NeedsArg()) {
          if ((java.math.BigInteger.valueOf((args).length())).compareTo(java.math.BigInteger.valueOf(2L)) < 0) {
            return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Option "), _15_longOpt), dafny.DafnySequence.asString(" requires an argument, but didn't get one.")));
          } else {
            return __default.GetOptions2((args).drop(java.math.BigInteger.valueOf(2L)), context, dafny.DafnySequence.<OneArg>concatenate(parms, (_18_opt).MakeArg(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))))), files);
          }
        } else if ((((_18_opt).is_Flag()) && ((_18_opt).dtor_solo())) && (((!java.util.Objects.equals(java.math.BigInteger.valueOf((args).length()), java.math.BigInteger.ONE)) || ((java.math.BigInteger.valueOf((parms).length())).signum() != 0)) || ((java.math.BigInteger.valueOf((files).length())).signum() != 0))) {
          return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Option '"), _15_longOpt), dafny.DafnySequence.asString("' used with other stuff, but must only be used alone.")));
        } else {
          return __default.GetOptions2((args).drop(java.math.BigInteger.ONE), context, dafny.DafnySequence.<OneArg>concatenate(parms, (_18_opt).MakeArg(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))), files);
        }
      } else {
        return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Option "), _15_longOpt), dafny.DafnySequence.asString(" not recognized.")));
      }
    } else if ((dafny.DafnySequence.asString("-")).equals(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
      return __default.GetOptions2((args).drop(java.math.BigInteger.ONE), context, parms, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>concatenate(files, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))));
    } else if ((dafny.DafnySequence.asString("-")).isProperPrefixOf(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
      Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>, dafny.DafnySequence<? extends Character>> _19_valueOrError4 = __default.GetShort((((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).drop(java.math.BigInteger.ONE), (context).dtor_longMap(), (context).dtor_shortMap(), dafny.DafnySequence.<OneArg> empty(OneArg._typeDescriptor()));
      if ((_19_valueOrError4).IsFailure(dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>_typeDescriptor(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), Wrappers_Compile.Option.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_19_valueOrError4).<Parsed>PropagateFailure(dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>_typeDescriptor(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), Wrappers_Compile.Option.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Parsed._typeDescriptor());
      } else {
        dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>> _let_tmp_rhs3 = (_19_valueOrError4).Extract(dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>_typeDescriptor(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), Wrappers_Compile.Option.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        dafny.DafnySequence<? extends OneArg> _20_newParms = ((dafny.DafnySequence<? extends OneArg>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>)_let_tmp_rhs3).dtor__0()));
        Wrappers_Compile.Option<Character> _21_nextParm = ((Wrappers_Compile.Option<Character>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>)_let_tmp_rhs3).dtor__1()));
        if ((_21_nextParm).is_None()) {
          return __default.GetOptions2((args).drop(java.math.BigInteger.ONE), context, dafny.DafnySequence.<OneArg>concatenate(parms, _20_newParms), files);
        } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((args).length()), java.math.BigInteger.ONE)) {
          return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Short option "), dafny.DafnySequence.<Character> of((_21_nextParm).dtor_value())), dafny.DafnySequence.asString(" requires argument but didn't get one.")));
        } else {
          dafny.DafnySequence<? extends Character> _22_longOpt = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(((context).dtor_shortMap()).get((_21_nextParm).dtor_value())));
          Param _23_opt = ((Param)(java.lang.Object)(((context).dtor_longMap()).get(_22_longOpt)));
          return __default.GetOptions2((args).drop(java.math.BigInteger.valueOf(2L)), context, dafny.DafnySequence.<OneArg>concatenate(dafny.DafnySequence.<OneArg>concatenate(parms, _20_newParms), (_23_opt).MakeArg(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))))), files);
        }
      }
    } else if ((java.math.BigInteger.valueOf(((context).dtor_commands()).size())).signum() == 0) {
      return __default.GetOptions2((args).drop(java.math.BigInteger.ONE), context, parms, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>concatenate(files, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))));
    } else {
      return Wrappers_Compile.Result.<Parsed, dafny.DafnySequence<? extends Character>>create_Failure(Parsed._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Unrecognized command "), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((args).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), dafny.DafnySequence.asString(" for ")), (context).dtor_command()), dafny.DafnySequence.asString("\nRun '")), (context).dtor_command()), dafny.DafnySequence.asString(" --help' for usage.")));
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>, dafny.DafnySequence<? extends Character>> GetShort(dafny.DafnySequence<? extends Character> arg, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> longMap, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> shortMap, dafny.DafnySequence<? extends OneArg> parms)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((arg).length())).signum() == 0) {
        return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>_typeDescriptor(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), Wrappers_Compile.Option.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>create(parms, Wrappers_Compile.Option.<Character>create_None(dafny.TypeDescriptor.CHAR)));
      } else {
        char _0_ch = ((char)(java.lang.Object)((arg).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
        if ((shortMap).<Character>contains(_0_ch)) {
          dafny.DafnySequence<? extends Character> _1_opt = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((shortMap).get(_0_ch)));
          if ((((Param)(java.lang.Object)((longMap).get(_1_opt)))).NeedsArg()) {
            if (java.util.Objects.equals(java.math.BigInteger.valueOf((arg).length()), java.math.BigInteger.ONE)) {
              return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>_typeDescriptor(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), Wrappers_Compile.Option.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>create(parms, Wrappers_Compile.Option.<Character>create_Some(dafny.TypeDescriptor.CHAR, _0_ch)));
            } else {
              return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>_typeDescriptor(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), Wrappers_Compile.Option.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>create(dafny.DafnySequence.<OneArg>concatenate(parms, (((Param)(java.lang.Object)((longMap).get(_1_opt)))).MakeArg(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (arg).drop(java.math.BigInteger.ONE)))), Wrappers_Compile.Option.<Character>create_None(dafny.TypeDescriptor.CHAR)));
            }
          } else {
            dafny.DafnySequence<? extends Character> _in0 = (arg).drop(java.math.BigInteger.ONE);
            dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _in1 = longMap;
            dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _in2 = shortMap;
            dafny.DafnySequence<? extends OneArg> _in3 = dafny.DafnySequence.<OneArg>concatenate(parms, (((Param)(java.lang.Object)((longMap).get(_1_opt)))).MakeArg(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
            arg = _in0;
            longMap = _in1;
            shortMap = _in2;
            parms = _in3;
            continue TAIL_CALL_START;
          }
        } else {
          return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.Tuple2.<dafny.DafnySequence<? extends OneArg>, Wrappers_Compile.Option<Character>>_typeDescriptor(dafny.DafnySequence.<OneArg>_typeDescriptor(OneArg._typeDescriptor()), Wrappers_Compile.Option.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Short option '"), dafny.DafnySequence.<Character> of(_0_ch)), dafny.DafnySequence.asString("' not recognized.")));
        }
      }
    }
  }
  public static char NullChar()
  {
    return (char)dafny.Helpers.toInt((java.math.BigInteger.ZERO));
  }
  public static dafny.DafnySequence<? extends Character> HELP__STR()
  {
    return dafny.DafnySequence.asString("help");
  }
  public static Param HELP__PARAM()
  {
    return Param.create_Flag(__default.HELP__STR(), dafny.DafnySequence.asString("This help text."), __default.NullChar(), true, true, Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  }
  @Override
  public java.lang.String toString() {
    return "GetOpt._default";
  }
}
