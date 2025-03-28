// Class S3SseAlgorithm_AES256
// Dafny class S3SseAlgorithm_AES256 compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class S3SseAlgorithm_AES256 extends S3SseAlgorithm {
  public S3SseAlgorithm_AES256 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    S3SseAlgorithm_AES256 o = (S3SseAlgorithm_AES256)other;
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
    s.append("ComAmazonawsDynamodbTypes.S3SseAlgorithm.AES256");
    return s.toString();
  }
}
