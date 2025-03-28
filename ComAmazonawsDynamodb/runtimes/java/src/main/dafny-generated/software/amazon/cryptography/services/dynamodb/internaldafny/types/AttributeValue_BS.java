// Class AttributeValue_BS
// Dafny class AttributeValue_BS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_BS extends AttributeValue {
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _BS;
  public AttributeValue_BS (dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> BS) {
    super();
    this._BS = BS;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_BS o = (AttributeValue_BS)other;
    return true && java.util.Objects.equals(this._BS, o._BS);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BS);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.BS");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BS));
    s.append(")");
    return s.toString();
  }
}
