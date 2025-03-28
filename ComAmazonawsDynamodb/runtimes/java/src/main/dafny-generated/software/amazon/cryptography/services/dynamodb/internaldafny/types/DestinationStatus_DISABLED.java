// Class DestinationStatus_DISABLED
// Dafny class DestinationStatus_DISABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DestinationStatus_DISABLED extends DestinationStatus {
  public DestinationStatus_DISABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DestinationStatus_DISABLED o = (DestinationStatus_DISABLED)other;
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
    s.append("ComAmazonawsDynamodbTypes.DestinationStatus.DISABLED");
    return s.toString();
  }
}
