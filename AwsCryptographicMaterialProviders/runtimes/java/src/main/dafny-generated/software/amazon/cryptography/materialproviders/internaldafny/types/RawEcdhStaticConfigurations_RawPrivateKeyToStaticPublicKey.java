// Class RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey
// Dafny class RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey extends RawEcdhStaticConfigurations {
  public RawPrivateKeyToStaticPublicKeyInput _RawPrivateKeyToStaticPublicKey;
  public RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey (RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey) {
    super();
    this._RawPrivateKeyToStaticPublicKey = RawPrivateKeyToStaticPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey o = (RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey)other;
    return true && java.util.Objects.equals(this._RawPrivateKeyToStaticPublicKey, o._RawPrivateKeyToStaticPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RawPrivateKeyToStaticPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.RawPrivateKeyToStaticPublicKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RawPrivateKeyToStaticPublicKey));
    s.append(")");
    return s.toString();
  }
}
