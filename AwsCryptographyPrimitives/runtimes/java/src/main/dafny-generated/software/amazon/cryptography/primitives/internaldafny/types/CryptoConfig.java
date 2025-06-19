// Class CryptoConfig
// Dafny class CryptoConfig compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CryptoConfig {
  public CryptoConfig () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CryptoConfig o = (CryptoConfig)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.CryptoConfig.CryptoConfig");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CryptoConfig> _TYPE = dafny.TypeDescriptor.<CryptoConfig>referenceWithInitializer(CryptoConfig.class, () -> CryptoConfig.Default());
  public static dafny.TypeDescriptor<CryptoConfig> _typeDescriptor() {
    return (dafny.TypeDescriptor<CryptoConfig>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CryptoConfig theDefault = CryptoConfig.create();
  public static CryptoConfig Default() {
    return theDefault;
  }
  public static CryptoConfig create() {
    return new CryptoConfig();
  }
  public static CryptoConfig create_CryptoConfig() {
    return create();
  }
  public boolean is_CryptoConfig() { return true; }
  public static java.util.ArrayList<CryptoConfig> AllSingletonConstructors() {
    java.util.ArrayList<CryptoConfig> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new CryptoConfig());
    return singleton_iterator;
  }
}
