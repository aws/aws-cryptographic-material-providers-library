// Class ReturnValuesOnConditionCheckFailure_ALL__OLD
// Dafny class ReturnValuesOnConditionCheckFailure_ALL__OLD compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnValuesOnConditionCheckFailure_ALL__OLD extends ReturnValuesOnConditionCheckFailure {
  public ReturnValuesOnConditionCheckFailure_ALL__OLD () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnValuesOnConditionCheckFailure_ALL__OLD o = (ReturnValuesOnConditionCheckFailure_ALL__OLD)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnValuesOnConditionCheckFailure.ALL_OLD");
    return s.toString();
  }
}
