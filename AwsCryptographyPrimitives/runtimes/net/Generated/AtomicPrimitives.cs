// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using System.IO;
using System.Collections.Generic;
using AWS.Cryptography.Primitives;
using software.amazon.cryptography.primitives.internaldafny.types;
namespace AWS.Cryptography.Primitives
{
    public class AtomicPrimitives
    {
        private readonly software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient _impl;
        public AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient impl)
        {
            this._impl = impl;
        }
        public software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient impl()
        {
            return this._impl;
        }
        public AtomicPrimitives(AWS.Cryptography.Primitives.CryptoConfig input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._ICryptoConfig internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S12_CryptoConfig(input);
            var result = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            this._impl = result.dtor_value;
        }
        public System.IO.MemoryStream GenerateRandomBytes(AWS.Cryptography.Primitives.GenerateRandomBytesInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IGenerateRandomBytesInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S24_GenerateRandomBytesInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.GenerateRandomBytes(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S25_GenerateRandomBytesOutput(result.dtor_value);
        }
        public System.IO.MemoryStream Digest(AWS.Cryptography.Primitives.DigestInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IDigestInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S11_DigestInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.Digest(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S12_DigestOutput(result.dtor_value);
        }
        public System.IO.MemoryStream HMac(AWS.Cryptography.Primitives.HMacInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IHMacInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S9_HMacInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.HMac(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S10_HMacOutput(result.dtor_value);
        }
        public System.IO.MemoryStream HkdfExtract(AWS.Cryptography.Primitives.HkdfExtractInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IHkdfExtractInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S16_HkdfExtractInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.HkdfExtract(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S17_HkdfExtractOutput(result.dtor_value);
        }
        public System.IO.MemoryStream HkdfExpand(AWS.Cryptography.Primitives.HkdfExpandInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IHkdfExpandInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_HkdfExpandInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.HkdfExpand(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S16_HkdfExpandOutput(result.dtor_value);
        }
        public System.IO.MemoryStream Hkdf(AWS.Cryptography.Primitives.HkdfInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IHkdfInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S9_HkdfInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.Hkdf(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S10_HkdfOutput(result.dtor_value);
        }
        public System.IO.MemoryStream KdfCounterMode(AWS.Cryptography.Primitives.KdfCtrInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IKdfCtrInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S11_KdfCtrInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.KdfCounterMode(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S12_KdfCtrOutput(result.dtor_value);
        }
        public System.IO.MemoryStream AesKdfCounterMode(AWS.Cryptography.Primitives.AesKdfCtrInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IAesKdfCtrInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S14_AesKdfCtrInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.AesKdfCounterMode(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S15_AesKdfCtrOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.AESEncryptOutput AESEncrypt(AWS.Cryptography.Primitives.AESEncryptInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IAESEncryptInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_AESEncryptInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IAESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.AESEncrypt(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S16_AESEncryptOutput(result.dtor_value);
        }
        public System.IO.MemoryStream AESDecrypt(AWS.Cryptography.Primitives.AESDecryptInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IAESDecryptInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_AESDecryptInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.AESDecrypt(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S16_AESDecryptOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.GenerateRSAKeyPairOutput GenerateRSAKeyPair(AWS.Cryptography.Primitives.GenerateRSAKeyPairInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IGenerateRSAKeyPairInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S23_GenerateRSAKeyPairInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IGenerateRSAKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.GenerateRSAKeyPair(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S24_GenerateRSAKeyPairOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.GetRSAKeyModulusLengthOutput GetRSAKeyModulusLength(AWS.Cryptography.Primitives.GetRSAKeyModulusLengthInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IGetRSAKeyModulusLengthInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S27_GetRSAKeyModulusLengthInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IGetRSAKeyModulusLengthOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.GetRSAKeyModulusLength(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S28_GetRSAKeyModulusLengthOutput(result.dtor_value);
        }
        public System.IO.MemoryStream RSADecrypt(AWS.Cryptography.Primitives.RSADecryptInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IRSADecryptInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_RSADecryptInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.RSADecrypt(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S16_RSADecryptOutput(result.dtor_value);
        }
        public System.IO.MemoryStream RSAEncrypt(AWS.Cryptography.Primitives.RSAEncryptInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IRSAEncryptInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_RSAEncryptInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.RSAEncrypt(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S16_RSAEncryptOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.GenerateECDSASignatureKeyOutput GenerateECDSASignatureKey(AWS.Cryptography.Primitives.GenerateECDSASignatureKeyInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IGenerateECDSASignatureKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S30_GenerateECDSASignatureKeyInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IGenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.GenerateECDSASignatureKey(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S31_GenerateECDSASignatureKeyOutput(result.dtor_value);
        }
        public System.IO.MemoryStream ECDSASign(AWS.Cryptography.Primitives.ECDSASignInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IECDSASignInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S14_ECDSASignInput(input);
            Wrappers_Compile._IResult<Dafny.ISequence<byte>, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.ECDSASign(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S15_ECDSASignOutput(result.dtor_value);
        }
        public bool ECDSAVerify(AWS.Cryptography.Primitives.ECDSAVerifyInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IECDSAVerifyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S16_ECDSAVerifyInput(input);
            Wrappers_Compile._IResult<bool, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.ECDSAVerify(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S17_ECDSAVerifyOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.GenerateECCKeyPairOutput GenerateECCKeyPair(AWS.Cryptography.Primitives.GenerateECCKeyPairInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IGenerateECCKeyPairInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S23_GenerateECCKeyPairInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IGenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.GenerateECCKeyPair(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S24_GenerateECCKeyPairOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.GetPublicKeyFromPrivateKeyOutput GetPublicKeyFromPrivateKey(AWS.Cryptography.Primitives.GetPublicKeyFromPrivateKeyInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IGetPublicKeyFromPrivateKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S31_GetPublicKeyFromPrivateKeyInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IGetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.GetPublicKeyFromPrivateKey(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S32_GetPublicKeyFromPrivateKeyOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.ValidatePublicKeyOutput ValidatePublicKey(AWS.Cryptography.Primitives.ValidatePublicKeyInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IValidatePublicKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S22_ValidatePublicKeyInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.ValidatePublicKey(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S23_ValidatePublicKeyOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.DeriveSharedSecretOutput DeriveSharedSecret(AWS.Cryptography.Primitives.DeriveSharedSecretInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IDeriveSharedSecretInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S23_DeriveSharedSecretInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IDeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.DeriveSharedSecret(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S24_DeriveSharedSecretOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.CompressPublicKeyOutput CompressPublicKey(AWS.Cryptography.Primitives.CompressPublicKeyInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._ICompressPublicKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S22_CompressPublicKeyInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._ICompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.CompressPublicKey(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S23_CompressPublicKeyOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.DecompressPublicKeyOutput DecompressPublicKey(AWS.Cryptography.Primitives.DecompressPublicKeyInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IDecompressPublicKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S24_DecompressPublicKeyInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IDecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.DecompressPublicKey(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S25_DecompressPublicKeyOutput(result.dtor_value);
        }
        public AWS.Cryptography.Primitives.ParsePublicKeyOutput ParsePublicKey(AWS.Cryptography.Primitives.ParsePublicKeyInput input)
        {
            software.amazon.cryptography.primitives.internaldafny.types._IParsePublicKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N10_primitives__S19_ParsePublicKeyInput(input);
            Wrappers_Compile._IResult<software.amazon.cryptography.primitives.internaldafny.types._IParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types._IError> result = _impl.ParsePublicKey(internalInput);
            if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
            return TypeConversion.FromDafny_N3_aws__N12_cryptography__N10_primitives__S20_ParsePublicKeyOutput(result.dtor_value);
        }
    }
}
