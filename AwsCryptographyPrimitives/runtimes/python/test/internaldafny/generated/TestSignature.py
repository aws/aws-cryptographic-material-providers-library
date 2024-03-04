import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws

# Module: TestSignature

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RequireGoodKeyLengths(alg, sigKeyPair):
        if not((len((sigKeyPair).verificationKey)) == (Signature.default__.FieldSize(alg))):
            raise _dafny.HaltException("test/TestSignature.dfy(24,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def YCompression(alg, fieldSize):
        d_0_res_: Signature.SignatureKeyPair
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(Signature.SignatureKeyPair.default())()
        out0_: Wrappers.Result
        out0_ = Signature.ECDSA.ExternKeyGen(alg)
        d_1_valueOrError0_ = out0_
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(28,12): " + _dafny.string_of(d_1_valueOrError0_))
        d_0_res_ = (d_1_valueOrError0_).Extract()
        default__.RequireGoodKeyLengths(alg, d_0_res_)
        d_2_public_: _dafny.Seq
        d_3_secret_: _dafny.Seq
        rhs0_ = (d_0_res_).verificationKey
        rhs1_ = (d_0_res_).signingKey
        d_2_public_ = rhs0_
        d_3_secret_ = rhs1_
        if not((0) < (len(d_3_secret_))):
            raise _dafny.HaltException("test/TestSignature.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(d_2_public_)) == ((1) + (_dafny.euclidian_division((fieldSize) + (7), 8)))):
            raise _dafny.HaltException("test/TestSignature.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_2_public_)[0]) == (2)) or (((d_2_public_)[0]) == (3))):
            raise _dafny.HaltException("test/TestSignature.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VerifyMessage(alg):
        d_4_message_: _dafny.Seq
        d_5_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_5_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("Hello, World!"))
        if not(not((d_5_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(39,16): " + _dafny.string_of(d_5_valueOrError0_))
        d_4_message_ = (d_5_valueOrError0_).Extract()
        d_6_genInput_: software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput
        d_6_genInput_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput(alg)
        d_7_keys_: Signature.SignatureKeyPair
        d_8_valueOrError1_: Wrappers.Result = Wrappers.Result.default(Signature.SignatureKeyPair.default())()
        out1_: Wrappers.Result
        out1_ = Signature.ECDSA.ExternKeyGen(alg)
        d_8_valueOrError1_ = out1_
        if not(not((d_8_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(41,13): " + _dafny.string_of(d_8_valueOrError1_))
        d_7_keys_ = (d_8_valueOrError1_).Extract()
        default__.RequireGoodKeyLengths(alg, d_7_keys_)
        d_9_signature_: _dafny.Seq
        d_10_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = Signature.ECDSA.Sign(alg, (d_7_keys_).signingKey, d_4_message_)
        d_10_valueOrError2_ = out2_
        if not(not((d_10_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(44,18): " + _dafny.string_of(d_10_valueOrError2_))
        d_9_signature_ = (d_10_valueOrError2_).Extract()
        d_11_shouldBeTrue_: bool
        d_12_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_12_valueOrError3_ = Signature.ECDSA_Verify(alg, (d_7_keys_).verificationKey, d_4_message_, d_9_signature_)
        if not(not((d_12_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(45,21): " + _dafny.string_of(d_12_valueOrError3_))
        d_11_shouldBeTrue_ = (d_12_valueOrError3_).Extract()
        if not(d_11_shouldBeTrue_):
            raise _dafny.HaltException("test/TestSignature.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_13_shouldBeFalse_: bool
        d_14_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_14_valueOrError4_ = Signature.ECDSA_Verify(alg, (d_7_keys_).verificationKey, (d_4_message_) + (_dafny.Seq([1])), d_9_signature_)
        if not(not((d_14_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(48,22): " + _dafny.string_of(d_14_valueOrError4_))
        d_13_shouldBeFalse_ = (d_14_valueOrError4_).Extract()
        if not(not(d_13_shouldBeFalse_)):
            raise _dafny.HaltException("test/TestSignature.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def YCompression384():
        default__.YCompression(default__.P384, 384)

    @staticmethod
    def YCompression256():
        default__.YCompression(default__.P256, 256)

    @staticmethod
    def VerifyMessage384():
        default__.VerifyMessage(default__.P384)

    @staticmethod
    def VerifyMessage256():
        default__.VerifyMessage(default__.P256)

    @_dafny.classproperty
    def P384(instance):
        return software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()
    @_dafny.classproperty
    def P256(instance):
        return software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256()
