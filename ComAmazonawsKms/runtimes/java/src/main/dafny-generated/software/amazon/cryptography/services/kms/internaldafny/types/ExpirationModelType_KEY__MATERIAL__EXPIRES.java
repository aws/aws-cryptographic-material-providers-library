// Class ExpirationModelType_KEY__MATERIAL__EXPIRES
// Dafny class ExpirationModelType_KEY__MATERIAL__EXPIRES compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ExpirationModelType_KEY__MATERIAL__EXPIRES extends ExpirationModelType {
  public ExpirationModelType_KEY__MATERIAL__EXPIRES () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExpirationModelType_KEY__MATERIAL__EXPIRES o = (ExpirationModelType_KEY__MATERIAL__EXPIRES)other;
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
    s.append("ComAmazonawsKmsTypes.ExpirationModelType.KEY_MATERIAL_EXPIRES");
    return s.toString();
  }
}
