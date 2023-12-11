// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package ACCP;

import static ACCP.ACCPUtils.getSecretKeyFactory;
import static com.amazon.corretto.crypto.provider.HkdfSpec.hkdfExpandSpec;
import static com.amazon.corretto.crypto.provider.HkdfSpec.hkdfExtractSpec;
import static com.amazon.corretto.crypto.provider.HkdfSpec.hkdfSpec;
import static software.amazon.cryptography.primitives.ToDafny.Error;

import Wrappers_Compile.Result;
// It SHOULD BE safe to reference ACCP in this class,
// as it will only be loaded if ACCPUtils determined ACCP
// is available.
import com.amazon.corretto.crypto.provider.HkdfSpec;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;
import javax.crypto.SecretKeyFactory;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput;
import software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput;
import software.amazon.cryptography.primitives.internaldafny.types.HkdfInput;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;
import software.amazon.smithy.dafny.conversion.ToDafny;

public class ACCP_HKDF {

  private static final byte[] EMPTY_ARRAY = new byte[0];

  // See ACCP's HKDF Extract in ACCP's HKDF Known Value Tests
  // for example of HKDF Extract via ACCP:
  // https://github.com/corretto/amazon-corretto-crypto-provider/blob/main/tst/com/amazon/corretto/crypto/provider/test/HkdfKatTest.java#L201-L206
  public static Result<
    dafny.DafnySequence<? extends java.lang.Byte>,
    Error
  > ExternExtract(HkdfExtractInput input) {
    //noinspection DuplicatedCode
    Result<SecretKeyFactory, Error> maybeKeyFactory =
      //= aws-encryption-sdk-specification/framework/transitive-requirements.md#hkdf-encryption-key
      // # - The hash function MUST be specified by the [algorithm suite key derivation settings](#algorithm-suites-encryption-key-derivation-settings).
      getSecretKeyFactory(input.dtor_digestAlgorithm());
    final SecretKeyFactory secretKeyFactory;
    if (maybeKeyFactory.is_Success()) {
      secretKeyFactory = maybeKeyFactory.dtor_value();
    } else {
      return Result.create_Failure(maybeKeyFactory.dtor_error());
    }
    final byte[] nativeSalt = input.dtor_salt().is_None()
      ? EMPTY_ARRAY
      : (byte[]) input.dtor_salt().dtor_value().toRawArray();
    final byte[] nativeIkm = (byte[]) input.dtor_ikm().toRawArray();
    try {
      final KeySpec hkdfExtractSpec = hkdfExtractSpec(
        nativeIkm,
        nativeSalt,
        null
      );
      final byte[] pseudoRandomKey = secretKeyFactory
        .generateSecret(hkdfExtractSpec)
        .getEncoded();
      return Result.create_Success(
        ToDafny.Simple.ByteSequence(pseudoRandomKey)
      );
    } catch (InvalidKeySpecException ex) {
      return Result.create_Failure(
        Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message("ACCP's HKDF throw an exception")
            .cause(ex)
            .build()
        )
      );
    }
  }

  // See ACCP's HKDF Expand in ACCP's HKDF Known Value Tests
  // for example of HKDF Expand via ACCP:
  // https://github.com/corretto/amazon-corretto-crypto-provider/blob/main/tst/com/amazon/corretto/crypto/provider/test/HkdfKatTest.java#L207-L209
  public static Result<
    dafny.DafnySequence<? extends java.lang.Byte>,
    Error
  > ExternExpand(HkdfExpandInput input) {
    Result<SecretKeyFactory, Error> maybeKeyFactory =
      //= aws-encryption-sdk-specification/framework/transitive-requirements.md#hkdf-encryption-key
      // # - The hash function MUST be specified by the [algorithm suite key derivation settings](#algorithm-suites-encryption-key-derivation-settings).
      getSecretKeyFactory(input.dtor_digestAlgorithm());
    final SecretKeyFactory secretKeyFactory;
    if (maybeKeyFactory.is_Success()) {
      secretKeyFactory = maybeKeyFactory.dtor_value();
    } else {
      return Result.create_Failure(maybeKeyFactory.dtor_error());
    }
    final byte[] nativePseudoRandomKey = (byte[]) input.dtor_prk().toRawArray();
    final byte[] nativeInfo = (byte[]) input.dtor_info().toRawArray();
    final int nativeKeyLength = input.dtor_expectedLength();
    try {
      final KeySpec hkdfExpandSpec = hkdfExpandSpec(
        nativePseudoRandomKey,
        nativeInfo,
        nativeKeyLength,
        null
      );
      final byte[] outputKeyingMaterial = secretKeyFactory
        .generateSecret(hkdfExpandSpec)
        .getEncoded();
      return Result.create_Success(
        ToDafny.Simple.ByteSequence(outputKeyingMaterial)
      );
    } catch (InvalidKeySpecException ex) {
      return Result.create_Failure(
        Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message("ACCP's HKDF throw an exception")
            .cause(ex)
            .build()
        )
      );
    }
  }

  public static Result<
    dafny.DafnySequence<? extends java.lang.Byte>,
    Error
  > ExternHkdf(HkdfInput input) {
    //noinspection DuplicatedCode
    Result<SecretKeyFactory, Error> maybeKeyFactory =
      //= aws-encryption-sdk-specification/framework/transitive-requirements.md#hkdf-encryption-key
      // # - The hash function MUST be specified by the [algorithm suite key derivation settings](#algorithm-suites-encryption-key-derivation-settings).
      getSecretKeyFactory(input.dtor_digestAlgorithm());
    final SecretKeyFactory secretKeyFactory;
    if (maybeKeyFactory.is_Success()) {
      secretKeyFactory = maybeKeyFactory.dtor_value();
    } else {
      return Result.create_Failure(maybeKeyFactory.dtor_error());
    }
    final byte[] nativeSalt = input.dtor_salt().is_None()
      ? EMPTY_ARRAY
      : (byte[]) input.dtor_salt().dtor_value().toRawArray();
    final byte[] nativeIkm = (byte[]) input.dtor_ikm().toRawArray();
    final byte[] nativeInfo = (byte[]) input.dtor_info().toRawArray();
    final int nativeKeyLength = input.dtor_expectedLength();
    try {
      final HkdfSpec hkdfSpec = hkdfSpec(
        nativeIkm,
        nativeSalt,
        nativeInfo,
        nativeKeyLength,
        null
      );
      final byte[] pseudoRandomKey = secretKeyFactory
        .generateSecret(hkdfSpec)
        .getEncoded();
      return Result.create_Success(
        ToDafny.Simple.ByteSequence(pseudoRandomKey)
      );
    } catch (InvalidKeySpecException ex) {
      return Result.create_Failure(
        Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message("ACCP's HKDF throw an exception")
            .cause(ex)
            .build()
        )
      );
    }
  }
}
