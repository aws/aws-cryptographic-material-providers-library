// Class __default
// Dafny class __default compiled into Java
package KMSKeystoreOperations_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> replaceRegion(dafny.DafnySequence<? extends Character> arn, dafny.DafnySequence<? extends Character> region)
  {
    Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>> _0_parsed = AwsArnParsing_Compile.__default.ParseAwsKmsArn(arn);
    if ((_0_parsed).is_Failure()) {
      return arn;
    } else if (!(AwsArnParsing_Compile.__default.IsMultiRegionAwsKmsArn((_0_parsed).dtor_value()))) {
      return arn;
    } else {
      dafny.DafnySequence<? extends Character> _1_newArn = ((_0_parsed).dtor_value()).ToArnString(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.RegionType._typeDescriptor(), region));
      if (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType(_1_newArn)) {
        return _1_newArn;
      } else {
        return arn;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> GetArn(software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends Character> discoverdArn)
  {
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _source0 = kmsConfiguration;
    if (_source0.is_kmsKeyArn()) {
      dafny.DafnySequence<? extends Character> _0___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsKeyArn)_source0)._kmsKeyArn;
      dafny.DafnySequence<? extends Character> _1_arn = _0___mcc_h0;
      return _1_arn;
    } else if (_source0.is_kmsMRKeyArn()) {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsMRKeyArn)_source0)._kmsMRKeyArn;
      dafny.DafnySequence<? extends Character> _3_arn = _2___mcc_h1;
      return _3_arn;
    } else if (_source0.is_discovery()) {
      software.amazon.cryptography.keystore.internaldafny.types.Discovery _4___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_discovery)_source0)._discovery;
      software.amazon.cryptography.keystore.internaldafny.types.Discovery _5_obj = _4___mcc_h2;
      return discoverdArn;
    } else {
      software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery _6___mcc_h3 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_mrDiscovery)_source0)._mrDiscovery;
      software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery _7_region = _6___mcc_h3;
      return __default.replaceRegion(discoverdArn, (_7_region).dtor_region());
    }
  }
  public static boolean AttemptKmsOperation_q(software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> encryptionContext)
  {
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _source0 = kmsConfiguration;
    if (_source0.is_kmsKeyArn()) {
      dafny.DafnySequence<? extends Character> _0___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsKeyArn)_source0)._kmsKeyArn;
      dafny.DafnySequence<? extends Character> _1_arn = _0___mcc_h0;
      return ((_1_arn).equals(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(Structure_Compile.__default.KMS__FIELD()))))) && (KmsArn_Compile.__default.ValidKmsArn_q(_1_arn));
    } else if (_source0.is_kmsMRKeyArn()) {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsMRKeyArn)_source0)._kmsMRKeyArn;
      dafny.DafnySequence<? extends Character> _3_arn = _2___mcc_h1;
      return (__default.MrkMatch(_3_arn, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(Structure_Compile.__default.KMS__FIELD()))))) && (KmsArn_Compile.__default.ValidKmsArn_q(_3_arn));
    } else if (_source0.is_discovery()) {
      software.amazon.cryptography.keystore.internaldafny.types.Discovery _4___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_discovery)_source0)._discovery;
      software.amazon.cryptography.keystore.internaldafny.types.Discovery _5_obj = _4___mcc_h2;
      return KmsArn_Compile.__default.ValidKmsArn_q(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(Structure_Compile.__default.KMS__FIELD()))));
    } else {
      software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery _6___mcc_h3 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_mrDiscovery)_source0)._mrDiscovery;
      software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery _7_obj = _6___mcc_h3;
      return KmsArn_Compile.__default.ValidKmsArn_q(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(Structure_Compile.__default.KMS__FIELD()))));
    }
  }
  public static boolean Compatible_q(software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends Character> keyId)
  {
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _source0 = kmsConfiguration;
    if (_source0.is_kmsKeyArn()) {
      dafny.DafnySequence<? extends Character> _0___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsKeyArn)_source0)._kmsKeyArn;
      dafny.DafnySequence<? extends Character> _1_arn = _0___mcc_h0;
      return (_1_arn).equals(keyId);
    } else {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsMRKeyArn)_source0)._kmsMRKeyArn;
      dafny.DafnySequence<? extends Character> _3_arn = _2___mcc_h1;
      return __default.MrkMatch(_3_arn, keyId);
    }
  }
  public static boolean OptCompatible_q(software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> keyId)
  {
    return ((keyId).is_Some()) && (__default.Compatible_q(kmsConfiguration, (keyId).dtor_value()));
  }
  public static boolean MrkMatch(dafny.DafnySequence<? extends Character> x, dafny.DafnySequence<? extends Character> y)
  {
    Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>> _0_xArn = AwsArnParsing_Compile.__default.ParseAwsKmsArn(x);
    Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>> _1_yArn = AwsArnParsing_Compile.__default.ParseAwsKmsArn(y);
    if (((_0_xArn).is_Failure()) || ((_1_yArn).is_Failure())) {
      return false;
    } else {
      return AwsKmsMrkMatchForDecrypt_Compile.__default.AwsKmsMrkMatchForDecrypt(AwsArnParsing_Compile.AwsKmsIdentifier.create_AwsKmsArnIdentifier((_0_xArn).dtor_value()), AwsArnParsing_Compile.AwsKmsIdentifier.create_AwsKmsArnIdentifier((_1_yArn).dtor_value()));
    }
  }
  public static boolean HasKeyId(software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration) {
    return ((kmsConfiguration).is_kmsKeyArn()) || ((kmsConfiguration).is_kmsMRKeyArn());
  }
  public static dafny.DafnySequence<? extends Character> GetKeyId(software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration) {
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _source0 = kmsConfiguration;
    if (_source0.is_kmsKeyArn()) {
      dafny.DafnySequence<? extends Character> _0___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsKeyArn)_source0)._kmsKeyArn;
      dafny.DafnySequence<? extends Character> _1_arn = _0___mcc_h0;
      return _1_arn;
    } else {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration_kmsMRKeyArn)_source0)._kmsMRKeyArn;
      dafny.DafnySequence<? extends Character> _3_arn = _2___mcc_h1;
      return _3_arn;
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> GenerateKey(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> encryptionContext, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> res = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse.Default());
    dafny.DafnySequence<? extends Character> _0_kmsKeyArn;
    _0_kmsKeyArn = __default.GetKeyId(kmsConfiguration);
    software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextRequest _1_generatorRequest;
    _1_generatorRequest = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextRequest.create(_0_kmsKeyArn, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(Structure_Compile.BranchKeyContext._typeDescriptor(), encryptionContext), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.DataKeySpec>create_None(software.amazon.cryptography.services.kms.internaldafny.types.DataKeySpec._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.NumberOfBytesType._typeDescriptor(), 32), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), grantTokens), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_maybeGenerateResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = (kmsClient).GenerateDataKeyWithoutPlaintext(_1_generatorRequest);
    _2_maybeGenerateResponse = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse.Default());
    _3_valueOrError0 = (_2_maybeGenerateResponse).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_4_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _4_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_4_e_boxed0));
      return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsKms(_4_e);
    }));
    if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError0).<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse _5_generateResponse;
    _5_generateResponse = (_3_valueOrError0).Extract(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (true) && (((_5_generateResponse).dtor_KeyId()).is_Some()), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid response from KMS GenerateDataKey:: Invalid Key Id")));
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError1).<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((_5_generateResponse).dtor_CiphertextBlob()).is_Some()) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__CiphertextType(((_5_generateResponse).dtor_CiphertextBlob()).dtor_value())), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")));
    if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError2).<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor());
      return res;
    }
    res = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), _5_generateResponse);
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> ReEncryptKey(dafny.DafnySequence<? extends java.lang.Byte> ciphertext, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> sourceEncryptionContext, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> destinationEncryptionContext, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> res = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse.Default());
    dafny.DafnySequence<? extends Character> _0_kmsKeyArn;
    _0_kmsKeyArn = __default.GetKeyId(kmsConfiguration);
    software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptRequest _1_reEncryptRequest;
    _1_reEncryptRequest = software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptRequest.create(ciphertext, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(Structure_Compile.BranchKeyContext._typeDescriptor(), sourceEncryptionContext), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.KeyIdType._typeDescriptor(), _0_kmsKeyArn), _0_kmsKeyArn, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(Structure_Compile.BranchKeyContext._typeDescriptor(), destinationEncryptionContext), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>create_None(software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>create_None(software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), grantTokens), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_maybeReEncryptResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = (kmsClient).ReEncrypt(_1_reEncryptRequest);
    _2_maybeReEncryptResponse = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse.Default());
    _3_valueOrError0 = (_2_maybeReEncryptResponse).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_4_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _4_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_4_e_boxed0));
      return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsKms(_4_e);
    }));
    if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError0).<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse _5_reEncryptResponse;
    _5_reEncryptResponse = (_3_valueOrError0).Extract(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((((_5_reEncryptResponse).dtor_SourceKeyId()).is_Some()) && (((_5_reEncryptResponse).dtor_KeyId()).is_Some())) && ((((_5_reEncryptResponse).dtor_SourceKeyId()).dtor_value()).equals(_0_kmsKeyArn))) && ((((_5_reEncryptResponse).dtor_KeyId()).dtor_value()).equals(_0_kmsKeyArn)), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid response from KMS ReEncrypt:: Invalid Key Id")));
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError1).<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((_5_reEncryptResponse).dtor_CiphertextBlob()).is_Some()) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__CiphertextType(((_5_reEncryptResponse).dtor_CiphertextBlob()).dtor_value())), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")));
    if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError2).<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor());
      return res;
    }
    res = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), _5_reEncryptResponse);
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> DecryptKey(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> encryptionContext, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> item, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.Default());
    if(true) {
      dafny.DafnySequence<? extends Character> _0_kmsKeyArn;
      _0_kmsKeyArn = __default.GetArn(kmsConfiguration, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(Structure_Compile.__default.KMS__FIELD()))));
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _1_maybeDecryptResponse;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
      _out0 = (kmsClient).Decrypt(software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest.create((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((item).get(Structure_Compile.__default.BRANCH__KEY__FIELD())))).dtor_B(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(Structure_Compile.BranchKeyContext._typeDescriptor(), encryptionContext), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), grantTokens), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.KeyIdType._typeDescriptor(), _0_kmsKeyArn), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>create_None(software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN)));
      _1_maybeDecryptResponse = _out0;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.Default());
      _2_valueOrError0 = (_1_maybeDecryptResponse).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_3_e_boxed0) -> {
        software.amazon.cryptography.services.kms.internaldafny.types.Error _3_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_3_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsKms(_3_e);
      }));
      if ((_2_valueOrError0).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_2_valueOrError0).<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse _4_decryptResponse;
      _4_decryptResponse = (_2_valueOrError0).Extract(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _5_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((_4_decryptResponse).dtor_Plaintext()).is_Some()) && (java.util.Objects.equals(java.math.BigInteger.valueOf(32L), java.math.BigInteger.valueOf((((_4_decryptResponse).dtor_Plaintext()).dtor_value()).length()))), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")));
      if ((_5_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_5_valueOrError1).<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor());
        return output;
      }
      output = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), _4_decryptResponse);
    }
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "KMSKeystoreOperations._default";
  }
}
