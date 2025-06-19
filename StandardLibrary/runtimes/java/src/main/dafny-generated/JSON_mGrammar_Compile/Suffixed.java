// Class Suffixed<T, S>
// Dafny class Suffixed<T, S> compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Suffixed<T, S> {
  public T _t;
  public Maybe<Structural<S>> _suffix;
  protected dafny.TypeDescriptor<T> _td_T;
  protected dafny.TypeDescriptor<S> _td_S;
  public Suffixed (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<S> _td_S, T t, Maybe<Structural<S>> suffix) {
    this._td_T = _td_T;
    this._td_S = _td_S;
    this._t = t;
    this._suffix = suffix;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Suffixed<T, S> o = (Suffixed<T, S>)other;
    return true && java.util.Objects.equals(this._t, o._t) && java.util.Objects.equals(this._suffix, o._suffix);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._t);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._suffix);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Suffixed.Suffixed");
    s.append("(");
    s.append(dafny.Helpers.toString(this._t));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._suffix));
    s.append(")");
    return s.toString();
  }
  public static <T, S> dafny.TypeDescriptor<Suffixed<T, S>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<S> _td_S) {
    return (dafny.TypeDescriptor<Suffixed<T, S>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Suffixed<T, S>>referenceWithInitializer(Suffixed.class, () -> Suffixed.<T, S>Default(_td_T, _td_S, _td_T.defaultValue()));
  }

  public static <T, S> Suffixed<T, S> Default(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<S> _td_S, T _default_T) {
    return Suffixed.<T, S>create(_td_T, _td_S, _default_T, Maybe.<Structural<S>>Default(Structural.<S>_typeDescriptor(_td_S)));
  }
  @Deprecated()
  public static <T, S> Suffixed<T, S> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    dafny.TypeDescriptor<S> _td_S = null;
    return Suffixed.<T, S>create(_td_T, _td_S, _default_T, Maybe.<Structural<S>>Default(Structural.<S>_typeDescriptor(_td_S)));
  }
  public static <T, S> Suffixed<T, S> create(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<S> _td_S, T t, Maybe<Structural<S>> suffix) {
    return new Suffixed<T, S>(_td_T, _td_S, t, suffix);
  }
  @Deprecated()
  public static <T, S> Suffixed<T, S> create(T t, Maybe<Structural<S>> suffix) {
    return new Suffixed<T, S>(null, null, t, suffix);
  }
  public static <T, S> Suffixed<T, S> create_Suffixed(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<S> _td_S, T t, Maybe<Structural<S>> suffix) {
    return create(_td_T, _td_S, t, suffix);
  }
  @Deprecated()
  public static <T, S> Suffixed<T, S> create_Suffixed(T t, Maybe<Structural<S>> suffix) {
    return create(null, null, t, suffix);
  }
  public boolean is_Suffixed() { return true; }
  public T dtor_t() {
    return this._t;
  }
  public Maybe<Structural<S>> dtor_suffix() {
    return this._suffix;
  }
}
