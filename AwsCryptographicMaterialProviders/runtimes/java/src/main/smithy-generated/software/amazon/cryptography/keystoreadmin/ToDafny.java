// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin;

import Wrappers_Compile.Option;
import dafny.DafnyMap;
import dafny.DafnySequence;
import dafny.TypeDescriptor;
import java.lang.Byte;
import java.lang.Character;
import java.lang.IllegalArgumentException;
import java.lang.Integer;
import java.lang.RuntimeException;
import java.util.List;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.types.Storage;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationLockInvalidException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KMSIdentifier;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput;
import software.amazon.cryptography.keystoreadmin.model.CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.MutationConflictException;
import software.amazon.cryptography.keystoreadmin.model.MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.model.MutationLockInvalidException;
import software.amazon.cryptography.keystoreadmin.model.OpaqueError;
import software.amazon.cryptography.keystoreadmin.model.UnexpectedStateException;

public class ToDafny {

  public static Error Error(RuntimeException nativeValue) {
    if (nativeValue instanceof KeyStoreAdminException) {
      return ToDafny.Error((KeyStoreAdminException) nativeValue);
    }
    if (nativeValue instanceof MutationConflictException) {
      return ToDafny.Error((MutationConflictException) nativeValue);
    }
    if (nativeValue instanceof MutationInvalidException) {
      return ToDafny.Error((MutationInvalidException) nativeValue);
    }
    if (nativeValue instanceof MutationLockInvalidException) {
      return ToDafny.Error((MutationLockInvalidException) nativeValue);
    }
    if (nativeValue instanceof UnexpectedStateException) {
      return ToDafny.Error((UnexpectedStateException) nativeValue);
    }
    if (nativeValue instanceof OpaqueError) {
      return ToDafny.Error((OpaqueError) nativeValue);
    }
    if (nativeValue instanceof CollectionOfErrors) {
      return ToDafny.Error((CollectionOfErrors) nativeValue);
    }
    return Error.create_Opaque(nativeValue);
  }

  public static Error Error(OpaqueError nativeValue) {
    return Error.create_Opaque(nativeValue.obj());
  }

  public static Error Error(CollectionOfErrors nativeValue) {
    DafnySequence<? extends Error> list =
      software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
        nativeValue.list(),
        ToDafny::Error,
        Error._typeDescriptor()
      );
    DafnySequence<? extends Character> message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.getMessage()
      );
    return Error.create_CollectionOfErrors(list, message);
  }

  public static ApplyMutationInput ApplyMutationInput(
    software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput nativeValue
  ) {
    MutationToken mutationToken;
    mutationToken = ToDafny.MutationToken(nativeValue.mutationToken());
    Option<Integer> pageSize;
    pageSize =
      Objects.nonNull(nativeValue.pageSize())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.pageSize()))
        : Option.create_None(TypeDescriptor.INT);
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    return new ApplyMutationInput(mutationToken, pageSize, strategy);
  }

  public static ApplyMutationOutput ApplyMutationOutput(
    software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput nativeValue
  ) {
    ApplyMutationResult result;
    result = ToDafny.ApplyMutationResult(nativeValue.result());
    DafnySequence<? extends MutatedBranchKeyItem> mutatedBranchKeyItems;
    mutatedBranchKeyItems =
      ToDafny.MutatedBranchKeyItems(nativeValue.mutatedBranchKeyItems());
    return new ApplyMutationOutput(result, mutatedBranchKeyItems);
  }

  public static CreateKeyInput CreateKeyInput(
    software.amazon.cryptography.keystoreadmin.model.CreateKeyInput nativeValue
  ) {
    Option<DafnySequence<? extends Character>> branchKeyIdentifier;
    branchKeyIdentifier =
      Objects.nonNull(nativeValue.branchKeyIdentifier())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.branchKeyIdentifier()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Byte>,
        ? extends DafnySequence<? extends Byte>
      >
    > encryptionContext;
    encryptionContext =
      (Objects.nonNull(nativeValue.encryptionContext()) &&
          nativeValue.encryptionContext().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE),
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
          ),
          software.amazon.cryptography.keystore.ToDafny.EncryptionContext(
            nativeValue.encryptionContext()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE),
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
          )
        );
    KMSIdentifier kmsArn;
    kmsArn = ToDafny.KMSIdentifier(nativeValue.kmsArn());
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    return new CreateKeyInput(
      branchKeyIdentifier,
      encryptionContext,
      kmsArn,
      strategy
    );
  }

  public static CreateKeyOutput CreateKeyOutput(
    software.amazon.cryptography.keystoreadmin.model.CreateKeyOutput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    return new CreateKeyOutput(branchKeyIdentifier);
  }

  public static InitializeMutationInput InitializeMutationInput(
    software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    Mutations mutations;
    mutations = ToDafny.Mutations(nativeValue.mutations());
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    return new InitializeMutationInput(
      branchKeyIdentifier,
      mutations,
      strategy
    );
  }

  public static InitializeMutationOutput InitializeMutationOutput(
    software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput nativeValue
  ) {
    MutationToken mutationToken;
    mutationToken = ToDafny.MutationToken(nativeValue.mutationToken());
    DafnySequence<? extends MutatedBranchKeyItem> mutatedBranchKeyItems;
    mutatedBranchKeyItems =
      ToDafny.MutatedBranchKeyItems(nativeValue.mutatedBranchKeyItems());
    return new InitializeMutationOutput(mutationToken, mutatedBranchKeyItems);
  }

  public static KeyStoreAdminConfig KeyStoreAdminConfig(
    software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig nativeValue
  ) {
    DafnySequence<? extends Character> logicalKeyStoreName;
    logicalKeyStoreName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.logicalKeyStoreName()
      );
    Storage storage;
    storage =
      software.amazon.cryptography.keystore.ToDafny.Storage(
        nativeValue.storage()
      );
    return new KeyStoreAdminConfig(logicalKeyStoreName, storage);
  }

  public static MutatedBranchKeyItem MutatedBranchKeyItem(
    software.amazon.cryptography.keystoreadmin.model.MutatedBranchKeyItem nativeValue
  ) {
    DafnySequence<? extends Character> itemType;
    itemType =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.itemType()
      );
    DafnySequence<? extends Character> description;
    description =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.description()
      );
    return new MutatedBranchKeyItem(itemType, description);
  }

  public static MutationComplete MutationComplete(
    software.amazon.cryptography.keystoreadmin.model.MutationComplete nativeValue
  ) {
    return new MutationComplete();
  }

  public static Mutations Mutations(
    software.amazon.cryptography.keystoreadmin.model.Mutations nativeValue
  ) {
    Option<DafnySequence<? extends Character>> terminalKmsArn;
    terminalKmsArn =
      Objects.nonNull(nativeValue.terminalKmsArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.terminalKmsArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > terminalEncryptionContext;
    terminalEncryptionContext =
      (Objects.nonNull(nativeValue.terminalEncryptionContext()) &&
          nativeValue.terminalEncryptionContext().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          software.amazon.cryptography.keystore.ToDafny.EncryptionContextString(
            nativeValue.terminalEncryptionContext()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    return new Mutations(terminalKmsArn, terminalEncryptionContext);
  }

  public static MutationToken MutationToken(
    software.amazon.cryptography.keystoreadmin.model.MutationToken nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    DafnySequence<? extends Byte> original;
    original =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.Original()
      );
    DafnySequence<? extends Byte> terminal;
    terminal =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.Terminal()
      );
    Option<DafnySequence<? extends Byte>> exclusiveStartKey;
    exclusiveStartKey =
      Objects.nonNull(nativeValue.ExclusiveStartKey())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.BYTE),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.ExclusiveStartKey()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
        );
    Option<DafnySequence<? extends Character>> uUID;
    uUID =
      Objects.nonNull(nativeValue.UUID())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.UUID()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    DafnySequence<? extends Character> createTime;
    createTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.CreateTime()
      );
    return new MutationToken(
      identifier,
      original,
      terminal,
      exclusiveStartKey,
      uUID,
      createTime
    );
  }

  public static VersionKeyInput VersionKeyInput(
    software.amazon.cryptography.keystoreadmin.model.VersionKeyInput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    KMSIdentifier kmsArn;
    kmsArn = ToDafny.KMSIdentifier(nativeValue.kmsArn());
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    return new VersionKeyInput(branchKeyIdentifier, kmsArn, strategy);
  }

  public static VersionKeyOutput VersionKeyOutput(
    software.amazon.cryptography.keystoreadmin.model.VersionKeyOutput nativeValue
  ) {
    return new VersionKeyOutput();
  }

  public static Error Error(KeyStoreAdminException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_KeyStoreAdminException(message);
  }

  public static Error Error(MutationConflictException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MutationConflictException(message);
  }

  public static Error Error(MutationInvalidException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MutationInvalidException(message);
  }

  public static Error Error(MutationLockInvalidException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MutationLockInvalidException(message);
  }

  public static Error Error(UnexpectedStateException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_UnexpectedStateException(message);
  }

  public static ApplyMutationResult ApplyMutationResult(
    software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult nativeValue
  ) {
    if (Objects.nonNull(nativeValue.continueMutation())) {
      return ApplyMutationResult.create_continueMutation(
        ToDafny.MutationToken(nativeValue.continueMutation())
      );
    }
    if (Objects.nonNull(nativeValue.completeMutation())) {
      return ApplyMutationResult.create_completeMutation(
        ToDafny.MutationComplete(nativeValue.completeMutation())
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult."
    );
  }

  public static KeyManagementStrategy KeyManagementStrategy(
    software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy nativeValue
  ) {
    if (Objects.nonNull(nativeValue.AwsKmsReEncrypt())) {
      return KeyManagementStrategy.create(
        software.amazon.cryptography.keystore.ToDafny.AwsKms(
          nativeValue.AwsKmsReEncrypt()
        )
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy."
    );
  }

  public static KMSIdentifier KMSIdentifier(
    software.amazon.cryptography.keystoreadmin.model.KMSIdentifier nativeValue
  ) {
    if (Objects.nonNull(nativeValue.kmsKeyArn())) {
      return KMSIdentifier.create_kmsKeyArn(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.kmsKeyArn()
        )
      );
    }
    if (Objects.nonNull(nativeValue.kmsMRKeyArn())) {
      return KMSIdentifier.create_kmsMRKeyArn(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.kmsMRKeyArn()
        )
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.KMSIdentifier."
    );
  }

  public static DafnySequence<
    ? extends MutatedBranchKeyItem
  > MutatedBranchKeyItems(
    List<
      software.amazon.cryptography.keystoreadmin.model.MutatedBranchKeyItem
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.keystoreadmin.ToDafny::MutatedBranchKeyItem,
      MutatedBranchKeyItem._typeDescriptor()
    );
  }

  public static IKeyStoreAdminClient KeyStoreAdmin(KeyStoreAdmin nativeValue) {
    return nativeValue.impl();
  }
}
