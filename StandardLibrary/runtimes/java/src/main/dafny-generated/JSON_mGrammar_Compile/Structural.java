// Class Structural<T>
// Dafny class Structural<T> compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Structural<T> {
  public JSON_mUtils_mViews_mCore_Compile.View__ _before;
  public T _t;
  public JSON_mUtils_mViews_mCore_Compile.View__ _after;
  protected dafny.TypeDescriptor<T> _td_T;
  public Structural (dafny.TypeDescriptor<T> _td_T, JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    this._td_T = _td_T;
    this._before = before;
    this._t = t;
    this._after = after;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Structural<T> o = (Structural<T>)other;
    return true && java.util.Objects.equals(this._before, o._before) && java.util.Objects.equals(this._t, o._t) && java.util.Objects.equals(this._after, o._after);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._before);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._t);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._after);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Structural.Structural");
    s.append("(");
    s.append(dafny.Helpers.toString(this._before));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._t));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._after));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<Structural<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Structural<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Structural<T>>referenceWithInitializer(Structural.class, () -> Structural.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> Structural<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return Structural.<T>create(_td_T, jblanks.defaultValue(), _default_T, jblanks.defaultValue());
  }
  @Deprecated()
  public static <T> Structural<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return Structural.<T>create(_td_T, jblanks.defaultValue(), _default_T, jblanks.defaultValue());
  }
  public static <T> Structural<T> create(dafny.TypeDescriptor<T> _td_T, JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return new Structural<T>(_td_T, before, t, after);
  }
  @Deprecated()
  public static <T> Structural<T> create(JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return new Structural<T>(null, before, t, after);
  }
  public static <T> Structural<T> create_Structural(dafny.TypeDescriptor<T> _td_T, JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return create(_td_T, before, t, after);
  }
  @Deprecated()
  public static <T> Structural<T> create_Structural(JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return create(null, before, t, after);
  }
  public boolean is_Structural() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_before() {
    return this._before;
  }
  public T dtor_t() {
    return this._t;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_after() {
    return this._after;
  }
}
