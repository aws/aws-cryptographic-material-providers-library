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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF

# Module: WrappedHKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_251_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_251_valueOrError0_ = Wrappers.default__.Need(((((input).salt).is_None) or ((len(((input).salt).value)) != (0))) and ((len((input).ikm)) < (StandardLibrary_mUInt.default__.INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Extract needs a salt and reasonable ikm.")))
        if (d_251_valueOrError0_).IsFailure():
            output = (d_251_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs3_ = input
        d_252_digestAlgorithm_ = let_tmp_rhs3_.digestAlgorithm
        d_253_salt_ = let_tmp_rhs3_.salt
        d_254_ikm_ = let_tmp_rhs3_.ikm
        d_255_hmac_: HMAC.HMac
        d_256_valueOrError1_: Wrappers.Result = None
        out26_: Wrappers.Result
        out26_ = HMAC.HMac.Build(d_252_digestAlgorithm_)
        d_256_valueOrError1_ = out26_
        if (d_256_valueOrError1_).IsFailure():
            output = (d_256_valueOrError1_).PropagateFailure()
            return output
        d_255_hmac_ = (d_256_valueOrError1_).Extract()
        d_257_prk_: _dafny.Seq
        out27_: _dafny.Seq
        out27_ = HKDF.default__.Extract(d_255_hmac_, (d_253_salt_).UnwrapOr(StandardLibrary.default__.Fill(0, Digest.default__.Length(d_252_digestAlgorithm_))), d_254_ikm_)
        d_257_prk_ = out27_
        output = Wrappers.Result_Success(d_257_prk_)
        return output
        return output

    @staticmethod
    def Expand(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_258_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_258_valueOrError0_ = Wrappers.default__.Need(((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((len((input).info)) < (StandardLibrary_mUInt.default__.INT32__MAX__LIMIT))) and ((Digest.default__.Length((input).digestAlgorithm)) == (len((input).prk))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Expand needs valid input.")))
        if (d_258_valueOrError0_).IsFailure():
            output = (d_258_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs4_ = input
        d_259_digestAlgorithm_ = let_tmp_rhs4_.digestAlgorithm
        d_260_prk_ = let_tmp_rhs4_.prk
        d_261_info_ = let_tmp_rhs4_.info
        d_262_expectedLength_ = let_tmp_rhs4_.expectedLength
        d_263_hmac_: HMAC.HMac
        d_264_valueOrError1_: Wrappers.Result = None
        out28_: Wrappers.Result
        out28_ = HMAC.HMac.Build(d_259_digestAlgorithm_)
        d_264_valueOrError1_ = out28_
        if (d_264_valueOrError1_).IsFailure():
            output = (d_264_valueOrError1_).PropagateFailure()
            return output
        d_263_hmac_ = (d_264_valueOrError1_).Extract()
        d_265_omk_: _dafny.Seq
        out29_: _dafny.Seq
        out29_ = HKDF.default__.Expand(d_263_hmac_, d_260_prk_, d_261_info_, d_262_expectedLength_, d_259_digestAlgorithm_)
        d_265_omk_ = out29_
        output = Wrappers.Result_Success(d_265_omk_)
        return output
        return output

    @staticmethod
    def Hkdf(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_266_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_266_valueOrError0_ = Wrappers.default__.Need((((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((((input).salt).is_None) or ((len(((input).salt).value)) != (0)))) and ((len((input).info)) < (StandardLibrary_mUInt.default__.INT32__MAX__LIMIT))) and ((len((input).ikm)) < (StandardLibrary_mUInt.default__.INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Wrapped Hkdf input is invalid.")))
        if (d_266_valueOrError0_).IsFailure():
            output = (d_266_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs5_ = input
        d_267_digest_ = let_tmp_rhs5_.digestAlgorithm
        d_268_salt_ = let_tmp_rhs5_.salt
        d_269_ikm_ = let_tmp_rhs5_.ikm
        d_270_info_ = let_tmp_rhs5_.info
        d_271_expectedLength_ = let_tmp_rhs5_.expectedLength
        d_272_okm_: _dafny.Seq
        out30_: _dafny.Seq
        out30_ = HKDF.default__.Hkdf(d_267_digest_, d_268_salt_, d_269_ikm_, d_270_info_, d_271_expectedLength_)
        d_272_okm_ = out30_
        output = Wrappers.Result_Success(d_272_okm_)
        return output
        return output

