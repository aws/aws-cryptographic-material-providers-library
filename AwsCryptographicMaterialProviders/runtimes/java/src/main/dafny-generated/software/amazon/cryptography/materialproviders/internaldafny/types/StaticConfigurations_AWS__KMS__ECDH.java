// Class StaticConfigurations_AWS__KMS__ECDH
// Dafny class StaticConfigurations_AWS__KMS__ECDH compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class StaticConfigurations_AWS__KMS__ECDH extends StaticConfigurations {
  public KmsEcdhStaticConfigurations _AWS__KMS__ECDH;
  public StaticConfigurations_AWS__KMS__ECDH (KmsEcdhStaticConfigurations AWS__KMS__ECDH) {
    super();
    this._AWS__KMS__ECDH = AWS__KMS__ECDH;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StaticConfigurations_AWS__KMS__ECDH o = (StaticConfigurations_AWS__KMS__ECDH)other;
    return true && java.util.Objects.equals(this._AWS__KMS__ECDH, o._AWS__KMS__ECDH);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AWS__KMS__ECDH);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.StaticConfigurations.AWS_KMS_ECDH");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AWS__KMS__ECDH));
    s.append(")");
    return s.toString();
  }
}
