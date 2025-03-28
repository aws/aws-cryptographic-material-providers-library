// Class __default
// Dafny class __default compiled into Java
package Constants_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static int ECDH__PROVIDER__INFO__RPL__INDEX()
  {
    return 1;
  }
  public static java.math.BigInteger ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN()
  {
    return java.math.BigInteger.valueOf(4L);
  }
  public static int ECDH__PROVIDER__INFO__RPK__INDEX()
  {
    return (int) ((__default.ECDH__PROVIDER__INFO__RPL__INDEX()) + ((__default.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN()).intValue()));
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
  public static java.math.BigInteger UINT32__TO__SEQ__LEN()
  {
    return java.math.BigInteger.valueOf(4L);
  }
  public static int KDF__SALT__LEN()
  {
    return 32;
  }
  public static int KDF__EXPECTED__LEN()
  {
    return 64;
  }
  public static java.math.BigInteger ECDH__COMMITMENT__KEY__LENGTH()
  {
    return java.math.BigInteger.valueOf(32L);
  }
  public static java.math.BigInteger ECDH__COMMITMENT__KEY__INDEX()
  {
    return java.math.BigInteger.valueOf(32L);
  }
  public static java.math.BigInteger ECDH__WRAPPED__KEY__MATERIAL__INDEX()
  {
    return java.math.BigInteger.valueOf(64L);
  }
  public static dafny.DafnySequence<? extends Character> ECDH__KDF__STRING()
  {
    return dafny.DafnySequence.asString("ecdh-key-derivation");
  }
  public static dafny.DafnySequence<? extends Character> ECDH__KDF__PRF__STRING()
  {
    return dafny.DafnySequence.asString("HMAC_SHA384");
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ECDH__KDF__DELIMETER()
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
  public static java.math.BigInteger ECDH__PUBLIC__KEY__LEN__ECC__NIST__256()
  {
    return java.math.BigInteger.valueOf(91L);
  }
  public static java.math.BigInteger ECDH__PUBLIC__KEY__LEN__ECC__NIST__384()
  {
    return java.math.BigInteger.valueOf(120L);
  }
  public static java.math.BigInteger ECDH__PUBLIC__KEY__LEN__ECC__NIST__521()
  {
    return java.math.BigInteger.valueOf(158L);
  }
  public static java.math.BigInteger ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__256()
  {
    return java.math.BigInteger.valueOf(33L);
  }
  public static java.math.BigInteger ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__384()
  {
    return java.math.BigInteger.valueOf(49L);
  }
  public static java.math.BigInteger ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__521()
  {
    return java.math.BigInteger.valueOf(67L);
  }
  public static java.math.BigInteger CIPHERTEXT__WRAPPED__MATERIAL__INDEX()
  {
    return java.math.BigInteger.valueOf(68L);
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
    return UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("aws-kms-ecdh"));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> RAW__ECDH__PROVIDER__ID()
  {
    return UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("raw-ecdh"));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ECDH__KDF__PRF__NAME()
  {
    return UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("HMAC_SHA384"));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ECDH__KDF__UTF8()
  {
    return UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("ecdh-key-derivation"));
  }
  @Override
  public java.lang.String toString() {
    return "Constants._default";
  }
}
