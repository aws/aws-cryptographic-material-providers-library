// Class OnDecryptMrkAwareEncryptedDataKeyFilter
// Dafny class OnDecryptMrkAwareEncryptedDataKeyFilter compiled into Java
package AwsKmsUtils_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class OnDecryptMrkAwareEncryptedDataKeyFilter implements Actions_Compile.DeterministicActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.DeterministicAction<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public OnDecryptMrkAwareEncryptedDataKeyFilter() {
    this._awsKmsKey = (AwsArnParsing_Compile.AwsKmsIdentifier)null;
    this._providerId = UTF8.ValidUTF8Bytes.defaultValue();
  }
  public void __ctor(AwsArnParsing_Compile.AwsKmsIdentifier awsKmsKey, dafny.DafnySequence<? extends java.lang.Byte> providerId)
  {
    (this)._awsKmsKey = awsKmsKey;
    (this)._providerId = providerId;
  }
  public Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    if (!((edk).dtor_keyProviderId()).equals((this).providerId())) {
      res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
      return res;
    }
    if (!(UTF8.__default.ValidUTF8Seq((edk).dtor_keyProviderInfo()))) {
      res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid AWS KMS encoding, provider info is not UTF8.")));
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _0_valueOrError0 = (UTF8.__default.Decode((edk).dtor_keyProviderInfo())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default::WrapStringToError);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<Boolean>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
      return res;
    }
    dafny.DafnySequence<? extends Character> _1_keyId;
    _1_keyId = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _2_valueOrError1 = (AwsArnParsing_Compile.__default.ParseAwsKmsArn(_1_keyId)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default::WrapStringToError);
    if ((_2_valueOrError1).IsFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError1).<Boolean>PropagateFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
      return res;
    }
    AwsArnParsing_Compile.AwsArn _3_arn;
    _3_arn = (_2_valueOrError1).Extract(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsMrkMatchForDecrypt_Compile.__default.AwsKmsMrkMatchForDecrypt((this).awsKmsKey(), AwsArnParsing_Compile.AwsKmsIdentifier.create_AwsKmsArnIdentifier(_3_arn)));
    return res;
  }
  public AwsArnParsing_Compile.AwsKmsIdentifier _awsKmsKey;
  public AwsArnParsing_Compile.AwsKmsIdentifier awsKmsKey()
  {
    return this._awsKmsKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _providerId;
  public dafny.DafnySequence<? extends java.lang.Byte> providerId()
  {
    return this._providerId;
  }
  private static final dafny.TypeDescriptor<OnDecryptMrkAwareEncryptedDataKeyFilter> _TYPE = dafny.TypeDescriptor.<OnDecryptMrkAwareEncryptedDataKeyFilter>referenceWithInitializer(OnDecryptMrkAwareEncryptedDataKeyFilter.class, () -> (OnDecryptMrkAwareEncryptedDataKeyFilter) null);
  public static dafny.TypeDescriptor<OnDecryptMrkAwareEncryptedDataKeyFilter> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDecryptMrkAwareEncryptedDataKeyFilter>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter";
  }
}
