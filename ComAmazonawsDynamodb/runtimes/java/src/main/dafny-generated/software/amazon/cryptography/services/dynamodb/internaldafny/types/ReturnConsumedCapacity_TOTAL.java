// Class ReturnConsumedCapacity_TOTAL
// Dafny class ReturnConsumedCapacity_TOTAL compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnConsumedCapacity_TOTAL extends ReturnConsumedCapacity {
  public ReturnConsumedCapacity_TOTAL () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnConsumedCapacity_TOTAL o = (ReturnConsumedCapacity_TOTAL)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnConsumedCapacity.TOTAL");
    return s.toString();
  }
}
