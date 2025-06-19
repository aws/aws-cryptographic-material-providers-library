// Class jexp
// Dafny class jexp compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jexp {
  public JSON_mUtils_mViews_mCore_Compile.View__ _e;
  public JSON_mUtils_mViews_mCore_Compile.View__ _sign;
  public JSON_mUtils_mViews_mCore_Compile.View__ _num;
  public jexp (JSON_mUtils_mViews_mCore_Compile.View__ e, JSON_mUtils_mViews_mCore_Compile.View__ sign, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    this._e = e;
    this._sign = sign;
    this._num = num;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jexp o = (jexp)other;
    return true && java.util.Objects.equals(this._e, o._e) && java.util.Objects.equals(this._sign, o._sign) && java.util.Objects.equals(this._num, o._num);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._e);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._sign);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._num);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jexp.JExp");
    s.append("(");
    s.append(dafny.Helpers.toString(this._e));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._sign));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._num));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jexp> _TYPE = dafny.TypeDescriptor.<jexp>referenceWithInitializer(jexp.class, () -> jexp.Default());
  public static dafny.TypeDescriptor<jexp> _typeDescriptor() {
    return (dafny.TypeDescriptor<jexp>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jexp theDefault = jexp.create(je.defaultValue(), jsign.defaultValue(), jnum.defaultValue());
  public static jexp Default() {
    return theDefault;
  }
  public static jexp create(JSON_mUtils_mViews_mCore_Compile.View__ e, JSON_mUtils_mViews_mCore_Compile.View__ sign, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    return new jexp(e, sign, num);
  }
  public static jexp create_JExp(JSON_mUtils_mViews_mCore_Compile.View__ e, JSON_mUtils_mViews_mCore_Compile.View__ sign, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    return create(e, sign, num);
  }
  public boolean is_JExp() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_e() {
    return this._e;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_sign() {
    return this._sign;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_num() {
    return this._num;
  }
}
