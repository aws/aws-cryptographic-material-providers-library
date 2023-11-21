import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
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

assert "TestSignature" == __name__
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
        d_105_res_: Signature.SignatureKeyPair
        d_106_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(Signature.SignatureKeyPair.default())()
        out51_: Wrappers.Result
        out51_ = Signature.ECDSA.ExternKeyGen(alg)
        d_106_valueOrError0_ = out51_
        if not(not((d_106_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(28,12): " + _dafny.string_of(d_106_valueOrError0_))
        d_105_res_ = (d_106_valueOrError0_).Extract()
        TestSignature.default__.RequireGoodKeyLengths(alg, d_105_res_)
        d_107_public_: _dafny.Seq
        d_108_secret_: _dafny.Seq
        rhs0_: _dafny.Seq = (d_105_res_).verificationKey
        rhs1_: _dafny.Seq = (d_105_res_).signingKey
        d_107_public_ = rhs0_
        d_108_secret_ = rhs1_
        if not((0) < (len(d_108_secret_))):
            raise _dafny.HaltException("test/TestSignature.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(d_107_public_)) == ((1) + (_dafny.euclidian_division((fieldSize) + (7), 8)))):
            raise _dafny.HaltException("test/TestSignature.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_107_public_)[0]) == (2)) or (((d_107_public_)[0]) == (3))):
            raise _dafny.HaltException("test/TestSignature.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VerifyMessage(alg):
        d_109_message_: _dafny.Seq
        d_110_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_110_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("Hello, World!"))
        if not(not((d_110_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(39,16): " + _dafny.string_of(d_110_valueOrError0_))
        d_109_message_ = (d_110_valueOrError0_).Extract()
        d_111_genInput_: software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput
        d_111_genInput_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput(alg)
        d_112_keys_: Signature.SignatureKeyPair
        d_113_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(Signature.SignatureKeyPair.default())()
        out52_: Wrappers.Result
        out52_ = Signature.ECDSA.ExternKeyGen(alg)
        d_113_valueOrError1_ = out52_
        if not(not((d_113_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(41,13): " + _dafny.string_of(d_113_valueOrError1_))
        d_112_keys_ = (d_113_valueOrError1_).Extract()
        TestSignature.default__.RequireGoodKeyLengths(alg, d_112_keys_)
        d_114_signature_: _dafny.Seq
        d_115_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out53_: Wrappers.Result
        out53_ = Signature.ECDSA.Sign(alg, (d_112_keys_).signingKey, d_109_message_)
        d_115_valueOrError2_ = out53_
        if not(not((d_115_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(44,18): " + _dafny.string_of(d_115_valueOrError2_))
        d_114_signature_ = (d_115_valueOrError2_).Extract()
        d_116_shouldBeTrue_: bool
        d_117_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        d_117_valueOrError3_ = Signature.ECDSA.Verify(alg, (d_112_keys_).verificationKey, d_109_message_, d_114_signature_)
        if not(not((d_117_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(45,21): " + _dafny.string_of(d_117_valueOrError3_))
        d_116_shouldBeTrue_ = (d_117_valueOrError3_).Extract()
        if not(d_116_shouldBeTrue_):
            raise _dafny.HaltException("test/TestSignature.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_118_shouldBeFalse_: bool
        d_119_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        d_119_valueOrError4_ = Signature.ECDSA.Verify(alg, (d_112_keys_).verificationKey, (d_109_message_) + (_dafny.Seq([1])), d_114_signature_)
        if not(not((d_119_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(48,22): " + _dafny.string_of(d_119_valueOrError4_))
        d_118_shouldBeFalse_ = (d_119_valueOrError4_).Extract()
        if not(not(d_118_shouldBeFalse_)):
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
