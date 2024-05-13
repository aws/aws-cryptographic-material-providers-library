package ECDH;

import Wrappers_Compile.Result;
import software.amazon.cryptography.primitives.ToDafny;
import software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.model.OpaqueError;

public class KeyGeneration extends _ExternBase___default {

  public static Result<EccKeyPair, Error> GenerateKeyPair(
    ECDHCurveSpec ecdhCurveSpec
  ) {
    return CreateExternEccKeyGenFailure(
      ToDafny.Error(OpaqueError.builder().message("Implement me!").build())
    );
  }
}
