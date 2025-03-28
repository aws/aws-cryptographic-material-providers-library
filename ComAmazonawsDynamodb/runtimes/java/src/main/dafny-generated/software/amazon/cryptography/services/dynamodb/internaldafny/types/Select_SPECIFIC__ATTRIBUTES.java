// Class Select_SPECIFIC__ATTRIBUTES
// Dafny class Select_SPECIFIC__ATTRIBUTES compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class Select_SPECIFIC__ATTRIBUTES extends Select {
  public Select_SPECIFIC__ATTRIBUTES () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Select_SPECIFIC__ATTRIBUTES o = (Select_SPECIFIC__ATTRIBUTES)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Select.SPECIFIC_ATTRIBUTES");
    return s.toString();
  }
}
