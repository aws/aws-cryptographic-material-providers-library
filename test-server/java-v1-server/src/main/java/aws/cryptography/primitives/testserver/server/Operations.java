package aws.cryptography.primitives.testserver.server;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import java.nio.ByteBuffer;
import software.amazon.cryptography.primitives.AtomicPrimitives;
import software.amazon.cryptography.primitives.model.AESDecryptInput;
import software.amazon.cryptography.primitives.model.AESEncryptInput;
import software.amazon.cryptography.primitives.model.AESEncryptOutput;
import software.amazon.cryptography.primitives.model.AES_GCM;
import software.amazon.cryptography.primitives.model.DigestAlgorithm;
import software.amazon.cryptography.primitives.model.DigestInput;
import software.amazon.cryptography.primitives.model.ECDSASignInput;
import software.amazon.cryptography.primitives.model.ECDSASignatureAlgorithm;
import software.amazon.cryptography.primitives.model.ECDSAVerifyInput;
import software.amazon.cryptography.primitives.model.GenerateECDSASignatureKeyInput;
import software.amazon.cryptography.primitives.model.GenerateECDSASignatureKeyOutput;
import software.amazon.cryptography.primitives.model.GenerateRandomBytesInput;
import software.amazon.cryptography.primitives.model.HMacInput;
import software.amazon.cryptography.primitives.model.HkdfInput;
import software.amazon.cryptography.primitives.model.KdfCtrInput;

/** Maps each TestServer operation to a call on the Java AtomicPrimitives client. */
final class Operations {

  private static final int GCM_TAG_LENGTH = 16;
  private static final int GCM_IV_LENGTH = 12;

  private final AtomicPrimitives primitives;

  Operations(AtomicPrimitives primitives) {
    this.primitives = primitives;
  }

  ObjectNode dispatch(String operation, JsonNode request) {
    switch (operation) {
      case "AesEncrypt":
        return aesEncrypt(request);
      case "AesDecrypt":
        return aesDecrypt(request);
      case "GenerateRandomBytes":
        return generateRandomBytes(request);
      case "Digest":
        return digest(request);
      case "Hmac":
        return hmac(request);
      case "Hkdf":
        return hkdf(request);
      case "KbkdfCtrHmac":
        return kbkdfCtrHmac(request);
      case "EcdsaGenerateKeyPair":
        return ecdsaGenerateKeyPair(request);
      case "EcdsaSign":
        return ecdsaSign(request);
      case "EcdsaVerify":
        return ecdsaVerify(request);
      default:
        throw ModeledError.generic("unknown operation: " + operation);
    }
  }

  private ObjectNode aesEncrypt(JsonNode request) {
    AESEncryptOutput output = primitives.AESEncrypt(
      AESEncryptInput
        .builder()
        .encAlg(aesGcm(Cbor.string(request, "algorithm")))
        .iv(ByteBuffer.wrap(Cbor.blob(request, "iv")))
        .key(ByteBuffer.wrap(Cbor.blob(request, "key")))
        .msg(ByteBuffer.wrap(Cbor.blob(request, "message")))
        .aad(ByteBuffer.wrap(Cbor.blob(request, "aad")))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("ciphertext", Cbor.bytes(output.cipherText()));
    response.put("authTag", Cbor.bytes(output.authTag()));
    return response;
  }

  private ObjectNode aesDecrypt(JsonNode request) {
    ByteBuffer plaintext = primitives.AESDecrypt(
      AESDecryptInput
        .builder()
        .encAlg(aesGcm(Cbor.string(request, "algorithm")))
        .key(ByteBuffer.wrap(Cbor.blob(request, "key")))
        .cipherTxt(ByteBuffer.wrap(Cbor.blob(request, "ciphertext")))
        .authTag(ByteBuffer.wrap(Cbor.blob(request, "authTag")))
        .iv(ByteBuffer.wrap(Cbor.blob(request, "iv")))
        .aad(ByteBuffer.wrap(Cbor.blob(request, "aad")))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("plaintext", Cbor.bytes(plaintext));
    return response;
  }

  private ObjectNode generateRandomBytes(JsonNode request) {
    ByteBuffer data = primitives.GenerateRandomBytes(
      GenerateRandomBytesInput
        .builder()
        .length(Cbor.integer(request, "length"))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("data", Cbor.bytes(data));
    return response;
  }

  private ObjectNode digest(JsonNode request) {
    ByteBuffer digest = primitives.Digest(
      DigestInput
        .builder()
        .digestAlgorithm(digestAlgorithm(Cbor.string(request, "algorithm")))
        .message(ByteBuffer.wrap(Cbor.blob(request, "data")))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("digest", Cbor.bytes(digest));
    return response;
  }

  private ObjectNode hmac(JsonNode request) {
    ByteBuffer digest = primitives.HMac(
      HMacInput
        .builder()
        .digestAlgorithm(digestAlgorithm(Cbor.string(request, "algorithm")))
        .key(ByteBuffer.wrap(Cbor.blob(request, "key")))
        .message(ByteBuffer.wrap(Cbor.blob(request, "message")))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("digest", Cbor.bytes(digest));
    return response;
  }

  private ObjectNode hkdf(JsonNode request) {
    ByteBuffer okm = primitives.Hkdf(
      HkdfInput
        .builder()
        .digestAlgorithm(digestAlgorithm(Cbor.string(request, "algorithm")))
        .salt(ByteBuffer.wrap(Cbor.blob(request, "salt")))
        .ikm(ByteBuffer.wrap(Cbor.blob(request, "ikm")))
        .info(ByteBuffer.wrap(Cbor.blob(request, "info")))
        .expectedLength(Cbor.integer(request, "expectedLength"))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("okm", Cbor.bytes(okm));
    return response;
  }

  private ObjectNode kbkdfCtrHmac(JsonNode request) {
    ByteBuffer okm = primitives.KdfCounterMode(
      KdfCtrInput
        .builder()
        .digestAlgorithm(digestAlgorithm(Cbor.string(request, "algorithm")))
        .ikm(ByteBuffer.wrap(Cbor.blob(request, "ikm")))
        .purpose(ByteBuffer.wrap(Cbor.blob(request, "info")))
        .expectedLength(Cbor.integer(request, "expectedLength"))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("okm", Cbor.bytes(okm));
    return response;
  }

  private ObjectNode ecdsaGenerateKeyPair(JsonNode request) {
    GenerateECDSASignatureKeyOutput output =
      primitives.GenerateECDSASignatureKey(
        GenerateECDSASignatureKeyInput
          .builder()
          .signatureAlgorithm(ecdsaAlgorithm(Cbor.string(request, "algorithm")))
          .build()
      );
    ObjectNode response = Cbor.object();
    response.put("verificationKey", Cbor.bytes(output.verificationKey()));
    response.put("signingKey", Cbor.bytes(output.signingKey()));
    return response;
  }

  private ObjectNode ecdsaSign(JsonNode request) {
    ByteBuffer signature = primitives.ECDSASign(
      ECDSASignInput
        .builder()
        .signatureAlgorithm(ecdsaAlgorithm(Cbor.string(request, "algorithm")))
        .signingKey(ByteBuffer.wrap(Cbor.blob(request, "signingKey")))
        .message(ByteBuffer.wrap(Cbor.blob(request, "message")))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("signature", Cbor.bytes(signature));
    return response;
  }

  private ObjectNode ecdsaVerify(JsonNode request) {
    boolean valid = primitives.ECDSAVerify(
      ECDSAVerifyInput
        .builder()
        .signatureAlgorithm(ecdsaAlgorithm(Cbor.string(request, "algorithm")))
        .verificationKey(ByteBuffer.wrap(Cbor.blob(request, "verificationKey")))
        .message(ByteBuffer.wrap(Cbor.blob(request, "message")))
        .signature(ByteBuffer.wrap(Cbor.blob(request, "signature")))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("valid", valid);
    return response;
  }

  private static AES_GCM aesGcm(String algorithm) {
    int keyLength;
    switch (algorithm) {
      case "AES_128_GCM":
        keyLength = 16;
        break;
      case "AES_192_GCM":
        keyLength = 24;
        break;
      case "AES_256_GCM":
        keyLength = 32;
        break;
      default:
        throw ModeledError.generic("unknown AES algorithm: " + algorithm);
    }
    return AES_GCM
      .builder()
      .keyLength(keyLength)
      .tagLength(GCM_TAG_LENGTH)
      .ivLength(GCM_IV_LENGTH)
      .build();
  }

  private static DigestAlgorithm digestAlgorithm(String algorithm) {
    switch (algorithm) {
      case "SHA_256":
        return DigestAlgorithm.SHA_256;
      case "SHA_384":
        return DigestAlgorithm.SHA_384;
      case "SHA_512":
        return DigestAlgorithm.SHA_512;
      default:
        throw ModeledError.generic("unknown digest algorithm: " + algorithm);
    }
  }

  private static ECDSASignatureAlgorithm ecdsaAlgorithm(String algorithm) {
    switch (algorithm) {
      case "ECDSA_P256":
        return ECDSASignatureAlgorithm.ECDSA_P256;
      case "ECDSA_P384":
        return ECDSASignatureAlgorithm.ECDSA_P384;
      default:
        throw ModeledError.generic("unknown ECDSA algorithm: " + algorithm);
    }
  }
}
