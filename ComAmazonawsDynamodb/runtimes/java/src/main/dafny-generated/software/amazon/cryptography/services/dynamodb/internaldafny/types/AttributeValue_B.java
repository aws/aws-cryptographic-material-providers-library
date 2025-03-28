// Class AttributeValue_B
// Dafny class AttributeValue_B compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_B extends AttributeValue {
  public dafny.DafnySequence<? extends java.lang.Byte> _B;
  public AttributeValue_B (dafny.DafnySequence<? extends java.lang.Byte> B) {
    super();
    this._B = B;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_B o = (AttributeValue_B)other;
    return true && java.util.Objects.equals(this._B, o._B);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._B);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.B");
    s.append("(");
    s.append(dafny.Helpers.toString(this._B));
    s.append(")");
    return s.toString();
  }
}
