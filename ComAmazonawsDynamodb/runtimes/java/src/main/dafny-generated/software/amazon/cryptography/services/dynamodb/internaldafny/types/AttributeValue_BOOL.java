// Class AttributeValue_BOOL
// Dafny class AttributeValue_BOOL compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_BOOL extends AttributeValue {
  public boolean _BOOL;
  public AttributeValue_BOOL (boolean BOOL) {
    super();
    this._BOOL = BOOL;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_BOOL o = (AttributeValue_BOOL)other;
    return true && this._BOOL == o._BOOL;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._BOOL);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.BOOL");
    s.append("(");
    s.append(this._BOOL);
    s.append(")");
    return s.toString();
  }
}
