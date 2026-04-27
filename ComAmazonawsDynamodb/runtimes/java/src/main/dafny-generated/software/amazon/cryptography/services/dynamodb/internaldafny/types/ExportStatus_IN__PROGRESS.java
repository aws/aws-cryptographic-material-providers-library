// Class ExportStatus_IN__PROGRESS
// Dafny class ExportStatus_IN__PROGRESS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExportStatus_IN__PROGRESS extends ExportStatus {
  public ExportStatus_IN__PROGRESS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExportStatus_IN__PROGRESS o = (ExportStatus_IN__PROGRESS)other;
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
    s.append("ComAmazonawsDynamodbTypes.ExportStatus.IN_PROGRESS");
    return s.toString();
  }
}
