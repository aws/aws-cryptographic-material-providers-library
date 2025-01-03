package HMAC;

import Wrappers_Compile.Result;
import dafny.Array;
import dafny.DafnySequence;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import software.amazon.cryptography.primitives.ToDafny;
import software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;

public class HMac extends _ExternBase___default {

  private String algorithm;
  private Mac hmac;

  public static Result<HMAC.HMac, Error> Build(DigestAlgorithm digest) {
    try {
      final HMac output = new HMac(digest);
      return CreateHMacSuccess(output);
    } catch (NoSuchAlgorithmException ex) {
      final Error err = ToDafny.Error(
        AwsCryptographicPrimitivesError
          .builder()
          .message("Requested digest Algorithm is not supported.")
          .cause(ex)
          .build()
      );
      return CreateHMacFailure(err);
    }
  }

  public HMac(DigestAlgorithm digest) throws NoSuchAlgorithmException {
    if (digest.is_SHA__256()) {
      algorithm = "HmacSHA256";
    } else if (digest.is_SHA__384()) {
      algorithm = "HmacSHA384";
    } else if (digest.is_SHA__512()) {
      algorithm = "HmacSHA512";
    } else {
      throw new NoSuchAlgorithmException();
    }

    hmac = Mac.getInstance(algorithm);
  }

  public void Init(DafnySequence<? extends Byte> key) {
    final byte[] keyBytes = (byte[]) Array.unwrap(key.toArray());
    try {
      final SecretKeySpec secretKey = new SecretKeySpec(keyBytes, algorithm);
      hmac.init(secretKey);
    } catch (InvalidKeyException e) {
      // Dafny preconditions should ensure it is impossible to enter here.
      // In case this is ever not true, translate to a RuntimeException
      // which will be bubbled up.
      throw new IllegalStateException(
        "Encountered InvalidKeyException: " + e.getMessage()
      );
    }
  }

  public void BlockUpdate(DafnySequence<? extends Byte> input) {
    final byte[] inputBytes = (byte[]) Array.unwrap(input.toArray());
    hmac.update(inputBytes);
  }

  public DafnySequence<? extends Byte> GetResult() {
    final byte[] digest = hmac.doFinal();
    return DafnySequence.fromBytes(digest);
  }
}
