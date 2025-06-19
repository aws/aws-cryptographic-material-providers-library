// Class KmsHierarchyWrapKeyMaterial
// Dafny class KmsHierarchyWrapKeyMaterial compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsHierarchyWrapKeyMaterial implements MaterialWrapping_Compile.WrapMaterial<HierarchyWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.WrapInput, MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.WrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsHierarchyWrapKeyMaterial() {
    this._branchKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._branchKeyIdUtf8 = UTF8.ValidUTF8Bytes.defaultValue();
    this._branchKeyVersionAsBytes = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._crypto = null;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> branchKey, dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdUtf8, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersionAsBytes, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    (this)._branchKey = branchKey;
    (this)._branchKeyIdUtf8 = branchKeyIdUtf8;
    (this)._branchKeyVersionAsBytes = branchKeyVersionAsBytes;
    (this)._crypto = crypto;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.WrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>Default(HierarchyWrapInfo._typeDescriptor(), HierarchyWrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _1_maybeNonceSalt;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).crypto()).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create((int) ((__default.H__WRAP__SALT__LEN()) + (__default.H__WRAP__NONCE__LEN()))));
    _1_maybeNonceSalt = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _2_valueOrError0 = (_1_maybeNonceSalt).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_3_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _3_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_3_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_3_e);
    }));
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _4_saltAndNonce;
    _4_saltAndNonce = (_2_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _5_salt;
    _5_salt = (_4_saltAndNonce).take(__default.H__WRAP__SALT__LEN());
    dafny.DafnySequence<? extends java.lang.Byte> _6_nonce;
    _6_nonce = (_4_saltAndNonce).drop(__default.H__WRAP__SALT__LEN());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _7_valueOrError1 = (input).dtor_serializedEC();
    if ((_7_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError1).<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _8_serializedEC;
    _8_serializedEC = (_7_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _9_wrappingAad;
    _9_wrappingAad = __default.WrappingAad((this).branchKeyIdUtf8(), (this).branchKeyVersionAsBytes(), _8_serializedEC);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = __default.DeriveEncryptionKeyFromBranchKey((this).branchKey(), _5_salt, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(UTF8.ValidUTF8Bytes._typeDescriptor(), Constants_Compile.__default.PROVIDER__ID__HIERARCHY()), (this).crypto());
    _10_valueOrError2 = _out1;
    if ((_10_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError2).<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _11_derivedBranchKey;
    _11_derivedBranchKey = (_10_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _12_maybeWrappedPdk;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = ((this).crypto()).AESEncrypt(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput.create(__default.AES__256__ENC__ALG(), _6_nonce, _11_derivedBranchKey, (input).dtor_plaintextMaterial(), _9_wrappingAad));
    _12_maybeWrappedPdk = _out2;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.Default());
    _13_valueOrError3 = (_12_maybeWrappedPdk).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_14_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _14_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_14_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_14_e);
    }));
    if ((_13_valueOrError3).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_13_valueOrError3).<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput _15_wrappedPdk;
    _15_wrappedPdk = (_13_valueOrError3).Extract(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo> _16_output;
    _16_output = MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>create(HierarchyWrapInfo._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_5_salt, _6_nonce), (this).branchKeyVersionAsBytes()), (_15_wrappedPdk).dtor_cipherText()), (_15_wrappedPdk).dtor_authTag()), HierarchyWrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _16_output);
    return res;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKey;
  public dafny.DafnySequence<? extends java.lang.Byte> branchKey()
  {
    return this._branchKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKeyIdUtf8;
  public dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdUtf8()
  {
    return this._branchKeyIdUtf8;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKeyVersionAsBytes;
  public dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersionAsBytes()
  {
    return this._branchKeyVersionAsBytes;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _crypto;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto()
  {
    return this._crypto;
  }
  private static final dafny.TypeDescriptor<KmsHierarchyWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsHierarchyWrapKeyMaterial>referenceWithInitializer(KmsHierarchyWrapKeyMaterial.class, () -> (KmsHierarchyWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsHierarchyWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsHierarchyWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial";
  }
}
