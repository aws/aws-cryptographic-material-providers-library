// Class ReturnValuesOnConditionCheckFailure_NONE
// Dafny class ReturnValuesOnConditionCheckFailure_NONE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnValuesOnConditionCheckFailure_NONE extends ReturnValuesOnConditionCheckFailure {
  public ReturnValuesOnConditionCheckFailure_NONE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnValuesOnConditionCheckFailure_NONE o = (ReturnValuesOnConditionCheckFailure_NONE)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnValuesOnConditionCheckFailure.NONE");
    return s.toString();
  }
}
