// Class AttributeValue_N
// Dafny class AttributeValue_N compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_N extends AttributeValue {
  public dafny.DafnySequence<? extends Character> _N;
  public AttributeValue_N (dafny.DafnySequence<? extends Character> N) {
    super();
    this._N = N;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_N o = (AttributeValue_N)other;
    return true && java.util.Objects.equals(this._N, o._N);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._N);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.N");
    s.append("(");
    s.append(dafny.Helpers.toString(this._N));
    s.append(")");
    return s.toString();
  }
}
