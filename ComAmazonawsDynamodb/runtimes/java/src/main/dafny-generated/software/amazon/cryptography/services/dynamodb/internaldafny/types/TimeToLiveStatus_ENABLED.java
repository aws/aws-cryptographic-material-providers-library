// Class TimeToLiveStatus_ENABLED
// Dafny class TimeToLiveStatus_ENABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TimeToLiveStatus_ENABLED extends TimeToLiveStatus {
  public TimeToLiveStatus_ENABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TimeToLiveStatus_ENABLED o = (TimeToLiveStatus_ENABLED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TimeToLiveStatus.ENABLED");
    return s.toString();
  }
}
