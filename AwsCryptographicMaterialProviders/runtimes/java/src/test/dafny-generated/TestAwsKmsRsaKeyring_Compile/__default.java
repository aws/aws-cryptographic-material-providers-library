// Class __default
// Dafny class __default compiled into Java
package TestAwsKmsRsaKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestKmsRsaRoundtrip()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(21,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _2_valueOrError1 = UTF8.__default.Encode(TestUtils_Compile.__default.KMS__RSA__PUBLIC__KEY());
    if (!(!((_2_valueOrError1).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(23,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_publicKey;
    _3_publicKey = (_2_valueOrError1).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_1_mpl).CreateDefaultClientSupplier(software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create());
    _4_valueOrError2 = _out1;
    if (!(!((_4_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(25,26): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier _5_clientSupplier;
    _5_clientSupplier = (_4_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_5_clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create(dafny.DafnySequence.asString("us-west-2")));
    _6_valueOrError3 = _out2;
    if (!(!((_6_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(26,21): " + java.lang.String.valueOf(_6_valueOrError3));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _7_kmsClient;
    _7_kmsClient = (_6_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateAwsKmsRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(UTF8.ValidUTF8Bytes._typeDescriptor(), _3_publicKey), TestUtils_Compile.__default.KMS__RSA__PRIVATE__KEY__ARN(), software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__1(), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _7_kmsClient), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _8_valueOrError4 = _out3;
    if (!(!((_8_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(28,25): " + java.lang.String.valueOf(_8_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _9_kmsRsaKeyring;
    _9_kmsRsaKeyring = (_8_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _10_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
    _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _10_encryptionContext = _out4;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _11_algorithmSuiteId;
    _11_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _12_suite;
    _12_suite = AlgorithmSuites_Compile.__default.GetSuite(_11_algorithmSuiteId);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _13_valueOrError5 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_11_algorithmSuiteId, _10_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_13_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(40,33): " + java.lang.String.valueOf(_13_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _14_encryptionMaterialsIn;
    _14_encryptionMaterialsIn = (_13_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_9_kmsRsaKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_14_encryptionMaterialsIn));
    _15_valueOrError6 = _out5;
    if (!(!((_15_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(50,34): " + java.lang.String.valueOf(_15_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _16_encryptionMaterialsOut;
    _16_encryptionMaterialsOut = (_15_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError7 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _17_valueOrError7 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_16_encryptionMaterialsOut).dtor_materials());
    if (!(!((_17_valueOrError7).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(54,13): " + java.lang.String.valueOf(_17_valueOrError7));
    }
    dafny.Tuple0 _18___v0;
    _18___v0 = (_17_valueOrError7).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_16_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(56,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _19_edk;
    _19_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_16_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _20_valueOrError8 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_11_algorithmSuiteId, _10_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_20_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(60,33): " + java.lang.String.valueOf(_20_valueOrError8));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _21_decryptionMaterialsIn;
    _21_decryptionMaterialsIn = (_20_valueOrError8).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError9 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_9_kmsRsaKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_21_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _19_edk)));
    _22_valueOrError9 = _out6;
    if (!(!((_22_valueOrError9).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(67,34): " + java.lang.String.valueOf(_22_valueOrError9));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _23_decryptionMaterialsOut;
    _23_decryptionMaterialsOut = (_22_valueOrError9).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_16_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_23_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(74,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestKmsRsaWithAsymmetricSignatureFails()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(79,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _2_valueOrError1 = UTF8.__default.Encode(TestUtils_Compile.__default.KMS__RSA__PUBLIC__KEY());
    if (!(!((_2_valueOrError1).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(81,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_publicKey;
    _3_publicKey = (_2_valueOrError1).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_1_mpl).CreateDefaultClientSupplier(software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create());
    _4_valueOrError2 = _out1;
    if (!(!((_4_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(83,26): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier _5_clientSupplier;
    _5_clientSupplier = (_4_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_5_clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create(dafny.DafnySequence.asString("us-west-2")));
    _6_valueOrError3 = _out2;
    if (!(!((_6_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(84,21): " + java.lang.String.valueOf(_6_valueOrError3));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _7_kmsClient;
    _7_kmsClient = (_6_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateAwsKmsRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(UTF8.ValidUTF8Bytes._typeDescriptor(), _3_publicKey), TestUtils_Compile.__default.KMS__RSA__PRIVATE__KEY__ARN(), software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__1(), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _7_kmsClient), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _8_valueOrError4 = _out3;
    if (!(!((_8_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(86,25): " + java.lang.String.valueOf(_8_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _9_kmsRsaKeyring;
    _9_kmsRsaKeyring = (_8_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _10_algorithmSuiteId;
    _10_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384());
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _11_suite;
    _11_suite = AlgorithmSuites_Compile.__default.GetSuite(_10_algorithmSuiteId);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _12_valueOrError5 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_10_algorithmSuiteId, dafny.DafnyMap.fromElements(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0))));
    if (!(!((_12_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(96,33): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _13_encryptionMaterialsIn;
    _13_encryptionMaterialsIn = (_12_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_encryptionMaterialsOutRes;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_9_kmsRsaKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_13_encryptionMaterialsIn));
    _14_encryptionMaterialsOutRes = _out4;
    if (!((_14_encryptionMaterialsOutRes).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(110,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_14_encryptionMaterialsOutRes).dtor_error()).is_AwsCryptographicMaterialProvidersException())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(111,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_14_encryptionMaterialsOutRes).dtor_error()).dtor_message()).equals(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("AwsKmsRsaKeyring cannot be used with"), dafny.DafnySequence.asString(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing."))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(112,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _15_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_10_algorithmSuiteId, (_13_encryptionMaterialsIn).dtor_encryptionContext(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_15_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(115,33): " + java.lang.String.valueOf(_15_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _16_decryptionMaterialsIn;
    _16_decryptionMaterialsIn = (_15_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_decryptionMaterialsOutRes;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_9_kmsRsaKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_16_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor())));
    _17_decryptionMaterialsOutRes = _out5;
    if (!((_17_decryptionMaterialsOutRes).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(129,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_17_decryptionMaterialsOutRes).dtor_error()).is_AwsCryptographicMaterialProvidersException())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(130,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_17_decryptionMaterialsOutRes).dtor_error()).dtor_message()).equals(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("AwsKmsRsaKeyring cannot be used with"), dafny.DafnySequence.asString(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing."))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(131,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestAwsKmsRsaKeyring._default";
  }
}
