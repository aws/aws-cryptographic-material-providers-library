// Class BatchStatementErrorCodeEnum_AccessDenied
// Dafny class BatchStatementErrorCodeEnum_AccessDenied compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementErrorCodeEnum_AccessDenied extends BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum_AccessDenied () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementErrorCodeEnum_AccessDenied o = (BatchStatementErrorCodeEnum_AccessDenied)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.AccessDenied");
    return s.toString();
  }
}
