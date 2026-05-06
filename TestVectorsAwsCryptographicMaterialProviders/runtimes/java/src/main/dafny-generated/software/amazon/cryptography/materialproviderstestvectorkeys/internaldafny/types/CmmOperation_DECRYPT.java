// Class CmmOperation_DECRYPT
// Dafny class CmmOperation_DECRYPT compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CmmOperation_DECRYPT extends CmmOperation {
  public CmmOperation_DECRYPT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CmmOperation_DECRYPT o = (CmmOperation_DECRYPT)other;
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
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.DECRYPT");
    return s.toString();
  }
}
