// Class __default
// Dafny class __default compiled into Java
package AwsCryptographyPrimitivesOperations_Compile;

import software.amazon.cryptography.primitives.internaldafny.types.*;
import ExternRandom.*;
import Random_Compile.*;
import AESEncryption.*;
import ExternDigest.*;
import Digest_Compile.*;
import HMAC.*;
import WrappedHMAC_Compile.*;
import HKDF_Compile.*;
import WrappedHKDF_Compile.*;
import Signature.*;
import KdfCtr_Compile.*;
import RSAEncryption.*;
import ECDH.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateRandomBytes(Config config, software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = Random_Compile.__default.GenerateBytes((input).dtor_length());
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Digest(Config config, software.amazon.cryptography.primitives.internaldafny.types.DigestInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = Digest_Compile.__default.Digest(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> HMac(Config config, software.amazon.cryptography.primitives.internaldafny.types.HMacInput input)
  {
    return WrappedHMAC_Compile.__default.Digest(input);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> HkdfExtract(Config config, software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = WrappedHKDF_Compile.__default.Extract(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> HkdfExpand(Config config, software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = WrappedHKDF_Compile.__default.Expand(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Hkdf(Config config, software.amazon.cryptography.primitives.internaldafny.types.HkdfInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = WrappedHKDF_Compile.__default.Hkdf(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> KdfCounterMode(Config config, software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = KdfCtr_Compile.__default.KdfCounterMode(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> AesKdfCounterMode(Config config, software.amazon.cryptography.primitives.internaldafny.types.AesKdfCtrInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Implement")));
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> AESEncrypt(Config config, software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AESEncryption.__default.AESEncrypt(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> AESDecrypt(Config config, software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AESEncryption.__default.AESDecrypt(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateRSAKeyPair(Config config, software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    if(true) {
      software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey _0_publicKey;
      software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey _1_privateKey;
      software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey _out0;
      software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey _out1;
      dafny.Tuple2<software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey, software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey> _outcollector0 = RSAEncryption.__default.GenerateKeyPair((input).dtor_lengthBits());
      _out0 = (software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey) (Object) _outcollector0.dtor__0();
      _out1 = (software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey) (Object) _outcollector0.dtor__1();
      _0_publicKey = _out0;
      _1_privateKey = _out1;
      output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput.create(_0_publicKey, _1_privateKey));
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GetRSAKeyModulusLength(Config config, software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthInput input)
  {
    Wrappers_Compile.Result<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = RSAEncryption.__default.GetRSAKeyModulusLength((input).dtor_publicKey());
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.RSAModulusLengthBits._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.RSAModulusLengthBits._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput._typeDescriptor());
    } else {
      int _1_length = (_0_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.RSAModulusLengthBits._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      return Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput.create(_1_length));
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> RSADecrypt(Config config, software.amazon.cryptography.primitives.internaldafny.types.RSADecryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = RSAEncryption.__default.Decrypt(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> RSAEncrypt(Config config, software.amazon.cryptography.primitives.internaldafny.types.RSAEncryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = RSAEncryption.__default.Encrypt(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateECDSASignatureKey(Config config, software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = Signature.__default.KeyGen(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> ECDSASign(Config config, software.amazon.cryptography.primitives.internaldafny.types.ECDSASignInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = Signature.ECDSA.Sign((input).dtor_signatureAlgorithm(), (input).dtor_signingKey(), (input).dtor_message());
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> ECDSAVerify(Config config, software.amazon.cryptography.primitives.internaldafny.types.ECDSAVerifyInput input)
  {
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), false);
    if(true) {
      output = Signature.ECDSA.Verify((input).dtor_signatureAlgorithm(), (input).dtor_verificationKey(), (input).dtor_message(), (input).dtor_signature());
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateECCKeyPair(Config config, software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = ECDH.__default.GenerateEccKeyPair(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GetPublicKeyFromPrivateKey(Config config, software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = ECDH.__default.GetPublicKeyFromPrivate(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> ValidatePublicKey(Config config, software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = ECDH.__default.ValidatePublicKey(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> DeriveSharedSecret(Config config, software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = ECDH.__default.DeriveSharedSecret(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> CompressPublicKey(Config config, software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = ECDH.__default.CompressPublicKey(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> DecompressPublicKey(Config config, software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = ECDH.__default.DecompressPublicKey(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> ParsePublicKey(Config config, software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = ECDH.__default.ParsePublicKey(input);
      output = _out0;
    }
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "AwsCryptographyPrimitivesOperations._default";
  }
}
