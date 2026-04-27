// Class StaticKeyStore
// Dafny class StaticKeyStore compiled into Java
package CreateStaticKeyStores_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class StaticKeyStore implements software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient {
  public StaticKeyStore() {
    this._staticKeyMaterial = KeyMaterial_Compile.KeyMaterial.Default();
  }
  public void __ctor(KeyMaterial_Compile.KeyMaterial staticKeyMaterial)
  {
    (this)._staticKeyMaterial = staticKeyMaterial;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.create(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.create((input).dtor_branchKeyIdentifier(), ((this).staticKeyMaterial()).dtor_branchKeyVersion(), dafny.DafnyMap.fromElements(), ((this).staticKeyMaterial()).dtor_branchKey())));
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.create(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.create((input).dtor_branchKeyIdentifier(), ((this).staticKeyMaterial()).dtor_branchKeyVersion(), dafny.DafnyMap.fromElements(), ((this).staticKeyMaterial()).dtor_branchKey())));
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.create(software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials.create((input).dtor_branchKeyIdentifier(), dafny.DafnyMap.fromElements(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((this).staticKeyMaterial()).dtor_beaconKey()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))))));
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetKeyStoreInfo()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput.create(dafny.DafnySequence.asString("key-store-id"), dafny.DafnySequence.asString("key-store-name"), dafny.DafnySequence.asString("logical-key-store-name"), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(dafny.DafnySequence.asString("arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"))));
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateKeyStore(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Failure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Not Supported")));
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Failure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Not Supported")));
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> VersionKey(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.Default());
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Failure(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Not Supported")));
    }
    return output;
  }
  public KeyMaterial_Compile.KeyMaterial _staticKeyMaterial;
  public KeyMaterial_Compile.KeyMaterial staticKeyMaterial()
  {
    return this._staticKeyMaterial;
  }
  private static final dafny.TypeDescriptor<StaticKeyStore> _TYPE = dafny.TypeDescriptor.<StaticKeyStore>referenceWithInitializer(StaticKeyStore.class, () -> (StaticKeyStore) null);
  public static dafny.TypeDescriptor<StaticKeyStore> _typeDescriptor() {
    return (dafny.TypeDescriptor<StaticKeyStore>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "CreateStaticKeyStores.StaticKeyStore";
  }
}
