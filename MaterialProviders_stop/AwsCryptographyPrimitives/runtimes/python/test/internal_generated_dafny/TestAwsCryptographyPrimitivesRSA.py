import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
import StandardLibrary
import UTF8
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import AesKdfCtr
import TestAwsCryptographyPrimitivesAesKdfCtr
import TestAwsCryptographyPrimitivesHMacDigest
import TestAwsCryptographyPrimitivesDigest
import TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesAES

assert "TestAwsCryptographyPrimitivesRSA" == __name__
TestAwsCryptographyPrimitivesRSA = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RSAEncryptTests():
        d_38_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_39_valueOrError0_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_39_valueOrError0_ = out8_
        if not(not((d_39_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(51,15): " + _dafny.string_of(d_39_valueOrError0_))
        d_38_client_ = (d_39_valueOrError0_).Extract()
        d_40_keys_: Wrappers.Result
        out9_: Wrappers.Result
        out9_ = (d_38_client_).GenerateRSAKeyPair(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(2048))
        d_40_keys_ = out9_
        if not((d_40_keys_).is_Success):
            raise _dafny.HaltException("test/TestRSA.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        TestAwsCryptographyPrimitivesRSA.default__.BasicRSAEncryptTest(software_amazon_cryptography_primitives_internaldafny_types.RSAEncryptInput_RSAEncryptInput(software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA256(), (((d_40_keys_).value).publicKey).pem, _dafny.Seq([97, 115, 100, 102])), (d_40_keys_).value)

    @staticmethod
    def GetRSAKeyModulusLength():
        d_41_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_42_valueOrError0_: Wrappers.Result = None
        out10_: Wrappers.Result
        out10_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_42_valueOrError0_ = out10_
        if not(not((d_42_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(67,15): " + _dafny.string_of(d_42_valueOrError0_))
        d_41_client_ = (d_42_valueOrError0_).Extract()
        d_43_publicKey2048_: _dafny.Seq
        d_44_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_44_valueOrError1_ = UTF8.default__.Encode((TestAwsCryptographyPrimitivesRSA.default__).RSA__PUBLIC__2048)
        if not(not((d_44_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(71,22): " + _dafny.string_of(d_44_valueOrError1_))
        d_43_publicKey2048_ = (d_44_valueOrError1_).Extract()
        d_45_length2048_: software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput
        d_46_valueOrError2_: Wrappers.Result = None
        d_46_valueOrError2_ = (d_41_client_).GetRSAKeyModulusLength(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(d_43_publicKey2048_))
        if not(not((d_46_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(72,19): " + _dafny.string_of(d_46_valueOrError2_))
        d_45_length2048_ = (d_46_valueOrError2_).Extract()
        if not(((d_45_length2048_).length) == (2048)):
            raise _dafny.HaltException("test/TestRSA.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_47_publicKey3072_: _dafny.Seq
        d_48_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_48_valueOrError3_ = UTF8.default__.Encode((TestAwsCryptographyPrimitivesRSA.default__).RSA__PUBLIC__3072)
        if not(not((d_48_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(77,22): " + _dafny.string_of(d_48_valueOrError3_))
        d_47_publicKey3072_ = (d_48_valueOrError3_).Extract()
        d_49_length3072_: software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput
        d_50_valueOrError4_: Wrappers.Result = None
        d_50_valueOrError4_ = (d_41_client_).GetRSAKeyModulusLength(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(d_47_publicKey3072_))
        if not(not((d_50_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(78,19): " + _dafny.string_of(d_50_valueOrError4_))
        d_49_length3072_ = (d_50_valueOrError4_).Extract()
        if not(((d_49_length3072_).length) == (3072)):
            raise _dafny.HaltException("test/TestRSA.dfy(80,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_51_publicKey4096_: _dafny.Seq
        d_52_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_52_valueOrError5_ = UTF8.default__.Encode((TestAwsCryptographyPrimitivesRSA.default__).RSA__PUBLIC__4096)
        if not(not((d_52_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(83,22): " + _dafny.string_of(d_52_valueOrError5_))
        d_51_publicKey4096_ = (d_52_valueOrError5_).Extract()
        d_53_length4096_: software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput
        d_54_valueOrError6_: Wrappers.Result = None
        d_54_valueOrError6_ = (d_41_client_).GetRSAKeyModulusLength(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(d_51_publicKey4096_))
        if not(not((d_54_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(84,19): " + _dafny.string_of(d_54_valueOrError6_))
        d_53_length4096_ = (d_54_valueOrError6_).Extract()
        if not(((d_53_length4096_).length) == (4096)):
            raise _dafny.HaltException("test/TestRSA.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicRSADecryptTests(input, expectedOutput):
        d_55_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_56_valueOrError0_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_56_valueOrError0_ = out11_
        if not(not((d_56_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(94,15): " + _dafny.string_of(d_56_valueOrError0_))
        d_55_client_ = (d_56_valueOrError0_).Extract()
        d_57_output_: _dafny.Seq
        d_58_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out12_: Wrappers.Result
        out12_ = (d_55_client_).RSADecrypt(input)
        d_58_valueOrError1_ = out12_
        if not(not((d_58_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(95,15): " + _dafny.string_of(d_58_valueOrError1_))
        d_57_output_ = (d_58_valueOrError1_).Extract()
        if not((d_57_output_) == (expectedOutput)):
            raise _dafny.HaltException("test/TestRSA.dfy(97,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicRSAEncryptTest(input, keypair):
        d_59_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_60_valueOrError0_: Wrappers.Result = None
        out13_: Wrappers.Result
        out13_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_60_valueOrError0_ = out13_
        if not(not((d_60_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(106,15): " + _dafny.string_of(d_60_valueOrError0_))
        d_59_client_ = (d_60_valueOrError0_).Extract()
        d_61_output_: _dafny.Seq
        d_62_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out14_: Wrappers.Result
        out14_ = (d_59_client_).RSAEncrypt(input)
        d_62_valueOrError1_ = out14_
        if not(not((d_62_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(107,15): " + _dafny.string_of(d_62_valueOrError1_))
        d_61_output_ = (d_62_valueOrError1_).Extract()
        d_63_decryptInput_: software_amazon_cryptography_primitives_internaldafny_types.RSADecryptInput
        d_63_decryptInput_ = software_amazon_cryptography_primitives_internaldafny_types.RSADecryptInput_RSADecryptInput((input).padding, ((keypair).privateKey).pem, d_61_output_)
        TestAwsCryptographyPrimitivesRSA.default__.BasicRSADecryptTests(d_63_decryptInput_, (input).plaintext)

    @staticmethod
    def TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM():
        d_64_allPadding_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
            for compr_0_ in software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode.AllSingletonConstructors:
                d_65_p_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode = compr_0_
                if True:
                    coll0_ = coll0_.union(_dafny.Set([d_65_p_]))
            return _dafny.Set(coll0_)
        d_64_allPadding_ = iife0_()
        
        d_66_PublicKeyFromGenerateRSAKeyPairPemBytes_: _dafny.Seq
        d_67_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_67_valueOrError0_ = UTF8.default__.Encode(TestAwsCryptographyPrimitivesRSA.default__.StaticPublicKeyFromGenerateRSAKeyPair())
        if not(not((d_67_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(121,48): " + _dafny.string_of(d_67_valueOrError0_))
        d_66_PublicKeyFromGenerateRSAKeyPairPemBytes_ = (d_67_valueOrError0_).Extract()
        d_68_PrivateKeyFromGenerateRSAKeyPairPemBytes_: _dafny.Seq
        d_69_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_69_valueOrError1_ = UTF8.default__.Encode(TestAwsCryptographyPrimitivesRSA.default__.StaticPrivateKeyFromGenerateRSAKeyPair())
        if not(not((d_69_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(122,49): " + _dafny.string_of(d_69_valueOrError1_))
        d_68_PrivateKeyFromGenerateRSAKeyPairPemBytes_ = (d_69_valueOrError1_).Extract()
        d_70_KeyFromGenerateRSAKeyPair_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        d_70_KeyFromGenerateRSAKeyPair_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey_RSAPublicKey(2048, d_66_PublicKeyFromGenerateRSAKeyPairPemBytes_), software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey_RSAPrivateKey(2048, d_68_PrivateKeyFromGenerateRSAKeyPairPemBytes_))
        while (d_64_allPadding_) != (_dafny.Set({})):
            d_71_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
            with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                assign_such_that_0_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
                for assign_such_that_0_ in (d_64_allPadding_).Elements:
                    d_71_padding_ = assign_such_that_0_
                    if (d_71_padding_) in (d_64_allPadding_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                raise Exception("assign-such-that search produced no value (line 136)")
                pass
            TestAwsCryptographyPrimitivesRSA.default__.BasicRSAEncryptTest(software_amazon_cryptography_primitives_internaldafny_types.RSAEncryptInput_RSAEncryptInput(d_71_padding_, ((d_70_KeyFromGenerateRSAKeyPair_).publicKey).pem, _dafny.Seq([97, 115, 100, 102])), d_70_KeyFromGenerateRSAKeyPair_)
            d_64_allPadding_ = (d_64_allPadding_) - (_dafny.Set({d_71_padding_}))

    @staticmethod
    def TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM():
        d_72_allPadding_: _dafny.Set
        def iife1_():
            coll1_ = _dafny.Set()
            compr_1_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
            for compr_1_ in software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode.AllSingletonConstructors:
                d_73_p_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode = compr_1_
                if True:
                    coll1_ = coll1_.union(_dafny.Set([d_73_p_]))
            return _dafny.Set(coll1_)
        d_72_allPadding_ = iife1_()
        
        d_74_PublicKeyFromTestVectorsPemBytes_: _dafny.Seq
        d_75_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_75_valueOrError0_ = UTF8.default__.Encode(TestAwsCryptographyPrimitivesRSA.default__.StaticPublicKeyFromTestVectors())
        if not(not((d_75_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(154,41): " + _dafny.string_of(d_75_valueOrError0_))
        d_74_PublicKeyFromTestVectorsPemBytes_ = (d_75_valueOrError0_).Extract()
        d_76_PrivateKeyFromTestVectorsPemBytes_: _dafny.Seq
        d_77_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_77_valueOrError1_ = UTF8.default__.Encode(TestAwsCryptographyPrimitivesRSA.default__.StaticPrivateKeyFromTestVectors())
        if not(not((d_77_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestRSA.dfy(155,42): " + _dafny.string_of(d_77_valueOrError1_))
        d_76_PrivateKeyFromTestVectorsPemBytes_ = (d_77_valueOrError1_).Extract()
        d_78_KeyFromTestVectorsPair_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        d_78_KeyFromTestVectorsPair_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey_RSAPublicKey(4096, d_74_PublicKeyFromTestVectorsPemBytes_), software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey_RSAPrivateKey(4096, d_76_PrivateKeyFromTestVectorsPemBytes_))
        while (d_72_allPadding_) != (_dafny.Set({})):
            d_79_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
            with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                assign_such_that_1_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
                for assign_such_that_1_ in (d_72_allPadding_).Elements:
                    d_79_padding_ = assign_such_that_1_
                    if (d_79_padding_) in (d_72_allPadding_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                raise Exception("assign-such-that search produced no value (line 169)")
                pass
            TestAwsCryptographyPrimitivesRSA.default__.BasicRSAEncryptTest(software_amazon_cryptography_primitives_internaldafny_types.RSAEncryptInput_RSAEncryptInput(d_79_padding_, ((d_78_KeyFromTestVectorsPair_).publicKey).pem, _dafny.Seq([97, 115, 100, 102])), d_78_KeyFromTestVectorsPair_)
            d_72_allPadding_ = (d_72_allPadding_) - (_dafny.Set({d_79_padding_}))

    @staticmethod
    def StaticPublicKeyFromGenerateRSAKeyPair():
        return ((((((((_dafny.Seq("-----BEGIN PUBLIC KEY-----\n")) + (_dafny.Seq("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0RbkftAm30eFm+o6JraW\n"))) + (_dafny.Seq("AbWR+2grPfQk3i3w4eCsZHDQib6iUwX0MVADd2DjTnlkYa1DytDHRKfWHjtTniQ/\n"))) + (_dafny.Seq("EdKbENIFC5mLgh1Max7n9nQ6bmo4EvH2s4pUr3YBSys/dXpRDUCD/Mt4G+qDE8DT\n"))) + (_dafny.Seq("NSe8dqX5U44HwImQmKzvLYvD5gUY7eM5co4ZpfYrlRRVNkpv5qVNK7bz9KvQmKfP\n"))) + (_dafny.Seq("bQfzyvOZgSqQyHKfxbCM6ByE8Dd0NoI1ALwBY8wCXn/+6q4xLWTywu4nGIXs5Vt7\n"))) + (_dafny.Seq("vrMqwHSvYaNQKjUyPjsG3xPMwKruh30mGzc2KlKLZ+MiV+SNAiooqVkL6CxH4yJc\n"))) + (_dafny.Seq("NwIDAQAB\n"))) + (_dafny.Seq("-----END PUBLIC KEY-----\n"))

    @staticmethod
    def StaticPrivateKeyFromGenerateRSAKeyPair():
        return (((((((((((((((((((((((((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDRFuR+0CbfR4Wb\n"))) + (_dafny.Seq("6jomtpYBtZH7aCs99CTeLfDh4KxkcNCJvqJTBfQxUAN3YONOeWRhrUPK0MdEp9Ye\n"))) + (_dafny.Seq("O1OeJD8R0psQ0gULmYuCHUxrHuf2dDpuajgS8fazilSvdgFLKz91elENQIP8y3gb\n"))) + (_dafny.Seq("6oMTwNM1J7x2pflTjgfAiZCYrO8ti8PmBRjt4zlyjhml9iuVFFU2Sm/mpU0rtvP0\n"))) + (_dafny.Seq("q9CYp89tB/PK85mBKpDIcp/FsIzoHITwN3Q2gjUAvAFjzAJef/7qrjEtZPLC7icY\n"))) + (_dafny.Seq("hezlW3u+syrAdK9ho1AqNTI+OwbfE8zAqu6HfSYbNzYqUotn4yJX5I0CKiipWQvo\n"))) + (_dafny.Seq("LEfjIlw3AgMBAAECggEAWe7DTCpCtgHg3X2jEnixT73lsuGMy+KBoxDWjYkiDTea\n"))) + (_dafny.Seq("8sxMrHIgpL86JnRFgMDk5MBuKsOfGhAooCs7XYdQm11fNh5nbiRWZZotftu1wQMg\n"))) + (_dafny.Seq("CNLmGHv7dSD4KNoUV10cN+7rAsyvmKF5oWQ+idYD4labkNr1wTMTcYSZ7ZlgbNFr\n"))) + (_dafny.Seq("ZFwsZizD4RrpwwyrpZ25f/H95p9fQrZXrB3Wt5aNn0uhTcQL0KfnvMamZNPfxj9b\n"))) + (_dafny.Seq("j6CWpyXtFOMc8nuT4fKOh7q4A87UsduBBhdAk4m4m98WvlIZIUW89w3kzIfr9zCT\n"))) + (_dafny.Seq("VxflBzeEDSM8+Sy1TJNRBBwhRnQ/gNLLD+e6/O/MTQKBgQD/vRxZvyJkWaRYkGeS\n"))) + (_dafny.Seq("VVAZQJOSQUPpVC5U3y2ghV8Dm30BfMEtySdD9hXd635X7e0dvIqwxJAwFgJ+SYT2\n"))) + (_dafny.Seq("NNE8wiIKolQH1h01cYK+kwAohB6vQPLymYwzc9HNcevCDFkt7VVRgnwUHk6BXz4T\n"))) + (_dafny.Seq("LsF/jYTUdzCyFfjYWGTOEh7PkwKBgQDRTZSe2Tqua2Groi75tmXMAzI6jQsiBqTn\n"))) + (_dafny.Seq("Jv0es+IMWZyh2yMy9x6numM7IBBamgt+6hNEKaUmQxoEFbo0dUsEx35RH2Pdkr8X\n"))) + (_dafny.Seq("IuXuh3IdRgRCV9WxnecBD32Cci9qLN1aaVJHfdA2dW4LAb7m4/GeuiS/8ZatXEm2\n"))) + (_dafny.Seq("Kf0YZAx/TQKBgEpbQtX5U9eXlMhHXEXY1kwxUXbx0PwThNEaftqwTJrw55y6GDTm\n"))) + (_dafny.Seq("yqrg7ySyJu8L96hwvGZ/EGlazOjJGYa4fqnKzDkJT6NjpuR2F4yvkxk0qPNN0BWn\n"))) + (_dafny.Seq("fXMsVrEEUYb/LiLDYc4sQUVcNnk5JwRO0OX0UM2xxg/RgaPtt4mPDTRPAoGBAJsY\n"))) + (_dafny.Seq("1izv5CAjyniY8h5xHvYS2EGzCrDoI4J2zdLWkYd9UChQbsDxhnHcGHRTykqZJDOj\n"))) + (_dafny.Seq("2SsFgS/dQYYNY7JDyJd+DQioLiSe/aNzZNdg3xr6K2XOGLhJvkh25han7qLLJCw/\n"))) + (_dafny.Seq("J416mbQBSM43OPN3rjBk1560s2c7oBOxAa/1U51xAoGBAOYFMvdk6H359yaJGmsN\n"))) + (_dafny.Seq("kY7lS6heh4cHfSM7Hw02lh/ovasdQm+afcnDWEW0XQYM6KQCcJiwbIK/kPkVsvJe\n"))) + (_dafny.Seq("o6gynyWoHrrQuRdmffPvzT50paccJuupeHAtfOAue5y57FQUc4Xm4Qj3P7cQJr9z\n"))) + (_dafny.Seq("UMCUAooEJcdmAUyVUy5BQc7P\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----\n"))

    @staticmethod
    def StaticPublicKeyFromTestVectors():
        return (((((((((((((_dafny.Seq("-----BEGIN PUBLIC KEY-----\n")) + (_dafny.Seq("MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs7RoNYEPAIws89VV+kra\n"))) + (_dafny.Seq("rVv/4wbdmUAaAKWgWuxZi5na9GJSmnhCkqyLRm7wPbQY4LCoa5/IMUxkHLsYDPdu\n"))) + (_dafny.Seq("udY0Qm0GcoxOlvJKHYo4RjF7HyiS34D6dvyO4Gd3aq0mZHoxSGCxW/7hf03wEMzc\n"))) + (_dafny.Seq("iVJXWHXhaI0lD6nrzIEgLrE4L+3V2LeAQjvZsTKd+bYMqeZOL2syiVVIAU8POwAG\n"))) + (_dafny.Seq("GVBroJoveFm/SUp6lCiN0M2kTeyQA2ax3QTtZSAa8nwrI7U52XOzVmdMicJsy2Pg\n"))) + (_dafny.Seq("uW98te3MuODdK24yNkHIkYameP/Umf/SJshUJQd5a/TUp3XE+HhOWAumx22tIDlC\n"))) + (_dafny.Seq("vZS11cuk2fp0WeHUnXaC19N5qWKfvHEKSugzty/z3lGP7ItFhrF2X1qJHeAAsL11\n"))) + (_dafny.Seq("kjo6Lc48KsE1vKvbnW4VLyB3wdNiVvmUNO29tPXwaR0Q5Gbr3jk3nUzdkEHouHWQ\n"))) + (_dafny.Seq("41lubOHCCBN3V13mh/MgtNhESHjfmmOnh54ErD9saA1d7CjTf8g2wqmjEqvGSW6N\n"))) + (_dafny.Seq("q7zhcWR2tp1olflS7oHzul4/I3hnkfL6Kb2xAWWaQKvg3mtsY2OPlzFEP0tR5UcH\n"))) + (_dafny.Seq("Pfp5CeS1Xzg7hN6vRICW6m4l3u2HJFld2akDMm1vnSz8RCbPW7jp7YBxUkWJmypM\n"))) + (_dafny.Seq("tG7Yv2aGZXGbUtM8o1cZarECAwEAAQ==\n"))) + (_dafny.Seq("-----END PUBLIC KEY-----"))

    @staticmethod
    def StaticPrivateKeyFromTestVectors():
        return (((((((((((((((((((((((((((((((((((((((((((((((((((_dafny.Seq("-----BEGIN PRIVATE KEY-----\n")) + (_dafny.Seq("MIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCztGg1gQ8AjCzz\n"))) + (_dafny.Seq("1VX6StqtW//jBt2ZQBoApaBa7FmLmdr0YlKaeEKSrItGbvA9tBjgsKhrn8gxTGQc\n"))) + (_dafny.Seq("uxgM92651jRCbQZyjE6W8kodijhGMXsfKJLfgPp2/I7gZ3dqrSZkejFIYLFb/uF/\n"))) + (_dafny.Seq("TfAQzNyJUldYdeFojSUPqevMgSAusTgv7dXYt4BCO9mxMp35tgyp5k4vazKJVUgB\n"))) + (_dafny.Seq("Tw87AAYZUGugmi94Wb9JSnqUKI3QzaRN7JADZrHdBO1lIBryfCsjtTnZc7NWZ0yJ\n"))) + (_dafny.Seq("wmzLY+C5b3y17cy44N0rbjI2QciRhqZ4/9SZ/9ImyFQlB3lr9NSndcT4eE5YC6bH\n"))) + (_dafny.Seq("ba0gOUK9lLXVy6TZ+nRZ4dSddoLX03mpYp+8cQpK6DO3L/PeUY/si0WGsXZfWokd\n"))) + (_dafny.Seq("4ACwvXWSOjotzjwqwTW8q9udbhUvIHfB02JW+ZQ07b209fBpHRDkZuveOTedTN2Q\n"))) + (_dafny.Seq("Qei4dZDjWW5s4cIIE3dXXeaH8yC02ERIeN+aY6eHngSsP2xoDV3sKNN/yDbCqaMS\n"))) + (_dafny.Seq("q8ZJbo2rvOFxZHa2nWiV+VLugfO6Xj8jeGeR8vopvbEBZZpAq+Dea2xjY4+XMUQ/\n"))) + (_dafny.Seq("S1HlRwc9+nkJ5LVfODuE3q9EgJbqbiXe7YckWV3ZqQMybW+dLPxEJs9buOntgHFS\n"))) + (_dafny.Seq("RYmbKky0bti/ZoZlcZtS0zyjVxlqsQIDAQABAoICAEr3m/GWIXgNAkPGX9PGnmtr\n"))) + (_dafny.Seq("0dgX6SIhh7d1YOwNZV3DlYAV9HfUa5Fcwc1kQny7QRWbHOepBI7sW2dQ9buTDXIh\n"))) + (_dafny.Seq("VjPP37yxo6d89EZWfxtpUP+yoXL0D4jL257qCvtJuJZ6E00qaVMDhXbiQKABlo8C\n"))) + (_dafny.Seq("9sVEiABhwXBDZsctpwtTiykTgv6hrrPy2+H8R8MAm0/VcBCAG9kG5r8FCEmIvQKa\n"))) + (_dafny.Seq("dgvNxrfiWNZuZ6yfLmpJH54SbhG9Kb4WbCKfvh4ihqyi0btRdSM6fMeLgG9o/zrc\n"))) + (_dafny.Seq("s54B0kHeLOYNVo0j7FQpZBFeSIbmHfln4RKBh7ntrTke/Ejbh3NbiPvxWSP0P067\n"))) + (_dafny.Seq("SYWPkQpip2q0ION81wSQZ1haP2GewFFu4IEjG3DlqqpKKGLqXrmjMufnildVFpBx\n"))) + (_dafny.Seq("ir+MgvgQfEBoGEx0aElyO7QuRYaEiXeb/BhMZeC5O65YhJrWSuTVizh3xgJWjgfV\n"))) + (_dafny.Seq("aYwYgxN8SBXBhXLIVvnPhadTqsW1C/aevLOk110eSFWcHf+FCK781ykIzcpXoRGX\n"))) + (_dafny.Seq("OwWcZzC/fmSABS0yH56ow+I0tjdLIEEMhoa4/kkamioHOJ4yyB+W1DO6/DnMyQlx\n"))) + (_dafny.Seq("g7y2WsAaIEBoWUARy776k70xPPMtYAxzFXI9KhqRVrPfeaRZ+ojeyLyr3GQGyyoo\n"))) + (_dafny.Seq("cuGRdMUblsmODv4ixmOxAoIBAQDvkznvVYNdP3Eg5vQeLm/qsP6dLejLijBLeq9i\n"))) + (_dafny.Seq("7DZH2gRpKcflXZxCkRjsKDDE+fgDcBYEp2zYfRIVvgrxlTQZdaSG+GoDcbjbNQn3\n"))) + (_dafny.Seq("djCCtOOACioN/vg2zFlX4Bs6Q+NaV7g5qP5SUaxUBjuHLe7Nc+ZkyheMHuNYVLvk\n"))) + (_dafny.Seq("HL/IoWyANpZYjMUU3xMbL/J29Gz7CPGr8Si28TihAHGfcNgn8S04OQZhTX+bU805\n"))) + (_dafny.Seq("/+7B4XW47Mthg/u7hlqFl+YIAaSJYvWkEaVP1A9I7Ve0aMDSMWwzTg9cle2uVaL3\n"))) + (_dafny.Seq("+PTzWY5coBlHKjqAg9ufhYSDhAqBd/JOSlv8RwcA3PDXJ6C/AoIBAQDABmXXYQky\n"))) + (_dafny.Seq("7phExXBvkLtJt2TBGjjwulf4R8TC6W5F51jJuoqY/mTqYcLcOn2nYGVwoFvPsy/Q\n"))) + (_dafny.Seq("CTjfODwJBXzbloXtYFR3PWAeL1Y6+7Cm+koMWIPJyVbD5Fzm+gZStM0GwP8FhDt2\n"))) + (_dafny.Seq("Wt8fWEyXmoLdAy6RAwiEmCagEh8o+13oBfwnBllbz7TxaErsUuR+XVgl/iHwztdv\n"))) + (_dafny.Seq("cdJKyRgaFfWSh9aiO7EMV2rBGWsoX09SRvprPFAGx8Ffm7YcqIk34QXsQyc45Dyn\n"))) + (_dafny.Seq("CwkvypxHoaB3ot/48FeFm9IubApb/ctv+EgkBfL4S4bdwRXS1rt+0+QihBoFyP2o\n"))) + (_dafny.Seq("J91cdm4hEWCPAoIBAQC6l11hFaYZo0bWDGsHcr2B+dZkzxPoKznQH76n+jeQoLIc\n"))) + (_dafny.Seq("wgjJkK4afm39yJOrZtEOxGaxu0CgIFFMk9ZsL/wC9EhvQt02z4TdXiLkFK5VrtMd\n"))) + (_dafny.Seq("r0zv16y06VWQhqBOMf/KJlX6uq9RqADi9HO6pkC+zc0cpPXQEWKaMmygju+kMG2U\n"))) + (_dafny.Seq("Mm/IieMZjWCRJTfgBCE5J88qTsqaKagkZXcZakdAXKwOhQN+F2EStiM6UCZB5PrO\n"))) + (_dafny.Seq("S8dfrO8ML+ki8Zqck8L1qhiNb5zkXtKExy4u+gNr8khGcT6vqqoSxOoH3mPRgOfL\n"))) + (_dafny.Seq("Jnppne8wlwIf7Vq3H8ka6zPSXEHma999gZcmy9t7AoIBAGbQhiLl79j3a0wXMvZp\n"))) + (_dafny.Seq("Vf5IVYgXFDnAbG2hb7a06bhAAIgyexcjzsC4C2+DWdgOgwHkuoPg+062QV8zauGh\n"))) + (_dafny.Seq("sJKaa6cHlvIpSJeg3NjD/nfJN3CYzCd0yCIm2Z9Ka6xI5iYhm+pGPNhIG4Na8deS\n"))) + (_dafny.Seq("gVL46yv1pc/o73VxfoGg5UzgN3xlp97Cva0sHEGguHr4W8Qr59xZw3wGQ4SLW35M\n"))) + (_dafny.Seq("F6qXVNKUh12GSMCPbZK2RXBWVKqqJmca+WzJoJ6DlsT2lQdFhXCus9L007xlDXxF\n"))) + (_dafny.Seq("C/hCmw1dEl+VaNo2Ou26W/zdwTKYhNlxBwsg4SB8nPNxXIsmlBBY54froFhriNfn\n"))) + (_dafny.Seq("x/0CggEAUzz+VMtjoEWw2HSHLOXrO4EmwJniNgiiwfX3DfZE4tMNZgqZwLkq67ns\n"))) + (_dafny.Seq("T0n3b0XfAOOkLgMZrUoOxPHkxFeyLLf7pAEJe7QNB+Qilw8e2zVqtiJrRk6uDIGJ\n"))) + (_dafny.Seq("Sv+yM52zkImZAe2jOdU3KeUZxSMmb5vIoiPBm+tb2WupAg3YdpKn1/jWTpVmV/+G\n"))) + (_dafny.Seq("UtTLVE6YpAyFp1gMxhutE9vfIS94ek+vt03AoEOlltt6hqZfv3xmY8vGuAjlnj12\n"))) + (_dafny.Seq("zHaq+fhCRPsbsZkzJ9nIVdXYnNIEGtMGNnxax7tYRej/UXqyazbxHiJ0iPF4PeDn\n"))) + (_dafny.Seq("dzxtGxpeTBi+KhKlca8SlCdCqYwG6Q==\n"))) + (_dafny.Seq("-----END PRIVATE KEY-----"))

    @_dafny.classproperty
    def RSA__PUBLIC__2048(instance):
        return ((((((((_dafny.Seq("-----BEGIN PUBLIC KEY-----\n")) + (_dafny.Seq("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqBvECLsPdF1J5DOkaA1n\n"))) + (_dafny.Seq("UrGwNT9ard3KSMaPypla/5Jhz0veCz1OSjnx35+FE3q7omHQBmKRs6XDkj4tJ5vh\n"))) + (_dafny.Seq("1baw2yzgIAqW9lOXK64GiYy0maH2NfRxGbj5LhVq5T4YOkKh9D3GFbfT9/NpcsOZ\n"))) + (_dafny.Seq("M2HDX8Z+M0HM3XymtcfpHk5o6QF1lbBW+rDJEcYhPN0obBufCXaasgsBRP5Ei2b5\n"))) + (_dafny.Seq("18xpy9M19By1yuC9mlNcpE5v5A8fq/qLLT4s34/6dnVxKX6gIoWDzDrUNrnPe0p5\n"))) + (_dafny.Seq("pqZ1SHalrELMf/liXPrf94+0cF8g1fYVGGo+MZsG5/HRngLiskP25w5smMT51U1y\n"))) + (_dafny.Seq("gQIDAQAB\n"))) + (_dafny.Seq("-----END PUBLIC KEY-----"))
    @_dafny.classproperty
    def RSA__PUBLIC__3072(instance):
        return ((((((((((_dafny.Seq("-----BEGIN PUBLIC KEY-----\n")) + (_dafny.Seq("MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAnrUonUAKKpZE+LbQfq6I\n"))) + (_dafny.Seq("gAR//GNnT7L6P3LCboXu44StJtvVyAmHZXPgdkxxT1EKLFx+Tys3B7jhgno9cs67\n"))) + (_dafny.Seq("Scf0pLjJAmXOVHa6881oxi5zeP0e6+KzOPugg3C+EknS2PSHTLsdTrkgZU+oUjde\n"))) + (_dafny.Seq("AgRSgmWrp8aMM1WpoLmNcWC/Pi0mSziVnIzE3WhkZ2Ccetz/viRL60VHlTwNQPVa\n"))) + (_dafny.Seq("7fqbcSqBxm/VjDzYvDwzmU+4GNEs5hrA2IFDxxsYZAU8HdASQM18A8W7n0Okaa4e\n"))) + (_dafny.Seq("c4svyKVFkncbNCqetynLU0A5ny7I5WVXV7DNi2VMjD/mZsEt8IrwfuWSMKuIPxs/\n"))) + (_dafny.Seq("Nb/4Psr7ZvbKSlaMwEpyReHvYYqM7dd6A4Y9FirnrpAPaqlfm8UFtHKQvUckxRoR\n"))) + (_dafny.Seq("05kzNN2jIRJtMwGpn+40tiei7eBGMmIn41/dnkM7GOJau4BarSJMiREK1yH9hh1C\n"))) + (_dafny.Seq("GbrQu6i0F9G0uBDITen9/uPX9cxK5pNHAxeWzr2UP1UzAgMBAAE=\n"))) + (_dafny.Seq("-----END PUBLIC KEY-----"))
    @_dafny.classproperty
    def RSA__PUBLIC__4096(instance):
        return (((((((((((((_dafny.Seq("-----BEGIN PUBLIC KEY-----\n")) + (_dafny.Seq("MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs86OIUN9RbdEdyQb2tGQ\n"))) + (_dafny.Seq("miDmmeJaYKanLB0lfWiuO85kJK8edZyLkHIzps81qwgVSzbMCBB7QGcMyPbb3wbE\n"))) + (_dafny.Seq("B4EJ32v3cuMVUs6sOvOYV4g1c1Hi1WVqnCeH+3RSFBfb7RL7SvSUmilX2tNV6uZy\n"))) + (_dafny.Seq("BmMSGBJ/IMzxoHjKSFn6r1ttwov8X5DmNTyIp4qG3qyL1qhpla1bUE5Nb6uMHI2v\n"))) + (_dafny.Seq("qMM+8zSPcRN40CfaQATxevNs/69++XJ+5L1nKU9fMwust1GEbtJ6cIBwAuqlyMm9\n"))) + (_dafny.Seq("CnZ+tn56FEVPrUrsQX35QRNjbi0jjKI8ItkdyJ5fLixCjJ20tCo5jeL5KJ32Rjuw\n"))) + (_dafny.Seq("BlB2KQrgdw5VEMrMlTJz9oozUv8GFzjtS4kx+tAsWhji5s0jry4QFYG01Q4ezVPb\n"))) + (_dafny.Seq("TYdxg1Yz265EyLmF0+/ZQtO1kQc7tXHD5Gzzwyqot/UdJwlXStUGB2yEe62HQ2LT\n"))) + (_dafny.Seq("9Ly3V7rUDJzO44zuFVjqchRPYWNdiYl8BVP/ak2bMtcowk06T9bo1tRf4HJWfpIM\n"))) + (_dafny.Seq("GF27MXqykKHxcmOb0UfGIfI0eUtkid4gJdCxhidiILj6SHpEr+oa/Oogz01rVCdm\n"))) + (_dafny.Seq("mbWmgFxmiKse8NXNQR+7qhMYX5GgdeSbp/Lg24HF9mvnd0S2wHkC86lGyQtvzrsd\n"))) + (_dafny.Seq("DdUJZ2jqiKvMLdMKNFHFGGUCAwEAAQ==\n"))) + (_dafny.Seq("-----END PUBLIC KEY-----"))
