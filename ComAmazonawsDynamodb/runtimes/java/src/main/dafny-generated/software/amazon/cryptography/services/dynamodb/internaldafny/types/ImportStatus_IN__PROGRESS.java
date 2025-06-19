// Class ImportStatus_IN__PROGRESS
// Dafny class ImportStatus_IN__PROGRESS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ImportStatus_IN__PROGRESS extends ImportStatus {
  public ImportStatus_IN__PROGRESS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportStatus_IN__PROGRESS o = (ImportStatus_IN__PROGRESS)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ImportStatus.IN_PROGRESS");
    return s.toString();
  }
}
