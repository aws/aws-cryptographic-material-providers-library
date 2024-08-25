// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin;

import Wrappers_Compile.Option;
import dafny.DafnyMap;
import dafny.DafnySequence;
import java.lang.Byte;
import java.lang.Character;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.types.Storage;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_VersionRaceException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KMSIdentifier;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KMSRelationship;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.OpaqueError;
import software.amazon.cryptography.keystoreadmin.model.VersionRaceException;
import software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient;

public class ToDafny {

  public static Error Error(RuntimeException nativeValue) {
    if (nativeValue instanceof KeyStoreAdminException) {
      return ToDafny.Error((KeyStoreAdminException) nativeValue);
    }
    if (nativeValue instanceof VersionRaceException) {
      return ToDafny.Error((VersionRaceException) nativeValue);
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

  public static CreateKeyInput CreateKeyInput(
    software.amazon.cryptography.keystoreadmin.model.CreateKeyInput nativeValue
  ) {
    Option<DafnySequence<? extends Character>> branchKeyIdentifier;
    branchKeyIdentifier =
      Objects.nonNull(nativeValue.branchKeyIdentifier())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.branchKeyIdentifier()
          )
        )
        : Option.create_None();
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
          software.amazon.cryptography.keystore.ToDafny.EncryptionContext(
            nativeValue.encryptionContext()
          )
        )
        : Option.create_None();
    KMSIdentifier kmsArn;
    kmsArn = ToDafny.KMSIdentifier(nativeValue.kmsArn());
    IKMSClient kmsClient;
    kmsClient =
      software.amazon.cryptography.services.kms.internaldafny.ToDafny.TrentService(
        nativeValue.kmsClient()
      );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(
          software.amazon.cryptography.keystore.ToDafny.GrantTokenList(
            nativeValue.grantTokens()
          )
        )
        : Option.create_None();
    return new CreateKeyInput(
      branchKeyIdentifier,
      encryptionContext,
      kmsArn,
      kmsClient,
      grantTokens
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

  public static Error Error(KeyStoreAdminException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_KeyStoreAdminException(message);
  }

  public static Error Error(VersionRaceException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_VersionRaceException(message);
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

  public static KMSRelationship KMSRelationship(
    software.amazon.cryptography.keystoreadmin.model.KMSRelationship nativeValue
  ) {
    if (Objects.nonNull(nativeValue.ReEncrypt())) {
      return KMSRelationship.create(
        software.amazon.cryptography.services.kms.internaldafny.ToDafny.TrentService(
          nativeValue.ReEncrypt()
        )
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystoreadmin.internaldafny.types.KMSRelationship."
    );
  }

  public static IKeyStoreAdminClient KeyStoreAdmin(KeyStoreAdmin nativeValue) {
    return nativeValue.impl();
  }
}
