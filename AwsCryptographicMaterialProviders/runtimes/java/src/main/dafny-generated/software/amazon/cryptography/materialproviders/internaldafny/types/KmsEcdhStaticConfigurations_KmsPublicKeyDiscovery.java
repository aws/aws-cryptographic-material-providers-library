// Class KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery
// Dafny class KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery extends KmsEcdhStaticConfigurations {
  public KmsPublicKeyDiscoveryInput _KmsPublicKeyDiscovery;
  public KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery (KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery) {
    super();
    this._KmsPublicKeyDiscovery = KmsPublicKeyDiscovery;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery o = (KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery)other;
    return true && java.util.Objects.equals(this._KmsPublicKeyDiscovery, o._KmsPublicKeyDiscovery);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KmsPublicKeyDiscovery);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations.KmsPublicKeyDiscovery");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KmsPublicKeyDiscovery));
    s.append(")");
    return s.toString();
  }
}
