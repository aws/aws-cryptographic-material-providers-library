// Class StaticConfigurations_RAW__ECDH
// Dafny class StaticConfigurations_RAW__ECDH compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class StaticConfigurations_RAW__ECDH extends StaticConfigurations {
  public RawEcdhStaticConfigurations _RAW__ECDH;
  public StaticConfigurations_RAW__ECDH (RawEcdhStaticConfigurations RAW__ECDH) {
    super();
    this._RAW__ECDH = RAW__ECDH;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StaticConfigurations_RAW__ECDH o = (StaticConfigurations_RAW__ECDH)other;
    return true && java.util.Objects.equals(this._RAW__ECDH, o._RAW__ECDH);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RAW__ECDH);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.StaticConfigurations.RAW_ECDH");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RAW__ECDH));
    s.append(")");
    return s.toString();
  }
}
