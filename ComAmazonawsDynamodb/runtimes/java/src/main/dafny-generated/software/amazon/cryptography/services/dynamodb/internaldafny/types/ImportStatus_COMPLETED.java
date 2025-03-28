// Class ImportStatus_COMPLETED
// Dafny class ImportStatus_COMPLETED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ImportStatus_COMPLETED extends ImportStatus {
  public ImportStatus_COMPLETED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportStatus_COMPLETED o = (ImportStatus_COMPLETED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ImportStatus.COMPLETED");
    return s.toString();
  }
}
