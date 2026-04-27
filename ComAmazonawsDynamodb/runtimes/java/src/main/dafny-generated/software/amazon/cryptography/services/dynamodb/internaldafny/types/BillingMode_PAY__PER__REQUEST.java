// Class BillingMode_PAY__PER__REQUEST
// Dafny class BillingMode_PAY__PER__REQUEST compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BillingMode_PAY__PER__REQUEST extends BillingMode {
  public BillingMode_PAY__PER__REQUEST () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BillingMode_PAY__PER__REQUEST o = (BillingMode_PAY__PER__REQUEST)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BillingMode.PAY_PER_REQUEST");
    return s.toString();
  }
}
