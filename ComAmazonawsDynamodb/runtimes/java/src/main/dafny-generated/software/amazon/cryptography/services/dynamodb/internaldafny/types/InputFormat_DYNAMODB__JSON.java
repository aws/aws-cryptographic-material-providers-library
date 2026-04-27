// Class InputFormat_DYNAMODB__JSON
// Dafny class InputFormat_DYNAMODB__JSON compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class InputFormat_DYNAMODB__JSON extends InputFormat {
  public InputFormat_DYNAMODB__JSON () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    InputFormat_DYNAMODB__JSON o = (InputFormat_DYNAMODB__JSON)other;
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
    s.append("ComAmazonawsDynamodbTypes.InputFormat.DYNAMODB_JSON");
    return s.toString();
  }
}
