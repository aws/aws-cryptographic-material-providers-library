// Class BillingMode_PROVISIONED
// Dafny class BillingMode_PROVISIONED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BillingMode_PROVISIONED extends BillingMode {
  public BillingMode_PROVISIONED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BillingMode_PROVISIONED o = (BillingMode_PROVISIONED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BillingMode.PROVISIONED");
    return s.toString();
  }
}
