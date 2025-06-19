// Class jfrac
// Dafny class jfrac compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jfrac {
  public JSON_mUtils_mViews_mCore_Compile.View__ _period;
  public JSON_mUtils_mViews_mCore_Compile.View__ _num;
  public jfrac (JSON_mUtils_mViews_mCore_Compile.View__ period, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    this._period = period;
    this._num = num;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jfrac o = (jfrac)other;
    return true && java.util.Objects.equals(this._period, o._period) && java.util.Objects.equals(this._num, o._num);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._period);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._num);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jfrac.JFrac");
    s.append("(");
    s.append(dafny.Helpers.toString(this._period));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._num));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jfrac> _TYPE = dafny.TypeDescriptor.<jfrac>referenceWithInitializer(jfrac.class, () -> jfrac.Default());
  public static dafny.TypeDescriptor<jfrac> _typeDescriptor() {
    return (dafny.TypeDescriptor<jfrac>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jfrac theDefault = jfrac.create(jperiod.defaultValue(), jnum.defaultValue());
  public static jfrac Default() {
    return theDefault;
  }
  public static jfrac create(JSON_mUtils_mViews_mCore_Compile.View__ period, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    return new jfrac(period, num);
  }
  public static jfrac create_JFrac(JSON_mUtils_mViews_mCore_Compile.View__ period, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    return create(period, num);
  }
  public boolean is_JFrac() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_period() {
    return this._period;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_num() {
    return this._num;
  }
}
