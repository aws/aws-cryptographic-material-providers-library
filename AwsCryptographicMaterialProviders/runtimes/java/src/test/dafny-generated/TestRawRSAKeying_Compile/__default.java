// Class __default
// Dafny class __default compiled into Java
package TestRawRSAKeying_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestOnEncryptOnDecryptSuppliedDataKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(20,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _2_namespace;
    dafny.DafnySequence<? extends Character> _3_name;
    dafny.DafnySequence<? extends Character> _out1;
    dafny.DafnySequence<? extends Character> _out2;
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _outcollector0 = TestUtils_Compile.__default.NamespaceAndName(java.math.BigInteger.ZERO);
    _out1 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__0();
    _out2 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__1();
    _2_namespace = _out1;
    _3_name = _out2;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _4_keys;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _out3;
    _out3 = __default.GenerateKeyPair(2048);
    _4_keys = _out3;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_1_mpl).CreateRawRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_2_namespace, _3_name, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_publicKey()).dtor_pem()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_privateKey()).dtor_pem())));
    _5_valueOrError1 = _out4;
    if (!(!((_5_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(24,25): " + java.lang.String.valueOf(_5_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawRSAKeyring;
    _6_rawRSAKeyring = (_5_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out5;
    _out5 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _7_encryptionContext = _out5;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(37,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_encryptionMaterialsIn;
    _10_encryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_6_rawRSAKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_10_encryptionMaterialsIn));
    _11_valueOrError3 = _out6;
    if (!(!((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(47,34): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _12_encryptionMaterialsOut;
    _12_encryptionMaterialsOut = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).dtor_materials());
    if (!(!((_13_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(50,13): " + java.lang.String.valueOf(_13_valueOrError4));
    }
    dafny.Tuple0 _14___v0;
    _14___v0 = (_13_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _15_edk;
    _15_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_12_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _16_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_16_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(54,33): " + java.lang.String.valueOf(_16_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _17_decryptionMaterialsIn;
    _17_decryptionMaterialsIn = (_16_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_6_rawRSAKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_17_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _15_edk)));
    _18_valueOrError6 = _out7;
    if (!(!((_18_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(62,34): " + java.lang.String.valueOf(_18_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _19_decryptionMaterialsOut;
    _19_decryptionMaterialsOut = (_18_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_19_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_12_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(74,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnDecryptKeyNameMismatch()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(80,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _2_namespace;
    dafny.DafnySequence<? extends Character> _3_name;
    dafny.DafnySequence<? extends Character> _out1;
    dafny.DafnySequence<? extends Character> _out2;
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _outcollector0 = TestUtils_Compile.__default.NamespaceAndName(java.math.BigInteger.ZERO);
    _out1 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__0();
    _out2 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__1();
    _2_namespace = _out1;
    _3_name = _out2;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _4_keys;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _out3;
    _out3 = __default.GenerateKeyPair(2048);
    _4_keys = _out3;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_1_mpl).CreateRawRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_2_namespace, _3_name, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_publicKey()).dtor_pem()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_privateKey()).dtor_pem())));
    _5_valueOrError1 = _out4;
    if (!(!((_5_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(84,25): " + java.lang.String.valueOf(_5_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawRSAKeyring;
    _6_rawRSAKeyring = (_5_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_1_mpl).CreateRawRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_2_namespace, dafny.DafnySequence.asString("mismatched"), software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_publicKey()).dtor_pem()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_privateKey()).dtor_pem())));
    _7_valueOrError2 = _out5;
    if (!(!((_7_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(92,32): " + java.lang.String.valueOf(_7_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _8_mismatchedRSAKeyring;
    _8_mismatchedRSAKeyring = (_7_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _9_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out6;
    _out6 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _9_encryptionContext = _out6;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _10_algorithmSuiteId;
    _10_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _11_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_10_algorithmSuiteId, _9_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(105,33): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _12_encryptionMaterialsIn;
    _12_encryptionMaterialsIn = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_6_rawRSAKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_12_encryptionMaterialsIn));
    _13_valueOrError4 = _out7;
    if (!(!((_13_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(114,34): " + java.lang.String.valueOf(_13_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _14_encryptionMaterialsOut;
    _14_encryptionMaterialsOut = (_13_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _15_valueOrError5 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_14_encryptionMaterialsOut).dtor_materials());
    if (!(!((_15_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(117,13): " + java.lang.String.valueOf(_15_valueOrError5));
    }
    dafny.Tuple0 _16___v1;
    _16___v1 = (_15_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _17_edk;
    _17_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_14_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _18_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_10_algorithmSuiteId, _9_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_18_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(121,33): " + java.lang.String.valueOf(_18_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _19_decryptionMaterialsIn;
    _19_decryptionMaterialsIn = (_18_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_decryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_8_mismatchedRSAKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_19_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _17_edk)));
    _20_decryptionMaterialsOut = _out8;
    if (!((_20_decryptionMaterialsOut).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(135,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_20_decryptionMaterialsOut).dtor_error()).is_CollectionOfErrors())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(136,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_20_decryptionMaterialsOut).dtor_error()).dtor_list()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(137,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)((((_20_decryptionMaterialsOut).dtor_error()).dtor_list()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_AwsCryptographicMaterialProvidersException())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(138,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)((((_20_decryptionMaterialsOut).dtor_error()).dtor_list()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_message()).equals(ErrorMessages_Compile.__default.IncorrectRawDataKeys(dafny.DafnySequence.asString("0"), dafny.DafnySequence.asString("RSAKeyring"), _2_namespace)))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(139,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnDecryptFailure()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(145,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _2_namespace;
    dafny.DafnySequence<? extends Character> _3_name;
    dafny.DafnySequence<? extends Character> _out1;
    dafny.DafnySequence<? extends Character> _out2;
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _outcollector0 = TestUtils_Compile.__default.NamespaceAndName(java.math.BigInteger.ZERO);
    _out1 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__0();
    _out2 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__1();
    _2_namespace = _out1;
    _3_name = _out2;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _4_encryptKeys;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _out3;
    _out3 = __default.GenerateKeyPair(2048);
    _4_encryptKeys = _out3;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _5_decryptKeys;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _out4;
    _out4 = __default.GenerateKeyPair(2048);
    _5_decryptKeys = _out4;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_1_mpl).CreateRawRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_2_namespace, _3_name, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_encryptKeys).dtor_publicKey()).dtor_pem()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_encryptKeys).dtor_privateKey()).dtor_pem())));
    _6_valueOrError1 = _out5;
    if (!(!((_6_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(153,26): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _7_encryptKeyring;
    _7_encryptKeyring = (_6_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_1_mpl).CreateRawRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_2_namespace, _3_name, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_5_decryptKeys).dtor_publicKey()).dtor_pem()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_5_decryptKeys).dtor_privateKey()).dtor_pem())));
    _8_valueOrError2 = _out6;
    if (!(!((_8_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(161,26): " + java.lang.String.valueOf(_8_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _9_decryptKeyring;
    _9_decryptKeyring = (_8_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _10_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out7;
    _out7 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _10_encryptionContext = _out7;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _11_algorithmSuiteId;
    _11_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _12_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_11_algorithmSuiteId, _10_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_12_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(172,33): " + java.lang.String.valueOf(_12_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _13_encryptionMaterialsIn;
    _13_encryptionMaterialsIn = (_12_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_7_encryptKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_13_encryptionMaterialsIn));
    _14_valueOrError4 = _out8;
    if (!(!((_14_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(181,34): " + java.lang.String.valueOf(_14_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _15_encryptionMaterialsOut;
    _15_encryptionMaterialsOut = (_14_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _16_valueOrError5 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_15_encryptionMaterialsOut).dtor_materials());
    if (!(!((_16_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(184,13): " + java.lang.String.valueOf(_16_valueOrError5));
    }
    dafny.Tuple0 _17___v2;
    _17___v2 = (_16_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _18_edk;
    _18_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_15_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _19_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_11_algorithmSuiteId, _10_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_19_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(188,33): " + java.lang.String.valueOf(_19_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _20_decryptionMaterialsIn;
    _20_decryptionMaterialsIn = (_19_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_decryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_9_decryptKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_20_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _18_edk)));
    _21_decryptionMaterialsOut = _out9;
    if (!((_21_decryptionMaterialsOut).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(206,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnDecryptBadAndGoodEdkSucceeds()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(218,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _2_namespace;
    dafny.DafnySequence<? extends Character> _3_name;
    dafny.DafnySequence<? extends Character> _out1;
    dafny.DafnySequence<? extends Character> _out2;
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _outcollector0 = TestUtils_Compile.__default.NamespaceAndName(java.math.BigInteger.ZERO);
    _out1 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__0();
    _out2 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__1();
    _2_namespace = _out1;
    _3_name = _out2;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _4_keys;
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput _out3;
    _out3 = __default.GenerateKeyPair(2048);
    _4_keys = _out3;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_1_mpl).CreateRawRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_2_namespace, _3_name, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_publicKey()).dtor_pem()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_4_keys).dtor_privateKey()).dtor_pem())));
    _5_valueOrError1 = _out4;
    if (!(!((_5_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(222,25): " + java.lang.String.valueOf(_5_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawRSAKeyring;
    _6_rawRSAKeyring = (_5_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out5;
    _out5 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _7_encryptionContext = _out5;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(235,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_encryptionMaterialsIn;
    _10_encryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_6_rawRSAKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_10_encryptionMaterialsIn));
    _11_valueOrError3 = _out6;
    if (!(!((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(244,34): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _12_encryptionMaterialsOut;
    _12_encryptionMaterialsOut = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).dtor_materials());
    if (!(!((_13_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(247,13): " + java.lang.String.valueOf(_13_valueOrError4));
    }
    dafny.Tuple0 _14___v3;
    _14___v3 = (_13_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _15_edk;
    _15_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_12_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _16_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_16_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(251,33): " + java.lang.String.valueOf(_16_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _17_decryptionMaterialsIn;
    _17_decryptionMaterialsIn = (_16_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _18_fakeEdk;
    _18_fakeEdk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create((_15_edk).dtor_keyProviderId(), (_15_edk).dtor_keyProviderInfo(), dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(((_15_edk).dtor_ciphertext()).length()), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_19_i_boxed0) -> {
  java.math.BigInteger _19_i = ((java.math.BigInteger)(java.lang.Object)(_19_i_boxed0));
  return (byte) 0;
})));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_6_rawRSAKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_17_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _18_fakeEdk, _15_edk)));
    _20_valueOrError6 = _out7;
    if (!(!((_20_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(268,34): " + java.lang.String.valueOf(_20_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _21_decryptionMaterialsOut;
    _21_decryptionMaterialsOut = (_20_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_21_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_12_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(279,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput GenerateKeyPair(int keyModulusLength)
  {
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput keys = (software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
      _0_valueOrError0 = _out0;
      if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(286,18): " + java.lang.String.valueOf(_0_valueOrError0));
      }
      software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _1_crypto;
      _1_crypto = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
      _out1 = (_1_crypto).GenerateRSAKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairInput.create(keyModulusLength));
      _2_valueOrError1 = _out1;
      if (!(!((_2_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(288,12): " + java.lang.String.valueOf(_2_valueOrError1));
      }
      keys = (_2_valueOrError1).Extract(software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    }
    return keys;
  }
  @Override
  public java.lang.String toString() {
    return "TestRawRSAKeying._default";
  }
}
