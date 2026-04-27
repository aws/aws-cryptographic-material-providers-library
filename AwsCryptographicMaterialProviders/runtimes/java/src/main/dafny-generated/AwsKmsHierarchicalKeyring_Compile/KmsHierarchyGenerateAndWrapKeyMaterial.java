// Class KmsHierarchyGenerateAndWrapKeyMaterial
// Dafny class KmsHierarchyGenerateAndWrapKeyMaterial compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsHierarchyGenerateAndWrapKeyMaterial implements MaterialWrapping_Compile.GenerateAndWrapMaterial<HierarchyWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.GenerateAndWrapInput, MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.GenerateAndWrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsHierarchyGenerateAndWrapKeyMaterial() {
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
  public Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.GenerateAndWrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.GenerateAndWrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<HierarchyWrapInfo>Default(HierarchyWrapInfo._typeDescriptor(), HierarchyWrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _1_pdkResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ((this).crypto()).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.create(AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_0_suite)));
    _1_pdkResult = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _2_valueOrError0 = (_1_pdkResult).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_3_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _3_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_3_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_3_e);
    }));
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _4_pdk;
    _4_pdk = (_2_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    KmsHierarchyWrapKeyMaterial _5_wrap;
    KmsHierarchyWrapKeyMaterial _nw0 = new KmsHierarchyWrapKeyMaterial();
    _nw0.__ctor((this).branchKey(), (this).branchKeyIdUtf8(), (this).branchKeyVersionAsBytes(), (this).crypto());
    _5_wrap = _nw0;
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>Default(HierarchyWrapInfo._typeDescriptor(), HierarchyWrapInfo.Default()));
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_5_wrap).Invoke(MaterialWrapping_Compile.WrapInput.create(_4_pdk, (input).dtor_algorithmSuite(), (input).dtor_encryptionContext(), (input).dtor_serializedEC()));
    _6_valueOrError1 = _out1;
    if ((_6_valueOrError1).IsFailure(MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError1).<MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>>PropagateFailure(MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.WrapOutput<HierarchyWrapInfo> _7_wrapOutput;
    _7_wrapOutput = (_6_valueOrError1).Extract(MaterialWrapping_Compile.WrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo> _8_output;
    _8_output = MaterialWrapping_Compile.GenerateAndWrapOutput.<HierarchyWrapInfo>create(HierarchyWrapInfo._typeDescriptor(), _4_pdk, (_7_wrapOutput).dtor_wrappedMaterial(), HierarchyWrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.GenerateAndWrapOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _8_output);
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
  private static final dafny.TypeDescriptor<KmsHierarchyGenerateAndWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsHierarchyGenerateAndWrapKeyMaterial>referenceWithInitializer(KmsHierarchyGenerateAndWrapKeyMaterial.class, () -> (KmsHierarchyGenerateAndWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsHierarchyGenerateAndWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsHierarchyGenerateAndWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial";
  }
}
