// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin;

import java.lang.RuntimeException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_VersionRaceException;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.model.CollectionOfErrors;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.model.KMSIdentifier;
import software.amazon.cryptography.keystoreadmin.model.KMSRelationship;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.OpaqueError;
import software.amazon.cryptography.keystoreadmin.model.VersionRaceException;

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

  public static VersionRaceException Error(
    Error_VersionRaceException dafnyValue
  ) {
    VersionRaceException.Builder nativeBuilder = VersionRaceException.builder();
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
    if (dafnyValue.is_VersionRaceException()) {
      return ToNative.Error((Error_VersionRaceException) dafnyValue);
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
    nativeBuilder.kmsClient(
      software.amazon.cryptography.services.kms.internaldafny.ToNative.TrentService(
        dafnyValue.dtor_kmsClient()
      )
    );
    if (dafnyValue.dtor_grantTokens().is_Some()) {
      nativeBuilder.grantTokens(
        software.amazon.cryptography.keystore.ToNative.GrantTokenList(
          dafnyValue.dtor_grantTokens().dtor_value()
        )
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

  public static KMSRelationship KMSRelationship(
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KMSRelationship dafnyValue
  ) {
    KMSRelationship.Builder nativeBuilder = KMSRelationship.builder();
    if (dafnyValue.is_ReEncrypt()) {
      nativeBuilder.ReEncrypt(
        software.amazon.cryptography.services.kms.internaldafny.ToNative.TrentService(
          dafnyValue.dtor_ReEncrypt()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static KeyStoreAdmin KeyStoreAdmin(IKeyStoreAdminClient dafnyValue) {
    return new KeyStoreAdmin(dafnyValue);
  }
}
