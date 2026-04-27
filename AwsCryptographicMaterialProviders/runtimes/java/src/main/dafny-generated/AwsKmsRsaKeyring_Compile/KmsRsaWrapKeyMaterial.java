// Class KmsRsaWrapKeyMaterial
// Dafny class KmsRsaWrapKeyMaterial compiled into Java
package AwsKmsRsaKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsRsaWrapKeyMaterial implements MaterialWrapping_Compile.WrapMaterial<KmsRsaWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.WrapInput, MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.WrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsRsaWrapKeyMaterial() {
    this._publicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._cryptoPrimitives = null;
    this._paddingScheme = software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.Default();
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> publicKey, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._publicKey = publicKey;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._paddingScheme = paddingScheme;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.WrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>Default(KmsRsaWrapInfo._typeDescriptor(), KmsRsaWrapInfo.Default()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = __default.EncryptionContextDigest((this).cryptoPrimitives(), (input).dtor_encryptionContext());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_encryptionContextDigest;
    _1_encryptionContextDigest = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode _2_padding;
    software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _source0 = (this).paddingScheme();
    if (_source0.is_RSAES__OAEP__SHA__1()) {
      _2_padding = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_OAEP__SHA1();
    } else {
      _2_padding = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_OAEP__SHA256();
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _3_RSAEncryptOutput;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = ((this).cryptoPrimitives()).RSAEncrypt(software.amazon.cryptography.primitives.internaldafny.types.RSAEncryptInput.create(_2_padding, (this).publicKey(), dafny.DafnySequence.<java.lang.Byte>concatenate(_1_encryptionContextDigest, (input).dtor_plaintextMaterial())));
    _3_RSAEncryptOutput = _out1;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _4_valueOrError1 = (_3_RSAEncryptOutput).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _5_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_5_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_5_e);
    }));
    if ((_4_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError1).<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _6_ciphertext;
    _6_ciphertext = (_4_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo> _7_output;
    _7_output = MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>create(KmsRsaWrapInfo._typeDescriptor(), _6_ciphertext, KmsRsaWrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.WrapOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _7_output);
    return res;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> publicKey()
  {
    return this._publicKey;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _paddingScheme;
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme()
  {
    return this._paddingScheme;
  }
  private static final dafny.TypeDescriptor<KmsRsaWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsRsaWrapKeyMaterial>referenceWithInitializer(KmsRsaWrapKeyMaterial.class, () -> (KmsRsaWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsRsaWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsRsaWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial";
  }
}
