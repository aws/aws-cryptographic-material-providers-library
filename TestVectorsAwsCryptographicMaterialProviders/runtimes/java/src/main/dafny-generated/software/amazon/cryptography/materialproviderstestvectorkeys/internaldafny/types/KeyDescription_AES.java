// Class KeyDescription_AES
// Dafny class KeyDescription_AES compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_AES extends KeyDescription {
  public RawAES _AES;
  public KeyDescription_AES (RawAES AES) {
    super();
    this._AES = AES;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_AES o = (KeyDescription_AES)other;
    return true && java.util.Objects.equals(this._AES, o._AES);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AES);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.AES");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AES));
    s.append(")");
    return s.toString();
  }
}
