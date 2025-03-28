// Class AttributeValue_SS
// Dafny class AttributeValue_SS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_SS extends AttributeValue {
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _SS;
  public AttributeValue_SS (dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> SS) {
    super();
    this._SS = SS;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_SS o = (AttributeValue_SS)other;
    return true && java.util.Objects.equals(this._SS, o._SS);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SS);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.SS");
    s.append("(");
    s.append(dafny.Helpers.toString(this._SS));
    s.append(")");
    return s.toString();
  }
}
