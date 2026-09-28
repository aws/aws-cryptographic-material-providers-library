// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Operation handlers: decode the rpcv2Cbor request, delegate to the .NET
// AtomicPrimitives client, and encode the response. A library failure becomes a
// PrimitivesError; a malformed request becomes a GenericServerError.

using AWS.Cryptography.Primitives;

namespace PrimitivesTestServer;

internal sealed class Handlers
{
    private readonly AtomicPrimitives _client = new(new CryptoConfig());

    internal byte[] AesEncrypt(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new AESEncryptInput
        {
            EncAlg = AesGcm(Model.Str(map, "algorithm")),
            Iv = Blob(Model.Bytes(map, "iv")),
            Key = Blob(Model.Bytes(map, "key")),
            Msg = Blob(Model.Bytes(map, "message")),
            Aad = Blob(Model.Bytes(map, "aad")),
        };
        var output = Call(() => _client.AESEncrypt(input));
        return Model.WriteBlobs(("ciphertext", output.CipherText.ToArray()), ("authTag", output.AuthTag.ToArray()));
    }

    internal byte[] AesDecrypt(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new AESDecryptInput
        {
            EncAlg = AesGcm(Model.Str(map, "algorithm")),
            Key = Blob(Model.Bytes(map, "key")),
            CipherTxt = Blob(Model.Bytes(map, "ciphertext")),
            AuthTag = Blob(Model.Bytes(map, "authTag")),
            Iv = Blob(Model.Bytes(map, "iv")),
            Aad = Blob(Model.Bytes(map, "aad")),
        };
        var plaintext = Call(() => _client.AESDecrypt(input));
        return Model.WriteBlobs(("plaintext", plaintext.ToArray()));
    }

    internal byte[] GenerateRandomBytes(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new GenerateRandomBytesInput { Length = Model.Int(map, "length") };
        var data = Call(() => _client.GenerateRandomBytes(input));
        return Model.WriteBlobs(("data", data.ToArray()));
    }

    internal byte[] Digest(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new DigestInput
        {
            DigestAlgorithm = DigestAlg(Model.Str(map, "algorithm")),
            Message = Blob(Model.Bytes(map, "data")),
        };
        var digest = Call(() => _client.Digest(input));
        return Model.WriteBlobs(("digest", digest.ToArray()));
    }

    internal byte[] Hmac(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new HMacInput
        {
            DigestAlgorithm = DigestAlg(Model.Str(map, "algorithm")),
            Key = Blob(Model.Bytes(map, "key")),
            Message = Blob(Model.Bytes(map, "message")),
        };
        var digest = Call(() => _client.HMac(input));
        return Model.WriteBlobs(("digest", digest.ToArray()));
    }

    internal byte[] Hkdf(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new HkdfInput
        {
            DigestAlgorithm = DigestAlg(Model.Str(map, "algorithm")),
            Salt = Blob(Model.Bytes(map, "salt")),
            Ikm = Blob(Model.Bytes(map, "ikm")),
            Info = Blob(Model.Bytes(map, "info")),
            ExpectedLength = Model.Int(map, "expectedLength"),
        };
        var okm = Call(() => _client.Hkdf(input));
        return Model.WriteBlobs(("okm", okm.ToArray()));
    }

    internal byte[] KbkdfCtrHmac(byte[] body)
    {
        var map = Model.ReadMap(body);
        // KdfCounterMode derives its fixed input internally from nonce and
        // purpose; feature-config lists kbkdf-ctr-hmac as unsupported.
        var input = new KdfCtrInput
        {
            DigestAlgorithm = DigestAlg(Model.Str(map, "algorithm")),
            Ikm = Blob(Model.Bytes(map, "ikm")),
            ExpectedLength = Model.Int(map, "expectedLength"),
            Nonce = Blob(Model.Bytes(map, "info")),
        };
        var okm = Call(() => _client.KdfCounterMode(input));
        return Model.WriteBlobs(("okm", okm.ToArray()));
    }

    internal byte[] EcdsaGenerateKeyPair(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new GenerateECDSASignatureKeyInput { SignatureAlgorithm = EcdsaAlg(Model.Str(map, "algorithm")) };
        var output = Call(() => _client.GenerateECDSASignatureKey(input));
        return Model.WriteBlobs(("verificationKey", output.VerificationKey.ToArray()), ("signingKey", output.SigningKey.ToArray()));
    }

    internal byte[] EcdsaSign(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new ECDSASignInput
        {
            SignatureAlgorithm = EcdsaAlg(Model.Str(map, "algorithm")),
            SigningKey = Blob(Model.Bytes(map, "signingKey")),
            Message = Blob(Model.Bytes(map, "message")),
        };
        var signature = Call(() => _client.ECDSASign(input));
        return Model.WriteBlobs(("signature", signature.ToArray()));
    }

    internal byte[] EcdsaVerify(byte[] body)
    {
        var map = Model.ReadMap(body);
        var input = new ECDSAVerifyInput
        {
            SignatureAlgorithm = EcdsaAlg(Model.Str(map, "algorithm")),
            VerificationKey = Blob(Model.Bytes(map, "verificationKey")),
            Message = Blob(Model.Bytes(map, "message")),
            Signature = Blob(Model.Bytes(map, "signature")),
        };
        var valid = Call(() => _client.ECDSAVerify(input));
        return Model.WriteBool("valid", valid);
    }

    // Each AES-GCM variant fixes the key length; GCM uses a 12-byte IV and a
    // 16-byte tag.
    private static AES_GCM AesGcm(string algorithm) => algorithm switch
    {
        "AES_128_GCM" => new AES_GCM { KeyLength = 16, TagLength = 16, IvLength = 12 },
        "AES_192_GCM" => new AES_GCM { KeyLength = 24, TagLength = 16, IvLength = 12 },
        "AES_256_GCM" => new AES_GCM { KeyLength = 32, TagLength = 16, IvLength = 12 },
        _ => throw ServerErrorException.Generic($"unknown AES algorithm '{algorithm}'"),
    };

    private static DigestAlgorithm DigestAlg(string algorithm) => algorithm switch
    {
        "SHA_256" => DigestAlgorithm.SHA_256,
        "SHA_384" => DigestAlgorithm.SHA_384,
        "SHA_512" => DigestAlgorithm.SHA_512,
        _ => throw ServerErrorException.Generic($"unknown digest algorithm '{algorithm}'"),
    };

    private static ECDSASignatureAlgorithm EcdsaAlg(string algorithm) => algorithm switch
    {
        "ECDSA_P256" => ECDSASignatureAlgorithm.ECDSA_P256,
        "ECDSA_P384" => ECDSASignatureAlgorithm.ECDSA_P384,
        _ => throw ServerErrorException.Generic($"unknown ECDSA algorithm '{algorithm}'"),
    };

    private static MemoryStream Blob(byte[] bytes) => new(bytes);

    // Forwards a library failure as a PrimitivesError carrying its message.
    private static T Call<T>(Func<T> operation)
    {
        try
        {
            return operation();
        }
        catch (Exception e)
        {
            throw ServerErrorException.Primitives(Describe(e));
        }
    }

    private static string Describe(Exception exception)
    {
        var message = exception.Message;
        if (exception.InnerException != null)
        {
            message = $"{message} [encountered: {Describe(exception.InnerException)}]";
        }
        return message;
    }
}
