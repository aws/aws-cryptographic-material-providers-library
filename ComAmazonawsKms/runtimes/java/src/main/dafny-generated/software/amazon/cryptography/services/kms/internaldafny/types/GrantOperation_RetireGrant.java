// Class GrantOperation_RetireGrant
// Dafny class GrantOperation_RetireGrant compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_RetireGrant extends GrantOperation {
  public GrantOperation_RetireGrant () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_RetireGrant o = (GrantOperation_RetireGrant)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 10;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.RetireGrant");
    return s.toString();
  }
}
