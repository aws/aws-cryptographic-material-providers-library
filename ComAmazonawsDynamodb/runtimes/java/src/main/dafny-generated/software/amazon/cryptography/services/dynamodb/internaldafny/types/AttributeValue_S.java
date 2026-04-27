// Class AttributeValue_S
// Dafny class AttributeValue_S compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_S extends AttributeValue {
  public dafny.DafnySequence<? extends Character> _S;
  public AttributeValue_S (dafny.DafnySequence<? extends Character> S) {
    super();
    this._S = S;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_S o = (AttributeValue_S)other;
    return true && java.util.Objects.equals(this._S, o._S);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.S");
    s.append("(");
    s.append(dafny.Helpers.toString(this._S));
    s.append(")");
    return s.toString();
  }
}
