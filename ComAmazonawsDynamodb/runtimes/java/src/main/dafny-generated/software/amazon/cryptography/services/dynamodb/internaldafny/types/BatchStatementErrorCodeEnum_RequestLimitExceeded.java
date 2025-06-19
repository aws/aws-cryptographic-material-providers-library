// Class BatchStatementErrorCodeEnum_RequestLimitExceeded
// Dafny class BatchStatementErrorCodeEnum_RequestLimitExceeded compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_RequestLimitExceeded extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_RequestLimitExceeded () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_RequestLimitExceeded o = (BatchStatementErrorCodeEnum_RequestLimitExceeded)other;
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
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.RequestLimitExceeded");
    return s.toString();
  }
}
