package aws.cryptography.mpl.testserver.tests;

import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

/**
 * Test-only key material. These keys protect nothing, are committed deliberately in
 * plain sight, and must never be used for anything real. Fixed rather than random so
 * failures reproduce from the test source alone.
 */
public final class TestKeyMaterial {

  private TestKeyMaterial() {}

  /** A 16-byte (AES-128) wrapping key. */
  public static final byte[] AES_128_KEY = repeating((byte) 0x11, 16);

  /** A 24-byte (AES-192) wrapping key. */
  public static final byte[] AES_192_KEY = repeating((byte) 0x22, 24);

  /** A 32-byte (AES-256) wrapping key. */
  public static final byte[] AES_256_KEY = repeating((byte) 0x33, 32);

  /** The namespace every test keyring uses. */
  public static final String KEY_NAMESPACE = "mpl-test-server";

  /** The key name every test AES keyring uses. */
  public static final String AES_KEY_NAME = "aes-test-key";

  /** The key name every test RSA keyring uses. */
  public static final String RSA_KEY_NAME = "rsa-test-key";

  /** Return a wrapping key of the length a given AES wrapping algorithm requires. */
  public static ByteBuffer aesKeyForBits(int bits) {
    return switch (bits) {
      case 128 -> ByteBuffer.wrap(AES_128_KEY);
      case 192 -> ByteBuffer.wrap(AES_192_KEY);
      case 256 -> ByteBuffer.wrap(AES_256_KEY);
      default -> throw new IllegalArgumentException(
        "No test AES key of " + bits + " bits; expected 128, 192, or 256."
      );
    };
  }

  private static byte[] repeating(byte value, int length) {
    byte[] bytes = new byte[length];
    java.util.Arrays.fill(bytes, value);
    return bytes;
  }

  /**
   * Test-only 2048-bit RSA public key, PEM-encoded X.509 SubjectPublicKeyInfo --
   * the encoding the MPL requires. A keyring with only this key can encrypt but
   * not decrypt.
   */
  public static final String RSA_PUBLIC_KEY_PEM =
    "-----BEGIN PUBLIC KEY-----\n" +
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy+dVz+r+dO4PV3BITWUl\n" +
    "RtmwJOk703QOIaJztUwxvsZMFd2ld7MNHU7s1/A0JuD3ycgkWlseEzCmmHLuvUdh\n" +
    "zZoJ/aQzyPQQCn+4s4w/lgKm4u8tj+INMJmS4ClYnI4UNaI0oo7ffe0VrSnUoL+O\n" +
    "251MP3rAMcAnulN0Blw9DSiNGcJrp3gGzDnMU35Lq/wEpyAj8NWRBB5sn8WEh/A5\n" +
    "qjG2ZUqjp0ODRlsaPQ5PqBLaY877CZYtL6mCFGE5wZYYYJ3JAtmSFG14K9675kq9\n" +
    "VSrhap9f0dIbku+S3nPjHDLZVGYgewVVYNlN9UIOAISFzYl/pWNfCjNSfKCRqqn4\n" +
    "DwIDAQAB\n" +
    "-----END PUBLIC KEY-----\n";

  /**
   * Matching test-only RSA private key, PEM-encoded PKCS#8 PrivateKeyInfo -- the
   * encoding the MPL requires. A keyring with only this key can decrypt but not
   * encrypt.
   */
  public static final String RSA_PRIVATE_KEY_PEM =
    "-----BEGIN PRIVATE KEY-----\n" +
    "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDL51XP6v507g9X\n" +
    "cEhNZSVG2bAk6TvTdA4honO1TDG+xkwV3aV3sw0dTuzX8DQm4PfJyCRaWx4TMKaY\n" +
    "cu69R2HNmgn9pDPI9BAKf7izjD+WAqbi7y2P4g0wmZLgKVicjhQ1ojSijt997RWt\n" +
    "KdSgv47bnUw/esAxwCe6U3QGXD0NKI0ZwmuneAbMOcxTfkur/ASnICPw1ZEEHmyf\n" +
    "xYSH8DmqMbZlSqOnQ4NGWxo9Dk+oEtpjzvsJli0vqYIUYTnBlhhgnckC2ZIUbXgr\n" +
    "3rvmSr1VKuFqn1/R0huS75Lec+McMtlUZiB7BVVg2U31Qg4AhIXNiX+lY18KM1J8\n" +
    "oJGqqfgPAgMBAAECggEAbZN1LxX3BrmELxYdFNJ9NNT5buyUBO+CRJr7mXtH5GDG\n" +
    "NJ33NRtYud5XMzhXnmkZYCuZNaFvyRpE/PoOyFMbARV9tvvOBHj8QdgfVwXQifoE\n" +
    "20Fzd7YgJnTxVFuDziYgQC5aIN2sxwxosLUhGf23dNfUSOzbaiD8eIoueNiKyo2B\n" +
    "kvpWg7pOtqlt6NAnMn/yaNAaq6jTJWDtE0AafUSPUsr4vMFBoobck1EDq3LLHT3Y\n" +
    "ZQ9CCpztrJn3niQrwVSNfH6UiQJczsdssmszu4oNeCfvvEPhW9etMDhrJMQkD/5s\n" +
    "dgt4cs3ZoE3eHtfb9xmMsoHmmnbBYmJz6IHfH3CZGQKBgQDrWnZdjHdLaOCRiWhX\n" +
    "i1xNT7BnEQvTWTJbgzDjn1xi3s+pMXGgBvMma8ulSPFPmoL0LZe6afJA3ujLdZX7\n" +
    "nJFrVk10MF5CKItdBKNJP83PyD4ehbG0ikDHX0KPoItj/TU7f8szLHMU8Ijhr1s4\n" +
    "x8cHgi7z1gHcrVtMmVOPZEo6QwKBgQDdypQzoGa3pRYp28yj8MW1++lGpDssB0du\n" +
    "sjq62SGErR0S9EKghmHqh1mfyuN2qkGJdIxgbPDNm7CCdWRw2R9YtRCVbiiNCVeN\n" +
    "S+Hb1s4oINW0mFUg8RNwtfqxFMlX/frBryCyzjsrFtEqN10+O/4uDbl0P84MUPfB\n" +
    "p+qR9lxsRQKBgQDpm6pfotyKinhVnVlnhBnDV3UWaLIfP6sfcLHnTjgqn1TqcPyC\n" +
    "xkM1gMvrrOJxjEGt00+GpkDiqR/TTEzqKfeh3lEVIil9a7chRkg5nc5RD0axjyzb\n" +
    "slsoSmLMI6QYRK5A99EfY2B7iWGk+iUG0C27QzoNp//DJoO4HXz2mKqg9wKBgCYf\n" +
    "iSPqoV1Vuh6N0noni8SBPZLP7f/ebG/hoOi3I+TLYOD+LWmsT65hf41Q8ZJXJ5a5\n" +
    "+tskPqwI4+k4xoADQjkcPnKBEeVUQsFd1r/UB3GsWy+Es7VK2v2XujSwDv/Z/z1F\n" +
    "ngg+HLuGW4O3KoblBwbhgwwxX3iMflnCRDa8sxxFAoGBAOhvemSs2ypY+j1i+yJS\n" +
    "SKBGmpj+JYN6tHAMOzecUhdzU7BfwPOGrqNwEB4qHiC05E4ZRssrkUlZHGo8RLXC\n" +
    "sTbvX166apn9dFKf0YLLW7culKPtCEsKYpDErAka/EZMJXCwcOPqevrqv+XhCQ1L\n" +
    "gSsUHdOjNshmLBcppValpm0d\n" +
    "-----END PRIVATE KEY-----\n";

  /** Return a UTF-8 view of a PEM string -- the encoding the MPL expects. */
  public static ByteBuffer pem(String pem) {
    return ByteBuffer.wrap(pem.getBytes(StandardCharsets.UTF_8));
  }
}
