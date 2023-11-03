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
import Signature

assert "KdfCtr" == __name__
KdfCtr = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def KdfCounterMode(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_368_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_368_valueOrError0_ = Wrappers.default__.Need((((((((input).digestAlgorithm) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256())) and ((len((input).ikm)) == (32))) and (((input).nonce).is_Some)) and ((len(((input).nonce).value)) == (16))) and (((input).expectedLength) == (32))) and (((0) < (((input).expectedLength) * (8))) and ((((input).expectedLength) * (8)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Kdf in Counter Mode input is invalid.")))
        if (d_368_valueOrError0_).IsFailure():
            output = (d_368_valueOrError0_).PropagateFailure()
            return output
        d_369_ikm_: _dafny.Seq
        d_369_ikm_ = (input).ikm
        d_370_label___: _dafny.Seq
        d_370_label___ = ((input).purpose).UnwrapOr(_dafny.Seq([]))
        d_371_info_: _dafny.Seq
        d_371_info_ = ((input).nonce).UnwrapOr(_dafny.Seq([]))
        d_372_okm_: _dafny.Seq
        d_372_okm_ = _dafny.Seq([])
        d_373_internalLength_: BoundedInts.uint32
        d_373_internalLength_ = ((4) + (len((KdfCtr.default__).SEPARATION__INDICATOR))) + (4)
        d_374_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_374_valueOrError1_ = Wrappers.default__.Need((True) and ((((d_373_internalLength_) + (len(d_370_label___))) + (len(d_371_info_))) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Input Length exceeds INT32_MAX_LIMIT")))
        if (d_374_valueOrError1_).IsFailure():
            output = (d_374_valueOrError1_).PropagateFailure()
            return output
        d_375_lengthBits_: _dafny.Seq
        d_375_lengthBits_ = StandardLibrary_mUInt.default__.UInt32ToSeq(((input).expectedLength) * (8))
        d_376_explicitInfo_: _dafny.Seq
        d_376_explicitInfo_ = (((d_370_label___) + ((KdfCtr.default__).SEPARATION__INDICATOR)) + (d_371_info_)) + (d_375_lengthBits_)
        d_377_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_377_valueOrError2_ = Wrappers.default__.Need(((4) + (len(d_376_explicitInfo_))) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("PRF input length exceeds INT32_MAX_LIMIT.")))
        if (d_377_valueOrError2_).IsFailure():
            output = (d_377_valueOrError2_).PropagateFailure()
            return output
        d_378_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out73_: Wrappers.Result
        out73_ = KdfCtr.default__.RawDerive(d_369_ikm_, d_376_explicitInfo_, (input).expectedLength, 0)
        d_378_valueOrError3_ = out73_
        if (d_378_valueOrError3_).IsFailure():
            output = (d_378_valueOrError3_).PropagateFailure()
            return output
        d_372_okm_ = (d_378_valueOrError3_).Extract()
        output = Wrappers.Result_Success(d_372_okm_)
        return output
        return output

    @staticmethod
    def RawDerive(ikm, explicitInfo, length, offset):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_379_derivationMac_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_379_derivationMac_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()
        d_380_hmac_: HMAC.HMac
        d_381_valueOrError0_: Wrappers.Result = None
        out74_: Wrappers.Result
        out74_ = HMAC.HMac.Build(d_379_derivationMac_)
        d_381_valueOrError0_ = out74_
        if (d_381_valueOrError0_).IsFailure():
            output = (d_381_valueOrError0_).PropagateFailure()
            return output
        d_380_hmac_ = (d_381_valueOrError0_).Extract()
        (d_380_hmac_).Init(ikm)
        d_382_macLengthBytes_: BoundedInts.int32
        d_382_macLengthBytes_ = Digest.default__.Length(d_379_derivationMac_)
        d_383_iterations_: BoundedInts.int32
        d_383_iterations_ = _dafny.euclidian_division(((length) + (d_382_macLengthBytes_)) - (1), d_382_macLengthBytes_)
        d_384_buffer_: _dafny.Seq
        d_384_buffer_ = _dafny.Seq([])
        d_385_i_: _dafny.Seq
        d_385_i_ = StandardLibrary_mUInt.default__.UInt32ToSeq((KdfCtr.default__).COUNTER__START__VALUE)
        hi0_: BoundedInts.int32 = (d_383_iterations_) + (1)
        for d_386_iteration_ in range(1, hi0_):
            (d_380_hmac_).BlockUpdate(d_385_i_)
            (d_380_hmac_).BlockUpdate(explicitInfo)
            d_387_tmp_: _dafny.Seq
            out75_: _dafny.Seq
            out75_ = (d_380_hmac_).GetResult()
            d_387_tmp_ = out75_
            d_384_buffer_ = (d_384_buffer_) + (d_387_tmp_)
            d_388_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
            d_388_valueOrError1_ = KdfCtr.default__.Increment(d_385_i_)
            if (d_388_valueOrError1_).IsFailure():
                output = (d_388_valueOrError1_).PropagateFailure()
                return output
            d_385_i_ = (d_388_valueOrError1_).Extract()
        d_389_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_389_valueOrError2_ = Wrappers.default__.Need((len(d_384_buffer_)) >= (length), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Failed to derive key of requested length")))
        if (d_389_valueOrError2_).IsFailure():
            output = (d_389_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(_dafny.Seq((d_384_buffer_)[:length:]))
        return output
        return output

    @staticmethod
    def Increment(x):
        if ((x)[3]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([(x)[0], (x)[1], (x)[2], ((x)[3]) + (1)]))
        elif ((x)[2]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([(x)[0], (x)[1], ((x)[2]) + (1), 0]))
        elif ((x)[1]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([(x)[0], ((x)[1]) + (1), 0, 0]))
        elif ((x)[0]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([((x)[0]) + (1), 0, 0, 0]))
        elif True:
            return Wrappers.Result_Failure(software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unable to derive key material; may have exceeded limit.")))

    @_dafny.classproperty
    def SEPARATION__INDICATOR(instance):
        return _dafny.Seq([0])
    @_dafny.classproperty
    def COUNTER__START__VALUE(instance):
        return 1
