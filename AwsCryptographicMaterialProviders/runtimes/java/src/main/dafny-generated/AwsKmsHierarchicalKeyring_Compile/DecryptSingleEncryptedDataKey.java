// Class DecryptSingleEncryptedDataKey
// Dafny class DecryptSingleEncryptedDataKey compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptSingleEncryptedDataKey implements Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public DecryptSingleEncryptedDataKey() {
    this._materials = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials)null;
    this._keyStore = null;
    this._cryptoPrimitives = null;
    this._branchKeyId = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    this._ttlSeconds = 0L;
    this._cache = null;
    this._partitionIdBytes = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._logicalKeyStoreNameBytes = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials, software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives, dafny.DafnySequence<? extends Character> branchKeyId, long ttlSeconds, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache cache, dafny.DafnySequence<? extends java.lang.Byte> partitionIdBytes, dafny.DafnySequence<? extends java.lang.Byte> logicalKeyStoreNameBytes)
  {
    (this)._materials = materials;
    (this)._keyStore = keyStore;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._branchKeyId = branchKeyId;
    (this)._ttlSeconds = ttlSeconds;
    (this)._cache = cache;
    (this)._partitionIdBytes = partitionIdBytes;
    (this)._logicalKeyStoreNameBytes = logicalKeyStoreNameBytes;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = ((this).materials()).dtor_algorithmSuite();
    dafny.DafnySequence<? extends java.lang.Byte> _1_keyProviderId;
    _1_keyProviderId = (edk).dtor_keyProviderId();
    dafny.DafnySequence<? extends java.lang.Byte> _2_branchKeyIdUtf8;
    _2_branchKeyIdUtf8 = (edk).dtor_keyProviderInfo();
    dafny.DafnySequence<? extends java.lang.Byte> _3_ciphertext;
    _3_ciphertext = (edk).dtor_ciphertext();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _4_valueOrError0 = EdkWrapping_Compile.__default.GetProviderWrappedMaterial(_3_ciphertext, _0_suite);
    if ((_4_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _5_providerWrappedMaterial;
    _5_providerWrappedMaterial = (_4_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) (_5_providerWrappedMaterial).cardinalityInt(), ((long) (__default.EDK__CIPHERTEXT__VERSION__INDEX()))) >= 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Received EDK Ciphertext of incorrect length.")));
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _7_branchKeyVersionUuid;
    _7_branchKeyVersionUuid = (_5_providerWrappedMaterial).subsequence(__default.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX(), __default.EDK__CIPHERTEXT__VERSION__INDEX());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _8_valueOrError2 = (UUID.__default.FromByteArray(_7_branchKeyVersionUuid)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_8_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends Character> _9_version;
    _9_version = (_8_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (this).GetVersionCacheId(_2_branchKeyIdUtf8, _9_version, (this).cryptoPrimitives());
    _10_valueOrError3 = _out0;
    if ((_10_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _11_cacheId;
    _11_cacheId = (_10_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (this).GetHierarchicalMaterialsVersion((this).branchKeyId(), _2_branchKeyIdUtf8, _9_version, _11_cacheId);
    _12_valueOrError4 = _out1;
    if ((_12_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_12_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _13_hierarchicalMaterials;
    _13_hierarchicalMaterials = (_12_valueOrError4).Extract(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _14_branchKey;
    _14_branchKey = (_13_hierarchicalMaterials).dtor_branchKey();
    dafny.DafnySequence<? extends java.lang.Byte> _15_branchKeyVersion;
    _15_branchKeyVersion = (_13_hierarchicalMaterials).dtor_branchKeyVersion();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _16_valueOrError5 = (UTF8.__default.Decode(_15_branchKeyVersion)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_16_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_16_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends Character> _17_branchKeyVersionAsString;
    _17_branchKeyVersionAsString = (_16_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _18_valueOrError6 = (UUID.__default.ToByteArray(_17_branchKeyVersionAsString)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_18_valueOrError6).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_18_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _19_branchKeyVersionAsBytes;
    _19_branchKeyVersionAsBytes = (_18_valueOrError6).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _20_maybeCrypto;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _20_maybeCrypto = _out2;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _21_valueOrError7 = (_20_maybeCrypto).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_22_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _22_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_22_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_22_e);
    }));
    if ((_21_valueOrError7).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_21_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient _23_cryptoPrimitivesX;
    _23_cryptoPrimitivesX = (_21_valueOrError7).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _24_cryptoPrimitives;
    _24_cryptoPrimitives = ((software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient)(java.lang.Object)(_23_cryptoPrimitivesX));
    KmsHierarchyUnwrapKeyMaterial _25_kmsHierarchyUnwrap;
    KmsHierarchyUnwrapKeyMaterial _nw0 = new KmsHierarchyUnwrapKeyMaterial();
    _nw0.__ctor(_14_branchKey, _2_branchKeyIdUtf8, _19_branchKeyVersionAsBytes, _24_cryptoPrimitives);
    _25_kmsHierarchyUnwrap = _nw0;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_unwrapOutputRes;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = EdkWrapping_Compile.__default.<HierarchyUnwrapInfo>UnwrapEdkMaterial(HierarchyUnwrapInfo._typeDescriptor(), (edk).dtor_ciphertext(), (this).materials(), _25_kmsHierarchyUnwrap);
    _26_unwrapOutputRes = _out3;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_valueOrError8 = Wrappers_Compile.Result.<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>Default(HierarchyUnwrapInfo._typeDescriptor(), HierarchyUnwrapInfo.Default()));
    _27_valueOrError8 = _26_unwrapOutputRes;
    if ((_27_valueOrError8).IsFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_27_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo> _28_unwrapOutput;
    _28_unwrapOutput = (_27_valueOrError8).Extract(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _29_valueOrError9 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _29_valueOrError9 = Materials_Compile.__default.DecryptionMaterialsAddDataKey((this).materials(), (_28_unwrapOutput).dtor_plaintextDataKey(), (_28_unwrapOutput).dtor_symmetricSigningKey());
    if ((_29_valueOrError9).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_29_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _30_result;
    _30_result = (_29_valueOrError9).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _30_result);
    return res;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetVersionCacheId(dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdUtf8, dafny.DafnySequence<? extends Character> branchKeyVersion, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> cacheId = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (true) && (((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Boolean>Let(UTF8.__default.Decode(branchKeyIdUtf8), boxed14 -> {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _pat_let7_0 = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed14));
      return ((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Boolean>Let(_pat_let7_0, boxed15 -> {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _1_branchKeyId = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed15));
        return ((_1_branchKeyId).is_Success()) && (((((long) ((_1_branchKeyId).dtor_value()).cardinalityInt()) == 0 ? 0 : 1) != -1) && (java.lang.Long.compareUnsigned((long) ((_1_branchKeyId).dtor_value()).cardinalityInt(), (StandardLibrary_mUInt_Compile.__default.UINT32__LIMIT()).longValue()) < 0));
      }
      )));
    }
    )))), __default.E(dafny.DafnySequence.asString("Invalid Branch Key ID Length")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _2_hashAlgorithm;
    _2_hashAlgorithm = software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384();
    dafny.DafnySequence<? extends java.lang.Byte> _3_resourceId;
    _3_resourceId = CacheConstants_Compile.__default.RESOURCE__ID__HIERARCHICAL__KEYRING();
    dafny.DafnySequence<? extends java.lang.Byte> _4_scopeId;
    _4_scopeId = CacheConstants_Compile.__default.SCOPE__ID__DECRYPT();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _5_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.__default.IsASCIIString(branchKeyVersion), __default.E(dafny.DafnySequence.asString("Unable to represent as an ASCII string.")));
    if ((_5_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_5_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
    _6_valueOrError2 = (UTF8.__default.Encode(branchKeyVersion)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_7_e_boxed0) -> {
      dafny.DafnySequence<? extends Character> _7_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_7_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_7_e);
    }));
    if ((_6_valueOrError2).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_6_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _8_versionBytes;
    _8_versionBytes = (_6_valueOrError2).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _9_suffix;
    _9_suffix = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate((this).logicalKeyStoreNameBytes(), CacheConstants_Compile.__default.NULL__BYTE()), branchKeyIdUtf8), CacheConstants_Compile.__default.NULL__BYTE()), _8_versionBytes);
    dafny.DafnySequence<? extends java.lang.Byte> _10_identifier;
    _10_identifier = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_3_resourceId, CacheConstants_Compile.__default.NULL__BYTE()), _4_scopeId), CacheConstants_Compile.__default.NULL__BYTE()), (this).partitionIdBytes()), CacheConstants_Compile.__default.NULL__BYTE()), _9_suffix);
    software.amazon.cryptography.primitives.internaldafny.types.DigestInput _11_identifierDigestInput;
    _11_identifierDigestInput = software.amazon.cryptography.primitives.internaldafny.types.DigestInput.create(_2_hashAlgorithm, _10_identifier);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _12_maybeCacheDigest;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = Digest_Compile.__default.Digest(_11_identifierDigestInput);
    _12_maybeCacheDigest = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _13_valueOrError3 = (_12_maybeCacheDigest).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_14_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _14_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_14_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_14_e);
    }));
    if ((_13_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_13_valueOrError3).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _15_cacheDigest;
    _15_cacheDigest = (_13_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    cacheId = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _15_cacheDigest);
    return cacheId;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetHierarchicalMaterialsVersion(dafny.DafnySequence<? extends Character> branchKeyId, dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdUtf8, dafny.DafnySequence<? extends Character> version, dafny.DafnySequence<? extends java.lang.Byte> cacheId)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> material = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.Default());
    if(true) {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput _0_getCacheInput;
      _0_getCacheInput = software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput.create(cacheId, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_getCacheOutput;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = ((this).cache()).GetCacheEntry(_0_getCacheInput);
      _1_getCacheOutput = _out0;
      if (((_1_getCacheOutput).is_Failure()) && (!(((_1_getCacheOutput).dtor_error()).is_EntryDoesNotExist()))) {
        material = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_1_getCacheOutput).dtor_error());
        return material;
      }
      long _2_now;
      long _out1;
      _out1 = Time.__default.CurrentRelativeTime();
      _2_now = _out1;
      if (((_1_getCacheOutput).is_Failure()) || (!(__default.cacheEntryWithinLimits(((_1_getCacheOutput).dtor_value()).dtor_creationTime(), _2_now, (this).ttlSeconds())))) {
        Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_maybeGetBranchKeyVersionOutput;
        Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
        _out2 = ((this).keyStore()).GetBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create(branchKeyId, version));
        _3_maybeGetBranchKeyVersionOutput = _out2;
        Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
        _4_valueOrError0 = (_3_maybeGetBranchKeyVersionOutput).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.keystore.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
          software.amazon.cryptography.keystore.internaldafny.types.Error _5_e = ((software.amazon.cryptography.keystore.internaldafny.types.Error)(java.lang.Object)(_5_e_boxed0));
          return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyKeyStore(_5_e);
        }));
        if ((_4_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          material = (_4_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor());
          return material;
        }
        software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput _6_getBranchKeyVersionOutput;
        _6_getBranchKeyVersionOutput = (_4_valueOrError0).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _7_branchKeyMaterials;
        _7_branchKeyMaterials = (_6_getBranchKeyVersionOutput).dtor_branchKeyMaterials();
        long _8_now;
        long _out3;
        _out3 = Time.__default.CurrentRelativeTime();
        _8_now = _out3;
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _9_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.math.BigInteger.valueOf(_8_now)).add(java.math.BigInteger.valueOf((this).ttlSeconds()))).compareTo(StandardLibrary_mUInt_Compile.__default.INT64__MAX__LIMIT()) < 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("INT64 Overflow when putting cache entry.")));
        if ((_9_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          material = (_9_valueOrError1).<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor());
          return material;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput _10_putCacheEntryInput;
        _10_putCacheEntryInput = software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput.create(cacheId, software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_BranchKey(_7_branchKeyMaterials), _8_now, (long) (long) (((this).ttlSeconds()) + (_8_now)), Wrappers_Compile.Option.<java.lang.Integer>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor()));
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_putResult;
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
        _out4 = ((this).cache()).PutCacheEntry(_10_putCacheEntryInput);
        _11_putResult = _out4;
        if (((_11_putResult).is_Failure()) && (!(((_11_putResult).dtor_error()).is_EntryAlreadyExists()))) {
          material = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_11_putResult).dtor_error());
          return material;
        }
        material = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _7_branchKeyMaterials);
        return material;
      } else {
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _12_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_1_getCacheOutput).dtor_value()).dtor_materials()).is_BranchKey(), __default.E(dafny.DafnySequence.asString("Invalid Material Type.")));
        if ((_12_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          material = (_12_valueOrError2).<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor());
          return material;
        }
        material = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_1_getCacheOutput).dtor_value()).dtor_materials()).dtor_BranchKey());
        return material;
      }
    }
    return material;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _materials;
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials()
  {
    return this._materials;
  }
  public software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient _keyStore;
  public software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore()
  {
    return this._keyStore;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public dafny.DafnySequence<? extends Character> _branchKeyId;
  public dafny.DafnySequence<? extends Character> branchKeyId()
  {
    return this._branchKeyId;
  }
  public long _ttlSeconds;
  public long ttlSeconds()
  {
    return this._ttlSeconds;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _cache;
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache cache()
  {
    return this._cache;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _partitionIdBytes;
  public dafny.DafnySequence<? extends java.lang.Byte> partitionIdBytes()
  {
    return this._partitionIdBytes;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _logicalKeyStoreNameBytes;
  public dafny.DafnySequence<? extends java.lang.Byte> logicalKeyStoreNameBytes()
  {
    return this._logicalKeyStoreNameBytes;
  }
  private static final dafny.TypeDescriptor<DecryptSingleEncryptedDataKey> _TYPE = dafny.TypeDescriptor.<DecryptSingleEncryptedDataKey>referenceWithInitializer(DecryptSingleEncryptedDataKey.class, () -> (DecryptSingleEncryptedDataKey) null);
  public static dafny.TypeDescriptor<DecryptSingleEncryptedDataKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptSingleEncryptedDataKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsHierarchicalKeyring.DecryptSingleEncryptedDataKey";
  }
}
