// Class BatchStatementErrorCodeEnum_ThrottlingError
// Dafny class BatchStatementErrorCodeEnum_ThrottlingError compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_ThrottlingError extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_ThrottlingError () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_ThrottlingError o = (BatchStatementErrorCodeEnum_ThrottlingError)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ThrottlingError");
    return s.toString();
  }
}
