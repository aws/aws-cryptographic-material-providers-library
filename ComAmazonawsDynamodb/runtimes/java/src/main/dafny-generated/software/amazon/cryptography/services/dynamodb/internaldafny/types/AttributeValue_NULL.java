// Class AttributeValue_NULL
// Dafny class AttributeValue_NULL compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_NULL extends AttributeValue {
  public boolean _NULL;
  public AttributeValue_NULL (boolean NULL) {
    super();
    this._NULL = NULL;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_NULL o = (AttributeValue_NULL)other;
    return true && this._NULL == o._NULL;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._NULL);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.NULL");
    s.append("(");
    s.append(this._NULL);
    s.append(")");
    return s.toString();
  }
}
