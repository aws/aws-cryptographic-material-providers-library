// Class KMSConfiguration_mrDiscovery
// Dafny class KMSConfiguration_mrDiscovery compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KMSConfiguration_mrDiscovery extends KMSConfiguration {
  public MRDiscovery _mrDiscovery;
  public KMSConfiguration_mrDiscovery (MRDiscovery mrDiscovery) {
    super();
    this._mrDiscovery = mrDiscovery;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KMSConfiguration_mrDiscovery o = (KMSConfiguration_mrDiscovery)other;
    return true && java.util.Objects.equals(this._mrDiscovery, o._mrDiscovery);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._mrDiscovery);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.KMSConfiguration.mrDiscovery");
    s.append("(");
    s.append(dafny.Helpers.toString(this._mrDiscovery));
    s.append(")");
    return s.toString();
  }
}
