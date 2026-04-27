// Class __default
// Dafny class __default compiled into Java
package TestIntermediateKeyWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void IntermediateWrapUnwrapTest()
  {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_encCtx;
    _0_encCtx = dafny.DafnyMap.fromElements();
    java.math.BigInteger _1_keyLen = java.math.BigInteger.ZERO;
    _1_keyLen = java.math.BigInteger.valueOf((((__default.TEST__ALG__SUITE()).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength());
    java.math.BigInteger _2_tagLen = java.math.BigInteger.ZERO;
    _2_tagLen = java.math.BigInteger.valueOf((((__default.TEST__ALG__SUITE()).dtor_encrypt()).dtor_AES__GCM()).dtor_tagLength());
    dafny.DafnySequence<? extends java.lang.Byte> _3_pdk;
    _3_pdk = dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), _1_keyLen, ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_4___v2_boxed0) -> {
      java.math.BigInteger _4___v2 = ((java.math.BigInteger)(java.lang.Object)(_4___v2_boxed0));
      return (byte) 0;
    }));
    TestGenerateAndWrapKeyMaterial _5_testGenerateAndWrap;
    TestGenerateAndWrapKeyMaterial _nw0 = new TestGenerateAndWrapKeyMaterial();
    _nw0.__ctor();
    _5_testGenerateAndWrap = _nw0;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_intermediateWrapOutput;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = IntermediateKeyWrapping_Compile.__default.<TestInfo>IntermediateWrap(TestInfo._typeDescriptor(), _5_testGenerateAndWrap, _3_pdk, __default.TEST__ALG__SUITE(), _0_encCtx);
    _6_intermediateWrapOutput = _out0;
    if (!((_6_intermediateWrapOutput).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(36,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_6_intermediateWrapOutput).dtor_value()).dtor_wrappedMaterial()).length()), ((_1_keyLen).add(_2_tagLen)).add(java.math.BigInteger.valueOf((__default.WRAPPED__MAT()).length()))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(37,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((((_6_intermediateWrapOutput).dtor_value()).dtor_wrappedMaterial()).drop((_1_keyLen).add(_2_tagLen))).equals(__default.WRAPPED__MAT()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(38,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    TestUnwrapKeyMaterial _7_testUnwrap;
    TestUnwrapKeyMaterial _nw1 = new TestUnwrapKeyMaterial();
    _nw1.__ctor();
    _7_testUnwrap = _nw1;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_intermediateUnwrapOutput;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = IntermediateKeyWrapping_Compile.__default.<TestInfo>IntermediateUnwrap(TestInfo._typeDescriptor(), _7_testUnwrap, ((_6_intermediateWrapOutput).dtor_value()).dtor_wrappedMaterial(), __default.TEST__ALG__SUITE(), _0_encCtx);
    _8_intermediateUnwrapOutput = _out1;
    if (!((_8_intermediateUnwrapOutput).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(47,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_8_intermediateUnwrapOutput).dtor_value()).dtor_plaintextDataKey()).equals(_3_pdk))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(48,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_6_intermediateWrapOutput).dtor_value()).dtor_symmetricSigningKey()).equals(((_8_intermediateUnwrapOutput).dtor_value()).dtor_symmetricSigningKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(49,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void IntermediateGenerateAndWrapUnwrapTest()
  {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_encCtx;
    _0_encCtx = dafny.DafnyMap.fromElements();
    java.math.BigInteger _1_keyLen = java.math.BigInteger.ZERO;
    _1_keyLen = java.math.BigInteger.valueOf((((__default.TEST__ALG__SUITE()).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength());
    java.math.BigInteger _2_tagLen = java.math.BigInteger.ZERO;
    _2_tagLen = java.math.BigInteger.valueOf((((__default.TEST__ALG__SUITE()).dtor_encrypt()).dtor_AES__GCM()).dtor_tagLength());
    TestGenerateAndWrapKeyMaterial _3_testGenerateAndWrap;
    TestGenerateAndWrapKeyMaterial _nw0 = new TestGenerateAndWrapKeyMaterial();
    _nw0.__ctor();
    _3_testGenerateAndWrap = _nw0;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_intermediateWrapOutput;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = IntermediateKeyWrapping_Compile.__default.<TestInfo>IntermediateGenerateAndWrap(TestInfo._typeDescriptor(), _3_testGenerateAndWrap, __default.TEST__ALG__SUITE(), _0_encCtx);
    _4_intermediateWrapOutput = _out0;
    if (!((_4_intermediateWrapOutput).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(63,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_4_intermediateWrapOutput).dtor_value()).dtor_wrappedMaterial()).length()), ((_1_keyLen).add(_2_tagLen)).add(java.math.BigInteger.valueOf((__default.WRAPPED__MAT()).length()))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(64,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((((_4_intermediateWrapOutput).dtor_value()).dtor_wrappedMaterial()).drop((_1_keyLen).add(_2_tagLen))).equals(__default.WRAPPED__MAT()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(65,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    TestUnwrapKeyMaterial _5_testUnwrap;
    TestUnwrapKeyMaterial _nw1 = new TestUnwrapKeyMaterial();
    _nw1.__ctor();
    _5_testUnwrap = _nw1;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_intermediateUnwrapOutput;
    Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = IntermediateKeyWrapping_Compile.__default.<TestInfo>IntermediateUnwrap(TestInfo._typeDescriptor(), _5_testUnwrap, ((_4_intermediateWrapOutput).dtor_value()).dtor_wrappedMaterial(), __default.TEST__ALG__SUITE(), _0_encCtx);
    _6_intermediateUnwrapOutput = _out1;
    if (!((_6_intermediateUnwrapOutput).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(74,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_4_intermediateWrapOutput).dtor_value()).dtor_plaintextDataKey()).equals(((_6_intermediateUnwrapOutput).dtor_value()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(75,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((((_4_intermediateWrapOutput).dtor_value()).dtor_symmetricSigningKey()).equals(((_6_intermediateUnwrapOutput).dtor_value()).dtor_symmetricSigningKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(76,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo TEST__ALG__SUITE()
  {
    return AlgorithmSuites_Compile.__default.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384();
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> PLAINTEXT__MAT()
  {
    return dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf((((__default.TEST__ALG__SUITE()).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_0___v0_boxed0) -> {
      java.math.BigInteger _0___v0 = ((java.math.BigInteger)(java.lang.Object)(_0___v0_boxed0));
      return (byte) 1;
    }));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> WRAPPED__MAT()
  {
    return dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf((((__default.TEST__ALG__SUITE()).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_0___v1_boxed0) -> {
      java.math.BigInteger _0___v1 = ((java.math.BigInteger)(java.lang.Object)(_0___v1_boxed0));
      return (byte) 2;
    }));
  }
  @Override
  public java.lang.String toString() {
    return "TestIntermediateKeyWrapping._default";
  }
}
