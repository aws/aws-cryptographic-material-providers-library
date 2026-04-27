// Class __default
// Dafny class __default compiled into Java
package TestAwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials GetTestMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId suiteId)
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials out = (software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(66,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _2_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out1;
    _out1 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _2_encryptionContext = _out1;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _3_suite;
    _3_suite = AlgorithmSuites_Compile.__default.GetSuite(suiteId);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _4_valueOrError1 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(suiteId, _2_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_4_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(71,33): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _5_encryptionMaterialsIn;
    _5_encryptionMaterialsIn = (_4_valueOrError1).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    out = _5_encryptionMaterialsIn;
    return out;
  }
  public static void TestHierarchyClientESDKSuite()
  {
    dafny.DafnySequence<? extends Character> _0_branchKeyId;
    _0_branchKeyId = __default.BRANCH__KEY__ID();
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(89,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _4_valueOrError1 = _out1;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(91,21): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _5_kmsClient;
    _5_kmsClient = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(92,21): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _7_ddbClient;
    _7_ddbClient = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _8_kmsConfig;
    _8_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _9_keyStoreConfig;
    _9_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _8_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _7_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _5_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_9_keyStoreConfig);
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(105,20): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _11_keyStore;
    _11_keyStore = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyId), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _11_keyStore, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _12_valueOrError4 = _out4;
    if (!(!((_12_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(107,28): " + java.lang.String.valueOf(_12_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _13_hierarchyKeyring;
    _13_hierarchyKeyring = (_12_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _14_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out5;
    _out5 = __default.GetTestMaterials(__default.TEST__ESDK__ALG__SUITE__ID());
    _14_materials = _out5;
    __default.TestRoundtrip(_13_hierarchyKeyring, _14_materials, __default.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyId);
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _15_suite;
    _15_suite = AlgorithmSuites_Compile.__default.GetSuite(__default.TEST__ESDK__ALG__SUITE__ID());
    dafny.DafnySequence<? extends java.lang.Byte> _16_zeroedKey;
    _16_zeroedKey = dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_15_suite)), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_17___v0_boxed0) -> {
      java.math.BigInteger _17___v0 = ((java.math.BigInteger)(java.lang.Object)(_17___v0_boxed0));
      return (byte) 0;
    }));
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _18_dt__update__tmp_h0 = _14_materials;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _19_dt__update_hplaintextDataKey_h0 = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_zeroedKey);
    _14_materials = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create((_18_dt__update__tmp_h0).dtor_algorithmSuite(), (_18_dt__update__tmp_h0).dtor_encryptionContext(), (_18_dt__update__tmp_h0).dtor_encryptedDataKeys(), (_18_dt__update__tmp_h0).dtor_requiredEncryptionContextKeys(), _19_dt__update_hplaintextDataKey_h0, (_18_dt__update__tmp_h0).dtor_signingKey(), (_18_dt__update__tmp_h0).dtor_symmetricSigningKeys());
    __default.TestRoundtrip(_13_hierarchyKeyring, _14_materials, __default.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyId);
  }
  public static void TestHierarchyClientDBESuite()
  {
    dafny.DafnySequence<? extends Character> _0_branchKeyId;
    _0_branchKeyId = __default.BRANCH__KEY__ID();
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(132,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _4_valueOrError1 = _out1;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(134,21): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _5_kmsClient;
    _5_kmsClient = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(135,21): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _7_ddbClient;
    _7_ddbClient = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _8_kmsConfig;
    _8_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _9_keyStoreConfig;
    _9_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _8_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _7_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _5_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_9_keyStoreConfig);
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(148,20): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _11_keyStore;
    _11_keyStore = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyId), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _11_keyStore, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _12_valueOrError4 = _out4;
    if (!(!((_12_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(150,28): " + java.lang.String.valueOf(_12_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _13_hierarchyKeyring;
    _13_hierarchyKeyring = (_12_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _14_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out5;
    _out5 = __default.GetTestMaterials(__default.TEST__DBE__ALG__SUITE__ID());
    _14_materials = _out5;
    __default.TestRoundtrip(_13_hierarchyKeyring, _14_materials, __default.TEST__DBE__ALG__SUITE__ID(), _0_branchKeyId);
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _15_suite;
    _15_suite = AlgorithmSuites_Compile.__default.GetSuite(__default.TEST__DBE__ALG__SUITE__ID());
    dafny.DafnySequence<? extends java.lang.Byte> _16_zeroedKey;
    _16_zeroedKey = dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_15_suite)), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_17___v1_boxed0) -> {
      java.math.BigInteger _17___v1 = ((java.math.BigInteger)(java.lang.Object)(_17___v1_boxed0));
      return (byte) 0;
    }));
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _18_dt__update__tmp_h0 = _14_materials;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _19_dt__update_hplaintextDataKey_h0 = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_zeroedKey);
    _14_materials = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create((_18_dt__update__tmp_h0).dtor_algorithmSuite(), (_18_dt__update__tmp_h0).dtor_encryptionContext(), (_18_dt__update__tmp_h0).dtor_encryptedDataKeys(), (_18_dt__update__tmp_h0).dtor_requiredEncryptionContextKeys(), _19_dt__update_hplaintextDataKey_h0, (_18_dt__update__tmp_h0).dtor_signingKey(), (_18_dt__update__tmp_h0).dtor_symmetricSigningKeys());
    __default.TestRoundtrip(_13_hierarchyKeyring, _14_materials, __default.TEST__DBE__ALG__SUITE__ID(), _0_branchKeyId);
  }
  public static void TestBranchKeyIdSupplier()
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier _0_branchKeyIdSupplier;
    DummyBranchKeyIdSupplier _nw0 = new DummyBranchKeyIdSupplier();
    _nw0.__ctor();
    _0_branchKeyIdSupplier = _nw0;
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(176,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _4_valueOrError1 = _out1;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(178,21): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _5_kmsClient;
    _5_kmsClient = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(179,21): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _7_ddbClient;
    _7_ddbClient = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _8_kmsConfig;
    _8_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _9_keyStoreConfig;
    _9_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _8_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _7_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _5_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_9_keyStoreConfig);
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(192,20): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _11_keyStore;
    _11_keyStore = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class)), _0_branchKeyIdSupplier), _11_keyStore, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _12_valueOrError4 = _out4;
    if (!(!((_12_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(194,28): " + java.lang.String.valueOf(_12_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _13_hierarchyKeyring;
    _13_hierarchyKeyring = (_12_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _14_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out5;
    _out5 = __default.GetTestMaterials(__default.TEST__DBE__ALG__SUITE__ID());
    _14_materials = _out5;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _15_contextCaseA;
    _15_contextCaseA = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>update((_14_materials).dtor_encryptionContext(), __default.BRANCH__KEY(), __default.CASE__A());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _16_dt__update__tmp_h0 = _14_materials;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _17_dt__update_hencryptionContext_h0 = _15_contextCaseA;
    _14_materials = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create((_16_dt__update__tmp_h0).dtor_algorithmSuite(), _17_dt__update_hencryptionContext_h0, (_16_dt__update__tmp_h0).dtor_encryptedDataKeys(), (_16_dt__update__tmp_h0).dtor_requiredEncryptionContextKeys(), (_16_dt__update__tmp_h0).dtor_plaintextDataKey(), (_16_dt__update__tmp_h0).dtor_signingKey(), (_16_dt__update__tmp_h0).dtor_symmetricSigningKeys());
    __default.TestRoundtrip(_13_hierarchyKeyring, _14_materials, __default.TEST__DBE__ALG__SUITE__ID(), __default.BRANCH__KEY__ID__A());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _18_contextCaseB;
    _18_contextCaseB = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>update((_14_materials).dtor_encryptionContext(), __default.BRANCH__KEY(), __default.CASE__B());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _19_dt__update__tmp_h1 = _14_materials;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _20_dt__update_hencryptionContext_h1 = _18_contextCaseB;
    _14_materials = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create((_19_dt__update__tmp_h1).dtor_algorithmSuite(), _20_dt__update_hencryptionContext_h1, (_19_dt__update__tmp_h1).dtor_encryptedDataKeys(), (_19_dt__update__tmp_h1).dtor_requiredEncryptionContextKeys(), (_19_dt__update__tmp_h1).dtor_plaintextDataKey(), (_19_dt__update__tmp_h1).dtor_signingKey(), (_19_dt__update__tmp_h1).dtor_symmetricSigningKeys());
    __default.TestRoundtrip(_13_hierarchyKeyring, _14_materials, __default.TEST__DBE__ALG__SUITE__ID(), __default.BRANCH__KEY__ID__B());
  }
  public static void TestInvalidDataKeyError()
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier _0_branchKeyIdSupplier;
    DummyBranchKeyIdSupplier _nw0 = new DummyBranchKeyIdSupplier();
    _nw0.__ctor();
    _0_branchKeyIdSupplier = _nw0;
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(222,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _4_valueOrError1 = _out1;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(223,21): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _5_kmsClient;
    _5_kmsClient = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _6_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(224,21): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _7_ddbClient;
    _7_ddbClient = (_6_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _8_kmsConfig;
    _8_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _9_keyStoreConfig;
    _9_keyStoreConfig = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _8_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _7_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _5_kmsClient));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_9_keyStoreConfig);
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(235,20): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _11_keyStore;
    _11_keyStore = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class)), _0_branchKeyIdSupplier), _11_keyStore, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _12_valueOrError4 = _out4;
    if (!(!((_12_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(236,28): " + java.lang.String.valueOf(_12_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _13_hierarchyKeyring;
    _13_hierarchyKeyring = (_12_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _14_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out5;
    _out5 = __default.GetTestMaterials(__default.TEST__DBE__ALG__SUITE__ID());
    _14_materials = _out5;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _15_contextCaseA;
    _15_contextCaseA = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>update((_14_materials).dtor_encryptionContext(), __default.BRANCH__KEY(), __default.CASE__A());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _16_contextCaseB;
    _16_contextCaseB = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>update((_14_materials).dtor_encryptionContext(), __default.BRANCH__KEY(), __default.CASE__B());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _17_materialsA;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _18_dt__update__tmp_h0 = _14_materials;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _19_dt__update_hencryptionContext_h0 = _15_contextCaseA;
    _17_materialsA = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create((_18_dt__update__tmp_h0).dtor_algorithmSuite(), _19_dt__update_hencryptionContext_h0, (_18_dt__update__tmp_h0).dtor_encryptedDataKeys(), (_18_dt__update__tmp_h0).dtor_requiredEncryptionContextKeys(), (_18_dt__update__tmp_h0).dtor_plaintextDataKey(), (_18_dt__update__tmp_h0).dtor_signingKey(), (_18_dt__update__tmp_h0).dtor_symmetricSigningKeys());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _20_materialsB;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _21_dt__update__tmp_h1 = _14_materials;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _22_dt__update_hencryptionContext_h1 = _16_contextCaseB;
    _20_materialsB = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create((_21_dt__update__tmp_h1).dtor_algorithmSuite(), _22_dt__update_hencryptionContext_h1, (_21_dt__update__tmp_h1).dtor_encryptedDataKeys(), (_21_dt__update__tmp_h1).dtor_requiredEncryptionContextKeys(), (_21_dt__update__tmp_h1).dtor_plaintextDataKey(), (_21_dt__update__tmp_h1).dtor_signingKey(), (_21_dt__update__tmp_h1).dtor_symmetricSigningKeys());
    __default.TestInvalidDataKeyFailureCase(_13_hierarchyKeyring, _17_materialsA, _20_materialsB, __default.TEST__DBE__ALG__SUITE__ID());
  }
  public static void TestInvalidDataKeyFailureCase(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring hierarchyKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptionMaterialsInEncrypt, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptionMaterialsInDecrypt, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId algorithmSuiteId)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (hierarchyKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(encryptionMaterialsInEncrypt));
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(265,34): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _1_encryptionMaterialsOut;
    _1_encryptionMaterialsOut = (_0_valueOrError0).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(269,15): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _4_valueOrError2 = (_3_mpl).EncryptionMaterialsHasPlaintextDataKey((_1_encryptionMaterialsOut).dtor_materials());
    if (!(!((_4_valueOrError2).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(270,13): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    dafny.Tuple0 _5___v2;
    _5___v2 = (_4_valueOrError2).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_1_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(272,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _6_edk;
    _6_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_1_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _7_valueOrError3 = (_3_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(algorithmSuiteId, (encryptionMaterialsInDecrypt).dtor_encryptionContext(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_7_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(276,33): " + java.lang.String.valueOf(_7_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _8_decryptionMaterialsIn;
    _8_decryptionMaterialsIn = (_7_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_decryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (hierarchyKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_8_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _6_edk)));
    _9_decryptionMaterialsOut = _out2;
    if (!((_9_decryptionMaterialsOut).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(289,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_9_decryptionMaterialsOut).dtor_error()).is_AwsCryptographicMaterialProvidersException())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(290,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _10_valueOrError4 = ErrorMessages_Compile.__default.IncorrectDataKeys(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _6_edk), (_8_decryptionMaterialsIn).dtor_algorithmSuite(), dafny.DafnySequence.asString(""));
    if (!(!((_10_valueOrError4).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(291,32): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    dafny.DafnySequence<? extends Character> _11_expectedErrorMessage;
    _11_expectedErrorMessage = (_10_valueOrError4).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((((_9_decryptionMaterialsOut).dtor_error()).dtor_message()).equals(_11_expectedErrorMessage))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(292,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestRoundtrip(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring hierarchyKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptionMaterialsIn, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId algorithmSuiteId, dafny.DafnySequence<? extends Character> expectedBranchKeyId)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (hierarchyKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(encryptionMaterialsIn));
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(305,34): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _1_encryptionMaterialsOut;
    _1_encryptionMaterialsOut = (_0_valueOrError0).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(309,15): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _4_valueOrError2 = (_3_mpl).EncryptionMaterialsHasPlaintextDataKey((_1_encryptionMaterialsOut).dtor_materials());
    if (!(!((_4_valueOrError2).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(310,13): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    dafny.Tuple0 _5___v3;
    _5___v3 = (_4_valueOrError2).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_1_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(312,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _6_edk;
    _6_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_1_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _7_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _7_valueOrError3 = UTF8.__default.Encode(expectedBranchKeyId);
    if (!(!((_7_valueOrError3).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(317,35): " + java.lang.String.valueOf(_7_valueOrError3));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _8_expectedBranchKeyIdUTF8;
    _8_expectedBranchKeyIdUTF8 = (_7_valueOrError3).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (!(((_6_edk).dtor_keyProviderInfo()).equals(_8_expectedBranchKeyIdUTF8))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(318,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError4 = (_3_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(algorithmSuiteId, (encryptionMaterialsIn).dtor_encryptionContext(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_9_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(320,33): " + java.lang.String.valueOf(_9_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _10_decryptionMaterialsIn;
    _10_decryptionMaterialsIn = (_9_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (hierarchyKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_10_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _6_edk)));
    _11_valueOrError5 = _out2;
    if (!(!((_11_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(327,34): " + java.lang.String.valueOf(_11_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _12_decryptionMaterialsOut;
    _12_decryptionMaterialsOut = (_11_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_1_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_12_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(339,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestSharedCacheWithSamePartitionIdAndSameLogicalKeyStoreName()
  {
    dafny.DafnySequence<? extends Character> _0_branchKeyIdWest;
    _0_branchKeyIdWest = __default.BRANCH__KEY__ID();
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(348,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _4_regionWest;
    _4_regionWest = dafny.DafnySequence.asString("us-west-2");
    dafny.DafnySequence<? extends Character> _5_regionEast;
    _5_regionEast = dafny.DafnySequence.asString("us-east-2");
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _6_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_4_regionWest);
    _6_valueOrError1 = _out1;
    if (!(!((_6_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(353,25): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _7_kmsClientWest;
    _7_kmsClientWest = (_6_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_5_regionEast);
    _8_valueOrError2 = _out2;
    if (!(!((_8_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(354,25): " + java.lang.String.valueOf(_8_valueOrError2));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _9_kmsClientEast;
    _9_kmsClientEast = (_8_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(355,21): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _11_ddbClient;
    _11_ddbClient = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _12_kmsConfig;
    _12_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _13_keyStoreConfigClientRegionWest;
    _13_keyStoreConfigClientRegionWest = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _7_kmsClientWest));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _14_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_13_keyStoreConfigClientRegionWest);
    _14_valueOrError4 = _out4;
    if (!(!((_14_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(371,36): " + java.lang.String.valueOf(_14_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _15_keyStoreClientRegionWest;
    _15_keyStoreClientRegionWest = (_14_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _16_keyStoreConfigClientRegionEast;
    _16_keyStoreConfigClientRegionEast = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _9_kmsClientEast));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _17_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_16_keyStoreConfigClientRegionEast);
    _17_valueOrError5 = _out5;
    if (!(!((_17_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(387,36): " + java.lang.String.valueOf(_17_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _18_keyStoreClientRegionEast;
    _18_keyStoreClientRegionEast = (_17_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_3_mpl).CreateCryptographicMaterialsCache(software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Default(software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache.create(100))));
    _19_valueOrError6 = _out6;
    if (!(!((_19_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(390,28): " + java.lang.String.valueOf(_19_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _20_sharedCacheInput;
    _20_sharedCacheInput = (_19_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.CacheType _21_sharedCache;
    _21_sharedCache = software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Shared(_20_sharedCacheInput);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _15_keyStoreClientRegionWest, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _21_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("partitionId"))));
    _22_valueOrError7 = _out7;
    if (!(!((_22_valueOrError7).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(408,29): " + java.lang.String.valueOf(_22_valueOrError7));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _23_hierarchyKeyring1;
    _23_hierarchyKeyring1 = (_22_valueOrError7).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _18_keyStoreClientRegionEast, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _21_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("partitionId"))));
    _24_valueOrError8 = _out8;
    if (!(!((_24_valueOrError8).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(422,29): " + java.lang.String.valueOf(_24_valueOrError8));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _25_hierarchyKeyring2;
    _25_hierarchyKeyring2 = (_24_valueOrError8).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _26_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out9;
    _out9 = __default.GetTestMaterials(__default.TEST__ESDK__ALG__SUITE__ID());
    _26_materials = _out9;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_encryptionMaterialsOutMismatchedRegion;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_25_hierarchyKeyring2).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_26_materials));
    _27_encryptionMaterialsOutMismatchedRegion = _out10;
    if (!((_27_encryptionMaterialsOutMismatchedRegion).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(449,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    __default.TestRoundtrip(_23_hierarchyKeyring1, _26_materials, __default.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest);
    __default.TestRoundtrip(_25_hierarchyKeyring2, _26_materials, __default.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest);
  }
  public static void TestSharedCacheWithDifferentUnspecifiedPartitionIdAndSameLogicalKeyStoreName()
  {
    dafny.DafnySequence<? extends Character> _0_branchKeyIdWest;
    _0_branchKeyIdWest = __default.BRANCH__KEY__ID();
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(488,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _4_regionWest;
    _4_regionWest = dafny.DafnySequence.asString("us-west-2");
    dafny.DafnySequence<? extends Character> _5_regionEast;
    _5_regionEast = dafny.DafnySequence.asString("us-east-2");
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _6_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_4_regionWest);
    _6_valueOrError1 = _out1;
    if (!(!((_6_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(493,25): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _7_kmsClientWest;
    _7_kmsClientWest = (_6_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_5_regionEast);
    _8_valueOrError2 = _out2;
    if (!(!((_8_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(494,25): " + java.lang.String.valueOf(_8_valueOrError2));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _9_kmsClientEast;
    _9_kmsClientEast = (_8_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(495,21): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _11_ddbClient;
    _11_ddbClient = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _12_kmsConfig;
    _12_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _13_keyStoreConfigClientRegionWest;
    _13_keyStoreConfigClientRegionWest = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _7_kmsClientWest));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _14_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_13_keyStoreConfigClientRegionWest);
    _14_valueOrError4 = _out4;
    if (!(!((_14_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(511,36): " + java.lang.String.valueOf(_14_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _15_keyStoreClientRegionWest;
    _15_keyStoreClientRegionWest = (_14_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _16_keyStoreConfigClientRegionEast;
    _16_keyStoreConfigClientRegionEast = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _9_kmsClientEast));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _17_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_16_keyStoreConfigClientRegionEast);
    _17_valueOrError5 = _out5;
    if (!(!((_17_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(527,36): " + java.lang.String.valueOf(_17_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _18_keyStoreClientRegionEast;
    _18_keyStoreClientRegionEast = (_17_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_3_mpl).CreateCryptographicMaterialsCache(software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Default(software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache.create(100))));
    _19_valueOrError6 = _out6;
    if (!(!((_19_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(530,28): " + java.lang.String.valueOf(_19_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _20_sharedCacheInput;
    _20_sharedCacheInput = (_19_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.CacheType _21_sharedCache;
    _21_sharedCache = software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Shared(_20_sharedCacheInput);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _15_keyStoreClientRegionWest, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _21_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _22_valueOrError7 = _out7;
    if (!(!((_22_valueOrError7).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(548,29): " + java.lang.String.valueOf(_22_valueOrError7));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _23_hierarchyKeyring1;
    _23_hierarchyKeyring1 = (_22_valueOrError7).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _18_keyStoreClientRegionEast, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _21_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _24_valueOrError8 = _out8;
    if (!(!((_24_valueOrError8).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(562,29): " + java.lang.String.valueOf(_24_valueOrError8));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _25_hierarchyKeyring2;
    _25_hierarchyKeyring2 = (_24_valueOrError8).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _26_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out9;
    _out9 = __default.GetTestMaterials(__default.TEST__ESDK__ALG__SUITE__ID());
    _26_materials = _out9;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_encryptionMaterialsOutMismatchedRegion;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_25_hierarchyKeyring2).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_26_materials));
    _27_encryptionMaterialsOutMismatchedRegion = _out10;
    if (!((_27_encryptionMaterialsOutMismatchedRegion).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(583,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    __default.TestRoundtrip(_23_hierarchyKeyring1, _26_materials, __default.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_encryptionMaterialsOutMismatchedRegionFromCache;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = (_25_hierarchyKeyring2).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_26_materials));
    _28_encryptionMaterialsOutMismatchedRegionFromCache = _out11;
    if (!((_28_encryptionMaterialsOutMismatchedRegionFromCache).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(600,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestSharedCacheWithDifferentSpecifiedPartitionIdAndSameLogicalKeyStoreName()
  {
    dafny.DafnySequence<? extends Character> _0_branchKeyIdWest;
    _0_branchKeyIdWest = __default.BRANCH__KEY__ID();
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(608,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _4_regionWest;
    _4_regionWest = dafny.DafnySequence.asString("us-west-2");
    dafny.DafnySequence<? extends Character> _5_regionEast;
    _5_regionEast = dafny.DafnySequence.asString("us-east-2");
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _6_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_4_regionWest);
    _6_valueOrError1 = _out1;
    if (!(!((_6_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(613,25): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _7_kmsClientWest;
    _7_kmsClientWest = (_6_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_5_regionEast);
    _8_valueOrError2 = _out2;
    if (!(!((_8_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(614,25): " + java.lang.String.valueOf(_8_valueOrError2));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _9_kmsClientEast;
    _9_kmsClientEast = (_8_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(615,21): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _11_ddbClient;
    _11_ddbClient = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _12_kmsConfig;
    _12_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _13_keyStoreConfigClientRegionWest;
    _13_keyStoreConfigClientRegionWest = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _7_kmsClientWest));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _14_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_13_keyStoreConfigClientRegionWest);
    _14_valueOrError4 = _out4;
    if (!(!((_14_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(631,36): " + java.lang.String.valueOf(_14_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _15_keyStoreClientRegionWest;
    _15_keyStoreClientRegionWest = (_14_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _16_keyStoreConfigClientRegionEast;
    _16_keyStoreConfigClientRegionEast = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, __default.logicalKeyStoreName(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _9_kmsClientEast));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _17_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_16_keyStoreConfigClientRegionEast);
    _17_valueOrError5 = _out5;
    if (!(!((_17_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(647,36): " + java.lang.String.valueOf(_17_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _18_keyStoreClientRegionEast;
    _18_keyStoreClientRegionEast = (_17_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_3_mpl).CreateCryptographicMaterialsCache(software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Default(software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache.create(100))));
    _19_valueOrError6 = _out6;
    if (!(!((_19_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(650,28): " + java.lang.String.valueOf(_19_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _20_sharedCacheInput;
    _20_sharedCacheInput = (_19_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.CacheType _21_sharedCache;
    _21_sharedCache = software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Shared(_20_sharedCacheInput);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _15_keyStoreClientRegionWest, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _21_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("partitionIdHK1"))));
    _22_valueOrError7 = _out7;
    if (!(!((_22_valueOrError7).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(668,29): " + java.lang.String.valueOf(_22_valueOrError7));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _23_hierarchyKeyring1;
    _23_hierarchyKeyring1 = (_22_valueOrError7).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _18_keyStoreClientRegionEast, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _21_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("partitionIdHK2"))));
    _24_valueOrError8 = _out8;
    if (!(!((_24_valueOrError8).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(683,29): " + java.lang.String.valueOf(_24_valueOrError8));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _25_hierarchyKeyring2;
    _25_hierarchyKeyring2 = (_24_valueOrError8).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _26_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out9;
    _out9 = __default.GetTestMaterials(__default.TEST__ESDK__ALG__SUITE__ID());
    _26_materials = _out9;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_encryptionMaterialsOutMismatchedRegion;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_25_hierarchyKeyring2).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_26_materials));
    _27_encryptionMaterialsOutMismatchedRegion = _out10;
    if (!((_27_encryptionMaterialsOutMismatchedRegion).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(704,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    __default.TestRoundtrip(_23_hierarchyKeyring1, _26_materials, __default.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_encryptionMaterialsOutMismatchedRegionFromCache;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = (_25_hierarchyKeyring2).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_26_materials));
    _28_encryptionMaterialsOutMismatchedRegionFromCache = _out11;
    if (!((_28_encryptionMaterialsOutMismatchedRegionFromCache).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(718,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestSharedCacheWithSamePartitionIdAndDifferentLogicalKeyStoreName()
  {
    dafny.DafnySequence<? extends Character> _0_branchKeyIdWest;
    _0_branchKeyIdWest = __default.BRANCH__KEY__ID();
    long _1_ttl;
    _1_ttl = (long) (long) (((long) (long) (((long) 1L) * ((long) 60000L))) * ((long) 10L));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _2_valueOrError0 = _out0;
    if (!(!((_2_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(726,15): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _3_mpl;
    _3_mpl = (_2_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _4_regionWest;
    _4_regionWest = dafny.DafnySequence.asString("us-west-2");
    dafny.DafnySequence<? extends Character> _5_regionEast;
    _5_regionEast = dafny.DafnySequence.asString("us-east-2");
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _6_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_4_regionWest);
    _6_valueOrError1 = _out1;
    if (!(!((_6_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(731,25): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _7_kmsClientWest;
    _7_kmsClientWest = (_6_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion(_5_regionEast);
    _8_valueOrError2 = _out2;
    if (!(!((_8_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(732,25): " + java.lang.String.valueOf(_8_valueOrError2));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _9_kmsClientEast;
    _9_kmsClientEast = (_8_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(733,21): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _11_ddbClient;
    _11_ddbClient = (_10_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _12_kmsConfig;
    _12_kmsConfig = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.keyArn());
    dafny.DafnySequence<? extends Character> _13_logicalKeyStoreName;
    _13_logicalKeyStoreName = __default.logicalKeyStoreName();
    dafny.DafnySequence<? extends Character> _14_logicalKeyStoreNameNew;
    _14_logicalKeyStoreNameNew = dafny.DafnySequence.<Character>concatenate(_13_logicalKeyStoreName, dafny.DafnySequence.asString("New"));
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _15_keyStoreConfigClientRegionWest;
    _15_keyStoreConfigClientRegionWest = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, _13_logicalKeyStoreName, Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _7_kmsClientWest));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _16_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
    _out4 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_15_keyStoreConfigClientRegionWest);
    _16_valueOrError4 = _out4;
    if (!(!((_16_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(753,36): " + java.lang.String.valueOf(_16_valueOrError4));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _17_keyStoreClientRegionWest;
    _17_keyStoreClientRegionWest = (_16_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig _18_keyStoreConfigClientRegionEast;
    _18_keyStoreConfigClientRegionEast = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(__default.branchKeyStoreName(), _12_kmsConfig, _14_logicalKeyStoreNameNew, Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), _11_ddbClient), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _9_kmsClientEast));
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _19_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _out5;
    _out5 = software.amazon.cryptography.keystore.internaldafny.__default.KeyStore(_18_keyStoreConfigClientRegionEast);
    _19_valueOrError5 = _out5;
    if (!(!((_19_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(770,36): " + java.lang.String.valueOf(_19_valueOrError5));
    }
    software.amazon.cryptography.keystore.internaldafny.KeyStoreClient _20_keyStoreClientRegionEast;
    _20_keyStoreClientRegionEast = (_19_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_3_mpl).CreateCryptographicMaterialsCache(software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Default(software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache.create(100))));
    _21_valueOrError6 = _out6;
    if (!(!((_21_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(773,28): " + java.lang.String.valueOf(_21_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _22_sharedCacheInput;
    _22_sharedCacheInput = (_21_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.CacheType _23_sharedCache;
    _23_sharedCache = software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Shared(_22_sharedCacheInput);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _17_keyStoreClientRegionWest, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _23_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("partitionId"))));
    _24_valueOrError7 = _out7;
    if (!(!((_24_valueOrError7).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(791,29): " + java.lang.String.valueOf(_24_valueOrError7));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _25_hierarchyKeyring1;
    _25_hierarchyKeyring1 = (_24_valueOrError7).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_3_mpl).CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_branchKeyIdWest), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _20_keyStoreClientRegionEast, _1_ttl, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor(), _23_sharedCache), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("partitionId"))));
    _26_valueOrError8 = _out8;
    if (!(!((_26_valueOrError8).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(805,29): " + java.lang.String.valueOf(_26_valueOrError8));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _27_hierarchyKeyring2;
    _27_hierarchyKeyring2 = (_26_valueOrError8).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _28_materials;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out9;
    _out9 = __default.GetTestMaterials(__default.TEST__ESDK__ALG__SUITE__ID());
    _28_materials = _out9;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _29_encryptionMaterialsOutMismatchedRegion;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_27_hierarchyKeyring2).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_28_materials));
    _29_encryptionMaterialsOutMismatchedRegion = _out10;
    if (!((_29_encryptionMaterialsOutMismatchedRegion).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(826,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    __default.TestRoundtrip(_25_hierarchyKeyring1, _28_materials, __default.TEST__ESDK__ALG__SUITE__ID(), _0_branchKeyIdWest);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _30_encryptionMaterialsOutMismatchedRegionFromCache;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = (_27_hierarchyKeyring2).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_28_materials));
    _30_encryptionMaterialsOutMismatchedRegionFromCache = _out11;
    if (!((_30_encryptionMaterialsOutMismatchedRegionFromCache).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(840,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static dafny.DafnySequence<? extends Character> branchKeyStoreName()
  {
    return Fixtures_Compile.__default.branchKeyStoreName();
  }
  public static dafny.DafnySequence<? extends Character> logicalKeyStoreName()
  {
    return __default.branchKeyStoreName();
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__ID()
  {
    return Fixtures_Compile.__default.branchKeyId();
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__ID__A()
  {
    return __default.BRANCH__KEY__ID();
  }
  public static dafny.DafnySequence<? extends Character> keyArn()
  {
    return Fixtures_Compile.__default.keyArn();
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId TEST__ESDK__ALG__SUITE__ID()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId TEST__DBE__ALG__SUITE__ID()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> BRANCH__KEY()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 98, (byte) 114, (byte) 97, (byte) 110, (byte) 99, (byte) 104, (byte) 75, (byte) 101, (byte) 121);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> CASE__A()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 99, (byte) 97, (byte) 115, (byte) 101, (byte) 65);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> CASE__B()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 99, (byte) 97, (byte) 115, (byte) 101, (byte) 66);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__ID__B()
  {
    return Fixtures_Compile.__default.branchKeyIdWithEC();
  }
  @Override
  public java.lang.String toString() {
    return "TestAwsKmsHierarchicalKeyring._default";
  }
}
