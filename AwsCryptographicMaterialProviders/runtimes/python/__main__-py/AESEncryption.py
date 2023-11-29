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

assert "AESEncryption" == __name__
AESEncryption = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionOutputFromByteSeq(s, encAlg):
        d_300_cipherText_ = _dafny.Seq((s)[:(len(s)) - ((encAlg).tagLength):])
        d_301_authTag_ = _dafny.Seq((s)[(len(s)) - ((encAlg).tagLength)::])
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(d_300_cipherText_, d_301_authTag_)

    @staticmethod
    def AESEncrypt(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        d_302_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_302_valueOrError0_ = Wrappers.default__.Need(((len((input).iv)) == (((input).encAlg).ivLength)) and ((len((input).key)) == (((input).encAlg).keyLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_302_valueOrError0_).IsFailure():
            res = (d_302_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs0_ = input
        d_303_encAlg_ = let_tmp_rhs0_.encAlg
        d_304_iv_ = let_tmp_rhs0_.iv
        d_305_key_ = let_tmp_rhs0_.key
        d_306_msg_ = let_tmp_rhs0_.msg
        d_307_aad_ = let_tmp_rhs0_.aad
        d_308_value_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_309_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out59_: Wrappers.Result
        out59_ = AESEncryption.AES_GCM.AESEncryptExtern(d_303_encAlg_, d_304_iv_, d_305_key_, d_306_msg_, d_307_aad_)
        d_309_valueOrError1_ = out59_
        if (d_309_valueOrError1_).IsFailure():
            res = (d_309_valueOrError1_).PropagateFailure()
            return res
        d_308_value_ = (d_309_valueOrError1_).Extract()
        d_310_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_310_valueOrError2_ = Wrappers.default__.Need((len((d_308_value_).cipherText)) == (len(d_306_msg_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncrypt did not return cipherText of expected length")))
        if (d_310_valueOrError2_).IsFailure():
            res = (d_310_valueOrError2_).PropagateFailure()
            return res
        d_311_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_311_valueOrError3_ = Wrappers.default__.Need((len((d_308_value_).authTag)) == ((d_303_encAlg_).tagLength), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncryption did not return valid tag")))
        if (d_311_valueOrError3_).IsFailure():
            res = (d_311_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_308_value_)
        return res
        return res

    @staticmethod
    def AESDecrypt(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_312_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_312_valueOrError0_ = Wrappers.default__.Need((((len((input).key)) == (((input).encAlg).keyLength)) and ((len((input).iv)) == (((input).encAlg).ivLength))) and ((len((input).authTag)) == (((input).encAlg).tagLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_312_valueOrError0_).IsFailure():
            res = (d_312_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs1_ = input
        d_313_encAlg_ = let_tmp_rhs1_.encAlg
        d_314_key_ = let_tmp_rhs1_.key
        d_315_cipherTxt_ = let_tmp_rhs1_.cipherTxt
        d_316_authTag_ = let_tmp_rhs1_.authTag
        d_317_iv_ = let_tmp_rhs1_.iv
        d_318_aad_ = let_tmp_rhs1_.aad
        d_319_value_: _dafny.Seq
        d_320_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out60_: Wrappers.Result
        out60_ = AESEncryption.AES_GCM.AESDecryptExtern(d_313_encAlg_, d_314_key_, d_315_cipherTxt_, d_316_authTag_, d_317_iv_, d_318_aad_)
        d_320_valueOrError1_ = out60_
        if (d_320_valueOrError1_).IsFailure():
            res = (d_320_valueOrError1_).PropagateFailure()
            return res
        d_319_value_ = (d_320_valueOrError1_).Extract()
        d_321_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_321_valueOrError2_ = Wrappers.default__.Need((len(d_315_cipherTxt_)) == (len(d_319_value_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESDecrypt did not return plaintext of expected length")))
        if (d_321_valueOrError2_).IsFailure():
            res = (d_321_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_319_value_)
        return res
        return res

