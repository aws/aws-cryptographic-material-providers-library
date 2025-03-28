// Class ComparisonOperator_BETWEEN
// Dafny class ComparisonOperator_BETWEEN compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ComparisonOperator_BETWEEN extends ComparisonOperator {
  public ComparisonOperator_BETWEEN () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ComparisonOperator_BETWEEN o = (ComparisonOperator_BETWEEN)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ComparisonOperator.BETWEEN");
    return s.toString();
  }
}
