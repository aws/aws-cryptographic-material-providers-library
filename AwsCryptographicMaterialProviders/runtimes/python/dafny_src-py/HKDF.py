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

assert "HKDF" == __name__
HKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(hmac, salt, ikm):
        prk: _dafny.Seq = _dafny.Seq({})
        (hmac).Init(salt)
        (hmac).BlockUpdate(ikm)
        out58_: _dafny.Seq
        out58_ = (hmac).GetResult()
        prk = out58_
        prk = prk
        return prk
        return prk

    @staticmethod
    def Expand(hmac, prk, info, expectedLength, digest):
        okm: _dafny.Seq = _dafny.Seq({})
        d_321_hashLength_: int
        d_321_hashLength_ = Digest.default__.Length(digest)
        d_322_n_: int
        d_322_n_ = _dafny.euclidian_division(((d_321_hashLength_) + (expectedLength)) - (1), d_321_hashLength_)
        (hmac).Init(prk)
        d_323_t__prev_: _dafny.Seq
        d_323_t__prev_ = _dafny.Seq([])
        d_324_t__n_: _dafny.Seq
        d_324_t__n_ = d_323_t__prev_
        d_325_i_: int
        d_325_i_ = 1
        while (d_325_i_) <= (d_322_n_):
            (hmac).BlockUpdate(d_323_t__prev_)
            (hmac).BlockUpdate(info)
            (hmac).BlockUpdate(_dafny.Seq([d_325_i_]))
            out59_: _dafny.Seq
            out59_ = (hmac).GetResult()
            d_323_t__prev_ = out59_
            d_324_t__n_ = (d_324_t__n_) + (d_323_t__prev_)
            d_325_i_ = (d_325_i_) + (1)
        okm = d_324_t__n_
        if (expectedLength) < (len(okm)):
            okm = _dafny.Seq((okm)[:expectedLength:])
        return okm

    @staticmethod
    def Hkdf(digest, salt, ikm, info, L):
        okm: _dafny.Seq = _dafny.Seq({})
        if (L) == (0):
            okm = _dafny.Seq([])
            return okm
        d_326_hmac_: HMAC.HMac
        d_327_valueOrError0_: Wrappers.Result = None
        out60_: Wrappers.Result
        out60_ = HMAC.HMac.Build(digest)
        d_327_valueOrError0_ = out60_
        if not(not((d_327_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("/Users/lucmcdon/Desktop/workplace/aws-database-encryption-sdk-dynamodb-java/submodules/MaterialProviders/AwsCryptographyPrimitives/src/HKDF/HKDF.dfy(222,13): " + _dafny.string_of(d_327_valueOrError0_))
        d_326_hmac_ = (d_327_valueOrError0_).Extract()
        d_328_hashLength_: int
        d_328_hashLength_ = Digest.default__.Length(digest)
        d_329_nonEmptySalt_: _dafny.Seq = _dafny.Seq({})
        source11_ = salt
        if source11_.is_None:
            d_329_nonEmptySalt_ = StandardLibrary.default__.Fill(0, d_328_hashLength_)
        elif True:
            d_330___mcc_h0_ = source11_.value
            d_331_s_ = d_330___mcc_h0_
            d_329_nonEmptySalt_ = d_331_s_
        d_332_prk_: _dafny.Seq
        out61_: _dafny.Seq
        out61_ = HKDF.default__.Extract(d_326_hmac_, d_329_nonEmptySalt_, ikm)
        d_332_prk_ = out61_
        out62_: _dafny.Seq
        out62_ = HKDF.default__.Expand(d_326_hmac_, d_332_prk_, info, L, digest)
        okm = out62_
        return okm

