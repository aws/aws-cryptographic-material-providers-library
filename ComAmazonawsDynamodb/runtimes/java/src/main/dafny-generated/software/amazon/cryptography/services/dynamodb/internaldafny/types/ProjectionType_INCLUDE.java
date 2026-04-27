// Class ProjectionType_INCLUDE
// Dafny class ProjectionType_INCLUDE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ProjectionType_INCLUDE extends ProjectionType {
  public ProjectionType_INCLUDE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ProjectionType_INCLUDE o = (ProjectionType_INCLUDE)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ProjectionType.INCLUDE");
    return s.toString();
  }
}
