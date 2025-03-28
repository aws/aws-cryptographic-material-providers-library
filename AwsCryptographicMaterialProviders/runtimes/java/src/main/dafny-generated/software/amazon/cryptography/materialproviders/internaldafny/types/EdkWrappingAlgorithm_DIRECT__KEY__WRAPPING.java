// Class EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING
// Dafny class EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING extends EdkWrappingAlgorithm {
  public DIRECT__KEY__WRAPPING _DIRECT__KEY__WRAPPING;
  public EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING (DIRECT__KEY__WRAPPING DIRECT__KEY__WRAPPING) {
    super();
    this._DIRECT__KEY__WRAPPING = DIRECT__KEY__WRAPPING;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING o = (EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING)other;
    return true && java.util.Objects.equals(this._DIRECT__KEY__WRAPPING, o._DIRECT__KEY__WRAPPING);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DIRECT__KEY__WRAPPING);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm.DIRECT_KEY_WRAPPING");
    s.append("(");
    s.append(dafny.Helpers.toString(this._DIRECT__KEY__WRAPPING));
    s.append(")");
    return s.toString();
  }
}
