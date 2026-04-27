// Class Error_InvalidAlgorithmSuiteInfoOnEncrypt
// Dafny class Error_InvalidAlgorithmSuiteInfoOnEncrypt compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Error_InvalidAlgorithmSuiteInfoOnEncrypt extends Error {
  public dafny.DafnySequence<? extends Character> _message;
  public Error_InvalidAlgorithmSuiteInfoOnEncrypt (dafny.DafnySequence<? extends Character> message) {
    super();
    this._message = message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Error_InvalidAlgorithmSuiteInfoOnEncrypt o = (Error_InvalidAlgorithmSuiteInfoOnEncrypt)other;
    return true && java.util.Objects.equals(this._message, o._message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.Error.InvalidAlgorithmSuiteInfoOnEncrypt");
    s.append("(");
    s.append(dafny.Helpers.toString(this._message));
    s.append(")");
    return s.toString();
  }
}
