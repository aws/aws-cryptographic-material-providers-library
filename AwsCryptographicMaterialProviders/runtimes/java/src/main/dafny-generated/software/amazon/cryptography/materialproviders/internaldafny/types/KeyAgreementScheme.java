// Class KeyAgreementScheme
// Dafny class KeyAgreementScheme compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyAgreementScheme {
  public StaticConfigurations _StaticConfiguration;
  public KeyAgreementScheme (StaticConfigurations StaticConfiguration) {
    this._StaticConfiguration = StaticConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyAgreementScheme o = (KeyAgreementScheme)other;
    return true && java.util.Objects.equals(this._StaticConfiguration, o._StaticConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StaticConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.KeyAgreementScheme.StaticConfiguration");
    s.append("(");
    s.append(dafny.Helpers.toString(this._StaticConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyAgreementScheme> _TYPE = dafny.TypeDescriptor.<KeyAgreementScheme>referenceWithInitializer(KeyAgreementScheme.class, () -> KeyAgreementScheme.Default());
  public static dafny.TypeDescriptor<KeyAgreementScheme> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyAgreementScheme>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyAgreementScheme theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.KeyAgreementScheme.create(StaticConfigurations.Default());
  public static KeyAgreementScheme Default() {
    return theDefault;
  }
  public static KeyAgreementScheme create(StaticConfigurations StaticConfiguration) {
    return new KeyAgreementScheme(StaticConfiguration);
  }
  public static KeyAgreementScheme create_StaticConfiguration(StaticConfigurations StaticConfiguration) {
    return create(StaticConfiguration);
  }
  public boolean is_StaticConfiguration() { return true; }
  public StaticConfigurations dtor_StaticConfiguration() {
    return this._StaticConfiguration;
  }
}
