package ECDH;

import static ECDH.ECCAlgorithm.eccAlgorithm;
import static ECDH.ECCUtils.checkBCProvider;

import Random_Compile.ExternRandom;
import StandardLibraryInternal.InternalResult;
import Wrappers_Compile.Result;
import dafny.DafnySequence;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.interfaces.ECPublicKey;
import java.security.spec.ECGenParameterSpec;
import java.security.spec.X509EncodedKeySpec;
import org.bouncycastle.asn1.gm.GMNamedCurves;
import org.bouncycastle.asn1.x9.X9ECParameters;
import org.bouncycastle.crypto.AsymmetricCipherKeyPair;
import org.bouncycastle.crypto.generators.ECKeyPairGenerator;
import org.bouncycastle.crypto.params.ECDomainParameters;
import org.bouncycastle.crypto.params.ECKeyGenerationParameters;
import org.bouncycastle.crypto.params.ECPrivateKeyParameters;
import org.bouncycastle.crypto.params.ECPublicKeyParameters;
import software.amazon.cryptography.primitives.ToDafny;
import software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;

public class KeyGeneration extends _ExternBase___default {

  static final String ELLIPTIC_CURVE_ALGORITHM = "EC";
  static final String SEC_PRIME_FIELD_PREFIX = "secp";
  static final String SEC_P256 = "256r1";
  static final String SEC_P384 = "384r1";
  static final String SEC_P521 = "521r1";
  static final String SM2_KA = "SM2";

  public static Result<EccKeyPair, Error> GenerateKeyPair(
    ECDHCurveSpec dtor_eccAlgorithm
  ) {
    checkBCProvider();
    final InternalResult<ECCAlgorithm, Error> maybeEccAlgorithm = eccAlgorithm(
      dtor_eccAlgorithm
    );
    if (maybeEccAlgorithm.isFailure()) {
      return CreateExternEccKeyGenFailure(maybeEccAlgorithm.error());
    }
    if (!maybeEccAlgorithm.value().curve.equals("SM2")) {
      final ECGenParameterSpec genParameterSpec = new ECGenParameterSpec(
        maybeEccAlgorithm.value().curve
      );

      final SecureRandom secureRandom = ExternRandom.getSecureRandom();
      final KeyPairGenerator keyGen;
      try {
        keyGen = KeyPairGenerator.getInstance(ELLIPTIC_CURVE_ALGORITHM, "BC");
        keyGen.initialize(genParameterSpec, secureRandom);
        final KeyPair keyPair = keyGen.generateKeyPair();

        final DafnySequence<Byte> privateKey = ECCUtils.encodePrivateKey(
          keyPair.getPrivate()
        );
        final byte[] publicKey = encodePublicKeyDerFormat(
          (ECPublicKey) keyPair.getPublic()
        );

        return CreateExternEccKeyGenSuccess(
          EccKeyPair.create(privateKey, DafnySequence.fromBytes(publicKey))
        );
      } catch (Exception e) {
        return CreateExternEccKeyGenFailure(
          ToDafny.Error(
            AwsCryptographicPrimitivesError
              .builder()
              .cause(e)
              .message(e.getMessage())
              .build()
          )
        );
      }
    } else {
      X9ECParameters SM2_X9EC_PARAMETERS = GMNamedCurves.getByName("sm2p256v1");
      ECDomainParameters domain = new ECDomainParameters(
        SM2_X9EC_PARAMETERS.getCurve(),
        SM2_X9EC_PARAMETERS.getG(),
        SM2_X9EC_PARAMETERS.getN(),
        SM2_X9EC_PARAMETERS.getH()
      );
      ECKeyPairGenerator generator = new ECKeyPairGenerator();
      ECKeyGenerationParameters keygenParams = new ECKeyGenerationParameters(
        domain,
        new SecureRandom()
      );
      generator.init(keygenParams);
      AsymmetricCipherKeyPair keypair = generator.generateKeyPair();
      final byte[] privateKey =
        ((ECPrivateKeyParameters) keypair.getPrivate()).getD().toByteArray();
      final byte[] publicKey =
        ((ECPublicKeyParameters) keypair.getPublic()).getQ().getEncoded(false);

      return CreateExternEccKeyGenSuccess(
        EccKeyPair.create(
          DafnySequence.fromBytes(privateKey),
          DafnySequence.fromBytes(publicKey)
        )
      );
    }
  }

  static byte[] encodePublicKeyDerFormat(final ECPublicKey publicKey) {
    X509EncodedKeySpec spec = new X509EncodedKeySpec(publicKey.getEncoded());
    return spec.getEncoded();
  }
}
