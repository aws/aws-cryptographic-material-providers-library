// Class DerivationAlgorithm_HKDF
// Dafny class DerivationAlgorithm_HKDF compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DerivationAlgorithm_HKDF extends DerivationAlgorithm {
  public HKDF _HKDF;
  public DerivationAlgorithm_HKDF (HKDF HKDF) {
    super();
    this._HKDF = HKDF;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DerivationAlgorithm_HKDF o = (DerivationAlgorithm_HKDF)other;
    return true && java.util.Objects.equals(this._HKDF, o._HKDF);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._HKDF);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.HKDF");
    s.append("(");
    s.append(dafny.Helpers.toString(this._HKDF));
    s.append(")");
    return s.toString();
  }
}
