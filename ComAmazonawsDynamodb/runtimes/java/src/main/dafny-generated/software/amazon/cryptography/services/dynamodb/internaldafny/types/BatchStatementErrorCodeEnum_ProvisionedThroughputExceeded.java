// Class BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded
// Dafny class BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded o = (BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ProvisionedThroughputExceeded");
    return s.toString();
  }
}
