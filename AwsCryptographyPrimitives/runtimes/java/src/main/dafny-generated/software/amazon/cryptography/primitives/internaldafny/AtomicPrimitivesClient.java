// Class AtomicPrimitivesClient
// Dafny class AtomicPrimitivesClient compiled into Java
package software.amazon.cryptography.primitives.internaldafny;

@SuppressWarnings({"unchecked", "deprecation"})
public class AtomicPrimitivesClient implements software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient {
  public AtomicPrimitivesClient() {
    this._config = AwsCryptographyPrimitivesOperations_Compile.Config.Default();
  }
  public void __ctor(AwsCryptographyPrimitivesOperations_Compile.Config config)
  {
    (this)._config = config;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.GenerateRandomBytes((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Digest(software.amazon.cryptography.primitives.internaldafny.types.DigestInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.Digest((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> HMac(software.amazon.cryptography.primitives.internaldafny.types.HMacInput input) {
    return AwsCryptographyPrimitivesOperations_Compile.__default.HMac((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> HkdfExtract(software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.HkdfExtract((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> HkdfExpand(software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.HkdfExpand((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Hkdf(software.amazon.cryptography.primitives.internaldafny.types.HkdfInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.Hkdf((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> KdfCounterMode(software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.KdfCounterMode((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> AesKdfCounterMode(software.amazon.cryptography.primitives.internaldafny.types.AesKdfCtrInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.AesKdfCounterMode((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> AESEncrypt(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.AESEncrypt((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> AESDecrypt(software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.AESDecrypt((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateRSAKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.GenerateRSAKeyPair((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GetRSAKeyModulusLength(software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthInput input) {
    return AwsCryptographyPrimitivesOperations_Compile.__default.GetRSAKeyModulusLength((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> RSADecrypt(software.amazon.cryptography.primitives.internaldafny.types.RSADecryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.RSADecrypt((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> RSAEncrypt(software.amazon.cryptography.primitives.internaldafny.types.RSAEncryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.RSAEncrypt((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateECDSASignatureKey(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.GenerateECDSASignatureKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> ECDSASign(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.ECDSASign((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> ECDSAVerify(software.amazon.cryptography.primitives.internaldafny.types.ECDSAVerifyInput input)
  {
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), false);
    if(true) {
      Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.ECDSAVerify((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateECCKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.GenerateECCKeyPair((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GetPublicKeyFromPrivateKey(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.GetPublicKeyFromPrivateKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> ValidatePublicKey(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.ValidatePublicKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> DeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.DeriveSharedSecret((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.CompressPublicKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> DecompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.DecompressPublicKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> ParsePublicKey(software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyPrimitivesOperations_Compile.__default.ParsePublicKey((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public AwsCryptographyPrimitivesOperations_Compile.Config _config;
  public AwsCryptographyPrimitivesOperations_Compile.Config config()
  {
    return this._config;
  }
  private static final dafny.TypeDescriptor<AtomicPrimitivesClient> _TYPE = dafny.TypeDescriptor.<AtomicPrimitivesClient>referenceWithInitializer(AtomicPrimitivesClient.class, () -> (AtomicPrimitivesClient) null);
  public static dafny.TypeDescriptor<AtomicPrimitivesClient> _typeDescriptor() {
    return (dafny.TypeDescriptor<AtomicPrimitivesClient>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AtomicPrimitives.AtomicPrimitivesClient";
  }
}
