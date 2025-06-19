// Class DecryptSingleAWSRSAEncryptedDataKey
// Dafny class DecryptSingleAWSRSAEncryptedDataKey compiled into Java
package AwsKmsRsaKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptSingleAWSRSAEncryptedDataKey implements Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public DecryptSingleAWSRSAEncryptedDataKey() {
    this._materials = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials)null;
    this._client = null;
    this._awsKmsKey = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    this._paddingScheme = software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.Default();
    this._encryptionContextDigest = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends Character> awsKmsKey, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme, dafny.DafnySequence<? extends java.lang.Byte> encryptionContextDigest, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    (this)._materials = materials;
    (this)._client = client;
    (this)._awsKmsKey = awsKmsKey;
    (this)._paddingScheme = paddingScheme;
    (this)._encryptionContextDigest = encryptionContextDigest;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    KmsRsaUnwrapKeyMaterial _0_unwrap;
    KmsRsaUnwrapKeyMaterial _nw0 = new KmsRsaUnwrapKeyMaterial();
    _nw0.__ctor((this).client(), (this).awsKmsKey(), (this).paddingScheme(), (this).encryptionContextDigest(), (this).grantTokens());
    _0_unwrap = _nw0;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<EdkWrapping_Compile.UnwrapEdkMaterialOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<KmsRsaUnwrapInfo>Default(KmsRsaUnwrapInfo._typeDescriptor(), KmsRsaUnwrapInfo.Default()));
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = EdkWrapping_Compile.__default.<KmsRsaUnwrapInfo>UnwrapEdkMaterial(KmsRsaUnwrapInfo._typeDescriptor(), (edk).dtor_ciphertext(), (this).materials(), _0_unwrap);
    _1_valueOrError0 = _out0;
    if ((_1_valueOrError0).IsFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    EdkWrapping_Compile.UnwrapEdkMaterialOutput<KmsRsaUnwrapInfo> _2_unwrapOutput;
    _2_unwrapOutput = (_1_valueOrError0).Extract(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _3_valueOrError1 = Materials_Compile.__default.DecryptionMaterialsAddDataKey((this).materials(), (_2_unwrapOutput).dtor_plaintextDataKey(), (_2_unwrapOutput).dtor_symmetricSigningKey());
    if ((_3_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _4_result;
    _4_result = (_3_valueOrError1).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_result);
    return res;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _materials;
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials()
  {
    return this._materials;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
  }
  public dafny.DafnySequence<? extends Character> _awsKmsKey;
  public dafny.DafnySequence<? extends Character> awsKmsKey()
  {
    return this._awsKmsKey;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _paddingScheme;
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme()
  {
    return this._paddingScheme;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _encryptionContextDigest;
  public dafny.DafnySequence<? extends java.lang.Byte> encryptionContextDigest()
  {
    return this._encryptionContextDigest;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens()
  {
    return this._grantTokens;
  }
  private static final dafny.TypeDescriptor<DecryptSingleAWSRSAEncryptedDataKey> _TYPE = dafny.TypeDescriptor.<DecryptSingleAWSRSAEncryptedDataKey>referenceWithInitializer(DecryptSingleAWSRSAEncryptedDataKey.class, () -> (DecryptSingleAWSRSAEncryptedDataKey) null);
  public static dafny.TypeDescriptor<DecryptSingleAWSRSAEncryptedDataKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptSingleAWSRSAEncryptedDataKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsRsaKeyring.DecryptSingleAWSRSAEncryptedDataKey";
  }
}
