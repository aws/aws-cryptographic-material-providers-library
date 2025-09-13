// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives;

import dafny.DafnySequence;
import java.lang.Boolean;
import java.lang.Byte;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.nio.ByteBuffer;
import software.amazon.cryptography.primitives.internaldafny.types.AES__CTR;
import software.amazon.cryptography.primitives.internaldafny.types.AES__GCM;
import software.amazon.cryptography.primitives.internaldafny.types.Error;
import software.amazon.cryptography.primitives.internaldafny.types.Error_AwsCryptographicPrimitivesError;
import software.amazon.cryptography.primitives.internaldafny.types.Error_CollectionOfErrors;
import software.amazon.cryptography.primitives.internaldafny.types.Error_Opaque;
import software.amazon.cryptography.primitives.internaldafny.types.Error_OpaqueWithText;
import software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient;
import software.amazon.cryptography.primitives.model.AESDecryptInput;
import software.amazon.cryptography.primitives.model.AESEncryptInput;
import software.amazon.cryptography.primitives.model.AESEncryptOutput;
import software.amazon.cryptography.primitives.model.AES_CTR;
import software.amazon.cryptography.primitives.model.AES_GCM;
import software.amazon.cryptography.primitives.model.AesKdfCtrInput;
import software.amazon.cryptography.primitives.model.AwsCryptographicPrimitivesError;
import software.amazon.cryptography.primitives.model.CollectionOfErrors;
import software.amazon.cryptography.primitives.model.CompressPublicKeyInput;
import software.amazon.cryptography.primitives.model.CompressPublicKeyOutput;
import software.amazon.cryptography.primitives.model.CryptoConfig;
import software.amazon.cryptography.primitives.model.DecompressPublicKeyInput;
import software.amazon.cryptography.primitives.model.DecompressPublicKeyOutput;
import software.amazon.cryptography.primitives.model.DeriveSharedSecretInput;
import software.amazon.cryptography.primitives.model.DeriveSharedSecretOutput;
import software.amazon.cryptography.primitives.model.DigestAlgorithm;
import software.amazon.cryptography.primitives.model.DigestInput;
import software.amazon.cryptography.primitives.model.ECCPrivateKey;
import software.amazon.cryptography.primitives.model.ECCPublicKey;
import software.amazon.cryptography.primitives.model.ECDHCurveSpec;
import software.amazon.cryptography.primitives.model.ECDSASignInput;
import software.amazon.cryptography.primitives.model.ECDSASignatureAlgorithm;
import software.amazon.cryptography.primitives.model.ECDSAVerifyInput;
import software.amazon.cryptography.primitives.model.GenerateECCKeyPairInput;
import software.amazon.cryptography.primitives.model.GenerateECCKeyPairOutput;
import software.amazon.cryptography.primitives.model.GenerateECDSASignatureKeyInput;
import software.amazon.cryptography.primitives.model.GenerateECDSASignatureKeyOutput;
import software.amazon.cryptography.primitives.model.GenerateRSAKeyPairInput;
import software.amazon.cryptography.primitives.model.GenerateRSAKeyPairOutput;
import software.amazon.cryptography.primitives.model.GenerateRandomBytesInput;
import software.amazon.cryptography.primitives.model.GetPublicKeyFromPrivateKeyInput;
import software.amazon.cryptography.primitives.model.GetPublicKeyFromPrivateKeyOutput;
import software.amazon.cryptography.primitives.model.GetRSAKeyModulusLengthInput;
import software.amazon.cryptography.primitives.model.GetRSAKeyModulusLengthOutput;
import software.amazon.cryptography.primitives.model.HMacInput;
import software.amazon.cryptography.primitives.model.HkdfExpandInput;
import software.amazon.cryptography.primitives.model.HkdfExtractInput;
import software.amazon.cryptography.primitives.model.HkdfInput;
import software.amazon.cryptography.primitives.model.KdfCtrInput;
import software.amazon.cryptography.primitives.model.OpaqueError;
import software.amazon.cryptography.primitives.model.OpaqueWithTextError;
import software.amazon.cryptography.primitives.model.ParsePublicKeyInput;
import software.amazon.cryptography.primitives.model.ParsePublicKeyOutput;
import software.amazon.cryptography.primitives.model.RSADecryptInput;
import software.amazon.cryptography.primitives.model.RSAEncryptInput;
import software.amazon.cryptography.primitives.model.RSAPaddingMode;
import software.amazon.cryptography.primitives.model.RSAPrivateKey;
import software.amazon.cryptography.primitives.model.RSAPublicKey;
import software.amazon.cryptography.primitives.model.ValidatePublicKeyInput;
import software.amazon.cryptography.primitives.model.ValidatePublicKeyOutput;

public class ToNative {

  public static OpaqueError Error(Error_Opaque dafnyValue) {
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue.dtor_obj());
    return nativeBuilder.build();
  }

  public static OpaqueWithTextError Error(Error_OpaqueWithText dafnyValue) {
    OpaqueWithTextError.Builder nativeBuilder = OpaqueWithTextError.builder();
    nativeBuilder.obj(dafnyValue.dtor_obj());
    nativeBuilder.objMessage(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_objMessage()
      )
    );
    return nativeBuilder.build();
  }

  public static CollectionOfErrors Error(Error_CollectionOfErrors dafnyValue) {
    CollectionOfErrors.Builder nativeBuilder = CollectionOfErrors.builder();
    nativeBuilder.list(
      software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToList(
        dafnyValue.dtor_list(),
        ToNative::Error
      )
    );
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static AwsCryptographicPrimitivesError Error(
    Error_AwsCryptographicPrimitivesError dafnyValue
  ) {
    AwsCryptographicPrimitivesError.Builder nativeBuilder =
      AwsCryptographicPrimitivesError.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static RuntimeException Error(Error dafnyValue) {
    if (dafnyValue.is_AwsCryptographicPrimitivesError()) {
      return ToNative.Error((Error_AwsCryptographicPrimitivesError) dafnyValue);
    }
    if (dafnyValue.is_Opaque()) {
      return ToNative.Error((Error_Opaque) dafnyValue);
    }
    if (dafnyValue.is_OpaqueWithText()) {
      return ToNative.Error((Error_OpaqueWithText) dafnyValue);
    }
    if (dafnyValue.is_CollectionOfErrors()) {
      return ToNative.Error((Error_CollectionOfErrors) dafnyValue);
    }
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue);
    return nativeBuilder.build();
  }

  public static AES_CTR AES_CTR(AES__CTR dafnyValue) {
    AES_CTR.Builder nativeBuilder = AES_CTR.builder();
    nativeBuilder.keyLength((dafnyValue.dtor_keyLength()));
    nativeBuilder.nonceLength((dafnyValue.dtor_nonceLength()));
    return nativeBuilder.build();
  }

  public static AES_GCM AES_GCM(AES__GCM dafnyValue) {
    AES_GCM.Builder nativeBuilder = AES_GCM.builder();
    nativeBuilder.keyLength((dafnyValue.dtor_keyLength()));
    nativeBuilder.tagLength((dafnyValue.dtor_tagLength()));
    nativeBuilder.ivLength((dafnyValue.dtor_ivLength()));
    return nativeBuilder.build();
  }

  public static AESDecryptInput AESDecryptInput(
    software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput dafnyValue
  ) {
    AESDecryptInput.Builder nativeBuilder = AESDecryptInput.builder();
    nativeBuilder.encAlg(ToNative.AES_GCM(dafnyValue.dtor_encAlg()));
    nativeBuilder.key(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_key()
      )
    );
    nativeBuilder.cipherTxt(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_cipherTxt()
      )
    );
    nativeBuilder.authTag(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_authTag()
      )
    );
    nativeBuilder.iv(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_iv()
      )
    );
    nativeBuilder.aad(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_aad()
      )
    );
    return nativeBuilder.build();
  }

  public static ByteBuffer AESDecryptOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static AESEncryptInput AESEncryptInput(
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput dafnyValue
  ) {
    AESEncryptInput.Builder nativeBuilder = AESEncryptInput.builder();
    nativeBuilder.encAlg(ToNative.AES_GCM(dafnyValue.dtor_encAlg()));
    nativeBuilder.iv(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_iv()
      )
    );
    nativeBuilder.key(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_key()
      )
    );
    nativeBuilder.msg(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_msg()
      )
    );
    nativeBuilder.aad(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_aad()
      )
    );
    return nativeBuilder.build();
  }

  public static AESEncryptOutput AESEncryptOutput(
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput dafnyValue
  ) {
    AESEncryptOutput.Builder nativeBuilder = AESEncryptOutput.builder();
    nativeBuilder.cipherText(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_cipherText()
      )
    );
    nativeBuilder.authTag(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_authTag()
      )
    );
    return nativeBuilder.build();
  }

  public static AesKdfCtrInput AesKdfCtrInput(
    software.amazon.cryptography.primitives.internaldafny.types.AesKdfCtrInput dafnyValue
  ) {
    AesKdfCtrInput.Builder nativeBuilder = AesKdfCtrInput.builder();
    nativeBuilder.ikm(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_ikm()
      )
    );
    nativeBuilder.expectedLength((dafnyValue.dtor_expectedLength()));
    if (dafnyValue.dtor_nonce().is_Some()) {
      nativeBuilder.nonce(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyValue.dtor_nonce().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static ByteBuffer AesKdfCtrOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static CompressPublicKeyInput CompressPublicKeyInput(
    software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyInput dafnyValue
  ) {
    CompressPublicKeyInput.Builder nativeBuilder =
      CompressPublicKeyInput.builder();
    nativeBuilder.publicKey(ToNative.ECCPublicKey(dafnyValue.dtor_publicKey()));
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    return nativeBuilder.build();
  }

  public static CompressPublicKeyOutput CompressPublicKeyOutput(
    software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput dafnyValue
  ) {
    CompressPublicKeyOutput.Builder nativeBuilder =
      CompressPublicKeyOutput.builder();
    nativeBuilder.compressedPublicKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_compressedPublicKey()
      )
    );
    return nativeBuilder.build();
  }

  public static CryptoConfig CryptoConfig(
    software.amazon.cryptography.primitives.internaldafny.types.CryptoConfig dafnyValue
  ) {
    CryptoConfig.Builder nativeBuilder = CryptoConfig.builder();
    return nativeBuilder.build();
  }

  public static DecompressPublicKeyInput DecompressPublicKeyInput(
    software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyInput dafnyValue
  ) {
    DecompressPublicKeyInput.Builder nativeBuilder =
      DecompressPublicKeyInput.builder();
    nativeBuilder.compressedPublicKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_compressedPublicKey()
      )
    );
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    return nativeBuilder.build();
  }

  public static DecompressPublicKeyOutput DecompressPublicKeyOutput(
    software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput dafnyValue
  ) {
    DecompressPublicKeyOutput.Builder nativeBuilder =
      DecompressPublicKeyOutput.builder();
    nativeBuilder.publicKey(ToNative.ECCPublicKey(dafnyValue.dtor_publicKey()));
    return nativeBuilder.build();
  }

  public static DeriveSharedSecretInput DeriveSharedSecretInput(
    software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput dafnyValue
  ) {
    DeriveSharedSecretInput.Builder nativeBuilder =
      DeriveSharedSecretInput.builder();
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    nativeBuilder.privateKey(
      ToNative.ECCPrivateKey(dafnyValue.dtor_privateKey())
    );
    nativeBuilder.publicKey(ToNative.ECCPublicKey(dafnyValue.dtor_publicKey()));
    return nativeBuilder.build();
  }

  public static DeriveSharedSecretOutput DeriveSharedSecretOutput(
    software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput dafnyValue
  ) {
    DeriveSharedSecretOutput.Builder nativeBuilder =
      DeriveSharedSecretOutput.builder();
    nativeBuilder.sharedSecret(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_sharedSecret()
      )
    );
    return nativeBuilder.build();
  }

  public static DigestInput DigestInput(
    software.amazon.cryptography.primitives.internaldafny.types.DigestInput dafnyValue
  ) {
    DigestInput.Builder nativeBuilder = DigestInput.builder();
    nativeBuilder.digestAlgorithm(
      ToNative.DigestAlgorithm(dafnyValue.dtor_digestAlgorithm())
    );
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static ByteBuffer DigestOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static ECCPrivateKey ECCPrivateKey(
    software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey dafnyValue
  ) {
    ECCPrivateKey.Builder nativeBuilder = ECCPrivateKey.builder();
    nativeBuilder.pem(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_pem()
      )
    );
    return nativeBuilder.build();
  }

  public static ECCPublicKey ECCPublicKey(
    software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey dafnyValue
  ) {
    ECCPublicKey.Builder nativeBuilder = ECCPublicKey.builder();
    nativeBuilder.der(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_der()
      )
    );
    return nativeBuilder.build();
  }

  public static ECDSASignInput ECDSASignInput(
    software.amazon.cryptography.primitives.internaldafny.types.ECDSASignInput dafnyValue
  ) {
    ECDSASignInput.Builder nativeBuilder = ECDSASignInput.builder();
    nativeBuilder.signatureAlgorithm(
      ToNative.ECDSASignatureAlgorithm(dafnyValue.dtor_signatureAlgorithm())
    );
    nativeBuilder.signingKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_signingKey()
      )
    );
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static ByteBuffer ECDSASignOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static ECDSAVerifyInput ECDSAVerifyInput(
    software.amazon.cryptography.primitives.internaldafny.types.ECDSAVerifyInput dafnyValue
  ) {
    ECDSAVerifyInput.Builder nativeBuilder = ECDSAVerifyInput.builder();
    nativeBuilder.signatureAlgorithm(
      ToNative.ECDSASignatureAlgorithm(dafnyValue.dtor_signatureAlgorithm())
    );
    nativeBuilder.verificationKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_verificationKey()
      )
    );
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_message()
      )
    );
    nativeBuilder.signature(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_signature()
      )
    );
    return nativeBuilder.build();
  }

  public static Boolean ECDSAVerifyOutput(Boolean dafnyValue) {
    return (dafnyValue);
  }

  public static GenerateECCKeyPairInput GenerateECCKeyPairInput(
    software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput dafnyValue
  ) {
    GenerateECCKeyPairInput.Builder nativeBuilder =
      GenerateECCKeyPairInput.builder();
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    return nativeBuilder.build();
  }

  public static GenerateECCKeyPairOutput GenerateECCKeyPairOutput(
    software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput dafnyValue
  ) {
    GenerateECCKeyPairOutput.Builder nativeBuilder =
      GenerateECCKeyPairOutput.builder();
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    nativeBuilder.privateKey(
      ToNative.ECCPrivateKey(dafnyValue.dtor_privateKey())
    );
    nativeBuilder.publicKey(ToNative.ECCPublicKey(dafnyValue.dtor_publicKey()));
    return nativeBuilder.build();
  }

  public static GenerateECDSASignatureKeyInput GenerateECDSASignatureKeyInput(
    software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyInput dafnyValue
  ) {
    GenerateECDSASignatureKeyInput.Builder nativeBuilder =
      GenerateECDSASignatureKeyInput.builder();
    nativeBuilder.signatureAlgorithm(
      ToNative.ECDSASignatureAlgorithm(dafnyValue.dtor_signatureAlgorithm())
    );
    return nativeBuilder.build();
  }

  public static GenerateECDSASignatureKeyOutput GenerateECDSASignatureKeyOutput(
    software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput dafnyValue
  ) {
    GenerateECDSASignatureKeyOutput.Builder nativeBuilder =
      GenerateECDSASignatureKeyOutput.builder();
    nativeBuilder.signatureAlgorithm(
      ToNative.ECDSASignatureAlgorithm(dafnyValue.dtor_signatureAlgorithm())
    );
    nativeBuilder.verificationKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_verificationKey()
      )
    );
    nativeBuilder.signingKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_signingKey()
      )
    );
    return nativeBuilder.build();
  }

  public static GenerateRandomBytesInput GenerateRandomBytesInput(
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput dafnyValue
  ) {
    GenerateRandomBytesInput.Builder nativeBuilder =
      GenerateRandomBytesInput.builder();
    nativeBuilder.length((dafnyValue.dtor_length()));
    return nativeBuilder.build();
  }

  public static ByteBuffer GenerateRandomBytesOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static GenerateRSAKeyPairInput GenerateRSAKeyPairInput(
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairInput dafnyValue
  ) {
    GenerateRSAKeyPairInput.Builder nativeBuilder =
      GenerateRSAKeyPairInput.builder();
    nativeBuilder.lengthBits((dafnyValue.dtor_lengthBits()));
    return nativeBuilder.build();
  }

  public static GenerateRSAKeyPairOutput GenerateRSAKeyPairOutput(
    software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput dafnyValue
  ) {
    GenerateRSAKeyPairOutput.Builder nativeBuilder =
      GenerateRSAKeyPairOutput.builder();
    nativeBuilder.publicKey(ToNative.RSAPublicKey(dafnyValue.dtor_publicKey()));
    nativeBuilder.privateKey(
      ToNative.RSAPrivateKey(dafnyValue.dtor_privateKey())
    );
    return nativeBuilder.build();
  }

  public static GetPublicKeyFromPrivateKeyInput GetPublicKeyFromPrivateKeyInput(
    software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyInput dafnyValue
  ) {
    GetPublicKeyFromPrivateKeyInput.Builder nativeBuilder =
      GetPublicKeyFromPrivateKeyInput.builder();
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    nativeBuilder.privateKey(
      ToNative.ECCPrivateKey(dafnyValue.dtor_privateKey())
    );
    return nativeBuilder.build();
  }

  public static GetPublicKeyFromPrivateKeyOutput GetPublicKeyFromPrivateKeyOutput(
    software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput dafnyValue
  ) {
    GetPublicKeyFromPrivateKeyOutput.Builder nativeBuilder =
      GetPublicKeyFromPrivateKeyOutput.builder();
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    nativeBuilder.privateKey(
      ToNative.ECCPrivateKey(dafnyValue.dtor_privateKey())
    );
    nativeBuilder.publicKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_publicKey()
      )
    );
    return nativeBuilder.build();
  }

  public static GetRSAKeyModulusLengthInput GetRSAKeyModulusLengthInput(
    software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthInput dafnyValue
  ) {
    GetRSAKeyModulusLengthInput.Builder nativeBuilder =
      GetRSAKeyModulusLengthInput.builder();
    nativeBuilder.publicKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_publicKey()
      )
    );
    return nativeBuilder.build();
  }

  public static GetRSAKeyModulusLengthOutput GetRSAKeyModulusLengthOutput(
    software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput dafnyValue
  ) {
    GetRSAKeyModulusLengthOutput.Builder nativeBuilder =
      GetRSAKeyModulusLengthOutput.builder();
    nativeBuilder.length((dafnyValue.dtor_length()));
    return nativeBuilder.build();
  }

  public static HkdfExpandInput HkdfExpandInput(
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput dafnyValue
  ) {
    HkdfExpandInput.Builder nativeBuilder = HkdfExpandInput.builder();
    nativeBuilder.digestAlgorithm(
      ToNative.DigestAlgorithm(dafnyValue.dtor_digestAlgorithm())
    );
    nativeBuilder.prk(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_prk()
      )
    );
    nativeBuilder.info(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_info()
      )
    );
    nativeBuilder.expectedLength((dafnyValue.dtor_expectedLength()));
    return nativeBuilder.build();
  }

  public static ByteBuffer HkdfExpandOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static HkdfExtractInput HkdfExtractInput(
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput dafnyValue
  ) {
    HkdfExtractInput.Builder nativeBuilder = HkdfExtractInput.builder();
    nativeBuilder.digestAlgorithm(
      ToNative.DigestAlgorithm(dafnyValue.dtor_digestAlgorithm())
    );
    if (dafnyValue.dtor_salt().is_Some()) {
      nativeBuilder.salt(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyValue.dtor_salt().dtor_value()
        )
      );
    }
    nativeBuilder.ikm(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_ikm()
      )
    );
    return nativeBuilder.build();
  }

  public static ByteBuffer HkdfExtractOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static HkdfInput HkdfInput(
    software.amazon.cryptography.primitives.internaldafny.types.HkdfInput dafnyValue
  ) {
    HkdfInput.Builder nativeBuilder = HkdfInput.builder();
    nativeBuilder.digestAlgorithm(
      ToNative.DigestAlgorithm(dafnyValue.dtor_digestAlgorithm())
    );
    if (dafnyValue.dtor_salt().is_Some()) {
      nativeBuilder.salt(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyValue.dtor_salt().dtor_value()
        )
      );
    }
    nativeBuilder.ikm(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_ikm()
      )
    );
    nativeBuilder.info(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_info()
      )
    );
    nativeBuilder.expectedLength((dafnyValue.dtor_expectedLength()));
    return nativeBuilder.build();
  }

  public static ByteBuffer HkdfOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static HMacInput HMacInput(
    software.amazon.cryptography.primitives.internaldafny.types.HMacInput dafnyValue
  ) {
    HMacInput.Builder nativeBuilder = HMacInput.builder();
    nativeBuilder.digestAlgorithm(
      ToNative.DigestAlgorithm(dafnyValue.dtor_digestAlgorithm())
    );
    nativeBuilder.key(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_key()
      )
    );
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static ByteBuffer HMacOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static KdfCtrInput KdfCtrInput(
    software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput dafnyValue
  ) {
    KdfCtrInput.Builder nativeBuilder = KdfCtrInput.builder();
    nativeBuilder.digestAlgorithm(
      ToNative.DigestAlgorithm(dafnyValue.dtor_digestAlgorithm())
    );
    nativeBuilder.ikm(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_ikm()
      )
    );
    nativeBuilder.expectedLength((dafnyValue.dtor_expectedLength()));
    if (dafnyValue.dtor_purpose().is_Some()) {
      nativeBuilder.purpose(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyValue.dtor_purpose().dtor_value()
        )
      );
    }
    if (dafnyValue.dtor_nonce().is_Some()) {
      nativeBuilder.nonce(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyValue.dtor_nonce().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static ByteBuffer KdfCtrOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static ParsePublicKeyInput ParsePublicKeyInput(
    software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyInput dafnyValue
  ) {
    ParsePublicKeyInput.Builder nativeBuilder = ParsePublicKeyInput.builder();
    nativeBuilder.publicKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_publicKey()
      )
    );
    return nativeBuilder.build();
  }

  public static ParsePublicKeyOutput ParsePublicKeyOutput(
    software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput dafnyValue
  ) {
    ParsePublicKeyOutput.Builder nativeBuilder = ParsePublicKeyOutput.builder();
    nativeBuilder.publicKey(ToNative.ECCPublicKey(dafnyValue.dtor_publicKey()));
    return nativeBuilder.build();
  }

  public static RSADecryptInput RSADecryptInput(
    software.amazon.cryptography.primitives.internaldafny.types.RSADecryptInput dafnyValue
  ) {
    RSADecryptInput.Builder nativeBuilder = RSADecryptInput.builder();
    nativeBuilder.padding(ToNative.RSAPaddingMode(dafnyValue.dtor_padding()));
    nativeBuilder.privateKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_privateKey()
      )
    );
    nativeBuilder.cipherText(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_cipherText()
      )
    );
    return nativeBuilder.build();
  }

  public static ByteBuffer RSADecryptOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static RSAEncryptInput RSAEncryptInput(
    software.amazon.cryptography.primitives.internaldafny.types.RSAEncryptInput dafnyValue
  ) {
    RSAEncryptInput.Builder nativeBuilder = RSAEncryptInput.builder();
    nativeBuilder.padding(ToNative.RSAPaddingMode(dafnyValue.dtor_padding()));
    nativeBuilder.publicKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_publicKey()
      )
    );
    nativeBuilder.plaintext(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_plaintext()
      )
    );
    return nativeBuilder.build();
  }

  public static ByteBuffer RSAEncryptOutput(
    DafnySequence<? extends Byte> dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
      dafnyValue
    );
  }

  public static RSAPrivateKey RSAPrivateKey(
    software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey dafnyValue
  ) {
    RSAPrivateKey.Builder nativeBuilder = RSAPrivateKey.builder();
    nativeBuilder.lengthBits((dafnyValue.dtor_lengthBits()));
    nativeBuilder.pem(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_pem()
      )
    );
    return nativeBuilder.build();
  }

  public static RSAPublicKey RSAPublicKey(
    software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey dafnyValue
  ) {
    RSAPublicKey.Builder nativeBuilder = RSAPublicKey.builder();
    nativeBuilder.lengthBits((dafnyValue.dtor_lengthBits()));
    nativeBuilder.pem(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_pem()
      )
    );
    return nativeBuilder.build();
  }

  public static ValidatePublicKeyInput ValidatePublicKeyInput(
    software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyInput dafnyValue
  ) {
    ValidatePublicKeyInput.Builder nativeBuilder =
      ValidatePublicKeyInput.builder();
    nativeBuilder.eccCurve(ToNative.ECDHCurveSpec(dafnyValue.dtor_eccCurve()));
    nativeBuilder.publicKey(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
        dafnyValue.dtor_publicKey()
      )
    );
    return nativeBuilder.build();
  }

  public static ValidatePublicKeyOutput ValidatePublicKeyOutput(
    software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput dafnyValue
  ) {
    ValidatePublicKeyOutput.Builder nativeBuilder =
      ValidatePublicKeyOutput.builder();
    nativeBuilder.success((dafnyValue.dtor_success()));
    return nativeBuilder.build();
  }

  public static DigestAlgorithm DigestAlgorithm(
    software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm dafnyValue
  ) {
    if (dafnyValue.is_SHA__512()) {
      return DigestAlgorithm.SHA_512;
    }
    if (dafnyValue.is_SHA__384()) {
      return DigestAlgorithm.SHA_384;
    }
    if (dafnyValue.is_SHA__256()) {
      return DigestAlgorithm.SHA_256;
    }
    throw new IllegalArgumentException(
      "No entry of software.amazon.cryptography.primitives.model.DigestAlgorithm matches the input : " +
      dafnyValue
    );
  }

  public static ECDHCurveSpec ECDHCurveSpec(
    software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec dafnyValue
  ) {
    if (dafnyValue.is_ECC__NIST__P256()) {
      return ECDHCurveSpec.ECC_NIST_P256;
    }
    if (dafnyValue.is_ECC__NIST__P384()) {
      return ECDHCurveSpec.ECC_NIST_P384;
    }
    if (dafnyValue.is_ECC__NIST__P521()) {
      return ECDHCurveSpec.ECC_NIST_P521;
    }
    if (dafnyValue.is_SM2()) {
      return ECDHCurveSpec.SM2;
    }
    throw new IllegalArgumentException(
      "No entry of software.amazon.cryptography.primitives.model.ECDHCurveSpec matches the input : " +
      dafnyValue
    );
  }

  public static ECDSASignatureAlgorithm ECDSASignatureAlgorithm(
    software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm dafnyValue
  ) {
    if (dafnyValue.is_ECDSA__P384()) {
      return ECDSASignatureAlgorithm.ECDSA_P384;
    }
    if (dafnyValue.is_ECDSA__P256()) {
      return ECDSASignatureAlgorithm.ECDSA_P256;
    }
    throw new IllegalArgumentException(
      "No entry of software.amazon.cryptography.primitives.model.ECDSASignatureAlgorithm matches the input : " +
      dafnyValue
    );
  }

  public static RSAPaddingMode RSAPaddingMode(
    software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode dafnyValue
  ) {
    if (dafnyValue.is_PKCS1()) {
      return RSAPaddingMode.PKCS1;
    }
    if (dafnyValue.is_OAEP__SHA1()) {
      return RSAPaddingMode.OAEP_SHA1;
    }
    if (dafnyValue.is_OAEP__SHA256()) {
      return RSAPaddingMode.OAEP_SHA256;
    }
    if (dafnyValue.is_OAEP__SHA384()) {
      return RSAPaddingMode.OAEP_SHA384;
    }
    if (dafnyValue.is_OAEP__SHA512()) {
      return RSAPaddingMode.OAEP_SHA512;
    }
    throw new IllegalArgumentException(
      "No entry of software.amazon.cryptography.primitives.model.RSAPaddingMode matches the input : " +
      dafnyValue
    );
  }

  public static AtomicPrimitives AwsCryptographicPrimitives(
    IAwsCryptographicPrimitivesClient dafnyValue
  ) {
    return new AtomicPrimitives(dafnyValue);
  }
}
