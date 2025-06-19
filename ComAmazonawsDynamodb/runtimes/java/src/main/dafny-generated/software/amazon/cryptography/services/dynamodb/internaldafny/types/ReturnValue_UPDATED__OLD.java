// Class ReturnValue_UPDATED__OLD
// Dafny class ReturnValue_UPDATED__OLD compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReturnValue_UPDATED__OLD extends ReturnValue {
  public ReturnValue_UPDATED__OLD () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReturnValue_UPDATED__OLD o = (ReturnValue_UPDATED__OLD)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReturnValue.UPDATED_OLD");
    return s.toString();
  }
}
