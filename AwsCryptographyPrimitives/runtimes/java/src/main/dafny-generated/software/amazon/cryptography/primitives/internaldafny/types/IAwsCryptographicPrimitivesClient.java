// Interface IAwsCryptographicPrimitivesClient
// Dafny trait IAwsCryptographicPrimitivesClient compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public interface IAwsCryptographicPrimitivesClient {
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> GenerateRandomBytes(GenerateRandomBytesInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> Digest(DigestInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> HMac(HMacInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> HkdfExtract(HkdfExtractInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> HkdfExpand(HkdfExpandInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> Hkdf(HkdfInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> KdfCounterMode(KdfCtrInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> AesKdfCounterMode(AesKdfCtrInput input);
  public Wrappers_Compile.Result<AESEncryptOutput, Error> AESEncrypt(AESEncryptInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> AESDecrypt(AESDecryptInput input);
  public Wrappers_Compile.Result<GenerateRSAKeyPairOutput, Error> GenerateRSAKeyPair(GenerateRSAKeyPairInput input);
  public Wrappers_Compile.Result<GetRSAKeyModulusLengthOutput, Error> GetRSAKeyModulusLength(GetRSAKeyModulusLengthInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> RSADecrypt(RSADecryptInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> RSAEncrypt(RSAEncryptInput input);
  public Wrappers_Compile.Result<GenerateECDSASignatureKeyOutput, Error> GenerateECDSASignatureKey(GenerateECDSASignatureKeyInput input);
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, Error> ECDSASign(ECDSASignInput input);
  public Wrappers_Compile.Result<Boolean, Error> ECDSAVerify(ECDSAVerifyInput input);
  public Wrappers_Compile.Result<GenerateECCKeyPairOutput, Error> GenerateECCKeyPair(GenerateECCKeyPairInput input);
  public Wrappers_Compile.Result<GetPublicKeyFromPrivateKeyOutput, Error> GetPublicKeyFromPrivateKey(GetPublicKeyFromPrivateKeyInput input);
  public Wrappers_Compile.Result<ValidatePublicKeyOutput, Error> ValidatePublicKey(ValidatePublicKeyInput input);
  public Wrappers_Compile.Result<DeriveSharedSecretOutput, Error> DeriveSharedSecret(DeriveSharedSecretInput input);
  public Wrappers_Compile.Result<CompressPublicKeyOutput, Error> CompressPublicKey(CompressPublicKeyInput input);
  public Wrappers_Compile.Result<DecompressPublicKeyOutput, Error> DecompressPublicKey(DecompressPublicKeyInput input);
  public Wrappers_Compile.Result<ParsePublicKeyOutput, Error> ParsePublicKey(ParsePublicKeyInput input);
}
