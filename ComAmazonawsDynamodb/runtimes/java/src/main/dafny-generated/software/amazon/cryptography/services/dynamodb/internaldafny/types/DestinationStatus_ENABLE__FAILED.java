// Class DestinationStatus_ENABLE__FAILED
// Dafny class DestinationStatus_ENABLE__FAILED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DestinationStatus_ENABLE__FAILED extends DestinationStatus {
  public DestinationStatus_ENABLE__FAILED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DestinationStatus_ENABLE__FAILED o = (DestinationStatus_ENABLE__FAILED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DestinationStatus.ENABLE_FAILED");
    return s.toString();
  }
}
