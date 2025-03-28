// Class ContributorInsightsStatus_DISABLED
// Dafny class ContributorInsightsStatus_DISABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ContributorInsightsStatus_DISABLED extends ContributorInsightsStatus {
  public ContributorInsightsStatus_DISABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContributorInsightsStatus_DISABLED o = (ContributorInsightsStatus_DISABLED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ContributorInsightsStatus.DISABLED");
    return s.toString();
  }
}
