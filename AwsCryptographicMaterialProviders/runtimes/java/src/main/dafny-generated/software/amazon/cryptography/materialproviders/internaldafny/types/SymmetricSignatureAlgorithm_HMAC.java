// Class SymmetricSignatureAlgorithm_HMAC
// Dafny class SymmetricSignatureAlgorithm_HMAC compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class SymmetricSignatureAlgorithm_HMAC extends SymmetricSignatureAlgorithm {
  public software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _HMAC;
  public SymmetricSignatureAlgorithm_HMAC (software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm HMAC) {
    super();
    this._HMAC = HMAC;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SymmetricSignatureAlgorithm_HMAC o = (SymmetricSignatureAlgorithm_HMAC)other;
    return true && java.util.Objects.equals(this._HMAC, o._HMAC);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._HMAC);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm.HMAC");
    s.append("(");
    s.append(dafny.Helpers.toString(this._HMAC));
    s.append(")");
    return s.toString();
  }
}
