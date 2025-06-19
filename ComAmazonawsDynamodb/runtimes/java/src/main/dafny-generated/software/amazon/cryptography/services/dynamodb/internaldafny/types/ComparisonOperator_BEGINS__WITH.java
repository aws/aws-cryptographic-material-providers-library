// Class ComparisonOperator_BEGINS__WITH
// Dafny class ComparisonOperator_BEGINS__WITH compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ComparisonOperator_BEGINS__WITH extends ComparisonOperator {
  public ComparisonOperator_BEGINS__WITH () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ComparisonOperator_BEGINS__WITH o = (ComparisonOperator_BEGINS__WITH)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 12;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ComparisonOperator.BEGINS_WITH");
    return s.toString();
  }
}
