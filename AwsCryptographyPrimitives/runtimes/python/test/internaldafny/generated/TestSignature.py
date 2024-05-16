import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries

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
            raise _dafny.HaltException("test/TestSignature.dfy(28,15): " + _dafny.string_of(d_1_valueOrError0_))
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
            raise _dafny.HaltException("test/TestSignature.dfy(39,19): " + _dafny.string_of(d_5_valueOrError0_))
        d_4_message_ = (d_5_valueOrError0_).Extract()
        d_6_genInput_: AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput
        d_6_genInput_ = AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput(alg)
        d_7_keys_: Signature.SignatureKeyPair
        d_8_valueOrError1_: Wrappers.Result = Wrappers.Result.default(Signature.SignatureKeyPair.default())()
        out1_: Wrappers.Result
        out1_ = Signature.ECDSA.ExternKeyGen(alg)
        d_8_valueOrError1_ = out1_
        if not(not((d_8_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(41,16): " + _dafny.string_of(d_8_valueOrError1_))
        d_7_keys_ = (d_8_valueOrError1_).Extract()
        default__.RequireGoodKeyLengths(alg, d_7_keys_)
        d_9_signature_: _dafny.Seq
        d_10_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = Signature.ECDSA.Sign(alg, (d_7_keys_).signingKey, d_4_message_)
        d_10_valueOrError2_ = out2_
        if not(not((d_10_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(44,21): " + _dafny.string_of(d_10_valueOrError2_))
        d_9_signature_ = (d_10_valueOrError2_).Extract()
        d_11_shouldBeTrue_: bool
        d_12_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_12_valueOrError3_ = Signature.ECDSA_Verify(alg, (d_7_keys_).verificationKey, d_4_message_, d_9_signature_)
        if not(not((d_12_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(45,24): " + _dafny.string_of(d_12_valueOrError3_))
        d_11_shouldBeTrue_ = (d_12_valueOrError3_).Extract()
        if not(d_11_shouldBeTrue_):
            raise _dafny.HaltException("test/TestSignature.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_13_shouldBeFalse_: bool
        d_14_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_14_valueOrError4_ = Signature.ECDSA_Verify(alg, (d_7_keys_).verificationKey, (d_4_message_) + (_dafny.Seq([1])), d_9_signature_)
        if not(not((d_14_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(48,25): " + _dafny.string_of(d_14_valueOrError4_))
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
        return AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()
    @_dafny.classproperty
    def P256(instance):
        return AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P256()
