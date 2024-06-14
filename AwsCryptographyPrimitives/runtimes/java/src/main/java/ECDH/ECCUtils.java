package ECDH;

import static ECDH.ECCAlgorithm.eccAlgorithm;
import static software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence;

import Signature.PublicKeyUtils;
import Signature.PublicKeyUtils;
import Signature.SignatureAlgorithm;
import StandardLibraryInternal.InternalResult;
import StandardLibraryInternal.InternalResult;
import Wrappers_Compile.Result;
import dafny.Array;
import dafny.DafnySequence;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringWriter;
import java.math.BigInteger;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.AlgorithmParameters;
import java.security.KeyFactory;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Security;
import java.security.interfaces.ECPrivateKey;
import java.security.interfaces.ECPublicKey;
import java.security.spec.ECGenParameterSpec;
import java.security.spec.ECPrivateKeySpec;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.InvalidParameterSpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import org.bouncycastle.asn1.x509.SubjectPublicKeyInfo;
import org.bouncycastle.crypto.params.ECDomainParameters;
import org.bouncycastle.crypto.params.ECPrivateKeyParameters;
import org.bouncycastle.crypto.util.PrivateKeyFactory;
import org.bouncycastle.crypto.util.PublicKeyFactory;
import org.bouncycastle.jce.ECNamedCurveTable;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.jce.spec.ECParameterSpec;
import org.bouncycastle.jce.spec.ECPublicKeySpec;
import org.bouncycastle.math.ec.ECCurve;
import org.bouncycastle.math.ec.ECPoint;
import org.bouncycastle.util.io.pem.PemObject;
import org.bouncycastle.util.io.pem.PemReader;
import org.bouncycastle.util.io.pem.PemWriter;
import software.amazon.cryptography.primitives.ToDafny;
import software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey;
import software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;

public class ECCUtils extends _ExternBase___default {

  public static Result<DafnySequence<? extends Byte>, Error> GetPublicKey(
    ECDHCurveSpec dtor_eccAlgorithm,
    ECCPrivateKey dtor_privateKey
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
      try {
        final byte[] pem = dafnyArrayUnWrapper(dtor_privateKey._pem);
        final ECPrivateKey privateKey =
          (ECPrivateKey) parsePrivateKeyEccPemBytesToPrivateKey(pem);

        ECParameterSpec parameterSpec = ECNamedCurveTable.getParameterSpec(
          maybeEccAlgorithm.value().curve
        );
        ECPoint Q = parameterSpec.getG().multiply(privateKey.getS());
        ECPublicKeySpec publicKeySpec = new ECPublicKeySpec(Q, parameterSpec);

        final KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");
        PublicKey publicKey = keyFactory.generatePublic(publicKeySpec);
        X509EncodedKeySpec encodedKeySpec = new X509EncodedKeySpec(
          publicKey.getEncoded()
        );

        return CreateExternGetPublicKeyFromPrivateSuccess(
          DafnySequence.fromBytes(encodedKeySpec.getEncoded())
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

  public static PrivateKey parsePrivateKeyEccPemBytesToPrivateKey(byte[] pem)
    throws NoSuchAlgorithmException, InvalidKeySpecException, IOException {
    byte[] privateKeyBytes = parsePrivateKeyPemBytes(pem);
    KeyFactory keyFactory = KeyFactory.getInstance("EC");
    return keyFactory.generatePrivate(new PKCS8EncodedKeySpec(privateKeyBytes));
  }

  public static Result<Boolean, Error> ValidatePublicKey(
    ECDHCurveSpec dtor_eccAlgorithm,
    DafnySequence<? extends Byte> dtro_publicKey
  ) {
    checkBCProvider();
    final byte[] publicKeyBytes = dafnyArrayUnWrapper(dtro_publicKey);

    final InternalResult<ECCAlgorithm, Error> maybeEccAlgorithm = eccAlgorithm(
      dtor_eccAlgorithm
    );
    if (maybeEccAlgorithm.isFailure()) {
      return CreateExternValidatePublicKeyError(maybeEccAlgorithm.error());
    }

    if (!maybeEccAlgorithm.value().curve.equals("SM2")) {
      try {
        final boolean validPublicKey = NistPublicKeyValidationCriteria(
          publicKeyBytes,
          maybeEccAlgorithm.value()
        );
        return CreateExternValidatePublicKeySuccess(validPublicKey);
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

  // We are verifying the NIST requirements for ECC Public Keys
  // https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=55
  static boolean NistPublicKeyValidationCriteria(
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
    return (
      ValidatePublicKeyIsNotInfinity(pointOnCurve) &&
      CoordinateBetween0AndP(
        ecPoint.getAffineXCoord().toBigInteger(),
        ecCurve
      ) &&
      CoordinateBetween0AndP(ecPoint.getAffineYCoord().toBigInteger(), ecCurve)
    );
  }

  private static boolean ValidatePublicKeyIsNotInfinity(ECPoint point) {
    return !point.isInfinity();
  }

  private static boolean CoordinateBetween0AndP(
    BigInteger coordinate,
    ECCurve curve
  ) {
    return (
      coordinate.compareTo(BigInteger.ZERO) > 0 &&
      coordinate.compareTo(curve.getField().getCharacteristic()) < 0
    );
  }

  public static Result<
    DafnySequence<? extends java.lang.Byte>,
    Error
  > CompressPublicKey(
    DafnySequence<? extends java.lang.Byte> publicKeyDerBytes,
    ECDHCurveSpec dtor_eccAlgorithm
  ) {
    try {
      checkBCProvider();
      final byte[] publicKeyBytes = dafnyArrayUnWrapper(publicKeyDerBytes);
      KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");
      org.bouncycastle.jce.interfaces.ECPublicKey publicKey =
        (org.bouncycastle.jce.interfaces.ECPublicKey) keyFactory.generatePublic(
          new X509EncodedKeySpec(publicKeyBytes)
        );
      final byte[] compressedPublicKey = publicKey.getQ().getEncoded(true);
      return CreateExternCompressPublicKeySuccess(
        DafnySequence.fromBytes(compressedPublicKey)
      );
    } catch (Exception e) {
      return CreateExternCompressPublicKeyError(
        ToDafny.Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message(e.getMessage())
            .build()
        )
      );
    }
  }

  public static Result<
    DafnySequence<? extends java.lang.Byte>,
    Error
  > DecompressPublicKey(
    DafnySequence<? extends Byte> compressedPublicKey,
    ECDHCurveSpec dtor_eccAlgorithm
  ) {
    try {
      checkBCProvider();
      final InternalResult<ECCAlgorithm, Error> maybeEccAlgorithm =
        eccAlgorithm(dtor_eccAlgorithm);
      if (maybeEccAlgorithm.isFailure()) {
        return CreateExternDecompressPublicKeyError(maybeEccAlgorithm.error());
      }
      final java.security.spec.ECParameterSpec ecParameterSpec =
        ecParameterSpec(maybeEccAlgorithm.value());
      final byte[] compressedPublicKeyBytes = dafnyArrayUnWrapper(
        compressedPublicKey
      );
      final java.security.spec.ECPoint point =
        PublicKeyUtils.byteArrayToECPoint(
          compressedPublicKeyBytes,
          ecParameterSpec
        );
      final java.security.spec.ECPublicKeySpec spec =
        new java.security.spec.ECPublicKeySpec(point, ecParameterSpec);
      final ECPublicKey publicKey = (ECPublicKey) KeyFactory
        .getInstance("EC")
        .generatePublic(spec);
      return CreateExternDecompressPublicKeySuccess(
        DafnySequence.fromBytes(publicKey.getEncoded())
      );
    } catch (Exception e) {
      return CreateExternDecompressPublicKeyError(
        ToDafny.Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message(e.getMessage())
            .build()
        )
      );
    }
  }

  public static Result<
    DafnySequence<? extends java.lang.Byte>,
    Error
  > ParsePublicKey(DafnySequence<? extends Byte> publicKey) {
    try {
      checkBCProvider();
      final byte[] publicKeyBytes = dafnyArrayUnWrapper(publicKey);
      SubjectPublicKeyInfo subjectPublicKeyInfo =
        SubjectPublicKeyInfo.getInstance(publicKeyBytes);
      X509EncodedKeySpec x509KeySpec = new X509EncodedKeySpec(
        subjectPublicKeyInfo.getEncoded()
      );
      KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");

      PublicKey ecPublicKey = keyFactory.generatePublic(x509KeySpec);
      return CreateExternParsePublicKeySuccess(
        DafnySequence.fromBytes(ecPublicKey.getEncoded())
      );
    } catch (Exception e) {
      return CreateExternParsePublicKeyError(
        ToDafny.Error(
          AwsCryptographicPrimitivesError
            .builder()
            .message(e.getMessage())
            .build()
        )
      );
    }
  }

  static DafnySequence<Byte> encodePrivateKey(final PrivateKey privateKey)
    throws IOException {
    PKCS8EncodedKeySpec pkcs8KeySpec = new PKCS8EncodedKeySpec(
      privateKey.getEncoded()
    );
    StringWriter stringWriter = new StringWriter();
    PemWriter pemWriter = new PemWriter(stringWriter);
    pemWriter.writeObject(
      new PemObject("PRIVATE KEY", pkcs8KeySpec.getEncoded())
    );
    pemWriter.close();
    ByteBuffer outBuffer = StandardCharsets.UTF_8.encode(
      stringWriter.toString()
    );
    return ByteSequence(outBuffer, 0, outBuffer.limit());
  }

  private static byte[] parsePrivateKeyPemBytes(byte[] pem) throws IOException {
    PemReader pemReader = new PemReader(
      new InputStreamReader(new ByteArrayInputStream(pem))
    );
    PemObject pemObject = pemReader.readPemObject();
    return pemObject.getContent();
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

  public static java.security.spec.ECParameterSpec ecParameterSpec(
    ECCAlgorithm eccAlgorithm
  ) throws NoSuchAlgorithmException, InvalidParameterSpecException {
    final ECGenParameterSpec spec = new ECGenParameterSpec(eccAlgorithm.curve);
    final AlgorithmParameters parameters = AlgorithmParameters.getInstance(
      KeyGeneration.ELLIPTIC_CURVE_ALGORITHM
    );
    parameters.init(spec);
    return parameters.getParameterSpec(
      java.security.spec.ECParameterSpec.class
    );
  }
}
