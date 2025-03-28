// Class StreamViewType_KEYS__ONLY
// Dafny class StreamViewType_KEYS__ONLY compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class StreamViewType_KEYS__ONLY extends StreamViewType {
  public StreamViewType_KEYS__ONLY () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StreamViewType_KEYS__ONLY o = (StreamViewType_KEYS__ONLY)other;
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
    s.append("ComAmazonawsDynamodbTypes.StreamViewType.KEYS_ONLY");
    return s.toString();
  }
}
