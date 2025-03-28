// Class GrantOperation_VerifyMac
// Dafny class GrantOperation_VerifyMac compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_VerifyMac extends GrantOperation {
  public GrantOperation_VerifyMac () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_VerifyMac o = (GrantOperation_VerifyMac)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 15;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.VerifyMac");
    return s.toString();
  }
}
