// Class ManifestOptions
// Dafny class ManifestOptions compiled into Java
package MplManifestOptions_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ManifestOptions {
  public ManifestOptions() {
  }
  private static final dafny.TypeDescriptor<ManifestOptions> _TYPE = dafny.TypeDescriptor.<ManifestOptions>referenceWithInitializer(ManifestOptions.class, () -> ManifestOptions.Default());
  public static dafny.TypeDescriptor<ManifestOptions> _typeDescriptor() {
    return (dafny.TypeDescriptor<ManifestOptions>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ManifestOptions theDefault = ManifestOptions.create_Decrypt(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ManifestOptions Default() {
    return theDefault;
  }
  public static ManifestOptions create_Decrypt(dafny.DafnySequence<? extends Character> manifestPath, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> testName) {
    return new ManifestOptions_Decrypt(manifestPath, testName);
  }
  public static ManifestOptions create_Encrypt(dafny.DafnySequence<? extends Character> manifestPath, dafny.DafnySequence<? extends Character> decryptManifestOutput, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> testName) {
    return new ManifestOptions_Encrypt(manifestPath, decryptManifestOutput, testName);
  }
  public static ManifestOptions create_EncryptManifest(dafny.DafnySequence<? extends Character> encryptManifestOutput) {
    return new ManifestOptions_EncryptManifest(encryptManifestOutput);
  }
  public boolean is_Decrypt() { return this instanceof ManifestOptions_Decrypt; }
  public boolean is_Encrypt() { return this instanceof ManifestOptions_Encrypt; }
  public boolean is_EncryptManifest() { return this instanceof ManifestOptions_EncryptManifest; }
  public dafny.DafnySequence<? extends Character> dtor_manifestPath() {
    ManifestOptions d = this;
    if (d instanceof ManifestOptions_Decrypt) { return ((ManifestOptions_Decrypt)d)._manifestPath; }
    return ((ManifestOptions_Encrypt)d)._manifestPath;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_testName() {
    ManifestOptions d = this;
    if (d instanceof ManifestOptions_Decrypt) { return ((ManifestOptions_Decrypt)d)._testName; }
    return ((ManifestOptions_Encrypt)d)._testName;
  }
  public dafny.DafnySequence<? extends Character> dtor_decryptManifestOutput() {
    ManifestOptions d = this;
    return ((ManifestOptions_Encrypt)d)._decryptManifestOutput;
  }
  public dafny.DafnySequence<? extends Character> dtor_encryptManifestOutput() {
    ManifestOptions d = this;
    return ((ManifestOptions_EncryptManifest)d)._encryptManifestOutput;
  }
}
