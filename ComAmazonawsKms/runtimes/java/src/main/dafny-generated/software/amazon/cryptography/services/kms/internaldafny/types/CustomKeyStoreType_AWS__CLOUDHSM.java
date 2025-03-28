// Class CustomKeyStoreType_AWS__CLOUDHSM
// Dafny class CustomKeyStoreType_AWS__CLOUDHSM compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CustomKeyStoreType_AWS__CLOUDHSM extends CustomKeyStoreType {
  public CustomKeyStoreType_AWS__CLOUDHSM () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomKeyStoreType_AWS__CLOUDHSM o = (CustomKeyStoreType_AWS__CLOUDHSM)other;
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
    s.append("ComAmazonawsKmsTypes.CustomKeyStoreType.AWS_CLOUDHSM");
    return s.toString();
  }
}
