// Class jKeyValue
// Dafny class jKeyValue compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jKeyValue {
  public jstring _k;
  public Structural<JSON_mUtils_mViews_mCore_Compile.View__> _colon;
  public Value _v;
  public jKeyValue (jstring k, Structural<JSON_mUtils_mViews_mCore_Compile.View__> colon, Value v) {
    this._k = k;
    this._colon = colon;
    this._v = v;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jKeyValue o = (jKeyValue)other;
    return true && java.util.Objects.equals(this._k, o._k) && java.util.Objects.equals(this._colon, o._colon) && java.util.Objects.equals(this._v, o._v);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._k);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._colon);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._v);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jKeyValue.KeyValue");
    s.append("(");
    s.append(dafny.Helpers.toString(this._k));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._colon));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._v));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jKeyValue> _TYPE = dafny.TypeDescriptor.<jKeyValue>referenceWithInitializer(jKeyValue.class, () -> jKeyValue.Default());
  public static dafny.TypeDescriptor<jKeyValue> _typeDescriptor() {
    return (dafny.TypeDescriptor<jKeyValue>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jKeyValue theDefault = jKeyValue.create(jstring.Default(), Structural.<JSON_mUtils_mViews_mCore_Compile.View__>Default(jcolon._typeDescriptor(), jcolon.defaultValue()), Value.Default());
  public static jKeyValue Default() {
    return theDefault;
  }
  public static jKeyValue create(jstring k, Structural<JSON_mUtils_mViews_mCore_Compile.View__> colon, Value v) {
    return new jKeyValue(k, colon, v);
  }
  public static jKeyValue create_KeyValue(jstring k, Structural<JSON_mUtils_mViews_mCore_Compile.View__> colon, Value v) {
    return create(k, colon, v);
  }
  public boolean is_KeyValue() { return true; }
  public jstring dtor_k() {
    return this._k;
  }
  public Structural<JSON_mUtils_mViews_mCore_Compile.View__> dtor_colon() {
    return this._colon;
  }
  public Value dtor_v() {
    return this._v;
  }
}
