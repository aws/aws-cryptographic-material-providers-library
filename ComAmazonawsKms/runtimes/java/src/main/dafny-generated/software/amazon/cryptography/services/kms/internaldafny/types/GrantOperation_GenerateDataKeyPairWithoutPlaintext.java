// Class GrantOperation_GenerateDataKeyPairWithoutPlaintext
// Dafny class GrantOperation_GenerateDataKeyPairWithoutPlaintext compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_GenerateDataKeyPairWithoutPlaintext extends GrantOperation {
  public GrantOperation_GenerateDataKeyPairWithoutPlaintext () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_GenerateDataKeyPairWithoutPlaintext o = (GrantOperation_GenerateDataKeyPairWithoutPlaintext)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 13;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.GenerateDataKeyPairWithoutPlaintext");
    return s.toString();
  }
}
