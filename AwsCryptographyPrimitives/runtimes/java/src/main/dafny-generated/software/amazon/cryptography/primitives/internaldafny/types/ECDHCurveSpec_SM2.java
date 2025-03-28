// Class ECDHCurveSpec_SM2
// Dafny class ECDHCurveSpec_SM2 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ECDHCurveSpec_SM2 extends ECDHCurveSpec {
  public ECDHCurveSpec_SM2 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECDHCurveSpec_SM2 o = (ECDHCurveSpec_SM2)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECDHCurveSpec.SM2");
    return s.toString();
  }
}
