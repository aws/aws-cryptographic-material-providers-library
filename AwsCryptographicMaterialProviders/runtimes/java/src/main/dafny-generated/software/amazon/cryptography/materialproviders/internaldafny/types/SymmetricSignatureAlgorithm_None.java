// Class SymmetricSignatureAlgorithm_None
// Dafny class SymmetricSignatureAlgorithm_None compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class SymmetricSignatureAlgorithm_None extends SymmetricSignatureAlgorithm {
  public None _None;
  public SymmetricSignatureAlgorithm_None (None None) {
    super();
    this._None = None;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SymmetricSignatureAlgorithm_None o = (SymmetricSignatureAlgorithm_None)other;
    return true && java.util.Objects.equals(this._None, o._None);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._None);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm.None");
    s.append("(");
    s.append(dafny.Helpers.toString(this._None));
    s.append(")");
    return s.toString();
  }
}
