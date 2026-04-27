// Class ContributorInsightsStatus_ENABLING
// Dafny class ContributorInsightsStatus_ENABLING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ContributorInsightsStatus_ENABLING extends ContributorInsightsStatus {
  public ContributorInsightsStatus_ENABLING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContributorInsightsStatus_ENABLING o = (ContributorInsightsStatus_ENABLING)other;
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
    s.append("ComAmazonawsDynamodbTypes.ContributorInsightsStatus.ENABLING");
    return s.toString();
  }
}
