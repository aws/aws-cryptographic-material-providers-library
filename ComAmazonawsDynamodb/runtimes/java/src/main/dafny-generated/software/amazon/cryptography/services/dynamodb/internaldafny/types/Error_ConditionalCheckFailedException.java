// Class Error_ConditionalCheckFailedException
// Dafny class Error_ConditionalCheckFailedException compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Error_ConditionalCheckFailedException extends Error {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _message;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Item;
  public Error_ConditionalCheckFailedException (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    super();
    this._message = message;
    this._Item = Item;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Error_ConditionalCheckFailedException o = (Error_ConditionalCheckFailedException)other;
    return true && java.util.Objects.equals(this._message, o._message) && java.util.Objects.equals(this._Item, o._Item);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Item);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Error.ConditionalCheckFailedException");
    s.append("(");
    s.append(dafny.Helpers.toString(this._message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Item));
    s.append(")");
    return s.toString();
  }
}
