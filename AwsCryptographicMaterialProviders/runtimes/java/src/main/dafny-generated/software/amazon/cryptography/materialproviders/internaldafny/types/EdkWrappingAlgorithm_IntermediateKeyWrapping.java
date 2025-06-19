// Class EdkWrappingAlgorithm_IntermediateKeyWrapping
// Dafny class EdkWrappingAlgorithm_IntermediateKeyWrapping compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EdkWrappingAlgorithm_IntermediateKeyWrapping extends EdkWrappingAlgorithm {
  public IntermediateKeyWrapping _IntermediateKeyWrapping;
  public EdkWrappingAlgorithm_IntermediateKeyWrapping (IntermediateKeyWrapping IntermediateKeyWrapping) {
    super();
    this._IntermediateKeyWrapping = IntermediateKeyWrapping;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EdkWrappingAlgorithm_IntermediateKeyWrapping o = (EdkWrappingAlgorithm_IntermediateKeyWrapping)other;
    return true && java.util.Objects.equals(this._IntermediateKeyWrapping, o._IntermediateKeyWrapping);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IntermediateKeyWrapping);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm.IntermediateKeyWrapping");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IntermediateKeyWrapping));
    s.append(")");
    return s.toString();
  }
}
