// Class ReturnValue_ALL__OLD
// Dafny class ReturnValue_ALL__OLD compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnValue_ALL__OLD extends ReturnValue {
  public ReturnValue_ALL__OLD () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnValue_ALL__OLD o = (ReturnValue_ALL__OLD)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnValue.ALL_OLD");
    return s.toString();
  }
}
