// Class KeyStoreClient
// Dafny class KeyStoreClient compiled into Java
package software.amazon.cryptography.keystore.internaldafny;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyStoreClient implements software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient {
  public KeyStoreClient() {
    this._config = (AwsCryptographyKeyStoreOperations_Compile.Config)null;
  }
  public void __ctor(AwsCryptographyKeyStoreOperations_Compile.Config config)
  {
    (this)._config = config;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetKeyStoreInfo()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyKeyStoreOperations_Compile.__default.GetKeyStoreInfo((this).config());
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateKeyStore(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyKeyStoreOperations_Compile.__default.CreateKeyStore((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyKeyStoreOperations_Compile.__default.CreateKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> VersionKey(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyKeyStoreOperations_Compile.__default.VersionKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyKeyStoreOperations_Compile.__default.GetActiveBranchKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyKeyStoreOperations_Compile.__default.GetBranchKeyVersion((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyKeyStoreOperations_Compile.__default.GetBeaconKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public AwsCryptographyKeyStoreOperations_Compile.Config _config;
  public AwsCryptographyKeyStoreOperations_Compile.Config config()
  {
    return this._config;
  }
  private static final dafny.TypeDescriptor<KeyStoreClient> _TYPE = dafny.TypeDescriptor.<KeyStoreClient>referenceWithInitializer(KeyStoreClient.class, () -> (KeyStoreClient) null);
  public static dafny.TypeDescriptor<KeyStoreClient> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyStoreClient>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "KeyStore.KeyStoreClient";
  }
}
