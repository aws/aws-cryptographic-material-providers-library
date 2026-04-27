// Class SmallEncryptionContextVariation_A
// Dafny class SmallEncryptionContextVariation_A compiled into Java
package TestUtils_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SmallEncryptionContextVariation_A extends SmallEncryptionContextVariation {
  public SmallEncryptionContextVariation_A () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SmallEncryptionContextVariation_A o = (SmallEncryptionContextVariation_A)other;
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
    s.append("TestUtils.SmallEncryptionContextVariation.A");
    return s.toString();
  }
}
