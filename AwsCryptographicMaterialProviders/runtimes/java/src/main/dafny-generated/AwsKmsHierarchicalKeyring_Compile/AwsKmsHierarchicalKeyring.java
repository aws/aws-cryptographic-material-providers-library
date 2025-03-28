// Class AwsKmsHierarchicalKeyring
// Dafny class AwsKmsHierarchicalKeyring compiled into Java
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
public class AwsKmsHierarchicalKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public AwsKmsHierarchicalKeyring() {
    this._keyStore = null;
    this._cryptoPrimitives = null;
    this._cache = null;
    this._branchKeyIdSupplier = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>Default(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class)));
    this._branchKeyId = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    this._ttlSeconds = 0L;
    this._partitionIdBytes = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._logicalKeyStoreNameBytes = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out6;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out6;
  }
  public void __ctor(software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyId, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier> branchKeyIdSupplier, long ttlSeconds, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache cmc, dafny.DafnySequence<? extends java.lang.Byte> partitionIdBytes, dafny.DafnySequence<? extends java.lang.Byte> logicalKeyStoreNameBytes, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._keyStore = keyStore;
    (this)._branchKeyId = branchKeyId;
    (this)._branchKeyIdSupplier = branchKeyIdSupplier;
    (this)._ttlSeconds = ttlSeconds;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._cache = cmc;
    (this)._partitionIdBytes = partitionIdBytes;
    (this)._logicalKeyStoreNameBytes = logicalKeyStoreNameBytes;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetBranchKeyId(dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> context)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ret = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    if(true) {
      if (((this).branchKeyId()).is_Some()) {
        ret = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).branchKeyId()).dtor_value());
        return ret;
      } else {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput.Default());
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = (((this).branchKeyIdSupplier()).dtor_value()).GetBranchKeyId(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdInput.create(context));
        _0_valueOrError0 = _out0;
        if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_0_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          return ret;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput _1_GetBranchKeyIdOut;
        _1_GetBranchKeyIdOut = (_0_valueOrError0).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        ret = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_1_GetBranchKeyIdOut).dtor_branchKeyId());
        return ret;
      }
    }
    return ret;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _0_materials;
      _0_materials = (input).dtor_materials();
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_suite;
      _1_suite = (_0_materials).dtor_algorithmSuite();
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (this).GetBranchKeyId((_0_materials).dtor_encryptionContext());
      _2_valueOrError0 = _out0;
      if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_2_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _3_branchKeyIdForEncrypt;
      _3_branchKeyIdForEncrypt = (_2_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
      _4_valueOrError1 = (UTF8.__default.Encode(_3_branchKeyIdForEncrypt)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
      if ((_4_valueOrError1).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_4_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _5_branchKeyIdUtf8;
      _5_branchKeyIdUtf8 = (_4_valueOrError1).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = (this).GetActiveCacheId(_3_branchKeyIdForEncrypt, _5_branchKeyIdUtf8, (this).cryptoPrimitives());
      _6_valueOrError2 = _out1;
      if ((_6_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_6_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _7_cacheId;
      _7_cacheId = (_6_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
      _out2 = (this).GetActiveHierarchicalMaterials(_3_branchKeyIdForEncrypt, _7_cacheId, (this).keyStore());
      _8_valueOrError3 = _out2;
      if ((_8_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_8_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _9_hierarchicalMaterials;
      _9_hierarchicalMaterials = (_8_valueOrError3).Extract(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnySequence<? extends java.lang.Byte> _10_branchKey;
      _10_branchKey = (_9_hierarchicalMaterials).dtor_branchKey();
      dafny.DafnySequence<? extends java.lang.Byte> _11_branchKeyVersion;
      _11_branchKeyVersion = (_9_hierarchicalMaterials).dtor_branchKeyVersion();
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _12_valueOrError4 = (UTF8.__default.Decode(_11_branchKeyVersion)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
      if ((_12_valueOrError4).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_12_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _13_branchKeyVersionAsString;
      _13_branchKeyVersionAsString = (_12_valueOrError4).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _14_valueOrError5 = (UUID.__default.ToByteArray(_13_branchKeyVersionAsString)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
      if ((_14_valueOrError5).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_14_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _15_branchKeyVersionAsBytes;
      _15_branchKeyVersionAsBytes = (_14_valueOrError5).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      KmsHierarchyGenerateAndWrapKeyMaterial _16_kmsHierarchyGenerateAndWrap;
      KmsHierarchyGenerateAndWrapKeyMaterial _nw0 = new KmsHierarchyGenerateAndWrapKeyMaterial();
      _nw0.__ctor((_9_hierarchicalMaterials).dtor_branchKey(), _5_branchKeyIdUtf8, _15_branchKeyVersionAsBytes, (this).cryptoPrimitives());
      _16_kmsHierarchyGenerateAndWrap = _nw0;
      KmsHierarchyWrapKeyMaterial _17_kmsHierarchyWrap;
      KmsHierarchyWrapKeyMaterial _nw1 = new KmsHierarchyWrapKeyMaterial();
      _nw1.__ctor((_9_hierarchicalMaterials).dtor_branchKey(), _5_branchKeyIdUtf8, _15_branchKeyVersionAsBytes, (this).cryptoPrimitives());
      _17_kmsHierarchyWrap = _nw1;
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError6 = Wrappers_Compile.Result.<EdkWrapping_Compile.WrapEdkMaterialOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.WrapEdkMaterialOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<HierarchyWrapInfo>Default(HierarchyWrapInfo._typeDescriptor(), HierarchyWrapInfo.Default()));
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<HierarchyWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
      _out3 = EdkWrapping_Compile.__default.<HierarchyWrapInfo>WrapEdkMaterial(HierarchyWrapInfo._typeDescriptor(), _0_materials, _17_kmsHierarchyWrap, _16_kmsHierarchyGenerateAndWrap);
      _18_valueOrError6 = _out3;
      if ((_18_valueOrError6).IsFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_18_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      EdkWrapping_Compile.WrapEdkMaterialOutput<HierarchyWrapInfo> _19_wrapOutput;
      _19_wrapOutput = (_18_valueOrError6).Extract(EdkWrapping_Compile.WrapEdkMaterialOutput.<HierarchyWrapInfo>_typeDescriptor(HierarchyWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _20_symmetricSigningKeyList;
      if (((_19_wrapOutput).dtor_symmetricSigningKey()).is_Some()) {
        _20_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_19_wrapOutput).dtor_symmetricSigningKey()).dtor_value()));
      } else {
        _20_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _21_edk;
      _21_edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(Constants_Compile.__default.PROVIDER__ID__HIERARCHY(), _5_branchKeyIdUtf8, (_19_wrapOutput).dtor_wrappedMaterial());
      if ((_19_wrapOutput).is_GenerateAndWrapEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _22_valueOrError7 = Materials_Compile.__default.EncryptionMaterialAddDataKey(_0_materials, (_19_wrapOutput).dtor_plaintextDataKey(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _21_edk), _20_symmetricSigningKeyList);
        if ((_22_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_22_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _23_result;
        _23_result = (_22_valueOrError7).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_23_result));
        return res;
      } else if ((_19_wrapOutput).is_WrapOnlyEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _24_valueOrError8 = Materials_Compile.__default.EncryptionMaterialAddEncryptedDataKeys(_0_materials, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _21_edk), _20_symmetricSigningKeyList);
        if ((_24_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_24_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _25_result;
        _25_result = (_24_valueOrError8).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_25_result));
        return res;
      }
    }
    return res;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _0_materials;
    _0_materials = (input).dtor_materials();
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_suite;
    _1_suite = ((input).dtor_materials()).dtor_algorithmSuite();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_0_materials), __default.E(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_2_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (this).GetBranchKeyId((_0_materials).dtor_encryptionContext());
    _3_valueOrError1 = _out0;
    if ((_3_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends Character> _4_branchKeyIdForDecrypt;
    _4_branchKeyIdForDecrypt = (_3_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    OnDecryptHierarchyEncryptedDataKeyFilter _5_filter;
    OnDecryptHierarchyEncryptedDataKeyFilter _nw0 = new OnDecryptHierarchyEncryptedDataKeyFilter();
    _nw0.__ctor(_4_branchKeyIdForDecrypt);
    _5_filter = _nw0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.Error>FilterWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _5_filter, (input).dtor_encryptedDataKeys());
    _6_valueOrError2 = _out1;
    if ((_6_valueOrError2).IsFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _7_edksToAttempt;
    _7_edksToAttempt = (_6_valueOrError2).Extract(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if ((java.math.BigInteger.valueOf((_7_edksToAttempt).length())).signum() == 0) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _8_valueOrError3 = ErrorMessages_Compile.__default.IncorrectDataKeys((input).dtor_encryptedDataKeys(), ((input).dtor_materials()).dtor_algorithmSuite(), dafny.DafnySequence.asString(""));
      if ((_8_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_8_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _9_errorMessage;
      _9_errorMessage = (_8_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_9_errorMessage));
      return res;
    }
    Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_decryptClosure;
    DecryptSingleEncryptedDataKey _nw1 = new DecryptSingleEncryptedDataKey();
    _nw1.__ctor(_0_materials, (this).keyStore(), (this).cryptoPrimitives(), _4_branchKeyIdForDecrypt, (this).ttlSeconds(), (this).cache(), (this).partitionIdBytes(), (this).logicalKeyStoreNameBytes());
    _10_decryptClosure = _nw1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _11_outcome;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _out2;
    _out2 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>ReduceToSuccess(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _10_decryptClosure, _7_edksToAttempt);
    _11_outcome = _out2;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _12_valueOrError4 = (_11_outcome).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_13_errors_boxed0) -> {
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_errors = ((dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_13_errors_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_13_errors, dafny.DafnySequence.asString("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."));
    }));
    if ((_12_valueOrError4).IsFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_12_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _14_SealedDecryptionMaterials;
    _14_SealedDecryptionMaterials = (_12_valueOrError4).Extract(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_14_SealedDecryptionMaterials));
    return res;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetActiveCacheId(dafny.DafnySequence<? extends Character> branchKeyId, dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdUtf8, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> cacheId = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((UTF8.__default.Decode(branchKeyIdUtf8)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError)).is_Success()) && (((boolean)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, Boolean>Let(((UTF8.__default.Decode(branchKeyIdUtf8)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError)).dtor_value(), boxed12 -> {
      dafny.DafnySequence<? extends Character> _pat_let6_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed12));
      return ((boolean)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, Boolean>Let(_pat_let6_0, boxed13 -> {
        dafny.DafnySequence<? extends Character> _1_branchKeyId = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed13));
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
    _4_scopeId = CacheConstants_Compile.__default.SCOPE__ID__ENCRYPT();
    dafny.DafnySequence<? extends java.lang.Byte> _5_suffix;
    _5_suffix = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate((this).logicalKeyStoreNameBytes(), CacheConstants_Compile.__default.NULL__BYTE()), branchKeyIdUtf8);
    dafny.DafnySequence<? extends java.lang.Byte> _6_identifier;
    _6_identifier = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_3_resourceId, CacheConstants_Compile.__default.NULL__BYTE()), _4_scopeId), CacheConstants_Compile.__default.NULL__BYTE()), (this).partitionIdBytes()), CacheConstants_Compile.__default.NULL__BYTE()), _5_suffix);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _7_maybeCacheIdDigest;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = (cryptoPrimitives).Digest(software.amazon.cryptography.primitives.internaldafny.types.DigestInput.create(_2_hashAlgorithm, _6_identifier));
    _7_maybeCacheIdDigest = _out0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _8_valueOrError1 = (_7_maybeCacheIdDigest).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_9_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _9_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_9_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_9_e);
    }));
    if ((_8_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_8_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _10_cacheDigest;
    _10_cacheDigest = (_8_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _11_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.util.Objects.equals(java.math.BigInteger.valueOf((_10_cacheDigest).length()), Digest_Compile.__default.Length(_2_hashAlgorithm)), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Digest generated a message not equal to the expected length.")));
    if ((_11_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      cacheId = (_11_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return cacheId;
    }
    cacheId = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _10_cacheDigest);
    return cacheId;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetActiveHierarchicalMaterials(dafny.DafnySequence<? extends Character> branchKeyId, dafny.DafnySequence<? extends java.lang.Byte> cacheId, software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore)
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
        Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_maybeGetActiveBranchKeyOutput;
        Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
        _out2 = (keyStore).GetActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput.create(branchKeyId));
        _3_maybeGetActiveBranchKeyOutput = _out2;
        Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
        _4_valueOrError0 = (_3_maybeGetActiveBranchKeyOutput).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.keystore.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
          software.amazon.cryptography.keystore.internaldafny.types.Error _5_e = ((software.amazon.cryptography.keystore.internaldafny.types.Error)(java.lang.Object)(_5_e_boxed0));
          return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyKeyStore(_5_e);
        }));
        if ((_4_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          material = (_4_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor());
          return material;
        }
        software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput _6_getActiveBranchKeyOutput;
        _6_getActiveBranchKeyOutput = (_4_valueOrError0).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials _7_branchKeyMaterials;
        _7_branchKeyMaterials = (_6_getActiveBranchKeyOutput).dtor_branchKeyMaterials();
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
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _cache;
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache cache()
  {
    return this._cache;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier> _branchKeyIdSupplier;
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier> branchKeyIdSupplier()
  {
    return this._branchKeyIdSupplier;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _branchKeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyId()
  {
    return this._branchKeyId;
  }
  public long _ttlSeconds;
  public long ttlSeconds()
  {
    return this._ttlSeconds;
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
  private static final dafny.TypeDescriptor<AwsKmsHierarchicalKeyring> _TYPE = dafny.TypeDescriptor.<AwsKmsHierarchicalKeyring>referenceWithInitializer(AwsKmsHierarchicalKeyring.class, () -> (AwsKmsHierarchicalKeyring) null);
  public static dafny.TypeDescriptor<AwsKmsHierarchicalKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsHierarchicalKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring";
  }
}
