// Class ContributorInsightsAction_DISABLE
// Dafny class ContributorInsightsAction_DISABLE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ContributorInsightsAction_DISABLE extends ContributorInsightsAction {
  public ContributorInsightsAction_DISABLE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContributorInsightsAction_DISABLE o = (ContributorInsightsAction_DISABLE)other;
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
    s.append("ComAmazonawsDynamodbTypes.ContributorInsightsAction.DISABLE");
    return s.toString();
  }
}
