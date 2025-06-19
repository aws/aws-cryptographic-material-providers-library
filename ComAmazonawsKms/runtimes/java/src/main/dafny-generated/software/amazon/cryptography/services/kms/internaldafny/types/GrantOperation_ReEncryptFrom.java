// Class GrantOperation_ReEncryptFrom
// Dafny class GrantOperation_ReEncryptFrom compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_ReEncryptFrom extends GrantOperation {
  public GrantOperation_ReEncryptFrom () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_ReEncryptFrom o = (GrantOperation_ReEncryptFrom)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.ReEncryptFrom");
    return s.toString();
  }
}
