// Class ECDSASignatureAlgorithm_ECDSA__P256
// Dafny class ECDSASignatureAlgorithm_ECDSA__P256 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ECDSASignatureAlgorithm_ECDSA__P256 extends ECDSASignatureAlgorithm {
  public ECDSASignatureAlgorithm_ECDSA__P256 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECDSASignatureAlgorithm_ECDSA__P256 o = (ECDSASignatureAlgorithm_ECDSA__P256)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm.ECDSA_P256");
    return s.toString();
  }
}
