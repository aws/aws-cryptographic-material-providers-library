// Class __default
// Dafny class __default compiled into Java
package TestVersionKey_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestVersionKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(27,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(28,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.keyArn());
    if (!(software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableName(Fixtures_Compile.__default.branchKeyStoreName()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(30,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(42,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = (_7_keyStore).CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(47,23): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput _9_branchKeyId;
    _9_branchKeyId = (_8_valueOrError3).Extract(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_9_branchKeyId).dtor_branchKeyIdentifier()));
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(52,27): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _11_oldActiveResult;
    _11_oldActiveResult = (_10_valueOrError4).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _12_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _12_valueOrError5 = UTF8.__default.Decode(((_11_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_12_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(57,28): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    dafny.DafnySequence<? extends Character> _13_oldActiveVersion;
    _13_oldActiveVersion = (_12_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _14_valueOrError6 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = (_7_keyStore).VersionKey(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput.create((_9_branchKeyId).dtor_branchKeyIdentifier()));
    _14_valueOrError6 = _out5;
    if (!(!((_14_valueOrError6).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(59,28): " + java.lang.String.valueOf(_14_valueOrError6));
    }
    software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput _15_versionKeyResult;
    _15_versionKeyResult = (_14_valueOrError6).Extract(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _16_valueOrError7 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out6;
    _out6 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create((_9_branchKeyId).dtor_branchKeyIdentifier(), _13_oldActiveVersion));
    _16_valueOrError7 = _out6;
    if (!(!((_16_valueOrError7).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(64,37): " + java.lang.String.valueOf(_16_valueOrError7));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _17_getBranchKeyVersionResult;
    _17_getBranchKeyVersionResult = (_16_valueOrError7).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _18_valueOrError8 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out7;
    _out7 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_9_branchKeyId).dtor_branchKeyIdentifier()));
    _18_valueOrError8 = _out7;
    if (!(!((_18_valueOrError8).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(72,27): " + java.lang.String.valueOf(_18_valueOrError8));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _19_newActiveResult;
    _19_newActiveResult = (_18_valueOrError8).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _20_valueOrError9 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _20_valueOrError9 = UTF8.__default.Decode(((_19_newActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_20_valueOrError9).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(77,28): " + java.lang.String.valueOf(_20_valueOrError9));
    }
    dafny.DafnySequence<? extends Character> _21_newActiveVersion;
    _21_newActiveVersion = (_20_valueOrError9).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    CleanupItems_Compile.__default.DeleteVersion((_9_branchKeyId).dtor_branchKeyIdentifier(), _21_newActiveVersion, _3_ddbClient);
    CleanupItems_Compile.__default.DeleteVersion((_9_branchKeyId).dtor_branchKeyIdentifier(), _13_oldActiveVersion, _3_ddbClient);
    CleanupItems_Compile.__default.DeleteActive((_9_branchKeyId).dtor_branchKeyIdentifier(), _3_ddbClient);
    if (!((((_17_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(((_11_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(87,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_17_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKey()).equals(((_11_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(88,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(!(((_17_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(((_19_newActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(90,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(!(((_17_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKey()).equals(((_19_newActiveResult).dtor_branchKeyMaterials()).dtor_branchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(91,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestVersionKeyWithEC()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(96,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _1_kmsClient;
    _1_kmsClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(97,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _3_ddbClient;
    _3_ddbClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _4_kmsConfig;
    _4_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(Fixtures_Compile.__default.keyArn());
    if (!(software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableName(Fixtures_Compile.__default.branchKeyStoreName()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(99,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _5_keyStoreConfig;
    _5_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), _4_kmsConfig, Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _3_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _1_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_5_keyStoreConfig);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(111,20): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _7_keyStore;
    _7_keyStore = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _8_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out3;
    _out3 = UUID.__default.GenerateUUID();
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(116,14): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    dafny.DafnySequence<? extends Character> _9_id;
    _9_id = (_8_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _10_customEC;
    _10_customEC = dafny.DafnyMap.fromElements(new dafny.Tuple2(dafny.DafnySequence.asString("some"), dafny.DafnySequence.asString("encryption")), new dafny.Tuple2(dafny.DafnySequence.asString("context"), dafny.DafnySequence.asString("values")));
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _11_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _out4;
    _out4 = Fixtures_Compile.__default.EncodeEncryptionContext(_10_customEC);
    _11_valueOrError4 = _out4;
    if (!(!((_11_valueOrError4).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(122,29): " + java.lang.String.valueOf(_11_valueOrError4));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _12_encryptionContext;
    _12_encryptionContext = (_11_valueOrError4).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _13_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = (_7_keyStore).CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _9_id), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _12_encryptionContext)));
    _13_valueOrError5 = _out5;
    if (!(!((_13_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(124,23): " + java.lang.String.valueOf(_13_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput _14_branchKeyId;
    _14_branchKeyId = (_13_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!(((_14_branchKeyId).dtor_branchKeyIdentifier()).equals(_9_id))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(129,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _15_valueOrError6 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out6;
    _out6 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_14_branchKeyId).dtor_branchKeyIdentifier()));
    _15_valueOrError6 = _out6;
    if (!(!((_15_valueOrError6).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(131,27): " + java.lang.String.valueOf(_15_valueOrError6));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _16_oldActiveResult;
    _16_oldActiveResult = (_15_valueOrError6).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _17_mat;
    _17_mat = (_16_oldActiveResult).dtor_branchKeyMaterials();
    if (!(((_17_mat).dtor_branchKeyIdentifier()).equals(_9_id))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(136,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _18_valueOrError7 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _out7;
    _out7 = Fixtures_Compile.__default.DecodeEncryptionContext((_17_mat).dtor_encryptionContext());
    _18_valueOrError7 = _out7;
    if (!(!((_18_valueOrError7).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(137,17): " + java.lang.String.valueOf(_18_valueOrError7));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _19_matEC;
    _19_matEC = (_18_valueOrError7).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((_19_matEC).equals(_10_customEC))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(138,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _20_valueOrError8 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _20_valueOrError8 = UTF8.__default.Decode(((_16_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_20_valueOrError8).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(140,28): " + java.lang.String.valueOf(_20_valueOrError8));
    }
    dafny.DafnySequence<? extends Character> _21_oldActiveVersion;
    _21_oldActiveVersion = (_20_valueOrError8).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _22_valueOrError9 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out8;
    _out8 = (_7_keyStore).VersionKey(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput.create((_14_branchKeyId).dtor_branchKeyIdentifier()));
    _22_valueOrError9 = _out8;
    if (!(!((_22_valueOrError9).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(142,28): " + java.lang.String.valueOf(_22_valueOrError9));
    }
    software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput _23_versionKeyResult;
    _23_versionKeyResult = (_22_valueOrError9).Extract(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _24_valueOrError10 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out9;
    _out9 = (_7_keyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create((_14_branchKeyId).dtor_branchKeyIdentifier(), _21_oldActiveVersion));
    _24_valueOrError10 = _out9;
    if (!(!((_24_valueOrError10).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(147,37): " + java.lang.String.valueOf(_24_valueOrError10));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _25_getBranchKeyVersionResult;
    _25_getBranchKeyVersionResult = (_24_valueOrError10).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _26_mat2;
    _26_mat2 = (_25_getBranchKeyVersionResult).dtor_branchKeyMaterials();
    if (!(((_17_mat).dtor_branchKeyIdentifier()).equals(_9_id))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(155,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _27_valueOrError11 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _out10;
    _out10 = Fixtures_Compile.__default.DecodeEncryptionContext((_17_mat).dtor_encryptionContext());
    _27_valueOrError11 = _out10;
    if (!(!((_27_valueOrError11).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(156,18): " + java.lang.String.valueOf(_27_valueOrError11));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _28_mat2EC;
    _28_mat2EC = (_27_valueOrError11).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((_28_mat2EC).equals(_10_customEC))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(157,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_26_mat2).dtor_branchKeyVersion()).equals((_17_mat).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(158,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _29_valueOrError12 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out11;
    _out11 = (_7_keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_14_branchKeyId).dtor_branchKeyIdentifier()));
    _29_valueOrError12 = _out11;
    if (!(!((_29_valueOrError12).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(160,27): " + java.lang.String.valueOf(_29_valueOrError12));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _30_newActiveResult;
    _30_newActiveResult = (_29_valueOrError12).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _31_mat3;
    _31_mat3 = (_30_newActiveResult).dtor_branchKeyMaterials();
    if (!(((_17_mat).dtor_branchKeyIdentifier()).equals(_9_id))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(165,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _32_valueOrError13 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _out12;
    _out12 = Fixtures_Compile.__default.DecodeEncryptionContext((_17_mat).dtor_encryptionContext());
    _32_valueOrError13 = _out12;
    if (!(!((_32_valueOrError13).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(166,18): " + java.lang.String.valueOf(_32_valueOrError13));
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _33_mat3EC;
    _33_mat3EC = (_32_valueOrError13).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((_33_mat3EC).equals(_10_customEC))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(167,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(!((_31_mat3).dtor_branchKeyVersion()).equals((_17_mat).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(168,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _34_valueOrError14 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _34_valueOrError14 = UTF8.__default.Decode(((_30_newActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_34_valueOrError14).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(170,28): " + java.lang.String.valueOf(_34_valueOrError14));
    }
    dafny.DafnySequence<? extends Character> _35_newActiveVersion;
    _35_newActiveVersion = (_34_valueOrError14).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!(!(_35_newActiveVersion).equals(_21_oldActiveVersion))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(172,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    CleanupItems_Compile.__default.DeleteVersion((_14_branchKeyId).dtor_branchKeyIdentifier(), _35_newActiveVersion, _3_ddbClient);
    CleanupItems_Compile.__default.DeleteVersion((_14_branchKeyId).dtor_branchKeyIdentifier(), _21_oldActiveVersion, _3_ddbClient);
    CleanupItems_Compile.__default.DeleteActive((_14_branchKeyId).dtor_branchKeyIdentifier(), _3_ddbClient);
    if (!((((_25_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(((_16_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(182,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_25_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKey()).equals(((_16_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(183,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(!(((_25_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(((_30_newActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(185,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(!(((_25_getBranchKeyVersionResult).dtor_branchKeyMaterials()).dtor_branchKey()).equals(((_30_newActiveResult).dtor_branchKeyMaterials()).dtor_branchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(186,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((_19_matEC).equals(_10_customEC))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(193,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((_28_mat2EC).equals(_10_customEC))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(194,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((_33_mat3EC).equals(_10_customEC))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(195,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestMrkVersionKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(200,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _1_ddbClient;
    _1_ddbClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _2_eastKeyStoreConfig;
    _2_eastKeyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(Fixtures_Compile.__default.branchKeyStoreName(), Fixtures_Compile.__default.KmsMrkConfigEast(), Fixtures_Compile.__default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _1_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class))));
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _3_westKeyStoreConfig;
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _4_dt__update__tmp_h0 = _2_eastKeyStoreConfig;
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _5_dt__update_hkmsConfiguration_h0 = Fixtures_Compile.__default.KmsMrkConfigWest();
    _3_westKeyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create((_4_dt__update__tmp_h0).dtor_ddbTableName(), _5_dt__update_hkmsConfiguration_h0, (_4_dt__update__tmp_h0).dtor_logicalKeyStoreName(), (_4_dt__update__tmp_h0).dtor_id(), (_4_dt__update__tmp_h0).dtor_grantTokens(), (_4_dt__update__tmp_h0).dtor_ddbClient(), (_4_dt__update__tmp_h0).dtor_kmsClient());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _6_eastSrkKeyStoreConfig;
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _7_dt__update__tmp_h1 = _2_eastKeyStoreConfig;
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _8_dt__update_hkmsConfiguration_h1 = Fixtures_Compile.__default.KmsSrkConfigEast();
    _6_eastSrkKeyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create((_7_dt__update__tmp_h1).dtor_ddbTableName(), _8_dt__update_hkmsConfiguration_h1, (_7_dt__update__tmp_h1).dtor_logicalKeyStoreName(), (_7_dt__update__tmp_h1).dtor_id(), (_7_dt__update__tmp_h1).dtor_grantTokens(), (_7_dt__update__tmp_h1).dtor_ddbClient(), (_7_dt__update__tmp_h1).dtor_kmsClient());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _9_westSrkKeyStoreConfig;
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _10_dt__update__tmp_h2 = _2_eastKeyStoreConfig;
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _11_dt__update_hkmsConfiguration_h2 = Fixtures_Compile.__default.KmsSrkConfigWest();
    _9_westSrkKeyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create((_10_dt__update__tmp_h2).dtor_ddbTableName(), _11_dt__update_hkmsConfiguration_h2, (_10_dt__update__tmp_h2).dtor_logicalKeyStoreName(), (_10_dt__update__tmp_h2).dtor_id(), (_10_dt__update__tmp_h2).dtor_grantTokens(), (_10_dt__update__tmp_h2).dtor_ddbClient(), (_10_dt__update__tmp_h2).dtor_kmsClient());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _12_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_2_eastKeyStoreConfig);
    _12_valueOrError1 = _out1;
    if (!(!((_12_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(215,24): " + java.lang.String.valueOf(_12_valueOrError1));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _13_eastKeyStore;
    _13_eastKeyStore = (_12_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _14_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_3_westKeyStoreConfig);
    _14_valueOrError2 = _out2;
    if (!(!((_14_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(216,24): " + java.lang.String.valueOf(_14_valueOrError2));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _15_westKeyStore;
    _15_westKeyStore = (_14_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _16_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_6_eastSrkKeyStoreConfig);
    _16_valueOrError3 = _out3;
    if (!(!((_16_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(217,27): " + java.lang.String.valueOf(_16_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _17_eastSrkKeyStore;
    _17_eastSrkKeyStore = (_16_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _18_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_9_westSrkKeyStoreConfig);
    _18_valueOrError4 = _out4;
    if (!(!((_18_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(218,27): " + java.lang.String.valueOf(_18_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _19_westSrkKeyStore;
    _19_westSrkKeyStore = (_18_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _20_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = (_15_westKeyStore).CreateKey(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
    _20_valueOrError5 = _out5;
    if (!(!((_20_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(223,23): " + java.lang.String.valueOf(_20_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput _21_branchKeyId;
    _21_branchKeyId = (_20_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _22_valueOrError6 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out6;
    _out6 = (_15_westKeyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_21_branchKeyId).dtor_branchKeyIdentifier()));
    _22_valueOrError6 = _out6;
    if (!(!((_22_valueOrError6).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(228,27): " + java.lang.String.valueOf(_22_valueOrError6));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _23_oldActiveResult;
    _23_oldActiveResult = (_22_valueOrError6).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _24_valueOrError7 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _24_valueOrError7 = UTF8.__default.Decode(((_23_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_24_valueOrError7).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(233,28): " + java.lang.String.valueOf(_24_valueOrError7));
    }
    dafny.DafnySequence<? extends Character> _25_oldActiveVersion;
    _25_oldActiveVersion = (_24_valueOrError7).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _26_valueOrError8 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out7;
    _out7 = (_13_eastKeyStore).VersionKey(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput.create((_21_branchKeyId).dtor_branchKeyIdentifier()));
    _26_valueOrError8 = _out7;
    if (!(!((_26_valueOrError8).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(236,28): " + java.lang.String.valueOf(_26_valueOrError8));
    }
    software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput _27_versionKeyResult;
    _27_versionKeyResult = (_26_valueOrError8).Extract(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _28_valueOrError9 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out8;
    _out8 = (_15_westKeyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create((_21_branchKeyId).dtor_branchKeyIdentifier(), _25_oldActiveVersion));
    _28_valueOrError9 = _out8;
    if (!(!((_28_valueOrError9).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(241,41): " + java.lang.String.valueOf(_28_valueOrError9));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _29_getBranchKeyVersionResultWest;
    _29_getBranchKeyVersionResultWest = (_28_valueOrError9).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _30_valueOrError10 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out9;
    _out9 = (_13_eastKeyStore).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create((_21_branchKeyId).dtor_branchKeyIdentifier(), _25_oldActiveVersion));
    _30_valueOrError10 = _out9;
    if (!(!((_30_valueOrError10).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(249,41): " + java.lang.String.valueOf(_30_valueOrError10));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _31_getBranchKeyVersionResultEast;
    _31_getBranchKeyVersionResultEast = (_30_valueOrError10).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(_29_getBranchKeyVersionResultWest, _31_getBranchKeyVersionResultEast))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(257,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _32_valueOrError11 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out10;
    _out10 = (_15_westKeyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_21_branchKeyId).dtor_branchKeyIdentifier()));
    _32_valueOrError11 = _out10;
    if (!(!((_32_valueOrError11).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(259,31): " + java.lang.String.valueOf(_32_valueOrError11));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _33_newActiveResultWest;
    _33_newActiveResultWest = (_32_valueOrError11).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _34_valueOrError12 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out11;
    _out11 = (_13_eastKeyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_21_branchKeyId).dtor_branchKeyIdentifier()));
    _34_valueOrError12 = _out11;
    if (!(!((_34_valueOrError12).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(263,31): " + java.lang.String.valueOf(_34_valueOrError12));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _35_newActiveResultEast;
    _35_newActiveResultEast = (_34_valueOrError12).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(_33_newActiveResultWest, _35_newActiveResultEast))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(268,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _36_valueOrError13 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out12;
    _out12 = (_19_westSrkKeyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_21_branchKeyId).dtor_branchKeyIdentifier()));
    _36_valueOrError13 = _out12;
    if (!(!((_36_valueOrError13).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(274,34): " + java.lang.String.valueOf(_36_valueOrError13));
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _37_newActiveResultSrkWest;
    _37_newActiveResultSrkWest = (_36_valueOrError13).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(_37_newActiveResultSrkWest, _35_newActiveResultEast))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(279,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _38_newActiveResultSrkEastResult;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out13;
    _out13 = (_17_eastSrkKeyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create((_21_branchKeyId).dtor_branchKeyIdentifier()));
    _38_newActiveResultSrkEastResult = _out13;
    if (!((_38_newActiveResultSrkEastResult).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(285,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals((_38_newActiveResultSrkEastResult).dtor_error(), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.GET__KEY__ARN__DISAGREEMENT())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(286,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _39_valueOrError14 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _39_valueOrError14 = UTF8.__default.Decode(((_33_newActiveResultWest).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_39_valueOrError14).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(289,32): " + java.lang.String.valueOf(_39_valueOrError14));
    }
    dafny.DafnySequence<? extends Character> _40_newActiveVersionWest;
    _40_newActiveVersionWest = (_39_valueOrError14).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _41_valueOrError15 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _41_valueOrError15 = UTF8.__default.Decode(((_35_newActiveResultEast).dtor_branchKeyMaterials()).dtor_branchKeyVersion());
    if (!(!((_41_valueOrError15).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(290,32): " + java.lang.String.valueOf(_41_valueOrError15));
    }
    dafny.DafnySequence<? extends Character> _42_newActiveVersionEast;
    _42_newActiveVersionEast = (_41_valueOrError15).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!((_40_newActiveVersionWest).equals(_42_newActiveVersionEast))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(291,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    CleanupItems_Compile.__default.DeleteVersion((_21_branchKeyId).dtor_branchKeyIdentifier(), _42_newActiveVersionEast, _1_ddbClient);
    CleanupItems_Compile.__default.DeleteVersion((_21_branchKeyId).dtor_branchKeyIdentifier(), _25_oldActiveVersion, _1_ddbClient);
    CleanupItems_Compile.__default.DeleteActive((_21_branchKeyId).dtor_branchKeyIdentifier(), _1_ddbClient);
    if (!((((_31_getBranchKeyVersionResultEast).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(((_23_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(301,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_31_getBranchKeyVersionResultEast).dtor_branchKeyMaterials()).dtor_branchKey()).equals(((_23_oldActiveResult).dtor_branchKeyMaterials()).dtor_branchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(302,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(!(((_31_getBranchKeyVersionResultEast).dtor_branchKeyMaterials()).dtor_branchKeyVersion()).equals(((_35_newActiveResultEast).dtor_branchKeyMaterials()).dtor_branchKeyVersion()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(304,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(!(((_31_getBranchKeyVersionResultEast).dtor_branchKeyMaterials()).dtor_branchKey()).equals(((_35_newActiveResultEast).dtor_branchKeyMaterials()).dtor_branchKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(305,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void InsertingADuplicateVersionWillFail()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(316,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _1_ddbClient;
    _1_ddbClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    if (!((java.math.BigInteger.valueOf((Fixtures_Compile.__default.branchKeyId()).length())).signum() == 1)) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(318,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((java.math.BigInteger.valueOf((Fixtures_Compile.__default.branchKeyIdActiveVersion()).length())).signum() == 1)) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(319,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_customEncryptionContext;
    _2_customEncryptionContext = dafny.DafnyMap.fromElements();
    if (!(((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, Boolean>)(_3_customEncryptionContext) -> dafny.Helpers.Quantifier((_3_customEncryptionContext).keySet().Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends Character> _forall_var_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends Character> _4_k = (dafny.DafnySequence<? extends Character>)_forall_var_0;
      return !((_3_customEncryptionContext).<dafny.DafnySequence<? extends Character>>contains(_4_k)) || (software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__AttributeName(dafny.DafnySequence.<Character>concatenate(Structure_Compile.__default.ENCRYPTION__CONTEXT__PREFIX(), _4_k)));
    }))).apply(_2_customEncryptionContext))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(321,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _5_encryptionContext;
    _5_encryptionContext = Structure_Compile.__default.DecryptOnlyBranchKeyEncryptionContext(Fixtures_Compile.__default.branchKeyId(), Fixtures_Compile.__default.branchKeyIdActiveVersion(), dafny.DafnySequence.asString(""), dafny.DafnySequence.asString(""), Fixtures_Compile.__default.keyArn(), dafny.DafnyMap.fromElements());
    if (!(software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableName(Fixtures_Compile.__default.branchKeyStoreName()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(332,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    dafny.DafnySequence<? extends Character> _6_myBranchKeyStoreName;
    _6_myBranchKeyStoreName = Fixtures_Compile.__default.branchKeyStoreName();
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _7_versionBranchKeyItem;
    _7_versionBranchKeyItem = Structure_Compile.__default.ToAttributeMap(_5_encryptionContext, dafny.DafnySequence.<java.lang.Byte> of((byte) 1));
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _8_activeBranchKeyItem;
    _8_activeBranchKeyItem = Structure_Compile.__default.ToAttributeMap(Structure_Compile.__default.ActiveBranchKeyEncryptionContext(_5_encryptionContext), dafny.DafnySequence.<java.lang.Byte> of((byte) 2));
    if (!(java.util.Objects.equals(((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_8_activeBranchKeyItem).get(Structure_Compile.__default.BRANCH__KEY__IDENTIFIER__FIELD()))), ((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_7_versionBranchKeyItem).get(Structure_Compile.__default.BRANCH__KEY__IDENTIFIER__FIELD())))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(336,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_8_activeBranchKeyItem).get(Structure_Compile.__default.BRANCH__KEY__ACTIVE__VERSION__FIELD()))), ((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_7_versionBranchKeyItem).get(Structure_Compile.__default.TYPE__FIELD())))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(337,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _9_output;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out1;
    _out1 = DDBKeystoreOperations_Compile.__default.WriteNewBranchKeyVersionToKeystore(_7_versionBranchKeyItem, _8_activeBranchKeyItem, _6_myBranchKeyStoreName, _1_ddbClient);
    _9_output = _out1;
    if (!((_9_output).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(346,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void VersioningANonexistentBranchKeyWillFail()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(352,21): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _1_ddbClient;
    _1_ddbClient = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_encryptionContext;
    _2_encryptionContext = Structure_Compile.__default.DecryptOnlyBranchKeyEncryptionContext(dafny.DafnySequence.asString("!= branchKeyId"), Fixtures_Compile.__default.branchKeyIdActiveVersion(), dafny.DafnySequence.asString(""), dafny.DafnySequence.asString(""), Fixtures_Compile.__default.keyArn(), dafny.DafnyMap.fromElements());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _3_versionBranchKeyItem;
    _3_versionBranchKeyItem = Structure_Compile.__default.ToAttributeMap(_2_encryptionContext, dafny.DafnySequence.<java.lang.Byte> of((byte) 1));
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _4_activeBranchKeyItem;
    _4_activeBranchKeyItem = Structure_Compile.__default.ToAttributeMap(Structure_Compile.__default.ActiveBranchKeyEncryptionContext(_2_encryptionContext), dafny.DafnySequence.<java.lang.Byte> of((byte) 2));
    if (!(java.util.Objects.equals(((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_4_activeBranchKeyItem).get(Structure_Compile.__default.BRANCH__KEY__IDENTIFIER__FIELD()))), ((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_3_versionBranchKeyItem).get(Structure_Compile.__default.BRANCH__KEY__IDENTIFIER__FIELD())))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(365,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_4_activeBranchKeyItem).get(Structure_Compile.__default.BRANCH__KEY__ACTIVE__VERSION__FIELD()))), ((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_3_versionBranchKeyItem).get(Structure_Compile.__default.TYPE__FIELD())))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(366,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableName(Fixtures_Compile.__default.branchKeyStoreName()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(367,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    dafny.DafnySequence<? extends Character> _5_myBranchKeyStoreName;
    _5_myBranchKeyStoreName = Fixtures_Compile.__default.branchKeyStoreName();
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _6_output;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out1;
    _out1 = DDBKeystoreOperations_Compile.__default.WriteNewBranchKeyVersionToKeystore(_3_versionBranchKeyItem, _4_activeBranchKeyItem, _5_myBranchKeyStoreName, _1_ddbClient);
    _6_output = _out1;
    if (!((_6_output).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(377,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestVersionKey._default";
  }
}
