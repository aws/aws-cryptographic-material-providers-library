// Class StreamViewType_NEW__IMAGE
// Dafny class StreamViewType_NEW__IMAGE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class StreamViewType_NEW__IMAGE extends StreamViewType {
  public StreamViewType_NEW__IMAGE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StreamViewType_NEW__IMAGE o = (StreamViewType_NEW__IMAGE)other;
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
    s.append("ComAmazonawsDynamodbTypes.StreamViewType.NEW_IMAGE");
    return s.toString();
  }
}
