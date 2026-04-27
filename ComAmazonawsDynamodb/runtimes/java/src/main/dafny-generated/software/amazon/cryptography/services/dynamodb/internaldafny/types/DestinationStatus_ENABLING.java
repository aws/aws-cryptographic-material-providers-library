// Class DestinationStatus_ENABLING
// Dafny class DestinationStatus_ENABLING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DestinationStatus_ENABLING extends DestinationStatus {
  public DestinationStatus_ENABLING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DestinationStatus_ENABLING o = (DestinationStatus_ENABLING)other;
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
    s.append("ComAmazonawsDynamodbTypes.DestinationStatus.ENABLING");
    return s.toString();
  }
}
