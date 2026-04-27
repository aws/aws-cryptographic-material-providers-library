// Class ReturnConsumedCapacity_NONE
// Dafny class ReturnConsumedCapacity_NONE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnConsumedCapacity_NONE extends ReturnConsumedCapacity {
  public ReturnConsumedCapacity_NONE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnConsumedCapacity_NONE o = (ReturnConsumedCapacity_NONE)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnConsumedCapacity.NONE");
    return s.toString();
  }
}
