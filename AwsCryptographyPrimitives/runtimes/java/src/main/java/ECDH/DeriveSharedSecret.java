package ECDH;

import static ECDH.ECCAlgorithm.eccAlgorithm;
import static ECDH.ECCUtils.checkBCProvider;
import static ECDH.ECCUtils.dafnyArrayUnWrapper;
import static ECDH.KeyGeneration.SM2_KA;

import StandardLibraryInternal.InternalResult;
import Wrappers_Compile.Result;
import dafny.DafnySequence;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.X509EncodedKeySpec;
import javax.crypto.KeyAgreement;
import software.amazon.cryptography.primitives.ToDafny;
import software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey;
import software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey;
import software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;

public class DeriveSharedSecret extends _ExternBase___default {

  public static Result<
    DafnySequence<? extends Byte>,
    Error
  > CalculateSharedSecret(
    ECDHCurveSpec dtor_eccAlgorithm,
    ECCPrivateKey dtor_privateKey,
    ECCPublicKey dtro_publicKey
  ) {
    checkBCProvider();
    final byte[] privateKeyBytes = dafnyArrayUnWrapper(dtor_privateKey._pem);
    final byte[] publicKeyBytes = dafnyArrayUnWrapper(dtro_publicKey._der);

    final InternalResult<ECCAlgorithm, Error> maybeEccAlgorithm = eccAlgorithm(
      dtor_eccAlgorithm
    );
    if (maybeEccAlgorithm.isFailure()) {
      return CreateExternDerivesharedSecretError(maybeEccAlgorithm.error());
    }

    if (!maybeEccAlgorithm.value().curve.equals(SM2_KA)) {
      try {
        KeyAgreement keyAgreement = KeyAgreement.getInstance("ECDH", "BC");
        keyAgreement.init(
          ECCUtils.parsePrivateKeyEccPemBytesToPrivateKey(privateKeyBytes),
          new SecureRandom()
        );
        keyAgreement.doPhase(fromBytesPublicKey(publicKeyBytes), true);
        byte[] sharedSecret = keyAgreement.generateSecret();
        return CreateExternDerivesharedSecretSuccess(
          DafnySequence.fromBytes(sharedSecret)
        );
      } catch (Exception e) {
        return CreateExternDerivesharedSecretError(
          ToDafny.Error(
            AwsCryptographicPrimitivesError
              .builder()
              .cause(e)
              .message(e.getMessage())
              .build()
          )
        );
      }
    }
    return CreateExternDerivesharedSecretError(
      ToDafny.Error(new RuntimeException("SM2 Not yet Supported."))
    );
  }

  private static PublicKey fromBytesPublicKey(byte[] publicKeyBytes)
    throws NoSuchAlgorithmException, NoSuchProviderException, InvalidKeySpecException {
    KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");
    return keyFactory.generatePublic(new X509EncodedKeySpec(publicKeyBytes));
  }
}
