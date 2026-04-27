// Class jnumber
// Dafny class jnumber compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jnumber {
  public JSON_mUtils_mViews_mCore_Compile.View__ _minus;
  public JSON_mUtils_mViews_mCore_Compile.View__ _num;
  public Maybe<jfrac> _frac;
  public Maybe<jexp> _exp;
  public jnumber (JSON_mUtils_mViews_mCore_Compile.View__ minus, JSON_mUtils_mViews_mCore_Compile.View__ num, Maybe<jfrac> frac, Maybe<jexp> exp) {
    this._minus = minus;
    this._num = num;
    this._frac = frac;
    this._exp = exp;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jnumber o = (jnumber)other;
    return true && java.util.Objects.equals(this._minus, o._minus) && java.util.Objects.equals(this._num, o._num) && java.util.Objects.equals(this._frac, o._frac) && java.util.Objects.equals(this._exp, o._exp);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._minus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._num);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._frac);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._exp);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jnumber.JNumber");
    s.append("(");
    s.append(dafny.Helpers.toString(this._minus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._num));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._frac));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._exp));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jnumber> _TYPE = dafny.TypeDescriptor.<jnumber>referenceWithInitializer(jnumber.class, () -> jnumber.Default());
  public static dafny.TypeDescriptor<jnumber> _typeDescriptor() {
    return (dafny.TypeDescriptor<jnumber>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jnumber theDefault = jnumber.create(jminus.defaultValue(), jnum.defaultValue(), Maybe.<jfrac>Default(jfrac._typeDescriptor()), Maybe.<jexp>Default(jexp._typeDescriptor()));
  public static jnumber Default() {
    return theDefault;
  }
  public static jnumber create(JSON_mUtils_mViews_mCore_Compile.View__ minus, JSON_mUtils_mViews_mCore_Compile.View__ num, Maybe<jfrac> frac, Maybe<jexp> exp) {
    return new jnumber(minus, num, frac, exp);
  }
  public static jnumber create_JNumber(JSON_mUtils_mViews_mCore_Compile.View__ minus, JSON_mUtils_mViews_mCore_Compile.View__ num, Maybe<jfrac> frac, Maybe<jexp> exp) {
    return create(minus, num, frac, exp);
  }
  public boolean is_JNumber() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_minus() {
    return this._minus;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_num() {
    return this._num;
  }
  public Maybe<jfrac> dtor_frac() {
    return this._frac;
  }
  public Maybe<jexp> dtor_exp() {
    return this._exp;
  }
}
