// Class AwsKmsDiscoveryKeyring
// Dafny class AwsKmsDiscoveryKeyring compiled into Java
package AwsKmsDiscoveryKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsDiscoveryKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public AwsKmsDiscoveryKeyring() {
    this._client = null;
    this._discoveryFilter = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>Default(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor());
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out5;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out5;
  }
  public void __ctor(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    (this)._client = client;
    (this)._discoveryFilter = discoveryFilter;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Encryption is not supported with a Discovery Keyring.")));
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _0_materials;
    _0_materials = (input).dtor_materials();
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _1_encryptedDataKeys;
    _1_encryptedDataKeys = (input).dtor_encryptedDataKeys();
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_suite;
    _2_suite = ((input).dtor_materials()).dtor_algorithmSuite();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _3_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_0_materials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    AwsKmsEncryptedDataKeyFilter _4_edkFilter;
    AwsKmsEncryptedDataKeyFilter _nw0 = new AwsKmsEncryptedDataKeyFilter();
    _nw0.__ctor((this).discoveryFilter());
    _4_edkFilter = _nw0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.Error>FilterWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_edkFilter, _1_encryptedDataKeys);
    _5_valueOrError1 = _out0;
    if ((_5_valueOrError1).IsFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _6_matchingEdks;
    _6_matchingEdks = (_5_valueOrError1).Extract(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    AwsKmsEncryptedDataKeyTransformer _7_edkTransform;
    AwsKmsEncryptedDataKeyTransformer _nw1 = new AwsKmsEncryptedDataKeyTransformer();
    _nw1.__ctor();
    _7_edkTransform = _nw1;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper> empty(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Constants_Compile.AwsKmsEdkHelper, software.amazon.cryptography.materialproviders.internaldafny.types.Error>DeterministicFlatMapWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), Constants_Compile.AwsKmsEdkHelper._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _7_edkTransform, _6_matchingEdks);
    _8_valueOrError2 = _out1;
    if ((_8_valueOrError2).IsFailure(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper> _9_edksToAttempt;
    _9_edksToAttempt = (_8_valueOrError2).Extract(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if ((((long) (_9_edksToAttempt).cardinalityInt()) == 0 ? 0 : 1) == 0) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _10_valueOrError3 = ErrorMessages_Compile.__default.IncorrectDataKeys((input).dtor_encryptedDataKeys(), ((input).dtor_materials()).dtor_algorithmSuite(), dafny.DafnySequence.asString(""));
      if ((_10_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_10_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _11_errorMessage;
      _11_errorMessage = (_10_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_11_errorMessage));
      return res;
    }
    AwsKmsEncryptedDataKeyDecryptor _12_decryptAction;
    AwsKmsEncryptedDataKeyDecryptor _nw2 = new AwsKmsEncryptedDataKeyDecryptor();
    _nw2.__ctor(_0_materials, (this).client(), (this).grantTokens());
    _12_decryptAction = _nw2;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _13_outcome;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _out2;
    _out2 = Actions_Compile.__default.<Constants_Compile.AwsKmsEdkHelper, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>ReduceToSuccess(Constants_Compile.AwsKmsEdkHelper._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _12_decryptAction, _9_edksToAttempt);
    _13_outcome = _out2;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _source0 = _13_outcome;
    if (_source0.is_Success()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _14___mcc_h0 = ((Wrappers_Compile.Result_Success<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>>)_source0)._value;
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _15_mat = _14___mcc_h0;
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_15_mat));
    } else {
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16___mcc_h1 = ((Wrappers_Compile.Result_Failure<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>>)_source0)._error;
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_errors = _16___mcc_h1;
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_17_errors, dafny.DafnySequence.asString("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")));
    }
    return res;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _discoveryFilter;
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter()
  {
    return this._discoveryFilter;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens()
  {
    return this._grantTokens;
  }
  private static final dafny.TypeDescriptor<AwsKmsDiscoveryKeyring> _TYPE = dafny.TypeDescriptor.<AwsKmsDiscoveryKeyring>referenceWithInitializer(AwsKmsDiscoveryKeyring.class, () -> (AwsKmsDiscoveryKeyring) null);
  public static dafny.TypeDescriptor<AwsKmsDiscoveryKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsDiscoveryKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring";
  }
}
