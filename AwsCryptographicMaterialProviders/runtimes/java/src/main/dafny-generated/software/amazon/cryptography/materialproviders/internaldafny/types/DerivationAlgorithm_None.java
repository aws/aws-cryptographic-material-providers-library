// Class DerivationAlgorithm_None
// Dafny class DerivationAlgorithm_None compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DerivationAlgorithm_None extends DerivationAlgorithm {
  public None _None;
  public DerivationAlgorithm_None (None None) {
    super();
    this._None = None;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DerivationAlgorithm_None o = (DerivationAlgorithm_None)other;
    return true && java.util.Objects.equals(this._None, o._None);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._None);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.None");
    s.append("(");
    s.append(dafny.Helpers.toString(this._None));
    s.append(")");
    return s.toString();
  }
}
