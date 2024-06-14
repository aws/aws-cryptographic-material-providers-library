// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0


using System.Security.Cryptography;
using System.Text;
using Dafny;
using Org.BouncyCastle.Asn1;
using Org.BouncyCastle.Asn1.Pkcs;
using Org.BouncyCastle.Asn1.Sec;
using Org.BouncyCastle.Asn1.X509;
using Org.BouncyCastle.Asn1.X9;
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Crypto.Agreement;
using Org.BouncyCastle.Crypto.Generators;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Crypto.Signers;
using Org.BouncyCastle.Math;
using Org.BouncyCastle.OpenSsl;
using Org.BouncyCastle.Security;
using Org.BouncyCastle.Utilities;
using Org.BouncyCastle.Utilities.IO.Pem;
using Org.BouncyCastle.X509;
using software.amazon.cryptography.primitives.internaldafny.types;
using Wrappers_Compile;
using icharseq = Dafny.ISequence<char>;
using ibyteseq = Dafny.ISequence<byte>;
using byteseq = Dafny.Sequence<byte>;
using _IError = software.amazon.cryptography.primitives.internaldafny.types._IError;
using Asn1Object = ThirdParty.BouncyCastle.Asn1.Asn1Object;
using ECCurve = Org.BouncyCastle.Math.EC.ECCurve;
using ECPoint = Org.BouncyCastle.Math.EC.ECPoint;
using Error_Opaque = software.amazon.cryptography.primitives.internaldafny.types.Error_Opaque;
using PemReader = Org.BouncyCastle.OpenSsl.PemReader;
using PemWriter = Org.BouncyCastle.OpenSsl.PemWriter;
using X509Certificate = System.Security.Cryptography.X509Certificates.X509Certificate;

namespace ECDH
{
    public partial class KeyGeneration
    {
        public static _IResult<EccKeyPair, _IError> GenerateKeyPair(_IECDHCurveSpec curveSpec)
        {
            try
            {
                ECKeyPairGenerator generator = new ECKeyPairGenerator();
                SecureRandom rng = new SecureRandom();
                X9ECParameters p = ECCUtils.GetX9EcParameters(curveSpec);

                var domainParameters = new ECDomainParameters(p.Curve, p.G, p.N, p.H);
                generator.Init(new ECKeyGenerationParameters(domainParameters, rng));
                AsymmetricCipherKeyPair kp = generator.GenerateKeyPair();
                ECPublicKeyParameters publicKeyParameters = (ECPublicKeyParameters)kp.Public;
                // serialize the public and private keys, and then return them
                var publicKey = SerializePublicKey(kp, curveSpec);
                byte[] privateKey;
                ECCUtils.EncodePrivateKey(kp, out privateKey);

                return new Result_Success<EccKeyPair, _IError>(new EccKeyPair(byteseq.FromArray(privateKey), publicKey));
            }
            catch (Exception e)
            {
                return Result<EccKeyPair, _IError>
                    .create_Failure(new Error_Opaque(e));
            }
        }

        public static ibyteseq SerializePublicKey(AsymmetricCipherKeyPair kp, _IECDHCurveSpec curveSpec)
        {
            var lookUpOid = ECCUtils.OidLookUp(curveSpec);
            var ecPublicKeyParam = (ECPublicKeyParameters)kp.Public;
            var pubInfo = SubjectPublicKeyInfoFactory.CreateSubjectPublicKeyInfo(ecPublicKeyParam);

            var algId = new AlgorithmIdentifier(pubInfo.Algorithm.Algorithm, new DerObjectIdentifier(lookUpOid.Value));
            var spki = new SubjectPublicKeyInfo(algId, pubInfo.PublicKey);
            var spkiPublicKey = spki.GetDerEncoded();

            return byteseq.FromArray(spkiPublicKey);
        }

    }

    public partial class ECCUtils
    {
        public static _IResult<Dafny.ISequence<byte>, _IError> GetPublicKey(_IECDHCurveSpec curveSpec,
            _IECCPrivateKey privateKey)
        {
            try
            {
                X9ECParameters p = GetX9EcParameters(curveSpec);

                ECDomainParameters dp = new ECDomainParameters(p);
                ECPrivateKeyParameters skp = new ECPrivateKeyParameters(
                    ECCUtils.ParsePrivateKeyEccPemBytesToPrivateKey(privateKey.dtor_pem.CloneAsArray()),
                    dp);

                ECPoint Q = dp.G.Multiply(skp.D);
                ECPublicKeyParameters parameters = new ECPublicKeyParameters(Q, dp);

                var subjectPublicKeyInfo = SubjectPublicKeyInfoFactory.CreateSubjectPublicKeyInfo(parameters);

                var lookUpOid = OidLookUp(curveSpec);
                var algId = new AlgorithmIdentifier(subjectPublicKeyInfo.Algorithm.Algorithm, new DerObjectIdentifier(lookUpOid.Value));
                var spki = new SubjectPublicKeyInfo(algId, subjectPublicKeyInfo.PublicKey);
                var spkiPublicKey = spki.GetDerEncoded();
                return new Result_Success<ibyteseq, _IError>(byteseq.FromArray(spkiPublicKey));
            }
            catch (Exception e)
            {
                return Result<Dafny.ISequence<byte>, _IError>.create_Failure(new Error_Opaque(e));
            }

        }

        public static Oid OidLookUp(_IECDHCurveSpec curveSpec)
        {
            Oid o;
#if NETFRAMEWORK
            // in .net framework the oid name is different that in .net
            if (curveSpec.is_ECC__NIST__P256)
            {
                o = Oid.FromFriendlyName("ECDSA_P256", OidGroup.All);
            }
            else if (curveSpec.is_ECC__NIST__P384)
            {
                o = Oid.FromFriendlyName("ECDSA_P384", OidGroup.All);
            }
            else if (curveSpec.is_ECC__NIST__P521)
            {
                o = Oid.FromFriendlyName("ECDSA_P521", OidGroup.All);
            }
            else
            {
                throw new Exception("Curve not supported");
            }
#else
            if (curveSpec.is_ECC__NIST__P256)
            {
                o = Oid.FromFriendlyName("secp256r1", OidGroup.All);
            }
            else if (curveSpec.is_ECC__NIST__P384)
            {
                o = Oid.FromFriendlyName("secp384r1", OidGroup.All);
            }
            else if (curveSpec.is_ECC__NIST__P521)
            {
                o = Oid.FromFriendlyName("secp521r1", OidGroup.All);
            }
            else
            {
                throw new Exception("Curve not supported");
            }
#endif

            return o;
        }

        public static _IResult<bool, _IError> ValidatePublicKey(_IECDHCurveSpec curveSpec,
            Dafny.ISequence<byte> publicKey)
        {
            try
            {
                X9ECParameters p = GetX9EcParameters(curveSpec);

                ECDomainParameters dp = new ECDomainParameters(p.Curve, p.G, p.N, p.H);
                bool validPublicKey = NistPublicKeyValidationCriteria(publicKey.Elements, dp);
                return new Result_Success<bool, _IError>(validPublicKey);
            }
            catch (Exception e)
            {
                return Result<bool, _IError>.create_Failure(new Error_Opaque(e));
            }
        }

        private static bool NistPublicKeyValidationCriteria(byte[] publicKey, ECDomainParameters dp)
        {
            var spki = SubjectPublicKeyInfo.GetInstance(publicKey);
            var spkiPublicKey = spki.PublicKey.GetBytes();


            ECPublicKeyParameters publicKeyParameters = new ECPublicKeyParameters(dp.Curve.DecodePoint(spkiPublicKey), dp);

            ECPoint q = publicKeyParameters.Q;
            ECPoint pointOnCurve =
                publicKeyParameters.Parameters.Curve.ValidatePoint(q.AffineXCoord.ToBigInteger(),
                    q.AffineYCoord.ToBigInteger());

            return ValidatePointOnCurveIsNotInfinity(pointOnCurve) &&
                   CoordinateBetweenZeroAndP(pointOnCurve.AffineXCoord.ToBigInteger(), dp.Curve) &&
                   CoordinateBetweenZeroAndP(pointOnCurve.AffineYCoord.ToBigInteger(), dp.Curve);
        }

        private static bool ValidatePointOnCurveIsNotInfinity(ECPoint ecPoint)
        {
            return !ecPoint.IsInfinity;
        }

        private static bool CoordinateBetweenZeroAndP(BigInteger coordinate, ECCurve curve)
        {
            return coordinate.CompareTo(BigInteger.Zero) > 0 && coordinate.CompareTo(curve.Field.Characteristic) < 0;
        }

        public static void EncodePrivateKey(AsymmetricCipherKeyPair keyPair, out byte[] privateKeyBytes)
        {
            using (var stringWriter = new StringWriter())
            {
                var pemWriter = new PemWriter(stringWriter);
                pemWriter.WriteObject(keyPair.Private);
                privateKeyBytes = Encoding.UTF8.GetBytes(stringWriter.ToString());
            }
        }

        public static BigInteger ParsePrivateKeyEccPemBytesToPrivateKey(byte[] pemPrivateKey)
        {
            ECPrivateKeyParameters privateKey = ParsePrivateKeyPemBytes(pemPrivateKey);
            return privateKey.D;
        }

        private static ECPrivateKeyParameters ParsePrivateKeyPemBytes(byte[] pemPrivateKey)
        {
            using (var stringReader = new StringReader(Encoding.UTF8.GetString(pemPrivateKey)))
            {
                switch (new PemReader(stringReader).ReadObject())
                {
                    // These casts are for correctness.
                    // This is to return ECPrivateKey parameters,
                    // and these two types both extend from AsymmetricKeyParameter.
                    // But also other things do as well (elliptic curves),
                    // these checks are to make sure that we only get EC keys back.
                    case AsymmetricCipherKeyPair keypair:
                        var keyParams = (ECPrivateKeyParameters)keypair.Private;
                        return keyParams;
                    case ECPrivateKeyParameters keyParameter:
                        return keyParameter;
                    default:
                        throw new ArgumentException("PEM does not contain an EC private key.");
                }
            }
        }

        public static _IResult<ibyteseq, _IError> ParsePublicKey(ibyteseq dtorPublicKey)
        {
            try
            {
                var publicKeyBytes = dtorPublicKey.CloneAsArray();
                var subjectPublicKeyInfo = SubjectPublicKeyInfo.GetInstance(publicKeyBytes);
                var derEncodedPublicKey = subjectPublicKeyInfo.GetDerEncoded();
                return new Result_Success<ibyteseq, _IError>(byteseq.FromArray(derEncodedPublicKey));
            }
            catch (Exception e)
            {
                return Result<ibyteseq, _IError>.create_Failure(
                    new Error_AwsCryptographicPrimitivesError(Sequence<char>.FromArray(e.Message.ToCharArray()))
                    );
            }
        }

        public static _IResult<ibyteseq, _IError> DecompressPublicKey(ibyteseq dtorCompressedPublicKey, _IECDHCurveSpec dtorEccCurve)
        {
            try
            {
                X9ECParameters p = GetX9EcParameters(dtorEccCurve);

                ECDomainParameters dp = new ECDomainParameters(p.Curve, p.G, p.N, p.H);
                var compressedPublicKeyBytes = dtorCompressedPublicKey.CloneAsArray();
                ECPoint compressedPoint = dp.Curve.DecodePoint(compressedPublicKeyBytes);
                ECPublicKeyParameters publicKeyParameters = new ECPublicKeyParameters(compressedPoint, dp);
                var lookUpOid = OidLookUp(dtorEccCurve);
                var pubInfo = SubjectPublicKeyInfoFactory.CreateSubjectPublicKeyInfo(publicKeyParameters);

                var algId = new AlgorithmIdentifier(pubInfo.Algorithm.Algorithm, new DerObjectIdentifier(lookUpOid.Value));
                var spki = new SubjectPublicKeyInfo(algId, pubInfo.PublicKey);
                var spkiPublicKey = spki.GetDerEncoded();
                return new Result_Success<ibyteseq, _IError>(byteseq.FromArray(spkiPublicKey));
            }
            catch (Exception e)
            {
                return Result<ISequence<byte>, _IError>.create_Failure(new Error_Opaque(e));
            }
        }


        public static _IResult<ibyteseq, _IError> CompressPublicKey(ibyteseq dafnyPublicKey, _IECDHCurveSpec dtorEccCurve)
        {
            try
            {
                X9ECParameters p = GetX9EcParameters(dtorEccCurve);

                ECDomainParameters dp = new ECDomainParameters(p.Curve, p.G, p.N, p.H);
                var spki = SubjectPublicKeyInfo.GetInstance(dafnyPublicKey.CloneAsArray());
                var spkiPublicKey = spki.PublicKey.GetBytes();

                ECPublicKeyParameters publicKeyParameters = new ECPublicKeyParameters(dp.Curve.DecodePoint(spkiPublicKey), dp);
                return new Result_Success<ibyteseq, _IError>(byteseq.FromArray(publicKeyParameters.Q.GetEncoded(true)));
            }
            catch (Exception e)
            {
                return Result<ISequence<byte>, _IError>.create_Failure(new Error_Opaque(e));
            }
        }

        public static X9ECParameters GetX9EcParameters(_IECDHCurveSpec dtorEccCurve)
        {
            X9ECParameters p;
            if (dtorEccCurve.is_ECC__NIST__P256)
            {
                p = ECNamedCurveTable.GetByName("secp256r1");
            }
            else if (dtorEccCurve.is_ECC__NIST__P384)
            {
                p = ECNamedCurveTable.GetByName("secp384r1");
            }
            else if (dtorEccCurve.is_ECC__NIST__P521)
            {
                p = ECNamedCurveTable.GetByName("secp521r1");
            }
            else
            {
                throw new Exception($"Unsupported ECC Algorithm: {dtorEccCurve}");
            }
            return p;
        }
    }

    public partial class DeriveSharedSecret
    {
        public static _IResult<Dafny.ISequence<byte>, _IError> CalculateSharedSecret(_IECDHCurveSpec curveSpec,
            _IECCPrivateKey dafnyPrivateKey, _IECCPublicKey dafnyPublicKey)
        {
            try
            {
                X9ECParameters p = ECCUtils.GetX9EcParameters(curveSpec);

                ECDomainParameters dp = new ECDomainParameters(p.Curve, p.G, p.N, p.H);
                ECPrivateKeyParameters skp = new ECPrivateKeyParameters(ECCUtils.ParsePrivateKeyEccPemBytesToPrivateKey(dafnyPrivateKey.dtor_pem.CloneAsArray()), dp);

                ECPoint pt = p.Curve.DecodePoint(_fromBytesPublicKey((byte[])dafnyPublicKey.dtor_der.Elements.Clone(), dp));
                ECPublicKeyParameters rkp = new ECPublicKeyParameters(pt, dp);

                var ecdhKeyAgreement = new ECDHBasicAgreement();
                ecdhKeyAgreement.Init(skp);
                var sharedSecret = ecdhKeyAgreement.CalculateAgreement(rkp).ToByteArrayUnsigned();

                return new Result_Success<ibyteseq, _IError>(byteseq.FromArray(sharedSecret));
            }
            catch (Exception e)
            {
                return Result<ISequence<byte>, _IError>.create_Failure(new Error_Opaque(e));
            }
        }
        private static byte[] _fromBytesPublicKey(byte[] publicKeyBytes, ECDomainParameters dp)
        {
            var spki = SubjectPublicKeyInfo.GetInstance(publicKeyBytes);
            var spkiPublicKey = spki.PublicKey.GetBytes();

            ECPublicKeyParameters publicKeyParameters = new ECPublicKeyParameters(dp.Curve.DecodePoint(spkiPublicKey), dp);
            return publicKeyParameters.Q.GetEncoded();
        }
    }
}
