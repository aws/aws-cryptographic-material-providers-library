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
        d_358_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_358_valueOrError0_ = Wrappers.default__.Need((((((((input).digestAlgorithm) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256())) and ((len((input).ikm)) == (32))) and (((input).nonce).is_Some)) and ((len(((input).nonce).value)) == (16))) and (((input).expectedLength) == (32))) and (((0) < (((input).expectedLength) * (8))) and ((((input).expectedLength) * (8)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Kdf in Counter Mode input is invalid.")))
        if (d_358_valueOrError0_).IsFailure():
            output = (d_358_valueOrError0_).PropagateFailure()
            return output
        d_359_ikm_: _dafny.Seq
        d_359_ikm_ = (input).ikm
        d_360_label___: _dafny.Seq
        d_360_label___ = ((input).purpose).UnwrapOr(_dafny.Seq([]))
        d_361_info_: _dafny.Seq
        d_361_info_ = ((input).nonce).UnwrapOr(_dafny.Seq([]))
        d_362_okm_: _dafny.Seq
        d_362_okm_ = _dafny.Seq([])
        d_363_internalLength_: BoundedInts.uint32
        d_363_internalLength_ = ((4) + (len((KdfCtr.default__).SEPARATION__INDICATOR))) + (4)
        d_364_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_364_valueOrError1_ = Wrappers.default__.Need((True) and ((((d_363_internalLength_) + (len(d_360_label___))) + (len(d_361_info_))) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Input Length exceeds INT32_MAX_LIMIT")))
        if (d_364_valueOrError1_).IsFailure():
            output = (d_364_valueOrError1_).PropagateFailure()
            return output
        d_365_lengthBits_: _dafny.Seq
        d_365_lengthBits_ = StandardLibrary_mUInt.default__.UInt32ToSeq(((input).expectedLength) * (8))
        d_366_explicitInfo_: _dafny.Seq
        d_366_explicitInfo_ = (((d_360_label___) + ((KdfCtr.default__).SEPARATION__INDICATOR)) + (d_361_info_)) + (d_365_lengthBits_)
        d_367_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_367_valueOrError2_ = Wrappers.default__.Need(((4) + (len(d_366_explicitInfo_))) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("PRF input length exceeds INT32_MAX_LIMIT.")))
        if (d_367_valueOrError2_).IsFailure():
            output = (d_367_valueOrError2_).PropagateFailure()
            return output
        d_368_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out69_: Wrappers.Result
        out69_ = KdfCtr.default__.RawDerive(d_359_ikm_, d_366_explicitInfo_, (input).expectedLength, 0)
        d_368_valueOrError3_ = out69_
        if (d_368_valueOrError3_).IsFailure():
            output = (d_368_valueOrError3_).PropagateFailure()
            return output
        d_362_okm_ = (d_368_valueOrError3_).Extract()
        output = Wrappers.Result_Success(d_362_okm_)
        return output
        return output

    @staticmethod
    def RawDerive(ikm, explicitInfo, length, offset):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_369_derivationMac_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_369_derivationMac_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()
        d_370_hmac_: HMAC.HMac
        d_371_valueOrError0_: Wrappers.Result = None
        out70_: Wrappers.Result
        out70_ = HMAC.HMac.Build(d_369_derivationMac_)
        d_371_valueOrError0_ = out70_
        if (d_371_valueOrError0_).IsFailure():
            output = (d_371_valueOrError0_).PropagateFailure()
            return output
        d_370_hmac_ = (d_371_valueOrError0_).Extract()
        (d_370_hmac_).Init(ikm)
        d_372_macLengthBytes_: BoundedInts.int32
        d_372_macLengthBytes_ = Digest.default__.Length(d_369_derivationMac_)
        d_373_iterations_: BoundedInts.int32
        d_373_iterations_ = _dafny.euclidian_division(((length) + (d_372_macLengthBytes_)) - (1), d_372_macLengthBytes_)
        d_374_buffer_: _dafny.Seq
        d_374_buffer_ = _dafny.Seq([])
        d_375_i_: _dafny.Seq
        d_375_i_ = StandardLibrary_mUInt.default__.UInt32ToSeq((KdfCtr.default__).COUNTER__START__VALUE)
        hi0_: BoundedInts.int32 = (d_373_iterations_) + (1)
        for d_376_iteration_ in range(1, hi0_):
            (d_370_hmac_).BlockUpdate(d_375_i_)
            (d_370_hmac_).BlockUpdate(explicitInfo)
            d_377_tmp_: _dafny.Seq
            out71_: _dafny.Seq
            out71_ = (d_370_hmac_).GetResult()
            d_377_tmp_ = out71_
            d_374_buffer_ = (d_374_buffer_) + (d_377_tmp_)
            d_378_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
            d_378_valueOrError1_ = KdfCtr.default__.Increment(d_375_i_)
            if (d_378_valueOrError1_).IsFailure():
                output = (d_378_valueOrError1_).PropagateFailure()
                return output
            d_375_i_ = (d_378_valueOrError1_).Extract()
        d_379_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_379_valueOrError2_ = Wrappers.default__.Need((len(d_374_buffer_)) >= (length), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Failed to derive key of requested length")))
        if (d_379_valueOrError2_).IsFailure():
            output = (d_379_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(_dafny.Seq((d_374_buffer_)[:length:]))
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
