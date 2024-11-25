// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin;

import dafny.DafnySequence;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.List;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_OpaqueWithText;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnsupportedFeatureException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.AwsKmsDecryptEncrypt;
import software.amazon.cryptography.keystoreadmin.model.CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationFlag;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricEncryption;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricKeyArn;
import software.amazon.cryptography.keystoreadmin.model.MutableBranchKeyProperties;
import software.amazon.cryptography.keystoreadmin.model.MutatedBranchKeyItem;
import software.amazon.cryptography.keystoreadmin.model.MutationComplete;
import software.amazon.cryptography.keystoreadmin.model.MutationConflictException;
import software.amazon.cryptography.keystoreadmin.model.MutationDescription;
import software.amazon.cryptography.keystoreadmin.model.MutationDetails;
import software.amazon.cryptography.keystoreadmin.model.MutationFromException;
import software.amazon.cryptography.keystoreadmin.model.MutationInFlight;
import software.amazon.cryptography.keystoreadmin.model.MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.model.MutationToException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.MutationVerificationException;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.OpaqueError;
import software.amazon.cryptography.keystoreadmin.model.OpaqueWithTextError;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;
import software.amazon.cryptography.keystoreadmin.model.UnexpectedStateException;
import software.amazon.cryptography.keystoreadmin.model.UnsupportedFeatureException;
import software.amazon.cryptography.keystoreadmin.model.VersionKeyInput;
import software.amazon.cryptography.keystoreadmin.model.VersionKeyOutput;

public class ToNative {

  public static OpaqueError Error(Error_Opaque dafnyValue) {
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue.dtor_obj());
    return nativeBuilder.build();
  }

  public static OpaqueWithTextError Error(Error_OpaqueWithText dafnyValue) {
    OpaqueWithTextError.Builder nativeBuilder = OpaqueWithTextError.builder();
    nativeBuilder.obj(dafnyValue.dtor_obj());
    nativeBuilder.objMessage(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_objMessage()
      )
    );
    return nativeBuilder.build();
  }

  public static CollectionOfErrors Error(Error_CollectionOfErrors dafnyValue) {
    CollectionOfErrors.Builder nativeBuilder = CollectionOfErrors.builder();
    nativeBuilder.list(
      software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToList(
        dafnyValue.dtor_list(),
        ToNative::Error
      )
    );
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static KeyStoreAdminException Error(
    Error_KeyStoreAdminException dafnyValue
  ) {
    KeyStoreAdminException.Builder nativeBuilder =
      KeyStoreAdminException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MutationConflictException Error(
    Error_MutationConflictException dafnyValue
  ) {
    MutationConflictException.Builder nativeBuilder =
      MutationConflictException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MutationFromException Error(
    Error_MutationFromException dafnyValue
  ) {
    MutationFromException.Builder nativeBuilder =
      MutationFromException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MutationInvalidException Error(
    Error_MutationInvalidException dafnyValue
  ) {
    MutationInvalidException.Builder nativeBuilder =
      MutationInvalidException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MutationToException Error(
    Error_MutationToException dafnyValue
  ) {
    MutationToException.Builder nativeBuilder = MutationToException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MutationVerificationException Error(
    Error_MutationVerificationException dafnyValue
  ) {
    MutationVerificationException.Builder nativeBuilder =
      MutationVerificationException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static UnexpectedStateException Error(
    Error_UnexpectedStateException dafnyValue
  ) {
    UnexpectedStateException.Builder nativeBuilder =
      UnexpectedStateException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static UnsupportedFeatureException Error(
    Error_UnsupportedFeatureException dafnyValue
  ) {
    UnsupportedFeatureException.Builder nativeBuilder =
      UnsupportedFeatureException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static RuntimeException Error(Error dafnyValue) {
    if (dafnyValue.is_KeyStoreAdminException()) {
      return ToNative.Error((Error_KeyStoreAdminException) dafnyValue);
    }
    if (dafnyValue.is_MutationConflictException()) {
      return ToNative.Error((Error_MutationConflictException) dafnyValue);
    }
    if (dafnyValue.is_MutationFromException()) {
      return ToNative.Error((Error_MutationFromException) dafnyValue);
    }
    if (dafnyValue.is_MutationInvalidException()) {
      return ToNative.Error((Error_MutationInvalidException) dafnyValue);
    }
    if (dafnyValue.is_MutationToException()) {
      return ToNative.Error((Error_MutationToException) dafnyValue);
    }
    if (dafnyValue.is_MutationVerificationException()) {
      return ToNative.Error((Error_MutationVerificationException) dafnyValue);
    }
    if (dafnyValue.is_UnexpectedStateException()) {
      return ToNative.Error((Error_UnexpectedStateException) dafnyValue);
    }
    if (dafnyValue.is_UnsupportedFeatureException()) {
      return ToNative.Error((Error_UnsupportedFeatureException) dafnyValue);
    }
    if (dafnyValue.is_Opaque()) {
      return ToNative.Error((Error_Opaque) dafnyValue);
    }
    if (dafnyValue.is_OpaqueWithText()) {
      return ToNative.Error((Error_OpaqueWithText) dafnyValue);
    }
    if (dafnyValue.is_CollectionOfErrors()) {
      return ToNative.Error((Error_CollectionOfErrors) dafnyValue);
    }
    if (dafnyValue.is_AwsCryptographyPrimitives()) {
      return software.amazon.cryptography.primitives.ToNative.Error(
        dafnyValue.dtor_AwsCryptographyPrimitives()
      );
    }
    if (dafnyValue.is_ComAmazonawsDynamodb()) {
      return software.amazon.cryptography.services.dynamodb.internaldafny.ToNative.Error(
        dafnyValue.dtor_ComAmazonawsDynamodb()
      );
    }
    if (dafnyValue.is_ComAmazonawsKms()) {
      return software.amazon.cryptography.services.kms.internaldafny.ToNative.Error(
        dafnyValue.dtor_ComAmazonawsKms()
      );
    }
    if (dafnyValue.is_AwsCryptographyKeyStore()) {
      return software.amazon.cryptography.keystore.ToNative.Error(
        dafnyValue.dtor_AwsCryptographyKeyStore()
      );
    }
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue);
    return nativeBuilder.build();
  }

  public static ApplyMutationInput ApplyMutationInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput dafnyValue
  ) {
    ApplyMutationInput.Builder nativeBuilder = ApplyMutationInput.builder();
    nativeBuilder.MutationToken(
      ToNative.MutationToken(dafnyValue.dtor_MutationToken())
    );
    if (dafnyValue.dtor_PageSize().is_Some()) {
      nativeBuilder.PageSize((dafnyValue.dtor_PageSize().dtor_value()));
    }
    if (dafnyValue.dtor_Strategy().is_Some()) {
      nativeBuilder.Strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_Strategy().dtor_value())
      );
    }
    if (dafnyValue.dtor_SystemKey().is_Some()) {
      nativeBuilder.SystemKey(
        ToNative.SystemKey(dafnyValue.dtor_SystemKey().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static ApplyMutationOutput ApplyMutationOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput dafnyValue
  ) {
    ApplyMutationOutput.Builder nativeBuilder = ApplyMutationOutput.builder();
    nativeBuilder.MutationResult(
      ToNative.ApplyMutationResult(dafnyValue.dtor_MutationResult())
    );
    nativeBuilder.MutatedBranchKeyItems(
      ToNative.MutatedBranchKeyItems(dafnyValue.dtor_MutatedBranchKeyItems())
    );
    return nativeBuilder.build();
  }

  public static AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.AwsKmsDecryptEncrypt dafnyValue
  ) {
    AwsKmsDecryptEncrypt.Builder nativeBuilder = AwsKmsDecryptEncrypt.builder();
    if (dafnyValue.dtor_decrypt().is_Some()) {
      nativeBuilder.decrypt(
        software.amazon.cryptography.keystore.ToNative.AwsKms(
          dafnyValue.dtor_decrypt().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_encrypt().is_Some()) {
      nativeBuilder.encrypt(
        software.amazon.cryptography.keystore.ToNative.AwsKms(
          dafnyValue.dtor_encrypt().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static CreateKeyInput CreateKeyInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput dafnyValue
  ) {
    CreateKeyInput.Builder nativeBuilder = CreateKeyInput.builder();
    if (dafnyValue.dtor_Identifier().is_Some()) {
      nativeBuilder.Identifier(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_Identifier().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_EncryptionContext().is_Some()) {
      nativeBuilder.EncryptionContext(
        software.amazon.cryptography.keystore.ToNative.EncryptionContext(
          dafnyValue.dtor_EncryptionContext().dtor_value()
        )
      );
    }
    nativeBuilder.KmsArn(ToNative.KmsSymmetricKeyArn(dafnyValue.dtor_KmsArn()));
    if (dafnyValue.dtor_Strategy().is_Some()) {
      nativeBuilder.Strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_Strategy().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static CreateKeyOutput CreateKeyOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput dafnyValue
  ) {
    CreateKeyOutput.Builder nativeBuilder = CreateKeyOutput.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    return nativeBuilder.build();
  }

  public static DescribeMutationInput DescribeMutationInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput dafnyValue
  ) {
    DescribeMutationInput.Builder nativeBuilder =
      DescribeMutationInput.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    return nativeBuilder.build();
  }

  public static DescribeMutationOutput DescribeMutationOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput dafnyValue
  ) {
    DescribeMutationOutput.Builder nativeBuilder =
      DescribeMutationOutput.builder();
    nativeBuilder.MutationInFlight(
      ToNative.MutationInFlight(dafnyValue.dtor_MutationInFlight())
    );
    return nativeBuilder.build();
  }

  public static InitializeMutationInput InitializeMutationInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput dafnyValue
  ) {
    InitializeMutationInput.Builder nativeBuilder =
      InitializeMutationInput.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    nativeBuilder.Mutations(ToNative.Mutations(dafnyValue.dtor_Mutations()));
    if (dafnyValue.dtor_Strategy().is_Some()) {
      nativeBuilder.Strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_Strategy().dtor_value())
      );
    }
    if (dafnyValue.dtor_SystemKey().is_Some()) {
      nativeBuilder.SystemKey(
        ToNative.SystemKey(dafnyValue.dtor_SystemKey().dtor_value())
      );
    }
    if (dafnyValue.dtor_DoNotVersion().is_Some()) {
      nativeBuilder.DoNotVersion((dafnyValue.dtor_DoNotVersion().dtor_value()));
    }
    return nativeBuilder.build();
  }

  public static InitializeMutationOutput InitializeMutationOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput dafnyValue
  ) {
    InitializeMutationOutput.Builder nativeBuilder =
      InitializeMutationOutput.builder();
    nativeBuilder.MutationToken(
      ToNative.MutationToken(dafnyValue.dtor_MutationToken())
    );
    nativeBuilder.MutatedBranchKeyItems(
      ToNative.MutatedBranchKeyItems(dafnyValue.dtor_MutatedBranchKeyItems())
    );
    nativeBuilder.InitializeMutationFlag(
      ToNative.InitializeMutationFlag(dafnyValue.dtor_InitializeMutationFlag())
    );
    return nativeBuilder.build();
  }

  public static KeyStoreAdminConfig KeyStoreAdminConfig(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig dafnyValue
  ) {
    KeyStoreAdminConfig.Builder nativeBuilder = KeyStoreAdminConfig.builder();
    nativeBuilder.logicalKeyStoreName(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_logicalKeyStoreName()
      )
    );
    nativeBuilder.storage(
      software.amazon.cryptography.keystore.ToNative.Storage(
        dafnyValue.dtor_storage()
      )
    );
    return nativeBuilder.build();
  }

  public static KmsSymmetricEncryption KmsSymmetricEncryption(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricEncryption dafnyValue
  ) {
    KmsSymmetricEncryption.Builder nativeBuilder =
      KmsSymmetricEncryption.builder();
    nativeBuilder.KmsArn(ToNative.KmsSymmetricKeyArn(dafnyValue.dtor_KmsArn()));
    nativeBuilder.AwsKms(
      software.amazon.cryptography.keystore.ToNative.AwsKms(
        dafnyValue.dtor_AwsKms()
      )
    );
    return nativeBuilder.build();
  }

  public static MutableBranchKeyProperties MutableBranchKeyProperties(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyProperties dafnyValue
  ) {
    MutableBranchKeyProperties.Builder nativeBuilder =
      MutableBranchKeyProperties.builder();
    nativeBuilder.KmsArn(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_KmsArn()
      )
    );
    nativeBuilder.CustomEncryptionContext(
      software.amazon.cryptography.keystore.ToNative.EncryptionContextString(
        dafnyValue.dtor_CustomEncryptionContext()
      )
    );
    return nativeBuilder.build();
  }

  public static MutatedBranchKeyItem MutatedBranchKeyItem(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem dafnyValue
  ) {
    MutatedBranchKeyItem.Builder nativeBuilder = MutatedBranchKeyItem.builder();
    nativeBuilder.ItemType(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_ItemType()
      )
    );
    nativeBuilder.Description(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Description()
      )
    );
    return nativeBuilder.build();
  }

  public static MutationComplete MutationComplete(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete dafnyValue
  ) {
    MutationComplete.Builder nativeBuilder = MutationComplete.builder();
    return nativeBuilder.build();
  }

  public static MutationDescription MutationDescription(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDescription dafnyValue
  ) {
    MutationDescription.Builder nativeBuilder = MutationDescription.builder();
    nativeBuilder.MutationDetails(
      ToNative.MutationDetails(dafnyValue.dtor_MutationDetails())
    );
    nativeBuilder.MutationToken(
      ToNative.MutationToken(dafnyValue.dtor_MutationToken())
    );
    return nativeBuilder.build();
  }

  public static MutationDetails MutationDetails(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDetails dafnyValue
  ) {
    MutationDetails.Builder nativeBuilder = MutationDetails.builder();
    nativeBuilder.Original(
      ToNative.MutableBranchKeyProperties(dafnyValue.dtor_Original())
    );
    nativeBuilder.Terminal(
      ToNative.MutableBranchKeyProperties(dafnyValue.dtor_Terminal())
    );
    nativeBuilder.Input(ToNative.Mutations(dafnyValue.dtor_Input()));
    nativeBuilder.SystemKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_SystemKey()
      )
    );
    nativeBuilder.CreateTime(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_CreateTime()
      )
    );
    nativeBuilder.UUID(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_UUID()
      )
    );
    return nativeBuilder.build();
  }

  public static Mutations Mutations(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations dafnyValue
  ) {
    Mutations.Builder nativeBuilder = Mutations.builder();
    if (dafnyValue.dtor_TerminalKmsArn().is_Some()) {
      nativeBuilder.TerminalKmsArn(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_TerminalKmsArn().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_TerminalEncryptionContext().is_Some()) {
      nativeBuilder.TerminalEncryptionContext(
        software.amazon.cryptography.keystore.ToNative.EncryptionContextString(
          dafnyValue.dtor_TerminalEncryptionContext().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static MutationToken MutationToken(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken dafnyValue
  ) {
    MutationToken.Builder nativeBuilder = MutationToken.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    nativeBuilder.UUID(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_UUID()
      )
    );
    nativeBuilder.CreateTime(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_CreateTime()
      )
    );
    return nativeBuilder.build();
  }

  public static TrustStorage TrustStorage(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage dafnyValue
  ) {
    TrustStorage.Builder nativeBuilder = TrustStorage.builder();
    return nativeBuilder.build();
  }

  public static VersionKeyInput VersionKeyInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput dafnyValue
  ) {
    VersionKeyInput.Builder nativeBuilder = VersionKeyInput.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    nativeBuilder.KmsArn(ToNative.KmsSymmetricKeyArn(dafnyValue.dtor_KmsArn()));
    if (dafnyValue.dtor_Strategy().is_Some()) {
      nativeBuilder.Strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_Strategy().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static VersionKeyOutput VersionKeyOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput dafnyValue
  ) {
    VersionKeyOutput.Builder nativeBuilder = VersionKeyOutput.builder();
    return nativeBuilder.build();
  }

  public static InitializeMutationFlag InitializeMutationFlag(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag dafnyValue
  ) {
    if (dafnyValue.is_Created()) {
      return InitializeMutationFlag.Created;
    }
    if (dafnyValue.is_Resumed()) {
      return InitializeMutationFlag.Resumed;
    }
    if (dafnyValue.is_ResumedWithoutIndex()) {
      return InitializeMutationFlag.ResumedWithoutIndex;
    }
    throw new IllegalArgumentException(
      "No entry of software.amazon.cryptography.keystoreadmin.model.InitializeMutationFlag matches the input : " +
      dafnyValue
    );
  }

  public static ApplyMutationResult ApplyMutationResult(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult dafnyValue
  ) {
    ApplyMutationResult.Builder nativeBuilder = ApplyMutationResult.builder();
    if (dafnyValue.is_ContinueMutation()) {
      nativeBuilder.ContinueMutation(
        ToNative.MutationToken(dafnyValue.dtor_ContinueMutation())
      );
    }
    if (dafnyValue.is_CompleteMutation()) {
      nativeBuilder.CompleteMutation(
        ToNative.MutationComplete(dafnyValue.dtor_CompleteMutation())
      );
    }
    return nativeBuilder.build();
  }

  public static KeyManagementStrategy KeyManagementStrategy(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy dafnyValue
  ) {
    KeyManagementStrategy.Builder nativeBuilder =
      KeyManagementStrategy.builder();
    if (dafnyValue.is_AwsKmsReEncrypt()) {
      nativeBuilder.AwsKmsReEncrypt(
        software.amazon.cryptography.keystore.ToNative.AwsKms(
          dafnyValue.dtor_AwsKmsReEncrypt()
        )
      );
    }
    if (dafnyValue.is_AwsKmsDecryptEncrypt()) {
      nativeBuilder.AwsKmsDecryptEncrypt(
        ToNative.AwsKmsDecryptEncrypt(dafnyValue.dtor_AwsKmsDecryptEncrypt())
      );
    }
    return nativeBuilder.build();
  }

  public static KmsSymmetricKeyArn KmsSymmetricKeyArn(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricKeyArn dafnyValue
  ) {
    KmsSymmetricKeyArn.Builder nativeBuilder = KmsSymmetricKeyArn.builder();
    if (dafnyValue.is_KmsKeyArn()) {
      nativeBuilder.KmsKeyArn(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_KmsKeyArn()
        )
      );
    }
    if (dafnyValue.is_KmsMRKeyArn()) {
      nativeBuilder.KmsMRKeyArn(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_KmsMRKeyArn()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static MutationInFlight MutationInFlight(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationInFlight dafnyValue
  ) {
    MutationInFlight.Builder nativeBuilder = MutationInFlight.builder();
    if (dafnyValue.is_Yes()) {
      nativeBuilder.Yes(ToNative.MutationDescription(dafnyValue.dtor_Yes()));
    }
    if (dafnyValue.is_No()) {
      nativeBuilder.No(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_No()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static SystemKey SystemKey(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey dafnyValue
  ) {
    SystemKey.Builder nativeBuilder = SystemKey.builder();
    if (dafnyValue.is_kmsSymmetricEncryption()) {
      nativeBuilder.kmsSymmetricEncryption(
        ToNative.KmsSymmetricEncryption(
          dafnyValue.dtor_kmsSymmetricEncryption()
        )
      );
    }
    if (dafnyValue.is_trustStorage()) {
      nativeBuilder.trustStorage(
        ToNative.TrustStorage(dafnyValue.dtor_trustStorage())
      );
    }
    return nativeBuilder.build();
  }

  public static List<MutatedBranchKeyItem> MutatedBranchKeyItems(
    DafnySequence<
      ? extends software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem
    > dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToList(
      dafnyValue,
      software.amazon.cryptography.keystoreadmin.ToNative::MutatedBranchKeyItem
    );
  }

  public static KeyStoreAdmin KeyStoreAdmin(IKeyStoreAdminClient dafnyValue) {
    return new KeyStoreAdmin(dafnyValue);
  }
}
