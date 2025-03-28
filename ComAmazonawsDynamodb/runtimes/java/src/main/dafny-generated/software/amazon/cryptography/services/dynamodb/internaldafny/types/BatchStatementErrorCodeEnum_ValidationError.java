// Class BatchStatementErrorCodeEnum_ValidationError
// Dafny class BatchStatementErrorCodeEnum_ValidationError compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_ValidationError extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_ValidationError () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_ValidationError o = (BatchStatementErrorCodeEnum_ValidationError)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ValidationError");
    return s.toString();
  }
}
