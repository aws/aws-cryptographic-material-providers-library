// Class Result<T, R>
// Dafny class Result<T, R> compiled into Java
package Wrappers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Result<T, R> {
  protected dafny.TypeDescriptor<T> _td_T;
  protected dafny.TypeDescriptor<R> _td_R;
  public Result(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    this._td_T = _td_T;
    this._td_R = _td_R;
  }
  public static <T, R> dafny.TypeDescriptor<Result<T, R>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<Result<T, R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Result<T, R>>referenceWithInitializer(Result.class, () -> Result.<T, R>Default(_td_T, _td_R, _td_T.defaultValue()));
  }

  public static <T, R> Result<T, R> Default(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, T _default_T) {
    return Result.<T, R>create_Success(_td_T, _td_R, _default_T);
  }
  @Deprecated()
  public static <T, R> Result<T, R> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    dafny.TypeDescriptor<R> _td_R = null;
    return Result.<T, R>create_Success(_td_T, _td_R, _default_T);
  }
  public static <T, R> Result<T, R> create_Success(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, T value) {
    return new Result_Success<T, R>(_td_T, _td_R, value);
  }
  @Deprecated()
  public static <T, R> Result<T, R> create_Success(T value) {
    return new Result_Success<T, R>(null, null, value);
  }
  public static <T, R> Result<T, R> create_Failure(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, R error) {
    return new Result_Failure<T, R>(_td_T, _td_R, error);
  }
  @Deprecated()
  public static <T, R> Result<T, R> create_Failure(R error) {
    return new Result_Failure<T, R>(null, null, error);
  }
  public boolean is_Success() { return this instanceof Result_Success; }
  public boolean is_Failure() { return this instanceof Result_Failure; }
  public T dtor_value() {
    Result<T, R> d = this;
    return ((Result_Success<T, R>)d)._value;
  }
  public R dtor_error() {
    Result<T, R> d = this;
    return ((Result_Failure<T, R>)d)._error;
  }
  public Option<T> ToOption(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R)
  {
    Result<T, R> _source0 = this;
    if (_source0.is_Success()) {
      T _0___mcc_h0 = ((Wrappers_Compile.Result_Success<T, R>)_source0)._value;
      T _1_s = _0___mcc_h0;
      return Option.<T>create_Some(_td_T, _1_s);
    } else {
      R _2___mcc_h1 = ((Wrappers_Compile.Result_Failure<T, R>)_source0)._error;
      R _3_e = _2___mcc_h1;
      return Option.<T>create_None(_td_T);
    }
  }
  public T UnwrapOr(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, T default_)
  {
    Result<T, R> _source0 = this;
    if (_source0.is_Success()) {
      T _0___mcc_h0 = ((Wrappers_Compile.Result_Success<T, R>)_source0)._value;
      T _1_s = _0___mcc_h0;
      return _1_s;
    } else {
      R _2___mcc_h1 = ((Wrappers_Compile.Result_Failure<T, R>)_source0)._error;
      R _3_e = _2___mcc_h1;
      return default_;
    }
  }
  public boolean IsFailure(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R)
  {
    return (this).is_Failure();
  }
  public <__U> Result<__U, R> PropagateFailure(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, dafny.TypeDescriptor<__U> _td___U)
  {
    return Result.<__U, R>create_Failure(_td___U, _td_R, (this).dtor_error());
  }
  public <__NewR> Result<T, __NewR> MapFailure(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, dafny.TypeDescriptor<__NewR> _td___NewR, java.util.function.Function<R, __NewR> reWrap)
  {
    Result<T, R> _source0 = this;
    if (_source0.is_Success()) {
      T _0___mcc_h0 = ((Wrappers_Compile.Result_Success<T, R>)_source0)._value;
      T _1_s = _0___mcc_h0;
      return Result.<T, __NewR>create_Success(_td_T, _td___NewR, _1_s);
    } else {
      R _2___mcc_h1 = ((Wrappers_Compile.Result_Failure<T, R>)_source0)._error;
      R _3_e = _2___mcc_h1;
      return Result.<T, __NewR>create_Failure(_td_T, _td___NewR, ((__NewR)(java.lang.Object)((reWrap).apply(_3_e))));
    }
  }
  public T Extract(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R)
  {
    return (this).dtor_value();
  }
}
