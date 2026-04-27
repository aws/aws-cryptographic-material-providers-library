// Class ImportStatus_CANCELLING
// Dafny class ImportStatus_CANCELLING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ImportStatus_CANCELLING extends ImportStatus {
  public ImportStatus_CANCELLING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportStatus_CANCELLING o = (ImportStatus_CANCELLING)other;
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
    s.append("ComAmazonawsDynamodbTypes.ImportStatus.CANCELLING");
    return s.toString();
  }
}
