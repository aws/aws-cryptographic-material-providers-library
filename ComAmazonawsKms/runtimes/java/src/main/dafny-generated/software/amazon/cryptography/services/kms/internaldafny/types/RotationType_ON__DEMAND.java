// Class RotationType_ON__DEMAND
// Dafny class RotationType_ON__DEMAND compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RotationType_ON__DEMAND extends RotationType {
  public RotationType_ON__DEMAND () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RotationType_ON__DEMAND o = (RotationType_ON__DEMAND)other;
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
    s.append("ComAmazonawsKmsTypes.RotationType.ON_DEMAND");
    return s.toString();
  }
}
