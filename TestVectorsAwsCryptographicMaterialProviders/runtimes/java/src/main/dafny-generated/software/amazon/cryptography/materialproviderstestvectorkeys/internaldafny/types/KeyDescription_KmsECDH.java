// Class KeyDescription_KmsECDH
// Dafny class KeyDescription_KmsECDH compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_KmsECDH extends KeyDescription {
  public KmsEcdhKeyring _KmsECDH;
  public KeyDescription_KmsECDH (KmsEcdhKeyring KmsECDH) {
    super();
    this._KmsECDH = KmsECDH;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_KmsECDH o = (KeyDescription_KmsECDH)other;
    return true && java.util.Objects.equals(this._KmsECDH, o._KmsECDH);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KmsECDH);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsECDH");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KmsECDH));
    s.append(")");
    return s.toString();
  }
}
