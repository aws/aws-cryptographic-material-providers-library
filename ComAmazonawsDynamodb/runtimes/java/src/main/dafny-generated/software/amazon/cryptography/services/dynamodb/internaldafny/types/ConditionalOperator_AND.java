// Class ConditionalOperator_AND
// Dafny class ConditionalOperator_AND compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConditionalOperator_AND extends ConditionalOperator {
  public ConditionalOperator_AND () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConditionalOperator_AND o = (ConditionalOperator_AND)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ConditionalOperator.AND");
    return s.toString();
  }
}
