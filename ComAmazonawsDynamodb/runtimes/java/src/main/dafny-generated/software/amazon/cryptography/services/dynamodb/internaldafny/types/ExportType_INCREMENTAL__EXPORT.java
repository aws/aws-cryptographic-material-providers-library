// Class ExportType_INCREMENTAL__EXPORT
// Dafny class ExportType_INCREMENTAL__EXPORT compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExportType_INCREMENTAL__EXPORT extends ExportType {
  public ExportType_INCREMENTAL__EXPORT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExportType_INCREMENTAL__EXPORT o = (ExportType_INCREMENTAL__EXPORT)other;
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
    s.append("ComAmazonawsDynamodbTypes.ExportType.INCREMENTAL_EXPORT");
    return s.toString();
  }
}
