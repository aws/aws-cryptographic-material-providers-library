// Class KeyVectorsConfig
// Dafny class KeyVectorsConfig compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyVectorsConfig {
  public dafny.DafnySequence<? extends Character> _keyManifestPath;
  public KeyVectorsConfig (dafny.DafnySequence<? extends Character> keyManifestPath) {
    this._keyManifestPath = keyManifestPath;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyVectorsConfig o = (KeyVectorsConfig)other;
    return true && java.util.Objects.equals(this._keyManifestPath, o._keyManifestPath);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyManifestPath);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig.KeyVectorsConfig");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyManifestPath));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyVectorsConfig> _TYPE = dafny.TypeDescriptor.<KeyVectorsConfig>referenceWithInitializer(KeyVectorsConfig.class, () -> KeyVectorsConfig.Default());
  public static dafny.TypeDescriptor<KeyVectorsConfig> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyVectorsConfig>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyVectorsConfig theDefault = KeyVectorsConfig.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KeyVectorsConfig Default() {
    return theDefault;
  }
  public static KeyVectorsConfig create(dafny.DafnySequence<? extends Character> keyManifestPath) {
    return new KeyVectorsConfig(keyManifestPath);
  }
  public static KeyVectorsConfig create_KeyVectorsConfig(dafny.DafnySequence<? extends Character> keyManifestPath) {
    return create(keyManifestPath);
  }
  public boolean is_KeyVectorsConfig() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyManifestPath() {
    return this._keyManifestPath;
  }
}
