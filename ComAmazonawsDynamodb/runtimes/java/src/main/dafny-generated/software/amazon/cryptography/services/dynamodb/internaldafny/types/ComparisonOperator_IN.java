// Class ComparisonOperator_IN
// Dafny class ComparisonOperator_IN compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ComparisonOperator_IN extends ComparisonOperator {
  public ComparisonOperator_IN () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ComparisonOperator_IN o = (ComparisonOperator_IN)other;
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
    s.append("ComAmazonawsDynamodbTypes.ComparisonOperator.IN");
    return s.toString();
  }
}
