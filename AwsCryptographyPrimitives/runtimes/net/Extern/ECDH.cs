// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0


using Org.BouncyCastle.Asn1.X9;
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Crypto.Generators;
using Org.BouncyCastle.Security;
using software.amazon.cryptography.primitives.internaldafny.types;
using Wrappers_Compile;
using icharseq = Dafny.ISequence<char>;
using ibyteseq = Dafny.ISequence<byte>;
using byteseq = Dafny.Sequence<byte>;
using _IError = software.amazon.cryptography.primitives.internaldafny.types._IError;
using Error_Opaque = software.amazon.cryptography.primitives.internaldafny.types.Error_Opaque;

namespace ECDH
{
    public partial class KeyGeneration
    {
        static void Main()
        {
            GenerateKeyPair(new ECDHCurveSpec_ECC__NIST__P384());
        }
        public static _IResult<EccKeyPair, _IError> GenerateKeyPair(_IECDHCurveSpec x)
        {
            try
            {
                ECKeyPairGenerator generator = new ECKeyPairGenerator();
                SecureRandom rng = new SecureRandom();
                X9ECParameters p;
                if (x.is_ECC__NIST__P256)
                {
                    p = ECNamedCurveTable.GetByName("secp256r1");
                }
                else if (x.is_ECC__NIST__P384)
                {
                    p = ECNamedCurveTable.GetByName("secp384r1");
                }
                else if (x.is_ECC__NIST__P521)
                {
                    p = ECNamedCurveTable.GetByName("secp521r1");
                }
                else if (x.is_SM2)
                {
                    p = ECNamedCurveTable.GetByName("sm2p256v1");
                }
                else
                {
                    return Result<EccKeyPair, _IError>
                        .create_Failure(new Error_AwsCryptographicPrimitivesError(
                            Dafny.Sequence<char>.FromString(string.Format("Unsupported ECC Algorithm: {0}", x))));
                }

                AsymmetricCipherKeyPair k = generator.GenerateKeyPair();
            }
            catch (Exception e)
            {
                return Result<EccKeyPair, _IError>
                    .create_Failure(new Error_Opaque(e));
            }
            return Result<EccKeyPair, _IError>
                .create_Failure(new Error_Opaque("Implement me!"));
        }
    }
}
