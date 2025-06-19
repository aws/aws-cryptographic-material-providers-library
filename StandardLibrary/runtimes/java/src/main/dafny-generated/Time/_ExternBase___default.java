// Class _ExternBase___default
// Dafny class __default compiled into Java
package Time;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static dafny.DafnySequence<? extends Character> FormatMilli(long diff) {
    dafny.DafnySequence<? extends Character> _0_whole = StandardLibrary_mString_Compile.__default.Base10Int2String(dafny.Helpers.unsignedToBigInteger((long) java.lang.Long.divideUnsigned(diff, (long) 1000L)));
    dafny.DafnySequence<? extends Character> _1_frac = StandardLibrary_mString_Compile.__default.Base10Int2String(dafny.Helpers.unsignedToBigInteger((long) java.lang.Long.remainderUnsigned(diff, (long) 1000L)));
    if (java.util.Objects.equals(java.math.BigInteger.valueOf((_1_frac).length()), java.math.BigInteger.ONE)) {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(_0_whole, dafny.DafnySequence.asString(".00")), _1_frac);
    } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((_1_frac).length()), java.math.BigInteger.valueOf(2L))) {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(_0_whole, dafny.DafnySequence.asString(".0")), _1_frac);
    } else {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(_0_whole, dafny.DafnySequence.asString(".")), _1_frac);
    }
  }
  public static dafny.DafnySequence<? extends Character> FormatMilliDiff(long start, long end)
  {
    if ((start) <= (end)) {
      return __default.FormatMilli(((long) (long) ((end) - (start))));
    } else {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-"), __default.FormatMilli(((long) (long) ((start) - (end)))));
    }
  }
  public static AbsoluteTime GetAbsoluteTime()
  {
    AbsoluteTime output = AbsoluteTime.Default();
    long _0_ClockTime;
    long _out0;
    _out0 = __default.CurrentRelativeTimeMilli();
    _0_ClockTime = _out0;
    long _1_CpuTime;
    long _out1;
    _out1 = __default.GetProcessCpuTimeMillis();
    _1_CpuTime = _out1;
    output = AbsoluteTime.create((_0_ClockTime), (_1_CpuTime));
    return output;
  }
  public static void PrintTimeSince(AbsoluteTime start)
  {
    RelativeTime _0_t;
    RelativeTime _out0;
    _out0 = __default.TimeSince(start);
    _0_t = _out0;
    __default.PrintTime(_0_t);
  }
  public static void PrintTimeSinceShort(AbsoluteTime start)
  {
    RelativeTime _0_t;
    RelativeTime _out0;
    _out0 = __default.TimeSince(start);
    _0_t = _out0;
    __default.PrintTimeShort(_0_t);
  }
  public static AbsoluteTime PrintTimeSinceShortChained(AbsoluteTime start)
  {
    AbsoluteTime x = AbsoluteTime.Default();
    AbsoluteTime _0_end;
    AbsoluteTime _out0;
    _out0 = __default.GetAbsoluteTime();
    _0_end = _out0;
    __default.PrintTimeShort(__default.TimeDiff(start, _0_end));
    x = _0_end;
    return x;
  }
  public static RelativeTime TimeDiff(AbsoluteTime start, AbsoluteTime end)
  {
    if ((java.lang.Long.compareUnsigned((start).dtor_ClockTime(), (end).dtor_ClockTime()) <= 0) && (java.lang.Long.compareUnsigned((start).dtor_CpuTime(), (end).dtor_CpuTime()) <= 0)) {
      return RelativeTime.create((long) (long) (((end).dtor_ClockTime()) - ((start).dtor_ClockTime())), (long) (long) (((end).dtor_CpuTime()) - ((start).dtor_CpuTime())));
    } else {
      return RelativeTime.create((long) 0L, (long) 0L);
    }
  }
  public static RelativeTime TimeSince(AbsoluteTime start)
  {
    RelativeTime output = RelativeTime.Default();
    if(true) {
      AbsoluteTime _0_end;
      AbsoluteTime _out0;
      _out0 = __default.GetAbsoluteTime();
      _0_end = _out0;
      output = __default.TimeDiff(start, _0_end);
    }
    return output;
  }
  public static void PrintTime(RelativeTime time)
  {
    System.out.print((dafny.DafnySequence.asString("Clock Time : ")).verbatimString());
    System.out.print((__default.FormatMilli((time).dtor_ClockTime())).verbatimString());
    System.out.print((dafny.DafnySequence.asString(" CPU Time : ")).verbatimString());
    System.out.print((__default.FormatMilli((time).dtor_CpuTime())).verbatimString());
    System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
  }
  public static void PrintTimeSinceLong(AbsoluteTime start, dafny.DafnySequence<? extends Character> tag, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> file)
  {
    RelativeTime _0_t;
    RelativeTime _out0;
    _out0 = __default.TimeSince(start);
    _0_t = _out0;
    __default.PrintTimeLong(_0_t, tag, file);
  }
  public static void PrintTimeLong(RelativeTime time, dafny.DafnySequence<? extends Character> tag, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> file)
  {
    dafny.DafnySequence<? extends Character> _0_val;
    _0_val = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(tag, dafny.DafnySequence.asString(" ")), OsLang.__default.GetOsShort()), dafny.DafnySequence.asString(" ")), OsLang.__default.GetLanguageShort()), dafny.DafnySequence.asString(" ")), __default.FormatMilli((time).dtor_ClockTime())), dafny.DafnySequence.asString(" ")), __default.FormatMilli((time).dtor_CpuTime())), dafny.DafnySequence.asString("\n"));
    System.out.print((_0_val).verbatimString());
    if ((file).is_Some()) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _1_utf8__val;
      _1_utf8__val = UTF8.__default.Encode(_0_val);
      if ((_1_utf8__val).is_Success()) {
        Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _2___v0;
        Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out0;
        _out0 = FileIO_Compile.__default.AppendBytesToFile((file).dtor_value(), (_1_utf8__val).dtor_value());
        _2___v0 = _out0;
      }
    }
  }
  public static void PrintTimeShort(RelativeTime time)
  {
    System.out.print((dafny.DafnySequence.asString("CPU:")).verbatimString());
    System.out.print((__default.FormatMilli((time).dtor_CpuTime())).verbatimString());
    System.out.print((dafny.DafnySequence.asString(" ")).verbatimString());
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> CreateGetCurrentTimeStampSuccess(dafny.DafnySequence<? extends Character> value) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), value);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> CreateGetCurrentTimeStampFailure(dafny.DafnySequence<? extends Character> error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), error);
  }
  @Override
  public java.lang.String toString() {
    return "Time._default";
  }
}
