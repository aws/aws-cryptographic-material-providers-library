// Class __default
// Dafny class __default compiled into Java
package AwsKmsEcdhKeyring_Compile;

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
import RawECDHKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DeriveSharedSecret(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends Character> senderAwsKmsKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretRequest _0_deriveSharedSecretRequest;
    _0_deriveSharedSecretRequest = software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretRequest.create(senderAwsKmsKey, software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec.create(), recipientPublicKey, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), grantTokens), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor()));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _1_maybeDeriveSharedSecret;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = (client).DeriveSharedSecret(_0_deriveSharedSecretRequest);
    _1_maybeDeriveSharedSecret = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse.Default());
    _2_valueOrError0 = (_1_maybeDeriveSharedSecret).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_3_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _3_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_3_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_ComAmazonawsKms(_3_e);
    }));
    if ((_2_valueOrError0).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse _4_deriveSharedSecretResponse;
    _4_deriveSharedSecretResponse = (_2_valueOrError0).Extract(software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _5_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((((((_4_deriveSharedSecretResponse).dtor_KeyId()).is_Some()) && (((_4_deriveSharedSecretResponse).dtor_SharedSecret()).is_Some())) && (((_4_deriveSharedSecretResponse).dtor_KeyAgreementAlgorithm()).is_Some())) && ((((_4_deriveSharedSecretResponse).dtor_KeyId()).dtor_value()).equals(senderAwsKmsKey))) && (java.util.Objects.equals(((_4_deriveSharedSecretResponse).dtor_KeyAgreementAlgorithm()).dtor_value(), software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec.create())), __default.E(dafny.DafnySequence.asString("Invalid response from KMS DeriveSharedSecret")));
    if ((_5_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.services.kms.internaldafny.types.PlaintextType._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_4_deriveSharedSecretResponse).dtor_SharedSecret()).dtor_value());
    return res;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Error E(dafny.DafnySequence<? extends Character> s) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(s);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> AWS__KMS__ECDH__KEYRING__VERSION()
  {
    return RawECDHKeyring_Compile.__default.RAW__ECDH__KEYRING__VERSION();
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsEcdhKeyring._default";
  }
}
