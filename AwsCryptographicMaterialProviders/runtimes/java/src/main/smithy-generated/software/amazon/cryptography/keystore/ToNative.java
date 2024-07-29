// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import dafny.DafnyMap;
import dafny.DafnySequence;
import java.lang.Byte;
import java.lang.Character;
import java.lang.RuntimeException;
import java.lang.String;
import java.nio.ByteBuffer;
import java.util.List;
import java.util.Map;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
import software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors;
import software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException;
import software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque;
import software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient;
import software.amazon.cryptography.keystore.model.ActiveHierarchicalSymmetricBeacon;
import software.amazon.cryptography.keystore.model.AwsKms;
import software.amazon.cryptography.keystore.model.BeaconKeyMaterials;
import software.amazon.cryptography.keystore.model.BranchKeyMaterials;
import software.amazon.cryptography.keystore.model.BranchKeyType;
import software.amazon.cryptography.keystore.model.CollectionOfErrors;
import software.amazon.cryptography.keystore.model.CreateKeyInput;
import software.amazon.cryptography.keystore.model.CreateKeyOutput;
import software.amazon.cryptography.keystore.model.CreateKeyStoreInput;
import software.amazon.cryptography.keystore.model.CreateKeyStoreOutput;
import software.amazon.cryptography.keystore.model.Discovery;
import software.amazon.cryptography.keystore.model.DynamoDBTable;
import software.amazon.cryptography.keystore.model.EncryptedHierarchicalKey;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyOutput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.model.GetKeyStoreInfoOutput;
import software.amazon.cryptography.keystore.model.GetTableNameInput;
import software.amazon.cryptography.keystore.model.GetTableNameOutput;
import software.amazon.cryptography.keystore.model.KMSConfiguration;
import software.amazon.cryptography.keystore.model.KeyManagement;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;
import software.amazon.cryptography.keystore.model.KeyStoreException;
import software.amazon.cryptography.keystore.model.MRDiscovery;
import software.amazon.cryptography.keystore.model.OpaqueError;
import software.amazon.cryptography.keystore.model.Storage;
import software.amazon.cryptography.keystore.model.VersionKeyInput;
import software.amazon.cryptography.keystore.model.VersionKeyOutput;
import software.amazon.cryptography.keystore.model.WriteNewBranchKeyVersionToKeystoreInput;
import software.amazon.cryptography.keystore.model.WriteNewBranchKeyVersionToKeystoreOutput;
import software.amazon.cryptography.keystore.model.WriteNewKeyToStoreInput;
import software.amazon.cryptography.keystore.model.WriteNewKeyToStoreOutput;

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

  public static KeyStoreException Error(Error_KeyStoreException dafnyValue) {
    KeyStoreException.Builder nativeBuilder = KeyStoreException.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static RuntimeException Error(Error dafnyValue) {
    if (dafnyValue.is_KeyStoreException()) {
      return ToNative.Error((Error_KeyStoreException) dafnyValue);
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

  public static ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon(
    software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetricBeacon dafnyValue
  ) {
    ActiveHierarchicalSymmetricBeacon.Builder nativeBuilder =
      ActiveHierarchicalSymmetricBeacon.builder();
    return nativeBuilder.build();
  }

  public static AwsKms AwsKms(
    software.amazon.cryptography.keystore.internaldafny.types.AwsKms dafnyValue
  ) {
    AwsKms.Builder nativeBuilder = AwsKms.builder();
    if (dafnyValue.dtor_grantTokens().is_Some()) {
      nativeBuilder.grantTokens(
        ToNative.GrantTokenList(dafnyValue.dtor_grantTokens().dtor_value())
      );
    }
    if (dafnyValue.dtor_kmsClient().is_Some()) {
      nativeBuilder.kmsClient(
        software.amazon.cryptography.services.kms.internaldafny.ToNative.TrentService(
          dafnyValue.dtor_kmsClient().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static BeaconKeyMaterials BeaconKeyMaterials(
    software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials dafnyValue
  ) {
    BeaconKeyMaterials.Builder nativeBuilder = BeaconKeyMaterials.builder();
    nativeBuilder.beaconKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_beaconKeyIdentifier()
      )
    );
    nativeBuilder.encryptionContext(
      ToNative.EncryptionContext(dafnyValue.dtor_encryptionContext())
    );
    if (dafnyValue.dtor_beaconKey().is_Some()) {
      nativeBuilder.beaconKey(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyValue.dtor_beaconKey().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_hmacKeys().is_Some()) {
      nativeBuilder.hmacKeys(
        ToNative.HmacKeyMap(dafnyValue.dtor_hmacKeys().dtor_value())
      );
    }
    return nativeBuilder.build();
  }

  public static BranchKeyMaterials BranchKeyMaterials(
    software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials dafnyValue
  ) {
    BranchKeyMaterials.Builder nativeBuilder = BranchKeyMaterials.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    nativeBuilder.branchKeyVersion(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.DafnyUtf8Bytes(
        dafnyValue.dtor_branchKeyVersion()
      )
    );
    nativeBuilder.encryptionContext(
      ToNative.EncryptionContext(dafnyValue.dtor_encryptionContext())
    );
    nativeBuilder.branchKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_branchKey()
      )
    );
    return nativeBuilder.build();
  }

  public static CreateKeyInput CreateKeyInput(
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput dafnyValue
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
        ToNative.EncryptionContext(
          dafnyValue.dtor_encryptionContext().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static CreateKeyOutput CreateKeyOutput(
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput dafnyValue
  ) {
    CreateKeyOutput.Builder nativeBuilder = CreateKeyOutput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    return nativeBuilder.build();
  }

  public static CreateKeyStoreInput CreateKeyStoreInput(
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput dafnyValue
  ) {
    CreateKeyStoreInput.Builder nativeBuilder = CreateKeyStoreInput.builder();
    return nativeBuilder.build();
  }

  public static CreateKeyStoreOutput CreateKeyStoreOutput(
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput dafnyValue
  ) {
    CreateKeyStoreOutput.Builder nativeBuilder = CreateKeyStoreOutput.builder();
    nativeBuilder.tableArn(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_tableArn()
      )
    );
    return nativeBuilder.build();
  }

  public static Discovery Discovery(
    software.amazon.cryptography.keystore.internaldafny.types.Discovery dafnyValue
  ) {
    Discovery.Builder nativeBuilder = Discovery.builder();
    return nativeBuilder.build();
  }

  public static DynamoDBTable DynamoDBTable(
    software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable dafnyValue
  ) {
    DynamoDBTable.Builder nativeBuilder = DynamoDBTable.builder();
    nativeBuilder.ddbTableName(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_ddbTableName()
      )
    );
    if (dafnyValue.dtor_ddbClient().is_Some()) {
      nativeBuilder.ddbClient(
        software.amazon.cryptography.services.dynamodb.internaldafny.ToNative.DynamoDB_20120810(
          dafnyValue.dtor_ddbClient().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static EncryptedHierarchicalKey EncryptedHierarchicalKey(
    software.amazon.cryptography.keystore.internaldafny.types.EncryptedHierarchicalKey dafnyValue
  ) {
    EncryptedHierarchicalKey.Builder nativeBuilder =
      EncryptedHierarchicalKey.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    nativeBuilder.Type(ToNative.BranchKeyType(dafnyValue.dtor_Type()));
    nativeBuilder.CreateTime(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_CreateTime()
      )
    );
    nativeBuilder.KmsArn(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_KmsArn()
      )
    );
    nativeBuilder.EncryptionContext(
      ToNative.EncryptionContextString(dafnyValue.dtor_EncryptionContext())
    );
    nativeBuilder.CiphertextBlob(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_CiphertextBlob()
      )
    );
    return nativeBuilder.build();
  }

  public static GetActiveBranchKeyInput GetActiveBranchKeyInput(
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput dafnyValue
  ) {
    GetActiveBranchKeyInput.Builder nativeBuilder =
      GetActiveBranchKeyInput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    return nativeBuilder.build();
  }

  public static GetActiveBranchKeyOutput GetActiveBranchKeyOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput dafnyValue
  ) {
    GetActiveBranchKeyOutput.Builder nativeBuilder =
      GetActiveBranchKeyOutput.builder();
    nativeBuilder.branchKeyMaterials(
      ToNative.BranchKeyMaterials(dafnyValue.dtor_branchKeyMaterials())
    );
    return nativeBuilder.build();
  }

  public static GetBeaconKeyInput GetBeaconKeyInput(
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput dafnyValue
  ) {
    GetBeaconKeyInput.Builder nativeBuilder = GetBeaconKeyInput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    return nativeBuilder.build();
  }

  public static GetBeaconKeyOutput GetBeaconKeyOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput dafnyValue
  ) {
    GetBeaconKeyOutput.Builder nativeBuilder = GetBeaconKeyOutput.builder();
    nativeBuilder.beaconKeyMaterials(
      ToNative.BeaconKeyMaterials(dafnyValue.dtor_beaconKeyMaterials())
    );
    return nativeBuilder.build();
  }

  public static GetBranchKeyVersionInput GetBranchKeyVersionInput(
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput dafnyValue
  ) {
    GetBranchKeyVersionInput.Builder nativeBuilder =
      GetBranchKeyVersionInput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    nativeBuilder.branchKeyVersion(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyVersion()
      )
    );
    return nativeBuilder.build();
  }

  public static GetBranchKeyVersionOutput GetBranchKeyVersionOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput dafnyValue
  ) {
    GetBranchKeyVersionOutput.Builder nativeBuilder =
      GetBranchKeyVersionOutput.builder();
    nativeBuilder.branchKeyMaterials(
      ToNative.BranchKeyMaterials(dafnyValue.dtor_branchKeyMaterials())
    );
    return nativeBuilder.build();
  }

  public static GetEncryptedActiveBranchKeyInput GetEncryptedActiveBranchKeyInput(
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput dafnyValue
  ) {
    GetEncryptedActiveBranchKeyInput.Builder nativeBuilder =
      GetEncryptedActiveBranchKeyInput.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    return nativeBuilder.build();
  }

  public static GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKeyOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput dafnyValue
  ) {
    GetEncryptedActiveBranchKeyOutput.Builder nativeBuilder =
      GetEncryptedActiveBranchKeyOutput.builder();
    nativeBuilder.Item(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Item())
    );
    return nativeBuilder.build();
  }

  public static GetEncryptedBeaconKeyInput GetEncryptedBeaconKeyInput(
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput dafnyValue
  ) {
    GetEncryptedBeaconKeyInput.Builder nativeBuilder =
      GetEncryptedBeaconKeyInput.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    return nativeBuilder.build();
  }

  public static GetEncryptedBeaconKeyOutput GetEncryptedBeaconKeyOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput dafnyValue
  ) {
    GetEncryptedBeaconKeyOutput.Builder nativeBuilder =
      GetEncryptedBeaconKeyOutput.builder();
    nativeBuilder.Item(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Item())
    );
    return nativeBuilder.build();
  }

  public static GetEncryptedBranchKeyVersionInput GetEncryptedBranchKeyVersionInput(
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput dafnyValue
  ) {
    GetEncryptedBranchKeyVersionInput.Builder nativeBuilder =
      GetEncryptedBranchKeyVersionInput.builder();
    nativeBuilder.Identifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Identifier()
      )
    );
    nativeBuilder.Version(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_Version()
      )
    );
    return nativeBuilder.build();
  }

  public static GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersionOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput dafnyValue
  ) {
    GetEncryptedBranchKeyVersionOutput.Builder nativeBuilder =
      GetEncryptedBranchKeyVersionOutput.builder();
    nativeBuilder.Item(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Item())
    );
    return nativeBuilder.build();
  }

  public static GetKeyStoreInfoOutput GetKeyStoreInfoOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput dafnyValue
  ) {
    GetKeyStoreInfoOutput.Builder nativeBuilder =
      GetKeyStoreInfoOutput.builder();
    nativeBuilder.keyStoreId(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_keyStoreId()
      )
    );
    nativeBuilder.keyStoreName(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_keyStoreName()
      )
    );
    nativeBuilder.logicalKeyStoreName(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_logicalKeyStoreName()
      )
    );
    nativeBuilder.grantTokens(
      ToNative.GrantTokenList(dafnyValue.dtor_grantTokens())
    );
    nativeBuilder.kmsConfiguration(
      ToNative.KMSConfiguration(dafnyValue.dtor_kmsConfiguration())
    );
    return nativeBuilder.build();
  }

  public static GetTableNameInput GetTableNameInput(
    software.amazon.cryptography.keystore.internaldafny.types.GetTableNameInput dafnyValue
  ) {
    GetTableNameInput.Builder nativeBuilder = GetTableNameInput.builder();
    return nativeBuilder.build();
  }

  public static GetTableNameOutput GetTableNameOutput(
    software.amazon.cryptography.keystore.internaldafny.types.GetTableNameOutput dafnyValue
  ) {
    GetTableNameOutput.Builder nativeBuilder = GetTableNameOutput.builder();
    nativeBuilder.Name(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.DafnyUtf8Bytes(
        dafnyValue.dtor_Name()
      )
    );
    return nativeBuilder.build();
  }

  public static KeyStoreConfig KeyStoreConfig(
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig dafnyValue
  ) {
    KeyStoreConfig.Builder nativeBuilder = KeyStoreConfig.builder();
    nativeBuilder.kmsConfiguration(
      ToNative.KMSConfiguration(dafnyValue.dtor_kmsConfiguration())
    );
    nativeBuilder.logicalKeyStoreName(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_logicalKeyStoreName()
      )
    );
    if (dafnyValue.dtor_keyManagement().is_Some()) {
      nativeBuilder.keyManagement(
        ToNative.KeyManagement(dafnyValue.dtor_keyManagement().dtor_value())
      );
    }
    if (dafnyValue.dtor_ddbTableName().is_Some()) {
      nativeBuilder.ddbTableName(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_ddbTableName().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_id().is_Some()) {
      nativeBuilder.id(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_id().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_grantTokens().is_Some()) {
      nativeBuilder.grantTokens(
        ToNative.GrantTokenList(dafnyValue.dtor_grantTokens().dtor_value())
      );
    }
    if (dafnyValue.dtor_storage().is_Some()) {
      nativeBuilder.storage(
        ToNative.Storage(dafnyValue.dtor_storage().dtor_value())
      );
    }
    if (dafnyValue.dtor_ddbClient().is_Some()) {
      nativeBuilder.ddbClient(
        software.amazon.cryptography.services.dynamodb.internaldafny.ToNative.DynamoDB_20120810(
          dafnyValue.dtor_ddbClient().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_kmsClient().is_Some()) {
      nativeBuilder.kmsClient(
        software.amazon.cryptography.services.kms.internaldafny.ToNative.TrentService(
          dafnyValue.dtor_kmsClient().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static MRDiscovery MRDiscovery(
    software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery dafnyValue
  ) {
    MRDiscovery.Builder nativeBuilder = MRDiscovery.builder();
    nativeBuilder.region(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_region()
      )
    );
    return nativeBuilder.build();
  }

  public static VersionKeyInput VersionKeyInput(
    software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput dafnyValue
  ) {
    VersionKeyInput.Builder nativeBuilder = VersionKeyInput.builder();
    nativeBuilder.branchKeyIdentifier(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_branchKeyIdentifier()
      )
    );
    return nativeBuilder.build();
  }

  public static VersionKeyOutput VersionKeyOutput(
    software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput dafnyValue
  ) {
    VersionKeyOutput.Builder nativeBuilder = VersionKeyOutput.builder();
    return nativeBuilder.build();
  }

  public static WriteNewBranchKeyVersionToKeystoreInput WriteNewBranchKeyVersionToKeystoreInput(
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreInput dafnyValue
  ) {
    WriteNewBranchKeyVersionToKeystoreInput.Builder nativeBuilder =
      WriteNewBranchKeyVersionToKeystoreInput.builder();
    nativeBuilder.Active(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Active())
    );
    nativeBuilder.Version(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Version())
    );
    nativeBuilder.oldActive(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_oldActive())
    );
    return nativeBuilder.build();
  }

  public static WriteNewBranchKeyVersionToKeystoreOutput WriteNewBranchKeyVersionToKeystoreOutput(
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreOutput dafnyValue
  ) {
    WriteNewBranchKeyVersionToKeystoreOutput.Builder nativeBuilder =
      WriteNewBranchKeyVersionToKeystoreOutput.builder();
    return nativeBuilder.build();
  }

  public static WriteNewKeyToStoreInput WriteNewKeyToStoreInput(
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreInput dafnyValue
  ) {
    WriteNewKeyToStoreInput.Builder nativeBuilder =
      WriteNewKeyToStoreInput.builder();
    nativeBuilder.Active(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Active())
    );
    nativeBuilder.Version(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Version())
    );
    nativeBuilder.Beacon(
      ToNative.EncryptedHierarchicalKey(dafnyValue.dtor_Beacon())
    );
    return nativeBuilder.build();
  }

  public static WriteNewKeyToStoreOutput WriteNewKeyToStoreOutput(
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreOutput dafnyValue
  ) {
    WriteNewKeyToStoreOutput.Builder nativeBuilder =
      WriteNewKeyToStoreOutput.builder();
    return nativeBuilder.build();
  }

  public static BranchKeyType BranchKeyType(
    software.amazon.cryptography.keystore.internaldafny.types.BranchKeyType dafnyValue
  ) {
    BranchKeyType.Builder nativeBuilder = BranchKeyType.builder();
    if (dafnyValue.is_ActiveHierarchicalSymmetricVersion()) {
      nativeBuilder.ActiveHierarchicalSymmetricVersion(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_ActiveHierarchicalSymmetricVersion()
        )
      );
    }
    if (dafnyValue.is_HierarchicalSymmetricVersion()) {
      nativeBuilder.HierarchicalSymmetricVersion(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_HierarchicalSymmetricVersion()
        )
      );
    }
    if (dafnyValue.is_ActiveHierarchicalSymmetricBeacon()) {
      nativeBuilder.ActiveHierarchicalSymmetricBeacon(
        ToNative.ActiveHierarchicalSymmetricBeacon(
          dafnyValue.dtor_ActiveHierarchicalSymmetricBeacon()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static KeyManagement KeyManagement(
    software.amazon.cryptography.keystore.internaldafny.types.KeyManagement dafnyValue
  ) {
    KeyManagement.Builder nativeBuilder = KeyManagement.builder();
    if (dafnyValue.is_kms()) {
      nativeBuilder.kms(ToNative.AwsKms(dafnyValue.dtor_kms()));
    }
    return nativeBuilder.build();
  }

  public static KMSConfiguration KMSConfiguration(
    software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration dafnyValue
  ) {
    KMSConfiguration.Builder nativeBuilder = KMSConfiguration.builder();
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
    if (dafnyValue.is_discovery()) {
      nativeBuilder.discovery(ToNative.Discovery(dafnyValue.dtor_discovery()));
    }
    if (dafnyValue.is_mrDiscovery()) {
      nativeBuilder.mrDiscovery(
        ToNative.MRDiscovery(dafnyValue.dtor_mrDiscovery())
      );
    }
    return nativeBuilder.build();
  }

  public static Storage Storage(
    software.amazon.cryptography.keystore.internaldafny.types.Storage dafnyValue
  ) {
    Storage.Builder nativeBuilder = Storage.builder();
    if (dafnyValue.is_ddb()) {
      nativeBuilder.ddb(ToNative.DynamoDBTable(dafnyValue.dtor_ddb()));
    }
    if (dafnyValue.is_custom()) {
      nativeBuilder.custom(
        ToNative.EncryptedKeyStore(dafnyValue.dtor_custom())
      );
    }
    return nativeBuilder.build();
  }

  public static List<String> GrantTokenList(
    DafnySequence<? extends DafnySequence<? extends Character>> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToList(
      dafnyValue,
      software.amazon.smithy.dafny.conversion.ToNative.Simple::String
    );
  }

  public static Map<String, String> EncryptionContext(
    DafnyMap<
      ? extends DafnySequence<? extends Byte>,
      ? extends DafnySequence<? extends Byte>
    > dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToMap(
      dafnyValue,
      software.amazon.smithy.dafny.conversion.ToNative.Simple::DafnyUtf8Bytes,
      software.amazon.smithy.dafny.conversion.ToNative.Simple::DafnyUtf8Bytes
    );
  }

  public static Map<String, String> EncryptionContextString(
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends DafnySequence<? extends Character>
    > dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToMap(
      dafnyValue,
      software.amazon.smithy.dafny.conversion.ToNative.Simple::String,
      software.amazon.smithy.dafny.conversion.ToNative.Simple::String
    );
  }

  public static Map<String, ByteBuffer> HmacKeyMap(
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends DafnySequence<? extends Byte>
    > dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToMap(
      dafnyValue,
      software.amazon.smithy.dafny.conversion.ToNative.Simple::String,
      software.amazon.smithy.dafny.conversion.ToNative.Simple::ByteBuffer
    );
  }

  public static IEncryptedKeyStore EncryptedKeyStore(
    software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore dafnyValue
  ) {
    if (dafnyValue instanceof EncryptedKeyStore.NativeWrapper) {
      return ((EncryptedKeyStore.NativeWrapper) dafnyValue)._impl;
    }
    return EncryptedKeyStore.wrap(dafnyValue);
  }

  public static KeyStore KeyStore(IKeyStoreClient dafnyValue) {
    return new KeyStore(dafnyValue);
  }
}
