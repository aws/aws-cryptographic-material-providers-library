// Class GrantOperation_CreateGrant
// Dafny class GrantOperation_CreateGrant compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_CreateGrant extends GrantOperation {
  public GrantOperation_CreateGrant () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_CreateGrant o = (GrantOperation_CreateGrant)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.CreateGrant");
    return s.toString();
  }
}
