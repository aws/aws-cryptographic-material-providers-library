// Class BatchStatementErrorCodeEnum_ResourceNotFound
// Dafny class BatchStatementErrorCodeEnum_ResourceNotFound compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_ResourceNotFound extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_ResourceNotFound () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_ResourceNotFound o = (BatchStatementErrorCodeEnum_ResourceNotFound)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ResourceNotFound");
    return s.toString();
  }
}
