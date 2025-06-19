// Class __default
// Dafny class __default compiled into Java
package Constants_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static int ECDH__PROVIDER__INFO__RPL__INDEX()
  {
    return 1;
  }
  public static long ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN()
  {
    return (long) 4L;
  }
  public static int ECDH__PROVIDER__INFO__RPK__INDEX()
  {
    return (int) ((__default.ECDH__PROVIDER__INFO__RPL__INDEX()) + (((int) (__default.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN()))));
  }
  public static int ECDH__AES__256__ENC__KEY__LENGTH()
  {
    return 32;
  }
  public static int ECDH__AES__256__ENC__TAG__LENGTH()
  {
    return 16;
  }
  public static int ECDH__AES__256__ENC__IV__LENGTH()
  {
    return 12;
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.AES__GCM ECDH__AES__256__ENC__ALG()
  {
    return software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(__default.ECDH__AES__256__ENC__KEY__LENGTH(), __default.ECDH__AES__256__ENC__TAG__LENGTH(), __default.ECDH__AES__256__ENC__IV__LENGTH());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> PROVIDER__ID()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 119, (byte) 115, (byte) 45, (byte) 107, (byte) 109, (byte) 115);
    return _0_s;
  }
  public static long UINT32__TO__SEQ__LEN()
  {
    return (long) 4L;
  }
  public static int KDF__SALT__LEN()
  {
    return 32;
  }
  public static int KDF__EXPECTED__LEN()
  {
    return 64;
  }
  public static long ECDH__COMMITMENT__KEY__LENGTH()
  {
    return (long) 32L;
  }
  public static long ECDH__COMMITMENT__KEY__INDEX()
  {
    return (long) 32L;
  }
  public static long ECDH__WRAPPED__KEY__MATERIAL__INDEX()
  {
    return (long) 64L;
  }
  public static dafny.DafnySequence<? extends Character> ECDH__KDF__STRING()
  {
    return dafny.DafnySequence.asString("ecdh-key-derivation");
  }
  public static dafny.DafnySequence<? extends Character> ECDH__KDF__PRF__STRING()
  {
    return dafny.DafnySequence.asString("HMAC_SHA384");
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ECDH__KDF__DELIMITER()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 0);
  }
  public static int ECDH__PROVIDER__INFO__256__LEN()
  {
    return 75;
  }
  public static int ECDH__PROVIDER__INFO__384__LEN()
  {
    return 107;
  }
  public static int ECDH__PROVIDER__INFO__521__LEN()
  {
    return 143;
  }
  public static long ECDH__PUBLIC__KEY__LEN__ECC__NIST__256()
  {
    return (long) 91L;
  }
  public static long ECDH__PUBLIC__KEY__LEN__ECC__NIST__384()
  {
    return (long) 120L;
  }
  public static long ECDH__PUBLIC__KEY__LEN__ECC__NIST__521()
  {
    return (long) 158L;
  }
  public static long ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__256()
  {
    return (long) 33L;
  }
  public static long ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__384()
  {
    return (long) 49L;
  }
  public static long ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__521()
  {
    return (long) 67L;
  }
  public static long CIPHERTEXT__WRAPPED__MATERIAL__INDEX()
  {
    return (long) 68L;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> PROVIDER__ID__HIERARCHY()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 119, (byte) 115, (byte) 45, (byte) 107, (byte) 109, (byte) 115, (byte) 45, (byte) 104, (byte) 105, (byte) 101, (byte) 114, (byte) 97, (byte) 114, (byte) 99, (byte) 104, (byte) 121);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> RSA__PROVIDER__ID()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 119, (byte) 115, (byte) 45, (byte) 107, (byte) 109, (byte) 115, (byte) 45, (byte) 114, (byte) 115, (byte) 97);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> KMS__ECDH__PROVIDER__ID()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 119, (byte) 115, (byte) 45, (byte) 107, (byte) 109, (byte) 115, (byte) 45, (byte) 101, (byte) 99, (byte) 100, (byte) 104);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> RAW__ECDH__PROVIDER__ID()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 114, (byte) 97, (byte) 119, (byte) 45, (byte) 101, (byte) 99, (byte) 100, (byte) 104);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ECDH__KDF__PRF__NAME()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 72, (byte) 77, (byte) 65, (byte) 67, (byte) 95, (byte) 83, (byte) 72, (byte) 65, (byte) 51, (byte) 56, (byte) 52);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ECDH__KDF__UTF8()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 101, (byte) 99, (byte) 100, (byte) 104, (byte) 45, (byte) 107, (byte) 101, (byte) 121, (byte) 45, (byte) 100, (byte) 101, (byte) 114, (byte) 105, (byte) 118, (byte) 97, (byte) 116, (byte) 105, (byte) 111, (byte) 110);
    return _0_s;
  }
  @Override
  public java.lang.String toString() {
    return "Constants._default";
  }
}
