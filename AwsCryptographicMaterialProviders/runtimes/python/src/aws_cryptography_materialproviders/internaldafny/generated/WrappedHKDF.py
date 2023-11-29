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

# assert "WrappedHKDF" == __name__
WrappedHKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_343_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_343_valueOrError0_ = Wrappers.default__.Need(((((input).salt).is_None) or ((len(((input).salt).value)) != (0))) and ((len((input).ikm)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Extract needs a salt and reasonable ikm.")))
        if (d_343_valueOrError0_).IsFailure():
            output = (d_343_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs3_ = input
        d_344_digestAlgorithm_ = let_tmp_rhs3_.digestAlgorithm
        d_345_salt_ = let_tmp_rhs3_.salt
        d_346_ikm_ = let_tmp_rhs3_.ikm
        d_347_hmac_: HMAC.HMac
        d_348_valueOrError1_: Wrappers.Result = None
        out67_: Wrappers.Result
        out67_ = HMAC.HMac.Build(d_344_digestAlgorithm_)
        d_348_valueOrError1_ = out67_
        if (d_348_valueOrError1_).IsFailure():
            output = (d_348_valueOrError1_).PropagateFailure()
            return output
        d_347_hmac_ = (d_348_valueOrError1_).Extract()
        d_349_prk_: _dafny.Seq
        out68_: _dafny.Seq
        out68_ = HKDF.default__.Extract(d_347_hmac_, (d_345_salt_).UnwrapOr(StandardLibrary.default__.Fill(0, Digest.default__.Length(d_344_digestAlgorithm_))), d_346_ikm_)
        d_349_prk_ = out68_
        output = Wrappers.Result_Success(d_349_prk_)
        return output
        return output

    @staticmethod
    def Expand(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_350_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_350_valueOrError0_ = Wrappers.default__.Need(((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((len((input).info)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))) and ((Digest.default__.Length((input).digestAlgorithm)) == (len((input).prk))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Expand needs valid input.")))
        if (d_350_valueOrError0_).IsFailure():
            output = (d_350_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs4_ = input
        d_351_digestAlgorithm_ = let_tmp_rhs4_.digestAlgorithm
        d_352_prk_ = let_tmp_rhs4_.prk
        d_353_info_ = let_tmp_rhs4_.info
        d_354_expectedLength_ = let_tmp_rhs4_.expectedLength
        d_355_hmac_: HMAC.HMac
        d_356_valueOrError1_: Wrappers.Result = None
        out69_: Wrappers.Result
        out69_ = HMAC.HMac.Build(d_351_digestAlgorithm_)
        d_356_valueOrError1_ = out69_
        if (d_356_valueOrError1_).IsFailure():
            output = (d_356_valueOrError1_).PropagateFailure()
            return output
        d_355_hmac_ = (d_356_valueOrError1_).Extract()
        d_357_omk_: _dafny.Seq
        out70_: _dafny.Seq
        out70_ = HKDF.default__.Expand(d_355_hmac_, d_352_prk_, d_353_info_, d_354_expectedLength_, d_351_digestAlgorithm_)
        d_357_omk_ = out70_
        output = Wrappers.Result_Success(d_357_omk_)
        return output
        return output

    @staticmethod
    def Hkdf(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_358_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_358_valueOrError0_ = Wrappers.default__.Need((((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((((input).salt).is_None) or ((len(((input).salt).value)) != (0)))) and ((len((input).info)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))) and ((len((input).ikm)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Wrapped Hkdf input is invalid.")))
        if (d_358_valueOrError0_).IsFailure():
            output = (d_358_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs5_ = input
        d_359_digest_ = let_tmp_rhs5_.digestAlgorithm
        d_360_salt_ = let_tmp_rhs5_.salt
        d_361_ikm_ = let_tmp_rhs5_.ikm
        d_362_info_ = let_tmp_rhs5_.info
        d_363_expectedLength_ = let_tmp_rhs5_.expectedLength
        d_364_okm_: _dafny.Seq
        out71_: _dafny.Seq
        out71_ = HKDF.default__.Hkdf(d_359_digest_, d_360_salt_, d_361_ikm_, d_362_info_, d_363_expectedLength_)
        d_364_okm_ = out71_
        output = Wrappers.Result_Success(d_364_okm_)
        return output
        return output

