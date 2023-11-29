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
import TestAwsCryptographyPrimitivesRSA
import TestKDF
import TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesHKDF
import TestHKDF__Rfc5869TestVectors
import ConstantTime
import ConstantTimeTest
import TestAwsCryptographyPrimitivesGenerateRandomBytes

# assert "TestSignature" == __name__
TestSignature = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RequireGoodKeyLengths(alg, sigKeyPair):
        if not((len((sigKeyPair).verificationKey)) == (Signature.default__.FieldSize(alg))):
            raise _dafny.HaltException("test/TestSignature.dfy(24,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def YCompression(alg, fieldSize):
        d_136_res_: Signature.SignatureKeyPair
        d_137_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(Signature.SignatureKeyPair.default())()
        out26_: Wrappers.Result
        out26_ = Signature.ECDSA.ExternKeyGen(alg)
        d_137_valueOrError0_ = out26_
        if not(not((d_137_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(28,12): " + _dafny.string_of(d_137_valueOrError0_))
        d_136_res_ = (d_137_valueOrError0_).Extract()
        TestSignature.default__.RequireGoodKeyLengths(alg, d_136_res_)
        d_138_public_: _dafny.Seq
        d_139_secret_: _dafny.Seq
        rhs0_: _dafny.Seq = (d_136_res_).verificationKey
        rhs1_: _dafny.Seq = (d_136_res_).signingKey
        d_138_public_ = rhs0_
        d_139_secret_ = rhs1_
        if not((0) < (len(d_139_secret_))):
            raise _dafny.HaltException("test/TestSignature.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(d_138_public_)) == ((1) + (_dafny.euclidian_division((fieldSize) + (7), 8)))):
            raise _dafny.HaltException("test/TestSignature.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_138_public_)[0]) == (2)) or (((d_138_public_)[0]) == (3))):
            raise _dafny.HaltException("test/TestSignature.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VerifyMessage(alg):
        d_140_message_: _dafny.Seq
        d_141_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_141_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("Hello, World!"))
        if not(not((d_141_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(39,16): " + _dafny.string_of(d_141_valueOrError0_))
        d_140_message_ = (d_141_valueOrError0_).Extract()
        d_142_genInput_: software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput
        d_142_genInput_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput(alg)
        d_143_keys_: Signature.SignatureKeyPair
        d_144_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(Signature.SignatureKeyPair.default())()
        out27_: Wrappers.Result
        out27_ = Signature.ECDSA.ExternKeyGen(alg)
        d_144_valueOrError1_ = out27_
        if not(not((d_144_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(41,13): " + _dafny.string_of(d_144_valueOrError1_))
        d_143_keys_ = (d_144_valueOrError1_).Extract()
        TestSignature.default__.RequireGoodKeyLengths(alg, d_143_keys_)
        d_145_signature_: _dafny.Seq
        d_146_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out28_: Wrappers.Result
        out28_ = Signature.ECDSA.Sign(alg, (d_143_keys_).signingKey, d_140_message_)
        d_146_valueOrError2_ = out28_
        if not(not((d_146_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(44,18): " + _dafny.string_of(d_146_valueOrError2_))
        d_145_signature_ = (d_146_valueOrError2_).Extract()
        d_147_shouldBeTrue_: bool
        d_148_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        d_148_valueOrError3_ = Signature.ECDSA.Verify(alg, (d_143_keys_).verificationKey, d_140_message_, d_145_signature_)
        if not(not((d_148_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(45,21): " + _dafny.string_of(d_148_valueOrError3_))
        d_147_shouldBeTrue_ = (d_148_valueOrError3_).Extract()
        if not(d_147_shouldBeTrue_):
            raise _dafny.HaltException("test/TestSignature.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_149_shouldBeFalse_: bool
        d_150_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        d_150_valueOrError4_ = Signature.ECDSA.Verify(alg, (d_143_keys_).verificationKey, (d_140_message_) + (_dafny.Seq([1])), d_145_signature_)
        if not(not((d_150_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(48,22): " + _dafny.string_of(d_150_valueOrError4_))
        d_149_shouldBeFalse_ = (d_150_valueOrError4_).Extract()
        if not(not(d_149_shouldBeFalse_)):
            raise _dafny.HaltException("test/TestSignature.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def YCompression384():
        TestSignature.default__.YCompression((TestSignature.default__).P384, 384)

    @staticmethod
    def YCompression256():
        TestSignature.default__.YCompression((TestSignature.default__).P256, 256)

    @staticmethod
    def VerifyMessage384():
        TestSignature.default__.VerifyMessage((TestSignature.default__).P384)

    @staticmethod
    def VerifyMessage256():
        TestSignature.default__.VerifyMessage((TestSignature.default__).P256)

    @_dafny.classproperty
    def P384(instance):
        return software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()
    @_dafny.classproperty
    def P256(instance):
        return software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256()
