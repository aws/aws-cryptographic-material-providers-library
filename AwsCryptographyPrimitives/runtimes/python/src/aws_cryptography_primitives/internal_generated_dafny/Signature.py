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

# Module: Signature

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SignatureLength(signatureAlgorithm):
        source2_ = signatureAlgorithm
        if source2_.is_ECDSA__P384:
            return 103
        elif True:
            return 71

    @staticmethod
    def FieldSize(signatureAlgorithm):
        source3_ = signatureAlgorithm
        if source3_.is_ECDSA__P384:
            return 49
        elif True:
            return 33

    @staticmethod
    def KeyGen(input):
        res: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        d_68_sigKeyPair_: SignatureKeyPair
        d_69_valueOrError0_: Wrappers.Result = Wrappers.Result.default(SignatureKeyPair.default())()
        out14_: Wrappers.Result
        out14_ = ECDSA.ExternKeyGen((input).signatureAlgorithm)
        d_69_valueOrError0_ = out14_
        if (d_69_valueOrError0_).IsFailure():
            res = (d_69_valueOrError0_).PropagateFailure()
            return res
        d_68_sigKeyPair_ = (d_69_valueOrError0_).Extract()
        d_70_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_70_valueOrError1_ = Wrappers.default__.Need((len((d_68_sigKeyPair_).verificationKey)) == (default__.FieldSize((input).signatureAlgorithm)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect verification-key length from ExternKeyGen.")))
        if (d_70_valueOrError1_).IsFailure():
            res = (d_70_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput((input).signatureAlgorithm, (d_68_sigKeyPair_).verificationKey, (d_68_sigKeyPair_).signingKey))
        return res
        return res


class SignatureKeyPair:
    @classmethod
    def default(cls, ):
        return lambda: SignatureKeyPair_SignatureKeyPair(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SignatureKeyPair(self) -> bool:
        return isinstance(self, SignatureKeyPair_SignatureKeyPair)

class SignatureKeyPair_SignatureKeyPair(SignatureKeyPair, NamedTuple('SignatureKeyPair', [('verificationKey', Any), ('signingKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'SignatureKeyPair.SignatureKeyPair({_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.signingKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SignatureKeyPair_SignatureKeyPair) and self.verificationKey == __o.verificationKey and self.signingKey == __o.signingKey
    def __hash__(self) -> int:
        return super().__hash__()

