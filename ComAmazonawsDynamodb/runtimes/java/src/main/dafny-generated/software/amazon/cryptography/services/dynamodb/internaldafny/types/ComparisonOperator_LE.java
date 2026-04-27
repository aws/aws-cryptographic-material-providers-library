// Class ComparisonOperator_LE
// Dafny class ComparisonOperator_LE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ComparisonOperator_LE extends ComparisonOperator {
  public ComparisonOperator_LE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ComparisonOperator_LE o = (ComparisonOperator_LE)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ComparisonOperator.LE");
    return s.toString();
  }
}
