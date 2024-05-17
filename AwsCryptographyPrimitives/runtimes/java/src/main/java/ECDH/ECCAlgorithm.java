package ECDH;

import static ECDH.KeyGeneration.SEC_P256;
import static ECDH.KeyGeneration.SEC_P384;
import static ECDH.KeyGeneration.SEC_P521;
import static ECDH.KeyGeneration.SEC_PRIME_FIELD_PREFIX;
import static ECDH.KeyGeneration.SM2;

import StandardLibraryInternal.InternalResult;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidParameterSpecException;
import org.bouncycastle.jce.ECNamedCurveTable;
import org.bouncycastle.jce.spec.ECParameterSpec;
import software.amazon.cryptography.primitives.ToDafny;
import software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;

// TODO; we cam probably refactor this enum and the SignatureAlgorithm enum in order
// to have shared functionality. We would do this by creating an ECC Curve Interface.
public enum ECCAlgorithm {
  P256(SEC_PRIME_FIELD_PREFIX + SEC_P256),
  P384(SEC_PRIME_FIELD_PREFIX + SEC_P384),
  P521(SEC_PRIME_FIELD_PREFIX + SEC_P521),
  SM2PKE(SM2);

  public final String curve;

  ECCAlgorithm(final String curve) {
    this.curve = curve;
  }

  static InternalResult<ECCAlgorithm, Error> eccAlgorithm(
    ECDHCurveSpec dtor_eccAlgorithm
  ) {
    final ECCAlgorithm namedCurveAlgorithm;

    if (dtor_eccAlgorithm.is_ECC__NIST__P256()) {
      namedCurveAlgorithm = P256;
    } else if (dtor_eccAlgorithm.is_ECC__NIST__P384()) {
      namedCurveAlgorithm = P384;
    } else if (dtor_eccAlgorithm.is_ECC__NIST__P521()) {
      namedCurveAlgorithm = P521;
    } else if (dtor_eccAlgorithm.is_SM2()) {
      namedCurveAlgorithm = SM2PKE;
    } else {
      return InternalResult.failure(
        ToDafny.Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message(
              String.format(
                "Requested Curve is not supported. Requested %s.",
                dtor_eccAlgorithm
              )
            )
            .build()
        )
      );
    }
    return InternalResult.success(namedCurveAlgorithm);
  }

  static ECParameterSpec ecParameterSpec(ECCAlgorithm algorithm)
    throws NoSuchAlgorithmException, InvalidParameterSpecException {
    return ECNamedCurveTable.getParameterSpec(algorithm.curve);
  }
}
