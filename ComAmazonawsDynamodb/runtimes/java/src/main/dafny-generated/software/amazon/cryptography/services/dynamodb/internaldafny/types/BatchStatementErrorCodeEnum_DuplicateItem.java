// Class BatchStatementErrorCodeEnum_DuplicateItem
// Dafny class BatchStatementErrorCodeEnum_DuplicateItem compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_DuplicateItem extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_DuplicateItem () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_DuplicateItem o = (BatchStatementErrorCodeEnum_DuplicateItem)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 10;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.DuplicateItem");
    return s.toString();
  }
}
