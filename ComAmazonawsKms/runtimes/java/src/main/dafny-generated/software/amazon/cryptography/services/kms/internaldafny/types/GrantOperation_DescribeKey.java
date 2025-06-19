// Class GrantOperation_DescribeKey
// Dafny class GrantOperation_DescribeKey compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantOperation_DescribeKey extends GrantOperation {
  public GrantOperation_DescribeKey () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantOperation_DescribeKey o = (GrantOperation_DescribeKey)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 11;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantOperation.DescribeKey");
    return s.toString();
  }
}
