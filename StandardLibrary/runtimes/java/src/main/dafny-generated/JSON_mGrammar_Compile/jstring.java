// Class jstring
// Dafny class jstring compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jstring {
  public JSON_mUtils_mViews_mCore_Compile.View__ _lq;
  public JSON_mUtils_mViews_mCore_Compile.View__ _contents;
  public JSON_mUtils_mViews_mCore_Compile.View__ _rq;
  public jstring (JSON_mUtils_mViews_mCore_Compile.View__ lq, JSON_mUtils_mViews_mCore_Compile.View__ contents, JSON_mUtils_mViews_mCore_Compile.View__ rq) {
    this._lq = lq;
    this._contents = contents;
    this._rq = rq;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jstring o = (jstring)other;
    return true && java.util.Objects.equals(this._lq, o._lq) && java.util.Objects.equals(this._contents, o._contents) && java.util.Objects.equals(this._rq, o._rq);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._lq);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._contents);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._rq);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jstring.JString");
    s.append("(");
    s.append(dafny.Helpers.toString(this._lq));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._contents));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._rq));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jstring> _TYPE = dafny.TypeDescriptor.<jstring>referenceWithInitializer(jstring.class, () -> jstring.Default());
  public static dafny.TypeDescriptor<jstring> _typeDescriptor() {
    return (dafny.TypeDescriptor<jstring>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jstring theDefault = jstring.create(jquote.defaultValue(), jstr.defaultValue(), jquote.defaultValue());
  public static jstring Default() {
    return theDefault;
  }
  public static jstring create(JSON_mUtils_mViews_mCore_Compile.View__ lq, JSON_mUtils_mViews_mCore_Compile.View__ contents, JSON_mUtils_mViews_mCore_Compile.View__ rq) {
    return new jstring(lq, contents, rq);
  }
  public static jstring create_JString(JSON_mUtils_mViews_mCore_Compile.View__ lq, JSON_mUtils_mViews_mCore_Compile.View__ contents, JSON_mUtils_mViews_mCore_Compile.View__ rq) {
    return create(lq, contents, rq);
  }
  public boolean is_JString() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_lq() {
    return this._lq;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_contents() {
    return this._contents;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_rq() {
    return this._rq;
  }
}
