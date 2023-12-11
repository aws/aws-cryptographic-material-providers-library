// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package ACCP;

import static software.amazon.cryptography.primitives.ToDafny.Error;

import Wrappers_Compile.Result;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import javax.crypto.SecretKeyFactory;
import software.amazon.cryptography.primitives.ToNative;
import software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.internaldafny.types.HKDFProvider;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;

public class ACCPUtils {

  /** @return The determined HKDF Provider. */
  public static Result<HKDFProvider, Error> ExternCheckForAccp() {
    boolean isAccpInstalled = getSecretKeyFactory(
      DigestAlgorithm.create_SHA__256()
    )
      .is_Success();

    if (isAccpInstalled) {
      return Result.create_Success(HKDFProvider.create_ACCP());
    }
    return Result.create_Success(HKDFProvider.create_MPL());
  }

  protected static Result<SecretKeyFactory, Error> getSecretKeyFactory(
    DigestAlgorithm digestAlgorithm
  ) {
    final String nativeDigest =
      "HkdfWithHmac" +
      ToNative.DigestAlgorithm(digestAlgorithm).toString().replace("_", "");
    try {
      final SecretKeyFactory secretKeyFactory = SecretKeyFactory.getInstance(
        nativeDigest,
        "AmazonCorrettoCryptoProvider"
      );
      return Result.create_Success(secretKeyFactory);
    } catch (NoSuchAlgorithmException | NoSuchProviderException ex) {
      return Result.create_Failure(
        Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message(
              String.format(
                "ACCP does not support requested HKDF Algorithm: %s",
                nativeDigest
              )
            )
            .cause(ex)
            .build()
        )
      );
    }
  }
}
