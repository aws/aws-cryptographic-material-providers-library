// Class __default
// Dafny class __default compiled into Java
package IntermediateKeyWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> GetIvLengthZeros(int len) {
    if ((len) == (12)) {
      return dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0, (byte) 0);
    } else {
      return dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf(len), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_0___v0_boxed0) -> {
        java.math.BigInteger _0___v0 = ((java.math.BigInteger)(java.lang.Object)(_0___v0_boxed0));
        return (byte) 0;
      }));
    }
  }
  public static <__T> Wrappers_Compile.Result<IntermediateUnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> IntermediateUnwrap(dafny.TypeDescriptor<__T> _td___T, MaterialWrapping_Compile.UnwrapMaterial<__T> unwrap, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext)
  {
    Wrappers_Compile.Result<IntermediateUnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<IntermediateUnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeCrypto;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _0_maybeCrypto = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _1_valueOrError0 = (_0_maybeCrypto).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<IntermediateUnwrapOutput<__T>>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient _3_cryptoPrimitivesX;
    _3_cryptoPrimitivesX = (_1_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _4_cryptoPrimitives;
    _4_cryptoPrimitives = ((software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient)(java.lang.Object)(_3_cryptoPrimitivesX));
    Wrappers_Compile.Result<DeserializedIntermediateWrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<DeserializedIntermediateWrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(DeserializedIntermediateWrappedMaterial._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), DeserializedIntermediateWrappedMaterial.Default());
    _5_valueOrError1 = __default.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite);
    if ((_5_valueOrError1).IsFailure(DeserializedIntermediateWrappedMaterial._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<IntermediateUnwrapOutput<__T>>PropagateFailure(DeserializedIntermediateWrappedMaterial._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    DeserializedIntermediateWrappedMaterial _6_deserializedWrapped;
    _6_deserializedWrapped = (_5_valueOrError1).Extract(DeserializedIntermediateWrappedMaterial._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    DeserializedIntermediateWrappedMaterial _let_tmp_rhs0 = _6_deserializedWrapped;
    dafny.DafnySequence<? extends java.lang.Byte> _7_encryptedPdk = ((IntermediateKeyWrapping_Compile.DeserializedIntermediateWrappedMaterial)_let_tmp_rhs0)._encryptedPdk;
    dafny.DafnySequence<? extends java.lang.Byte> _8_providerWrappedIkm = ((IntermediateKeyWrapping_Compile.DeserializedIntermediateWrappedMaterial)_let_tmp_rhs0)._providerWrappedIkm;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_serializedEC;
    _9_serializedEC = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD(encryptionContext);
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError2 = (Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (unwrap).Invoke(MaterialWrapping_Compile.UnwrapInput.create(_8_providerWrappedIkm, algorithmSuite, encryptionContext, _9_serializedEC));
    _10_valueOrError2 = _out1;
    if ((_10_valueOrError2).IsFailure(MaterialWrapping_Compile.UnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError2).<IntermediateUnwrapOutput<__T>>PropagateFailure(MaterialWrapping_Compile.UnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    MaterialWrapping_Compile.UnwrapOutput<__T> _11_unwrapOutput;
    _11_unwrapOutput = (_10_valueOrError2).Extract(MaterialWrapping_Compile.UnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.UnwrapOutput<__T> _let_tmp_rhs1 = _11_unwrapOutput;
    dafny.DafnySequence<? extends java.lang.Byte> _12_intermediateMaterial = ((MaterialWrapping_Compile.UnwrapOutput<__T>)_let_tmp_rhs1)._unwrappedMaterial;
    __T _13_unwrapInfo = ((MaterialWrapping_Compile.UnwrapOutput<__T>)_let_tmp_rhs1)._unwrapInfo;
    Wrappers_Compile.Result<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError3 = Wrappers_Compile.Result.<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), PdkEncryptionAndSymmetricSigningKeys.Default());
    Wrappers_Compile.Result<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = __default.DeriveKeysFromIntermediateMaterial(_12_intermediateMaterial, algorithmSuite, encryptionContext, _4_cryptoPrimitives);
    _14_valueOrError3 = _out2;
    if ((_14_valueOrError3).IsFailure(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_14_valueOrError3).<IntermediateUnwrapOutput<__T>>PropagateFailure(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    PdkEncryptionAndSymmetricSigningKeys _15_derivedKeys;
    _15_derivedKeys = (_14_valueOrError3).Extract(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    PdkEncryptionAndSymmetricSigningKeys _let_tmp_rhs2 = _15_derivedKeys;
    dafny.DafnySequence<? extends java.lang.Byte> _16_pdkEncryptionKey = ((IntermediateKeyWrapping_Compile.PdkEncryptionAndSymmetricSigningKeys)_let_tmp_rhs2)._pdkEncryptionKey;
    dafny.DafnySequence<? extends java.lang.Byte> _17_symmetricSigningKey = ((IntermediateKeyWrapping_Compile.PdkEncryptionAndSymmetricSigningKeys)_let_tmp_rhs2)._symmetricSigningKey;
    dafny.DafnySequence<? extends java.lang.Byte> _18_iv;
    _18_iv = __default.GetIvLengthZeros(AlgorithmSuites_Compile.__default.GetEncryptIvLength(algorithmSuite));
    long _19_tagIndex;
    _19_tagIndex = (long) (long) (((long) (_7_encryptedPdk).cardinalityInt()) - (((long) (AlgorithmSuites_Compile.__default.GetEncryptTagLength(algorithmSuite)))));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _20_valueOrError4 = _9_serializedEC;
    if ((_20_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_20_valueOrError4).<IntermediateUnwrapOutput<__T>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _21_aad;
    _21_aad = (_20_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput _22_decInput;
    _22_decInput = software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput.create(((algorithmSuite).dtor_encrypt()).dtor_AES__GCM(), _16_pdkEncryptionKey, (_7_encryptedPdk).take(_19_tagIndex), (_7_encryptedPdk).drop(_19_tagIndex), _18_iv, _21_aad);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _23_decOutR;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out3;
    _out3 = (_4_cryptoPrimitives).AESDecrypt(_22_decInput);
    _23_decOutR = _out3;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _24_valueOrError5 = (_23_decOutR).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_25_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _25_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_25_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_25_e);
    }));
    if ((_24_valueOrError5).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_24_valueOrError5).<IntermediateUnwrapOutput<__T>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _26_plaintextDataKey;
    _26_plaintextDataKey = (_24_valueOrError5).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<IntermediateUnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateUnwrapOutput.<__T>create(_td___T, _26_plaintextDataKey, _17_symmetricSigningKey, _13_unwrapInfo));
    return res;
  }
  public static <__T> Wrappers_Compile.Result<IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> IntermediateWrap(dafny.TypeDescriptor<__T> _td___T, MaterialWrapping_Compile.GenerateAndWrapMaterial<__T> generateAndWrap, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext)
  {
    Wrappers_Compile.Result<IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeCrypto;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _0_maybeCrypto = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _1_valueOrError0 = (_0_maybeCrypto).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<IntermediateWrapOutput<__T>>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient _3_cryptoPrimitivesX;
    _3_cryptoPrimitivesX = (_1_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _4_cryptoPrimitives;
    _4_cryptoPrimitives = ((software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient)(java.lang.Object)(_3_cryptoPrimitivesX));
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = (Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (generateAndWrap).Invoke(MaterialWrapping_Compile.GenerateAndWrapInput.create(algorithmSuite, encryptionContext, CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD(encryptionContext)));
    _5_valueOrError1 = _out1;
    if ((_5_valueOrError1).IsFailure(MaterialWrapping_Compile.GenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<IntermediateWrapOutput<__T>>PropagateFailure(MaterialWrapping_Compile.GenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    MaterialWrapping_Compile.GenerateAndWrapOutput<__T> _6_generateAndWrapOutput;
    _6_generateAndWrapOutput = (_5_valueOrError1).Extract(MaterialWrapping_Compile.GenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.GenerateAndWrapOutput<__T> _let_tmp_rhs0 = _6_generateAndWrapOutput;
    dafny.DafnySequence<? extends java.lang.Byte> _7_intermediateMaterial = ((MaterialWrapping_Compile.GenerateAndWrapOutput<__T>)_let_tmp_rhs0)._plaintextMaterial;
    dafny.DafnySequence<? extends java.lang.Byte> _8_providerWrappedIkm = ((MaterialWrapping_Compile.GenerateAndWrapOutput<__T>)_let_tmp_rhs0)._wrappedMaterial;
    __T _9_wrapInfo = ((MaterialWrapping_Compile.GenerateAndWrapOutput<__T>)_let_tmp_rhs0)._wrapInfo;
    Wrappers_Compile.Result<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError2 = Wrappers_Compile.Result.<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), PdkEncryptionAndSymmetricSigningKeys.Default());
    Wrappers_Compile.Result<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = __default.DeriveKeysFromIntermediateMaterial(_7_intermediateMaterial, algorithmSuite, encryptionContext, _4_cryptoPrimitives);
    _10_valueOrError2 = _out2;
    if ((_10_valueOrError2).IsFailure(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError2).<IntermediateWrapOutput<__T>>PropagateFailure(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    PdkEncryptionAndSymmetricSigningKeys _11_derivedKeys;
    _11_derivedKeys = (_10_valueOrError2).Extract(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    PdkEncryptionAndSymmetricSigningKeys _let_tmp_rhs1 = _11_derivedKeys;
    dafny.DafnySequence<? extends java.lang.Byte> _12_pdkEncryptionKey = ((IntermediateKeyWrapping_Compile.PdkEncryptionAndSymmetricSigningKeys)_let_tmp_rhs1)._pdkEncryptionKey;
    dafny.DafnySequence<? extends java.lang.Byte> _13_symmetricSigningKey = ((IntermediateKeyWrapping_Compile.PdkEncryptionAndSymmetricSigningKeys)_let_tmp_rhs1)._symmetricSigningKey;
    dafny.DafnySequence<? extends java.lang.Byte> _14_iv;
    _14_iv = __default.GetIvLengthZeros(AlgorithmSuites_Compile.__default.GetEncryptIvLength(algorithmSuite));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _15_valueOrError3 = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD(encryptionContext);
    if ((_15_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_15_valueOrError3).<IntermediateWrapOutput<__T>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _16_aad;
    _16_aad = (_15_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput _17_encInput;
    _17_encInput = software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput.create(((algorithmSuite).dtor_encrypt()).dtor_AES__GCM(), _14_iv, _12_pdkEncryptionKey, plaintextDataKey, _16_aad);
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _18_encOutR;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out3;
    _out3 = (_4_cryptoPrimitives).AESEncrypt(_17_encInput);
    _18_encOutR = _out3;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.Default());
    _19_valueOrError4 = (_18_encOutR).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_20_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _20_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_20_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_20_e);
    }));
    if ((_19_valueOrError4).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_19_valueOrError4).<IntermediateWrapOutput<__T>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput _21_encryptedPdk;
    _21_encryptedPdk = (_19_valueOrError4).Extract(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _22_serializedMaterial;
    _22_serializedMaterial = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate((_21_encryptedPdk).dtor_cipherText(), (_21_encryptedPdk).dtor_authTag()), _8_providerWrappedIkm);
    res = Wrappers_Compile.Result.<IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(IntermediateWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateWrapOutput.<__T>create(_td___T, _22_serializedMaterial, _13_symmetricSigningKey, _9_wrapInfo));
    return res;
  }
  public static <__T> Wrappers_Compile.Result<IntermediateGenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> IntermediateGenerateAndWrap(dafny.TypeDescriptor<__T> _td___T, MaterialWrapping_Compile.GenerateAndWrapMaterial<__T> generateAndWrap, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext)
  {
    Wrappers_Compile.Result<IntermediateGenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<IntermediateGenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeCrypto;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _0_maybeCrypto = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _1_valueOrError0 = (_0_maybeCrypto).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<IntermediateGenerateAndWrapOutput<__T>>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateGenerateAndWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _3_cryptoPrimitives;
    _3_cryptoPrimitives = (_1_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _4_generateBytesResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = (_3_cryptoPrimitives).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create(AlgorithmSuites_Compile.__default.GetEncryptKeyLength(algorithmSuite)));
    _4_generateBytesResult = _out1;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _5_valueOrError1 = (_4_generateBytesResult).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_6_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _6_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_6_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_6_e);
    }));
    if ((_5_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<IntermediateGenerateAndWrapOutput<__T>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateGenerateAndWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _7_plaintextDataKey;
    _7_plaintextDataKey = (_5_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = __default.<__T>IntermediateWrap(_td___T, generateAndWrap, _7_plaintextDataKey, algorithmSuite, encryptionContext);
    _8_valueOrError2 = _out2;
    if ((_8_valueOrError2).IsFailure(IntermediateWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError2).<IntermediateGenerateAndWrapOutput<__T>>PropagateFailure(IntermediateWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateGenerateAndWrapOutput.<__T>_typeDescriptor(_td___T));
      return res;
    }
    IntermediateWrapOutput<__T> _9_wrapOutput;
    _9_wrapOutput = (_8_valueOrError2).Extract(IntermediateWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<IntermediateGenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(IntermediateGenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), IntermediateGenerateAndWrapOutput.<__T>create(_td___T, _7_plaintextDataKey, (_9_wrapOutput).dtor_wrappedMaterial(), (_9_wrapOutput).dtor_symmetricSigningKey(), (_9_wrapOutput).dtor_wrapInfo()));
    return res;
  }
  public static Wrappers_Compile.Result<DeserializedIntermediateWrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DeserializeIntermediateWrappedMaterial(dafny.DafnySequence<? extends java.lang.Byte> material, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algSuite)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) (material).cardinalityInt(), ((long) ((int) ((AlgorithmSuites_Compile.__default.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites_Compile.__default.GetEncryptTagLength(algSuite)))))) >= 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Unable to deserialize Intermediate Key Wrapped material: too short.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<DeserializedIntermediateWrappedMaterial>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), DeserializedIntermediateWrappedMaterial._typeDescriptor());
    } else {
      int _1_encryptedPdkLen = (int) ((AlgorithmSuites_Compile.__default.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites_Compile.__default.GetEncryptTagLength(algSuite)));
      return Wrappers_Compile.Result.<DeserializedIntermediateWrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(DeserializedIntermediateWrappedMaterial._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), DeserializedIntermediateWrappedMaterial.create((material).take(_1_encryptedPdkLen), (material).drop(_1_encryptedPdkLen)));
    }
  }
  public static Wrappers_Compile.Result<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DeriveKeysFromIntermediateMaterial(dafny.DafnySequence<? extends java.lang.Byte> intermediateMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    Wrappers_Compile.Result<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), PdkEncryptionAndSymmetricSigningKeys.Default());
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput _0_hkdfExtractInput;
    _0_hkdfExtractInput = software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput.create((((algorithmSuite).dtor_commitment()).dtor_HKDF()).dtor_hmac(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), intermediateMaterial);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _1_maybePseudoRandomKey;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = (cryptoPrimitives).HkdfExtract(_0_hkdfExtractInput);
    _1_maybePseudoRandomKey = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _2_valueOrError0 = (_1_maybePseudoRandomKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_3_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _3_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_3_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_3_e);
    }));
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<PdkEncryptionAndSymmetricSigningKeys>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), PdkEncryptionAndSymmetricSigningKeys._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _4_pseudoRandomKey;
    _4_pseudoRandomKey = (_2_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput _5_symmetricSigningKeyInput;
    _5_symmetricSigningKeyInput = software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput.create((((algorithmSuite).dtor_commitment()).dtor_HKDF()).dtor_hmac(), _4_pseudoRandomKey, __default.KEYWRAP__MAC__INFO(), (((algorithmSuite).dtor_commitment()).dtor_HKDF()).dtor_outputKeyLength());
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput _6_pdkEncryptionKeyInput;
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput _7_dt__update__tmp_h0 = _5_symmetricSigningKeyInput;
    dafny.DafnySequence<? extends java.lang.Byte> _8_dt__update_hinfo_h0 = __default.KEYWRAP__ENC__INFO();
    _6_pdkEncryptionKeyInput = software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput.create((_7_dt__update__tmp_h0).dtor_digestAlgorithm(), (_7_dt__update__tmp_h0).dtor_prk(), _8_dt__update_hinfo_h0, (_7_dt__update__tmp_h0).dtor_expectedLength());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _9_maybeSymmetricSigningKey;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = (cryptoPrimitives).HkdfExpand(_5_symmetricSigningKeyInput);
    _9_maybeSymmetricSigningKey = _out1;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _10_valueOrError1 = (_9_maybeSymmetricSigningKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_11_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _11_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_11_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_11_e);
    }));
    if ((_10_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError1).<PdkEncryptionAndSymmetricSigningKeys>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), PdkEncryptionAndSymmetricSigningKeys._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _12_symmetricSigningKey;
    _12_symmetricSigningKey = (_10_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _13_maybePdkEncryptionKey;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = (cryptoPrimitives).HkdfExpand(_6_pdkEncryptionKeyInput);
    _13_maybePdkEncryptionKey = _out2;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _14_valueOrError2 = (_13_maybePdkEncryptionKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_15_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _15_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_15_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_15_e);
    }));
    if ((_14_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_14_valueOrError2).<PdkEncryptionAndSymmetricSigningKeys>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), PdkEncryptionAndSymmetricSigningKeys._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _16_pdkEncryptionKey;
    _16_pdkEncryptionKey = (_14_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<PdkEncryptionAndSymmetricSigningKeys, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(PdkEncryptionAndSymmetricSigningKeys._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), PdkEncryptionAndSymmetricSigningKeys.create(_16_pdkEncryptionKey, _12_symmetricSigningKey));
    return res;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> KEYWRAP__MAC__INFO()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 65, (byte) 87, (byte) 83, (byte) 95, (byte) 77, (byte) 80, (byte) 76, (byte) 95, (byte) 73, (byte) 78, (byte) 84, (byte) 69, (byte) 82, (byte) 77, (byte) 69, (byte) 68, (byte) 73, (byte) 65, (byte) 84, (byte) 69, (byte) 95, (byte) 75, (byte) 69, (byte) 89, (byte) 87, (byte) 82, (byte) 65, (byte) 80, (byte) 95, (byte) 77, (byte) 65, (byte) 67);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> KEYWRAP__ENC__INFO()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 65, (byte) 87, (byte) 83, (byte) 95, (byte) 77, (byte) 80, (byte) 76, (byte) 95, (byte) 73, (byte) 78, (byte) 84, (byte) 69, (byte) 82, (byte) 77, (byte) 69, (byte) 68, (byte) 73, (byte) 65, (byte) 84, (byte) 69, (byte) 95, (byte) 75, (byte) 69, (byte) 89, (byte) 87, (byte) 82, (byte) 65, (byte) 80, (byte) 95, (byte) 69, (byte) 78, (byte) 67);
    return _0_s;
  }
  @Override
  public java.lang.String toString() {
    return "IntermediateKeyWrapping._default";
  }
}
