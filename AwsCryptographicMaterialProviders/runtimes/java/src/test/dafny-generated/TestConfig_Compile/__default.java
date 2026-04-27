// Class __default
// Dafny class __default compiled into Java
package TestConfig_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestInvalidKmsKeyArnConfig()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(19,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(20,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.keyId());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_keyStore;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_keyStore = _out2;
    if (!((_6_keyStore).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(34,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source0 = (_6_keyStore).dtor_error();
    if (_source0.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _7___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source0)._message;
      dafny.DafnySequence<? extends Character> _8_message = _7___mcc_h0;
      if (!((java.math.BigInteger.valueOf((_8_message).length())).compareTo(java.math.BigInteger.valueOf((KeyStoreErrorMessages_Compile.__default.KMS__CONFIG__KMS__ARN__INVALID()).length())) > 0)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(37,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      if (!(((_8_message).take(java.math.BigInteger.valueOf((KeyStoreErrorMessages_Compile.__default.KMS__CONFIG__KMS__ARN__INVALID()).length()))).equals(KeyStoreErrorMessages_Compile.__default.KMS__CONFIG__KMS__ARN__INVALID()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(38,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _9___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source0)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,16): " + (dafny.DafnySequence.asString("Invalid KMS Key ARN should fail Key Store Construction")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _10___mcc_h4 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,16): " + (dafny.DafnySequence.asString("Invalid KMS Key ARN should fail Key Store Construction")).verbatimString());
      }
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _11___mcc_h6 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _12___mcc_h7 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,16): " + (dafny.DafnySequence.asString("Invalid KMS Key ARN should fail Key Store Construction")).verbatimString());
      }
    } else if (_source0.is_Opaque()) {
      Object _13___mcc_h10 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source0)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,16): " + (dafny.DafnySequence.asString("Invalid KMS Key ARN should fail Key Store Construction")).verbatimString());
      }
    } else {
      Object _14___mcc_h12 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _15___mcc_h13 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,16): " + (dafny.DafnySequence.asString("Invalid KMS Key ARN should fail Key Store Construction")).verbatimString());
      }
    }
  }
  public static void TestInvalidKmsKeyArnAliasConfig()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(47,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(48,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.kmsKeyAlias());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_keyStore;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_keyStore = _out2;
    if (!((_6_keyStore).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(62,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source0 = (_6_keyStore).dtor_error();
    if (_source0.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _7___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source0)._message;
      dafny.DafnySequence<? extends Character> _8_message = _7___mcc_h0;
      if (!((java.math.BigInteger.valueOf((_8_message).length())).compareTo(java.math.BigInteger.valueOf((KeyStoreErrorMessages_Compile.__default.ALIAS__NOT__ALLOWED()).length())) >= 0)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(65,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      if (!(((_8_message).take(java.math.BigInteger.valueOf((KeyStoreErrorMessages_Compile.__default.ALIAS__NOT__ALLOWED()).length()))).equals(KeyStoreErrorMessages_Compile.__default.ALIAS__NOT__ALLOWED()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(66,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _9___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source0)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(67,16): " + (dafny.DafnySequence.asString("Alias should fail Key Store Construction")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _10___mcc_h4 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(67,16): " + (dafny.DafnySequence.asString("Alias should fail Key Store Construction")).verbatimString());
      }
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _11___mcc_h6 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _12___mcc_h7 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(67,16): " + (dafny.DafnySequence.asString("Alias should fail Key Store Construction")).verbatimString());
      }
    } else if (_source0.is_Opaque()) {
      Object _13___mcc_h10 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source0)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(67,16): " + (dafny.DafnySequence.asString("Alias should fail Key Store Construction")).verbatimString());
      }
    } else {
      Object _14___mcc_h12 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _15___mcc_h13 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(67,16): " + (dafny.DafnySequence.asString("Alias should fail Key Store Construction")).verbatimString());
      }
    }
  }
  public static void TestValidConfig()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(73,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(74,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_keyStore;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_keyStore = _out2;
    if (!((_6_keyStore).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(88,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _7_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = ((_6_keyStore).dtor_value()).GetKeyStoreInfo();
    _7_valueOrError2 = _out3;
    if (!(!((_7_valueOrError2).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(90,16): " + java.lang.String.valueOf(_7_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput _8_conf;
    _8_conf = (_7_valueOrError2).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _9_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _9_valueOrError3 = UUID.__default.ToByteArray((_8_conf).dtor_keyStoreId());
    if (!(!((_9_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(95,22): " + java.lang.String.valueOf(_9_valueOrError3));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _10_idByteUUID;
    _10_idByteUUID = (_9_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _11_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _11_valueOrError4 = UUID.__default.FromByteArray(_10_idByteUUID);
    if (!(!((_11_valueOrError4).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(96,23): " + java.lang.String.valueOf(_11_valueOrError4));
    }
    dafny.DafnySequence<? extends Character> _12_idRoundTrip;
    _12_idRoundTrip = (_11_valueOrError4).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((_12_idRoundTrip).equals((_8_conf).dtor_keyStoreId()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(97,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_8_conf).dtor_keyStoreName()).equals(Fixtures_Compile.__default.branchKeyStoreName()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(99,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_8_conf).dtor_logicalKeyStoreName()).equals(Fixtures_Compile.__default.logicalKeyStoreName()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(100,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals((_8_conf).dtor_kmsConfiguration(), _4_kmsConfig))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(101,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestValidConfigNoClients()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(106,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(107,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class))));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_keyStore;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_keyStore = _out2;
    if (!((_6_keyStore).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(134,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class))), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_keyStore = _out3;
    if (!((_6_keyStore).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(160,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class))), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class))));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_keyStore = _out4;
    if (!((_6_keyStore).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(193,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestConfig._default";
  }
}
