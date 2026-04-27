// Class __default
// Dafny class __default compiled into Java
package TestRawAESKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestOnEncryptOnDecryptGenerateDataKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(20,15): " + java.lang.String.valueOf(_0_valueOrError0));
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, _3_name, dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_5_i_boxed0) -> {
  java.math.BigInteger _5_i = ((java.math.BigInteger)(java.lang.Object)(_5_i_boxed0));
  return (byte) 0;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _4_valueOrError1 = _out3;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(23,25): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawAESKeyring;
    _6_rawAESKeyring = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
    _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _7_encryptionContext = _out4;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(32,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_encryptionMaterialsIn;
    _10_encryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_6_rawAESKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_10_encryptionMaterialsIn));
    _11_valueOrError3 = _out5;
    if (!(!((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(42,34): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _12_encryptionMaterialsOut;
    _12_encryptionMaterialsOut = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).dtor_materials());
    if (!(!((_13_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(57,13): " + java.lang.String.valueOf(_13_valueOrError4));
    }
    dafny.Tuple0 _14___v0;
    _14___v0 = (_13_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_12_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(64,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _15_edk;
    _15_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_12_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _16_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_16_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(68,33): " + java.lang.String.valueOf(_16_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _17_decryptionMaterialsIn;
    _17_decryptionMaterialsIn = (_16_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_6_rawAESKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_17_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _15_edk)));
    _18_valueOrError6 = _out6;
    if (!(!((_18_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(75,34): " + java.lang.String.valueOf(_18_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _19_decryptionMaterialsOut;
    _19_decryptionMaterialsOut = (_18_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_12_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_12_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(86,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnEncryptOnDecryptSuppliedDataKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(93,15): " + java.lang.String.valueOf(_0_valueOrError0));
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, _3_name, dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_5_i_boxed0) -> {
  java.math.BigInteger _5_i = ((java.math.BigInteger)(java.lang.Object)(_5_i_boxed0));
  return (byte) 0;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _4_valueOrError1 = _out3;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(96,25): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawAESKeyring;
    _6_rawAESKeyring = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
    _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _7_encryptionContext = _out4;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(105,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_encryptionMaterialsIn;
    _10_encryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _11_pdk;
    _11_pdk = dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_12_i_boxed0) -> {
      java.math.BigInteger _12_i = ((java.math.BigInteger)(java.lang.Object)(_12_i_boxed0));
      return (byte) 0;
    }));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    dafny.DafnySequence<? extends java.lang.Byte> _pat_let_tv0 = _11_pdk;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_6_rawAESKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>Let(_10_encryptionMaterialsIn, boxed6 -> {
  software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _pat_let3_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)(java.lang.Object)(boxed6));
  return ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>Let(_pat_let3_0, boxed7 -> {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _14_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)(java.lang.Object)(boxed7));
    return ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>Let(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _pat_let_tv0), boxed8 -> {
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _pat_let4_0 = ((Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(boxed8));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>Let(_pat_let4_0, boxed9 -> {
        Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _15_dt__update_hplaintextDataKey_h0 = ((Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(boxed9));
        return software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create((_14_dt__update__tmp_h0).dtor_algorithmSuite(), (_14_dt__update__tmp_h0).dtor_encryptionContext(), (_14_dt__update__tmp_h0).dtor_encryptedDataKeys(), (_14_dt__update__tmp_h0).dtor_requiredEncryptionContextKeys(), _15_dt__update_hplaintextDataKey_h0, (_14_dt__update__tmp_h0).dtor_signingKey(), (_14_dt__update__tmp_h0).dtor_symmetricSigningKeys());
      }
      )));
    }
    )));
  }
  )));
}
)))));
    _13_valueOrError3 = _out5;
    if (!(!((_13_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(120,34): " + java.lang.String.valueOf(_13_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _16_encryptionMaterialsOut;
    _16_encryptionMaterialsOut = (_13_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _17_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_16_encryptionMaterialsOut).dtor_materials());
    if (!(!((_17_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(124,13): " + java.lang.String.valueOf(_17_valueOrError4));
    }
    dafny.Tuple0 _18___v1;
    _18___v1 = (_17_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _19_edk;
    _19_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_16_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _20_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_20_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(128,33): " + java.lang.String.valueOf(_20_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _21_decryptionMaterialsIn;
    _21_decryptionMaterialsIn = (_20_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_6_rawAESKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_21_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _19_edk)));
    _22_valueOrError6 = _out6;
    if (!(!((_22_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(136,34): " + java.lang.String.valueOf(_22_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _23_decryptionMaterialsOut;
    _23_decryptionMaterialsOut = (_22_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_23_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_pdk)))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(148,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnDecryptKeyNameMismatch()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(154,15): " + java.lang.String.valueOf(_0_valueOrError0));
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, _3_name, dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_5_i_boxed0) -> {
  java.math.BigInteger _5_i = ((java.math.BigInteger)(java.lang.Object)(_5_i_boxed0));
  return (byte) 0;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _4_valueOrError1 = _out3;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(157,25): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawAESKeyring;
    _6_rawAESKeyring = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, dafny.DafnySequence.asString("mismatched"), dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_8_i_boxed0) -> {
  java.math.BigInteger _8_i = ((java.math.BigInteger)(java.lang.Object)(_8_i_boxed0));
  return (byte) 1;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _7_valueOrError2 = _out4;
    if (!(!((_7_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(164,32): " + java.lang.String.valueOf(_7_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _9_mismatchedAESKeyring;
    _9_mismatchedAESKeyring = (_7_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _10_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out5;
    _out5 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _10_encryptionContext = _out5;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _11_algorithmSuiteId;
    _11_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _12_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_11_algorithmSuiteId, _10_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_12_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(174,33): " + java.lang.String.valueOf(_12_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _13_encryptionMaterialsIn;
    _13_encryptionMaterialsIn = (_12_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_6_rawAESKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_13_encryptionMaterialsIn));
    _14_valueOrError4 = _out6;
    if (!(!((_14_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(184,34): " + java.lang.String.valueOf(_14_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _15_encryptionMaterialsOut;
    _15_encryptionMaterialsOut = (_14_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _16_valueOrError5 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_15_encryptionMaterialsOut).dtor_materials());
    if (!(!((_16_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(188,13): " + java.lang.String.valueOf(_16_valueOrError5));
    }
    dafny.Tuple0 _17___v2;
    _17___v2 = (_16_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _18_edk;
    _18_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_15_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _19_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_11_algorithmSuiteId, _10_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_19_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(192,33): " + java.lang.String.valueOf(_19_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _20_decryptionMaterialsIn;
    _20_decryptionMaterialsIn = (_19_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_decryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_9_mismatchedAESKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_20_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _18_edk)));
    _21_decryptionMaterialsOut = _out7;
    if (!((_21_decryptionMaterialsOut).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(205,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_21_decryptionMaterialsOut).dtor_error()).is_CollectionOfErrors())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_21_decryptionMaterialsOut).dtor_error()).dtor_list()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(207,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)((((_21_decryptionMaterialsOut).dtor_error()).dtor_list()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).is_AwsCryptographicMaterialProvidersException())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(208,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)((((_21_decryptionMaterialsOut).dtor_error()).dtor_list()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor_message()).equals(ErrorMessages_Compile.__default.IncorrectRawDataKeys(dafny.DafnySequence.asString("0"), dafny.DafnySequence.asString("AESKeyring"), _2_namespace)))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(209,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnDecryptBadAndGoodEdkSucceeds()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,15): " + java.lang.String.valueOf(_0_valueOrError0));
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, _3_name, dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_5_i_boxed0) -> {
  java.math.BigInteger _5_i = ((java.math.BigInteger)(java.lang.Object)(_5_i_boxed0));
  return (byte) 0;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _4_valueOrError1 = _out3;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(218,25): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawAESKeyring;
    _6_rawAESKeyring = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
    _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _7_encryptionContext = _out4;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(227,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_encryptionMaterialsIn;
    _10_encryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_6_rawAESKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_10_encryptionMaterialsIn));
    _11_valueOrError3 = _out5;
    if (!(!((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(237,34): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _12_encryptionMaterialsOut;
    _12_encryptionMaterialsOut = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).dtor_materials());
    if (!(!((_13_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(241,13): " + java.lang.String.valueOf(_13_valueOrError4));
    }
    dafny.Tuple0 _14___v3;
    _14___v3 = (_13_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _15_edk;
    _15_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_12_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _16_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_16_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(245,33): " + java.lang.String.valueOf(_16_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _17_decryptionMaterialsIn;
    _17_decryptionMaterialsIn = (_16_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _18_fakeEdk;
    _18_fakeEdk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create((_15_edk).dtor_keyProviderId(), (_15_edk).dtor_keyProviderInfo(), dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(((_15_edk).dtor_ciphertext()).length()), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_19_i_boxed0) -> {
  java.math.BigInteger _19_i = ((java.math.BigInteger)(java.lang.Object)(_19_i_boxed0));
  return (byte) 0;
})));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_6_rawAESKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_17_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _18_fakeEdk, _15_edk)));
    _20_valueOrError6 = _out6;
    if (!(!((_20_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(258,34): " + java.lang.String.valueOf(_20_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _21_decryptionMaterialsOut;
    _21_decryptionMaterialsOut = (_20_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_21_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_12_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(265,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnDecryptNoEDKs()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,15): " + java.lang.String.valueOf(_0_valueOrError0));
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, _3_name, dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_5_i_boxed0) -> {
  java.math.BigInteger _5_i = ((java.math.BigInteger)(java.lang.Object)(_5_i_boxed0));
  return (byte) 0;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _4_valueOrError1 = _out3;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(274,25): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawAESKeyring;
    _6_rawAESKeyring = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
    _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _7_encryptionContext = _out4;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(283,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _10_decryptionMaterialsIn;
    _10_decryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_decryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_6_rawAESKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_10_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor())));
    _11_decryptionMaterialsOut = _out5;
    if (!((_11_decryptionMaterialsOut).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(296,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnEncryptUnserializableEC()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,15): " + java.lang.String.valueOf(_0_valueOrError0));
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, _3_name, dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_5_i_boxed0) -> {
  java.math.BigInteger _5_i = ((java.math.BigInteger)(java.lang.Object)(_5_i_boxed0));
  return (byte) 0;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _4_valueOrError1 = _out3;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(308,25): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawAESKeyring;
    _6_rawAESKeyring = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_unserializableEncryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
    _out4 = __default.generateUnserializableEncryptionContext();
    _7_unserializableEncryptionContext = _out4;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_8_algorithmSuiteId, _7_unserializableEncryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(317,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_encryptionMaterialsIn;
    _10_encryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_encryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_6_rawAESKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_10_encryptionMaterialsIn));
    _11_encryptionMaterialsOut = _out5;
    if (!((_11_encryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(329,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestOnDecryptUnserializableEC()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,15): " + java.lang.String.valueOf(_0_valueOrError0));
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
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_2_namespace, _3_name, dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(32L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_5_i_boxed0) -> {
  java.math.BigInteger _5_i = ((java.math.BigInteger)(java.lang.Object)(_5_i_boxed0));
  return (byte) 0;
})), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16()));
    _4_valueOrError1 = _out3;
    if (!(!((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(342,25): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _6_rawAESKeyring;
    _6_rawAESKeyring = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
    _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _7_encryptionContext = _out4;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _8_algorithmSuiteId;
    _8_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _9_valueOrError2 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_8_algorithmSuiteId, _7_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_9_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(351,33): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _10_encryptionMaterialsIn;
    _10_encryptionMaterialsIn = (_9_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_6_rawAESKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_10_encryptionMaterialsIn));
    _11_valueOrError3 = _out5;
    if (!(!((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(361,34): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _12_encryptionMaterialsOut;
    _12_encryptionMaterialsOut = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _13_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_12_encryptionMaterialsOut).dtor_materials());
    if (!(!((_13_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(364,13): " + java.lang.String.valueOf(_13_valueOrError4));
    }
    dafny.Tuple0 _14___v4;
    _14___v4 = (_13_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _15_edk;
    _15_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_12_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _16_unserializableEncryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out6;
    _out6 = __default.generateUnserializableEncryptionContext();
    _16_unserializableEncryptionContext = _out6;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _17_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_8_algorithmSuiteId, _16_unserializableEncryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_17_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(369,33): " + java.lang.String.valueOf(_17_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _18_decryptionMaterialsIn;
    _18_decryptionMaterialsIn = (_17_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_decryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_6_rawAESKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_18_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _15_edk)));
    _19_decryptionMaterialsOut = _out7;
    if (!((_19_decryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(382,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> generateUnserializableEncryptionContext()
  {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encCtx = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _0_valueOrError0 = UTF8.__default.Encode(dafny.DafnySequence.asString("keyA"));
    if (!(!((_0_valueOrError0).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(387,16): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_keyA;
    _1_keyA = (_0_valueOrError0).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends java.lang.Byte> _2_invalidVal;
    _2_invalidVal = dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(65536L), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_3___v5_boxed0) -> {
      java.math.BigInteger _3___v5 = ((java.math.BigInteger)(java.lang.Object)(_3___v5_boxed0));
      return (byte) 0;
    }));
    encCtx = dafny.DafnyMap.fromElements(new dafny.Tuple2(_1_keyA, _2_invalidVal));
    return encCtx;
  }
  @Override
  public java.lang.String toString() {
    return "TestRawAESKeyring._default";
  }
}
