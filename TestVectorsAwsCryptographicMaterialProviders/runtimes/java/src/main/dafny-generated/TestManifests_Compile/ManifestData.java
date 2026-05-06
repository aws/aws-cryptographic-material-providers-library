// Class ManifestData
// Dafny class ManifestData compiled into Java
package TestManifests_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ManifestData {
  public ManifestData() {
  }
  private static final dafny.TypeDescriptor<ManifestData> _TYPE = dafny.TypeDescriptor.<ManifestData>referenceWithInitializer(ManifestData.class, () -> ManifestData.Default());
  public static dafny.TypeDescriptor<ManifestData> _typeDescriptor() {
    return (dafny.TypeDescriptor<ManifestData>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ManifestData theDefault = ManifestData.create_DecryptManifest(java.math.BigInteger.ZERO, null, JSON_mValues_Compile.JSON.Default(), dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> empty(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())));
  public static ManifestData Default() {
    return theDefault;
  }
  public static ManifestData create_DecryptManifest(java.math.BigInteger version, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, JSON_mValues_Compile.JSON client, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> jsonTests) {
    return new ManifestData_DecryptManifest(version, keys, client, jsonTests);
  }
  public static ManifestData create_EncryptManifest(java.math.BigInteger version, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> jsonTests) {
    return new ManifestData_EncryptManifest(version, keys, jsonTests);
  }
  public boolean is_DecryptManifest() { return this instanceof ManifestData_DecryptManifest; }
  public boolean is_EncryptManifest() { return this instanceof ManifestData_EncryptManifest; }
  public java.math.BigInteger dtor_version() {
    ManifestData d = this;
    if (d instanceof ManifestData_DecryptManifest) { return ((ManifestData_DecryptManifest)d)._version; }
    return ((ManifestData_EncryptManifest)d)._version;
  }
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient dtor_keys() {
    ManifestData d = this;
    if (d instanceof ManifestData_DecryptManifest) { return ((ManifestData_DecryptManifest)d)._keys; }
    return ((ManifestData_EncryptManifest)d)._keys;
  }
  public JSON_mValues_Compile.JSON dtor_client() {
    ManifestData d = this;
    return ((ManifestData_DecryptManifest)d)._client;
  }
  public dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> dtor_jsonTests() {
    ManifestData d = this;
    if (d instanceof ManifestData_DecryptManifest) { return ((ManifestData_DecryptManifest)d)._jsonTests; }
    return ((ManifestData_EncryptManifest)d)._jsonTests;
  }
}
