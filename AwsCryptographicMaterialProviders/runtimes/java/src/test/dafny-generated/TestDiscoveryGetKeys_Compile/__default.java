// Class __default
// Dafny class __default compiled into Java
package TestDiscoveryGetKeys_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestGetBeaconKeyForTwoKmsArnsSuccess()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(24,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(25,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_discovery(software.amazon.cryptography.keystore.internaldafny.types.Discovery.create());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(38,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create(Fixtures_Compile.__default.branchKeyId()));
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(40,27): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput _9_beaconKeyResult;
    _9_beaconKeyResult = (_8_valueOrError3).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!((((_9_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_beaconKeyIdentifier()).equals(Fixtures_Compile.__default.branchKeyId()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(44,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = (_7_keyStore).GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create(Fixtures_Compile.__default.postalHornBranchKeyId()));
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(46,23): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    _9_beaconKeyResult = (_10_valueOrError4).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!((((_9_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_beaconKeyIdentifier()).equals(Fixtures_Compile.__default.postalHornBranchKeyId()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(51,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestGetActiveKeyForTwoKmsArnsSuccess()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(57,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(58,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_discovery(software.amazon.cryptography.keystore.internaldafny.types.Discovery.create());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(71,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create(Fixtures_Compile.__default.branchKeyId()));
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(73,24): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _9_activeResult;
    _9_activeResult = (_8_valueOrError3).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!((((_9_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(Fixtures_Compile.__default.branchKeyId()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(78,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create(Fixtures_Compile.__default.postalHornBranchKeyId()));
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(80,20): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    _9_activeResult = (_10_valueOrError4).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!((((_9_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(Fixtures_Compile.__default.postalHornBranchKeyId()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(85,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestGetBranchKeyVersionForTwoKmsArnsSuccess()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(90,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(91,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_discovery(software.amazon.cryptography.keystore.internaldafny.types.Discovery.create());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(104,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create(Fixtures_Compile.__default.branchKeyId(), Fixtures_Compile.__default.branchKeyIdActiveVersion()));
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(106,25): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _9_versionResult;
    _9_versionResult = (_8_valueOrError3).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _10_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _10_valueOrError4 = UTF8.__default.Encode(Fixtures_Compile.__default.branchKeyIdActiveVersion());
    if (!(!((_10_valueOrError4).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(111,21): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _11_testBytes;
    _11_testBytes = (_10_valueOrError4).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((((_9_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(Fixtures_Compile.__default.branchKeyId()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(112,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((((_9_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(Fixtures_Compile.__default.branchKeyIdActiveVersionUtf8Bytes())) && ((Fixtures_Compile.__default.branchKeyIdActiveVersionUtf8Bytes()).equals(_11_testBytes)))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(113,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _12_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create(Fixtures_Compile.__default.postalHornBranchKeyId(), Fixtures_Compile.__default.postalHornBranchKeyActiveVersion()));
    _12_valueOrError5 = _out4;
    if (!(!((_12_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(115,21): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    _9_versionResult = (_12_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _13_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _13_valueOrError6 = UTF8.__default.Encode(Fixtures_Compile.__default.postalHornBranchKeyActiveVersion());
    if (!(!((_13_valueOrError6).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(120,17): " + java.lang.String.valueOf(_13_valueOrError6));
    }
    _11_testBytes = (_13_valueOrError6).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((((_9_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(Fixtures_Compile.__default.postalHornBranchKeyId()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(121,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_9_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(_11_testBytes))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(122,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestGetKeysForMrk()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(127,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(128,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfigMr;
    _4_kmsConfigMr = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_mrDiscovery(software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery.create(dafny.DafnySequence.asString("us-west-2")));
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _5_kmsConfigSr;
    _5_kmsConfigSr = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_discovery(software.amazon.cryptography.keystore.internaldafny.types.Discovery.create());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _6_keyStoreConfigMr;
    _6_keyStoreConfigMr = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfigMr, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _7_keyStoreConfigSr;
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _8_dt__update__tmp_h0 = _6_keyStoreConfigMr;
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _9_dt__update_hkmsConfiguration_h0 = _5_kmsConfigSr;
    _7_keyStoreConfigSr = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create((_8_dt__update__tmp_h0).dtor_ddbTableName(), _9_dt__update_hkmsConfiguration_h0, (_8_dt__update__tmp_h0).dtor_logicalKeyStoreName(), (_8_dt__update__tmp_h0).dtor_id(), (_8_dt__update__tmp_h0).dtor_grantTokens(), (_8_dt__update__tmp_h0).dtor_ddbClient(), (_8_dt__update__tmp_h0).dtor_kmsClient());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_6_keyStoreConfigMr);
    _10_valueOrError2 = _out2;
    if (!(!((_10_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(144,22): " + java.lang.String.valueOf(_10_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _11_keyStoreMr;
    _11_keyStoreMr = (_10_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _12_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_7_keyStoreConfigSr);
    _12_valueOrError3 = _out3;
    if (!(!((_12_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(145,22): " + java.lang.String.valueOf(_12_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _13_keyStoreSr;
    _13_keyStoreSr = (_12_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput _14_beaconInput;
    _14_beaconInput = software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create(Fixtures_Compile.__default.EastBranchKey());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _15_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = (_11_keyStoreMr).GetBeaconKey(_14_beaconInput);
    _15_valueOrError4 = _out4;
    if (!(!((_15_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(148,29): " + java.lang.String.valueOf(_15_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput _16_beaconKeyResultMr;
    _16_beaconKeyResultMr = (_15_valueOrError4).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!((((_16_beaconKeyResultMr).dtor_beaconKeyMaterials()).dtor_beaconKeyIdentifier()).equals(Fixtures_Compile.__default.EastBranchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(149,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _17_beaconKeyResultSr;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = (_13_keyStoreSr).GetBeaconKey(_14_beaconInput);
    _17_beaconKeyResultSr = _out5;
    if (!((_17_beaconKeyResultSr).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(152,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_17_beaconKeyResultSr).dtor_error()).is_ComAmazonawsKms())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(153,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source0 = (_17_beaconKeyResultSr).dtor_error();
    if (_source0.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _18___mcc_h0 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + (dafny.DafnySequence.asString("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _19___mcc_h2 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source0)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + (dafny.DafnySequence.asString("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _20___mcc_h4 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      software.amazon.cryptography.services.kms.internaldafny.types.Error _21_nestedError = _20___mcc_h4;
      if (!((_21_nestedError).is_IncorrectKeyException())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(156,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _22___mcc_h6 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _23___mcc_h7 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + (dafny.DafnySequence.asString("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source0.is_Opaque()) {
      Object _24___mcc_h10 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source0)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + (dafny.DafnySequence.asString("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else {
      Object _25___mcc_h12 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _26___mcc_h13 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + (dafny.DafnySequence.asString("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput _27_branchInput;
    _27_branchInput = software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create(Fixtures_Compile.__default.EastBranchKey());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _28_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out6;
    _out6 = (_11_keyStoreMr).GetActiveBranchKey(_27_branchInput);
    _28_valueOrError5 = _out6;
    if (!(!((_28_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(161,29): " + java.lang.String.valueOf(_28_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _29_branchKeyResultMr;
    _29_branchKeyResultMr = (_28_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!((((_29_branchKeyResultMr).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(Fixtures_Compile.__default.EastBranchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(162,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _30_branchKeyResultSr;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out7;
    _out7 = (_13_keyStoreSr).GetActiveBranchKey(_27_branchInput);
    _30_branchKeyResultSr = _out7;
    if (!((_30_branchKeyResultSr).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(165,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_30_branchKeyResultSr).dtor_error()).is_ComAmazonawsKms())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(166,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.Error _source1 = (_30_branchKeyResultSr).dtor_error();
    if (_source1.is_KeyStoreException()) {
      dafny.DafnySequence<? extends Character> _31___mcc_h16 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException)_source1)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + (dafny.DafnySequence.asString("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source1.is_ComAmazonawsDynamodb()) {
      software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _32___mcc_h18 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb)_source1)._ComAmazonawsDynamodb;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + (dafny.DafnySequence.asString("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source1.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _33___mcc_h20 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms)_source1)._ComAmazonawsKms;
      software.amazon.cryptography.services.kms.internaldafny.types.Error _34_nestedError = _33___mcc_h20;
      if (!((_34_nestedError).is_IncorrectKeyException())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(170,8): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    } else if (_source1.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.keystore.internaldafny.types.Error> _35___mcc_h22 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source1)._list;
      dafny.DafnySequence<? extends Character> _36___mcc_h23 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors)_source1)._message;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + (dafny.DafnySequence.asString("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else if (_source1.is_Opaque()) {
      Object _37___mcc_h26 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque)_source1)._obj;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + (dafny.DafnySequence.asString("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    } else {
      Object _38___mcc_h28 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source1)._obj;
      dafny.DafnySequence<? extends Character> _39___mcc_h29 = ((software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText)_source1)._objMessage;
      if (!(false)) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + (dafny.DafnySequence.asString("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")).verbatimString());
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestDiscoveryGetKeys._default";
  }
}
