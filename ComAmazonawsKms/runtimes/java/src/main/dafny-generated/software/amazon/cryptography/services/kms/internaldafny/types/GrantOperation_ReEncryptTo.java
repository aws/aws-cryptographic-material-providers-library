// Class GrantOperation_ReEncryptTo
// Dafny class GrantOperation_ReEncryptTo compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_ReEncryptTo extends GrantOperation {
  public GrantOperation_ReEncryptTo () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_ReEncryptTo o = (GrantOperation_ReEncryptTo)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.ReEncryptTo");
    return s.toString();
  }
}
