// Class StreamViewType_OLD__IMAGE
// Dafny class StreamViewType_OLD__IMAGE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class StreamViewType_OLD__IMAGE extends StreamViewType {
  public StreamViewType_OLD__IMAGE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StreamViewType_OLD__IMAGE o = (StreamViewType_OLD__IMAGE)other;
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
    s.append("ComAmazonawsDynamodbTypes.StreamViewType.OLD_IMAGE");
    return s.toString();
  }
}
