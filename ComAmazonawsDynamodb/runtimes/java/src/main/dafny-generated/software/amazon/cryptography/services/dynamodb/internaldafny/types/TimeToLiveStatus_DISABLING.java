// Class TimeToLiveStatus_DISABLING
// Dafny class TimeToLiveStatus_DISABLING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TimeToLiveStatus_DISABLING extends TimeToLiveStatus {
  public TimeToLiveStatus_DISABLING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TimeToLiveStatus_DISABLING o = (TimeToLiveStatus_DISABLING)other;
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
    s.append("ComAmazonawsDynamodbTypes.TimeToLiveStatus.DISABLING");
    return s.toString();
  }
}
