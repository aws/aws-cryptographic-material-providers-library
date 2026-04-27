// Class KeyDescription_KmsRsa
// Dafny class KeyDescription_KmsRsa compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_KmsRsa extends KeyDescription {
  public KmsRsaKeyring _KmsRsa;
  public KeyDescription_KmsRsa (KmsRsaKeyring KmsRsa) {
    super();
    this._KmsRsa = KmsRsa;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_KmsRsa o = (KeyDescription_KmsRsa)other;
    return true && java.util.Objects.equals(this._KmsRsa, o._KmsRsa);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KmsRsa);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsRsa");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KmsRsa));
    s.append(")");
    return s.toString();
  }
}
