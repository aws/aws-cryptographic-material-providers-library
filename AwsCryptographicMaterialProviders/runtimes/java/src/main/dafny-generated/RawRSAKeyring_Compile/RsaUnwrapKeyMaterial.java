// Class RsaUnwrapKeyMaterial
// Dafny class RsaUnwrapKeyMaterial compiled into Java
package RawRSAKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RsaUnwrapKeyMaterial implements MaterialWrapping_Compile.UnwrapMaterial<RsaUnwrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.UnwrapInput, MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.UnwrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public RsaUnwrapKeyMaterial() {
    this._cryptoPrimitives = null;
    this._privateKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._paddingScheme = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.Default();
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> privateKey, software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._privateKey = privateKey;
    (this)._paddingScheme = paddingScheme;
    (this)._cryptoPrimitives = cryptoPrimitives;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.UnwrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.UnwrapOutput.<RsaUnwrapInfo>_typeDescriptor(RsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<RsaUnwrapInfo>Default(RsaUnwrapInfo._typeDescriptor(), RsaUnwrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    dafny.DafnySequence<? extends java.lang.Byte> _1_wrappedMaterial;
    _1_wrappedMaterial = (input).dtor_wrappedMaterial();
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _2_aad;
    _2_aad = (input).dtor_encryptionContext();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _3_maybeDecryptResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).cryptoPrimitives()).RSADecrypt(software.amazon.cryptography.primitives.internaldafny.types.RSADecryptInput.create((this).paddingScheme(), (this).privateKey(), _1_wrappedMaterial));
    _3_maybeDecryptResult = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _4_valueOrError0 = (_3_maybeDecryptResult).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _5_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_5_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_5_e);
    }));
    if ((_4_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError0).<MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<RsaUnwrapInfo>_typeDescriptor(RsaUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _6_decryptResult;
    _6_decryptResult = (_4_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((long) (_6_decryptResult).cardinalityInt()) == (((long) (AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_0_suite)))), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid plaintext length.")));
    if ((_7_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError1).<MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<RsaUnwrapInfo>_typeDescriptor(RsaUnwrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo> _8_output;
    _8_output = MaterialWrapping_Compile.UnwrapOutput.<RsaUnwrapInfo>create(RsaUnwrapInfo._typeDescriptor(), _6_decryptResult, RsaUnwrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.UnwrapOutput.<RsaUnwrapInfo>_typeDescriptor(RsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _8_output);
    return res;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _privateKey;
  public dafny.DafnySequence<? extends java.lang.Byte> privateKey()
  {
    return this._privateKey;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode _paddingScheme;
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme()
  {
    return this._paddingScheme;
  }
  private static final dafny.TypeDescriptor<RsaUnwrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<RsaUnwrapKeyMaterial>referenceWithInitializer(RsaUnwrapKeyMaterial.class, () -> (RsaUnwrapKeyMaterial) null);
  public static dafny.TypeDescriptor<RsaUnwrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<RsaUnwrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawRSAKeyring.RsaUnwrapKeyMaterial";
  }
}
