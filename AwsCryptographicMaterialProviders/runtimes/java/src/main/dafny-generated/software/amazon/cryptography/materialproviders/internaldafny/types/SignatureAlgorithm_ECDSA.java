// Class SignatureAlgorithm_ECDSA
// Dafny class SignatureAlgorithm_ECDSA compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class SignatureAlgorithm_ECDSA extends SignatureAlgorithm {
  public ECDSA _ECDSA;
  public SignatureAlgorithm_ECDSA (ECDSA ECDSA) {
    super();
    this._ECDSA = ECDSA;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SignatureAlgorithm_ECDSA o = (SignatureAlgorithm_ECDSA)other;
    return true && java.util.Objects.equals(this._ECDSA, o._ECDSA);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ECDSA);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm.ECDSA");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ECDSA));
    s.append(")");
    return s.toString();
  }
}
