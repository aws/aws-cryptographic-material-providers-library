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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import TestSignature as TestSignature
import TestAwsCryptographyPrimitivesHKDF as TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes as TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime as ConstantTime
import ConstantTimeTest as ConstantTimeTest
import TestHKDF__Rfc5869TestVectors as TestHKDF__Rfc5869TestVectors

# Module: TestKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def KdfRawDeriveTest(ikm, info, L, expectedOKM, digestAlgorithm):
        d_51_output_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = KdfCtr.default__.RawDerive(ikm, info, L, 0, digestAlgorithm)
        d_51_output_ = out11_
        if (d_51_output_).is_Success:
            if not((len((d_51_output_).value)) == (L)):
                raise _dafny.HaltException("test/TestKDF.dfy(35,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_51_output_).value) == (expectedOKM)):
                raise _dafny.HaltException("test/TestKDF.dfy(36,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def KdfTest(input, expectedOKM):
        d_52_client_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_53_valueOrError0_: Wrappers.Result = None
        out12_: Wrappers.Result
        out12_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_53_valueOrError0_ = out12_
        if not(not((d_53_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(45,18): " + _dafny.string_of(d_53_valueOrError0_))
        d_52_client_ = (d_53_valueOrError0_).Extract()
        d_54_output_: _dafny.Seq
        d_55_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out13_: Wrappers.Result
        out13_ = (d_52_client_).KdfCounterMode(input)
        d_55_valueOrError1_ = out13_
        if not(not((d_55_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(47,18): " + _dafny.string_of(d_55_valueOrError1_))
        d_54_output_ = (d_55_valueOrError1_).Extract()
        if not((len(d_54_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestKDF.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_54_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestKDF.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

