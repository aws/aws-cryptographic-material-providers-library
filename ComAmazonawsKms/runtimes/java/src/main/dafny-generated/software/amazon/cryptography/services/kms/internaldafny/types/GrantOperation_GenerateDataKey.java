// Class GrantOperation_GenerateDataKey
// Dafny class GrantOperation_GenerateDataKey compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_GenerateDataKey extends GrantOperation {
  public GrantOperation_GenerateDataKey () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_GenerateDataKey o = (GrantOperation_GenerateDataKey)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.GenerateDataKey");
    return s.toString();
  }
}
