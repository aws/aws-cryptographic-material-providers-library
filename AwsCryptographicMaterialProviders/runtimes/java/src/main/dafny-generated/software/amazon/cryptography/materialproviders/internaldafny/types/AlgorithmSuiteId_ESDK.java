// Class AlgorithmSuiteId_ESDK
// Dafny class AlgorithmSuiteId_ESDK compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AlgorithmSuiteId_ESDK extends AlgorithmSuiteId {
  public ESDKAlgorithmSuiteId _ESDK;
  public AlgorithmSuiteId_ESDK (ESDKAlgorithmSuiteId ESDK) {
    super();
    this._ESDK = ESDK;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AlgorithmSuiteId_ESDK o = (AlgorithmSuiteId_ESDK)other;
    return true && java.util.Objects.equals(this._ESDK, o._ESDK);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ESDK);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId.ESDK");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ESDK));
    s.append(")");
    return s.toString();
  }
}
