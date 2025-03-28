// Class Error_TransactionCanceledException
// Dafny class Error_TransactionCanceledException compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class Error_TransactionCanceledException extends Error {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Message;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends CancellationReason>> _CancellationReasons;
  public Error_TransactionCanceledException (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message, Wrappers_Compile.Option<dafny.DafnySequence<? extends CancellationReason>> CancellationReasons) {
    super();
    this._Message = Message;
    this._CancellationReasons = CancellationReasons;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Error_TransactionCanceledException o = (Error_TransactionCanceledException)other;
    return true && java.util.Objects.equals(this._Message, o._Message) && java.util.Objects.equals(this._CancellationReasons, o._CancellationReasons);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 30;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CancellationReasons);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Error.TransactionCanceledException");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CancellationReasons));
    s.append(")");
    return s.toString();
  }
}
