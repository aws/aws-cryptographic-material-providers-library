// Class StaticMaterialsKeyring
// Dafny class StaticMaterialsKeyring compiled into Java
package CreateStaticKeyrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class StaticMaterialsKeyring implements software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public StaticMaterialsKeyring() {
    this._encryptMaterial = (software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)null;
    this._decryptMaterial = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials)null;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out0;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out0;
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials decryptMaterial)
  {
    (this)._encryptMaterial = encryptMaterial;
    (this)._decryptMaterial = decryptMaterial;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create((this).encryptMaterial()));
    return res;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create((this).decryptMaterial()));
    return res;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _encryptMaterial;
  public software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptMaterial()
  {
    return this._encryptMaterial;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _decryptMaterial;
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials decryptMaterial()
  {
    return this._decryptMaterial;
  }
  private static final dafny.TypeDescriptor<StaticMaterialsKeyring> _TYPE = dafny.TypeDescriptor.<StaticMaterialsKeyring>referenceWithInitializer(StaticMaterialsKeyring.class, () -> (StaticMaterialsKeyring) null);
  public static dafny.TypeDescriptor<StaticMaterialsKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<StaticMaterialsKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "CreateStaticKeyrings.StaticMaterialsKeyring";
  }
}
