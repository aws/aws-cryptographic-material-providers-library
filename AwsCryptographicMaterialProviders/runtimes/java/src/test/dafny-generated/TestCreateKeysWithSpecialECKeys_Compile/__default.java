// Class __default
// Dafny class __default compiled into Java
package TestCreateKeysWithSpecialECKeys_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void HappyCaseRoundTrip(dafny.DafnySequence<? extends Character> id, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(32,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(33,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(46,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), id), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), encryptionContext)));
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(49,23): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput _9_branchKeyId;
    _9_branchKeyId = (_8_valueOrError3).Extract(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = (_7_keyStore).GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create((_9_branchKeyId).dtor_branchKeyIdentifier()));
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(55,27): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput _11_beaconKeyResult;
    _11_beaconKeyResult = (_10_valueOrError4).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _12_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_9_branchKeyId).dtor_branchKeyIdentifier()));
    _12_valueOrError5 = _out5;
    if (!(!((_12_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(60,24): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _13_activeResult;
    _13_activeResult = (_12_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _14_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _14_valueOrError6 = UTF8.__default.Decode(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_14_valueOrError6).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(65,28): " + java.lang.String.valueOf(_14_valueOrError6));
    }
    dafny.DafnySequence<? extends Character> _15_branchKeyVersion;
    _15_branchKeyVersion = (_14_valueOrError6).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _16_valueOrError7 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out6;
    _out6 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create((_9_branchKeyId).dtor_branchKeyIdentifier(), _15_branchKeyVersion));
    _16_valueOrError7 = _out6;
    if (!(!((_16_valueOrError7).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(66,25): " + java.lang.String.valueOf(_16_valueOrError7));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _17_versionResult;
    _17_versionResult = (_16_valueOrError7).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _18_valueOrError8 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out7;
    _out7 = CleanupItems_Compile.__default.DeleteBranchKey((_9_branchKeyId).dtor_branchKeyIdentifier(), Fixtures_Compile.__default.branchKeyStoreName(), _3_ddbClient);
    _18_valueOrError8 = _out7;
    if (!(!((_18_valueOrError8).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(73,13): " + java.lang.String.valueOf(_18_valueOrError8));
    }
    boolean _19___v0;
    _19___v0 = (_18_valueOrError8).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    if (!((((id).equals(((_17_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier())) && ((((_17_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()))) && ((((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(((_11_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_beaconKeyIdentifier())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(76,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((encryptionContext).equals(((_17_versionResult).dtor_branchKeyMaterials()).dtor_encryptionContext())) && ((((_17_versionResult).dtor_branchKeyMaterials()).dtor_encryptionContext()).equals(((_13_activeResult).dtor_branchKeyMaterials()).dtor_encryptionContext()))) && ((((_13_activeResult).dtor_branchKeyMaterials()).dtor_encryptionContext()).equals(((_11_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_encryptionContext())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(81,4): " + (dafny.DafnySequence.asString("Failed to retrieve encryption context with branch key materials")).verbatimString());
    }
  }
  public static void TestCreateKeyWithEmptyKeyEC()
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = UUID.__default.GenerateUUID();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(91,16): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    dafny.DafnySequence<? extends Character> _1_uuid;
    _1_uuid = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends Character> _2_id;
    _2_id = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("test-empty-string-key-ec-"), _1_uuid);
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _3_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _out1;
    _out1 = Fixtures_Compile.__default.EncodeEncryptionContext(dafny.DafnyMap.fromElements(new dafny.Tuple2(dafny.DafnySequence.asString(""), dafny.DafnySequence.asString("encryption"))));
    _3_valueOrError1 = _out1;
    if (!(!((_3_valueOrError1).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(95,29): " + java.lang.String.valueOf(_3_valueOrError1));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_encryptionContext;
    _4_encryptionContext = (_3_valueOrError1).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    __default.HappyCaseRoundTrip(_2_id, _4_encryptionContext);
  }
  public static void TestCreateKeyWithWhiteSpaceEC()
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = UUID.__default.GenerateUUID();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(109,16): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    dafny.DafnySequence<? extends Character> _1_uuid;
    _1_uuid = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends Character> _2_id;
    _2_id = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("test-white-space-key-ec-"), _1_uuid);
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _3_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _out1;
    _out1 = Fixtures_Compile.__default.EncodeEncryptionContext(dafny.DafnyMap.fromElements(new dafny.Tuple2(dafny.DafnySequence.asString(" "), dafny.DafnySequence.asString("encryption"))));
    _3_valueOrError1 = _out1;
    if (!(!((_3_valueOrError1).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(113,29): " + java.lang.String.valueOf(_3_valueOrError1));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_encryptionContext;
    _4_encryptionContext = (_3_valueOrError1).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    __default.HappyCaseRoundTrip(_2_id, _4_encryptionContext);
  }
  public static void TestCreateKeyWithAllSpecialCharsEC()
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = UUID.__default.GenerateUUID();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(127,16): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    dafny.DafnySequence<? extends Character> _1_uuid;
    _1_uuid = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends Character> _2_id;
    _2_id = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("test-all-special-chars-ec-"), _1_uuid);
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _3_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _out1;
    _out1 = Fixtures_Compile.__default.EncodeEncryptionContext(dafny.DafnyMap.fromElements(new dafny.Tuple2(dafny.DafnySequence.asString("\n"), dafny.DafnySequence.asString("newline")), new dafny.Tuple2(dafny.DafnySequence.asString("\t"), dafny.DafnySequence.asString("tab")), new dafny.Tuple2(dafny.DafnySequence.asString("\r"), dafny.DafnySequence.asString("carriage-return")), new dafny.Tuple2(dafny.DafnySequence.asString(" "), dafny.DafnySequence.asString("space")), new dafny.Tuple2(dafny.DafnySequence.asString("   "), dafny.DafnySequence.asString("multiple-spaces")), new dafny.Tuple2(dafny.DafnySequence.asString("NormalKey"), dafny.DafnySequence.asString("Value with\nspecial\rchars\t")), new dafny.Tuple2(dafny.DafnySequence.asString("\u0007"), dafny.DafnySequence.asString("bell-unicode")), new dafny.Tuple2(dafny.DafnySequence.asString("\u0001"), dafny.DafnySequence.asString("unicode"))));
    _3_valueOrError1 = _out1;
    if (!(!((_3_valueOrError1).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeysWithSpecialECKeys.dfy(131,29): " + java.lang.String.valueOf(_3_valueOrError1));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_encryptionContext;
    _4_encryptionContext = (_3_valueOrError1).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    __default.HappyCaseRoundTrip(_2_id, _4_encryptionContext);
  }
  @Override
  public java.lang.String toString() {
    return "TestCreateKeysWithSpecialECKeys._default";
  }
}
