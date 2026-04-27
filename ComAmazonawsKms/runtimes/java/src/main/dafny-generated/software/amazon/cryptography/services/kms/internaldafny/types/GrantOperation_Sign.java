// Class GrantOperation_Sign
// Dafny class GrantOperation_Sign compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_Sign extends GrantOperation {
  public GrantOperation_Sign () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_Sign o = (GrantOperation_Sign)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.Sign");
    return s.toString();
  }
}
