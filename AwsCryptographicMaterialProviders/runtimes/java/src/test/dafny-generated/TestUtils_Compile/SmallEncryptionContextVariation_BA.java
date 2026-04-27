// Class SmallEncryptionContextVariation_BA
// Dafny class SmallEncryptionContextVariation_BA compiled into Java
package TestUtils_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SmallEncryptionContextVariation_BA extends SmallEncryptionContextVariation {
  public SmallEncryptionContextVariation_BA () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SmallEncryptionContextVariation_BA o = (SmallEncryptionContextVariation_BA)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestUtils.SmallEncryptionContextVariation.BA");
    return s.toString();
  }
}
