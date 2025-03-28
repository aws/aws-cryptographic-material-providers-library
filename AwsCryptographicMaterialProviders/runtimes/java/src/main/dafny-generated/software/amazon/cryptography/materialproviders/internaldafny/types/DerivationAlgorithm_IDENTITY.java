// Class DerivationAlgorithm_IDENTITY
// Dafny class DerivationAlgorithm_IDENTITY compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DerivationAlgorithm_IDENTITY extends DerivationAlgorithm {
  public IDENTITY _IDENTITY;
  public DerivationAlgorithm_IDENTITY (IDENTITY IDENTITY) {
    super();
    this._IDENTITY = IDENTITY;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DerivationAlgorithm_IDENTITY o = (DerivationAlgorithm_IDENTITY)other;
    return true && java.util.Objects.equals(this._IDENTITY, o._IDENTITY);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IDENTITY);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.IDENTITY");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IDENTITY));
    s.append(")");
    return s.toString();
  }
}
