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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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
import TestSignature as TestSignature
import TestAwsCryptographyPrimitivesHKDF as TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes as TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime as ConstantTime
import ConstantTimeTest as ConstantTimeTest
import TestHKDF__Rfc5869TestVectors as TestHKDF__Rfc5869TestVectors
import TestKDF as TestKDF
import TestKDFK__TestVectors as TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesRSA as TestAwsCryptographyPrimitivesRSA

# Module: TestAwsCryptographyPrimitivesAES

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AESDecryptTests():
        default__.BasicAESDecryptTest(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(32, 16, 12), _dafny.Seq([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), _dafny.Seq([102, 165, 173, 47]), _dafny.Seq([54, 200, 18, 56, 172, 194, 174, 23, 239, 151, 47, 180, 143, 232, 142, 184]), _dafny.Seq([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), _dafny.Seq([3, 3, 3, 3])), _dafny.Seq([97, 115, 100, 102]))

    @staticmethod
    def AESEncryptTests():
        default__.BasicAESEncryptTest(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(32, 16, 12), _dafny.Seq([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), _dafny.Seq([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([3, 3, 3, 3])))

    @staticmethod
    def BasicAESDecryptTest(input, expectedOutput):
        d_117_client_: AtomicPrimitives.AtomicPrimitivesClient
        d_118_valueOrError0_: Wrappers.Result = None
        out21_: Wrappers.Result
        out21_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_118_valueOrError0_ = out21_
        if not(not((d_118_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(99,18): " + _dafny.string_of(d_118_valueOrError0_))
        d_117_client_ = (d_118_valueOrError0_).Extract()
        d_119_output_: _dafny.Seq
        d_120_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out22_: Wrappers.Result
        out22_ = (d_117_client_).AESDecrypt(input)
        d_120_valueOrError1_ = out22_
        if not(not((d_120_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(100,18): " + _dafny.string_of(d_120_valueOrError1_))
        d_119_output_ = (d_120_valueOrError1_).Extract()
        if not((d_119_output_) == (expectedOutput)):
            raise _dafny.HaltException("test/TestAES.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicAESEncryptTest(input):
        d_121_client_: AtomicPrimitives.AtomicPrimitivesClient
        d_122_valueOrError0_: Wrappers.Result = None
        out23_: Wrappers.Result
        out23_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_122_valueOrError0_ = out23_
        if not(not((d_122_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(108,18): " + _dafny.string_of(d_122_valueOrError0_))
        d_121_client_ = (d_122_valueOrError0_).Extract()
        d_123_output_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_124_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        out24_: Wrappers.Result
        out24_ = (d_121_client_).AESEncrypt(input)
        d_124_valueOrError1_ = out24_
        if not(not((d_124_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(109,18): " + _dafny.string_of(d_124_valueOrError1_))
        d_123_output_ = (d_124_valueOrError1_).Extract()
        d_125_decryptInput_: AwsCryptographyPrimitivesTypes.AESDecryptInput
        d_125_decryptInput_ = AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput((input).encAlg, (input).key, (d_123_output_).cipherText, (d_123_output_).authTag, (input).iv, (input).aad)
        default__.BasicAESDecryptTest(d_125_decryptInput_, (input).msg)

