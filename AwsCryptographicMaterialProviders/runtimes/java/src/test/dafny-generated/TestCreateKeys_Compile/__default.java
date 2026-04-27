// Class __default
// Dafny class __default compiled into Java
package TestCreateKeys_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestCreateBranchAndBeaconKeys()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(68,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(69,21): " + java.lang.String.valueOf(_2_valueOrError1));
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
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(82,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(84,23): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput _9_branchKeyId;
    _9_branchKeyId = (_8_valueOrError3).Extract(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = (_7_keyStore).GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create((_9_branchKeyId).dtor_branchKeyIdentifier()));
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(88,27): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput _11_beaconKeyResult;
    _11_beaconKeyResult = (_10_valueOrError4).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _12_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_9_branchKeyId).dtor_branchKeyIdentifier()));
    _12_valueOrError5 = _out5;
    if (!(!((_12_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(93,24): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _13_activeResult;
    _13_activeResult = (_12_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _14_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _14_valueOrError6 = UTF8.__default.Decode(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_14_valueOrError6).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(98,28): " + java.lang.String.valueOf(_14_valueOrError6));
    }
    dafny.DafnySequence<? extends Character> _15_branchKeyVersion;
    _15_branchKeyVersion = (_14_valueOrError6).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _16_valueOrError7 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out6;
    _out6 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create((_9_branchKeyId).dtor_branchKeyIdentifier(), _15_branchKeyVersion));
    _16_valueOrError7 = _out6;
    if (!(!((_16_valueOrError7).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(99,25): " + java.lang.String.valueOf(_16_valueOrError7));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _17_versionResult;
    _17_versionResult = (_16_valueOrError7).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    CleanupItems_Compile.__default.DeleteVersion((_9_branchKeyId).dtor_branchKeyIdentifier(), _15_branchKeyVersion, _3_ddbClient);
    CleanupItems_Compile.__default.DeleteActive((_9_branchKeyId).dtor_branchKeyIdentifier(), _3_ddbClient);
    if (!((((_11_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_beaconKey()).is_Some())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(111,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf(((((_11_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_beaconKey()).dtor_value()).length()), java.math.BigInteger.valueOf(32L)))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(112,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKey()).length()), java.math.BigInteger.valueOf(32L)))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(113,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_17_versionResult).dtor_branchKeyMaterials()).dtor_branchKey()).equals(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(114,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((((_17_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier())) && ((((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(((_11_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_beaconKeyIdentifier())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(115,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_17_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(118,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _18_valueOrError8 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _18_valueOrError8 = UUID.__default.ToByteArray(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier());
    if (!(!((_18_valueOrError8).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(125,22): " + java.lang.String.valueOf(_18_valueOrError8));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _19_idByteUUID;
    _19_idByteUUID = (_18_valueOrError8).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _20_valueOrError9 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _20_valueOrError9 = UUID.__default.FromByteArray(_19_idByteUUID);
    if (!(!((_20_valueOrError9).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(126,23): " + java.lang.String.valueOf(_20_valueOrError9));
    }
    dafny.DafnySequence<? extends Character> _21_idRoundTrip;
    _21_idRoundTrip = (_20_valueOrError9).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((_21_idRoundTrip).equals(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(127,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _22_valueOrError10 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _22_valueOrError10 = UTF8.__default.Decode(((_13_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_22_valueOrError10).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(133,25): " + java.lang.String.valueOf(_22_valueOrError10));
    }
    dafny.DafnySequence<? extends Character> _23_versionString;
    _23_versionString = (_22_valueOrError10).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _24_valueOrError11 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _24_valueOrError11 = UUID.__default.ToByteArray(_23_versionString);
    if (!(!((_24_valueOrError11).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(134,27): " + java.lang.String.valueOf(_24_valueOrError11));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _25_versionByteUUID;
    _25_versionByteUUID = (_24_valueOrError11).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _26_valueOrError12 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _26_valueOrError12 = UUID.__default.FromByteArray(_25_versionByteUUID);
    if (!(!((_26_valueOrError12).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(135,28): " + java.lang.String.valueOf(_26_valueOrError12));
    }
    dafny.DafnySequence<? extends Character> _27_versionRoundTrip;
    _27_versionRoundTrip = (_26_valueOrError12).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((_27_versionRoundTrip).equals(_23_versionString))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(136,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestCreateOptions()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(142,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(143,21): " + java.lang.String.valueOf(_2_valueOrError1));
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
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(156,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _8_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out3;
    _out3 = UUID.__default.GenerateUUID();
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(159,14): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    dafny.DafnySequence<? extends Character> _9_id;
    _9_id = (_8_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _10_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _out4;
    _out4 = Fixtures_Compile.__default.EncodeEncryptionContext(dafny.DafnyMap.fromElements(new dafny.Tuple2(dafny.DafnySequence.asString("some"), dafny.DafnySequence.asString("encryption")), new dafny.Tuple2(dafny.DafnySequence.asString("context"), dafny.DafnySequence.asString("values"))));
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(161,29): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _11_encryptionContext;
    _11_encryptionContext = (_10_valueOrError4).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _12_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = (_7_keyStore).CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _9_id), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _11_encryptionContext)));
    _12_valueOrError5 = _out5;
    if (!(!((_12_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(166,23): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput _13_branchKeyId;
    _13_branchKeyId = (_12_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _14_valueOrError6 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out6;
    _out6 = (_7_keyStore).GetBeaconKey(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create((_13_branchKeyId).dtor_branchKeyIdentifier()));
    _14_valueOrError6 = _out6;
    if (!(!((_14_valueOrError6).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(171,27): " + java.lang.String.valueOf(_14_valueOrError6));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput _15_beaconKeyResult;
    _15_beaconKeyResult = (_14_valueOrError6).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _16_valueOrError7 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out7;
    _out7 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_13_branchKeyId).dtor_branchKeyIdentifier()));
    _16_valueOrError7 = _out7;
    if (!(!((_16_valueOrError7).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(176,24): " + java.lang.String.valueOf(_16_valueOrError7));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _17_activeResult;
    _17_activeResult = (_16_valueOrError7).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _18_valueOrError8 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _18_valueOrError8 = UTF8.__default.Decode(((_17_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_18_valueOrError8).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(181,28): " + java.lang.String.valueOf(_18_valueOrError8));
    }
    dafny.DafnySequence<? extends Character> _19_branchKeyVersion;
    _19_branchKeyVersion = (_18_valueOrError8).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _20_valueOrError9 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out8;
    _out8 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create((_13_branchKeyId).dtor_branchKeyIdentifier(), _19_branchKeyVersion));
    _20_valueOrError9 = _out8;
    if (!(!((_20_valueOrError9).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(182,25): " + java.lang.String.valueOf(_20_valueOrError9));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _21_versionResult;
    _21_versionResult = (_20_valueOrError9).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    CleanupItems_Compile.__default.DeleteVersion((_13_branchKeyId).dtor_branchKeyIdentifier(), _19_branchKeyVersion, _3_ddbClient);
    CleanupItems_Compile.__default.DeleteActive((_13_branchKeyId).dtor_branchKeyIdentifier(), _3_ddbClient);
    if (!((((_9_id).equals(((_21_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier())) && ((((_21_versionResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(((_17_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()))) && ((((_17_activeResult).dtor_branchKeyMaterials()).dtor_branchKeyIdentifier()).equals(((_15_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_beaconKeyIdentifier())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(195,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_11_encryptionContext).equals(((_21_versionResult).dtor_branchKeyMaterials()).dtor_encryptionContext())) && ((((_21_versionResult).dtor_branchKeyMaterials()).dtor_encryptionContext()).equals(((_17_activeResult).dtor_branchKeyMaterials()).dtor_encryptionContext()))) && ((((_17_activeResult).dtor_branchKeyMaterials()).dtor_encryptionContext()).equals(((_15_beaconKeyResult).dtor_beaconKeyMaterials()).dtor_encryptionContext())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(200,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestCreateDuplicate()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(209,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(210,21): " + java.lang.String.valueOf(_2_valueOrError1));
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
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(223,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_attempt;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Fixtures_Compile.__default.branchKeyId()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
    _8_attempt = _out3;
    if (!((_8_attempt).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(230,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void InsertingADuplicateWillFail()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(236,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _1_ddbClient;
    _1_ddbClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_encryptionContext;
    _2_encryptionContext = Structure_Compile.__default.DecryptOnlyBranchKeyEncryptionContext(Fixtures_Compile.__default.branchKeyId(), Fixtures_Compile.__default.branchKeyIdActiveVersion(), dafny.DafnySequence.asString(""), dafny.DafnySequence.asString(""), Fixtures_Compile.__default.keyArn(), dafny.DafnyMap.fromElements());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_output;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out1;
    _out1 = DDBKeystoreOperations_Compile.__default.WriteNewKeyToStore(Structure_Compile.__default.ToAttributeMap(_2_encryptionContext, dafny.DafnySequence.<java.lang.Byte> of((byte) 1)), Structure_Compile.__default.ToAttributeMap(Structure_Compile.__default.ActiveBranchKeyEncryptionContext(_2_encryptionContext), dafny.DafnySequence.<java.lang.Byte> of((byte) 2)), Structure_Compile.__default.ToAttributeMap(Structure_Compile.__default.BeaconKeyEncryptionContext(_2_encryptionContext), dafny.DafnySequence.<java.lang.Byte> of((byte) 3)), Fixtures_Compile.__default.branchKeyStoreName(), _1_ddbClient);
    _3_output = _out1;
    if (!((_3_output).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(255,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void InsertingADuplicateWillWithADifferentVersionFail()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(261,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _1_ddbClient;
    _1_ddbClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_encryptionContext;
    _2_encryptionContext = Structure_Compile.__default.DecryptOnlyBranchKeyEncryptionContext(Fixtures_Compile.__default.branchKeyId(), dafny.DafnySequence.asString("!= branchKeyIdActiveVersion"), dafny.DafnySequence.asString(""), dafny.DafnySequence.asString(""), Fixtures_Compile.__default.keyArn(), dafny.DafnyMap.fromElements());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_output;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out1;
    _out1 = DDBKeystoreOperations_Compile.__default.WriteNewKeyToStore(Structure_Compile.__default.ToAttributeMap(_2_encryptionContext, dafny.DafnySequence.<java.lang.Byte> of((byte) 1)), Structure_Compile.__default.ToAttributeMap(Structure_Compile.__default.ActiveBranchKeyEncryptionContext(_2_encryptionContext), dafny.DafnySequence.<java.lang.Byte> of((byte) 2)), Structure_Compile.__default.ToAttributeMap(Structure_Compile.__default.BeaconKeyEncryptionContext(_2_encryptionContext), dafny.DafnySequence.<java.lang.Byte> of((byte) 3)), Fixtures_Compile.__default.branchKeyStoreName(), _1_ddbClient);
    _3_output = _out1;
    if (!((_3_output).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(280,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestCreateKeys._default";
  }
}
