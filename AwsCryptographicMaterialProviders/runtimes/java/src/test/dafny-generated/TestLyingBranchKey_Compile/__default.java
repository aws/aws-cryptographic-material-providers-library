// Class __default
// Dafny class __default compiled into Java
package TestLyingBranchKey_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestGetActiveKeyForLyingBranchKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(26,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(27,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.postalHornKeyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(38,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_result;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create(Fixtures_Compile.__default.lyingBranchKeyId()));
    _8_result = _out3;
    if (!((_8_result).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(44,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source0 = (_8_result).dtor_error();
    if (_source0.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _9___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(48,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _10___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source0)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(48,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _11___mcc_h4 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      software.amazon.cryptography.services.kms.internaldafny.types.Error _12_nestedError = _11___mcc_h4;
      if (!((_12_nestedError).is_IncorrectKeyException())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(47,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _13___mcc_h6 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _14___mcc_h7 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(48,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_Opaque()) {
      Object _15___mcc_h10 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source0)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(48,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else {
      Object _16___mcc_h12 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _17___mcc_h13 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(48,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    }
  }
  public static void TestGetBranchKeyVersionForLyingBranchKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(53,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(54,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.postalHornKeyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(65,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_result;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create(Fixtures_Compile.__default.lyingBranchKeyId(), Fixtures_Compile.__default.lyingBranchKeyDecryptOnlyVersion()));
    _8_result = _out3;
    if (!((_8_result).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(72,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source0 = (_8_result).dtor_error();
    if (_source0.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _9___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(76,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _10___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source0)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(76,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _11___mcc_h4 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      software.amazon.cryptography.services.kms.internaldafny.types.Error _12_nestedError = _11___mcc_h4;
      if (!((_12_nestedError).is_IncorrectKeyException())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(75,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _13___mcc_h6 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _14___mcc_h7 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(76,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_Opaque()) {
      Object _15___mcc_h10 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source0)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(76,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else {
      Object _16___mcc_h12 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _17___mcc_h13 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(76,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    }
  }
  public static void TestGetBeaconKeyForLyingBranchKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(81,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(82,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.postalHornKeyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(93,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_result;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create(Fixtures_Compile.__default.lyingBranchKeyId()));
    _8_result = _out3;
    if (!((_8_result).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(99,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source0 = (_8_result).dtor_error();
    if (_source0.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _9___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(103,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _10___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source0)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(103,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _11___mcc_h4 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      software.amazon.cryptography.services.kms.internaldafny.types.Error _12_nestedError = _11___mcc_h4;
      if (!((_12_nestedError).is_IncorrectKeyException())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(102,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _13___mcc_h6 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _14___mcc_h7 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(103,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_Opaque()) {
      Object _15___mcc_h10 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source0)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(103,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else {
      Object _16___mcc_h12 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _17___mcc_h13 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(103,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    }
  }
  public static void TestVersionKeyForLyingBranchKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(108,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(109,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.postalHornKeyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(120,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_result;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).VersionKey(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput.create(Fixtures_Compile.__default.lyingBranchKeyId()));
    _8_result = _out3;
    if (!((_8_result).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(126,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source0 = (_8_result).dtor_error();
    if (_source0.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _9___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(130,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _10___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source0)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(130,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _11___mcc_h4 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      software.amazon.cryptography.services.kms.internaldafny.types.Error _12_nestedError = _11___mcc_h4;
      if (!((_12_nestedError).is_IncorrectKeyException())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(129,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _13___mcc_h6 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _14___mcc_h7 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(130,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_Opaque()) {
      Object _15___mcc_h10 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source0)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(130,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else {
      Object _16___mcc_h12 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _17___mcc_h13 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(130,16): " + (dafny.DafnySequence.asString("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")).verbatimString());
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestLyingBranchKey._default";
  }
}
