// Class OriginType_AWS__CLOUDHSM
// Dafny class OriginType_AWS__CLOUDHSM compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class OriginType_AWS__CLOUDHSM extends OriginType {
  public OriginType_AWS__CLOUDHSM () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OriginType_AWS__CLOUDHSM o = (OriginType_AWS__CLOUDHSM)other;
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
    s.append("ComAmazonawsKmsTypes.OriginType.AWS_CLOUDHSM");
    return s.toString();
  }
}
