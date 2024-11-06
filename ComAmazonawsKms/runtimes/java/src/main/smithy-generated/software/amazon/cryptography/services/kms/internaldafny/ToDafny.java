// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.services.kms.internaldafny;

import Wrappers_Compile.Option;
import dafny.DafnyMap;
import dafny.DafnySequence;
import dafny.TypeDescriptor;
import java.lang.Boolean;
import java.lang.Byte;
import java.lang.Character;
import java.lang.Exception;
import java.lang.Integer;
import java.lang.RuntimeException;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.awssdk.services.kms.model.AlreadyExistsException;
import software.amazon.awssdk.services.kms.model.CloudHsmClusterInUseException;
import software.amazon.awssdk.services.kms.model.CloudHsmClusterInvalidConfigurationException;
import software.amazon.awssdk.services.kms.model.CloudHsmClusterNotActiveException;
import software.amazon.awssdk.services.kms.model.CloudHsmClusterNotFoundException;
import software.amazon.awssdk.services.kms.model.CloudHsmClusterNotRelatedException;
import software.amazon.awssdk.services.kms.model.ConflictException;
import software.amazon.awssdk.services.kms.model.CustomKeyStoreHasCmKsException;
import software.amazon.awssdk.services.kms.model.CustomKeyStoreInvalidStateException;
import software.amazon.awssdk.services.kms.model.CustomKeyStoreNameInUseException;
import software.amazon.awssdk.services.kms.model.CustomKeyStoreNotFoundException;
import software.amazon.awssdk.services.kms.model.DependencyTimeoutException;
import software.amazon.awssdk.services.kms.model.DisabledException;
import software.amazon.awssdk.services.kms.model.DryRunOperationException;
import software.amazon.awssdk.services.kms.model.ExpiredImportTokenException;
import software.amazon.awssdk.services.kms.model.IncorrectKeyException;
import software.amazon.awssdk.services.kms.model.IncorrectKeyMaterialException;
import software.amazon.awssdk.services.kms.model.IncorrectTrustAnchorException;
import software.amazon.awssdk.services.kms.model.InvalidAliasNameException;
import software.amazon.awssdk.services.kms.model.InvalidArnException;
import software.amazon.awssdk.services.kms.model.InvalidCiphertextException;
import software.amazon.awssdk.services.kms.model.InvalidGrantIdException;
import software.amazon.awssdk.services.kms.model.InvalidGrantTokenException;
import software.amazon.awssdk.services.kms.model.InvalidImportTokenException;
import software.amazon.awssdk.services.kms.model.InvalidKeyUsageException;
import software.amazon.awssdk.services.kms.model.InvalidMarkerException;
import software.amazon.awssdk.services.kms.model.KeyUnavailableException;
import software.amazon.awssdk.services.kms.model.KmsException;
import software.amazon.awssdk.services.kms.model.KmsInternalException;
import software.amazon.awssdk.services.kms.model.KmsInvalidMacException;
import software.amazon.awssdk.services.kms.model.KmsInvalidSignatureException;
import software.amazon.awssdk.services.kms.model.KmsInvalidStateException;
import software.amazon.awssdk.services.kms.model.LimitExceededException;
import software.amazon.awssdk.services.kms.model.MalformedPolicyDocumentException;
import software.amazon.awssdk.services.kms.model.NotFoundException;
import software.amazon.awssdk.services.kms.model.TagException;
import software.amazon.awssdk.services.kms.model.UnsupportedOperationException;
import software.amazon.awssdk.services.kms.model.XksKeyAlreadyInUseException;
import software.amazon.awssdk.services.kms.model.XksKeyInvalidConfigurationException;
import software.amazon.awssdk.services.kms.model.XksKeyNotFoundException;
import software.amazon.awssdk.services.kms.model.XksProxyIncorrectAuthenticationCredentialException;
import software.amazon.awssdk.services.kms.model.XksProxyInvalidConfigurationException;
import software.amazon.awssdk.services.kms.model.XksProxyInvalidResponseException;
import software.amazon.awssdk.services.kms.model.XksProxyUriEndpointInUseException;
import software.amazon.awssdk.services.kms.model.XksProxyUriInUseException;
import software.amazon.awssdk.services.kms.model.XksProxyUriUnreachableException;
import software.amazon.awssdk.services.kms.model.XksProxyVpcEndpointServiceInUseException;
import software.amazon.awssdk.services.kms.model.XksProxyVpcEndpointServiceInvalidConfigurationException;
import software.amazon.awssdk.services.kms.model.XksProxyVpcEndpointServiceNotFoundException;
import software.amazon.cryptography.services.kms.internaldafny.types.AlgorithmSpec;
import software.amazon.cryptography.services.kms.internaldafny.types.AliasListEntry;
import software.amazon.cryptography.services.kms.internaldafny.types.CancelKeyDeletionRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.CancelKeyDeletionResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.ConnectCustomKeyStoreRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ConnectCustomKeyStoreResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.ConnectionErrorCodeType;
import software.amazon.cryptography.services.kms.internaldafny.types.ConnectionStateType;
import software.amazon.cryptography.services.kms.internaldafny.types.CreateAliasRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.CreateCustomKeyStoreRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.CreateCustomKeyStoreResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.CreateGrantRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.CreateGrantResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.CreateKeyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.CreateKeyResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.CustomKeyStoreType;
import software.amazon.cryptography.services.kms.internaldafny.types.CustomKeyStoresListEntry;
import software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec;
import software.amazon.cryptography.services.kms.internaldafny.types.DataKeyPairSpec;
import software.amazon.cryptography.services.kms.internaldafny.types.DataKeySpec;
import software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.DeleteAliasRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DeleteCustomKeyStoreRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DeleteCustomKeyStoreResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.DeleteImportedKeyMaterialRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DeriveSharedSecretResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.DescribeCustomKeyStoresRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DescribeCustomKeyStoresResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.DescribeKeyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DescribeKeyResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.DisableKeyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DisableKeyRotationRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DisconnectCustomKeyStoreRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.DisconnectCustomKeyStoreResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.EnableKeyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.EnableKeyRotationRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.EncryptRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec;
import software.amazon.cryptography.services.kms.internaldafny.types.Error;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_AlreadyExistsException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CloudHsmClusterInUseException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CloudHsmClusterInvalidConfigurationException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CloudHsmClusterNotActiveException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CloudHsmClusterNotFoundException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CloudHsmClusterNotRelatedException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_ConflictException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CustomKeyStoreHasCMKsException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CustomKeyStoreInvalidStateException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CustomKeyStoreNameInUseException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_CustomKeyStoreNotFoundException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_DependencyTimeoutException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_DisabledException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_DryRunOperationException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_ExpiredImportTokenException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_IncorrectKeyException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_IncorrectKeyMaterialException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_IncorrectTrustAnchorException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidAliasNameException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidArnException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidCiphertextException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidGrantIdException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidGrantTokenException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidImportTokenException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidKeyUsageException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_InvalidMarkerException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_KMSInternalException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_KMSInvalidMacException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_KMSInvalidSignatureException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_KMSInvalidStateException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_KeyUnavailableException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_LimitExceededException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_MalformedPolicyDocumentException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_NotFoundException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_TagException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_UnsupportedOperationException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksKeyAlreadyInUseException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksKeyInvalidConfigurationException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksKeyNotFoundException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyIncorrectAuthenticationCredentialException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyInvalidConfigurationException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyInvalidResponseException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyUriEndpointInUseException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyUriInUseException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyUriUnreachableException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyVpcEndpointServiceInUseException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyVpcEndpointServiceInvalidConfigurationException;
import software.amazon.cryptography.services.kms.internaldafny.types.Error_XksProxyVpcEndpointServiceNotFoundException;
import software.amazon.cryptography.services.kms.internaldafny.types.ExpirationModelType;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyPairRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyPairResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyPairWithoutPlaintextRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyPairWithoutPlaintextResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateMacRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateMacResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateRandomRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GenerateRandomResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GetKeyPolicyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GetKeyPolicyResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GetKeyRotationStatusRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GetKeyRotationStatusResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GetParametersForImportRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GetParametersForImportResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.GrantConstraints;
import software.amazon.cryptography.services.kms.internaldafny.types.GrantListEntry;
import software.amazon.cryptography.services.kms.internaldafny.types.GrantOperation;
import software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient;
import software.amazon.cryptography.services.kms.internaldafny.types.ImportKeyMaterialRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ImportKeyMaterialResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec;
import software.amazon.cryptography.services.kms.internaldafny.types.KeyEncryptionMechanism;
import software.amazon.cryptography.services.kms.internaldafny.types.KeyListEntry;
import software.amazon.cryptography.services.kms.internaldafny.types.KeyManagerType;
import software.amazon.cryptography.services.kms.internaldafny.types.KeyMetadata;
import software.amazon.cryptography.services.kms.internaldafny.types.KeySpec;
import software.amazon.cryptography.services.kms.internaldafny.types.KeyState;
import software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType;
import software.amazon.cryptography.services.kms.internaldafny.types.ListAliasesRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ListAliasesResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.ListGrantsRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ListGrantsResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.ListKeyPoliciesRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ListKeyPoliciesResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.ListKeyRotationsRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ListKeyRotationsResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.ListKeysRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ListKeysResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.ListResourceTagsRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ListResourceTagsResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.MacAlgorithmSpec;
import software.amazon.cryptography.services.kms.internaldafny.types.MessageType;
import software.amazon.cryptography.services.kms.internaldafny.types.MultiRegionConfiguration;
import software.amazon.cryptography.services.kms.internaldafny.types.MultiRegionKey;
import software.amazon.cryptography.services.kms.internaldafny.types.MultiRegionKeyType;
import software.amazon.cryptography.services.kms.internaldafny.types.OriginType;
import software.amazon.cryptography.services.kms.internaldafny.types.PutKeyPolicyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo;
import software.amazon.cryptography.services.kms.internaldafny.types.ReplicateKeyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ReplicateKeyResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.RetireGrantRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.RevokeGrantRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.RotateKeyOnDemandRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.RotateKeyOnDemandResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.RotationType;
import software.amazon.cryptography.services.kms.internaldafny.types.RotationsListEntry;
import software.amazon.cryptography.services.kms.internaldafny.types.ScheduleKeyDeletionRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.ScheduleKeyDeletionResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.SignRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.SignResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec;
import software.amazon.cryptography.services.kms.internaldafny.types.Tag;
import software.amazon.cryptography.services.kms.internaldafny.types.TagResourceRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.UntagResourceRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.UpdateAliasRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.UpdateCustomKeyStoreRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.UpdateCustomKeyStoreResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.UpdateKeyDescriptionRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.UpdatePrimaryRegionRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.VerifyMacRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.VerifyMacResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.VerifyRequest;
import software.amazon.cryptography.services.kms.internaldafny.types.VerifyResponse;
import software.amazon.cryptography.services.kms.internaldafny.types.WrappingKeySpec;
import software.amazon.cryptography.services.kms.internaldafny.types.XksKeyConfigurationType;
import software.amazon.cryptography.services.kms.internaldafny.types.XksProxyAuthenticationCredentialType;
import software.amazon.cryptography.services.kms.internaldafny.types.XksProxyConfigurationType;
import software.amazon.cryptography.services.kms.internaldafny.types.XksProxyConnectivityType;

public class ToDafny {

  public static DafnySequence<? extends AliasListEntry> AliasList(
    List<software.amazon.awssdk.services.kms.model.AliasListEntry> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::AliasListEntry,
      AliasListEntry._typeDescriptor()
    );
  }

  public static AliasListEntry AliasListEntry(
    software.amazon.awssdk.services.kms.model.AliasListEntry nativeValue
  ) {
    Option<DafnySequence<? extends Character>> aliasName;
    aliasName =
      Objects.nonNull(nativeValue.aliasName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.aliasName()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> aliasArn;
    aliasArn =
      Objects.nonNull(nativeValue.aliasArn())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.aliasArn()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> targetKeyId;
    targetKeyId =
      Objects.nonNull(nativeValue.targetKeyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.targetKeyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> creationDate;
    creationDate =
      Objects.nonNull(nativeValue.creationDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.creationDate()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> lastUpdatedDate;
    lastUpdatedDate =
      Objects.nonNull(nativeValue.lastUpdatedDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastUpdatedDate()
          )
        )
        : Option.create_None();
    return new AliasListEntry(
      aliasName,
      aliasArn,
      targetKeyId,
      creationDate,
      lastUpdatedDate
    );
  }

  public static CancelKeyDeletionRequest CancelKeyDeletionRequest(
    software.amazon.awssdk.services.kms.model.CancelKeyDeletionRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    return new CancelKeyDeletionRequest(keyId);
  }

  public static CancelKeyDeletionResponse CancelKeyDeletionResponse(
    software.amazon.awssdk.services.kms.model.CancelKeyDeletionResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    return new CancelKeyDeletionResponse(keyId);
  }

  public static ConnectCustomKeyStoreRequest ConnectCustomKeyStoreRequest(
    software.amazon.awssdk.services.kms.model.ConnectCustomKeyStoreRequest nativeValue
  ) {
    DafnySequence<? extends Character> customKeyStoreId;
    customKeyStoreId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.customKeyStoreId()
      );
    return new ConnectCustomKeyStoreRequest(customKeyStoreId);
  }

  public static ConnectCustomKeyStoreResponse ConnectCustomKeyStoreResponse(
    software.amazon.awssdk.services.kms.model.ConnectCustomKeyStoreResponse nativeValue
  ) {
    return new ConnectCustomKeyStoreResponse();
  }

  public static CreateAliasRequest CreateAliasRequest(
    software.amazon.awssdk.services.kms.model.CreateAliasRequest nativeValue
  ) {
    DafnySequence<? extends Character> aliasName;
    aliasName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.aliasName()
      );
    DafnySequence<? extends Character> targetKeyId;
    targetKeyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.targetKeyId()
      );
    return new CreateAliasRequest(aliasName, targetKeyId);
  }

  public static CreateCustomKeyStoreRequest CreateCustomKeyStoreRequest(
    software.amazon.awssdk.services.kms.model.CreateCustomKeyStoreRequest nativeValue
  ) {
    DafnySequence<? extends Character> customKeyStoreName;
    customKeyStoreName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.customKeyStoreName()
      );
    Option<DafnySequence<? extends Character>> cloudHsmClusterId;
    cloudHsmClusterId =
      Objects.nonNull(nativeValue.cloudHsmClusterId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.cloudHsmClusterId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> trustAnchorCertificate;
    trustAnchorCertificate =
      Objects.nonNull(nativeValue.trustAnchorCertificate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.trustAnchorCertificate()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyStorePassword;
    keyStorePassword =
      Objects.nonNull(nativeValue.keyStorePassword())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyStorePassword()
          )
        )
        : Option.create_None();
    Option<CustomKeyStoreType> customKeyStoreType;
    customKeyStoreType =
      Objects.nonNull(nativeValue.customKeyStoreType())
        ? Option.create_Some(
          ToDafny.CustomKeyStoreType(nativeValue.customKeyStoreType())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> xksProxyUriEndpoint;
    xksProxyUriEndpoint =
      Objects.nonNull(nativeValue.xksProxyUriEndpoint())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.xksProxyUriEndpoint()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> xksProxyUriPath;
    xksProxyUriPath =
      Objects.nonNull(nativeValue.xksProxyUriPath())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.xksProxyUriPath()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> xksProxyVpcEndpointServiceName;
    xksProxyVpcEndpointServiceName =
      Objects.nonNull(nativeValue.xksProxyVpcEndpointServiceName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.xksProxyVpcEndpointServiceName()
          )
        )
        : Option.create_None();
    Option<
      XksProxyAuthenticationCredentialType
    > xksProxyAuthenticationCredential;
    xksProxyAuthenticationCredential =
      Objects.nonNull(nativeValue.xksProxyAuthenticationCredential())
        ? Option.create_Some(
          ToDafny.XksProxyAuthenticationCredentialType(
            nativeValue.xksProxyAuthenticationCredential()
          )
        )
        : Option.create_None();
    Option<XksProxyConnectivityType> xksProxyConnectivity;
    xksProxyConnectivity =
      Objects.nonNull(nativeValue.xksProxyConnectivity())
        ? Option.create_Some(
          ToDafny.XksProxyConnectivityType(nativeValue.xksProxyConnectivity())
        )
        : Option.create_None();
    return new CreateCustomKeyStoreRequest(
      customKeyStoreName,
      cloudHsmClusterId,
      trustAnchorCertificate,
      keyStorePassword,
      customKeyStoreType,
      xksProxyUriEndpoint,
      xksProxyUriPath,
      xksProxyVpcEndpointServiceName,
      xksProxyAuthenticationCredential,
      xksProxyConnectivity
    );
  }

  public static CreateCustomKeyStoreResponse CreateCustomKeyStoreResponse(
    software.amazon.awssdk.services.kms.model.CreateCustomKeyStoreResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> customKeyStoreId;
    customKeyStoreId =
      Objects.nonNull(nativeValue.customKeyStoreId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreId()
          )
        )
        : Option.create_None();
    return new CreateCustomKeyStoreResponse(customKeyStoreId);
  }

  public static CreateGrantRequest CreateGrantRequest(
    software.amazon.awssdk.services.kms.model.CreateGrantRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Character> granteePrincipal;
    granteePrincipal =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.granteePrincipal()
      );
    Option<DafnySequence<? extends Character>> retiringPrincipal;
    retiringPrincipal =
      Objects.nonNull(nativeValue.retiringPrincipal())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.retiringPrincipal()
          )
        )
        : Option.create_None();
    DafnySequence<? extends GrantOperation> operations;
    operations = ToDafny.GrantOperationList(nativeValue.operations());
    Option<GrantConstraints> constraints;
    constraints =
      Objects.nonNull(nativeValue.constraints())
        ? Option.create_Some(
          ToDafny.GrantConstraints(nativeValue.constraints())
        )
        : Option.create_None();
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> name;
    name =
      Objects.nonNull(nativeValue.name())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.name()
          )
        )
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new CreateGrantRequest(
      keyId,
      granteePrincipal,
      retiringPrincipal,
      operations,
      constraints,
      grantTokens,
      name,
      dryRun
    );
  }

  public static CreateGrantResponse CreateGrantResponse(
    software.amazon.awssdk.services.kms.model.CreateGrantResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> grantToken;
    grantToken =
      Objects.nonNull(nativeValue.grantToken())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.grantToken()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> grantId;
    grantId =
      Objects.nonNull(nativeValue.grantId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.grantId()
          )
        )
        : Option.create_None();
    return new CreateGrantResponse(grantToken, grantId);
  }

  public static CreateKeyRequest CreateKeyRequest(
    software.amazon.awssdk.services.kms.model.CreateKeyRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> policy;
    policy =
      Objects.nonNull(nativeValue.policy())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policy()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> description;
    description =
      Objects.nonNull(nativeValue.description())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.description()
          )
        )
        : Option.create_None();
    Option<KeyUsageType> keyUsage;
    keyUsage =
      Objects.nonNull(nativeValue.keyUsage())
        ? Option.create_Some(ToDafny.KeyUsageType(nativeValue.keyUsage()))
        : Option.create_None();
    Option<CustomerMasterKeySpec> customerMasterKeySpec;
    customerMasterKeySpec =
      Objects.nonNull(nativeValue.customerMasterKeySpec())
        ? Option.create_Some(
          ToDafny.CustomerMasterKeySpec(nativeValue.customerMasterKeySpec())
        )
        : Option.create_None();
    Option<KeySpec> keySpec;
    keySpec =
      Objects.nonNull(nativeValue.keySpec())
        ? Option.create_Some(ToDafny.KeySpec(nativeValue.keySpec()))
        : Option.create_None();
    Option<OriginType> origin;
    origin =
      Objects.nonNull(nativeValue.origin())
        ? Option.create_Some(ToDafny.OriginType(nativeValue.origin()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> customKeyStoreId;
    customKeyStoreId =
      Objects.nonNull(nativeValue.customKeyStoreId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreId()
          )
        )
        : Option.create_None();
    Option<Boolean> bypassPolicyLockoutSafetyCheck;
    bypassPolicyLockoutSafetyCheck =
      Objects.nonNull(nativeValue.bypassPolicyLockoutSafetyCheck())
        ? Option.create_Some((nativeValue.bypassPolicyLockoutSafetyCheck()))
        : Option.create_None();
    Option<DafnySequence<? extends Tag>> tags;
    tags =
      (Objects.nonNull(nativeValue.tags()) && nativeValue.tags().size() > 0)
        ? Option.create_Some(ToDafny.TagList(nativeValue.tags()))
        : Option.create_None();
    Option<Boolean> multiRegion;
    multiRegion =
      Objects.nonNull(nativeValue.multiRegion())
        ? Option.create_Some((nativeValue.multiRegion()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> xksKeyId;
    xksKeyId =
      Objects.nonNull(nativeValue.xksKeyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.xksKeyId()
          )
        )
        : Option.create_None();
    return new CreateKeyRequest(
      policy,
      description,
      keyUsage,
      customerMasterKeySpec,
      keySpec,
      origin,
      customKeyStoreId,
      bypassPolicyLockoutSafetyCheck,
      tags,
      multiRegion,
      xksKeyId
    );
  }

  public static CreateKeyResponse CreateKeyResponse(
    software.amazon.awssdk.services.kms.model.CreateKeyResponse nativeValue
  ) {
    Option<KeyMetadata> keyMetadata;
    keyMetadata =
      Objects.nonNull(nativeValue.keyMetadata())
        ? Option.create_Some(ToDafny.KeyMetadata(nativeValue.keyMetadata()))
        : Option.create_None();
    return new CreateKeyResponse(keyMetadata);
  }

  public static DafnySequence<
    ? extends CustomKeyStoresListEntry
  > CustomKeyStoresList(
    List<
      software.amazon.awssdk.services.kms.model.CustomKeyStoresListEntry
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::CustomKeyStoresListEntry,
      CustomKeyStoresListEntry._typeDescriptor()
    );
  }

  public static CustomKeyStoresListEntry CustomKeyStoresListEntry(
    software.amazon.awssdk.services.kms.model.CustomKeyStoresListEntry nativeValue
  ) {
    Option<DafnySequence<? extends Character>> customKeyStoreId;
    customKeyStoreId =
      Objects.nonNull(nativeValue.customKeyStoreId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> customKeyStoreName;
    customKeyStoreName =
      Objects.nonNull(nativeValue.customKeyStoreName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreName()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> cloudHsmClusterId;
    cloudHsmClusterId =
      Objects.nonNull(nativeValue.cloudHsmClusterId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.cloudHsmClusterId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> trustAnchorCertificate;
    trustAnchorCertificate =
      Objects.nonNull(nativeValue.trustAnchorCertificate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.trustAnchorCertificate()
          )
        )
        : Option.create_None();
    Option<ConnectionStateType> connectionState;
    connectionState =
      Objects.nonNull(nativeValue.connectionState())
        ? Option.create_Some(
          ToDafny.ConnectionStateType(nativeValue.connectionState())
        )
        : Option.create_None();
    Option<ConnectionErrorCodeType> connectionErrorCode;
    connectionErrorCode =
      Objects.nonNull(nativeValue.connectionErrorCode())
        ? Option.create_Some(
          ToDafny.ConnectionErrorCodeType(nativeValue.connectionErrorCode())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> creationDate;
    creationDate =
      Objects.nonNull(nativeValue.creationDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.creationDate()
          )
        )
        : Option.create_None();
    Option<CustomKeyStoreType> customKeyStoreType;
    customKeyStoreType =
      Objects.nonNull(nativeValue.customKeyStoreType())
        ? Option.create_Some(
          ToDafny.CustomKeyStoreType(nativeValue.customKeyStoreType())
        )
        : Option.create_None();
    Option<XksProxyConfigurationType> xksProxyConfiguration;
    xksProxyConfiguration =
      Objects.nonNull(nativeValue.xksProxyConfiguration())
        ? Option.create_Some(
          ToDafny.XksProxyConfigurationType(nativeValue.xksProxyConfiguration())
        )
        : Option.create_None();
    return new CustomKeyStoresListEntry(
      customKeyStoreId,
      customKeyStoreName,
      cloudHsmClusterId,
      trustAnchorCertificate,
      connectionState,
      connectionErrorCode,
      creationDate,
      customKeyStoreType,
      xksProxyConfiguration
    );
  }

  public static DecryptRequest DecryptRequest(
    software.amazon.awssdk.services.kms.model.DecryptRequest nativeValue
  ) {
    DafnySequence<? extends Byte> ciphertextBlob;
    ciphertextBlob =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.ciphertextBlob().asByteArray()
      );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContext;
    encryptionContext =
      (Objects.nonNull(nativeValue.encryptionContext()) &&
          nativeValue.encryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContext())
        )
        : Option.create_None();
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> encryptionAlgorithm;
    encryptionAlgorithm =
      Objects.nonNull(nativeValue.encryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(nativeValue.encryptionAlgorithm())
        )
        : Option.create_None();
    Option<RecipientInfo> recipient;
    recipient =
      Objects.nonNull(nativeValue.recipient())
        ? Option.create_Some(ToDafny.RecipientInfo(nativeValue.recipient()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new DecryptRequest(
      ciphertextBlob,
      encryptionContext,
      grantTokens,
      keyId,
      encryptionAlgorithm,
      recipient,
      dryRun
    );
  }

  public static DecryptResponse DecryptResponse(
    software.amazon.awssdk.services.kms.model.DecryptResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> plaintext;
    plaintext =
      Objects.nonNull(nativeValue.plaintext())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.plaintext().asByteArray()
          )
        )
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> encryptionAlgorithm;
    encryptionAlgorithm =
      Objects.nonNull(nativeValue.encryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(nativeValue.encryptionAlgorithm())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> ciphertextForRecipient;
    ciphertextForRecipient =
      Objects.nonNull(nativeValue.ciphertextForRecipient())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextForRecipient().asByteArray()
          )
        )
        : Option.create_None();
    return new DecryptResponse(
      keyId,
      plaintext,
      encryptionAlgorithm,
      ciphertextForRecipient
    );
  }

  public static DeleteAliasRequest DeleteAliasRequest(
    software.amazon.awssdk.services.kms.model.DeleteAliasRequest nativeValue
  ) {
    DafnySequence<? extends Character> aliasName;
    aliasName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.aliasName()
      );
    return new DeleteAliasRequest(aliasName);
  }

  public static DeleteCustomKeyStoreRequest DeleteCustomKeyStoreRequest(
    software.amazon.awssdk.services.kms.model.DeleteCustomKeyStoreRequest nativeValue
  ) {
    DafnySequence<? extends Character> customKeyStoreId;
    customKeyStoreId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.customKeyStoreId()
      );
    return new DeleteCustomKeyStoreRequest(customKeyStoreId);
  }

  public static DeleteCustomKeyStoreResponse DeleteCustomKeyStoreResponse(
    software.amazon.awssdk.services.kms.model.DeleteCustomKeyStoreResponse nativeValue
  ) {
    return new DeleteCustomKeyStoreResponse();
  }

  public static DeleteImportedKeyMaterialRequest DeleteImportedKeyMaterialRequest(
    software.amazon.awssdk.services.kms.model.DeleteImportedKeyMaterialRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    return new DeleteImportedKeyMaterialRequest(keyId);
  }

  public static DeriveSharedSecretRequest DeriveSharedSecretRequest(
    software.amazon.awssdk.services.kms.model.DeriveSharedSecretRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    KeyAgreementAlgorithmSpec keyAgreementAlgorithm;
    keyAgreementAlgorithm =
      ToDafny.KeyAgreementAlgorithmSpec(nativeValue.keyAgreementAlgorithm());
    DafnySequence<? extends Byte> publicKey;
    publicKey =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.publicKey().asByteArray()
      );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    Option<RecipientInfo> recipient;
    recipient =
      Objects.nonNull(nativeValue.recipient())
        ? Option.create_Some(ToDafny.RecipientInfo(nativeValue.recipient()))
        : Option.create_None();
    return new DeriveSharedSecretRequest(
      keyId,
      keyAgreementAlgorithm,
      publicKey,
      grantTokens,
      dryRun,
      recipient
    );
  }

  public static DeriveSharedSecretResponse DeriveSharedSecretResponse(
    software.amazon.awssdk.services.kms.model.DeriveSharedSecretResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> sharedSecret;
    sharedSecret =
      Objects.nonNull(nativeValue.sharedSecret())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.sharedSecret().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> ciphertextForRecipient;
    ciphertextForRecipient =
      Objects.nonNull(nativeValue.ciphertextForRecipient())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextForRecipient().asByteArray()
          )
        )
        : Option.create_None();
    Option<KeyAgreementAlgorithmSpec> keyAgreementAlgorithm;
    keyAgreementAlgorithm =
      Objects.nonNull(nativeValue.keyAgreementAlgorithm())
        ? Option.create_Some(
          ToDafny.KeyAgreementAlgorithmSpec(nativeValue.keyAgreementAlgorithm())
        )
        : Option.create_None();
    Option<OriginType> keyOrigin;
    keyOrigin =
      Objects.nonNull(nativeValue.keyOrigin())
        ? Option.create_Some(ToDafny.OriginType(nativeValue.keyOrigin()))
        : Option.create_None();
    return new DeriveSharedSecretResponse(
      keyId,
      sharedSecret,
      ciphertextForRecipient,
      keyAgreementAlgorithm,
      keyOrigin
    );
  }

  public static DescribeCustomKeyStoresRequest DescribeCustomKeyStoresRequest(
    software.amazon.awssdk.services.kms.model.DescribeCustomKeyStoresRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> customKeyStoreId;
    customKeyStoreId =
      Objects.nonNull(nativeValue.customKeyStoreId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> customKeyStoreName;
    customKeyStoreName =
      Objects.nonNull(nativeValue.customKeyStoreName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreName()
          )
        )
        : Option.create_None();
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some((nativeValue.limit()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> marker;
    marker =
      Objects.nonNull(nativeValue.marker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.marker()
          )
        )
        : Option.create_None();
    return new DescribeCustomKeyStoresRequest(
      customKeyStoreId,
      customKeyStoreName,
      limit,
      marker
    );
  }

  public static DescribeCustomKeyStoresResponse DescribeCustomKeyStoresResponse(
    software.amazon.awssdk.services.kms.model.DescribeCustomKeyStoresResponse nativeValue
  ) {
    Option<DafnySequence<? extends CustomKeyStoresListEntry>> customKeyStores;
    customKeyStores =
      (Objects.nonNull(nativeValue.customKeyStores()) &&
          nativeValue.customKeyStores().size() > 0)
        ? Option.create_Some(
          ToDafny.CustomKeyStoresList(nativeValue.customKeyStores())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextMarker;
    nextMarker =
      Objects.nonNull(nativeValue.nextMarker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextMarker()
          )
        )
        : Option.create_None();
    Option<Boolean> truncated;
    truncated =
      Objects.nonNull(nativeValue.truncated())
        ? Option.create_Some((nativeValue.truncated()))
        : Option.create_None();
    return new DescribeCustomKeyStoresResponse(
      customKeyStores,
      nextMarker,
      truncated
    );
  }

  public static DescribeKeyRequest DescribeKeyRequest(
    software.amazon.awssdk.services.kms.model.DescribeKeyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    return new DescribeKeyRequest(keyId, grantTokens);
  }

  public static DescribeKeyResponse DescribeKeyResponse(
    software.amazon.awssdk.services.kms.model.DescribeKeyResponse nativeValue
  ) {
    Option<KeyMetadata> keyMetadata;
    keyMetadata =
      Objects.nonNull(nativeValue.keyMetadata())
        ? Option.create_Some(ToDafny.KeyMetadata(nativeValue.keyMetadata()))
        : Option.create_None();
    return new DescribeKeyResponse(keyMetadata);
  }

  public static DisableKeyRequest DisableKeyRequest(
    software.amazon.awssdk.services.kms.model.DisableKeyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    return new DisableKeyRequest(keyId);
  }

  public static DisableKeyRotationRequest DisableKeyRotationRequest(
    software.amazon.awssdk.services.kms.model.DisableKeyRotationRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    return new DisableKeyRotationRequest(keyId);
  }

  public static DisconnectCustomKeyStoreRequest DisconnectCustomKeyStoreRequest(
    software.amazon.awssdk.services.kms.model.DisconnectCustomKeyStoreRequest nativeValue
  ) {
    DafnySequence<? extends Character> customKeyStoreId;
    customKeyStoreId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.customKeyStoreId()
      );
    return new DisconnectCustomKeyStoreRequest(customKeyStoreId);
  }

  public static DisconnectCustomKeyStoreResponse DisconnectCustomKeyStoreResponse(
    software.amazon.awssdk.services.kms.model.DisconnectCustomKeyStoreResponse nativeValue
  ) {
    return new DisconnectCustomKeyStoreResponse();
  }

  public static EnableKeyRequest EnableKeyRequest(
    software.amazon.awssdk.services.kms.model.EnableKeyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    return new EnableKeyRequest(keyId);
  }

  public static EnableKeyRotationRequest EnableKeyRotationRequest(
    software.amazon.awssdk.services.kms.model.EnableKeyRotationRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<Integer> rotationPeriodInDays;
    rotationPeriodInDays =
      Objects.nonNull(nativeValue.rotationPeriodInDays())
        ? Option.create_Some((nativeValue.rotationPeriodInDays()))
        : Option.create_None();
    return new EnableKeyRotationRequest(keyId, rotationPeriodInDays);
  }

  public static DafnySequence<
    ? extends EncryptionAlgorithmSpec
  > EncryptionAlgorithmSpecList(
    List<
      software.amazon.awssdk.services.kms.model.EncryptionAlgorithmSpec
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::EncryptionAlgorithmSpec,
      EncryptionAlgorithmSpec._typeDescriptor()
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends DafnySequence<? extends Character>
  > EncryptionContextType(Map<String, String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence
    );
  }

  public static EncryptRequest EncryptRequest(
    software.amazon.awssdk.services.kms.model.EncryptRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Byte> plaintext;
    plaintext =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.plaintext().asByteArray()
      );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContext;
    encryptionContext =
      (Objects.nonNull(nativeValue.encryptionContext()) &&
          nativeValue.encryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContext())
        )
        : Option.create_None();
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> encryptionAlgorithm;
    encryptionAlgorithm =
      Objects.nonNull(nativeValue.encryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(nativeValue.encryptionAlgorithm())
        )
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new EncryptRequest(
      keyId,
      plaintext,
      encryptionContext,
      grantTokens,
      encryptionAlgorithm,
      dryRun
    );
  }

  public static EncryptResponse EncryptResponse(
    software.amazon.awssdk.services.kms.model.EncryptResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> ciphertextBlob;
    ciphertextBlob =
      Objects.nonNull(nativeValue.ciphertextBlob())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextBlob().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> encryptionAlgorithm;
    encryptionAlgorithm =
      Objects.nonNull(nativeValue.encryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(nativeValue.encryptionAlgorithm())
        )
        : Option.create_None();
    return new EncryptResponse(ciphertextBlob, keyId, encryptionAlgorithm);
  }

  public static GenerateDataKeyPairRequest GenerateDataKeyPairRequest(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyPairRequest nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContext;
    encryptionContext =
      (Objects.nonNull(nativeValue.encryptionContext()) &&
          nativeValue.encryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContext())
        )
        : Option.create_None();
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DataKeyPairSpec keyPairSpec;
    keyPairSpec = ToDafny.DataKeyPairSpec(nativeValue.keyPairSpec());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<RecipientInfo> recipient;
    recipient =
      Objects.nonNull(nativeValue.recipient())
        ? Option.create_Some(ToDafny.RecipientInfo(nativeValue.recipient()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new GenerateDataKeyPairRequest(
      encryptionContext,
      keyId,
      keyPairSpec,
      grantTokens,
      recipient,
      dryRun
    );
  }

  public static GenerateDataKeyPairResponse GenerateDataKeyPairResponse(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyPairResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> privateKeyCiphertextBlob;
    privateKeyCiphertextBlob =
      Objects.nonNull(nativeValue.privateKeyCiphertextBlob())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.privateKeyCiphertextBlob().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> privateKeyPlaintext;
    privateKeyPlaintext =
      Objects.nonNull(nativeValue.privateKeyPlaintext())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.privateKeyPlaintext().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> publicKey;
    publicKey =
      Objects.nonNull(nativeValue.publicKey())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.publicKey().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DataKeyPairSpec> keyPairSpec;
    keyPairSpec =
      Objects.nonNull(nativeValue.keyPairSpec())
        ? Option.create_Some(ToDafny.DataKeyPairSpec(nativeValue.keyPairSpec()))
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> ciphertextForRecipient;
    ciphertextForRecipient =
      Objects.nonNull(nativeValue.ciphertextForRecipient())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextForRecipient().asByteArray()
          )
        )
        : Option.create_None();
    return new GenerateDataKeyPairResponse(
      privateKeyCiphertextBlob,
      privateKeyPlaintext,
      publicKey,
      keyId,
      keyPairSpec,
      ciphertextForRecipient
    );
  }

  public static GenerateDataKeyPairWithoutPlaintextRequest GenerateDataKeyPairWithoutPlaintextRequest(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyPairWithoutPlaintextRequest nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContext;
    encryptionContext =
      (Objects.nonNull(nativeValue.encryptionContext()) &&
          nativeValue.encryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContext())
        )
        : Option.create_None();
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DataKeyPairSpec keyPairSpec;
    keyPairSpec = ToDafny.DataKeyPairSpec(nativeValue.keyPairSpec());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new GenerateDataKeyPairWithoutPlaintextRequest(
      encryptionContext,
      keyId,
      keyPairSpec,
      grantTokens,
      dryRun
    );
  }

  public static GenerateDataKeyPairWithoutPlaintextResponse GenerateDataKeyPairWithoutPlaintextResponse(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyPairWithoutPlaintextResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> privateKeyCiphertextBlob;
    privateKeyCiphertextBlob =
      Objects.nonNull(nativeValue.privateKeyCiphertextBlob())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.privateKeyCiphertextBlob().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> publicKey;
    publicKey =
      Objects.nonNull(nativeValue.publicKey())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.publicKey().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DataKeyPairSpec> keyPairSpec;
    keyPairSpec =
      Objects.nonNull(nativeValue.keyPairSpec())
        ? Option.create_Some(ToDafny.DataKeyPairSpec(nativeValue.keyPairSpec()))
        : Option.create_None();
    return new GenerateDataKeyPairWithoutPlaintextResponse(
      privateKeyCiphertextBlob,
      publicKey,
      keyId,
      keyPairSpec
    );
  }

  public static GenerateDataKeyRequest GenerateDataKeyRequest(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContext;
    encryptionContext =
      (Objects.nonNull(nativeValue.encryptionContext()) &&
          nativeValue.encryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContext())
        )
        : Option.create_None();
    Option<Integer> numberOfBytes;
    numberOfBytes =
      Objects.nonNull(nativeValue.numberOfBytes())
        ? Option.create_Some((nativeValue.numberOfBytes()))
        : Option.create_None();
    Option<DataKeySpec> keySpec;
    keySpec =
      Objects.nonNull(nativeValue.keySpec())
        ? Option.create_Some(ToDafny.DataKeySpec(nativeValue.keySpec()))
        : Option.create_None();
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<RecipientInfo> recipient;
    recipient =
      Objects.nonNull(nativeValue.recipient())
        ? Option.create_Some(ToDafny.RecipientInfo(nativeValue.recipient()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new GenerateDataKeyRequest(
      keyId,
      encryptionContext,
      numberOfBytes,
      keySpec,
      grantTokens,
      recipient,
      dryRun
    );
  }

  public static GenerateDataKeyResponse GenerateDataKeyResponse(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> ciphertextBlob;
    ciphertextBlob =
      Objects.nonNull(nativeValue.ciphertextBlob())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextBlob().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> plaintext;
    plaintext =
      Objects.nonNull(nativeValue.plaintext())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.plaintext().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> ciphertextForRecipient;
    ciphertextForRecipient =
      Objects.nonNull(nativeValue.ciphertextForRecipient())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextForRecipient().asByteArray()
          )
        )
        : Option.create_None();
    return new GenerateDataKeyResponse(
      ciphertextBlob,
      plaintext,
      keyId,
      ciphertextForRecipient
    );
  }

  public static GenerateDataKeyWithoutPlaintextRequest GenerateDataKeyWithoutPlaintextRequest(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyWithoutPlaintextRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContext;
    encryptionContext =
      (Objects.nonNull(nativeValue.encryptionContext()) &&
          nativeValue.encryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContext())
        )
        : Option.create_None();
    Option<DataKeySpec> keySpec;
    keySpec =
      Objects.nonNull(nativeValue.keySpec())
        ? Option.create_Some(ToDafny.DataKeySpec(nativeValue.keySpec()))
        : Option.create_None();
    Option<Integer> numberOfBytes;
    numberOfBytes =
      Objects.nonNull(nativeValue.numberOfBytes())
        ? Option.create_Some((nativeValue.numberOfBytes()))
        : Option.create_None();
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new GenerateDataKeyWithoutPlaintextRequest(
      keyId,
      encryptionContext,
      keySpec,
      numberOfBytes,
      grantTokens,
      dryRun
    );
  }

  public static GenerateDataKeyWithoutPlaintextResponse GenerateDataKeyWithoutPlaintextResponse(
    software.amazon.awssdk.services.kms.model.GenerateDataKeyWithoutPlaintextResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> ciphertextBlob;
    ciphertextBlob =
      Objects.nonNull(nativeValue.ciphertextBlob())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextBlob().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    return new GenerateDataKeyWithoutPlaintextResponse(ciphertextBlob, keyId);
  }

  public static GenerateMacRequest GenerateMacRequest(
    software.amazon.awssdk.services.kms.model.GenerateMacRequest nativeValue
  ) {
    DafnySequence<? extends Byte> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.message().asByteArray()
      );
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    MacAlgorithmSpec macAlgorithm;
    macAlgorithm = ToDafny.MacAlgorithmSpec(nativeValue.macAlgorithm());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new GenerateMacRequest(
      message,
      keyId,
      macAlgorithm,
      grantTokens,
      dryRun
    );
  }

  public static GenerateMacResponse GenerateMacResponse(
    software.amazon.awssdk.services.kms.model.GenerateMacResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> mac;
    mac =
      Objects.nonNull(nativeValue.mac())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.mac().asByteArray()
          )
        )
        : Option.create_None();
    Option<MacAlgorithmSpec> macAlgorithm;
    macAlgorithm =
      Objects.nonNull(nativeValue.macAlgorithm())
        ? Option.create_Some(
          ToDafny.MacAlgorithmSpec(nativeValue.macAlgorithm())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    return new GenerateMacResponse(mac, macAlgorithm, keyId);
  }

  public static GenerateRandomRequest GenerateRandomRequest(
    software.amazon.awssdk.services.kms.model.GenerateRandomRequest nativeValue
  ) {
    Option<Integer> numberOfBytes;
    numberOfBytes =
      Objects.nonNull(nativeValue.numberOfBytes())
        ? Option.create_Some((nativeValue.numberOfBytes()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> customKeyStoreId;
    customKeyStoreId =
      Objects.nonNull(nativeValue.customKeyStoreId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreId()
          )
        )
        : Option.create_None();
    Option<RecipientInfo> recipient;
    recipient =
      Objects.nonNull(nativeValue.recipient())
        ? Option.create_Some(ToDafny.RecipientInfo(nativeValue.recipient()))
        : Option.create_None();
    return new GenerateRandomRequest(
      numberOfBytes,
      customKeyStoreId,
      recipient
    );
  }

  public static GenerateRandomResponse GenerateRandomResponse(
    software.amazon.awssdk.services.kms.model.GenerateRandomResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> plaintext;
    plaintext =
      Objects.nonNull(nativeValue.plaintext())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.plaintext().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> ciphertextForRecipient;
    ciphertextForRecipient =
      Objects.nonNull(nativeValue.ciphertextForRecipient())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextForRecipient().asByteArray()
          )
        )
        : Option.create_None();
    return new GenerateRandomResponse(plaintext, ciphertextForRecipient);
  }

  public static GetKeyPolicyRequest GetKeyPolicyRequest(
    software.amazon.awssdk.services.kms.model.GetKeyPolicyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<DafnySequence<? extends Character>> policyName;
    policyName =
      Objects.nonNull(nativeValue.policyName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policyName()
          )
        )
        : Option.create_None();
    return new GetKeyPolicyRequest(keyId, policyName);
  }

  public static GetKeyPolicyResponse GetKeyPolicyResponse(
    software.amazon.awssdk.services.kms.model.GetKeyPolicyResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> policy;
    policy =
      Objects.nonNull(nativeValue.policy())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policy()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> policyName;
    policyName =
      Objects.nonNull(nativeValue.policyName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policyName()
          )
        )
        : Option.create_None();
    return new GetKeyPolicyResponse(policy, policyName);
  }

  public static GetKeyRotationStatusRequest GetKeyRotationStatusRequest(
    software.amazon.awssdk.services.kms.model.GetKeyRotationStatusRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    return new GetKeyRotationStatusRequest(keyId);
  }

  public static GetKeyRotationStatusResponse GetKeyRotationStatusResponse(
    software.amazon.awssdk.services.kms.model.GetKeyRotationStatusResponse nativeValue
  ) {
    Option<Boolean> keyRotationEnabled;
    keyRotationEnabled =
      Objects.nonNull(nativeValue.keyRotationEnabled())
        ? Option.create_Some((nativeValue.keyRotationEnabled()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<Integer> rotationPeriodInDays;
    rotationPeriodInDays =
      Objects.nonNull(nativeValue.rotationPeriodInDays())
        ? Option.create_Some((nativeValue.rotationPeriodInDays()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextRotationDate;
    nextRotationDate =
      Objects.nonNull(nativeValue.nextRotationDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextRotationDate()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> onDemandRotationStartDate;
    onDemandRotationStartDate =
      Objects.nonNull(nativeValue.onDemandRotationStartDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.onDemandRotationStartDate()
          )
        )
        : Option.create_None();
    return new GetKeyRotationStatusResponse(
      keyRotationEnabled,
      keyId,
      rotationPeriodInDays,
      nextRotationDate,
      onDemandRotationStartDate
    );
  }

  public static GetParametersForImportRequest GetParametersForImportRequest(
    software.amazon.awssdk.services.kms.model.GetParametersForImportRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    AlgorithmSpec wrappingAlgorithm;
    wrappingAlgorithm = ToDafny.AlgorithmSpec(nativeValue.wrappingAlgorithm());
    WrappingKeySpec wrappingKeySpec;
    wrappingKeySpec = ToDafny.WrappingKeySpec(nativeValue.wrappingKeySpec());
    return new GetParametersForImportRequest(
      keyId,
      wrappingAlgorithm,
      wrappingKeySpec
    );
  }

  public static GetParametersForImportResponse GetParametersForImportResponse(
    software.amazon.awssdk.services.kms.model.GetParametersForImportResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> importToken;
    importToken =
      Objects.nonNull(nativeValue.importToken())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.importToken().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> publicKey;
    publicKey =
      Objects.nonNull(nativeValue.publicKey())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.publicKey().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> parametersValidTo;
    parametersValidTo =
      Objects.nonNull(nativeValue.parametersValidTo())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.parametersValidTo()
          )
        )
        : Option.create_None();
    return new GetParametersForImportResponse(
      keyId,
      importToken,
      publicKey,
      parametersValidTo
    );
  }

  public static GetPublicKeyRequest GetPublicKeyRequest(
    software.amazon.awssdk.services.kms.model.GetPublicKeyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    return new GetPublicKeyRequest(keyId, grantTokens);
  }

  public static GetPublicKeyResponse GetPublicKeyResponse(
    software.amazon.awssdk.services.kms.model.GetPublicKeyResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> publicKey;
    publicKey =
      Objects.nonNull(nativeValue.publicKey())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.publicKey().asByteArray()
          )
        )
        : Option.create_None();
    Option<CustomerMasterKeySpec> customerMasterKeySpec;
    customerMasterKeySpec =
      Objects.nonNull(nativeValue.customerMasterKeySpec())
        ? Option.create_Some(
          ToDafny.CustomerMasterKeySpec(nativeValue.customerMasterKeySpec())
        )
        : Option.create_None();
    Option<KeySpec> keySpec;
    keySpec =
      Objects.nonNull(nativeValue.keySpec())
        ? Option.create_Some(ToDafny.KeySpec(nativeValue.keySpec()))
        : Option.create_None();
    Option<KeyUsageType> keyUsage;
    keyUsage =
      Objects.nonNull(nativeValue.keyUsage())
        ? Option.create_Some(ToDafny.KeyUsageType(nativeValue.keyUsage()))
        : Option.create_None();
    Option<
      DafnySequence<? extends EncryptionAlgorithmSpec>
    > encryptionAlgorithms;
    encryptionAlgorithms =
      (Objects.nonNull(nativeValue.encryptionAlgorithms()) &&
          nativeValue.encryptionAlgorithms().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpecList(
            nativeValue.encryptionAlgorithms()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends SigningAlgorithmSpec>> signingAlgorithms;
    signingAlgorithms =
      (Objects.nonNull(nativeValue.signingAlgorithms()) &&
          nativeValue.signingAlgorithms().size() > 0)
        ? Option.create_Some(
          ToDafny.SigningAlgorithmSpecList(nativeValue.signingAlgorithms())
        )
        : Option.create_None();
    Option<
      DafnySequence<? extends KeyAgreementAlgorithmSpec>
    > keyAgreementAlgorithms;
    keyAgreementAlgorithms =
      (Objects.nonNull(nativeValue.keyAgreementAlgorithms()) &&
          nativeValue.keyAgreementAlgorithms().size() > 0)
        ? Option.create_Some(
          ToDafny.KeyAgreementAlgorithmSpecList(
            nativeValue.keyAgreementAlgorithms()
          )
        )
        : Option.create_None();
    return new GetPublicKeyResponse(
      keyId,
      publicKey,
      customerMasterKeySpec,
      keySpec,
      keyUsage,
      encryptionAlgorithms,
      signingAlgorithms,
      keyAgreementAlgorithms
    );
  }

  public static GrantConstraints GrantConstraints(
    software.amazon.awssdk.services.kms.model.GrantConstraints nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContextSubset;
    encryptionContextSubset =
      (Objects.nonNull(nativeValue.encryptionContextSubset()) &&
          nativeValue.encryptionContextSubset().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContextSubset())
        )
        : Option.create_None();
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > encryptionContextEquals;
    encryptionContextEquals =
      (Objects.nonNull(nativeValue.encryptionContextEquals()) &&
          nativeValue.encryptionContextEquals().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.encryptionContextEquals())
        )
        : Option.create_None();
    return new GrantConstraints(
      encryptionContextSubset,
      encryptionContextEquals
    );
  }

  public static DafnySequence<? extends GrantListEntry> GrantList(
    List<software.amazon.awssdk.services.kms.model.GrantListEntry> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::GrantListEntry,
      GrantListEntry._typeDescriptor()
    );
  }

  public static GrantListEntry GrantListEntry(
    software.amazon.awssdk.services.kms.model.GrantListEntry nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> grantId;
    grantId =
      Objects.nonNull(nativeValue.grantId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.grantId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> name;
    name =
      Objects.nonNull(nativeValue.name())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.name()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> creationDate;
    creationDate =
      Objects.nonNull(nativeValue.creationDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.creationDate()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> granteePrincipal;
    granteePrincipal =
      Objects.nonNull(nativeValue.granteePrincipal())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.granteePrincipal()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> retiringPrincipal;
    retiringPrincipal =
      Objects.nonNull(nativeValue.retiringPrincipal())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.retiringPrincipal()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> issuingAccount;
    issuingAccount =
      Objects.nonNull(nativeValue.issuingAccount())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.issuingAccount()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends GrantOperation>> operations;
    operations =
      (Objects.nonNull(nativeValue.operations()) &&
          nativeValue.operations().size() > 0)
        ? Option.create_Some(
          ToDafny.GrantOperationList(nativeValue.operations())
        )
        : Option.create_None();
    Option<GrantConstraints> constraints;
    constraints =
      Objects.nonNull(nativeValue.constraints())
        ? Option.create_Some(
          ToDafny.GrantConstraints(nativeValue.constraints())
        )
        : Option.create_None();
    return new GrantListEntry(
      keyId,
      grantId,
      name,
      creationDate,
      granteePrincipal,
      retiringPrincipal,
      issuingAccount,
      operations,
      constraints
    );
  }

  public static DafnySequence<? extends GrantOperation> GrantOperationList(
    List<software.amazon.awssdk.services.kms.model.GrantOperation> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::GrantOperation,
      GrantOperation._typeDescriptor()
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > GrantTokenList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static ImportKeyMaterialRequest ImportKeyMaterialRequest(
    software.amazon.awssdk.services.kms.model.ImportKeyMaterialRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Byte> importToken;
    importToken =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.importToken().asByteArray()
      );
    DafnySequence<? extends Byte> encryptedKeyMaterial;
    encryptedKeyMaterial =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.encryptedKeyMaterial().asByteArray()
      );
    Option<DafnySequence<? extends Character>> validTo;
    validTo =
      Objects.nonNull(nativeValue.validTo())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.validTo()
          )
        )
        : Option.create_None();
    Option<ExpirationModelType> expirationModel;
    expirationModel =
      Objects.nonNull(nativeValue.expirationModel())
        ? Option.create_Some(
          ToDafny.ExpirationModelType(nativeValue.expirationModel())
        )
        : Option.create_None();
    return new ImportKeyMaterialRequest(
      keyId,
      importToken,
      encryptedKeyMaterial,
      validTo,
      expirationModel
    );
  }

  public static ImportKeyMaterialResponse ImportKeyMaterialResponse(
    software.amazon.awssdk.services.kms.model.ImportKeyMaterialResponse nativeValue
  ) {
    return new ImportKeyMaterialResponse();
  }

  public static DafnySequence<
    ? extends KeyAgreementAlgorithmSpec
  > KeyAgreementAlgorithmSpecList(
    List<
      software.amazon.awssdk.services.kms.model.KeyAgreementAlgorithmSpec
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::KeyAgreementAlgorithmSpec,
      KeyAgreementAlgorithmSpec._typeDescriptor()
    );
  }

  public static DafnySequence<? extends KeyListEntry> KeyList(
    List<software.amazon.awssdk.services.kms.model.KeyListEntry> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::KeyListEntry,
      KeyListEntry._typeDescriptor()
    );
  }

  public static KeyListEntry KeyListEntry(
    software.amazon.awssdk.services.kms.model.KeyListEntry nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyArn;
    keyArn =
      Objects.nonNull(nativeValue.keyArn())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyArn()
          )
        )
        : Option.create_None();
    return new KeyListEntry(keyId, keyArn);
  }

  public static KeyMetadata KeyMetadata(
    software.amazon.awssdk.services.kms.model.KeyMetadata nativeValue
  ) {
    Option<DafnySequence<? extends Character>> aWSAccountId;
    aWSAccountId =
      Objects.nonNull(nativeValue.awsAccountId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.awsAccountId()
          )
        )
        : Option.create_None();
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<DafnySequence<? extends Character>> arn;
    arn =
      Objects.nonNull(nativeValue.arn())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.arn()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> creationDate;
    creationDate =
      Objects.nonNull(nativeValue.creationDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.creationDate()
          )
        )
        : Option.create_None();
    Option<Boolean> enabled;
    enabled =
      Objects.nonNull(nativeValue.enabled())
        ? Option.create_Some((nativeValue.enabled()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> description;
    description =
      Objects.nonNull(nativeValue.description())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.description()
          )
        )
        : Option.create_None();
    Option<KeyUsageType> keyUsage;
    keyUsage =
      Objects.nonNull(nativeValue.keyUsage())
        ? Option.create_Some(ToDafny.KeyUsageType(nativeValue.keyUsage()))
        : Option.create_None();
    Option<KeyState> keyState;
    keyState =
      Objects.nonNull(nativeValue.keyState())
        ? Option.create_Some(ToDafny.KeyState(nativeValue.keyState()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> deletionDate;
    deletionDate =
      Objects.nonNull(nativeValue.deletionDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.deletionDate()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> validTo;
    validTo =
      Objects.nonNull(nativeValue.validTo())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.validTo()
          )
        )
        : Option.create_None();
    Option<OriginType> origin;
    origin =
      Objects.nonNull(nativeValue.origin())
        ? Option.create_Some(ToDafny.OriginType(nativeValue.origin()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> customKeyStoreId;
    customKeyStoreId =
      Objects.nonNull(nativeValue.customKeyStoreId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.customKeyStoreId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> cloudHsmClusterId;
    cloudHsmClusterId =
      Objects.nonNull(nativeValue.cloudHsmClusterId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.cloudHsmClusterId()
          )
        )
        : Option.create_None();
    Option<ExpirationModelType> expirationModel;
    expirationModel =
      Objects.nonNull(nativeValue.expirationModel())
        ? Option.create_Some(
          ToDafny.ExpirationModelType(nativeValue.expirationModel())
        )
        : Option.create_None();
    Option<KeyManagerType> keyManager;
    keyManager =
      Objects.nonNull(nativeValue.keyManager())
        ? Option.create_Some(ToDafny.KeyManagerType(nativeValue.keyManager()))
        : Option.create_None();
    Option<CustomerMasterKeySpec> customerMasterKeySpec;
    customerMasterKeySpec =
      Objects.nonNull(nativeValue.customerMasterKeySpec())
        ? Option.create_Some(
          ToDafny.CustomerMasterKeySpec(nativeValue.customerMasterKeySpec())
        )
        : Option.create_None();
    Option<KeySpec> keySpec;
    keySpec =
      Objects.nonNull(nativeValue.keySpec())
        ? Option.create_Some(ToDafny.KeySpec(nativeValue.keySpec()))
        : Option.create_None();
    Option<
      DafnySequence<? extends EncryptionAlgorithmSpec>
    > encryptionAlgorithms;
    encryptionAlgorithms =
      (Objects.nonNull(nativeValue.encryptionAlgorithms()) &&
          nativeValue.encryptionAlgorithms().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpecList(
            nativeValue.encryptionAlgorithms()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends SigningAlgorithmSpec>> signingAlgorithms;
    signingAlgorithms =
      (Objects.nonNull(nativeValue.signingAlgorithms()) &&
          nativeValue.signingAlgorithms().size() > 0)
        ? Option.create_Some(
          ToDafny.SigningAlgorithmSpecList(nativeValue.signingAlgorithms())
        )
        : Option.create_None();
    Option<
      DafnySequence<? extends KeyAgreementAlgorithmSpec>
    > keyAgreementAlgorithms;
    keyAgreementAlgorithms =
      (Objects.nonNull(nativeValue.keyAgreementAlgorithms()) &&
          nativeValue.keyAgreementAlgorithms().size() > 0)
        ? Option.create_Some(
          ToDafny.KeyAgreementAlgorithmSpecList(
            nativeValue.keyAgreementAlgorithms()
          )
        )
        : Option.create_None();
    Option<Boolean> multiRegion;
    multiRegion =
      Objects.nonNull(nativeValue.multiRegion())
        ? Option.create_Some((nativeValue.multiRegion()))
        : Option.create_None();
    Option<MultiRegionConfiguration> multiRegionConfiguration;
    multiRegionConfiguration =
      Objects.nonNull(nativeValue.multiRegionConfiguration())
        ? Option.create_Some(
          ToDafny.MultiRegionConfiguration(
            nativeValue.multiRegionConfiguration()
          )
        )
        : Option.create_None();
    Option<Integer> pendingDeletionWindowInDays;
    pendingDeletionWindowInDays =
      Objects.nonNull(nativeValue.pendingDeletionWindowInDays())
        ? Option.create_Some((nativeValue.pendingDeletionWindowInDays()))
        : Option.create_None();
    Option<DafnySequence<? extends MacAlgorithmSpec>> macAlgorithms;
    macAlgorithms =
      (Objects.nonNull(nativeValue.macAlgorithms()) &&
          nativeValue.macAlgorithms().size() > 0)
        ? Option.create_Some(
          ToDafny.MacAlgorithmSpecList(nativeValue.macAlgorithms())
        )
        : Option.create_None();
    Option<XksKeyConfigurationType> xksKeyConfiguration;
    xksKeyConfiguration =
      Objects.nonNull(nativeValue.xksKeyConfiguration())
        ? Option.create_Some(
          ToDafny.XksKeyConfigurationType(nativeValue.xksKeyConfiguration())
        )
        : Option.create_None();
    return new KeyMetadata(
      aWSAccountId,
      keyId,
      arn,
      creationDate,
      enabled,
      description,
      keyUsage,
      keyState,
      deletionDate,
      validTo,
      origin,
      customKeyStoreId,
      cloudHsmClusterId,
      expirationModel,
      keyManager,
      customerMasterKeySpec,
      keySpec,
      encryptionAlgorithms,
      signingAlgorithms,
      keyAgreementAlgorithms,
      multiRegion,
      multiRegionConfiguration,
      pendingDeletionWindowInDays,
      macAlgorithms,
      xksKeyConfiguration
    );
  }

  public static ListAliasesRequest ListAliasesRequest(
    software.amazon.awssdk.services.kms.model.ListAliasesRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some((nativeValue.limit()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> marker;
    marker =
      Objects.nonNull(nativeValue.marker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.marker()
          )
        )
        : Option.create_None();
    return new ListAliasesRequest(keyId, limit, marker);
  }

  public static ListAliasesResponse ListAliasesResponse(
    software.amazon.awssdk.services.kms.model.ListAliasesResponse nativeValue
  ) {
    Option<DafnySequence<? extends AliasListEntry>> aliases;
    aliases =
      (Objects.nonNull(nativeValue.aliases()) &&
          nativeValue.aliases().size() > 0)
        ? Option.create_Some(ToDafny.AliasList(nativeValue.aliases()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextMarker;
    nextMarker =
      Objects.nonNull(nativeValue.nextMarker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextMarker()
          )
        )
        : Option.create_None();
    Option<Boolean> truncated;
    truncated =
      Objects.nonNull(nativeValue.truncated())
        ? Option.create_Some((nativeValue.truncated()))
        : Option.create_None();
    return new ListAliasesResponse(aliases, nextMarker, truncated);
  }

  public static ListGrantsRequest ListGrantsRequest(
    software.amazon.awssdk.services.kms.model.ListGrantsRequest nativeValue
  ) {
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some((nativeValue.limit()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> marker;
    marker =
      Objects.nonNull(nativeValue.marker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.marker()
          )
        )
        : Option.create_None();
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<DafnySequence<? extends Character>> grantId;
    grantId =
      Objects.nonNull(nativeValue.grantId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.grantId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> granteePrincipal;
    granteePrincipal =
      Objects.nonNull(nativeValue.granteePrincipal())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.granteePrincipal()
          )
        )
        : Option.create_None();
    return new ListGrantsRequest(
      limit,
      marker,
      keyId,
      grantId,
      granteePrincipal
    );
  }

  public static ListGrantsResponse ListGrantsResponse(
    software.amazon.awssdk.services.kms.model.ListGrantsResponse nativeValue
  ) {
    Option<DafnySequence<? extends GrantListEntry>> grants;
    grants =
      (Objects.nonNull(nativeValue.grants()) && nativeValue.grants().size() > 0)
        ? Option.create_Some(ToDafny.GrantList(nativeValue.grants()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextMarker;
    nextMarker =
      Objects.nonNull(nativeValue.nextMarker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextMarker()
          )
        )
        : Option.create_None();
    Option<Boolean> truncated;
    truncated =
      Objects.nonNull(nativeValue.truncated())
        ? Option.create_Some((nativeValue.truncated()))
        : Option.create_None();
    return new ListGrantsResponse(grants, nextMarker, truncated);
  }

  public static ListKeyPoliciesRequest ListKeyPoliciesRequest(
    software.amazon.awssdk.services.kms.model.ListKeyPoliciesRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some((nativeValue.limit()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> marker;
    marker =
      Objects.nonNull(nativeValue.marker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.marker()
          )
        )
        : Option.create_None();
    return new ListKeyPoliciesRequest(keyId, limit, marker);
  }

  public static ListKeyPoliciesResponse ListKeyPoliciesResponse(
    software.amazon.awssdk.services.kms.model.ListKeyPoliciesResponse nativeValue
  ) {
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > policyNames;
    policyNames =
      (Objects.nonNull(nativeValue.policyNames()) &&
          nativeValue.policyNames().size() > 0)
        ? Option.create_Some(ToDafny.PolicyNameList(nativeValue.policyNames()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextMarker;
    nextMarker =
      Objects.nonNull(nativeValue.nextMarker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextMarker()
          )
        )
        : Option.create_None();
    Option<Boolean> truncated;
    truncated =
      Objects.nonNull(nativeValue.truncated())
        ? Option.create_Some((nativeValue.truncated()))
        : Option.create_None();
    return new ListKeyPoliciesResponse(policyNames, nextMarker, truncated);
  }

  public static ListKeyRotationsRequest ListKeyRotationsRequest(
    software.amazon.awssdk.services.kms.model.ListKeyRotationsRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some((nativeValue.limit()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> marker;
    marker =
      Objects.nonNull(nativeValue.marker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.marker()
          )
        )
        : Option.create_None();
    return new ListKeyRotationsRequest(keyId, limit, marker);
  }

  public static ListKeyRotationsResponse ListKeyRotationsResponse(
    software.amazon.awssdk.services.kms.model.ListKeyRotationsResponse nativeValue
  ) {
    Option<DafnySequence<? extends RotationsListEntry>> rotations;
    rotations =
      (Objects.nonNull(nativeValue.rotations()) &&
          nativeValue.rotations().size() > 0)
        ? Option.create_Some(ToDafny.RotationsList(nativeValue.rotations()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextMarker;
    nextMarker =
      Objects.nonNull(nativeValue.nextMarker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextMarker()
          )
        )
        : Option.create_None();
    Option<Boolean> truncated;
    truncated =
      Objects.nonNull(nativeValue.truncated())
        ? Option.create_Some((nativeValue.truncated()))
        : Option.create_None();
    return new ListKeyRotationsResponse(rotations, nextMarker, truncated);
  }

  public static ListKeysRequest ListKeysRequest(
    software.amazon.awssdk.services.kms.model.ListKeysRequest nativeValue
  ) {
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some((nativeValue.limit()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> marker;
    marker =
      Objects.nonNull(nativeValue.marker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.marker()
          )
        )
        : Option.create_None();
    return new ListKeysRequest(limit, marker);
  }

  public static ListKeysResponse ListKeysResponse(
    software.amazon.awssdk.services.kms.model.ListKeysResponse nativeValue
  ) {
    Option<DafnySequence<? extends KeyListEntry>> keys;
    keys =
      (Objects.nonNull(nativeValue.keys()) && nativeValue.keys().size() > 0)
        ? Option.create_Some(ToDafny.KeyList(nativeValue.keys()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextMarker;
    nextMarker =
      Objects.nonNull(nativeValue.nextMarker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextMarker()
          )
        )
        : Option.create_None();
    Option<Boolean> truncated;
    truncated =
      Objects.nonNull(nativeValue.truncated())
        ? Option.create_Some((nativeValue.truncated()))
        : Option.create_None();
    return new ListKeysResponse(keys, nextMarker, truncated);
  }

  public static ListResourceTagsRequest ListResourceTagsRequest(
    software.amazon.awssdk.services.kms.model.ListResourceTagsRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some((nativeValue.limit()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> marker;
    marker =
      Objects.nonNull(nativeValue.marker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.marker()
          )
        )
        : Option.create_None();
    return new ListResourceTagsRequest(keyId, limit, marker);
  }

  public static ListResourceTagsResponse ListResourceTagsResponse(
    software.amazon.awssdk.services.kms.model.ListResourceTagsResponse nativeValue
  ) {
    Option<DafnySequence<? extends Tag>> tags;
    tags =
      (Objects.nonNull(nativeValue.tags()) && nativeValue.tags().size() > 0)
        ? Option.create_Some(ToDafny.TagList(nativeValue.tags()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> nextMarker;
    nextMarker =
      Objects.nonNull(nativeValue.nextMarker())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextMarker()
          )
        )
        : Option.create_None();
    Option<Boolean> truncated;
    truncated =
      Objects.nonNull(nativeValue.truncated())
        ? Option.create_Some((nativeValue.truncated()))
        : Option.create_None();
    return new ListResourceTagsResponse(tags, nextMarker, truncated);
  }

  public static DafnySequence<? extends MacAlgorithmSpec> MacAlgorithmSpecList(
    List<software.amazon.awssdk.services.kms.model.MacAlgorithmSpec> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::MacAlgorithmSpec,
      MacAlgorithmSpec._typeDescriptor()
    );
  }

  public static MultiRegionConfiguration MultiRegionConfiguration(
    software.amazon.awssdk.services.kms.model.MultiRegionConfiguration nativeValue
  ) {
    Option<MultiRegionKeyType> multiRegionKeyType;
    multiRegionKeyType =
      Objects.nonNull(nativeValue.multiRegionKeyType())
        ? Option.create_Some(
          ToDafny.MultiRegionKeyType(nativeValue.multiRegionKeyType())
        )
        : Option.create_None();
    Option<MultiRegionKey> primaryKey;
    primaryKey =
      Objects.nonNull(nativeValue.primaryKey())
        ? Option.create_Some(ToDafny.MultiRegionKey(nativeValue.primaryKey()))
        : Option.create_None();
    Option<DafnySequence<? extends MultiRegionKey>> replicaKeys;
    replicaKeys =
      (Objects.nonNull(nativeValue.replicaKeys()) &&
          nativeValue.replicaKeys().size() > 0)
        ? Option.create_Some(
          ToDafny.MultiRegionKeyList(nativeValue.replicaKeys())
        )
        : Option.create_None();
    return new MultiRegionConfiguration(
      multiRegionKeyType,
      primaryKey,
      replicaKeys
    );
  }

  public static MultiRegionKey MultiRegionKey(
    software.amazon.awssdk.services.kms.model.MultiRegionKey nativeValue
  ) {
    Option<DafnySequence<? extends Character>> arn;
    arn =
      Objects.nonNull(nativeValue.arn())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.arn()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> region;
    region =
      Objects.nonNull(nativeValue.region())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.region()
          )
        )
        : Option.create_None();
    return new MultiRegionKey(arn, region);
  }

  public static DafnySequence<? extends MultiRegionKey> MultiRegionKeyList(
    List<software.amazon.awssdk.services.kms.model.MultiRegionKey> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::MultiRegionKey,
      MultiRegionKey._typeDescriptor()
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > PolicyNameList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static PutKeyPolicyRequest PutKeyPolicyRequest(
    software.amazon.awssdk.services.kms.model.PutKeyPolicyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<DafnySequence<? extends Character>> policyName;
    policyName =
      Objects.nonNull(nativeValue.policyName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policyName()
          )
        )
        : Option.create_None();
    DafnySequence<? extends Character> policy;
    policy =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.policy()
      );
    Option<Boolean> bypassPolicyLockoutSafetyCheck;
    bypassPolicyLockoutSafetyCheck =
      Objects.nonNull(nativeValue.bypassPolicyLockoutSafetyCheck())
        ? Option.create_Some((nativeValue.bypassPolicyLockoutSafetyCheck()))
        : Option.create_None();
    return new PutKeyPolicyRequest(
      keyId,
      policyName,
      policy,
      bypassPolicyLockoutSafetyCheck
    );
  }

  public static RecipientInfo RecipientInfo(
    software.amazon.awssdk.services.kms.model.RecipientInfo nativeValue
  ) {
    Option<KeyEncryptionMechanism> keyEncryptionAlgorithm;
    keyEncryptionAlgorithm =
      Objects.nonNull(nativeValue.keyEncryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.KeyEncryptionMechanism(nativeValue.keyEncryptionAlgorithm())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> attestationDocument;
    attestationDocument =
      Objects.nonNull(nativeValue.attestationDocument())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.attestationDocument().asByteArray()
          )
        )
        : Option.create_None();
    return new RecipientInfo(keyEncryptionAlgorithm, attestationDocument);
  }

  public static ReEncryptRequest ReEncryptRequest(
    software.amazon.awssdk.services.kms.model.ReEncryptRequest nativeValue
  ) {
    DafnySequence<? extends Byte> ciphertextBlob;
    ciphertextBlob =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.ciphertextBlob().asByteArray()
      );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > sourceEncryptionContext;
    sourceEncryptionContext =
      (Objects.nonNull(nativeValue.sourceEncryptionContext()) &&
          nativeValue.sourceEncryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(nativeValue.sourceEncryptionContext())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> sourceKeyId;
    sourceKeyId =
      Objects.nonNull(nativeValue.sourceKeyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.sourceKeyId()
          )
        )
        : Option.create_None();
    DafnySequence<? extends Character> destinationKeyId;
    destinationKeyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.destinationKeyId()
      );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > destinationEncryptionContext;
    destinationEncryptionContext =
      (Objects.nonNull(nativeValue.destinationEncryptionContext()) &&
          nativeValue.destinationEncryptionContext().size() > 0)
        ? Option.create_Some(
          ToDafny.EncryptionContextType(
            nativeValue.destinationEncryptionContext()
          )
        )
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> sourceEncryptionAlgorithm;
    sourceEncryptionAlgorithm =
      Objects.nonNull(nativeValue.sourceEncryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(
            nativeValue.sourceEncryptionAlgorithm()
          )
        )
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> destinationEncryptionAlgorithm;
    destinationEncryptionAlgorithm =
      Objects.nonNull(nativeValue.destinationEncryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(
            nativeValue.destinationEncryptionAlgorithm()
          )
        )
        : Option.create_None();
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new ReEncryptRequest(
      ciphertextBlob,
      sourceEncryptionContext,
      sourceKeyId,
      destinationKeyId,
      destinationEncryptionContext,
      sourceEncryptionAlgorithm,
      destinationEncryptionAlgorithm,
      grantTokens,
      dryRun
    );
  }

  public static ReEncryptResponse ReEncryptResponse(
    software.amazon.awssdk.services.kms.model.ReEncryptResponse nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> ciphertextBlob;
    ciphertextBlob =
      Objects.nonNull(nativeValue.ciphertextBlob())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ciphertextBlob().asByteArray()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> sourceKeyId;
    sourceKeyId =
      Objects.nonNull(nativeValue.sourceKeyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.sourceKeyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> sourceEncryptionAlgorithm;
    sourceEncryptionAlgorithm =
      Objects.nonNull(nativeValue.sourceEncryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(
            nativeValue.sourceEncryptionAlgorithm()
          )
        )
        : Option.create_None();
    Option<EncryptionAlgorithmSpec> destinationEncryptionAlgorithm;
    destinationEncryptionAlgorithm =
      Objects.nonNull(nativeValue.destinationEncryptionAlgorithm())
        ? Option.create_Some(
          ToDafny.EncryptionAlgorithmSpec(
            nativeValue.destinationEncryptionAlgorithm()
          )
        )
        : Option.create_None();
    return new ReEncryptResponse(
      ciphertextBlob,
      sourceKeyId,
      keyId,
      sourceEncryptionAlgorithm,
      destinationEncryptionAlgorithm
    );
  }

  public static ReplicateKeyRequest ReplicateKeyRequest(
    software.amazon.awssdk.services.kms.model.ReplicateKeyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Character> replicaRegion;
    replicaRegion =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.replicaRegion()
      );
    Option<DafnySequence<? extends Character>> policy;
    policy =
      Objects.nonNull(nativeValue.policy())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policy()
          )
        )
        : Option.create_None();
    Option<Boolean> bypassPolicyLockoutSafetyCheck;
    bypassPolicyLockoutSafetyCheck =
      Objects.nonNull(nativeValue.bypassPolicyLockoutSafetyCheck())
        ? Option.create_Some((nativeValue.bypassPolicyLockoutSafetyCheck()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> description;
    description =
      Objects.nonNull(nativeValue.description())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.description()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Tag>> tags;
    tags =
      (Objects.nonNull(nativeValue.tags()) && nativeValue.tags().size() > 0)
        ? Option.create_Some(ToDafny.TagList(nativeValue.tags()))
        : Option.create_None();
    return new ReplicateKeyRequest(
      keyId,
      replicaRegion,
      policy,
      bypassPolicyLockoutSafetyCheck,
      description,
      tags
    );
  }

  public static ReplicateKeyResponse ReplicateKeyResponse(
    software.amazon.awssdk.services.kms.model.ReplicateKeyResponse nativeValue
  ) {
    Option<KeyMetadata> replicaKeyMetadata;
    replicaKeyMetadata =
      Objects.nonNull(nativeValue.replicaKeyMetadata())
        ? Option.create_Some(
          ToDafny.KeyMetadata(nativeValue.replicaKeyMetadata())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> replicaPolicy;
    replicaPolicy =
      Objects.nonNull(nativeValue.replicaPolicy())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.replicaPolicy()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Tag>> replicaTags;
    replicaTags =
      (Objects.nonNull(nativeValue.replicaTags()) &&
          nativeValue.replicaTags().size() > 0)
        ? Option.create_Some(ToDafny.TagList(nativeValue.replicaTags()))
        : Option.create_None();
    return new ReplicateKeyResponse(
      replicaKeyMetadata,
      replicaPolicy,
      replicaTags
    );
  }

  public static RetireGrantRequest RetireGrantRequest(
    software.amazon.awssdk.services.kms.model.RetireGrantRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> grantToken;
    grantToken =
      Objects.nonNull(nativeValue.grantToken())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.grantToken()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> grantId;
    grantId =
      Objects.nonNull(nativeValue.grantId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.grantId()
          )
        )
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new RetireGrantRequest(grantToken, keyId, grantId, dryRun);
  }

  public static RevokeGrantRequest RevokeGrantRequest(
    software.amazon.awssdk.services.kms.model.RevokeGrantRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Character> grantId;
    grantId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.grantId()
      );
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new RevokeGrantRequest(keyId, grantId, dryRun);
  }

  public static RotateKeyOnDemandRequest RotateKeyOnDemandRequest(
    software.amazon.awssdk.services.kms.model.RotateKeyOnDemandRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    return new RotateKeyOnDemandRequest(keyId);
  }

  public static RotateKeyOnDemandResponse RotateKeyOnDemandResponse(
    software.amazon.awssdk.services.kms.model.RotateKeyOnDemandResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    return new RotateKeyOnDemandResponse(keyId);
  }

  public static DafnySequence<? extends RotationsListEntry> RotationsList(
    List<
      software.amazon.awssdk.services.kms.model.RotationsListEntry
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::RotationsListEntry,
      RotationsListEntry._typeDescriptor()
    );
  }

  public static RotationsListEntry RotationsListEntry(
    software.amazon.awssdk.services.kms.model.RotationsListEntry nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> rotationDate;
    rotationDate =
      Objects.nonNull(nativeValue.rotationDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.rotationDate()
          )
        )
        : Option.create_None();
    Option<RotationType> rotationType;
    rotationType =
      Objects.nonNull(nativeValue.rotationType())
        ? Option.create_Some(ToDafny.RotationType(nativeValue.rotationType()))
        : Option.create_None();
    return new RotationsListEntry(keyId, rotationDate, rotationType);
  }

  public static ScheduleKeyDeletionRequest ScheduleKeyDeletionRequest(
    software.amazon.awssdk.services.kms.model.ScheduleKeyDeletionRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    Option<Integer> pendingWindowInDays;
    pendingWindowInDays =
      Objects.nonNull(nativeValue.pendingWindowInDays())
        ? Option.create_Some((nativeValue.pendingWindowInDays()))
        : Option.create_None();
    return new ScheduleKeyDeletionRequest(keyId, pendingWindowInDays);
  }

  public static ScheduleKeyDeletionResponse ScheduleKeyDeletionResponse(
    software.amazon.awssdk.services.kms.model.ScheduleKeyDeletionResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> deletionDate;
    deletionDate =
      Objects.nonNull(nativeValue.deletionDate())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.deletionDate()
          )
        )
        : Option.create_None();
    Option<KeyState> keyState;
    keyState =
      Objects.nonNull(nativeValue.keyState())
        ? Option.create_Some(ToDafny.KeyState(nativeValue.keyState()))
        : Option.create_None();
    Option<Integer> pendingWindowInDays;
    pendingWindowInDays =
      Objects.nonNull(nativeValue.pendingWindowInDays())
        ? Option.create_Some((nativeValue.pendingWindowInDays()))
        : Option.create_None();
    return new ScheduleKeyDeletionResponse(
      keyId,
      deletionDate,
      keyState,
      pendingWindowInDays
    );
  }

  public static DafnySequence<
    ? extends SigningAlgorithmSpec
  > SigningAlgorithmSpecList(
    List<
      software.amazon.awssdk.services.kms.model.SigningAlgorithmSpec
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::SigningAlgorithmSpec,
      SigningAlgorithmSpec._typeDescriptor()
    );
  }

  public static SignRequest SignRequest(
    software.amazon.awssdk.services.kms.model.SignRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Byte> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.message().asByteArray()
      );
    Option<MessageType> messageType;
    messageType =
      Objects.nonNull(nativeValue.messageType())
        ? Option.create_Some(ToDafny.MessageType(nativeValue.messageType()))
        : Option.create_None();
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    SigningAlgorithmSpec signingAlgorithm;
    signingAlgorithm =
      ToDafny.SigningAlgorithmSpec(nativeValue.signingAlgorithm());
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new SignRequest(
      keyId,
      message,
      messageType,
      grantTokens,
      signingAlgorithm,
      dryRun
    );
  }

  public static SignResponse SignResponse(
    software.amazon.awssdk.services.kms.model.SignResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Byte>> signature;
    signature =
      Objects.nonNull(nativeValue.signature())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.signature().asByteArray()
          )
        )
        : Option.create_None();
    Option<SigningAlgorithmSpec> signingAlgorithm;
    signingAlgorithm =
      Objects.nonNull(nativeValue.signingAlgorithm())
        ? Option.create_Some(
          ToDafny.SigningAlgorithmSpec(nativeValue.signingAlgorithm())
        )
        : Option.create_None();
    return new SignResponse(keyId, signature, signingAlgorithm);
  }

  public static Tag Tag(
    software.amazon.awssdk.services.kms.model.Tag nativeValue
  ) {
    DafnySequence<? extends Character> tagKey;
    tagKey =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tagKey()
      );
    DafnySequence<? extends Character> tagValue;
    tagValue =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tagValue()
      );
    return new Tag(tagKey, tagValue);
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > TagKeyList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static DafnySequence<? extends Tag> TagList(
    List<software.amazon.awssdk.services.kms.model.Tag> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.kms.internaldafny.ToDafny::Tag,
      Tag._typeDescriptor()
    );
  }

  public static TagResourceRequest TagResourceRequest(
    software.amazon.awssdk.services.kms.model.TagResourceRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Tag> tags;
    tags = ToDafny.TagList(nativeValue.tags());
    return new TagResourceRequest(keyId, tags);
  }

  public static UntagResourceRequest UntagResourceRequest(
    software.amazon.awssdk.services.kms.model.UntagResourceRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends DafnySequence<? extends Character>> tagKeys;
    tagKeys = ToDafny.TagKeyList(nativeValue.tagKeys());
    return new UntagResourceRequest(keyId, tagKeys);
  }

  public static UpdateAliasRequest UpdateAliasRequest(
    software.amazon.awssdk.services.kms.model.UpdateAliasRequest nativeValue
  ) {
    DafnySequence<? extends Character> aliasName;
    aliasName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.aliasName()
      );
    DafnySequence<? extends Character> targetKeyId;
    targetKeyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.targetKeyId()
      );
    return new UpdateAliasRequest(aliasName, targetKeyId);
  }

  public static UpdateCustomKeyStoreRequest UpdateCustomKeyStoreRequest(
    software.amazon.awssdk.services.kms.model.UpdateCustomKeyStoreRequest nativeValue
  ) {
    DafnySequence<? extends Character> customKeyStoreId;
    customKeyStoreId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.customKeyStoreId()
      );
    Option<DafnySequence<? extends Character>> newCustomKeyStoreName;
    newCustomKeyStoreName =
      Objects.nonNull(nativeValue.newCustomKeyStoreName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.newCustomKeyStoreName()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> keyStorePassword;
    keyStorePassword =
      Objects.nonNull(nativeValue.keyStorePassword())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyStorePassword()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> cloudHsmClusterId;
    cloudHsmClusterId =
      Objects.nonNull(nativeValue.cloudHsmClusterId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.cloudHsmClusterId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> xksProxyUriEndpoint;
    xksProxyUriEndpoint =
      Objects.nonNull(nativeValue.xksProxyUriEndpoint())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.xksProxyUriEndpoint()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> xksProxyUriPath;
    xksProxyUriPath =
      Objects.nonNull(nativeValue.xksProxyUriPath())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.xksProxyUriPath()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> xksProxyVpcEndpointServiceName;
    xksProxyVpcEndpointServiceName =
      Objects.nonNull(nativeValue.xksProxyVpcEndpointServiceName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.xksProxyVpcEndpointServiceName()
          )
        )
        : Option.create_None();
    Option<
      XksProxyAuthenticationCredentialType
    > xksProxyAuthenticationCredential;
    xksProxyAuthenticationCredential =
      Objects.nonNull(nativeValue.xksProxyAuthenticationCredential())
        ? Option.create_Some(
          ToDafny.XksProxyAuthenticationCredentialType(
            nativeValue.xksProxyAuthenticationCredential()
          )
        )
        : Option.create_None();
    Option<XksProxyConnectivityType> xksProxyConnectivity;
    xksProxyConnectivity =
      Objects.nonNull(nativeValue.xksProxyConnectivity())
        ? Option.create_Some(
          ToDafny.XksProxyConnectivityType(nativeValue.xksProxyConnectivity())
        )
        : Option.create_None();
    return new UpdateCustomKeyStoreRequest(
      customKeyStoreId,
      newCustomKeyStoreName,
      keyStorePassword,
      cloudHsmClusterId,
      xksProxyUriEndpoint,
      xksProxyUriPath,
      xksProxyVpcEndpointServiceName,
      xksProxyAuthenticationCredential,
      xksProxyConnectivity
    );
  }

  public static UpdateCustomKeyStoreResponse UpdateCustomKeyStoreResponse(
    software.amazon.awssdk.services.kms.model.UpdateCustomKeyStoreResponse nativeValue
  ) {
    return new UpdateCustomKeyStoreResponse();
  }

  public static UpdateKeyDescriptionRequest UpdateKeyDescriptionRequest(
    software.amazon.awssdk.services.kms.model.UpdateKeyDescriptionRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Character> description;
    description =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.description()
      );
    return new UpdateKeyDescriptionRequest(keyId, description);
  }

  public static UpdatePrimaryRegionRequest UpdatePrimaryRegionRequest(
    software.amazon.awssdk.services.kms.model.UpdatePrimaryRegionRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Character> primaryRegion;
    primaryRegion =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.primaryRegion()
      );
    return new UpdatePrimaryRegionRequest(keyId, primaryRegion);
  }

  public static VerifyMacRequest VerifyMacRequest(
    software.amazon.awssdk.services.kms.model.VerifyMacRequest nativeValue
  ) {
    DafnySequence<? extends Byte> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.message().asByteArray()
      );
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    MacAlgorithmSpec macAlgorithm;
    macAlgorithm = ToDafny.MacAlgorithmSpec(nativeValue.macAlgorithm());
    DafnySequence<? extends Byte> mac;
    mac =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.mac().asByteArray()
      );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new VerifyMacRequest(
      message,
      keyId,
      macAlgorithm,
      mac,
      grantTokens,
      dryRun
    );
  }

  public static VerifyMacResponse VerifyMacResponse(
    software.amazon.awssdk.services.kms.model.VerifyMacResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<Boolean> macValid;
    macValid =
      Objects.nonNull(nativeValue.macValid())
        ? Option.create_Some((nativeValue.macValid()))
        : Option.create_None();
    Option<MacAlgorithmSpec> macAlgorithm;
    macAlgorithm =
      Objects.nonNull(nativeValue.macAlgorithm())
        ? Option.create_Some(
          ToDafny.MacAlgorithmSpec(nativeValue.macAlgorithm())
        )
        : Option.create_None();
    return new VerifyMacResponse(keyId, macValid, macAlgorithm);
  }

  public static VerifyRequest VerifyRequest(
    software.amazon.awssdk.services.kms.model.VerifyRequest nativeValue
  ) {
    DafnySequence<? extends Character> keyId;
    keyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyId()
      );
    DafnySequence<? extends Byte> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.message().asByteArray()
      );
    Option<MessageType> messageType;
    messageType =
      Objects.nonNull(nativeValue.messageType())
        ? Option.create_Some(ToDafny.MessageType(nativeValue.messageType()))
        : Option.create_None();
    DafnySequence<? extends Byte> signature;
    signature =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.signature().asByteArray()
      );
    SigningAlgorithmSpec signingAlgorithm;
    signingAlgorithm =
      ToDafny.SigningAlgorithmSpec(nativeValue.signingAlgorithm());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<Boolean> dryRun;
    dryRun =
      Objects.nonNull(nativeValue.dryRun())
        ? Option.create_Some((nativeValue.dryRun()))
        : Option.create_None();
    return new VerifyRequest(
      keyId,
      message,
      messageType,
      signature,
      signingAlgorithm,
      grantTokens,
      dryRun
    );
  }

  public static VerifyResponse VerifyResponse(
    software.amazon.awssdk.services.kms.model.VerifyResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> keyId;
    keyId =
      Objects.nonNull(nativeValue.keyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyId()
          )
        )
        : Option.create_None();
    Option<Boolean> signatureValid;
    signatureValid =
      Objects.nonNull(nativeValue.signatureValid())
        ? Option.create_Some((nativeValue.signatureValid()))
        : Option.create_None();
    Option<SigningAlgorithmSpec> signingAlgorithm;
    signingAlgorithm =
      Objects.nonNull(nativeValue.signingAlgorithm())
        ? Option.create_Some(
          ToDafny.SigningAlgorithmSpec(nativeValue.signingAlgorithm())
        )
        : Option.create_None();
    return new VerifyResponse(keyId, signatureValid, signingAlgorithm);
  }

  public static XksKeyConfigurationType XksKeyConfigurationType(
    software.amazon.awssdk.services.kms.model.XksKeyConfigurationType nativeValue
  ) {
    Option<DafnySequence<? extends Character>> id;
    id =
      Objects.nonNull(nativeValue.id())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.id()
          )
        )
        : Option.create_None();
    return new XksKeyConfigurationType(id);
  }

  public static XksProxyAuthenticationCredentialType XksProxyAuthenticationCredentialType(
    software.amazon.awssdk.services.kms.model.XksProxyAuthenticationCredentialType nativeValue
  ) {
    DafnySequence<? extends Character> accessKeyId;
    accessKeyId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.accessKeyId()
      );
    DafnySequence<? extends Character> rawSecretAccessKey;
    rawSecretAccessKey =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.rawSecretAccessKey()
      );
    return new XksProxyAuthenticationCredentialType(
      accessKeyId,
      rawSecretAccessKey
    );
  }

  public static XksProxyConfigurationType XksProxyConfigurationType(
    software.amazon.awssdk.services.kms.model.XksProxyConfigurationType nativeValue
  ) {
    Option<XksProxyConnectivityType> connectivity;
    connectivity =
      Objects.nonNull(nativeValue.connectivity())
        ? Option.create_Some(
          ToDafny.XksProxyConnectivityType(nativeValue.connectivity())
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> accessKeyId;
    accessKeyId =
      Objects.nonNull(nativeValue.accessKeyId())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.accessKeyId()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> uriEndpoint;
    uriEndpoint =
      Objects.nonNull(nativeValue.uriEndpoint())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.uriEndpoint()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> uriPath;
    uriPath =
      Objects.nonNull(nativeValue.uriPath())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.uriPath()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> vpcEndpointServiceName;
    vpcEndpointServiceName =
      Objects.nonNull(nativeValue.vpcEndpointServiceName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.vpcEndpointServiceName()
          )
        )
        : Option.create_None();
    return new XksProxyConfigurationType(
      connectivity,
      accessKeyId,
      uriEndpoint,
      uriPath,
      vpcEndpointServiceName
    );
  }

  public static Error Error(AlreadyExistsException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_AlreadyExistsException(message);
  }

  public static Error Error(CloudHsmClusterInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CloudHsmClusterInUseException(message);
  }

  public static Error Error(
    CloudHsmClusterInvalidConfigurationException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CloudHsmClusterInvalidConfigurationException(message);
  }

  public static Error Error(CloudHsmClusterNotActiveException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CloudHsmClusterNotActiveException(message);
  }

  public static Error Error(CloudHsmClusterNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CloudHsmClusterNotFoundException(message);
  }

  public static Error Error(CloudHsmClusterNotRelatedException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CloudHsmClusterNotRelatedException(message);
  }

  public static Error Error(ConflictException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_ConflictException(message);
  }

  public static Error Error(CustomKeyStoreHasCmKsException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CustomKeyStoreHasCMKsException(message);
  }

  public static Error Error(CustomKeyStoreInvalidStateException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CustomKeyStoreInvalidStateException(message);
  }

  public static Error Error(CustomKeyStoreNameInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CustomKeyStoreNameInUseException(message);
  }

  public static Error Error(CustomKeyStoreNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_CustomKeyStoreNotFoundException(message);
  }

  public static Error Error(DependencyTimeoutException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_DependencyTimeoutException(message);
  }

  public static Error Error(DisabledException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_DisabledException(message);
  }

  public static Error Error(DryRunOperationException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_DryRunOperationException(message);
  }

  public static Error Error(ExpiredImportTokenException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_ExpiredImportTokenException(message);
  }

  public static Error Error(IncorrectKeyException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_IncorrectKeyException(message);
  }

  public static Error Error(IncorrectKeyMaterialException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_IncorrectKeyMaterialException(message);
  }

  public static Error Error(IncorrectTrustAnchorException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_IncorrectTrustAnchorException(message);
  }

  public static Error Error(InvalidAliasNameException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidAliasNameException(message);
  }

  public static Error Error(InvalidArnException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidArnException(message);
  }

  public static Error Error(InvalidCiphertextException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidCiphertextException(message);
  }

  public static Error Error(InvalidGrantIdException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidGrantIdException(message);
  }

  public static Error Error(InvalidGrantTokenException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidGrantTokenException(message);
  }

  public static Error Error(InvalidImportTokenException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidImportTokenException(message);
  }

  public static Error Error(InvalidKeyUsageException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidKeyUsageException(message);
  }

  public static Error Error(InvalidMarkerException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_InvalidMarkerException(message);
  }

  public static Error Error(KeyUnavailableException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_KeyUnavailableException(message);
  }

  public static Error Error(KmsInternalException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_KMSInternalException(message);
  }

  public static Error Error(KmsInvalidMacException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_KMSInvalidMacException(message);
  }

  public static Error Error(KmsInvalidSignatureException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_KMSInvalidSignatureException(message);
  }

  public static Error Error(KmsInvalidStateException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_KMSInvalidStateException(message);
  }

  public static Error Error(LimitExceededException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_LimitExceededException(message);
  }

  public static Error Error(MalformedPolicyDocumentException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_MalformedPolicyDocumentException(message);
  }

  public static Error Error(NotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_NotFoundException(message);
  }

  public static Error Error(TagException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_TagException(message);
  }

  public static Error Error(UnsupportedOperationException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_UnsupportedOperationException(message);
  }

  public static Error Error(XksKeyAlreadyInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksKeyAlreadyInUseException(message);
  }

  public static Error Error(XksKeyInvalidConfigurationException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksKeyInvalidConfigurationException(message);
  }

  public static Error Error(XksKeyNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksKeyNotFoundException(message);
  }

  public static Error Error(
    XksProxyIncorrectAuthenticationCredentialException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyIncorrectAuthenticationCredentialException(
      message
    );
  }

  public static Error Error(XksProxyInvalidConfigurationException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyInvalidConfigurationException(message);
  }

  public static Error Error(XksProxyInvalidResponseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyInvalidResponseException(message);
  }

  public static Error Error(XksProxyUriEndpointInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyUriEndpointInUseException(message);
  }

  public static Error Error(XksProxyUriInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyUriInUseException(message);
  }

  public static Error Error(XksProxyUriUnreachableException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyUriUnreachableException(message);
  }

  public static Error Error(
    XksProxyVpcEndpointServiceInUseException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyVpcEndpointServiceInUseException(message);
  }

  public static Error Error(
    XksProxyVpcEndpointServiceInvalidConfigurationException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyVpcEndpointServiceInvalidConfigurationException(
      message
    );
  }

  public static Error Error(
    XksProxyVpcEndpointServiceNotFoundException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None();
    return new Error_XksProxyVpcEndpointServiceNotFoundException(message);
  }

  public static AlgorithmSpec AlgorithmSpec(
    software.amazon.awssdk.services.kms.model.AlgorithmSpec nativeValue
  ) {
    switch (nativeValue) {
      case RSAES_PKCS1_V1_5:
        {
          return AlgorithmSpec.create_RSAES__PKCS1__V1__5();
        }
      case RSAES_OAEP_SHA_1:
        {
          return AlgorithmSpec.create_RSAES__OAEP__SHA__1();
        }
      case RSAES_OAEP_SHA_256:
        {
          return AlgorithmSpec.create_RSAES__OAEP__SHA__256();
        }
      case RSA_AES_KEY_WRAP_SHA_1:
        {
          return AlgorithmSpec.create_RSA__AES__KEY__WRAP__SHA__1();
        }
      case RSA_AES_KEY_WRAP_SHA_256:
        {
          return AlgorithmSpec.create_RSA__AES__KEY__WRAP__SHA__256();
        }
      case SM2_PKE:
        {
          return AlgorithmSpec.create_SM2PKE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.AlgorithmSpec."
          );
        }
    }
  }

  public static ConnectionErrorCodeType ConnectionErrorCodeType(
    software.amazon.awssdk.services.kms.model.ConnectionErrorCodeType nativeValue
  ) {
    switch (nativeValue) {
      case INVALID_CREDENTIALS:
        {
          return ConnectionErrorCodeType.create_INVALID__CREDENTIALS();
        }
      case CLUSTER_NOT_FOUND:
        {
          return ConnectionErrorCodeType.create_CLUSTER__NOT__FOUND();
        }
      case NETWORK_ERRORS:
        {
          return ConnectionErrorCodeType.create_NETWORK__ERRORS();
        }
      case INTERNAL_ERROR:
        {
          return ConnectionErrorCodeType.create_INTERNAL__ERROR();
        }
      case INSUFFICIENT_CLOUDHSM_HSMS:
        {
          return ConnectionErrorCodeType.create_INSUFFICIENT__CLOUDHSM__HSMS();
        }
      case USER_LOCKED_OUT:
        {
          return ConnectionErrorCodeType.create_USER__LOCKED__OUT();
        }
      case USER_NOT_FOUND:
        {
          return ConnectionErrorCodeType.create_USER__NOT__FOUND();
        }
      case USER_LOGGED_IN:
        {
          return ConnectionErrorCodeType.create_USER__LOGGED__IN();
        }
      case SUBNET_NOT_FOUND:
        {
          return ConnectionErrorCodeType.create_SUBNET__NOT__FOUND();
        }
      case INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET:
        {
          return ConnectionErrorCodeType.create_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET();
        }
      case XKS_PROXY_ACCESS_DENIED:
        {
          return ConnectionErrorCodeType.create_XKS__PROXY__ACCESS__DENIED();
        }
      case XKS_PROXY_NOT_REACHABLE:
        {
          return ConnectionErrorCodeType.create_XKS__PROXY__NOT__REACHABLE();
        }
      case XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND:
        {
          return ConnectionErrorCodeType.create_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND();
        }
      case XKS_PROXY_INVALID_RESPONSE:
        {
          return ConnectionErrorCodeType.create_XKS__PROXY__INVALID__RESPONSE();
        }
      case XKS_PROXY_INVALID_CONFIGURATION:
        {
          return ConnectionErrorCodeType.create_XKS__PROXY__INVALID__CONFIGURATION();
        }
      case XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION:
        {
          return ConnectionErrorCodeType.create_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION();
        }
      case XKS_PROXY_TIMED_OUT:
        {
          return ConnectionErrorCodeType.create_XKS__PROXY__TIMED__OUT();
        }
      case XKS_PROXY_INVALID_TLS_CONFIGURATION:
        {
          return ConnectionErrorCodeType.create_XKS__PROXY__INVALID__TLS__CONFIGURATION();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.ConnectionErrorCodeType."
          );
        }
    }
  }

  public static ConnectionStateType ConnectionStateType(
    software.amazon.awssdk.services.kms.model.ConnectionStateType nativeValue
  ) {
    switch (nativeValue) {
      case CONNECTED:
        {
          return ConnectionStateType.create_CONNECTED();
        }
      case CONNECTING:
        {
          return ConnectionStateType.create_CONNECTING();
        }
      case FAILED:
        {
          return ConnectionStateType.create_FAILED();
        }
      case DISCONNECTED:
        {
          return ConnectionStateType.create_DISCONNECTED();
        }
      case DISCONNECTING:
        {
          return ConnectionStateType.create_DISCONNECTING();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.ConnectionStateType."
          );
        }
    }
  }

  public static CustomerMasterKeySpec CustomerMasterKeySpec(
    software.amazon.awssdk.services.kms.model.CustomerMasterKeySpec nativeValue
  ) {
    switch (nativeValue) {
      case RSA_2048:
        {
          return CustomerMasterKeySpec.create_RSA__2048();
        }
      case RSA_3072:
        {
          return CustomerMasterKeySpec.create_RSA__3072();
        }
      case RSA_4096:
        {
          return CustomerMasterKeySpec.create_RSA__4096();
        }
      case ECC_NIST_P256:
        {
          return CustomerMasterKeySpec.create_ECC__NIST__P256();
        }
      case ECC_NIST_P384:
        {
          return CustomerMasterKeySpec.create_ECC__NIST__P384();
        }
      case ECC_NIST_P521:
        {
          return CustomerMasterKeySpec.create_ECC__NIST__P521();
        }
      case ECC_SECG_P256_K1:
        {
          return CustomerMasterKeySpec.create_ECC__SECG__P256K1();
        }
      case SYMMETRIC_DEFAULT:
        {
          return CustomerMasterKeySpec.create_SYMMETRIC__DEFAULT();
        }
      case HMAC_224:
        {
          return CustomerMasterKeySpec.create_HMAC__224();
        }
      case HMAC_256:
        {
          return CustomerMasterKeySpec.create_HMAC__256();
        }
      case HMAC_384:
        {
          return CustomerMasterKeySpec.create_HMAC__384();
        }
      case HMAC_512:
        {
          return CustomerMasterKeySpec.create_HMAC__512();
        }
      case SM2:
        {
          return CustomerMasterKeySpec.create_SM2();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec."
          );
        }
    }
  }

  public static CustomKeyStoreType CustomKeyStoreType(
    software.amazon.awssdk.services.kms.model.CustomKeyStoreType nativeValue
  ) {
    switch (nativeValue) {
      case AWS_CLOUDHSM:
        {
          return CustomKeyStoreType.create_AWS__CLOUDHSM();
        }
      case EXTERNAL_KEY_STORE:
        {
          return CustomKeyStoreType.create_EXTERNAL__KEY__STORE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.CustomKeyStoreType."
          );
        }
    }
  }

  public static DataKeyPairSpec DataKeyPairSpec(
    software.amazon.awssdk.services.kms.model.DataKeyPairSpec nativeValue
  ) {
    switch (nativeValue) {
      case RSA_2048:
        {
          return DataKeyPairSpec.create_RSA__2048();
        }
      case RSA_3072:
        {
          return DataKeyPairSpec.create_RSA__3072();
        }
      case RSA_4096:
        {
          return DataKeyPairSpec.create_RSA__4096();
        }
      case ECC_NIST_P256:
        {
          return DataKeyPairSpec.create_ECC__NIST__P256();
        }
      case ECC_NIST_P384:
        {
          return DataKeyPairSpec.create_ECC__NIST__P384();
        }
      case ECC_NIST_P521:
        {
          return DataKeyPairSpec.create_ECC__NIST__P521();
        }
      case ECC_SECG_P256_K1:
        {
          return DataKeyPairSpec.create_ECC__SECG__P256K1();
        }
      case SM2:
        {
          return DataKeyPairSpec.create_SM2();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.DataKeyPairSpec."
          );
        }
    }
  }

  public static DataKeySpec DataKeySpec(
    software.amazon.awssdk.services.kms.model.DataKeySpec nativeValue
  ) {
    switch (nativeValue) {
      case AES_256:
        {
          return DataKeySpec.create_AES__256();
        }
      case AES_128:
        {
          return DataKeySpec.create_AES__128();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.DataKeySpec."
          );
        }
    }
  }

  public static EncryptionAlgorithmSpec EncryptionAlgorithmSpec(
    software.amazon.awssdk.services.kms.model.EncryptionAlgorithmSpec nativeValue
  ) {
    switch (nativeValue) {
      case SYMMETRIC_DEFAULT:
        {
          return EncryptionAlgorithmSpec.create_SYMMETRIC__DEFAULT();
        }
      case RSAES_OAEP_SHA_1:
        {
          return EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__1();
        }
      case RSAES_OAEP_SHA_256:
        {
          return EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__256();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec."
          );
        }
    }
  }

  public static ExpirationModelType ExpirationModelType(
    software.amazon.awssdk.services.kms.model.ExpirationModelType nativeValue
  ) {
    switch (nativeValue) {
      case KEY_MATERIAL_EXPIRES:
        {
          return ExpirationModelType.create_KEY__MATERIAL__EXPIRES();
        }
      case KEY_MATERIAL_DOES_NOT_EXPIRE:
        {
          return ExpirationModelType.create_KEY__MATERIAL__DOES__NOT__EXPIRE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.ExpirationModelType."
          );
        }
    }
  }

  public static GrantOperation GrantOperation(
    software.amazon.awssdk.services.kms.model.GrantOperation nativeValue
  ) {
    switch (nativeValue) {
      case DECRYPT:
        {
          return GrantOperation.create_Decrypt();
        }
      case ENCRYPT:
        {
          return GrantOperation.create_Encrypt();
        }
      case GENERATE_DATA_KEY:
        {
          return GrantOperation.create_GenerateDataKey();
        }
      case GENERATE_DATA_KEY_WITHOUT_PLAINTEXT:
        {
          return GrantOperation.create_GenerateDataKeyWithoutPlaintext();
        }
      case RE_ENCRYPT_FROM:
        {
          return GrantOperation.create_ReEncryptFrom();
        }
      case RE_ENCRYPT_TO:
        {
          return GrantOperation.create_ReEncryptTo();
        }
      case SIGN:
        {
          return GrantOperation.create_Sign();
        }
      case VERIFY:
        {
          return GrantOperation.create_Verify();
        }
      case GET_PUBLIC_KEY:
        {
          return GrantOperation.create_GetPublicKey();
        }
      case CREATE_GRANT:
        {
          return GrantOperation.create_CreateGrant();
        }
      case RETIRE_GRANT:
        {
          return GrantOperation.create_RetireGrant();
        }
      case DESCRIBE_KEY:
        {
          return GrantOperation.create_DescribeKey();
        }
      case GENERATE_DATA_KEY_PAIR:
        {
          return GrantOperation.create_GenerateDataKeyPair();
        }
      case GENERATE_DATA_KEY_PAIR_WITHOUT_PLAINTEXT:
        {
          return GrantOperation.create_GenerateDataKeyPairWithoutPlaintext();
        }
      case GENERATE_MAC:
        {
          return GrantOperation.create_GenerateMac();
        }
      case VERIFY_MAC:
        {
          return GrantOperation.create_VerifyMac();
        }
      case DERIVE_SHARED_SECRET:
        {
          return GrantOperation.create_DeriveSharedSecret();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.GrantOperation."
          );
        }
    }
  }

  public static KeyAgreementAlgorithmSpec KeyAgreementAlgorithmSpec(
    software.amazon.awssdk.services.kms.model.KeyAgreementAlgorithmSpec nativeValue
  ) {
    switch (nativeValue) {
      case ECDH:
        {
          return KeyAgreementAlgorithmSpec.create();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec."
          );
        }
    }
  }

  public static KeyEncryptionMechanism KeyEncryptionMechanism(
    software.amazon.awssdk.services.kms.model.KeyEncryptionMechanism nativeValue
  ) {
    switch (nativeValue) {
      case RSAES_OAEP_SHA_256:
        {
          return KeyEncryptionMechanism.create();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.KeyEncryptionMechanism."
          );
        }
    }
  }

  public static KeyManagerType KeyManagerType(
    software.amazon.awssdk.services.kms.model.KeyManagerType nativeValue
  ) {
    switch (nativeValue) {
      case AWS:
        {
          return KeyManagerType.create_AWS();
        }
      case CUSTOMER:
        {
          return KeyManagerType.create_CUSTOMER();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.KeyManagerType."
          );
        }
    }
  }

  public static KeySpec KeySpec(
    software.amazon.awssdk.services.kms.model.KeySpec nativeValue
  ) {
    switch (nativeValue) {
      case RSA_2048:
        {
          return KeySpec.create_RSA__2048();
        }
      case RSA_3072:
        {
          return KeySpec.create_RSA__3072();
        }
      case RSA_4096:
        {
          return KeySpec.create_RSA__4096();
        }
      case ECC_NIST_P256:
        {
          return KeySpec.create_ECC__NIST__P256();
        }
      case ECC_NIST_P384:
        {
          return KeySpec.create_ECC__NIST__P384();
        }
      case ECC_NIST_P521:
        {
          return KeySpec.create_ECC__NIST__P521();
        }
      case ECC_SECG_P256_K1:
        {
          return KeySpec.create_ECC__SECG__P256K1();
        }
      case SYMMETRIC_DEFAULT:
        {
          return KeySpec.create_SYMMETRIC__DEFAULT();
        }
      case HMAC_224:
        {
          return KeySpec.create_HMAC__224();
        }
      case HMAC_256:
        {
          return KeySpec.create_HMAC__256();
        }
      case HMAC_384:
        {
          return KeySpec.create_HMAC__384();
        }
      case HMAC_512:
        {
          return KeySpec.create_HMAC__512();
        }
      case SM2:
        {
          return KeySpec.create_SM2();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.KeySpec."
          );
        }
    }
  }

  public static KeyState KeyState(
    software.amazon.awssdk.services.kms.model.KeyState nativeValue
  ) {
    switch (nativeValue) {
      case CREATING:
        {
          return KeyState.create_Creating();
        }
      case ENABLED:
        {
          return KeyState.create_Enabled();
        }
      case DISABLED:
        {
          return KeyState.create_Disabled();
        }
      case PENDING_DELETION:
        {
          return KeyState.create_PendingDeletion();
        }
      case PENDING_IMPORT:
        {
          return KeyState.create_PendingImport();
        }
      case PENDING_REPLICA_DELETION:
        {
          return KeyState.create_PendingReplicaDeletion();
        }
      case UNAVAILABLE:
        {
          return KeyState.create_Unavailable();
        }
      case UPDATING:
        {
          return KeyState.create_Updating();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.KeyState."
          );
        }
    }
  }

  public static KeyUsageType KeyUsageType(
    software.amazon.awssdk.services.kms.model.KeyUsageType nativeValue
  ) {
    switch (nativeValue) {
      case SIGN_VERIFY:
        {
          return KeyUsageType.create_SIGN__VERIFY();
        }
      case ENCRYPT_DECRYPT:
        {
          return KeyUsageType.create_ENCRYPT__DECRYPT();
        }
      case GENERATE_VERIFY_MAC:
        {
          return KeyUsageType.create_GENERATE__VERIFY__MAC();
        }
      case KEY_AGREEMENT:
        {
          return KeyUsageType.create_KEY__AGREEMENT();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType."
          );
        }
    }
  }

  public static MacAlgorithmSpec MacAlgorithmSpec(
    software.amazon.awssdk.services.kms.model.MacAlgorithmSpec nativeValue
  ) {
    switch (nativeValue) {
      case HMAC_SHA_224:
        {
          return MacAlgorithmSpec.create_HMAC__SHA__224();
        }
      case HMAC_SHA_256:
        {
          return MacAlgorithmSpec.create_HMAC__SHA__256();
        }
      case HMAC_SHA_384:
        {
          return MacAlgorithmSpec.create_HMAC__SHA__384();
        }
      case HMAC_SHA_512:
        {
          return MacAlgorithmSpec.create_HMAC__SHA__512();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.MacAlgorithmSpec."
          );
        }
    }
  }

  public static MessageType MessageType(
    software.amazon.awssdk.services.kms.model.MessageType nativeValue
  ) {
    switch (nativeValue) {
      case RAW:
        {
          return MessageType.create_RAW();
        }
      case DIGEST:
        {
          return MessageType.create_DIGEST();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.MessageType."
          );
        }
    }
  }

  public static MultiRegionKeyType MultiRegionKeyType(
    software.amazon.awssdk.services.kms.model.MultiRegionKeyType nativeValue
  ) {
    switch (nativeValue) {
      case PRIMARY:
        {
          return MultiRegionKeyType.create_PRIMARY();
        }
      case REPLICA:
        {
          return MultiRegionKeyType.create_REPLICA();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.MultiRegionKeyType."
          );
        }
    }
  }

  public static OriginType OriginType(
    software.amazon.awssdk.services.kms.model.OriginType nativeValue
  ) {
    switch (nativeValue) {
      case AWS_KMS:
        {
          return OriginType.create_AWS__KMS();
        }
      case EXTERNAL:
        {
          return OriginType.create_EXTERNAL();
        }
      case AWS_CLOUDHSM:
        {
          return OriginType.create_AWS__CLOUDHSM();
        }
      case EXTERNAL_KEY_STORE:
        {
          return OriginType.create_EXTERNAL__KEY__STORE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.OriginType."
          );
        }
    }
  }

  public static RotationType RotationType(
    software.amazon.awssdk.services.kms.model.RotationType nativeValue
  ) {
    switch (nativeValue) {
      case AUTOMATIC:
        {
          return RotationType.create_AUTOMATIC();
        }
      case ON_DEMAND:
        {
          return RotationType.create_ON__DEMAND();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.RotationType."
          );
        }
    }
  }

  public static SigningAlgorithmSpec SigningAlgorithmSpec(
    software.amazon.awssdk.services.kms.model.SigningAlgorithmSpec nativeValue
  ) {
    switch (nativeValue) {
      case RSASSA_PSS_SHA_256:
        {
          return SigningAlgorithmSpec.create_RSASSA__PSS__SHA__256();
        }
      case RSASSA_PSS_SHA_384:
        {
          return SigningAlgorithmSpec.create_RSASSA__PSS__SHA__384();
        }
      case RSASSA_PSS_SHA_512:
        {
          return SigningAlgorithmSpec.create_RSASSA__PSS__SHA__512();
        }
      case RSASSA_PKCS1_V1_5_SHA_256:
        {
          return SigningAlgorithmSpec.create_RSASSA__PKCS1__V1__5__SHA__256();
        }
      case RSASSA_PKCS1_V1_5_SHA_384:
        {
          return SigningAlgorithmSpec.create_RSASSA__PKCS1__V1__5__SHA__384();
        }
      case RSASSA_PKCS1_V1_5_SHA_512:
        {
          return SigningAlgorithmSpec.create_RSASSA__PKCS1__V1__5__SHA__512();
        }
      case ECDSA_SHA_256:
        {
          return SigningAlgorithmSpec.create_ECDSA__SHA__256();
        }
      case ECDSA_SHA_384:
        {
          return SigningAlgorithmSpec.create_ECDSA__SHA__384();
        }
      case ECDSA_SHA_512:
        {
          return SigningAlgorithmSpec.create_ECDSA__SHA__512();
        }
      case SM2_DSA:
        {
          return SigningAlgorithmSpec.create_SM2DSA();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec."
          );
        }
    }
  }

  public static WrappingKeySpec WrappingKeySpec(
    software.amazon.awssdk.services.kms.model.WrappingKeySpec nativeValue
  ) {
    switch (nativeValue) {
      case RSA_2048:
        {
          return WrappingKeySpec.create_RSA__2048();
        }
      case RSA_3072:
        {
          return WrappingKeySpec.create_RSA__3072();
        }
      case RSA_4096:
        {
          return WrappingKeySpec.create_RSA__4096();
        }
      case SM2:
        {
          return WrappingKeySpec.create_SM2();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.WrappingKeySpec."
          );
        }
    }
  }

  public static XksProxyConnectivityType XksProxyConnectivityType(
    software.amazon.awssdk.services.kms.model.XksProxyConnectivityType nativeValue
  ) {
    switch (nativeValue) {
      case PUBLIC_ENDPOINT:
        {
          return XksProxyConnectivityType.create_PUBLIC__ENDPOINT();
        }
      case VPC_ENDPOINT_SERVICE:
        {
          return XksProxyConnectivityType.create_VPC__ENDPOINT__SERVICE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.kms.internaldafny.types.XksProxyConnectivityType."
          );
        }
    }
  }

  public static AlgorithmSpec AlgorithmSpec(String nativeValue) {
    return AlgorithmSpec(
      software.amazon.awssdk.services.kms.model.AlgorithmSpec.fromValue(
        nativeValue
      )
    );
  }

  public static ConnectionErrorCodeType ConnectionErrorCodeType(
    String nativeValue
  ) {
    return ConnectionErrorCodeType(
      software.amazon.awssdk.services.kms.model.ConnectionErrorCodeType.fromValue(
        nativeValue
      )
    );
  }

  public static ConnectionStateType ConnectionStateType(String nativeValue) {
    return ConnectionStateType(
      software.amazon.awssdk.services.kms.model.ConnectionStateType.fromValue(
        nativeValue
      )
    );
  }

  public static CustomerMasterKeySpec CustomerMasterKeySpec(
    String nativeValue
  ) {
    return CustomerMasterKeySpec(
      software.amazon.awssdk.services.kms.model.CustomerMasterKeySpec.fromValue(
        nativeValue
      )
    );
  }

  public static CustomKeyStoreType CustomKeyStoreType(String nativeValue) {
    return CustomKeyStoreType(
      software.amazon.awssdk.services.kms.model.CustomKeyStoreType.fromValue(
        nativeValue
      )
    );
  }

  public static DataKeyPairSpec DataKeyPairSpec(String nativeValue) {
    return DataKeyPairSpec(
      software.amazon.awssdk.services.kms.model.DataKeyPairSpec.fromValue(
        nativeValue
      )
    );
  }

  public static DataKeySpec DataKeySpec(String nativeValue) {
    return DataKeySpec(
      software.amazon.awssdk.services.kms.model.DataKeySpec.fromValue(
        nativeValue
      )
    );
  }

  public static EncryptionAlgorithmSpec EncryptionAlgorithmSpec(
    String nativeValue
  ) {
    return EncryptionAlgorithmSpec(
      software.amazon.awssdk.services.kms.model.EncryptionAlgorithmSpec.fromValue(
        nativeValue
      )
    );
  }

  public static ExpirationModelType ExpirationModelType(String nativeValue) {
    return ExpirationModelType(
      software.amazon.awssdk.services.kms.model.ExpirationModelType.fromValue(
        nativeValue
      )
    );
  }

  public static GrantOperation GrantOperation(String nativeValue) {
    return GrantOperation(
      software.amazon.awssdk.services.kms.model.GrantOperation.fromValue(
        nativeValue
      )
    );
  }

  public static KeyAgreementAlgorithmSpec KeyAgreementAlgorithmSpec(
    String nativeValue
  ) {
    return KeyAgreementAlgorithmSpec(
      software.amazon.awssdk.services.kms.model.KeyAgreementAlgorithmSpec.fromValue(
        nativeValue
      )
    );
  }

  public static KeyEncryptionMechanism KeyEncryptionMechanism(
    String nativeValue
  ) {
    return KeyEncryptionMechanism(
      software.amazon.awssdk.services.kms.model.KeyEncryptionMechanism.fromValue(
        nativeValue
      )
    );
  }

  public static KeyManagerType KeyManagerType(String nativeValue) {
    return KeyManagerType(
      software.amazon.awssdk.services.kms.model.KeyManagerType.fromValue(
        nativeValue
      )
    );
  }

  public static KeySpec KeySpec(String nativeValue) {
    return KeySpec(
      software.amazon.awssdk.services.kms.model.KeySpec.fromValue(nativeValue)
    );
  }

  public static KeyState KeyState(String nativeValue) {
    return KeyState(
      software.amazon.awssdk.services.kms.model.KeyState.fromValue(nativeValue)
    );
  }

  public static KeyUsageType KeyUsageType(String nativeValue) {
    return KeyUsageType(
      software.amazon.awssdk.services.kms.model.KeyUsageType.fromValue(
        nativeValue
      )
    );
  }

  public static MacAlgorithmSpec MacAlgorithmSpec(String nativeValue) {
    return MacAlgorithmSpec(
      software.amazon.awssdk.services.kms.model.MacAlgorithmSpec.fromValue(
        nativeValue
      )
    );
  }

  public static MessageType MessageType(String nativeValue) {
    return MessageType(
      software.amazon.awssdk.services.kms.model.MessageType.fromValue(
        nativeValue
      )
    );
  }

  public static MultiRegionKeyType MultiRegionKeyType(String nativeValue) {
    return MultiRegionKeyType(
      software.amazon.awssdk.services.kms.model.MultiRegionKeyType.fromValue(
        nativeValue
      )
    );
  }

  public static OriginType OriginType(String nativeValue) {
    return OriginType(
      software.amazon.awssdk.services.kms.model.OriginType.fromValue(
        nativeValue
      )
    );
  }

  public static RotationType RotationType(String nativeValue) {
    return RotationType(
      software.amazon.awssdk.services.kms.model.RotationType.fromValue(
        nativeValue
      )
    );
  }

  public static SigningAlgorithmSpec SigningAlgorithmSpec(String nativeValue) {
    return SigningAlgorithmSpec(
      software.amazon.awssdk.services.kms.model.SigningAlgorithmSpec.fromValue(
        nativeValue
      )
    );
  }

  public static WrappingKeySpec WrappingKeySpec(String nativeValue) {
    return WrappingKeySpec(
      software.amazon.awssdk.services.kms.model.WrappingKeySpec.fromValue(
        nativeValue
      )
    );
  }

  public static XksProxyConnectivityType XksProxyConnectivityType(
    String nativeValue
  ) {
    return XksProxyConnectivityType(
      software.amazon.awssdk.services.kms.model.XksProxyConnectivityType.fromValue(
        nativeValue
      )
    );
  }

  public static Error Error(KmsException nativeValue) {
    // While this is logically identical to the other Opaque Error case,
    // it is semantically distinct.
    // An un-modeled Service Error is different from a Java Heap Exhaustion error.
    // In the future, Smithy-Dafny MAY allow for this distinction.
    // Which would allow Dafny developers to treat the two differently.
    return Error.create_OpaqueWithText(
      nativeValue,
      dafny.DafnySequence.asString(nativeValue.getMessage())
    );
  }

  public static Error Error(Exception nativeValue) {
    // While this is logically identical to the other Opaque Error case,
    // it is semantically distinct.
    // An un-modeled Service Error is different from a Java Heap Exhaustion error.
    // In the future, Smithy-Dafny MAY allow for this distinction.
    // Which would allow Dafny developers to treat the two differently.
    return Error.create_OpaqueWithText(
      nativeValue,
      dafny.DafnySequence.asString(nativeValue.getMessage())
    );
  }

  public static IKMSClient TrentService(KmsClient nativeValue) {
    return new Shim(nativeValue, null);
  }
}
