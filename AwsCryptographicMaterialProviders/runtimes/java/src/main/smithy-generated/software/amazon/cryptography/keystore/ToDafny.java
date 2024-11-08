// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import Wrappers_Compile.Option;
import dafny.DafnyMap;
import dafny.DafnySequence;
import dafny.TypeDescriptor;
import java.lang.Boolean;
import java.lang.Byte;
import java.lang.Character;
import java.lang.IllegalArgumentException;
import java.lang.Integer;
import java.lang.RuntimeException;
import java.lang.String;
import java.nio.ByteBuffer;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetric;
import software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetricBeacon;
import software.amazon.cryptography.keystore.internaldafny.types.AwsKms;
import software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials;
import software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput;
import software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.Discovery;
import software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable;
import software.amazon.cryptography.keystore.internaldafny.types.EncryptedHierarchicalKey;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
import software.amazon.cryptography.keystore.internaldafny.types.Error_AlreadyExistsConditionFailed;
import software.amazon.cryptography.keystore.internaldafny.types.Error_KeyManagementException;
import software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStorageException;
import software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException;
import software.amazon.cryptography.keystore.internaldafny.types.Error_MutationCommitmentConditionFailed;
import software.amazon.cryptography.keystore.internaldafny.types.Error_NoLongerExistsConditionFailed;
import software.amazon.cryptography.keystore.internaldafny.types.Error_OldEncConditionFailed;
import software.amazon.cryptography.keystore.internaldafny.types.Error_VersionRaceException;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.HierarchicalKeyType;
import software.amazon.cryptography.keystore.internaldafny.types.HierarchicalSymmetric;
import software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient;
import software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration;
import software.amazon.cryptography.keystore.internaldafny.types.KeyManagement;
import software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig;
import software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery;
import software.amazon.cryptography.keystore.internaldafny.types.MutationCommitment;
import software.amazon.cryptography.keystore.internaldafny.types.MutationIndex;
import software.amazon.cryptography.keystore.internaldafny.types.OverWriteEncryptedHierarchicalKey;
import software.amazon.cryptography.keystore.internaldafny.types.OverWriteMutationIndex;
import software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput;
import software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput;
import software.amazon.cryptography.keystore.internaldafny.types.Storage;
import software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationVersion;
import software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.model.AlreadyExistsConditionFailed;
import software.amazon.cryptography.keystore.model.CollectionOfErrors;
import software.amazon.cryptography.keystore.model.KeyManagementException;
import software.amazon.cryptography.keystore.model.KeyStorageException;
import software.amazon.cryptography.keystore.model.KeyStoreException;
import software.amazon.cryptography.keystore.model.MutationCommitmentConditionFailed;
import software.amazon.cryptography.keystore.model.NoLongerExistsConditionFailed;
import software.amazon.cryptography.keystore.model.OldEncConditionFailed;
import software.amazon.cryptography.keystore.model.OpaqueError;
import software.amazon.cryptography.keystore.model.OpaqueWithTextError;
import software.amazon.cryptography.keystore.model.VersionRaceException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient;
import software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient;

public class ToDafny {

  public static Error Error(RuntimeException nativeValue) {
    if (nativeValue instanceof AlreadyExistsConditionFailed) {
      return ToDafny.Error((AlreadyExistsConditionFailed) nativeValue);
    }
    if (nativeValue instanceof KeyManagementException) {
      return ToDafny.Error((KeyManagementException) nativeValue);
    }
    if (nativeValue instanceof KeyStorageException) {
      return ToDafny.Error((KeyStorageException) nativeValue);
    }
    if (nativeValue instanceof KeyStoreException) {
      return ToDafny.Error((KeyStoreException) nativeValue);
    }
    if (nativeValue instanceof MutationCommitmentConditionFailed) {
      return ToDafny.Error((MutationCommitmentConditionFailed) nativeValue);
    }
    if (nativeValue instanceof NoLongerExistsConditionFailed) {
      return ToDafny.Error((NoLongerExistsConditionFailed) nativeValue);
    }
    if (nativeValue instanceof OldEncConditionFailed) {
      return ToDafny.Error((OldEncConditionFailed) nativeValue);
    }
    if (nativeValue instanceof VersionRaceException) {
      return ToDafny.Error((VersionRaceException) nativeValue);
    }
    if (nativeValue instanceof OpaqueError) {
      return ToDafny.Error((OpaqueError) nativeValue);
    }
    if (nativeValue instanceof OpaqueWithTextError) {
      return ToDafny.Error((OpaqueWithTextError) nativeValue);
    }
    if (nativeValue instanceof CollectionOfErrors) {
      return ToDafny.Error((CollectionOfErrors) nativeValue);
    }
    return Error.create_Opaque(nativeValue);
  }

  public static Error Error(OpaqueError nativeValue) {
    return Error.create_Opaque(nativeValue.obj());
  }

  public static Error Error(OpaqueWithTextError nativeValue) {
    return Error.create_OpaqueWithText(
      nativeValue.obj(),
      dafny.DafnySequence.asString(nativeValue.objMessage())
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

  public static ActiveHierarchicalSymmetric ActiveHierarchicalSymmetric(
    software.amazon.cryptography.keystore.model.ActiveHierarchicalSymmetric nativeValue
  ) {
    DafnySequence<? extends Character> version;
    version =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Version()
      );
    return new ActiveHierarchicalSymmetric(version);
  }

  public static ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon(
    software.amazon.cryptography.keystore.model.ActiveHierarchicalSymmetricBeacon nativeValue
  ) {
    return new ActiveHierarchicalSymmetricBeacon();
  }

  public static AwsKms AwsKms(
    software.amazon.cryptography.keystore.model.AwsKms nativeValue
  ) {
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.GrantTokenList(nativeValue.grantTokens())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<IKMSClient> kmsClient;
    kmsClient =
      Objects.nonNull(nativeValue.kmsClient())
        ? Option.create_Some(
          TypeDescriptor.reference(IKMSClient.class),
          software.amazon.cryptography.services.kms.internaldafny.ToDafny.TrentService(
            nativeValue.kmsClient()
          )
        )
        : Option.create_None(TypeDescriptor.reference(IKMSClient.class));
    return new AwsKms(grantTokens, kmsClient);
  }

  public static BeaconKeyMaterials BeaconKeyMaterials(
    software.amazon.cryptography.keystore.model.BeaconKeyMaterials nativeValue
  ) {
    DafnySequence<? extends Character> beaconKeyIdentifier;
    beaconKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.beaconKeyIdentifier()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Byte>,
      ? extends DafnySequence<? extends Byte>
    > encryptionContext;
    encryptionContext =
      ToDafny.EncryptionContext(nativeValue.encryptionContext());
    Option<DafnySequence<? extends Byte>> beaconKey;
    beaconKey =
      Objects.nonNull(nativeValue.beaconKey())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.BYTE),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.beaconKey()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Byte>
      >
    > hmacKeys;
    hmacKeys =
      (Objects.nonNull(nativeValue.hmacKeys()) &&
          nativeValue.hmacKeys().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
          ),
          ToDafny.HmacKeyMap(nativeValue.hmacKeys())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
          )
        );
    return new BeaconKeyMaterials(
      beaconKeyIdentifier,
      encryptionContext,
      beaconKey,
      hmacKeys
    );
  }

  public static BranchKeyMaterials BranchKeyMaterials(
    software.amazon.cryptography.keystore.model.BranchKeyMaterials nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    DafnySequence<? extends Byte> branchKeyVersion;
    branchKeyVersion =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.DafnyUtf8Bytes(
        nativeValue.branchKeyVersion()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Byte>,
      ? extends DafnySequence<? extends Byte>
    > encryptionContext;
    encryptionContext =
      ToDafny.EncryptionContext(nativeValue.encryptionContext());
    DafnySequence<? extends Byte> branchKey;
    branchKey =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.branchKey()
      );
    return new BranchKeyMaterials(
      branchKeyIdentifier,
      branchKeyVersion,
      encryptionContext,
      branchKey
    );
  }

  public static CreateKeyInput CreateKeyInput(
    software.amazon.cryptography.keystore.model.CreateKeyInput nativeValue
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
          ToDafny.EncryptionContext(nativeValue.encryptionContext())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE),
            DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
          )
        );
    return new CreateKeyInput(branchKeyIdentifier, encryptionContext);
  }

  public static CreateKeyOutput CreateKeyOutput(
    software.amazon.cryptography.keystore.model.CreateKeyOutput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    return new CreateKeyOutput(branchKeyIdentifier);
  }

  public static CreateKeyStoreInput CreateKeyStoreInput(
    software.amazon.cryptography.keystore.model.CreateKeyStoreInput nativeValue
  ) {
    return new CreateKeyStoreInput();
  }

  public static CreateKeyStoreOutput CreateKeyStoreOutput(
    software.amazon.cryptography.keystore.model.CreateKeyStoreOutput nativeValue
  ) {
    DafnySequence<? extends Character> tableArn;
    tableArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableArn()
      );
    return new CreateKeyStoreOutput(tableArn);
  }

  public static DeleteMutationInput DeleteMutationInput(
    software.amazon.cryptography.keystore.model.DeleteMutationInput nativeValue
  ) {
    MutationCommitment mutationCommitment;
    mutationCommitment =
      ToDafny.MutationCommitment(nativeValue.MutationCommitment());
    return new DeleteMutationInput(mutationCommitment);
  }

  public static DeleteMutationOutput DeleteMutationOutput(
    software.amazon.cryptography.keystore.model.DeleteMutationOutput nativeValue
  ) {
    return new DeleteMutationOutput();
  }

  public static Discovery Discovery(
    software.amazon.cryptography.keystore.model.Discovery nativeValue
  ) {
    return new Discovery();
  }

  public static DynamoDBTable DynamoDBTable(
    software.amazon.cryptography.keystore.model.DynamoDBTable nativeValue
  ) {
    DafnySequence<? extends Character> ddbTableName;
    ddbTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.ddbTableName()
      );
    Option<IDynamoDBClient> ddbClient;
    ddbClient =
      Objects.nonNull(nativeValue.ddbClient())
        ? Option.create_Some(
          TypeDescriptor.reference(IDynamoDBClient.class),
          software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny.DynamoDB_20120810(
            nativeValue.ddbClient()
          )
        )
        : Option.create_None(TypeDescriptor.reference(IDynamoDBClient.class));
    return new DynamoDBTable(ddbTableName, ddbClient);
  }

  public static EncryptedHierarchicalKey EncryptedHierarchicalKey(
    software.amazon.cryptography.keystore.model.EncryptedHierarchicalKey nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    HierarchicalKeyType type;
    type = ToDafny.HierarchicalKeyType(nativeValue.Type());
    DafnySequence<? extends Character> createTime;
    createTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.CreateTime()
      );
    DafnySequence<? extends Character> kmsArn;
    kmsArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.KmsArn()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends DafnySequence<? extends Character>
    > encryptionContext;
    encryptionContext =
      ToDafny.EncryptionContextString(nativeValue.EncryptionContext());
    DafnySequence<? extends Byte> ciphertextBlob;
    ciphertextBlob =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.CiphertextBlob()
      );
    return new EncryptedHierarchicalKey(
      identifier,
      type,
      createTime,
      kmsArn,
      encryptionContext,
      ciphertextBlob
    );
  }

  public static GetActiveBranchKeyInput GetActiveBranchKeyInput(
    software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    return new GetActiveBranchKeyInput(branchKeyIdentifier);
  }

  public static GetActiveBranchKeyOutput GetActiveBranchKeyOutput(
    software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput nativeValue
  ) {
    BranchKeyMaterials branchKeyMaterials;
    branchKeyMaterials =
      ToDafny.BranchKeyMaterials(nativeValue.branchKeyMaterials());
    return new GetActiveBranchKeyOutput(branchKeyMaterials);
  }

  public static GetBeaconKeyInput GetBeaconKeyInput(
    software.amazon.cryptography.keystore.model.GetBeaconKeyInput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    return new GetBeaconKeyInput(branchKeyIdentifier);
  }

  public static GetBeaconKeyOutput GetBeaconKeyOutput(
    software.amazon.cryptography.keystore.model.GetBeaconKeyOutput nativeValue
  ) {
    BeaconKeyMaterials beaconKeyMaterials;
    beaconKeyMaterials =
      ToDafny.BeaconKeyMaterials(nativeValue.beaconKeyMaterials());
    return new GetBeaconKeyOutput(beaconKeyMaterials);
  }

  public static GetBranchKeyVersionInput GetBranchKeyVersionInput(
    software.amazon.cryptography.keystore.model.GetBranchKeyVersionInput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    DafnySequence<? extends Character> branchKeyVersion;
    branchKeyVersion =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyVersion()
      );
    return new GetBranchKeyVersionInput(branchKeyIdentifier, branchKeyVersion);
  }

  public static GetBranchKeyVersionOutput GetBranchKeyVersionOutput(
    software.amazon.cryptography.keystore.model.GetBranchKeyVersionOutput nativeValue
  ) {
    BranchKeyMaterials branchKeyMaterials;
    branchKeyMaterials =
      ToDafny.BranchKeyMaterials(nativeValue.branchKeyMaterials());
    return new GetBranchKeyVersionOutput(branchKeyMaterials);
  }

  public static GetEncryptedActiveBranchKeyInput GetEncryptedActiveBranchKeyInput(
    software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new GetEncryptedActiveBranchKeyInput(identifier);
  }

  public static GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKeyOutput(
    software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyOutput nativeValue
  ) {
    EncryptedHierarchicalKey item;
    item = ToDafny.EncryptedHierarchicalKey(nativeValue.Item());
    return new GetEncryptedActiveBranchKeyOutput(item);
  }

  public static GetEncryptedBeaconKeyInput GetEncryptedBeaconKeyInput(
    software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new GetEncryptedBeaconKeyInput(identifier);
  }

  public static GetEncryptedBeaconKeyOutput GetEncryptedBeaconKeyOutput(
    software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyOutput nativeValue
  ) {
    EncryptedHierarchicalKey item;
    item = ToDafny.EncryptedHierarchicalKey(nativeValue.Item());
    return new GetEncryptedBeaconKeyOutput(item);
  }

  public static GetEncryptedBranchKeyVersionInput GetEncryptedBranchKeyVersionInput(
    software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    DafnySequence<? extends Character> version;
    version =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Version()
      );
    return new GetEncryptedBranchKeyVersionInput(identifier, version);
  }

  public static GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersionOutput(
    software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionOutput nativeValue
  ) {
    EncryptedHierarchicalKey item;
    item = ToDafny.EncryptedHierarchicalKey(nativeValue.Item());
    return new GetEncryptedBranchKeyVersionOutput(item);
  }

  public static GetItemsForInitializeMutationInput GetItemsForInitializeMutationInput(
    software.amazon.cryptography.keystore.model.GetItemsForInitializeMutationInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new GetItemsForInitializeMutationInput(identifier);
  }

  public static GetItemsForInitializeMutationOutput GetItemsForInitializeMutationOutput(
    software.amazon.cryptography.keystore.model.GetItemsForInitializeMutationOutput nativeValue
  ) {
    EncryptedHierarchicalKey activeItem;
    activeItem = ToDafny.EncryptedHierarchicalKey(nativeValue.ActiveItem());
    EncryptedHierarchicalKey beaconItem;
    beaconItem = ToDafny.EncryptedHierarchicalKey(nativeValue.BeaconItem());
    Option<MutationCommitment> mutationCommitment;
    mutationCommitment =
      Objects.nonNull(nativeValue.MutationCommitment())
        ? Option.create_Some(
          MutationCommitment._typeDescriptor(),
          ToDafny.MutationCommitment(nativeValue.MutationCommitment())
        )
        : Option.create_None(MutationCommitment._typeDescriptor());
    Option<MutationIndex> mutationIndex;
    mutationIndex =
      Objects.nonNull(nativeValue.MutationIndex())
        ? Option.create_Some(
          MutationIndex._typeDescriptor(),
          ToDafny.MutationIndex(nativeValue.MutationIndex())
        )
        : Option.create_None(MutationIndex._typeDescriptor());
    return new GetItemsForInitializeMutationOutput(
      activeItem,
      beaconItem,
      mutationCommitment,
      mutationIndex
    );
  }

  public static GetKeyStorageInfoInput GetKeyStorageInfoInput(
    software.amazon.cryptography.keystore.model.GetKeyStorageInfoInput nativeValue
  ) {
    return new GetKeyStorageInfoInput();
  }

  public static GetKeyStorageInfoOutput GetKeyStorageInfoOutput(
    software.amazon.cryptography.keystore.model.GetKeyStorageInfoOutput nativeValue
  ) {
    DafnySequence<? extends Byte> name;
    name =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.DafnyUtf8Bytes(
        nativeValue.Name()
      );
    DafnySequence<? extends Byte> logicalName;
    logicalName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.DafnyUtf8Bytes(
        nativeValue.LogicalName()
      );
    return new GetKeyStorageInfoOutput(name, logicalName);
  }

  public static GetKeyStoreInfoOutput GetKeyStoreInfoOutput(
    software.amazon.cryptography.keystore.model.GetKeyStoreInfoOutput nativeValue
  ) {
    DafnySequence<? extends Character> keyStoreId;
    keyStoreId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyStoreId()
      );
    DafnySequence<? extends Character> keyStoreName;
    keyStoreName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.keyStoreName()
      );
    DafnySequence<? extends Character> logicalKeyStoreName;
    logicalKeyStoreName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.logicalKeyStoreName()
      );
    DafnySequence<? extends DafnySequence<? extends Character>> grantTokens;
    grantTokens = ToDafny.GrantTokenList(nativeValue.grantTokens());
    KMSConfiguration kmsConfiguration;
    kmsConfiguration = ToDafny.KMSConfiguration(nativeValue.kmsConfiguration());
    return new GetKeyStoreInfoOutput(
      keyStoreId,
      keyStoreName,
      logicalKeyStoreName,
      grantTokens,
      kmsConfiguration
    );
  }

  public static GetMutationInput GetMutationInput(
    software.amazon.cryptography.keystore.model.GetMutationInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new GetMutationInput(identifier);
  }

  public static GetMutationOutput GetMutationOutput(
    software.amazon.cryptography.keystore.model.GetMutationOutput nativeValue
  ) {
    Option<MutationCommitment> mutationCommitment;
    mutationCommitment =
      Objects.nonNull(nativeValue.MutationCommitment())
        ? Option.create_Some(
          MutationCommitment._typeDescriptor(),
          ToDafny.MutationCommitment(nativeValue.MutationCommitment())
        )
        : Option.create_None(MutationCommitment._typeDescriptor());
    Option<MutationIndex> mutationIndex;
    mutationIndex =
      Objects.nonNull(nativeValue.MutationIndex())
        ? Option.create_Some(
          MutationIndex._typeDescriptor(),
          ToDafny.MutationIndex(nativeValue.MutationIndex())
        )
        : Option.create_None(MutationIndex._typeDescriptor());
    return new GetMutationOutput(mutationCommitment, mutationIndex);
  }

  public static HierarchicalSymmetric HierarchicalSymmetric(
    software.amazon.cryptography.keystore.model.HierarchicalSymmetric nativeValue
  ) {
    DafnySequence<? extends Character> version;
    version =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Version()
      );
    return new HierarchicalSymmetric(version);
  }

  public static KeyStoreConfig KeyStoreConfig(
    software.amazon.cryptography.keystore.model.KeyStoreConfig nativeValue
  ) {
    KMSConfiguration kmsConfiguration;
    kmsConfiguration = ToDafny.KMSConfiguration(nativeValue.kmsConfiguration());
    DafnySequence<? extends Character> logicalKeyStoreName;
    logicalKeyStoreName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.logicalKeyStoreName()
      );
    Option<KeyManagement> keyManagement;
    keyManagement =
      Objects.nonNull(nativeValue.keyManagement())
        ? Option.create_Some(
          KeyManagement._typeDescriptor(),
          ToDafny.KeyManagement(nativeValue.keyManagement())
        )
        : Option.create_None(KeyManagement._typeDescriptor());
    Option<DafnySequence<? extends Character>> ddbTableName;
    ddbTableName =
      Objects.nonNull(nativeValue.ddbTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.ddbTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> id;
    id =
      Objects.nonNull(nativeValue.id())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.id()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > grantTokens;
    grantTokens =
      (Objects.nonNull(nativeValue.grantTokens()) &&
          nativeValue.grantTokens().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.GrantTokenList(nativeValue.grantTokens())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<Storage> storage;
    storage =
      Objects.nonNull(nativeValue.storage())
        ? Option.create_Some(
          Storage._typeDescriptor(),
          ToDafny.Storage(nativeValue.storage())
        )
        : Option.create_None(Storage._typeDescriptor());
    Option<IDynamoDBClient> ddbClient;
    ddbClient =
      Objects.nonNull(nativeValue.ddbClient())
        ? Option.create_Some(
          TypeDescriptor.reference(IDynamoDBClient.class),
          software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny.DynamoDB_20120810(
            nativeValue.ddbClient()
          )
        )
        : Option.create_None(TypeDescriptor.reference(IDynamoDBClient.class));
    Option<IKMSClient> kmsClient;
    kmsClient =
      Objects.nonNull(nativeValue.kmsClient())
        ? Option.create_Some(
          TypeDescriptor.reference(IKMSClient.class),
          software.amazon.cryptography.services.kms.internaldafny.ToDafny.TrentService(
            nativeValue.kmsClient()
          )
        )
        : Option.create_None(TypeDescriptor.reference(IKMSClient.class));
    return new KeyStoreConfig(
      kmsConfiguration,
      logicalKeyStoreName,
      keyManagement,
      ddbTableName,
      id,
      grantTokens,
      storage,
      ddbClient,
      kmsClient
    );
  }

  public static MRDiscovery MRDiscovery(
    software.amazon.cryptography.keystore.model.MRDiscovery nativeValue
  ) {
    DafnySequence<? extends Character> region;
    region =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.region()
      );
    return new MRDiscovery(region);
  }

  public static MutationCommitment MutationCommitment(
    software.amazon.cryptography.keystore.model.MutationCommitment nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    DafnySequence<? extends Character> createTime;
    createTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.CreateTime()
      );
    DafnySequence<? extends Character> uUID;
    uUID =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.UUID()
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
    DafnySequence<? extends Byte> input;
    input =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.Input()
      );
    DafnySequence<? extends Byte> ciphertextBlob;
    ciphertextBlob =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.CiphertextBlob()
      );
    return new MutationCommitment(
      identifier,
      createTime,
      uUID,
      original,
      terminal,
      input,
      ciphertextBlob
    );
  }

  public static MutationIndex MutationIndex(
    software.amazon.cryptography.keystore.model.MutationIndex nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    DafnySequence<? extends Character> createTime;
    createTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.CreateTime()
      );
    DafnySequence<? extends Character> uUID;
    uUID =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.UUID()
      );
    DafnySequence<? extends Byte> pageIndex;
    pageIndex =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.PageIndex()
      );
    DafnySequence<? extends Byte> ciphertextBlob;
    ciphertextBlob =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.CiphertextBlob()
      );
    return new MutationIndex(
      identifier,
      createTime,
      uUID,
      pageIndex,
      ciphertextBlob
    );
  }

  public static OverWriteEncryptedHierarchicalKey OverWriteEncryptedHierarchicalKey(
    software.amazon.cryptography.keystore.model.OverWriteEncryptedHierarchicalKey nativeValue
  ) {
    EncryptedHierarchicalKey item;
    item = ToDafny.EncryptedHierarchicalKey(nativeValue.Item());
    EncryptedHierarchicalKey old;
    old = ToDafny.EncryptedHierarchicalKey(nativeValue.Old());
    return new OverWriteEncryptedHierarchicalKey(item, old);
  }

  public static OverWriteMutationIndex OverWriteMutationIndex(
    software.amazon.cryptography.keystore.model.OverWriteMutationIndex nativeValue
  ) {
    MutationIndex index;
    index = ToDafny.MutationIndex(nativeValue.Index());
    MutationIndex old;
    old = ToDafny.MutationIndex(nativeValue.Old());
    return new OverWriteMutationIndex(index, old);
  }

  public static QueryForVersionsInput QueryForVersionsInput(
    software.amazon.cryptography.keystore.model.QueryForVersionsInput nativeValue
  ) {
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
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    Integer pageSize;
    pageSize = (nativeValue.PageSize());
    return new QueryForVersionsInput(exclusiveStartKey, identifier, pageSize);
  }

  public static QueryForVersionsOutput QueryForVersionsOutput(
    software.amazon.cryptography.keystore.model.QueryForVersionsOutput nativeValue
  ) {
    DafnySequence<? extends Byte> exclusiveStartKey;
    exclusiveStartKey =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.ExclusiveStartKey()
      );
    DafnySequence<? extends EncryptedHierarchicalKey> items;
    items = ToDafny.EncryptedHierarchicalKeys(nativeValue.Items());
    return new QueryForVersionsOutput(exclusiveStartKey, items);
  }

  public static VersionKeyInput VersionKeyInput(
    software.amazon.cryptography.keystore.model.VersionKeyInput nativeValue
  ) {
    DafnySequence<? extends Character> branchKeyIdentifier;
    branchKeyIdentifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.branchKeyIdentifier()
      );
    return new VersionKeyInput(branchKeyIdentifier);
  }

  public static VersionKeyOutput VersionKeyOutput(
    software.amazon.cryptography.keystore.model.VersionKeyOutput nativeValue
  ) {
    return new VersionKeyOutput();
  }

  public static WriteAtomicMutationInput WriteAtomicMutationInput(
    software.amazon.cryptography.keystore.model.WriteAtomicMutationInput nativeValue
  ) {
    OverWriteEncryptedHierarchicalKey active;
    active = ToDafny.OverWriteEncryptedHierarchicalKey(nativeValue.Active());
    WriteInitializeMutationVersion version;
    version = ToDafny.WriteInitializeMutationVersion(nativeValue.Version());
    OverWriteEncryptedHierarchicalKey beacon;
    beacon = ToDafny.OverWriteEncryptedHierarchicalKey(nativeValue.Beacon());
    DafnySequence<? extends OverWriteEncryptedHierarchicalKey> items;
    items = ToDafny.OverWriteEncryptedHierarchicalKeys(nativeValue.Items());
    return new WriteAtomicMutationInput(active, version, beacon, items);
  }

  public static WriteAtomicMutationOutput WriteAtomicMutationOutput(
    software.amazon.cryptography.keystore.model.WriteAtomicMutationOutput nativeValue
  ) {
    return new WriteAtomicMutationOutput();
  }

  public static WriteInitializeMutationInput WriteInitializeMutationInput(
    software.amazon.cryptography.keystore.model.WriteInitializeMutationInput nativeValue
  ) {
    OverWriteEncryptedHierarchicalKey active;
    active = ToDafny.OverWriteEncryptedHierarchicalKey(nativeValue.Active());
    WriteInitializeMutationVersion version;
    version = ToDafny.WriteInitializeMutationVersion(nativeValue.Version());
    OverWriteEncryptedHierarchicalKey beacon;
    beacon = ToDafny.OverWriteEncryptedHierarchicalKey(nativeValue.Beacon());
    MutationCommitment mutationCommitment;
    mutationCommitment =
      ToDafny.MutationCommitment(nativeValue.MutationCommitment());
    MutationIndex mutationIndex;
    mutationIndex = ToDafny.MutationIndex(nativeValue.MutationIndex());
    return new WriteInitializeMutationInput(
      active,
      version,
      beacon,
      mutationCommitment,
      mutationIndex
    );
  }

  public static WriteInitializeMutationOutput WriteInitializeMutationOutput(
    software.amazon.cryptography.keystore.model.WriteInitializeMutationOutput nativeValue
  ) {
    return new WriteInitializeMutationOutput();
  }

  public static WriteMutatedVersionsInput WriteMutatedVersionsInput(
    software.amazon.cryptography.keystore.model.WriteMutatedVersionsInput nativeValue
  ) {
    DafnySequence<? extends OverWriteEncryptedHierarchicalKey> items;
    items = ToDafny.OverWriteEncryptedHierarchicalKeys(nativeValue.Items());
    MutationCommitment mutationCommitment;
    mutationCommitment =
      ToDafny.MutationCommitment(nativeValue.MutationCommitment());
    OverWriteMutationIndex mutationIndex;
    mutationIndex = ToDafny.OverWriteMutationIndex(nativeValue.MutationIndex());
    Boolean endMutation;
    endMutation = (nativeValue.EndMutation());
    return new WriteMutatedVersionsInput(
      items,
      mutationCommitment,
      mutationIndex,
      endMutation
    );
  }

  public static WriteMutatedVersionsOutput WriteMutatedVersionsOutput(
    software.amazon.cryptography.keystore.model.WriteMutatedVersionsOutput nativeValue
  ) {
    return new WriteMutatedVersionsOutput();
  }

  public static WriteMutationIndexInput WriteMutationIndexInput(
    software.amazon.cryptography.keystore.model.WriteMutationIndexInput nativeValue
  ) {
    MutationCommitment mutationCommitment;
    mutationCommitment =
      ToDafny.MutationCommitment(nativeValue.MutationCommitment());
    MutationIndex mutationIndex;
    mutationIndex = ToDafny.MutationIndex(nativeValue.MutationIndex());
    return new WriteMutationIndexInput(mutationCommitment, mutationIndex);
  }

  public static WriteMutationIndexOutput WriteMutationIndexOutput(
    software.amazon.cryptography.keystore.model.WriteMutationIndexOutput nativeValue
  ) {
    return new WriteMutationIndexOutput();
  }

  public static WriteNewEncryptedBranchKeyInput WriteNewEncryptedBranchKeyInput(
    software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyInput nativeValue
  ) {
    EncryptedHierarchicalKey active;
    active = ToDafny.EncryptedHierarchicalKey(nativeValue.Active());
    EncryptedHierarchicalKey version;
    version = ToDafny.EncryptedHierarchicalKey(nativeValue.Version());
    EncryptedHierarchicalKey beacon;
    beacon = ToDafny.EncryptedHierarchicalKey(nativeValue.Beacon());
    return new WriteNewEncryptedBranchKeyInput(active, version, beacon);
  }

  public static WriteNewEncryptedBranchKeyOutput WriteNewEncryptedBranchKeyOutput(
    software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyOutput nativeValue
  ) {
    return new WriteNewEncryptedBranchKeyOutput();
  }

  public static WriteNewEncryptedBranchKeyVersionInput WriteNewEncryptedBranchKeyVersionInput(
    software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyVersionInput nativeValue
  ) {
    OverWriteEncryptedHierarchicalKey active;
    active = ToDafny.OverWriteEncryptedHierarchicalKey(nativeValue.Active());
    EncryptedHierarchicalKey version;
    version = ToDafny.EncryptedHierarchicalKey(nativeValue.Version());
    return new WriteNewEncryptedBranchKeyVersionInput(active, version);
  }

  public static WriteNewEncryptedBranchKeyVersionOutput WriteNewEncryptedBranchKeyVersionOutput(
    software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyVersionOutput nativeValue
  ) {
    return new WriteNewEncryptedBranchKeyVersionOutput();
  }

  public static Error Error(AlreadyExistsConditionFailed nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_AlreadyExistsConditionFailed(message);
  }

  public static Error Error(KeyManagementException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_KeyManagementException(message);
  }

  public static Error Error(KeyStorageException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_KeyStorageException(message);
  }

  public static Error Error(KeyStoreException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_KeyStoreException(message);
  }

  public static Error Error(MutationCommitmentConditionFailed nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MutationCommitmentConditionFailed(message);
  }

  public static Error Error(NoLongerExistsConditionFailed nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_NoLongerExistsConditionFailed(message);
  }

  public static Error Error(OldEncConditionFailed nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_OldEncConditionFailed(message);
  }

  public static Error Error(VersionRaceException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_VersionRaceException(message);
  }

  public static HierarchicalKeyType HierarchicalKeyType(
    software.amazon.cryptography.keystore.model.HierarchicalKeyType nativeValue
  ) {
    if (Objects.nonNull(nativeValue.ActiveHierarchicalSymmetricVersion())) {
      return HierarchicalKeyType.create_ActiveHierarchicalSymmetricVersion(
        ToDafny.ActiveHierarchicalSymmetric(
          nativeValue.ActiveHierarchicalSymmetricVersion()
        )
      );
    }
    if (Objects.nonNull(nativeValue.HierarchicalSymmetricVersion())) {
      return HierarchicalKeyType.create_HierarchicalSymmetricVersion(
        ToDafny.HierarchicalSymmetric(
          nativeValue.HierarchicalSymmetricVersion()
        )
      );
    }
    if (Objects.nonNull(nativeValue.ActiveHierarchicalSymmetricBeacon())) {
      return HierarchicalKeyType.create_ActiveHierarchicalSymmetricBeacon(
        ToDafny.ActiveHierarchicalSymmetricBeacon(
          nativeValue.ActiveHierarchicalSymmetricBeacon()
        )
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystore.internaldafny.types.HierarchicalKeyType."
    );
  }

  public static KeyManagement KeyManagement(
    software.amazon.cryptography.keystore.model.KeyManagement nativeValue
  ) {
    if (Objects.nonNull(nativeValue.kms())) {
      return KeyManagement.create(ToDafny.AwsKms(nativeValue.kms()));
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystore.internaldafny.types.KeyManagement."
    );
  }

  public static KMSConfiguration KMSConfiguration(
    software.amazon.cryptography.keystore.model.KMSConfiguration nativeValue
  ) {
    if (Objects.nonNull(nativeValue.kmsKeyArn())) {
      return KMSConfiguration.create_kmsKeyArn(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.kmsKeyArn()
        )
      );
    }
    if (Objects.nonNull(nativeValue.kmsMRKeyArn())) {
      return KMSConfiguration.create_kmsMRKeyArn(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.kmsMRKeyArn()
        )
      );
    }
    if (Objects.nonNull(nativeValue.discovery())) {
      return KMSConfiguration.create_discovery(
        ToDafny.Discovery(nativeValue.discovery())
      );
    }
    if (Objects.nonNull(nativeValue.mrDiscovery())) {
      return KMSConfiguration.create_mrDiscovery(
        ToDafny.MRDiscovery(nativeValue.mrDiscovery())
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration."
    );
  }

  public static Storage Storage(
    software.amazon.cryptography.keystore.model.Storage nativeValue
  ) {
    if (Objects.nonNull(nativeValue.ddb())) {
      return Storage.create_ddb(ToDafny.DynamoDBTable(nativeValue.ddb()));
    }
    if (Objects.nonNull(nativeValue.custom())) {
      return Storage.create_custom(
        ToDafny.KeyStorageInterface(nativeValue.custom())
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystore.internaldafny.types.Storage."
    );
  }

  public static WriteInitializeMutationVersion WriteInitializeMutationVersion(
    software.amazon.cryptography.keystore.model.WriteInitializeMutationVersion nativeValue
  ) {
    if (Objects.nonNull(nativeValue.rotate())) {
      return WriteInitializeMutationVersion.create_rotate(
        ToDafny.EncryptedHierarchicalKey(nativeValue.rotate())
      );
    }
    if (Objects.nonNull(nativeValue.mutate())) {
      return WriteInitializeMutationVersion.create_mutate(
        ToDafny.OverWriteEncryptedHierarchicalKey(nativeValue.mutate())
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationVersion."
    );
  }

  public static DafnySequence<
    ? extends EncryptedHierarchicalKey
  > EncryptedHierarchicalKeys(
    List<
      software.amazon.cryptography.keystore.model.EncryptedHierarchicalKey
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.keystore.ToDafny::EncryptedHierarchicalKey,
      EncryptedHierarchicalKey._typeDescriptor()
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

  public static DafnySequence<
    ? extends OverWriteEncryptedHierarchicalKey
  > OverWriteEncryptedHierarchicalKeys(
    List<
      software.amazon.cryptography.keystore.model.OverWriteEncryptedHierarchicalKey
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.keystore.ToDafny::OverWriteEncryptedHierarchicalKey,
      OverWriteEncryptedHierarchicalKey._typeDescriptor()
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Byte>,
    ? extends DafnySequence<? extends Byte>
  > EncryptionContext(Map<String, String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::DafnyUtf8Bytes,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::DafnyUtf8Bytes
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends DafnySequence<? extends Character>
  > EncryptionContextString(Map<String, String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends DafnySequence<? extends Byte>
  > HmacKeyMap(Map<String, ByteBuffer> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::ByteSequence
    );
  }

  public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface KeyStorageInterface(
    IKeyStorageInterface nativeValue
  ) {
    return KeyStorageInterface.wrap(nativeValue).impl();
  }

  public static IKeyStoreClient KeyStore(KeyStore nativeValue) {
    return nativeValue.impl();
  }
}
