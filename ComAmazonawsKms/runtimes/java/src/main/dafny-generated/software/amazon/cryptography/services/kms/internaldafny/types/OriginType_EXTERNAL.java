// Class OriginType_EXTERNAL
// Dafny class OriginType_EXTERNAL compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class OriginType_EXTERNAL extends OriginType {
  public OriginType_EXTERNAL () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OriginType_EXTERNAL o = (OriginType_EXTERNAL)other;
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
    s.append("ComAmazonawsKmsTypes.OriginType.EXTERNAL");
    return s.toString();
  }
}
