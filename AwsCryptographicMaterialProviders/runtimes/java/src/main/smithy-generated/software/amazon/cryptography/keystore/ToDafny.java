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
import software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetricBeacon;
import software.amazon.cryptography.keystore.internaldafny.types.AwsKms;
import software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials;
import software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials;
import software.amazon.cryptography.keystore.internaldafny.types.BranchKeyType;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput;
import software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreInput;
import software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreOutput;
import software.amazon.cryptography.keystore.internaldafny.types.Discovery;
import software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable;
import software.amazon.cryptography.keystore.internaldafny.types.EncryptedHierarchicalKey;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
import software.amazon.cryptography.keystore.internaldafny.types.Error_EncryptedKeyStoreException;
import software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException;
import software.amazon.cryptography.keystore.internaldafny.types.Error_VersionRaceException;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetVersionInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetVersionOutput;
import software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient;
import software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration;
import software.amazon.cryptography.keystore.internaldafny.types.KeyManagement;
import software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig;
import software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery;
import software.amazon.cryptography.keystore.internaldafny.types.MutationLock;
import software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput;
import software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput;
import software.amazon.cryptography.keystore.internaldafny.types.Storage;
import software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionInput;
import software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionOutput;
import software.amazon.cryptography.keystore.model.CollectionOfErrors;
import software.amazon.cryptography.keystore.model.EncryptedKeyStoreException;
import software.amazon.cryptography.keystore.model.KeyStoreException;
import software.amazon.cryptography.keystore.model.OpaqueError;
import software.amazon.cryptography.keystore.model.VersionRaceException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient;
import software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient;

public class ToDafny {

  public static Error Error(RuntimeException nativeValue) {
    if (nativeValue instanceof EncryptedKeyStoreException) {
      return ToDafny.Error((EncryptedKeyStoreException) nativeValue);
    }
    if (nativeValue instanceof KeyStoreException) {
      return ToDafny.Error((KeyStoreException) nativeValue);
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
        ? Option.create_Some(ToDafny.GrantTokenList(nativeValue.grantTokens()))
        : Option.create_None();
    Option<IKMSClient> kmsClient;
    kmsClient =
      Objects.nonNull(nativeValue.kmsClient())
        ? Option.create_Some(
          software.amazon.cryptography.services.kms.internaldafny.ToDafny.TrentService(
            nativeValue.kmsClient()
          )
        )
        : Option.create_None();
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
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.beaconKey()
          )
        )
        : Option.create_None();
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Byte>
      >
    > hmacKeys;
    hmacKeys =
      (Objects.nonNull(nativeValue.hmacKeys()) &&
          nativeValue.hmacKeys().size() > 0)
        ? Option.create_Some(ToDafny.HmacKeyMap(nativeValue.hmacKeys()))
        : Option.create_None();
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
          ToDafny.EncryptionContext(nativeValue.encryptionContext())
        )
        : Option.create_None();
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

  public static DescribeEncryptedKeyStoreInput DescribeEncryptedKeyStoreInput(
    software.amazon.cryptography.keystore.model.DescribeEncryptedKeyStoreInput nativeValue
  ) {
    return new DescribeEncryptedKeyStoreInput();
  }

  public static DescribeEncryptedKeyStoreOutput DescribeEncryptedKeyStoreOutput(
    software.amazon.cryptography.keystore.model.DescribeEncryptedKeyStoreOutput nativeValue
  ) {
    DafnySequence<? extends Byte> name;
    name =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.DafnyUtf8Bytes(
        nativeValue.Name()
      );
    return new DescribeEncryptedKeyStoreOutput(name);
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
          software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny.DynamoDB_20120810(
            nativeValue.ddbClient()
          )
        )
        : Option.create_None();
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
    BranchKeyType type;
    type = ToDafny.BranchKeyType(nativeValue.Type());
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

  public static GetActiveInput GetActiveInput(
    software.amazon.cryptography.keystore.model.GetActiveInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new GetActiveInput(identifier);
  }

  public static GetActiveOutput GetActiveOutput(
    software.amazon.cryptography.keystore.model.GetActiveOutput nativeValue
  ) {
    EncryptedHierarchicalKey item;
    item = ToDafny.EncryptedHierarchicalKey(nativeValue.Item());
    return new GetActiveOutput(item);
  }

  public static GetBeaconInput GetBeaconInput(
    software.amazon.cryptography.keystore.model.GetBeaconInput nativeValue
  ) {
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    return new GetBeaconInput(identifier);
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

  public static GetBeaconOutput GetBeaconOutput(
    software.amazon.cryptography.keystore.model.GetBeaconOutput nativeValue
  ) {
    EncryptedHierarchicalKey item;
    item = ToDafny.EncryptedHierarchicalKey(nativeValue.Item());
    return new GetBeaconOutput(item);
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
    activeItem = ToDafny.EncryptedHierarchicalKey(nativeValue.activeItem());
    EncryptedHierarchicalKey beaconItem;
    beaconItem = ToDafny.EncryptedHierarchicalKey(nativeValue.beaconItem());
    Option<MutationLock> mutationLock;
    mutationLock =
      Objects.nonNull(nativeValue.mutationLock())
        ? Option.create_Some(ToDafny.MutationLock(nativeValue.mutationLock()))
        : Option.create_None();
    return new GetItemsForInitializeMutationOutput(
      activeItem,
      beaconItem,
      mutationLock
    );
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

  public static GetVersionInput GetVersionInput(
    software.amazon.cryptography.keystore.model.GetVersionInput nativeValue
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
    return new GetVersionInput(identifier, version);
  }

  public static GetVersionOutput GetVersionOutput(
    software.amazon.cryptography.keystore.model.GetVersionOutput nativeValue
  ) {
    EncryptedHierarchicalKey item;
    item = ToDafny.EncryptedHierarchicalKey(nativeValue.Item());
    return new GetVersionOutput(item);
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
        ? Option.create_Some(ToDafny.KeyManagement(nativeValue.keyManagement()))
        : Option.create_None();
    Option<DafnySequence<? extends Character>> ddbTableName;
    ddbTableName =
      Objects.nonNull(nativeValue.ddbTableName())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.ddbTableName()
          )
        )
        : Option.create_None();
    Option<DafnySequence<? extends Character>> id;
    id =
      Objects.nonNull(nativeValue.id())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.id()
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
    Option<Storage> storage;
    storage =
      Objects.nonNull(nativeValue.storage())
        ? Option.create_Some(ToDafny.Storage(nativeValue.storage()))
        : Option.create_None();
    Option<IDynamoDBClient> ddbClient;
    ddbClient =
      Objects.nonNull(nativeValue.ddbClient())
        ? Option.create_Some(
          software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny.DynamoDB_20120810(
            nativeValue.ddbClient()
          )
        )
        : Option.create_None();
    Option<IKMSClient> kmsClient;
    kmsClient =
      Objects.nonNull(nativeValue.kmsClient())
        ? Option.create_Some(
          software.amazon.cryptography.services.kms.internaldafny.ToDafny.TrentService(
            nativeValue.kmsClient()
          )
        )
        : Option.create_None();
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

  public static MutationLock MutationLock(
    software.amazon.cryptography.keystore.model.MutationLock nativeValue
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
    return new MutationLock(identifier, createTime, uUID, original, terminal);
  }

  public static QueryForVersionsInput QueryForVersionsInput(
    software.amazon.cryptography.keystore.model.QueryForVersionsInput nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> exclusiveStartKey;
    exclusiveStartKey =
      Objects.nonNull(nativeValue.exclusiveStartKey())
        ? Option.create_Some(
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
            nativeValue.exclusiveStartKey()
          )
        )
        : Option.create_None();
    DafnySequence<? extends Character> identifier;
    identifier =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.Identifier()
      );
    Integer pageSize;
    pageSize = (nativeValue.pageSize());
    return new QueryForVersionsInput(exclusiveStartKey, identifier, pageSize);
  }

  public static QueryForVersionsOutput QueryForVersionsOutput(
    software.amazon.cryptography.keystore.model.QueryForVersionsOutput nativeValue
  ) {
    DafnySequence<? extends Byte> exclusiveStartKey;
    exclusiveStartKey =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
        nativeValue.exclusiveStartKey()
      );
    DafnySequence<? extends EncryptedHierarchicalKey> items;
    items = ToDafny.EncryptedHierarchicalKeys(nativeValue.items());
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

  public static WriteCompleteMutationInput WriteCompleteMutationInput(
    software.amazon.cryptography.keystore.model.WriteCompleteMutationInput nativeValue
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
    return new WriteCompleteMutationInput(identifier, original, terminal);
  }

  public static WriteCompleteMutationOutput WriteCompleteMutationOutput(
    software.amazon.cryptography.keystore.model.WriteCompleteMutationOutput nativeValue
  ) {
    return new WriteCompleteMutationOutput();
  }

  public static WriteItemsForInitializeMutationInput WriteItemsForInitializeMutationInput(
    software.amazon.cryptography.keystore.model.WriteItemsForInitializeMutationInput nativeValue
  ) {
    EncryptedHierarchicalKey active;
    active = ToDafny.EncryptedHierarchicalKey(nativeValue.active());
    EncryptedHierarchicalKey oldActive;
    oldActive = ToDafny.EncryptedHierarchicalKey(nativeValue.oldActive());
    EncryptedHierarchicalKey version;
    version = ToDafny.EncryptedHierarchicalKey(nativeValue.version());
    EncryptedHierarchicalKey beacon;
    beacon = ToDafny.EncryptedHierarchicalKey(nativeValue.beacon());
    MutationLock mutationLock;
    mutationLock = ToDafny.MutationLock(nativeValue.mutationLock());
    return new WriteItemsForInitializeMutationInput(
      active,
      oldActive,
      version,
      beacon,
      mutationLock
    );
  }

  public static WriteItemsForInitializeMutationOutput WriteItemsForInitializeMutationOutput(
    software.amazon.cryptography.keystore.model.WriteItemsForInitializeMutationOutput nativeValue
  ) {
    return new WriteItemsForInitializeMutationOutput();
  }

  public static WriteMutatedVersionsInput WriteMutatedVersionsInput(
    software.amazon.cryptography.keystore.model.WriteMutatedVersionsInput nativeValue
  ) {
    DafnySequence<? extends EncryptedHierarchicalKey> items;
    items = ToDafny.EncryptedHierarchicalKeys(nativeValue.items());
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
    Option<Boolean> completeMutation;
    completeMutation =
      Objects.nonNull(nativeValue.CompleteMutation())
        ? Option.create_Some((nativeValue.CompleteMutation()))
        : Option.create_None();
    return new WriteMutatedVersionsInput(
      items,
      identifier,
      original,
      terminal,
      completeMutation
    );
  }

  public static WriteMutatedVersionsOutput WriteMutatedVersionsOutput(
    software.amazon.cryptography.keystore.model.WriteMutatedVersionsOutput nativeValue
  ) {
    return new WriteMutatedVersionsOutput();
  }

  public static WriteNewKeyInput WriteNewKeyInput(
    software.amazon.cryptography.keystore.model.WriteNewKeyInput nativeValue
  ) {
    EncryptedHierarchicalKey active;
    active = ToDafny.EncryptedHierarchicalKey(nativeValue.Active());
    EncryptedHierarchicalKey version;
    version = ToDafny.EncryptedHierarchicalKey(nativeValue.Version());
    EncryptedHierarchicalKey beacon;
    beacon = ToDafny.EncryptedHierarchicalKey(nativeValue.Beacon());
    return new WriteNewKeyInput(active, version, beacon);
  }

  public static WriteNewKeyOutput WriteNewKeyOutput(
    software.amazon.cryptography.keystore.model.WriteNewKeyOutput nativeValue
  ) {
    return new WriteNewKeyOutput();
  }

  public static WriteNewVersionInput WriteNewVersionInput(
    software.amazon.cryptography.keystore.model.WriteNewVersionInput nativeValue
  ) {
    EncryptedHierarchicalKey active;
    active = ToDafny.EncryptedHierarchicalKey(nativeValue.Active());
    EncryptedHierarchicalKey version;
    version = ToDafny.EncryptedHierarchicalKey(nativeValue.Version());
    EncryptedHierarchicalKey oldActive;
    oldActive = ToDafny.EncryptedHierarchicalKey(nativeValue.oldActive());
    return new WriteNewVersionInput(active, version, oldActive);
  }

  public static WriteNewVersionOutput WriteNewVersionOutput(
    software.amazon.cryptography.keystore.model.WriteNewVersionOutput nativeValue
  ) {
    return new WriteNewVersionOutput();
  }

  public static Error Error(EncryptedKeyStoreException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_EncryptedKeyStoreException(message);
  }

  public static Error Error(KeyStoreException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_KeyStoreException(message);
  }

  public static Error Error(VersionRaceException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_VersionRaceException(message);
  }

  public static BranchKeyType BranchKeyType(
    software.amazon.cryptography.keystore.model.BranchKeyType nativeValue
  ) {
    if (Objects.nonNull(nativeValue.ActiveHierarchicalSymmetricVersion())) {
      return BranchKeyType.create_ActiveHierarchicalSymmetricVersion(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.ActiveHierarchicalSymmetricVersion()
        )
      );
    }
    if (Objects.nonNull(nativeValue.HierarchicalSymmetricVersion())) {
      return BranchKeyType.create_HierarchicalSymmetricVersion(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          nativeValue.HierarchicalSymmetricVersion()
        )
      );
    }
    if (Objects.nonNull(nativeValue.ActiveHierarchicalSymmetricBeacon())) {
      return BranchKeyType.create_ActiveHierarchicalSymmetricBeacon(
        ToDafny.ActiveHierarchicalSymmetricBeacon(
          nativeValue.ActiveHierarchicalSymmetricBeacon()
        )
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystore.internaldafny.types.BranchKeyType."
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
        ToDafny.EncryptedKeyStore(nativeValue.custom())
      );
    }
    throw new IllegalArgumentException(
      "Cannot convert " +
      nativeValue +
      " to software.amazon.cryptography.keystore.internaldafny.types.Storage."
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

  public static software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore EncryptedKeyStore(
    IEncryptedKeyStore nativeValue
  ) {
    return EncryptedKeyStore.wrap(nativeValue).impl();
  }

  public static IKeyStoreClient KeyStore(KeyStore nativeValue) {
    return nativeValue.impl();
  }
}
