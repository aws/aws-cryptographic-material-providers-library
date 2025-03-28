// Class DecryptSingleEncryptedDataKey
// Dafny class DecryptSingleEncryptedDataKey compiled into Java
package RawECDHKeyring_Compile;

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
import AwsKmsHierarchicalKeyring_Compile.*;
import AwsKmsRsaKeyring_Compile.*;
import EcdhEdkWrapping_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptSingleEncryptedDataKey implements Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public DecryptSingleEncryptedDataKey() {
    this._materials = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials)null;
    this._cryptoPrimitives = null;
    this._recipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._senderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._keyAgreementScheme = software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.Default();
    this._curveSpec = software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.Default();
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives, dafny.DafnySequence<? extends java.lang.Byte> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey, software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations keyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec)
  {
    (this)._materials = materials;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._recipientPublicKey = recipientPublicKey;
    (this)._senderPublicKey = senderPublicKey;
    (this)._keyAgreementScheme = keyAgreementScheme;
    (this)._curveSpec = curveSpec;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.__default.ValidUTF8Seq((edk).dtor_keyProviderId()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Received invalid EDK provider id for AWS KMS ECDH Keyring")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_suite;
    _1_suite = ((this).materials()).dtor_algorithmSuite();
    dafny.DafnySequence<? extends java.lang.Byte> _2_keyProviderId;
    _2_keyProviderId = (edk).dtor_keyProviderId();
    dafny.DafnySequence<? extends java.lang.Byte> _3_providerInfo;
    _3_providerInfo = (edk).dtor_keyProviderInfo();
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
    _7_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.math.BigInteger.valueOf((_3_providerInfo).length())).compareTo(dafny.Helpers.unsignedToBigInteger(Constants_Compile.__default.ECDH__PROVIDER__INFO__521__LEN())) <= 0) && (__default.ValidProviderInfoLength(_3_providerInfo)), __default.E(dafny.DafnySequence.asString("EDK ProviderInfo longer than expected")));
    if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    byte _8_keyringVersion;
    _8_keyringVersion = ((byte)(java.lang.Object)((_3_providerInfo).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (dafny.DafnySequence.<java.lang.Byte> of(_8_keyringVersion)).equals(__default.RAW__ECDH__KEYRING__VERSION()), __default.E(dafny.DafnySequence.asString("Incorrect Keyring version found in provider info.")));
    if ((_9_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_9_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    java.math.BigInteger _10_recipientPublicKeyLength = java.math.BigInteger.ZERO;
    _10_recipientPublicKeyLength = dafny.Helpers.unsignedToBigInteger(StandardLibrary_mUInt_Compile.__default.SeqToUInt32((_3_providerInfo).subsequence(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPL__INDEX(), Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX())));
    java.math.BigInteger _11_recipientPublicKeyLengthIndex = java.math.BigInteger.ZERO;
    _11_recipientPublicKeyLengthIndex = (dafny.Helpers.unsignedToBigInteger(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX())).add(_10_recipientPublicKeyLength);
    java.math.BigInteger _12_senderPublicKeyIndex = java.math.BigInteger.ZERO;
    _12_senderPublicKeyIndex = (_11_recipientPublicKeyLengthIndex).add(Constants_Compile.__default.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _13_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_11_recipientPublicKeyLengthIndex).add(java.math.BigInteger.valueOf(4L))).compareTo(java.math.BigInteger.valueOf((_3_providerInfo).length())) < 0, __default.E(dafny.DafnySequence.asString("Key Provider Info Serialization Error. Serialized length less than expected.")));
    if ((_13_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_13_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _14_providerInfoRecipientPublicKey;
    _14_providerInfoRecipientPublicKey = (_3_providerInfo).subsequence(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX(), dafny.Helpers.toInt((_11_recipientPublicKeyLengthIndex)));
    dafny.DafnySequence<? extends java.lang.Byte> _15_providerInfoSenderPublicKey;
    _15_providerInfoSenderPublicKey = (_3_providerInfo).drop(_12_senderPublicKeyIndex);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = __default.DecompressPublicKey(_15_providerInfoSenderPublicKey, (this).curveSpec(), (this).cryptoPrimitives());
    _16_valueOrError5 = _out0;
    if ((_16_valueOrError5).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_16_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _17_senderPublicKey;
    _17_senderPublicKey = (_16_valueOrError5).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = __default.DecompressPublicKey(_14_providerInfoRecipientPublicKey, (this).curveSpec(), (this).cryptoPrimitives());
    _18_valueOrError6 = _out1;
    if ((_18_valueOrError6).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_18_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _19_recipientPublicKey;
    _19_recipientPublicKey = (_18_valueOrError6).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError7 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = __default.ValidatePublicKey((this).cryptoPrimitives(), (this).curveSpec(), _17_senderPublicKey);
    _20_valueOrError7 = _out2;
    if ((_20_valueOrError7).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_20_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    boolean _21___v0;
    _21___v0 = (_20_valueOrError7).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError8 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = __default.ValidatePublicKey((this).cryptoPrimitives(), (this).curveSpec(), _19_recipientPublicKey);
    _22_valueOrError8 = _out3;
    if ((_22_valueOrError8).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_22_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    boolean _23___v1;
    _23___v1 = (_22_valueOrError8).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _24_sharedSecretPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _25_sharedSecretPrivateKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _source0 = (this).keyAgreementScheme();
    if (_source0.is_PublicKeyDiscovery()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput _26___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations_PublicKeyDiscovery)_source0)._PublicKeyDiscovery;
      software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput _27_publicKeyDiscovery = _26___mcc_h0;
      {
        _24_sharedSecretPublicKey = _17_senderPublicKey;
        _25_sharedSecretPrivateKey = (_27_publicKeyDiscovery).dtor_recipientStaticPrivateKey();
      }
    } else if (_source0.is_RawPrivateKeyToStaticPublicKey()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput _28___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey)_source0)._RawPrivateKeyToStaticPublicKey;
      software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput _29_rawPrivateKeyToStaticPublicKey = _28___mcc_h1;
      {
        _25_sharedSecretPrivateKey = (_29_rawPrivateKeyToStaticPublicKey).dtor_senderStaticPrivateKey();
        if (((_29_rawPrivateKeyToStaticPublicKey).dtor_recipientPublicKey()).equals(_19_recipientPublicKey)) {
          _24_sharedSecretPublicKey = _19_recipientPublicKey;
        } else {
          _24_sharedSecretPublicKey = _17_senderPublicKey;
        }
      }
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput _30___mcc_h2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey)_source0)._EphemeralPrivateKeyToStaticPublicKey;
      {
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default.E(dafny.DafnySequence.asString("EphemeralPrivateKeyToStaticPublicKey Not allowed on decrypt")));
        return res;
      }
    }
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _31_valueOrError9 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = __default.ValidatePublicKey((this).cryptoPrimitives(), (this).curveSpec(), _24_sharedSecretPublicKey);
    _31_valueOrError9 = _out4;
    if ((_31_valueOrError9).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_31_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    boolean _32___v3;
    _32___v3 = (_31_valueOrError9).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _33_valueOrError10 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = __default.LocalDeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.create(_25_sharedSecretPrivateKey), software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_24_sharedSecretPublicKey), (this).curveSpec(), (this).cryptoPrimitives());
    _33_valueOrError10 = _out5;
    if ((_33_valueOrError10).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_33_valueOrError10).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _34_sharedSecret;
    _34_sharedSecret = (_33_valueOrError10).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    EcdhEdkWrapping_Compile.EcdhUnwrap _35_ecdhUnwrap;
    EcdhEdkWrapping_Compile.EcdhUnwrap _nw0 = new EcdhEdkWrapping_Compile.EcdhUnwrap();
    _nw0.__ctor(_15_providerInfoSenderPublicKey, _14_providerInfoRecipientPublicKey, _34_sharedSecret, __default.RAW__ECDH__KEYRING__VERSION(), (this).curveSpec(), (this).cryptoPrimitives());
    _35_ecdhUnwrap = _nw0;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _36_unwrapOutputRes;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = EdkWrapping_Compile.__default.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>UnwrapEdkMaterial(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor(), (edk).dtor_ciphertext(), (this).materials(), _35_ecdhUnwrap);
    _36_unwrapOutputRes = _out6;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _37_valueOrError11 = Wrappers_Compile.Result.<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>Default(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor(), EcdhEdkWrapping_Compile.EcdhUnwrapInfo.Default()));
    _37_valueOrError11 = _36_unwrapOutputRes;
    if ((_37_valueOrError11).IsFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_37_valueOrError11).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo> _38_unwrapOutput;
    _38_unwrapOutput = (_37_valueOrError11).Extract(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _39_valueOrError12 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _39_valueOrError12 = Materials_Compile.__default.DecryptionMaterialsAddDataKey((this).materials(), (_38_unwrapOutput).dtor_plaintextDataKey(), (_38_unwrapOutput).dtor_symmetricSigningKey());
    if ((_39_valueOrError12).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_39_valueOrError12).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _40_result;
    _40_result = (_39_valueOrError12).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _40_result);
    return res;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _materials;
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials()
  {
    return this._materials;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey()
  {
    return this._recipientPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _senderPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> senderPublicKey()
  {
    return this._senderPublicKey;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _keyAgreementScheme;
  public software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations keyAgreementScheme()
  {
    return this._keyAgreementScheme;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _curveSpec;
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec()
  {
    return this._curveSpec;
  }
  private static final dafny.TypeDescriptor<DecryptSingleEncryptedDataKey> _TYPE = dafny.TypeDescriptor.<DecryptSingleEncryptedDataKey>referenceWithInitializer(DecryptSingleEncryptedDataKey.class, () -> (DecryptSingleEncryptedDataKey) null);
  public static dafny.TypeDescriptor<DecryptSingleEncryptedDataKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptSingleEncryptedDataKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawECDHKeyring.DecryptSingleEncryptedDataKey";
  }
}
