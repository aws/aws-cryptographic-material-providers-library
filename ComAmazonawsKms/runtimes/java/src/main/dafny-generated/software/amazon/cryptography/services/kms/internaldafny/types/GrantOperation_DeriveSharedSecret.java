// Class GrantOperation_DeriveSharedSecret
// Dafny class GrantOperation_DeriveSharedSecret compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_DeriveSharedSecret extends GrantOperation {
  public GrantOperation_DeriveSharedSecret () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_DeriveSharedSecret o = (GrantOperation_DeriveSharedSecret)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 16;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.DeriveSharedSecret");
    return s.toString();
  }
}
