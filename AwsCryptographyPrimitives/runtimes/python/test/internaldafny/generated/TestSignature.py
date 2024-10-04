import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries

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
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(Signature.SignatureKeyPair.default())()
        out0_: Wrappers.Result
        out0_ = Signature.ECDSA.ExternKeyGen(alg)
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(28,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_res_: Signature.SignatureKeyPair
        d_1_res_ = (d_0_valueOrError0_).Extract()
        default__.RequireGoodKeyLengths(alg, d_1_res_)
        d_2_public_: _dafny.Seq
        d_3_secret_: _dafny.Seq
        rhs0_ = (d_1_res_).verificationKey
        rhs1_ = (d_1_res_).signingKey
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
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_0_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("Hello, World!"))
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(39,19): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_message_: _dafny.Seq
        d_1_message_ = (d_0_valueOrError0_).Extract()
        d_2_genInput_: AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput
        d_2_genInput_ = AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput(alg)
        d_3_valueOrError1_: Wrappers.Result = Wrappers.Result.default(Signature.SignatureKeyPair.default())()
        out0_: Wrappers.Result
        out0_ = Signature.ECDSA.ExternKeyGen(alg)
        d_3_valueOrError1_ = out0_
        if not(not((d_3_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(41,16): " + _dafny.string_of(d_3_valueOrError1_))
        d_4_keys_: Signature.SignatureKeyPair
        d_4_keys_ = (d_3_valueOrError1_).Extract()
        default__.RequireGoodKeyLengths(alg, d_4_keys_)
        d_5_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = Signature.ECDSA.Sign(alg, (d_4_keys_).signingKey, d_1_message_)
        d_5_valueOrError2_ = out1_
        if not(not((d_5_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(44,21): " + _dafny.string_of(d_5_valueOrError2_))
        d_6_signature_: _dafny.Seq
        d_6_signature_ = (d_5_valueOrError2_).Extract()
        d_7_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_7_valueOrError3_ = Signature.ECDSA_Verify(alg, (d_4_keys_).verificationKey, d_1_message_, d_6_signature_)
        if not(not((d_7_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(45,24): " + _dafny.string_of(d_7_valueOrError3_))
        d_8_shouldBeTrue_: bool
        d_8_shouldBeTrue_ = (d_7_valueOrError3_).Extract()
        if not(d_8_shouldBeTrue_):
            raise _dafny.HaltException("test/TestSignature.dfy(46,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_9_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_9_valueOrError4_ = Signature.ECDSA_Verify(alg, (d_4_keys_).verificationKey, (d_1_message_) + (_dafny.Seq([1])), d_6_signature_)
        if not(not((d_9_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("test/TestSignature.dfy(48,25): " + _dafny.string_of(d_9_valueOrError4_))
        d_10_shouldBeFalse_: bool
        d_10_shouldBeFalse_ = (d_9_valueOrError4_).Extract()
        if not(not(d_10_shouldBeFalse_)):
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
