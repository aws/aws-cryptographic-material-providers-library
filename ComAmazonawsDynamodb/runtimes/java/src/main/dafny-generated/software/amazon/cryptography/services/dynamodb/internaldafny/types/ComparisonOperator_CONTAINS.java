// Class ComparisonOperator_CONTAINS
// Dafny class ComparisonOperator_CONTAINS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ComparisonOperator_CONTAINS extends ComparisonOperator {
  public ComparisonOperator_CONTAINS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ComparisonOperator_CONTAINS o = (ComparisonOperator_CONTAINS)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 10;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ComparisonOperator.CONTAINS");
    return s.toString();
  }
}
