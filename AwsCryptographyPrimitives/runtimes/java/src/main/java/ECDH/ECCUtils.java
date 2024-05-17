package ECDH;

import static ECDH.ECCAlgorithm.eccAlgorithm;

import StandardLibraryInternal.InternalResult;
import Wrappers_Compile.Result;
import dafny.Array;
import dafny.DafnySequence;
import java.math.BigInteger;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.PublicKey;
import java.security.Security;
import java.security.interfaces.ECPublicKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.X509EncodedKeySpec;
import org.bouncycastle.crypto.params.ECDomainParameters;
import org.bouncycastle.crypto.params.ECPrivateKeyParameters;
import org.bouncycastle.jce.ECNamedCurveTable;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.jce.spec.ECParameterSpec;
import org.bouncycastle.jce.spec.ECPublicKeySpec;
import org.bouncycastle.math.ec.ECCurve;
import org.bouncycastle.math.ec.ECPoint;
import software.amazon.cryptography.primitives.ToDafny;
import software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;

public class ECCUtils extends _ExternBase___default {

  public static Result<DafnySequence<? extends Byte>, Error> GetPublicKey(
    ECDHCurveSpec dtor_eccAlgorithm,
    DafnySequence<? extends Byte> dtor_privateKey
  ) {
    checkBCProvider();
    final InternalResult<ECCAlgorithm, Error> maybeEccAlgorithm = eccAlgorithm(
      dtor_eccAlgorithm
    );
    if (maybeEccAlgorithm.isFailure()) {
      return CreateExternGetPublicKeyFromPrivateError(
        maybeEccAlgorithm.error()
      );
    }

    if (!maybeEccAlgorithm.value().curve.equals("SM2PKE")) {
      final ECPublicKey publicKey;
      try {
        final byte[] privateKeyBytes = dafnyArrayUnWrapper(dtor_privateKey);
        final ECParameterSpec ecParameterSpec = ECCAlgorithm.ecParameterSpec(
          maybeEccAlgorithm.value()
        );
        final ECDomainParameters domainParameters = new ECDomainParameters(
          ecParameterSpec.getCurve(),
          ecParameterSpec.getG(),
          ecParameterSpec.getN()
        );

        final ECPrivateKeyParameters privateKeySpec =
          new ECPrivateKeyParameters(
            new BigInteger(privateKeyBytes),
            domainParameters
          );

        final ECPoint Q = ecParameterSpec
          .getG()
          .multiply(privateKeySpec.getD());
        final ECPublicKeySpec publicKeySpec = new ECPublicKeySpec(
          Q,
          ecParameterSpec
        );

        final KeyFactory keyFactory = KeyFactory.getInstance(
          KeyGeneration.ELLIPTIC_CURVE_ALGORITHM,
          "BC"
        );
        publicKey = (ECPublicKey) keyFactory.generatePublic(publicKeySpec);

        return CreateExternGetPublicKeyFromPrivateSuccess(
          DafnySequence.fromBytes(publicKey.getEncoded())
        );
      } catch (Exception e) {
        return CreateExternGetPublicKeyFromPrivateError(
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
    // TODO SM2
    return CreateExternGetPublicKeyFromPrivateError(
      ToDafny.Error(new RuntimeException("SM2 Not yet Supported."))
    );
  }

  public static Result<Boolean, Error> ValidatePublicKey(
    ECDHCurveSpec dtor_eccAlgorithm,
    DafnySequence<? extends Byte> dtor_privateKey,
    DafnySequence<? extends Byte> dtro_publicKey
  ) {
    checkBCProvider();
    final byte[] privateKeyBytes = dafnyArrayUnWrapper(dtor_privateKey);
    final byte[] publicKeyBytes = dafnyArrayUnWrapper(dtro_publicKey);

    final InternalResult<ECCAlgorithm, Error> maybeEccAlgorithm = eccAlgorithm(
      dtor_eccAlgorithm
    );
    if (maybeEccAlgorithm.isFailure()) {
      return CreateExternValidatePublicKeyError(maybeEccAlgorithm.error());
    }

    if (!maybeEccAlgorithm.value().curve.equals("SM2PKE")) {
      try {
        BigInteger s = new BigInteger(privateKeyBytes);
        final ECParameterSpec ecParameterSpec = ECCAlgorithm.ecParameterSpec(
          maybeEccAlgorithm.value()
        );
        final boolean validPrivateKey = ValidatePrivateKeyOnCurve(
          s,
          ecParameterSpec
        );
        final boolean validPublicKey = ValidatePublicKeyOnCurve(
          publicKeyBytes,
          maybeEccAlgorithm.value()
        );

        return CreateExternValidatePublicKeySuccess(
          validPublicKey && validPrivateKey
        );
      } catch (Exception e) {
        return CreateExternValidatePublicKeyError(
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
    return CreateExternValidatePublicKeyError(
      ToDafny.Error(new RuntimeException("SM2 Not yet Supported."))
    );
  }

  static boolean ValidatePrivateKeyOnCurve(
    BigInteger privateKey,
    ECParameterSpec genParameterSpec
  ) {
    BigInteger n = genParameterSpec.getN();
    if (
      privateKey.compareTo(BigInteger.ONE) < 0 || privateKey.compareTo(n) >= 0
    ) {
      return false;
    }

    ECPoint G = genParameterSpec.getG();
    ECPoint Q = G.multiply(privateKey);

    return Q.isInfinity() || Q.multiply(n).isInfinity();
  }

  static boolean ValidatePublicKeyOnCurve(
    byte[] publicKeyBytes,
    ECCAlgorithm ecParameterSpec
  )
    throws NoSuchAlgorithmException, InvalidKeySpecException, NoSuchProviderException, IllegalArgumentException {
    KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");
    PublicKey publicKey = keyFactory.generatePublic(
      new X509EncodedKeySpec(publicKeyBytes)
    );
    ECParameterSpec spec = ECNamedCurveTable.getParameterSpec(
      ecParameterSpec.curve
    );
    ECCurve ecCurve = spec.getCurve();
    org.bouncycastle.jce.interfaces.ECPublicKey ecPublicKey =
      (org.bouncycastle.jce.interfaces.ECPublicKey) publicKey;

    ECPoint ecPoint = ecPublicKey.getQ();
    ECPoint pointOnCurve = ecCurve.validatePoint(
      ecPoint.getAffineXCoord().toBigInteger(),
      ecPoint.getAffineYCoord().toBigInteger()
    );
    return !pointOnCurve.isInfinity();
  }

  public static byte[] dafnyArrayUnWrapper(
    DafnySequence<? extends Byte> dafnyByteSequence
  ) {
    return (byte[]) Array.unwrap(dafnyByteSequence.toArray());
  }

  public static void checkBCProvider() {
    if (Security.getProvider("BC") == null) {
      Security.addProvider(new BouncyCastleProvider());
    }
  }
}
