// Class AttributeValue_M
// Dafny class AttributeValue_M compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_M extends AttributeValue {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> _M;
  public AttributeValue_M (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> M) {
    super();
    this._M = M;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_M o = (AttributeValue_M)other;
    return true && java.util.Objects.equals(this._M, o._M);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._M);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.M");
    s.append("(");
    s.append(dafny.Helpers.toString(this._M));
    s.append(")");
    return s.toString();
  }
}
