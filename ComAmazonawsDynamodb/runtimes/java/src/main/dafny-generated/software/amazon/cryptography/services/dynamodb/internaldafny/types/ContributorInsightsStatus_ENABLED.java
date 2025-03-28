// Class ContributorInsightsStatus_ENABLED
// Dafny class ContributorInsightsStatus_ENABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ContributorInsightsStatus_ENABLED extends ContributorInsightsStatus {
  public ContributorInsightsStatus_ENABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContributorInsightsStatus_ENABLED o = (ContributorInsightsStatus_ENABLED)other;
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
    s.append("ComAmazonawsDynamodbTypes.ContributorInsightsStatus.ENABLED");
    return s.toString();
  }
}
