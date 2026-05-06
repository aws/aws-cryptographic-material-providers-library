// Class KeyVectorsClient
// Dafny class KeyVectorsClient compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyVectorsClient implements software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient {
  public KeyVectorsClient() {
    this._config = KeysVectorOperations_Compile.Config.Default();
  }
  public void __ctor(KeysVectorOperations_Compile.Config config)
  {
    (this)._config = config;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> CreateTestVectorKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out0;
      _out0 = KeysVectorOperations_Compile.__default.CreateTestVectorKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> CreateWrappedTestVectorKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out0;
      _out0 = KeysVectorOperations_Compile.__default.CreateWrappedTestVectorKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> CreateWrappedTestVectorCmm(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorCmmInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out0;
      _out0 = KeysVectorOperations_Compile.__default.CreateWrappedTestVectorCmm((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionOutput, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> GetKeyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionInput input) {
    return KeysVectorOperations_Compile.__default.GetKeyDescription((this).config(), input);
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionOutput, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> SerializeKeyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionInput input) {
    return KeysVectorOperations_Compile.__default.SerializeKeyDescription((this).config(), input);
  }
  public KeysVectorOperations_Compile.Config _config;
  public KeysVectorOperations_Compile.Config config()
  {
    return this._config;
  }
  private static final dafny.TypeDescriptor<KeyVectorsClient> _TYPE = dafny.TypeDescriptor.<KeyVectorsClient>referenceWithInitializer(KeyVectorsClient.class, () -> (KeyVectorsClient) null);
  public static dafny.TypeDescriptor<KeyVectorsClient> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyVectorsClient>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "KeyVectors.KeyVectorsClient";
  }
}
