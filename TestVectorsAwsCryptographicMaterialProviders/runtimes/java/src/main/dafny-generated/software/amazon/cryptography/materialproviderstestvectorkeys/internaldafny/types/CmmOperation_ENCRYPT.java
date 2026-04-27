// Class CmmOperation_ENCRYPT
// Dafny class CmmOperation_ENCRYPT compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CmmOperation_ENCRYPT extends CmmOperation {
  public CmmOperation_ENCRYPT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CmmOperation_ENCRYPT o = (CmmOperation_ENCRYPT)other;
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
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.ENCRYPT");
    return s.toString();
  }
}
