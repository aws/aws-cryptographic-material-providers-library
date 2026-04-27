// Class MultiRegionKeyType_PRIMARY
// Dafny class MultiRegionKeyType_PRIMARY compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class MultiRegionKeyType_PRIMARY extends MultiRegionKeyType {
  public MultiRegionKeyType_PRIMARY () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MultiRegionKeyType_PRIMARY o = (MultiRegionKeyType_PRIMARY)other;
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
    s.append("ComAmazonawsKmsTypes.MultiRegionKeyType.PRIMARY");
    return s.toString();
  }
}
