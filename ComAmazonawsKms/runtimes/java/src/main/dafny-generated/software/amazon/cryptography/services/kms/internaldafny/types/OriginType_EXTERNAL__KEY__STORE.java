// Class OriginType_EXTERNAL__KEY__STORE
// Dafny class OriginType_EXTERNAL__KEY__STORE compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class OriginType_EXTERNAL__KEY__STORE extends OriginType {
  public OriginType_EXTERNAL__KEY__STORE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OriginType_EXTERNAL__KEY__STORE o = (OriginType_EXTERNAL__KEY__STORE)other;
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
    s.append("ComAmazonawsKmsTypes.OriginType.EXTERNAL_KEY_STORE");
    return s.toString();
  }
}
