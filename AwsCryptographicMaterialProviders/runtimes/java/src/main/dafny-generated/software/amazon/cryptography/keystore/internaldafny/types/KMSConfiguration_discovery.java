// Class KMSConfiguration_discovery
// Dafny class KMSConfiguration_discovery compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KMSConfiguration_discovery extends KMSConfiguration {
  public Discovery _discovery;
  public KMSConfiguration_discovery (Discovery discovery) {
    super();
    this._discovery = discovery;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KMSConfiguration_discovery o = (KMSConfiguration_discovery)other;
    return true && java.util.Objects.equals(this._discovery, o._discovery);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._discovery);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.KMSConfiguration.discovery");
    s.append("(");
    s.append(dafny.Helpers.toString(this._discovery));
    s.append(")");
    return s.toString();
  }
}
