// Class ConditionalOperator_OR
// Dafny class ConditionalOperator_OR compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConditionalOperator_OR extends ConditionalOperator {
  public ConditionalOperator_OR () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConditionalOperator_OR o = (ConditionalOperator_OR)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ConditionalOperator.OR");
    return s.toString();
  }
}
