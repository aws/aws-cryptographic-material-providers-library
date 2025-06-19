// Class ComparisonOperator_NULL
// Dafny class ComparisonOperator_NULL compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ComparisonOperator_NULL extends ComparisonOperator {
  public ComparisonOperator_NULL () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ComparisonOperator_NULL o = (ComparisonOperator_NULL)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ComparisonOperator.NULL");
    return s.toString();
  }
}
