// Class ImportStatus_CANCELLED
// Dafny class ImportStatus_CANCELLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ImportStatus_CANCELLED extends ImportStatus {
  public ImportStatus_CANCELLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportStatus_CANCELLED o = (ImportStatus_CANCELLED)other;
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
    s.append("ComAmazonawsDynamodbTypes.ImportStatus.CANCELLED");
    return s.toString();
  }
}
