// Class OnDecryptEcdhDataKeyFilter
// Dafny class OnDecryptEcdhDataKeyFilter compiled into Java
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
public class OnDecryptEcdhDataKeyFilter implements Actions_Compile.DeterministicActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.DeterministicAction<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public OnDecryptEcdhDataKeyFilter() {
    this._keyAgreementScheme = software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.Default();
    this._compressedRecipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._compressedSenderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations keyAgreementScheme, dafny.DafnySequence<? extends java.lang.Byte> compressedRecipientPublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> compressedSenderPublicKey)
  {
    (this)._keyAgreementScheme = keyAgreementScheme;
    (this)._compressedRecipientPublicKey = compressedRecipientPublicKey;
    if ((compressedSenderPublicKey).is_Some()) {
      (this)._compressedSenderPublicKey = (compressedSenderPublicKey).dtor_value();
    } else {
      (this)._compressedSenderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    }
  }
  public Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    if(true) {
      dafny.DafnySequence<? extends java.lang.Byte> _0_providerInfo;
      _0_providerInfo = (edk).dtor_keyProviderInfo();
      dafny.DafnySequence<? extends java.lang.Byte> _1_providerId;
      _1_providerId = (edk).dtor_keyProviderId();
      if ((!(_1_providerId).equals(Constants_Compile.__default.RAW__ECDH__PROVIDER__ID())) && (!(_1_providerId).equals(Constants_Compile.__default.KMS__ECDH__PROVIDER__ID()))) {
        res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
        return res;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _2_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.math.BigInteger.valueOf((_0_providerInfo).length())).compareTo(dafny.Helpers.unsignedToBigInteger(Constants_Compile.__default.ECDH__PROVIDER__INFO__521__LEN())) <= 0) && (__default.ValidProviderInfoLength(_0_providerInfo)), __default.E(dafny.DafnySequence.asString("EDK ProviderInfo longer than expected")));
      if ((_2_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_2_valueOrError0).<Boolean>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
        return res;
      }
      byte _3_keyringVersion;
      _3_keyringVersion = ((byte)(java.lang.Object)((_0_providerInfo).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _4_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (dafny.DafnySequence.<java.lang.Byte> of(_3_keyringVersion)).equals(__default.RAW__ECDH__KEYRING__VERSION()), __default.E(dafny.DafnySequence.asString("Incorrect Keyring version found in provider info.")));
      if ((_4_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_4_valueOrError1).<Boolean>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
        return res;
      }
      java.math.BigInteger _5_recipientPublicKeyLength = java.math.BigInteger.ZERO;
      _5_recipientPublicKeyLength = dafny.Helpers.unsignedToBigInteger(StandardLibrary_mUInt_Compile.__default.SeqToUInt32((_0_providerInfo).subsequence(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPL__INDEX(), Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX())));
      java.math.BigInteger _6_recipientPublicKeyLengthIndex = java.math.BigInteger.ZERO;
      _6_recipientPublicKeyLengthIndex = (dafny.Helpers.unsignedToBigInteger(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX())).add(_5_recipientPublicKeyLength);
      java.math.BigInteger _7_senderPublicKeyIndex = java.math.BigInteger.ZERO;
      _7_senderPublicKeyIndex = (_6_recipientPublicKeyLengthIndex).add(Constants_Compile.__default.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _8_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_6_recipientPublicKeyLengthIndex).add(java.math.BigInteger.valueOf(4L))).compareTo(java.math.BigInteger.valueOf((_0_providerInfo).length())) < 0, __default.E(dafny.DafnySequence.asString("Key Provider Info Serialization Error. Serialized length less than expected.")));
      if ((_8_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_8_valueOrError2).<Boolean>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _9_providerInfoRecipientPublicKey;
      _9_providerInfoRecipientPublicKey = (_0_providerInfo).subsequence(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX(), dafny.Helpers.toInt((_6_recipientPublicKeyLengthIndex)));
      dafny.DafnySequence<? extends java.lang.Byte> _10_providerInfoSenderPublicKey;
      _10_providerInfoSenderPublicKey = (_0_providerInfo).drop(_7_senderPublicKeyIndex);
      if (((this).keyAgreementScheme()).is_PublicKeyDiscovery()) {
        res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).compressedRecipientPublicKey()).equals(_9_providerInfoRecipientPublicKey));
        return res;
      } else {
        res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((((this).compressedSenderPublicKey()).equals(_10_providerInfoSenderPublicKey)) && (((this).compressedRecipientPublicKey()).equals(_9_providerInfoRecipientPublicKey))) || ((((this).compressedSenderPublicKey()).equals(_9_providerInfoRecipientPublicKey)) && (((this).compressedRecipientPublicKey()).equals(_10_providerInfoSenderPublicKey))));
        return res;
      }
    }
    return res;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _keyAgreementScheme;
  public software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations keyAgreementScheme()
  {
    return this._keyAgreementScheme;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _compressedRecipientPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> compressedRecipientPublicKey()
  {
    return this._compressedRecipientPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _compressedSenderPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> compressedSenderPublicKey()
  {
    return this._compressedSenderPublicKey;
  }
  private static final dafny.TypeDescriptor<OnDecryptEcdhDataKeyFilter> _TYPE = dafny.TypeDescriptor.<OnDecryptEcdhDataKeyFilter>referenceWithInitializer(OnDecryptEcdhDataKeyFilter.class, () -> (OnDecryptEcdhDataKeyFilter) null);
  public static dafny.TypeDescriptor<OnDecryptEcdhDataKeyFilter> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDecryptEcdhDataKeyFilter>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawECDHKeyring.OnDecryptEcdhDataKeyFilter";
  }
}
