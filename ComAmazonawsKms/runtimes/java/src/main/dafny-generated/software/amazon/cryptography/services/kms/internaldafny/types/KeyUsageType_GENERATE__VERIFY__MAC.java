// Class KeyUsageType_GENERATE__VERIFY__MAC
// Dafny class KeyUsageType_GENERATE__VERIFY__MAC compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeyUsageType_GENERATE__VERIFY__MAC extends KeyUsageType {
  public KeyUsageType_GENERATE__VERIFY__MAC () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyUsageType_GENERATE__VERIFY__MAC o = (KeyUsageType_GENERATE__VERIFY__MAC)other;
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
    s.append("ComAmazonawsKmsTypes.KeyUsageType.GENERATE_VERIFY_MAC");
    return s.toString();
  }
}
