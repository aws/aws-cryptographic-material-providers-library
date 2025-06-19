// Class AesGenerateAndWrapKeyMaterial
// Dafny class AesGenerateAndWrapKeyMaterial compiled into Java
package RawAESKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AesGenerateAndWrapKeyMaterial implements MaterialWrapping_Compile.GenerateAndWrapMaterial<AesWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.GenerateAndWrapInput, MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.GenerateAndWrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public AesGenerateAndWrapKeyMaterial() {
    this._wrap = null;
  }
  public void __ctor(AesWrapKeyMaterial wrap)
  {
    (this)._wrap = wrap;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.GenerateAndWrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.GenerateAndWrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<AesWrapInfo>Default(AesWrapInfo._typeDescriptor(), AesWrapInfo.Default()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_generateBytesResult;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = (((this).wrap()).cryptoPrimitives()).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create(AlgorithmSuites_Compile.__default.GetEncryptKeyLength((input).dtor_algorithmSuite())));
      _0_generateBytesResult = _out0;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _1_valueOrError0 = (_0_generateBytesResult).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
        software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
      }));
      if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_1_valueOrError0).<MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()));
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _3_plaintextMaterial;
      _3_plaintextMaterial = (_1_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<AesWrapInfo>Default(AesWrapInfo._typeDescriptor(), AesWrapInfo.Default()));
      Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = ((this).wrap()).Invoke(MaterialWrapping_Compile.WrapInput.create(_3_plaintextMaterial, (input).dtor_algorithmSuite(), (input).dtor_encryptionContext(), (input).dtor_serializedEC()));
      _4_valueOrError1 = _out1;
      if ((_4_valueOrError1).IsFailure(MaterialWrapping_Compile.WrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_4_valueOrError1).<MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>>PropagateFailure(MaterialWrapping_Compile.WrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()));
        return res;
      }
      MaterialWrapping_Compile.WrapOutput<AesWrapInfo> _5_wrapOutput;
      _5_wrapOutput = (_4_valueOrError1).Extract(MaterialWrapping_Compile.WrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.GenerateAndWrapOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<AesWrapInfo>create(AesWrapInfo._typeDescriptor(), _3_plaintextMaterial, (_5_wrapOutput).dtor_wrappedMaterial(), (_5_wrapOutput).dtor_wrapInfo()));
    }
    return res;
  }
  public AesWrapKeyMaterial _wrap;
  public AesWrapKeyMaterial wrap()
  {
    return this._wrap;
  }
  private static final dafny.TypeDescriptor<AesGenerateAndWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<AesGenerateAndWrapKeyMaterial>referenceWithInitializer(AesGenerateAndWrapKeyMaterial.class, () -> (AesGenerateAndWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<AesGenerateAndWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesGenerateAndWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawAESKeyring.AesGenerateAndWrapKeyMaterial";
  }
}
