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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF

assert "Signature" == __name__
Signature = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SignatureLength(signatureAlgorithm):
        source12_ = signatureAlgorithm
        if source12_.is_ECDSA__P384:
            return 103
        elif True:
            return 71

    @staticmethod
    def FieldSize(signatureAlgorithm):
        source13_ = signatureAlgorithm
        if source13_.is_ECDSA__P384:
            return 49
        elif True:
            return 33

    @staticmethod
    def KeyGen(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        d_365_sigKeyPair_: Signature.SignatureKeyPair
        d_366_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(Signature.SignatureKeyPair.default())()
        out72_: Wrappers.Result
        out72_ = Signature.ECDSA.ExternKeyGen((input).signatureAlgorithm)
        d_366_valueOrError0_ = out72_
        if (d_366_valueOrError0_).IsFailure():
            res = (d_366_valueOrError0_).PropagateFailure()
            return res
        d_365_sigKeyPair_ = (d_366_valueOrError0_).Extract()
        d_367_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_367_valueOrError1_ = Wrappers.default__.Need((len((d_365_sigKeyPair_).verificationKey)) == (Signature.default__.FieldSize((input).signatureAlgorithm)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect verification-key length from ExternKeyGen.")))
        if (d_367_valueOrError1_).IsFailure():
            res = (d_367_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput((input).signatureAlgorithm, (d_365_sigKeyPair_).verificationKey, (d_365_sigKeyPair_).signingKey))
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
        return isinstance(self, Signature.SignatureKeyPair_SignatureKeyPair)

class SignatureKeyPair_SignatureKeyPair(SignatureKeyPair, NamedTuple('SignatureKeyPair', [('verificationKey', Any), ('signingKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'Signature.SignatureKeyPair.SignatureKeyPair({_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.signingKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Signature.SignatureKeyPair_SignatureKeyPair) and self.verificationKey == __o.verificationKey and self.signingKey == __o.signingKey
    def __hash__(self) -> int:
        return super().__hash__()

