// Class AwsKmsMrkDiscoveryKeyring
// Dafny class AwsKmsMrkDiscoveryKeyring compiled into Java
package AwsKmsMrkDiscoveryKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsMrkDiscoveryKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public AwsKmsMrkDiscoveryKeyring() {
    this._client = null;
    this._region = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    this._discoveryFilter = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>Default(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor());
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out8;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out8;
  }
  public void __ctor(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends Character> region, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    (this)._client = client;
    (this)._region = region;
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _0_materials;
    _0_materials = (input).dtor_materials();
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _1_encryptedDataKeys;
    _1_encryptedDataKeys = (input).dtor_encryptedDataKeys();
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_suite;
    _2_suite = ((input).dtor_materials()).dtor_algorithmSuite();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _3_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_0_materials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_3_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    AwsKmsEncryptedDataKeyFilterTransform _4_edkFilterTransform;
    AwsKmsEncryptedDataKeyFilterTransform _nw0 = new AwsKmsEncryptedDataKeyFilterTransform();
    _nw0.__ctor((this).region(), (this).discoveryFilter());
    _4_edkFilterTransform = _nw0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper> empty(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Constants_Compile.AwsKmsEdkHelper, software.amazon.cryptography.materialproviders.internaldafny.types.Error>DeterministicFlatMapWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), Constants_Compile.AwsKmsEdkHelper._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_edkFilterTransform, _1_encryptedDataKeys);
    _5_valueOrError1 = _out0;
    if ((_5_valueOrError1).IsFailure(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper> _6_edksToAttempt;
    _6_edksToAttempt = (_5_valueOrError1).Extract(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if ((((long) (_6_edksToAttempt).cardinalityInt()) == 0 ? 0 : 1) == 0) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _7_valueOrError2 = ErrorMessages_Compile.__default.IncorrectDataKeys((input).dtor_encryptedDataKeys(), ((input).dtor_materials()).dtor_algorithmSuite(), dafny.DafnySequence.asString(""));
      if ((_7_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends Character> _8_errorMessage;
      _8_errorMessage = (_7_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_8_errorMessage));
      return output;
    }
    AwsKmsEncryptedDataKeyDecryptor _9_decryptAction;
    AwsKmsEncryptedDataKeyDecryptor _nw1 = new AwsKmsEncryptedDataKeyDecryptor();
    _nw1.__ctor(_0_materials, (this).client(), (this).region(), (this).grantTokens());
    _9_decryptAction = _nw1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _10_outcome;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _out1;
    _out1 = Actions_Compile.__default.<Constants_Compile.AwsKmsEdkHelper, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>ReduceToSuccess(Constants_Compile.AwsKmsEdkHelper._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _9_decryptAction, _6_edksToAttempt);
    _10_outcome = _out1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _source0 = _10_outcome;
    if (_source0.is_Success()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _11___mcc_h0 = ((Wrappers_Compile.Result_Success<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>>)_source0)._value;
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _12_mat = _11___mcc_h0;
      output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_12_mat));
    } else {
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13___mcc_h1 = ((Wrappers_Compile.Result_Failure<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>>)_source0)._error;
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_errors = _13___mcc_h1;
      output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_14_errors, dafny.DafnySequence.asString("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")));
    }
    return output;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
  }
  public dafny.DafnySequence<? extends Character> _region;
  public dafny.DafnySequence<? extends Character> region()
  {
    return this._region;
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
  private static final dafny.TypeDescriptor<AwsKmsMrkDiscoveryKeyring> _TYPE = dafny.TypeDescriptor.<AwsKmsMrkDiscoveryKeyring>referenceWithInitializer(AwsKmsMrkDiscoveryKeyring.class, () -> (AwsKmsMrkDiscoveryKeyring) null);
  public static dafny.TypeDescriptor<AwsKmsMrkDiscoveryKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsMrkDiscoveryKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring";
  }
}
