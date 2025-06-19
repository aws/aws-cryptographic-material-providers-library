// Class CustomKeyStoreType_EXTERNAL__KEY__STORE
// Dafny class CustomKeyStoreType_EXTERNAL__KEY__STORE compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CustomKeyStoreType_EXTERNAL__KEY__STORE extends CustomKeyStoreType {
  public CustomKeyStoreType_EXTERNAL__KEY__STORE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomKeyStoreType_EXTERNAL__KEY__STORE o = (CustomKeyStoreType_EXTERNAL__KEY__STORE)other;
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
    s.append("ComAmazonawsKmsTypes.CustomKeyStoreType.EXTERNAL_KEY_STORE");
    return s.toString();
  }
}
