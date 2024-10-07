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
import software.amazon.cryptography.keystore.internaldafny.types.AwsKms;
import software.amazon.cryptography.keystore.internaldafny.types.Storage;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationLockInvalidException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAes;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAesIdentifier;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyProperities;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput;
import software.amazon.cryptography.keystoreadmin.model.CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.MutationConflictException;
import software.amazon.cryptography.keystoreadmin.model.MutationFromException;
import software.amazon.cryptography.keystoreadmin.model.MutationInvalidException;
import software.amazon.cryptography.keystoreadmin.model.MutationLockInvalidException;
import software.amazon.cryptography.keystoreadmin.model.MutationToException;
import software.amazon.cryptography.keystoreadmin.model.MutationVerificationException;
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
    if (nativeValue instanceof MutationFromException) {
      return ToDafny.Error((MutationFromException) nativeValue);
    }
    if (nativeValue instanceof MutationInvalidException) {
      return ToDafny.Error((MutationInvalidException) nativeValue);
    }
    if (nativeValue instanceof MutationLockInvalidException) {
      return ToDafny.Error((MutationLockInvalidException) nativeValue);
    }
    if (nativeValue instanceof MutationToException) {
      return ToDafny.Error((MutationToException) nativeValue);
    }
    if (nativeValue instanceof MutationVerificationException) {
      return ToDafny.Error((MutationVerificationException) nativeValue);
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
    return Error.create_Opaque(
      nativeValue,
      dafny.DafnySequence.asString(
        java.util.Objects.nonNull(nativeValue.getMessage())
          ? nativeValue.getMessage()
          : ""
      )
    );
  }

  public static Error Error(OpaqueError nativeValue) {
    return Error.create_Opaque(
      nativeValue.obj(),
      dafny.DafnySequence.asString(
        java.util.Objects.nonNull(nativeValue.altText())
          ? nativeValue.altText()
          : ""
      )
    );
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
    mutationToken = ToDafny.MutationToken(nativeValue.MutationToken());
    Option<Integer> pageSize;
    pageSize =
      Objects.nonNull(nativeValue.PageSize())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.PageSize()))
        : Option.create_None(TypeDescriptor.INT);
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.Strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.Strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    SystemKey systemKey;
    systemKey = ToDafny.SystemKey(nativeValue.SystemKey());
    return new ApplyMutationInput(mutationToken, pageSize, strategy, systemKey);
  }

  public static ApplyMutationOutput ApplyMutationOutput(
    software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput nativeValue
  ) {
    ApplyMutationResult mutationResult;
    mutationResult = ToDafny.ApplyMutationResult(nativeValue.MutationResult());
    DafnySequence<? extends MutatedBranchKeyItem> mutatedBranchKeyItems;
    mutatedBranchKeyItems =
      ToDafny.MutatedBranchKeyItems(nativeValue.MutatedBranchKeyItems());
    return new ApplyMutationOutput(mutationResult, mutatedBranchKeyItems);
  }

  public static CreateKeyInput CreateKeyInput(
    software.amazon.cryptography.keystoreadmin.model.CreateKeyInput nativeValue
  ) {
    Option<DafnySequence<? extends Character>> identifier;
    identifier =
      Objects.nonNull(nativeValue.Identifier())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.Identifier()
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
      (Objects.nonNull(nativeValue.EncryptionContext()) &&
          nativeValue.EncryptionContext().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE),
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
          ),
          software.amazon.cryptography.keystore.ToDafny.EncryptionContext(
            nativeValue.EncryptionContext()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE),
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
          )
        );
    KmsAesIdentifier kmsArn;
    kmsArn = ToDafny.KmsAesIdentifier(nativeValue.KmsArn());
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.Strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.Strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    return new CreateKeyInput(identifier, encryptionContext, kmsArn, strategy);
  }

  public static CreateKeyOutput CreateKeyOutput(
    software.amazon.cryptography.keystoreadmin.model.CreateKeyOutput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new CreateKeyOutput(identifier);
  }

  public static DescribeMutationInput DescribeMutationInput(
    software.amazon.cryptography.keystoreadmin.model.DescribeMutationInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new DescribeMutationInput(identifier);
  }

  public static DescribeMutationOutput DescribeMutationOutput(
    software.amazon.cryptography.keystoreadmin.model.DescribeMutationOutput nativeValue
  ) {
    Option<MutableBranchKeyProperities> original;
    original =
      Objects.nonNull(nativeValue.Original())
        ? Option.create_Some(
          MutableBranchKeyProperities._typeDescriptor(),
          ToDafny.MutableBranchKeyProperities(nativeValue.Original())
        )
        : Option.create_None(MutableBranchKeyProperities._typeDescriptor());
    Option<MutableBranchKeyProperities> terminal;
    terminal =
      Objects.nonNull(nativeValue.Terminal())
        ? Option.create_Some(
          MutableBranchKeyProperities._typeDescriptor(),
          ToDafny.MutableBranchKeyProperities(nativeValue.Terminal())
        )
        : Option.create_None(MutableBranchKeyProperities._typeDescriptor());
    return new DescribeMutationOutput(original, terminal);
  }

  public static InitializeMutationInput InitializeMutationInput(
    software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    Mutations mutations;
    mutations = ToDafny.Mutations(nativeValue.Mutations());
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.Strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.Strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    SystemKey systemKey;
    systemKey = ToDafny.SystemKey(nativeValue.SystemKey());
    return new InitializeMutationInput(
      identifier,
      mutations,
      strategy,
      systemKey
    );
  }

  public static InitializeMutationOutput InitializeMutationOutput(
    software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput nativeValue
  ) {
    MutationToken mutationToken;
    mutationToken = ToDafny.MutationToken(nativeValue.MutationToken());
    DafnySequence<? extends MutatedBranchKeyItem> mutatedBranchKeyItems;
    mutatedBranchKeyItems =
      ToDafny.MutatedBranchKeyItems(nativeValue.MutatedBranchKeyItems());
    InitializeMutationFlag initializeMutationFlag;
    initializeMutationFlag =
      ToDafny.InitializeMutationFlag(nativeValue.InitializeMutationFlag());
    return new InitializeMutationOutput(
      mutationToken,
      mutatedBranchKeyItems,
      initializeMutationFlag
    );
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

  public static KmsAes KmsAes(
    software.amazon.cryptography.keystoreadmin.model.KmsAes nativeValue
  ) {
    KmsAesIdentifier kmsAesIdentifier;
    kmsAesIdentifier = ToDafny.KmsAesIdentifier(nativeValue.KmsAesIdentifier());
    AwsKms awsKms;
    awsKms =
      software.amazon.cryptography.keystore.ToDafny.AwsKms(
        nativeValue.AwsKms()
      );
    return new KmsAes(kmsAesIdentifier, awsKms);
  }

  public static MutableBranchKeyProperities MutableBranchKeyProperities(
    software.amazon.cryptography.keystoreadmin.model.MutableBranchKeyProperities nativeValue
  ) {
    DafnySequence<? extends Character> kmsArn;
    kmsArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.KmsArn()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends DafnySequence<? extends Character>
    > customEncryptionContext;
    customEncryptionContext =
      software.amazon.cryptography.keystore.ToDafny.EncryptionContextString(
        nativeValue.CustomEncryptionContext()
      );
    return new MutableBranchKeyProperities(kmsArn, customEncryptionContext);
  }

  public static MutatedBranchKeyItem MutatedBranchKeyItem(
    software.amazon.cryptography.keystoreadmin.model.MutatedBranchKeyItem nativeValue
  ) {
    DafnySequence<? extends Character> itemType;
    itemType =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.ItemType()
      );
    DafnySequence<? extends Character> description;
    description =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Description()
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
      Objects.nonNull(nativeValue.TerminalKmsArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.TerminalKmsArn()
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
      (Objects.nonNull(nativeValue.TerminalEncryptionContext()) &&
          nativeValue.TerminalEncryptionContext().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          software.amazon.cryptography.keystore.ToDafny.EncryptionContextString(
            nativeValue.TerminalEncryptionContext()
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
    return new MutationToken(identifier, uUID, createTime);
  }

  public static TrustStorage TrustStorage(
    software.amazon.cryptography.keystoreadmin.model.TrustStorage nativeValue
  ) {
    return new TrustStorage();
  }

  public static VersionKeyInput VersionKeyInput(
    software.amazon.cryptography.keystoreadmin.model.VersionKeyInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    KmsAesIdentifier kmsArn;
    kmsArn = ToDafny.KmsAesIdentifier(nativeValue.KmsArn());
    Option<KeyManagementStrategy> strategy;
    strategy =
      Objects.nonNull(nativeValue.Strategy())
        ? Option.create_Some(
          KeyManagementStrategy._typeDescriptor(),
          ToDafny.KeyManagementStrategy(nativeValue.Strategy())
        )
        : Option.create_None(KeyManagementStrategy._typeDescriptor());
    return new VersionKeyInput(identifier, kmsArn, strategy);
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

  public static Error Error(MutationFromException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MutationFromException(message);
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

  public static Error Error(MutationToException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MutationToException(message);
  }

  public static Error Error(MutationVerificationException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MutationVerificationException(message);
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
    if (Objects.nonNull(nativeValue.ContinueMutation())) {
      return ApplyMutationResult.create_ContinueMutation(
        ToDafny.MutationToken(nativeValue.ContinueMutation())
      );
    }
    if (Objects.nonNull(nativeValue.CompleteMutation())) {
      return ApplyMutationResult.create_CompleteMutation(
        ToDafny.MutationComplete(nativeValue.CompleteMutation())
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult."
    );
  }

  public static InitializeMutationFlag InitializeMutationFlag(
    software.amazon.cryptography.keystoreadmin.model.InitializeMutationFlag nativeValue
  ) {
    if (Objects.nonNull(nativeValue.Created())) {
      return InitializeMutationFlag.create_Created(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.Created()
        )
      );
    }
    if (Objects.nonNull(nativeValue.Resumed())) {
      return InitializeMutationFlag.create_Resumed(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.Resumed()
        )
      );
    }
    if (Objects.nonNull(nativeValue.ResumedWithoutIndex())) {
      return InitializeMutationFlag.create_ResumedWithoutIndex(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.ResumedWithoutIndex()
        )
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag."
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

  public static KmsAesIdentifier KmsAesIdentifier(
    software.amazon.cryptography.keystoreadmin.model.KmsAesIdentifier nativeValue
  ) {
    if (Objects.nonNull(nativeValue.KmsKeyArn())) {
      return KmsAesIdentifier.create_KmsKeyArn(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.KmsKeyArn()
        )
      );
    }
    if (Objects.nonNull(nativeValue.KmsMRKeyArn())) {
      return KmsAesIdentifier.create_KmsMRKeyArn(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.KmsMRKeyArn()
        )
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsAesIdentifier."
    );
  }

  public static SystemKey SystemKey(
    software.amazon.cryptography.keystoreadmin.model.SystemKey nativeValue
  ) {
    if (Objects.nonNull(nativeValue.KmsAes())) {
      return SystemKey.create_KmsAes(ToDafny.KmsAes(nativeValue.KmsAes()));
    }
    if (Objects.nonNull(nativeValue.TrustStorage())) {
      return SystemKey.create_TrustStorage(
        ToDafny.TrustStorage(nativeValue.TrustStorage())
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey."
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
