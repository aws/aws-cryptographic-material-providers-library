// Class RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey
// Dafny class RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey extends RawEcdhStaticConfigurations {
  public EphemeralPrivateKeyToStaticPublicKeyInput _EphemeralPrivateKeyToStaticPublicKey;
  public RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey (EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey) {
    super();
    this._EphemeralPrivateKeyToStaticPublicKey = EphemeralPrivateKeyToStaticPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey o = (RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey)other;
    return true && java.util.Objects.equals(this._EphemeralPrivateKeyToStaticPublicKey, o._EphemeralPrivateKeyToStaticPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EphemeralPrivateKeyToStaticPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.EphemeralPrivateKeyToStaticPublicKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._EphemeralPrivateKeyToStaticPublicKey));
    s.append(")");
    return s.toString();
  }
}
