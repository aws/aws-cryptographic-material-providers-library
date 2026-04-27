// Class Maybe<T>
// Dafny class Maybe<T> compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Maybe<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public Maybe(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
  }
  public static <T> dafny.TypeDescriptor<Maybe<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Maybe<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Maybe<T>>referenceWithInitializer(Maybe.class, () -> Maybe.<T>Default(_td_T));
  }

  public static <T> Maybe<T> Default(dafny.TypeDescriptor<T> _td_T) {
    return Maybe.<T>create_Empty(_td_T);
  }
  @Deprecated()
  public static <T> Maybe<T> Default() {
    dafny.TypeDescriptor<T> _td_T = null;
    return Maybe.<T>create_Empty(_td_T);
  }
  public static <T> Maybe<T> create_Empty(dafny.TypeDescriptor<T> _td_T) {
    return new Maybe_Empty<T>(_td_T);
  }
  @Deprecated()
  public static <T> Maybe<T> create_Empty() {
    return new Maybe_Empty<T>(null);
  }
  public static <T> Maybe<T> create_NonEmpty(dafny.TypeDescriptor<T> _td_T, T t) {
    return new Maybe_NonEmpty<T>(_td_T, t);
  }
  @Deprecated()
  public static <T> Maybe<T> create_NonEmpty(T t) {
    return new Maybe_NonEmpty<T>(null, t);
  }
  public boolean is_Empty() { return this instanceof Maybe_Empty; }
  public boolean is_NonEmpty() { return this instanceof Maybe_NonEmpty; }
  public T dtor_t() {
    Maybe<T> d = this;
    return ((Maybe_NonEmpty<T>)d)._t;
  }
}
