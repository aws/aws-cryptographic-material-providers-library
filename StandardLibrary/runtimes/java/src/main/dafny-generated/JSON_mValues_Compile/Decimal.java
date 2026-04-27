// Class Decimal
// Dafny class Decimal compiled into Java
package JSON_mValues_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Decimal {
  public java.math.BigInteger _n;
  public java.math.BigInteger _e10;
  public Decimal (java.math.BigInteger n, java.math.BigInteger e10) {
    this._n = n;
    this._e10 = e10;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Decimal o = (Decimal)other;
    return true && java.util.Objects.equals(this._n, o._n) && java.util.Objects.equals(this._e10, o._e10);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._n);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._e10);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Values.Decimal.Decimal");
    s.append("(");
    s.append(dafny.Helpers.toString(this._n));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._e10));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Decimal> _TYPE = dafny.TypeDescriptor.<Decimal>referenceWithInitializer(Decimal.class, () -> Decimal.Default());
  public static dafny.TypeDescriptor<Decimal> _typeDescriptor() {
    return (dafny.TypeDescriptor<Decimal>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Decimal theDefault = Decimal.create(java.math.BigInteger.ZERO, java.math.BigInteger.ZERO);
  public static Decimal Default() {
    return theDefault;
  }
  public static Decimal create(java.math.BigInteger n, java.math.BigInteger e10) {
    return new Decimal(n, e10);
  }
  public static Decimal create_Decimal(java.math.BigInteger n, java.math.BigInteger e10) {
    return create(n, e10);
  }
  public boolean is_Decimal() { return true; }
  public java.math.BigInteger dtor_n() {
    return this._n;
  }
  public java.math.BigInteger dtor_e10() {
    return this._e10;
  }
}
