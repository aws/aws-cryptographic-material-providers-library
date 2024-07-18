// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

import static software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion;

import Wrappers_Compile.Option;
import Wrappers_Compile.Result;
import dafny.TypeDescriptor;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.core.exception.SdkException;
import software.amazon.awssdk.services.kms.model.KmsException;
import software.amazon.cryptography.services.kms.internaldafny.ToNative;
import software.amazon.cryptography.services.kms.internaldafny.types.*;
import software.amazon.cryptography.services.kms.internaldafny.types.Error;
import software.amazon.smithy.dafny.conversion.ToDafny;

public class UnwrapGenericKmsTests {

  @Test
  public void noAccessUnwrappedFromOpaqueProperly() {
    final Result<IKMSClient, Error> kmsClient = KMSClientForRegion(
      ToDafny.Simple.CharacterSequence("us-west-2")
    );
    final String failingKeyId =
      "arn:aws:kms:us-west-2:370957321024:key/e20ac7b8-3d95-46ee-b3d5-f5dca6393945";
    Assert.assertTrue(kmsClient.is_Success());
    IKMSClient ikmsClient = kmsClient.dtor_value();
    Result<GenerateDataKeyWithoutPlaintextResponse, Error> response =
      ikmsClient.GenerateDataKeyWithoutPlaintext(
        software.amazon.cryptography.services.kms.internaldafny.ToDafny.GenerateDataKeyWithoutPlaintextRequest(
          software.amazon.awssdk.services.kms.model.GenerateDataKeyWithoutPlaintextRequest
            .builder()
            .keyId(failingKeyId)
            .build()
        )
      );
    Assert.assertTrue(response.is_Failure());
    final Exception ex = ToNative.Error(response.dtor_error());
    Assert.assertTrue(ex instanceof SdkException);
  }
}
