// Class ProjectionType_KEYS__ONLY
// Dafny class ProjectionType_KEYS__ONLY compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ProjectionType_KEYS__ONLY extends ProjectionType {
  public ProjectionType_KEYS__ONLY () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ProjectionType_KEYS__ONLY o = (ProjectionType_KEYS__ONLY)other;
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
    s.append("ComAmazonawsDynamodbTypes.ProjectionType.KEYS_ONLY");
    return s.toString();
  }
}
