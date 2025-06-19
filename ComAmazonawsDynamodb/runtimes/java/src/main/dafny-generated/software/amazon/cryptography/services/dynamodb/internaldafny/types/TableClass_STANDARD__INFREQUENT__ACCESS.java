// Class TableClass_STANDARD__INFREQUENT__ACCESS
// Dafny class TableClass_STANDARD__INFREQUENT__ACCESS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TableClass_STANDARD__INFREQUENT__ACCESS extends TableClass {
  public TableClass_STANDARD__INFREQUENT__ACCESS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableClass_STANDARD__INFREQUENT__ACCESS o = (TableClass_STANDARD__INFREQUENT__ACCESS)other;
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
    s.append("ComAmazonawsDynamodbTypes.TableClass.STANDARD_INFREQUENT_ACCESS");
    return s.toString();
  }
}
