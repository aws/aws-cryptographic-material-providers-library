// Class StreamViewType_NEW__AND__OLD__IMAGES
// Dafny class StreamViewType_NEW__AND__OLD__IMAGES compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class StreamViewType_NEW__AND__OLD__IMAGES extends StreamViewType {
  public StreamViewType_NEW__AND__OLD__IMAGES () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StreamViewType_NEW__AND__OLD__IMAGES o = (StreamViewType_NEW__AND__OLD__IMAGES)other;
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
    s.append("ComAmazonawsDynamodbTypes.StreamViewType.NEW_AND_OLD_IMAGES");
    return s.toString();
  }
}
