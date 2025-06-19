// Class ComparisonOperator_NOT__CONTAINS
// Dafny class ComparisonOperator_NOT__CONTAINS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ComparisonOperator_NOT__CONTAINS extends ComparisonOperator {
  public ComparisonOperator_NOT__CONTAINS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ComparisonOperator_NOT__CONTAINS o = (ComparisonOperator_NOT__CONTAINS)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 11;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ComparisonOperator.NOT_CONTAINS");
    return s.toString();
  }
}
