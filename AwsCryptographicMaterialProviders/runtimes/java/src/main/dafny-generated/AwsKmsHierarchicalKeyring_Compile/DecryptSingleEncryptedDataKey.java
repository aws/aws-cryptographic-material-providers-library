// Class DecryptSingleEncryptedDataKey
// Dafny class DecryptSingleEncryptedDataKey compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;
import MrkAwareStrictMultiKeyring_Compile.*;
import LocalCMC_Compile.*;
import StormTracker_Compile.*;
import software.amazon.cryptography.internaldafny.StormTrackingCMC.*;
import CacheConstants_Compile.*;

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
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.__default.ValidUTF8Seq((edk).dtor_keyProviderInfo()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Received invalid EDK provider info for Hierarchical Keyring")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_suite;
    _1_suite = ((this).materials()).dtor_algorithmSuite();
    dafny.DafnySequence<? extends java.lang.Byte> _2_keyProviderId;
    _2_keyProviderId = (edk).dtor_keyProviderId();
    dafny.DafnySequence<? extends java.lang.Byte> _3_branchKeyIdUtf8;
    _3_branchKeyIdUtf8 = (edk).dtor_keyProviderInfo();
    dafny.DafnySequence<? extends java.lang.Byte> _4_ciphertext;
    _4_ciphertext = (edk).dtor_ciphertext();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _5_valueOrError1 = EdkWrapping_Compile.__default.GetProviderWrappedMaterial(_4_ciphertext, _1_suite);
    if ((_5_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _6_providerWrappedMaterial;
    _6_providerWrappedMaterial = (_5_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf((_6_providerWrappedMaterial).length())).compareTo(java.math.BigInteger.valueOf(__default.EDK__CIPHERTEXT__VERSION__INDEX())) >= 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Received EDK Ciphertext of incorrect length.")));
    if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _8_branchKeyVersionUuid;
    _8_branchKeyVersionUuid = (_6_providerWrappedMaterial).subsequence(__default.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX(), __default.EDK__CIPHERTEXT__VERSION__INDEX());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _9_valueOrError3 = (UUID.__default.FromByteArray(_8_branchKeyVersionUuid)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_9_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_9_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends Character> _10_version;
    _10_version = (_9_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (this).GetVersionCacheId(_3_branchKeyIdUtf8, _10_version, (this).cryptoPrimitives());
    _11_valueOrError4 = _out0;
    if ((_11_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_11_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _12_cacheId;
    _12_cacheId = (_11_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (this).GetHierarchicalMaterialsVersion((this).branchKeyId(), _3_branchKeyIdUtf8, _10_version, _12_cacheId);
    _13_valueOrError5 = _out1;
    if ((_13_valueOrError5).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_13_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _14_hierarchicalMaterials;
    _14_hierarchicalMaterials = (_13_valueOrError5).Extract(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _15_branchKey;
    _15_branchKey = (_14_hierarchicalMaterials).dtor_branchKey();
    dafny.DafnySequence<? extends java.lang.Byte> _16_branchKeyVersion;
    _16_branchKeyVersion = (_14_hierarchicalMaterials).dtor_branchKeyVersion();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _17_valueOrError6 = (UTF8.__default.Decode(_16_branchKeyVersion)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_17_valueOrError6).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_17_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends Character> _18_branchKeyVersionAsString;
    _18_branchKeyVersionAsString = (_17_valueOrError6).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError7 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _19_valueOrError7 = (UUID.__default.ToByteArray(_18_branchKeyVersionAsString)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_19_valueOrError7).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_19_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _20_branchKeyVersionAsBytes;
    _20_branchKeyVersionAsBytes = (_19_valueOrError7).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _21_maybeCrypto;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _21_maybeCrypto = _out2;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _22_valueOrError8 = (_21_maybeCrypto).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_23_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _23_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_23_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_23_e);
    }));
    if ((_22_valueOrError8).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_22_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient _24_cryptoPrimitivesX;
    _24_cryptoPrimitivesX = (_22_valueOrError8).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _25_cryptoPrimitives;
    _25_cryptoPrimitives = ((software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient)(java.lang.Object)(_24_cryptoPrimitivesX));
    KmsHierarchyUnwrapKeyMaterial _26_kmsHierarchyUnwrap;
    KmsHierarchyUnwrapKeyMaterial _nw0 = new KmsHierarchyUnwrapKeyMaterial();
    _nw0.__ctor(_15_branchKey, _3_branchKeyIdUtf8, _20_branchKeyVersionAsBytes, _25_cryptoPrimitives);
    _26_kmsHierarchyUnwrap = _nw0;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_unwrapOutputRes;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = EdkWrapping_Compile.__default.<HierarchyUnwrapInfo>UnwrapEdkMaterial(HierarchyUnwrapInfo._typeDescriptor(), (edk).dtor_ciphertext(), (this).materials(), _26_kmsHierarchyUnwrap);
    _27_unwrapOutputRes = _out3;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_valueOrError9 = Wrappers_Compile.Result.<EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>Default(HierarchyUnwrapInfo._typeDescriptor(), HierarchyUnwrapInfo.Default()));
    _28_valueOrError9 = _27_unwrapOutputRes;
    if ((_28_valueOrError9).IsFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_28_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    EdkWrapping_Compile.UnwrapEdkMaterialOutput<HierarchyUnwrapInfo> _29_unwrapOutput;
    _29_unwrapOutput = (_28_valueOrError9).Extract(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<HierarchyUnwrapInfo>_typeDescriptor(HierarchyUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _30_valueOrError10 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _30_valueOrError10 = Materials_Compile.__default.DecryptionMaterialsAddDataKey((this).materials(), (_29_unwrapOutput).dtor_plaintextDataKey(), (_29_unwrapOutput).dtor_symmetricSigningKey());
    if ((_30_valueOrError10).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_30_valueOrError10).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _31_result;
    _31_result = (_30_valueOrError10).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _31_result);
    return res;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetVersionCacheId(dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdUtf8, dafny.DafnySequence<? extends Character> branchKeyVersion, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> cacheId = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((UTF8.__default.Decode(branchKeyIdUtf8)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError)).is_Success()) && (((boolean)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, Boolean>Let(((UTF8.__default.Decode(branchKeyIdUtf8)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError)).dtor_value(), boxed14 -> {
      dafny.DafnySequence<? extends Character> _pat_let7_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed14));
      return ((boolean)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, Boolean>Let(_pat_let7_0, boxed15 -> {
        dafny.DafnySequence<? extends Character> _1_branchKeyId = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed15));
        return (true) && (((java.math.BigInteger.valueOf((_1_branchKeyId).length())).signum() != -1) && ((java.math.BigInteger.valueOf((_1_branchKeyId).length())).compareTo(StandardLibrary_mUInt_Compile.__default.UINT32__LIMIT()) < 0));
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
    dafny.DafnySequence<? extends java.lang.Byte> _6_versionBytes;
    _6_versionBytes = UTF8.__default.EncodeAscii(branchKeyVersion);
    dafny.DafnySequence<? extends java.lang.Byte> _7_suffix;
    _7_suffix = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate((this).logicalKeyStoreNameBytes(), CacheConstants_Compile.__default.NULL__BYTE()), branchKeyIdUtf8), CacheConstants_Compile.__default.NULL__BYTE()), _6_versionBytes);
    dafny.DafnySequence<? extends java.lang.Byte> _8_identifier;
    _8_identifier = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_3_resourceId, CacheConstants_Compile.__default.NULL__BYTE()), _4_scopeId), CacheConstants_Compile.__default.NULL__BYTE()), (this).partitionIdBytes()), CacheConstants_Compile.__default.NULL__BYTE()), _7_suffix);
    software.amazon.cryptography.primitives.internaldafny.types.DigestInput _9_identifierDigestInput;
    _9_identifierDigestInput = software.amazon.cryptography.primitives.internaldafny.types.DigestInput.create(_2_hashAlgorithm, _8_identifier);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _10_maybeCacheDigest;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = Digest_Compile.__default.Digest(_9_identifierDigestInput);
    _10_maybeCacheDigest = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _11_valueOrError2 = (_10_maybeCacheDigest).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_12_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _12_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_12_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_12_e);
    }));
    if ((_11_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_11_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _13_cacheDigest;
    _13_cacheDigest = (_11_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _14_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.util.Objects.equals(java.math.BigInteger.valueOf((_13_cacheDigest).length()), Digest_Compile.__default.Length(_2_hashAlgorithm)), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Digest generated a message not equal to the expected length.")));
    if ((_14_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_14_valueOrError3).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    cacheId = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _13_cacheDigest);
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
        _12_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((((_1_getCacheOutput).dtor_value()).dtor_materials()).is_BranchKey()) && (java.util.Objects.equals(((_1_getCacheOutput).dtor_value()).dtor_materials(), software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_BranchKey((((_1_getCacheOutput).dtor_value()).dtor_materials()).dtor_BranchKey()))), __default.E(dafny.DafnySequence.asString("Invalid Material Type.")));
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
