// Class RotationType_AUTOMATIC
// Dafny class RotationType_AUTOMATIC compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RotationType_AUTOMATIC extends RotationType {
  public RotationType_AUTOMATIC () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RotationType_AUTOMATIC o = (RotationType_AUTOMATIC)other;
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
    s.append("ComAmazonawsKmsTypes.RotationType.AUTOMATIC");
    return s.toString();
  }
}
