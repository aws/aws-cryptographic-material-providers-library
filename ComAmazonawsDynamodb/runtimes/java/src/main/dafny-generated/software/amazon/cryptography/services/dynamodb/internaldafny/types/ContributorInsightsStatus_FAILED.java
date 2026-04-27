// Class ContributorInsightsStatus_FAILED
// Dafny class ContributorInsightsStatus_FAILED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ContributorInsightsStatus_FAILED extends ContributorInsightsStatus {
  public ContributorInsightsStatus_FAILED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContributorInsightsStatus_FAILED o = (ContributorInsightsStatus_FAILED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ContributorInsightsStatus.FAILED");
    return s.toString();
  }
}
