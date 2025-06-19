// Class DestinationStatus_ACTIVE
// Dafny class DestinationStatus_ACTIVE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DestinationStatus_ACTIVE extends DestinationStatus {
  public DestinationStatus_ACTIVE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DestinationStatus_ACTIVE o = (DestinationStatus_ACTIVE)other;
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
    s.append("ComAmazonawsDynamodbTypes.DestinationStatus.ACTIVE");
    return s.toString();
  }
}
