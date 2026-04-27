// Class Error_CloudHsmClusterInUseException
// Dafny class Error_CloudHsmClusterInUseException compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Error_CloudHsmClusterInUseException extends Error {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _message;
  public Error_CloudHsmClusterInUseException (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    super();
    this._message = message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Error_CloudHsmClusterInUseException o = (Error_CloudHsmClusterInUseException)other;
    return true && java.util.Objects.equals(this._message, o._message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.Error.CloudHsmClusterInUseException");
    s.append("(");
    s.append(dafny.Helpers.toString(this._message));
    s.append(")");
    return s.toString();
  }
}
