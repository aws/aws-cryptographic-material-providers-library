// Class ReturnItemCollectionMetrics_SIZE
// Dafny class ReturnItemCollectionMetrics_SIZE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnItemCollectionMetrics_SIZE extends ReturnItemCollectionMetrics {
  public ReturnItemCollectionMetrics_SIZE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnItemCollectionMetrics_SIZE o = (ReturnItemCollectionMetrics_SIZE)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnItemCollectionMetrics.SIZE");
    return s.toString();
  }
}
