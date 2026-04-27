// Class Config
// Dafny class Config compiled into Java
package AwsCryptographyMaterialProvidersOperations_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Config {
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _crypto;
  public Config (software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto) {
    this._crypto = crypto;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Config o = (Config)other;
    return true && this._crypto == o._crypto;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._crypto);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersOperations.Config.Config");
    s.append("(");
    s.append(dafny.Helpers.toString(this._crypto));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Config> _TYPE = dafny.TypeDescriptor.<Config>referenceWithInitializer(Config.class, () -> Config.Default());
  public static dafny.TypeDescriptor<Config> _typeDescriptor() {
    return (dafny.TypeDescriptor<Config>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Config theDefault = Config.create(null);
  public static Config Default() {
    return theDefault;
  }
  public static Config create(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto) {
    return new Config(crypto);
  }
  public static Config create_Config(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto) {
    return create(crypto);
  }
  public boolean is_Config() { return true; }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient dtor_crypto() {
    return this._crypto;
  }
}
