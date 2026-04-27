// Class KeyUsageType_ENCRYPT__DECRYPT
// Dafny class KeyUsageType_ENCRYPT__DECRYPT compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyUsageType_ENCRYPT__DECRYPT extends KeyUsageType {
  public KeyUsageType_ENCRYPT__DECRYPT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyUsageType_ENCRYPT__DECRYPT o = (KeyUsageType_ENCRYPT__DECRYPT)other;
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
    s.append("ComAmazonawsKmsTypes.KeyUsageType.ENCRYPT_DECRYPT");
    return s.toString();
  }
}
