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

assert "AESEncryption" == __name__
AESEncryption = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionOutputFromByteSeq(s, encAlg):
        d_290_cipherText_ = _dafny.Seq((s)[:(len(s)) - ((encAlg).tagLength):])
        d_291_authTag_ = _dafny.Seq((s)[(len(s)) - ((encAlg).tagLength)::])
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(d_290_cipherText_, d_291_authTag_)

    @staticmethod
    def AESEncrypt(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        d_292_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_292_valueOrError0_ = Wrappers.default__.Need(((len((input).iv)) == (((input).encAlg).ivLength)) and ((len((input).key)) == (((input).encAlg).keyLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_292_valueOrError0_).IsFailure():
            res = (d_292_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs0_ = input
        d_293_encAlg_ = let_tmp_rhs0_.encAlg
        d_294_iv_ = let_tmp_rhs0_.iv
        d_295_key_ = let_tmp_rhs0_.key
        d_296_msg_ = let_tmp_rhs0_.msg
        d_297_aad_ = let_tmp_rhs0_.aad
        d_298_value_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_299_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out55_: Wrappers.Result
        out55_ = AESEncryption.AES_GCM.AESEncryptExtern(d_293_encAlg_, d_294_iv_, d_295_key_, d_296_msg_, d_297_aad_)
        d_299_valueOrError1_ = out55_
        if (d_299_valueOrError1_).IsFailure():
            res = (d_299_valueOrError1_).PropagateFailure()
            return res
        d_298_value_ = (d_299_valueOrError1_).Extract()
        d_300_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_300_valueOrError2_ = Wrappers.default__.Need((len((d_298_value_).cipherText)) == (len(d_296_msg_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncrypt did not return cipherText of expected length")))
        if (d_300_valueOrError2_).IsFailure():
            res = (d_300_valueOrError2_).PropagateFailure()
            return res
        d_301_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_301_valueOrError3_ = Wrappers.default__.Need((len((d_298_value_).authTag)) == ((d_293_encAlg_).tagLength), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncryption did not return valid tag")))
        if (d_301_valueOrError3_).IsFailure():
            res = (d_301_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_298_value_)
        return res
        return res

    @staticmethod
    def AESDecrypt(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_302_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_302_valueOrError0_ = Wrappers.default__.Need((((len((input).key)) == (((input).encAlg).keyLength)) and ((len((input).iv)) == (((input).encAlg).ivLength))) and ((len((input).authTag)) == (((input).encAlg).tagLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_302_valueOrError0_).IsFailure():
            res = (d_302_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs1_ = input
        d_303_encAlg_ = let_tmp_rhs1_.encAlg
        d_304_key_ = let_tmp_rhs1_.key
        d_305_cipherTxt_ = let_tmp_rhs1_.cipherTxt
        d_306_authTag_ = let_tmp_rhs1_.authTag
        d_307_iv_ = let_tmp_rhs1_.iv
        d_308_aad_ = let_tmp_rhs1_.aad
        d_309_value_: _dafny.Seq
        d_310_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out56_: Wrappers.Result
        out56_ = AESEncryption.AES_GCM.AESDecryptExtern(d_303_encAlg_, d_304_key_, d_305_cipherTxt_, d_306_authTag_, d_307_iv_, d_308_aad_)
        d_310_valueOrError1_ = out56_
        if (d_310_valueOrError1_).IsFailure():
            res = (d_310_valueOrError1_).PropagateFailure()
            return res
        d_309_value_ = (d_310_valueOrError1_).Extract()
        d_311_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_311_valueOrError2_ = Wrappers.default__.Need((len(d_305_cipherTxt_)) == (len(d_309_value_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESDecrypt did not return plaintext of expected length")))
        if (d_311_valueOrError2_).IsFailure():
            res = (d_311_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_309_value_)
        return res
        return res

