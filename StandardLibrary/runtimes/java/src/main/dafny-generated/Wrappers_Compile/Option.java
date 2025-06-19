// Class Option<T>
// Dafny class Option<T> compiled into Java
package Wrappers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Option<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public Option(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
  }
  public static <T> dafny.TypeDescriptor<Option<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Option<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Option<T>>referenceWithInitializer(Option.class, () -> Option.<T>Default(_td_T));
  }

  public static <T> Option<T> Default(dafny.TypeDescriptor<T> _td_T) {
    return Option.<T>create_None(_td_T);
  }
  @Deprecated()
  public static <T> Option<T> Default() {
    dafny.TypeDescriptor<T> _td_T = null;
    return Option.<T>create_None(_td_T);
  }
  public static <T> Option<T> create_None(dafny.TypeDescriptor<T> _td_T) {
    return new Option_None<T>(_td_T);
  }
  @Deprecated()
  public static <T> Option<T> create_None() {
    return new Option_None<T>(null);
  }
  public static <T> Option<T> create_Some(dafny.TypeDescriptor<T> _td_T, T value) {
    return new Option_Some<T>(_td_T, value);
  }
  @Deprecated()
  public static <T> Option<T> create_Some(T value) {
    return new Option_Some<T>(null, value);
  }
  public boolean is_None() { return this instanceof Option_None; }
  public boolean is_Some() { return this instanceof Option_Some; }
  public T dtor_value() {
    Option<T> d = this;
    return ((Option_Some<T>)d)._value;
  }
  public Result<T, dafny.DafnySequence<? extends Character>> ToResult(dafny.TypeDescriptor<T> _td_T) {
    Option<T> _source0 = this;
    if (_source0.is_None()) {
      return Result.<T, dafny.DafnySequence<? extends Character>>create_Failure(_td_T, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Option is None"));
    } else {
      T _0___mcc_h0 = ((Wrappers_Compile.Option_Some<T>)_source0)._value;
      T _1_v = _0___mcc_h0;
      return Result.<T, dafny.DafnySequence<? extends Character>>create_Success(_td_T, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _1_v);
    }
  }
  public <__R> Result<T, __R> ToResult_k(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<__R> _td___R, __R error)
  {
    Option<T> _source0 = this;
    if (_source0.is_None()) {
      return Result.<T, __R>create_Failure(_td_T, _td___R, error);
    } else {
      T _0___mcc_h0 = ((Wrappers_Compile.Option_Some<T>)_source0)._value;
      T _1_v = _0___mcc_h0;
      return Result.<T, __R>create_Success(_td_T, _td___R, _1_v);
    }
  }
  public T UnwrapOr(dafny.TypeDescriptor<T> _td_T, T default_)
  {
    Option<T> _source0 = this;
    if (_source0.is_None()) {
      return default_;
    } else {
      T _0___mcc_h0 = ((Wrappers_Compile.Option_Some<T>)_source0)._value;
      T _1_v = _0___mcc_h0;
      return _1_v;
    }
  }
  public boolean IsFailure(dafny.TypeDescriptor<T> _td_T) {
    return (this).is_None();
  }
  public <__U> Option<__U> PropagateFailure(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<__U> _td___U)
  {
    return Option.<__U>create_None(_td___U);
  }
  public T Extract(dafny.TypeDescriptor<T> _td_T) {
    return (this).dtor_value();
  }
}
