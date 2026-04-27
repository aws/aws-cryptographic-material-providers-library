// Class RsaWrapKeyMaterial
// Dafny class RsaWrapKeyMaterial compiled into Java
package RawRSAKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RsaWrapKeyMaterial implements MaterialWrapping_Compile.WrapMaterial<RsaWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.WrapInput, MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.WrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public RsaWrapKeyMaterial() {
    this._cryptoPrimitives = null;
    this._publicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._paddingScheme = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.Default();
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> publicKey, software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._publicKey = publicKey;
    (this)._paddingScheme = paddingScheme;
    (this)._cryptoPrimitives = cryptoPrimitives;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.WrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>Default(RsaWrapInfo._typeDescriptor(), RsaWrapInfo.Default()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_RSAEncryptOutput;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).cryptoPrimitives()).RSAEncrypt(software.amazon.cryptography.primitives.internaldafny.types.RSAEncryptInput.create((this).paddingScheme(), (this).publicKey(), (input).dtor_plaintextMaterial()));
    _0_RSAEncryptOutput = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _1_valueOrError0 = (_0_RSAEncryptOutput).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_ciphertext;
    _3_ciphertext = (_1_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.WrapOutput<RsaWrapInfo> _4_output;
    _4_output = MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>create(RsaWrapInfo._typeDescriptor(), _3_ciphertext, RsaWrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.WrapOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_output);
    return res;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
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
  private static final dafny.TypeDescriptor<RsaWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<RsaWrapKeyMaterial>referenceWithInitializer(RsaWrapKeyMaterial.class, () -> (RsaWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<RsaWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<RsaWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawRSAKeyring.RsaWrapKeyMaterial";
  }
}
