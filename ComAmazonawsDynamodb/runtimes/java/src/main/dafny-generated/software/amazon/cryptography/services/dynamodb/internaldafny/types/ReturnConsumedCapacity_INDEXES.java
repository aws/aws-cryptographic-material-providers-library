// Class ReturnConsumedCapacity_INDEXES
// Dafny class ReturnConsumedCapacity_INDEXES compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnConsumedCapacity_INDEXES extends ReturnConsumedCapacity {
  public ReturnConsumedCapacity_INDEXES () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnConsumedCapacity_INDEXES o = (ReturnConsumedCapacity_INDEXES)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnConsumedCapacity.INDEXES");
    return s.toString();
  }
}
