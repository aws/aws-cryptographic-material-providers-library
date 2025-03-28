// Class ECDSASignatureAlgorithm_ECDSA__P384
// Dafny class ECDSASignatureAlgorithm_ECDSA__P384 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ECDSASignatureAlgorithm_ECDSA__P384 extends ECDSASignatureAlgorithm {
  public ECDSASignatureAlgorithm_ECDSA__P384 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECDSASignatureAlgorithm_ECDSA__P384 o = (ECDSASignatureAlgorithm_ECDSA__P384)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm.ECDSA_P384");
    return s.toString();
  }
}
