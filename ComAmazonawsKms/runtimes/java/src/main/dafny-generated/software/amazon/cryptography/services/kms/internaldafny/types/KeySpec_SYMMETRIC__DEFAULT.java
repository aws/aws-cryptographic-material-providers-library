// Class KeySpec_SYMMETRIC__DEFAULT
// Dafny class KeySpec_SYMMETRIC__DEFAULT compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeySpec_SYMMETRIC__DEFAULT extends KeySpec {
  public KeySpec_SYMMETRIC__DEFAULT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeySpec_SYMMETRIC__DEFAULT o = (KeySpec_SYMMETRIC__DEFAULT)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeySpec.SYMMETRIC_DEFAULT");
    return s.toString();
  }
}
