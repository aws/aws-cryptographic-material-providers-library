// Class RsaGenerateAndWrapKeyMaterial
// Dafny class RsaGenerateAndWrapKeyMaterial compiled into Java
package RawRSAKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RsaGenerateAndWrapKeyMaterial implements MaterialWrapping_Compile.GenerateAndWrapMaterial<RsaWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.GenerateAndWrapInput, MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.GenerateAndWrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public RsaGenerateAndWrapKeyMaterial() {
    this._publicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._paddingScheme = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.Default();
    this._cryptoPrimitives = null;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> publicKey, software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._publicKey = publicKey;
    (this)._paddingScheme = paddingScheme;
    (this)._cryptoPrimitives = cryptoPrimitives;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.GenerateAndWrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.GenerateAndWrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<RsaWrapInfo>Default(RsaWrapInfo._typeDescriptor(), RsaWrapInfo.Default()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_generateBytesResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).cryptoPrimitives()).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create(AlgorithmSuites_Compile.__default.GetEncryptKeyLength((input).dtor_algorithmSuite())));
    _0_generateBytesResult = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _1_valueOrError0 = (_0_generateBytesResult).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_plaintextMaterial;
    _3_plaintextMaterial = (_1_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    RsaWrapKeyMaterial _4_wrap;
    RsaWrapKeyMaterial _nw0 = new RsaWrapKeyMaterial();
    _nw0.__ctor((this).publicKey(), (this).paddingScheme(), (this).cryptoPrimitives());
    _4_wrap = _nw0;
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>Default(RsaWrapInfo._typeDescriptor(), RsaWrapInfo.Default()));
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_4_wrap).Invoke(MaterialWrapping_Compile.WrapInput.create(_3_plaintextMaterial, (input).dtor_algorithmSuite(), (input).dtor_encryptionContext(), (input).dtor_serializedEC()));
    _5_valueOrError1 = _out1;
    if ((_5_valueOrError1).IsFailure(MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>>PropagateFailure(MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.WrapOutput<RsaWrapInfo> _6_wrapOutput;
    _6_wrapOutput = (_5_valueOrError1).Extract(MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo> _7_output;
    _7_output = MaterialWrapping_Compile.GenerateAndWrapOutput.<RsaWrapInfo>create(RsaWrapInfo._typeDescriptor(), _3_plaintextMaterial, (_6_wrapOutput).dtor_wrappedMaterial(), RsaWrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.GenerateAndWrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _7_output);
    return res;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> publicKey()
  {
    return this._publicKey;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode _paddingScheme;
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme()
  {
    return this._paddingScheme;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  private static final dafny.TypeDescriptor<RsaGenerateAndWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<RsaGenerateAndWrapKeyMaterial>referenceWithInitializer(RsaGenerateAndWrapKeyMaterial.class, () -> (RsaGenerateAndWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<RsaGenerateAndWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<RsaGenerateAndWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawRSAKeyring.RsaGenerateAndWrapKeyMaterial";
  }
}
