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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF

assert "WrappedHKDF" == __name__
WrappedHKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_333_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_333_valueOrError0_ = Wrappers.default__.Need(((((input).salt).is_None) or ((len(((input).salt).value)) != (0))) and ((len((input).ikm)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Extract needs a salt and reasonable ikm.")))
        if (d_333_valueOrError0_).IsFailure():
            output = (d_333_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs3_ = input
        d_334_digestAlgorithm_ = let_tmp_rhs3_.digestAlgorithm
        d_335_salt_ = let_tmp_rhs3_.salt
        d_336_ikm_ = let_tmp_rhs3_.ikm
        d_337_hmac_: HMAC.HMac
        d_338_valueOrError1_: Wrappers.Result = None
        out63_: Wrappers.Result
        out63_ = HMAC.HMac.Build(d_334_digestAlgorithm_)
        d_338_valueOrError1_ = out63_
        if (d_338_valueOrError1_).IsFailure():
            output = (d_338_valueOrError1_).PropagateFailure()
            return output
        d_337_hmac_ = (d_338_valueOrError1_).Extract()
        d_339_prk_: _dafny.Seq
        out64_: _dafny.Seq
        out64_ = HKDF.default__.Extract(d_337_hmac_, (d_335_salt_).UnwrapOr(StandardLibrary.default__.Fill(0, Digest.default__.Length(d_334_digestAlgorithm_))), d_336_ikm_)
        d_339_prk_ = out64_
        output = Wrappers.Result_Success(d_339_prk_)
        return output
        return output

    @staticmethod
    def Expand(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_340_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_340_valueOrError0_ = Wrappers.default__.Need(((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((len((input).info)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))) and ((Digest.default__.Length((input).digestAlgorithm)) == (len((input).prk))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Expand needs valid input.")))
        if (d_340_valueOrError0_).IsFailure():
            output = (d_340_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs4_ = input
        d_341_digestAlgorithm_ = let_tmp_rhs4_.digestAlgorithm
        d_342_prk_ = let_tmp_rhs4_.prk
        d_343_info_ = let_tmp_rhs4_.info
        d_344_expectedLength_ = let_tmp_rhs4_.expectedLength
        d_345_hmac_: HMAC.HMac
        d_346_valueOrError1_: Wrappers.Result = None
        out65_: Wrappers.Result
        out65_ = HMAC.HMac.Build(d_341_digestAlgorithm_)
        d_346_valueOrError1_ = out65_
        if (d_346_valueOrError1_).IsFailure():
            output = (d_346_valueOrError1_).PropagateFailure()
            return output
        d_345_hmac_ = (d_346_valueOrError1_).Extract()
        d_347_omk_: _dafny.Seq
        out66_: _dafny.Seq
        out66_ = HKDF.default__.Expand(d_345_hmac_, d_342_prk_, d_343_info_, d_344_expectedLength_, d_341_digestAlgorithm_)
        d_347_omk_ = out66_
        output = Wrappers.Result_Success(d_347_omk_)
        return output
        return output

    @staticmethod
    def Hkdf(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_348_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_348_valueOrError0_ = Wrappers.default__.Need((((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((((input).salt).is_None) or ((len(((input).salt).value)) != (0)))) and ((len((input).info)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))) and ((len((input).ikm)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Wrapped Hkdf input is invalid.")))
        if (d_348_valueOrError0_).IsFailure():
            output = (d_348_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs5_ = input
        d_349_digest_ = let_tmp_rhs5_.digestAlgorithm
        d_350_salt_ = let_tmp_rhs5_.salt
        d_351_ikm_ = let_tmp_rhs5_.ikm
        d_352_info_ = let_tmp_rhs5_.info
        d_353_expectedLength_ = let_tmp_rhs5_.expectedLength
        d_354_okm_: _dafny.Seq
        out67_: _dafny.Seq
        out67_ = HKDF.default__.Hkdf(d_349_digest_, d_350_salt_, d_351_ikm_, d_352_info_, d_353_expectedLength_)
        d_354_okm_ = out67_
        output = Wrappers.Result_Success(d_354_okm_)
        return output
        return output

