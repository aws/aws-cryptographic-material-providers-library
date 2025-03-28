// Class TimeToLiveStatus_ENABLING
// Dafny class TimeToLiveStatus_ENABLING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TimeToLiveStatus_ENABLING extends TimeToLiveStatus {
  public TimeToLiveStatus_ENABLING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TimeToLiveStatus_ENABLING o = (TimeToLiveStatus_ENABLING)other;
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
    s.append("ComAmazonawsDynamodbTypes.TimeToLiveStatus.ENABLING");
    return s.toString();
  }
}
