// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin;

import dafny.DafnySequence;
import java.lang.RuntimeException;
import java.util.List;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationLockInvalidException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException;
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
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KMSIdentifier;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.MutatedBranchKeyItem;
import software.amazon.cryptography.keystoreadmin.model.MutationComplete;
import software.amazon.cryptography.keystoreadmin.model.MutationConflictException;
import software.amazon.cryptography.keystoreadmin.model.MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.model.MutationLockInvalidException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.OpaqueError;
import software.amazon.cryptography.keystoreadmin.model.UnexpectedStateException;
import software.amazon.cryptography.keystoreadmin.model.VersionKeyInput;
import software.amazon.cryptography.keystoreadmin.model.VersionKeyOutput;

public class ToNative {

  public static OpaqueError Error(Error_Opaque dafnyValue) {
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue.dtor_obj());
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

  public static MutationLockInvalidException Error(
    Error_MutationLockInvalidException dafnyValue
  ) {
    MutationLockInvalidException.Builder nativeBuilder =
      MutationLockInvalidException.builder();
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

  public static RuntimeException Error(Error dafnyValue) {
    if (dafnyValue.is_KeyStoreAdminException()) {
      return ToNative.Error((Error_KeyStoreAdminException) dafnyValue);
    }
    if (dafnyValue.is_MutationConflictException()) {
      return ToNative.Error((Error_MutationConflictException) dafnyValue);
    }
    if (dafnyValue.is_MutationInvalidException()) {
      return ToNative.Error((Error_MutationInvalidException) dafnyValue);
    }
    if (dafnyValue.is_MutationLockInvalidException()) {
      return ToNative.Error((Error_MutationLockInvalidException) dafnyValue);
    }
    if (dafnyValue.is_UnexpectedStateException()) {
      return ToNative.Error((Error_UnexpectedStateException) dafnyValue);
    }
    if (dafnyValue.is_Opaque()) {
      return ToNative.Error((Error_Opaque) dafnyValue);
    }
    if (dafnyValue.is_CollectionOfErrors()) {
      return ToNative.Error((Error_CollectionOfErrors) dafnyValue);
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
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue);
    return nativeBuilder.build();
  }

  public static ApplyMutationInput ApplyMutationInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput dafnyValue
  ) {
    ApplyMutationInput.Builder nativeBuilder = ApplyMutationInput.builder();
    nativeBuilder.mutationToken(
      ToNative.MutationToken(dafnyValue.dtor_mutationToken())
    );
    if (dafnyValue.dtor_pageSize().is_Some()) {
      nativeBuilder.pageSize((dafnyValue.dtor_pageSize().dtor_value()));
    }
    if (dafnyValue.dtor_strategy().is_Some()) {
      nativeBuilder.strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_strategy().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static ApplyMutationOutput ApplyMutationOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput dafnyValue
  ) {
    ApplyMutationOutput.Builder nativeBuilder = ApplyMutationOutput.builder();
    nativeBuilder.result(
      ToNative.ApplyMutationResult(dafnyValue.dtor_result())
    );
    nativeBuilder.mutatedBranchKeyItems(
      ToNative.MutatedBranchKeyItems(dafnyValue.dtor_mutatedBranchKeyItems())
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
    if (dafnyValue.dtor_branchKeyIdentifier().is_Some()) {
      nativeBuilder.branchKeyIdentifier(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_branchKeyIdentifier().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_encryptionContext().is_Some()) {
      nativeBuilder.encryptionContext(
        software.amazon.cryptography.keystore.ToNative.EncryptionContext(
          dafnyValue.dtor_encryptionContext().dtor_value()
        )
      );
    }
    nativeBuilder.kmsArn(ToNative.KMSIdentifier(dafnyValue.dtor_kmsArn()));
    if (dafnyValue.dtor_strategy().is_Some()) {
      nativeBuilder.strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_strategy().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static CreateKeyOutput CreateKeyOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput dafnyValue
  ) {
    CreateKeyOutput.Builder nativeBuilder = CreateKeyOutput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    return nativeBuilder.build();
  }

  public static DescribeMutationInput DescribeMutationInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput dafnyValue
  ) {
    DescribeMutationInput.Builder nativeBuilder =
      DescribeMutationInput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    return nativeBuilder.build();
  }

  public static DescribeMutationOutput DescribeMutationOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput dafnyValue
  ) {
    DescribeMutationOutput.Builder nativeBuilder =
      DescribeMutationOutput.builder();
    if (dafnyValue.dtor_mutationToken().is_Some()) {
      nativeBuilder.mutationToken(
        ToNative.MutationToken(dafnyValue.dtor_mutationToken().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static InitializeMutationInput InitializeMutationInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput dafnyValue
  ) {
    InitializeMutationInput.Builder nativeBuilder =
      InitializeMutationInput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    nativeBuilder.mutations(ToNative.Mutations(dafnyValue.dtor_mutations()));
    if (dafnyValue.dtor_strategy().is_Some()) {
      nativeBuilder.strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_strategy().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static InitializeMutationOutput InitializeMutationOutput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput dafnyValue
  ) {
    InitializeMutationOutput.Builder nativeBuilder =
      InitializeMutationOutput.builder();
    nativeBuilder.mutationToken(
      ToNative.MutationToken(dafnyValue.dtor_mutationToken())
    );
    nativeBuilder.mutatedBranchKeyItems(
      ToNative.MutatedBranchKeyItems(dafnyValue.dtor_mutatedBranchKeyItems())
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

  public static MutatedBranchKeyItem MutatedBranchKeyItem(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem dafnyValue
  ) {
    MutatedBranchKeyItem.Builder nativeBuilder = MutatedBranchKeyItem.builder();
    nativeBuilder.itemType(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_itemType()
      )
    );
    nativeBuilder.description(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_description()
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

  public static Mutations Mutations(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations dafnyValue
  ) {
    Mutations.Builder nativeBuilder = Mutations.builder();
    if (dafnyValue.dtor_finalKmsArn().is_Some()) {
      nativeBuilder.finalKmsArn(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_finalKmsArn().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_finalEncryptionContext().is_Some()) {
      nativeBuilder.finalEncryptionContext(
        software.amazon.cryptography.keystore.ToNative.EncryptionContextString(
          dafnyValue.dtor_finalEncryptionContext().dtor_value()
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
    nativeBuilder.Original(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_Original()
      )
    );
    nativeBuilder.Terminal(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_Terminal()
      )
    );
    if (dafnyValue.dtor_ExclusiveStartKey().is_Some()) {
      nativeBuilder.ExclusiveStartKey(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyValue.dtor_ExclusiveStartKey().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_UUID().is_Some()) {
      nativeBuilder.UUID(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_UUID().dtor_value()
        )
      );
    }
    nativeBuilder.CreateTime(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_CreateTime()
      )
    );
    return nativeBuilder.build();
  }

  public static VersionKeyInput VersionKeyInput(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput dafnyValue
  ) {
    VersionKeyInput.Builder nativeBuilder = VersionKeyInput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    nativeBuilder.kmsArn(ToNative.KMSIdentifier(dafnyValue.dtor_kmsArn()));
    if (dafnyValue.dtor_strategy().is_Some()) {
      nativeBuilder.strategy(
        ToNative.KeyManagementStrategy(dafnyValue.dtor_strategy().dtor_value())
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

  public static ApplyMutationResult ApplyMutationResult(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult dafnyValue
  ) {
    ApplyMutationResult.Builder nativeBuilder = ApplyMutationResult.builder();
    if (dafnyValue.is_continueMutation()) {
      nativeBuilder.continueMutation(
        ToNative.MutationToken(dafnyValue.dtor_continueMutation())
      );
    }
    if (dafnyValue.is_completeMutation()) {
      nativeBuilder.completeMutation(
        ToNative.MutationComplete(dafnyValue.dtor_completeMutation())
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

  public static KMSIdentifier KMSIdentifier(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KMSIdentifier dafnyValue
  ) {
    KMSIdentifier.Builder nativeBuilder = KMSIdentifier.builder();
    if (dafnyValue.is_kmsKeyArn()) {
      nativeBuilder.kmsKeyArn(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_kmsKeyArn()
        )
      );
    }
    if (dafnyValue.is_kmsMRKeyArn()) {
      nativeBuilder.kmsMRKeyArn(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_kmsMRKeyArn()
        )
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
