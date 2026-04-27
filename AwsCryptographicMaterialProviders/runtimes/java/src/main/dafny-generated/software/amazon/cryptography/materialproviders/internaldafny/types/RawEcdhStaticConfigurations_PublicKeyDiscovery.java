// Class RawEcdhStaticConfigurations_PublicKeyDiscovery
// Dafny class RawEcdhStaticConfigurations_PublicKeyDiscovery compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawEcdhStaticConfigurations_PublicKeyDiscovery extends RawEcdhStaticConfigurations {
  public PublicKeyDiscoveryInput _PublicKeyDiscovery;
  public RawEcdhStaticConfigurations_PublicKeyDiscovery (PublicKeyDiscoveryInput PublicKeyDiscovery) {
    super();
    this._PublicKeyDiscovery = PublicKeyDiscovery;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RawEcdhStaticConfigurations_PublicKeyDiscovery o = (RawEcdhStaticConfigurations_PublicKeyDiscovery)other;
    return true && java.util.Objects.equals(this._PublicKeyDiscovery, o._PublicKeyDiscovery);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PublicKeyDiscovery);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.PublicKeyDiscovery");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PublicKeyDiscovery));
    s.append(")");
    return s.toString();
  }
}
