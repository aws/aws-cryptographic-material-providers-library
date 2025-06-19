// Class KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey
// Dafny class KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey extends KmsEcdhStaticConfigurations {
  public KmsPrivateKeyToStaticPublicKeyInput _KmsPrivateKeyToStaticPublicKey;
  public KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey (KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey) {
    super();
    this._KmsPrivateKeyToStaticPublicKey = KmsPrivateKeyToStaticPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey o = (KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey)other;
    return true && java.util.Objects.equals(this._KmsPrivateKeyToStaticPublicKey, o._KmsPrivateKeyToStaticPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KmsPrivateKeyToStaticPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KmsPrivateKeyToStaticPublicKey));
    s.append(")");
    return s.toString();
  }
}
