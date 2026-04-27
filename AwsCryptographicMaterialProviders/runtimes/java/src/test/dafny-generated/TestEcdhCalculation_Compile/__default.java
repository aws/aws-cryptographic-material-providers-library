// Class __default
// Dafny class __default compiled into Java
package TestEcdhCalculation_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestKmsDeriveSharedSecretOfflineCalculation()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(32,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(33,22): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _3_primitives;
    _3_primitives = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = (_3_primitives).GenerateECCKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput.create(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256()));
    _4_valueOrError2 = _out2;
    if (!(!((_4_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(35,19): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput _5_keyPair;
    _5_keyPair = (_4_valueOrError2).Extract(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    if (!(((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((((_5_keyPair).dtor_publicKey()).dtor_der()).length())) <= 0) && ((java.math.BigInteger.valueOf((((_5_keyPair).dtor_publicKey()).dtor_der()).length())).compareTo(java.math.BigInteger.valueOf(8192L)) <= 0))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(41,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _6_kmsSharedSecret;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out3;
    _out3 = (_1_kmsClient).DeriveSharedSecret(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretRequest.create(__default.senderKmsKey(), software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec.create(), ((_5_keyPair).dtor_publicKey()).dtor_der(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor())));
    _6_kmsSharedSecret = _out3;
    if (!((_6_kmsSharedSecret).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(50,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_6_kmsSharedSecret).dtor_value()).dtor_SharedSecret()).is_Some())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(51,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _7_publicKeyResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out4;
    _out4 = (_1_kmsClient).GetPublicKey(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(__default.senderKmsKey(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor())));
    _7_publicKeyResponse = _out4;
    if (!((_7_publicKeyResponse).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(59,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse _let_tmp_rhs0 = (_7_publicKeyResponse).dtor_value();
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _8___v0 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyId;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _9_PublicKey = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._PublicKey;
    Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec> _10___v1 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._CustomerMasterKeySpec;
    Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeySpec> _11___v2 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeySpec;
    Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType> _12___v3 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyUsage;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>> _13___v4 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._EncryptionAlgorithms;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec>> _14___v5 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._SigningAlgorithms;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec>> _15___v6 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyAgreementAlgorithms;
    if (!((_9_PublicKey).is_Some())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(62,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _16_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out5;
    _out5 = (_3_primitives).DeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput.create(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256(), (_5_keyPair).dtor_privateKey(), software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create((_9_PublicKey).dtor_value())));
    _16_valueOrError3 = _out5;
    if (!(!((_16_valueOrError3).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(64,31): " + java.lang.String.valueOf(_16_valueOrError3));
    }
    software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput _17_offlineSharedSecret;
    _17_offlineSharedSecret = (_16_valueOrError3).Extract(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    if (!(((((_6_kmsSharedSecret).dtor_value()).dtor_SharedSecret()).dtor_value()).equals((_17_offlineSharedSecret).dtor_sharedSecret()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(72,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestKmsDeriveSharedSecretOfflineCalculationCurves()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(77,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(78,22): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _3_primitives;
    _3_primitives = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((__default.senderArns()).length());
    for (java.math.BigInteger _4_i = java.math.BigInteger.ZERO; _4_i.compareTo(_hi0) < 0; _4_i = _4_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _5_valueOrError2 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
      _out2 = (_3_primitives).GenerateECCKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput.create(((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((__default.curveSpecs()).select(dafny.Helpers.toInt((_4_i)))))));
      _5_valueOrError2 = _out2;
      if (!(!((_5_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(82,21): " + java.lang.String.valueOf(_5_valueOrError2));
      }
      software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput _6_keyPair;
      _6_keyPair = (_5_valueOrError2).Extract(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      if (!(((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((((_6_keyPair).dtor_publicKey()).dtor_der()).length())) <= 0) && ((java.math.BigInteger.valueOf((((_6_keyPair).dtor_publicKey()).dtor_der()).length())).compareTo(java.math.BigInteger.valueOf(8192L)) <= 0))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(87,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _7_kmsSharedSecret;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out3;
      _out3 = (_1_kmsClient).DeriveSharedSecret(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretRequest.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.senderArns()).select(dafny.Helpers.toInt((_4_i))))), software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec.create(), ((_6_keyPair).dtor_publicKey()).dtor_der(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor())));
      _7_kmsSharedSecret = _out3;
      if (!((_7_kmsSharedSecret).is_Success())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(96,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      if (!((((_7_kmsSharedSecret).dtor_value()).dtor_SharedSecret()).is_Some())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(97,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_publicKeyResponse;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out4;
      _out4 = (_1_kmsClient).GetPublicKey(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.senderArns()).select(dafny.Helpers.toInt((_4_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor())));
      _8_publicKeyResponse = _out4;
      if (!((_8_publicKeyResponse).is_Success())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(105,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse _let_tmp_rhs0 = (_8_publicKeyResponse).dtor_value();
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _9___v7 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyId;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _10_PublicKey = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._PublicKey;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec> _11___v8 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._CustomerMasterKeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeySpec> _12___v9 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType> _13___v10 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyUsage;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>> _14___v11 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._EncryptionAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec>> _15___v12 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._SigningAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec>> _16___v13 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyAgreementAlgorithms;
      if (!((_10_PublicKey).is_Some())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(108,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _17_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out5;
      _out5 = (_3_primitives).DeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput.create(((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((__default.curveSpecs()).select(dafny.Helpers.toInt((_4_i))))), (_6_keyPair).dtor_privateKey(), software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create((_10_PublicKey).dtor_value())));
      _17_valueOrError3 = _out5;
      if (!(!((_17_valueOrError3).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(110,33): " + java.lang.String.valueOf(_17_valueOrError3));
      }
      software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput _18_offlineSharedSecret;
      _18_offlineSharedSecret = (_17_valueOrError3).Extract(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      if (!(((((_7_kmsSharedSecret).dtor_value()).dtor_SharedSecret()).dtor_value()).equals((_18_offlineSharedSecret).dtor_sharedSecret()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(118,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    }
  }
  public static void TestOfflineDeriveSharedSecretStaticKeys()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(125,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(126,22): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _3_primitives;
    _3_primitives = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((__default.curveSpecs()).length());
    for (java.math.BigInteger _4_i = java.math.BigInteger.ZERO; _4_i.compareTo(_hi0) < 0; _4_i = _4_i.add(java.math.BigInteger.ONE)) {
      software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _5_curve;
      _5_curve = ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((__default.curveSpecs()).select(dafny.Helpers.toInt((_4_i)))));
      dafny.DafnySequence<? extends Character> _6_senderArn;
      _6_senderArn = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.senderArns()).select(dafny.Helpers.toInt((_4_i)))));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _7_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _7_valueOrError2 = Base64_Compile.__default.Decode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.senderArnPublicKeys()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_7_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(132,29): " + java.lang.String.valueOf(_7_valueOrError2));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _8_senderPublicKey;
      _8_senderPublicKey = (_7_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _9_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
      _9_valueOrError3 = UTF8.__default.Encode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.privateKeyReceivers()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_9_valueOrError3).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(133,33): " + java.lang.String.valueOf(_9_valueOrError3));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _10_recipientPrivateKey;
      _10_recipientPrivateKey = (_9_valueOrError3).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _11_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _11_valueOrError4 = Base64_Compile.__default.Decode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.publicKeyReceivers()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_11_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(134,32): " + java.lang.String.valueOf(_11_valueOrError4));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _12_recipientPublicKey;
      _12_recipientPublicKey = (_11_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _13_kmsSharedSecret;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
      _out2 = (_1_kmsClient).DeriveSharedSecret(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretRequest.create(_6_senderArn, software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec.create(), _12_recipientPublicKey, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor())));
      _13_kmsSharedSecret = _out2;
      if (!((_13_kmsSharedSecret).is_Success())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(143,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      if (!((((_13_kmsSharedSecret).dtor_value()).dtor_SharedSecret()).is_Some())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(144,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _14_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out3;
      _out3 = (_3_primitives).DeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput.create(((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((__default.curveSpecs()).select(dafny.Helpers.toInt((_4_i))))), software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.create(_10_recipientPrivateKey), software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_8_senderPublicKey)));
      _14_valueOrError5 = _out3;
      if (!(!((_14_valueOrError5).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(146,33): " + java.lang.String.valueOf(_14_valueOrError5));
      }
      software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput _15_offlineSharedSecret;
      _15_offlineSharedSecret = (_14_valueOrError5).Extract(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      if (!(((((_13_kmsSharedSecret).dtor_value()).dtor_SharedSecret()).dtor_value()).equals((_15_offlineSharedSecret).dtor_sharedSecret()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(155,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> senderKmsKey()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9");
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> senderArns()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__S());
  }
  public static dafny.DafnySequence<? extends software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> curveSpecs()
  {
    return dafny.DafnySequence.<software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> of(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P384(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P521());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> senderArnPublicKeys()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__PUBLIC__KEY__S(), TestUtils_Compile.__default.KMS__ECC__384__PUBLIC__KEY__S(), TestUtils_Compile.__default.KMS__ECC__521__PUBLIC__KEY__S());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> privateKeyReceivers()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.ECC__P256__PRIVATE(), TestUtils_Compile.__default.ECC__P384__PRIVATE(), TestUtils_Compile.__default.ECC__P521__PRIVATE());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> publicKeyReceivers()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.ECC__P256__PUBLIC(), TestUtils_Compile.__default.ECC__P384__PUBLIC(), TestUtils_Compile.__default.ECC__P521__PUBLIC());
  }
  public static dafny.DafnySequence<? extends Character> recipientKmsKey()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5");
  }
  @Override
  public java.lang.String toString() {
    return "TestEcdhCalculation._default";
  }
}
