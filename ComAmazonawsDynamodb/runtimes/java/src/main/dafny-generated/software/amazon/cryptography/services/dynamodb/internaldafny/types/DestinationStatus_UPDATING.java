// Class DestinationStatus_UPDATING
// Dafny class DestinationStatus_UPDATING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DestinationStatus_UPDATING extends DestinationStatus {
  public DestinationStatus_UPDATING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DestinationStatus_UPDATING o = (DestinationStatus_UPDATING)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DestinationStatus.UPDATING");
    return s.toString();
  }
}
