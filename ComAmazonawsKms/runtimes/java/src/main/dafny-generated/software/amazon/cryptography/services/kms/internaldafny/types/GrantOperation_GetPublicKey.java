// Class GrantOperation_GetPublicKey
// Dafny class GrantOperation_GetPublicKey compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_GetPublicKey extends GrantOperation {
  public GrantOperation_GetPublicKey () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_GetPublicKey o = (GrantOperation_GetPublicKey)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.GetPublicKey");
    return s.toString();
  }
}
