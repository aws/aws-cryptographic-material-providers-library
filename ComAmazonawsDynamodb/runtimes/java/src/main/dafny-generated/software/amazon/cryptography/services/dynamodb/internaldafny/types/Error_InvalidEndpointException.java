// Class Error_InvalidEndpointException
// Dafny class Error_InvalidEndpointException compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class Error_InvalidEndpointException extends Error {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Message;
  public Error_InvalidEndpointException (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message) {
    super();
    this._Message = Message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Error_InvalidEndpointException o = (Error_InvalidEndpointException)other;
    return true && java.util.Objects.equals(this._Message, o._Message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 14;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Error.InvalidEndpointException");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(")");
    return s.toString();
  }
}
