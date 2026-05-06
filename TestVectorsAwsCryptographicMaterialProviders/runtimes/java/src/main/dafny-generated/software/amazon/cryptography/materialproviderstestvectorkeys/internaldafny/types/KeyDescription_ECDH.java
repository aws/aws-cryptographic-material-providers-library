// Class KeyDescription_ECDH
// Dafny class KeyDescription_ECDH compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_ECDH extends KeyDescription {
  public RawEcdh _ECDH;
  public KeyDescription_ECDH (RawEcdh ECDH) {
    super();
    this._ECDH = ECDH;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_ECDH o = (KeyDescription_ECDH)other;
    return true && java.util.Objects.equals(this._ECDH, o._ECDH);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ECDH);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.ECDH");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ECDH));
    s.append(")");
    return s.toString();
  }
}
