// Class GrantOperation_GenerateDataKeyPair
// Dafny class GrantOperation_GenerateDataKeyPair compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_GenerateDataKeyPair extends GrantOperation {
  public GrantOperation_GenerateDataKeyPair () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_GenerateDataKeyPair o = (GrantOperation_GenerateDataKeyPair)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 12;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.GenerateDataKeyPair");
    return s.toString();
  }
}
