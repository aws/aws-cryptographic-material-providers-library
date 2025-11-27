// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import Wrappers_Compile.Option;
import dafny.DafnyMap;
import dafny.DafnySequence;
import dafny.TypeDescriptor;
import java.lang.Byte;
import java.lang.Character;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.lang.String;
import java.nio.ByteBuffer;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials;
import software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput;
import software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput;
import software.amazon.cryptography.keystore.internaldafny.types.Discovery;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
import software.amazon.cryptography.keystore.internaldafny.types.Error_BranchKeyCiphertextException;
import software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput;
import software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput;
import software.amazon.cryptography.keystore.internaldafny.types.HierarchyVersion;
import software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient;
import software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration;
import software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig;
import software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery;
import software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput;
import software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput;
import software.amazon.cryptography.keystore.model.BranchKeyCiphertextException;
import software.amazon.cryptography.keystore.model.CollectionOfErrors;
import software.amazon.cryptography.keystore.model.KeyStoreException;
import software.amazon.cryptography.keystore.model.OpaqueError;
import software.amazon.cryptography.keystore.model.OpaqueWithTextError;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient;
import software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient;

public class ToDafny {

  public static Error Error(RuntimeException nativeValue) {
    if (nativeValue instanceof BranchKeyCiphertextException) {
      return ToDafny.Error((BranchKeyCiphertextException) nativeValue);
    }
    if (nativeValue instanceof KeyStoreException) {
      return ToDafny.Error((KeyStoreException) nativeValue);
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
    DafnySequence<? extends Character> kmsArn;
    kmsArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.kmsArn()
      );
    DafnySequence<? extends Character> createTime;
    createTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.createTime()
      );
    HierarchyVersion hierarchyVersion;
    hierarchyVersion = ToDafny.HierarchyVersion(nativeValue.hierarchyVersion());
    return new BeaconKeyMaterials(
      beaconKeyIdentifier,
      encryptionContext,
      beaconKey,
      hmacKeys,
      kmsArn,
      createTime,
      hierarchyVersion
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
    DafnySequence<? extends Character> kmsArn;
    kmsArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.kmsArn()
      );
    DafnySequence<? extends Character> createTime;
    createTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.createTime()
      );
    HierarchyVersion hierarchyVersion;
    hierarchyVersion = ToDafny.HierarchyVersion(nativeValue.hierarchyVersion());
    return new BranchKeyMaterials(
      branchKeyIdentifier,
      branchKeyVersion,
      encryptionContext,
      branchKey,
      kmsArn,
      createTime,
      hierarchyVersion
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
    Option<HierarchyVersion> hierarchyVersion;
    hierarchyVersion =
      Objects.nonNull(nativeValue.hierarchyVersion())
        ? Option.create_Some(
          HierarchyVersion._typeDescriptor(),
          ToDafny.HierarchyVersion(nativeValue.hierarchyVersion())
        )
        : Option.create_None(HierarchyVersion._typeDescriptor());
    return new CreateKeyInput(
      branchKeyIdentifier,
      encryptionContext,
      hierarchyVersion
    );
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

  public static Discovery Discovery(
    software.amazon.cryptography.keystore.model.Discovery nativeValue
  ) {
    return new Discovery();
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

  public static KeyStoreConfig KeyStoreConfig(
    software.amazon.cryptography.keystore.model.KeyStoreConfig nativeValue
  ) {
    DafnySequence<? extends Character> ddbTableName;
    ddbTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.ddbTableName()
      );
    KMSConfiguration kmsConfiguration;
    kmsConfiguration = ToDafny.KMSConfiguration(nativeValue.kmsConfiguration());
    DafnySequence<? extends Character> logicalKeyStoreName;
    logicalKeyStoreName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.logicalKeyStoreName()
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
      ddbTableName,
      kmsConfiguration,
      logicalKeyStoreName,
      id,
      grantTokens,
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

  public static Error Error(BranchKeyCiphertextException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_BranchKeyCiphertextException(message);
  }

  public static Error Error(KeyStoreException nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_KeyStoreException(message);
  }

  public static HierarchyVersion HierarchyVersion(
    software.amazon.cryptography.keystore.model.HierarchyVersion nativeValue
  ) {
    switch (nativeValue) {
      case v1:
        {
          return HierarchyVersion.create_v1();
        }
      case v2:
        {
          return HierarchyVersion.create_v2();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.keystore.internaldafny.types.HierarchyVersion."
          );
        }
    }
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
    ? extends DafnySequence<? extends Byte>
  > HmacKeyMap(Map<String, ByteBuffer> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::ByteSequence
    );
  }

  public static IKeyStoreClient KeyStore(KeyStore nativeValue) {
    return nativeValue.impl();
  }
}
