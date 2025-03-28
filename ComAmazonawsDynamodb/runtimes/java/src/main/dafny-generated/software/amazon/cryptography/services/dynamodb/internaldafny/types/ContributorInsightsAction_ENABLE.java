// Class ContributorInsightsAction_ENABLE
// Dafny class ContributorInsightsAction_ENABLE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ContributorInsightsAction_ENABLE extends ContributorInsightsAction {
  public ContributorInsightsAction_ENABLE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContributorInsightsAction_ENABLE o = (ContributorInsightsAction_ENABLE)other;
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
    s.append("ComAmazonawsDynamodbTypes.ContributorInsightsAction.ENABLE");
    return s.toString();
  }
}
