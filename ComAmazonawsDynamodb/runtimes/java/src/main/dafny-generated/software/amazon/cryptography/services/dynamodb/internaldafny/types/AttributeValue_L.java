// Class AttributeValue_L
// Dafny class AttributeValue_L compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_L extends AttributeValue {
  public dafny.DafnySequence<? extends AttributeValue> _L;
  public AttributeValue_L (dafny.DafnySequence<? extends AttributeValue> L) {
    super();
    this._L = L;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_L o = (AttributeValue_L)other;
    return true && java.util.Objects.equals(this._L, o._L);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._L);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.L");
    s.append("(");
    s.append(dafny.Helpers.toString(this._L));
    s.append(")");
    return s.toString();
  }
}
