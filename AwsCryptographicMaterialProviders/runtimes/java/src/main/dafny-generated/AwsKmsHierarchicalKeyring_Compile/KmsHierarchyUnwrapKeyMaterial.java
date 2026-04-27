// Class KmsHierarchyUnwrapKeyMaterial
// Dafny class KmsHierarchyUnwrapKeyMaterial compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsHierarchyUnwrapKeyMaterial implements MaterialWrapping_Compile.UnwrapMaterial<HierarchyUnwrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.UnwrapInput, MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.UnwrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsHierarchyUnwrapKeyMaterial() {
    this._crypto = null;
    this._branchKeyIdUtf8 = UTF8.ValidUTF8Bytes.defaultValue();
    this._branchKeyVersionAsBytes = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._branchKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> branchKey, dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdUtf8, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersionAsBytes, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    (this)._branchKey = branchKey;
    (this)._branchKeyIdUtf8 = branchKeyIdUtf8;
    (this)._branchKeyVersionAsBytes = branchKeyVersionAsBytes;
    (this)._crypto = crypto;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.UnwrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>Default(HierarchyUnwrapInfo._typeDescriptor(), HierarchyUnwrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    dafny.DafnySequence<? extends java.lang.Byte> _1_wrappedMaterial;
    _1_wrappedMaterial = (input).dtor_wrappedMaterial();
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _2_aad;
    _2_aad = (input).dtor_encryptionContext();
    int _3_KeyLength;
    _3_KeyLength = AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_0_suite);
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _4_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((long) (_1_wrappedMaterial).cardinalityInt()) == ((long) (long) ((((long) (__default.EXPECTED__EDK__CIPHERTEXT__OVERHEAD()))) + (((long) (_3_KeyLength))))), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Received EDK Ciphertext of incorrect length2.")));
    if ((_4_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError0).<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _5_salt;
    _5_salt = (_1_wrappedMaterial).take(__default.H__WRAP__SALT__LEN());
    dafny.DafnySequence<? extends java.lang.Byte> _6_iv;
    _6_iv = (_1_wrappedMaterial).subsequence(__default.H__WRAP__SALT__LEN(), __default.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX());
    dafny.DafnySequence<? extends java.lang.Byte> _7_branchKeyVersionUuid;
    _7_branchKeyVersionUuid = (_1_wrappedMaterial).subsequence(__default.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX(), __default.EDK__CIPHERTEXT__VERSION__INDEX());
    dafny.DafnySequence<? extends java.lang.Byte> _8_wrappedKey;
    _8_wrappedKey = (_1_wrappedMaterial).subsequence(__default.EDK__CIPHERTEXT__VERSION__INDEX(), (int) ((__default.EDK__CIPHERTEXT__VERSION__INDEX()) + (_3_KeyLength)));
    dafny.DafnySequence<? extends java.lang.Byte> _9_authTag;
    _9_authTag = (_1_wrappedMaterial).drop((int) ((__default.EDK__CIPHERTEXT__VERSION__INDEX()) + (_3_KeyLength)));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _10_valueOrError1 = (input).dtor_serializedEC();
    if ((_10_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError1).<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _11_serializedEC;
    _11_serializedEC = (_10_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _12_wrappingAad;
    _12_wrappingAad = __default.WrappingAad((this).branchKeyIdUtf8(), (this).branchKeyVersionAsBytes(), _11_serializedEC);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = __default.DeriveEncryptionKeyFromBranchKey((this).branchKey(), _5_salt, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(UTF8.ValidUTF8Bytes._typeDescriptor(), Constants_Compile.__default.PROVIDER__ID__HIERARCHY()), (this).crypto());
    _13_valueOrError2 = _out0;
    if ((_13_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_13_valueOrError2).<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _14_derivedBranchKey;
    _14_derivedBranchKey = (_13_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _15_maybeUnwrappedPdk;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = ((this).crypto()).AESDecrypt(software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput.create(__default.AES__256__ENC__ALG(), _14_derivedBranchKey, _8_wrappedKey, _9_authTag, _6_iv, _12_wrappingAad));
    _15_maybeUnwrappedPdk = _out1;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _16_valueOrError3 = (_15_maybeUnwrappedPdk).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_17_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _17_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_17_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_17_e);
    }));
    if ((_16_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_16_valueOrError3).<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _18_unwrappedPdk;
    _18_unwrappedPdk = (_16_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo> _19_output;
    _19_output = MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>create(HierarchyUnwrapInfo._typeDescriptor(), _18_unwrappedPdk, HierarchyUnwrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.UnwrapOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _19_output);
    return res;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _crypto;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto()
  {
    return this._crypto;
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
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKey;
  public dafny.DafnySequence<? extends java.lang.Byte> branchKey()
  {
    return this._branchKey;
  }
  private static final dafny.TypeDescriptor<KmsHierarchyUnwrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsHierarchyUnwrapKeyMaterial>referenceWithInitializer(KmsHierarchyUnwrapKeyMaterial.class, () -> (KmsHierarchyUnwrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsHierarchyUnwrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsHierarchyUnwrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial";
  }
}
