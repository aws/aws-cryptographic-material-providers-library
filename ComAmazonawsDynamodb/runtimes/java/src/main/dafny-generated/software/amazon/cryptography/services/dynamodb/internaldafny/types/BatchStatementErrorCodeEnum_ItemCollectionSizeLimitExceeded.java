// Class BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded
// Dafny class BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded o = (BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded)other;
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
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ItemCollectionSizeLimitExceeded");
    return s.toString();
  }
}
