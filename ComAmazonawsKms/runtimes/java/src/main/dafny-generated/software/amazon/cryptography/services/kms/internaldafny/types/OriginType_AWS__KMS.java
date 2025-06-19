// Class OriginType_AWS__KMS
// Dafny class OriginType_AWS__KMS compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class OriginType_AWS__KMS extends OriginType {
  public OriginType_AWS__KMS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OriginType_AWS__KMS o = (OriginType_AWS__KMS)other;
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
    s.append("ComAmazonawsKmsTypes.OriginType.AWS_KMS");
    return s.toString();
  }
}
