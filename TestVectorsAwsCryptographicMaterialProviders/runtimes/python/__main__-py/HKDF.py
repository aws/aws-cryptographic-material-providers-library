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

# Module: HKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(hmac, salt, ikm):
        prk: _dafny.Seq = _dafny.Seq({})
        (hmac).Init(salt)
        (hmac).BlockUpdate(ikm)
        out21_: _dafny.Seq
        out21_ = (hmac).GetResult()
        prk = out21_
        prk = prk
        return prk
        return prk

    @staticmethod
    def Expand(hmac, prk, info, expectedLength, digest):
        okm: _dafny.Seq = _dafny.Seq({})
        d_239_hashLength_: int
        d_239_hashLength_ = Digest.default__.Length(digest)
        d_240_n_: int
        d_240_n_ = _dafny.euclidian_division(((d_239_hashLength_) + (expectedLength)) - (1), d_239_hashLength_)
        (hmac).Init(prk)
        d_241_t__prev_: _dafny.Seq
        d_241_t__prev_ = _dafny.Seq([])
        d_242_t__n_: _dafny.Seq
        d_242_t__n_ = d_241_t__prev_
        d_243_i_: int
        d_243_i_ = 1
        while (d_243_i_) <= (d_240_n_):
            (hmac).BlockUpdate(d_241_t__prev_)
            (hmac).BlockUpdate(info)
            (hmac).BlockUpdate(_dafny.Seq([d_243_i_]))
            out22_: _dafny.Seq
            out22_ = (hmac).GetResult()
            d_241_t__prev_ = out22_
            d_242_t__n_ = (d_242_t__n_) + (d_241_t__prev_)
            d_243_i_ = (d_243_i_) + (1)
        okm = d_242_t__n_
        if (expectedLength) < (len(okm)):
            okm = _dafny.Seq((okm)[:expectedLength:])
        return okm

    @staticmethod
    def Hkdf(digest, salt, ikm, info, L):
        okm: _dafny.Seq = _dafny.Seq({})
        if (L) == (0):
            okm = _dafny.Seq([])
            return okm
        d_244_hmac_: HMAC.HMac
        d_245_valueOrError0_: Wrappers.Result = None
        out23_: Wrappers.Result
        out23_ = HMAC.HMac.Build(digest)
        d_245_valueOrError0_ = out23_
        if not(not((d_245_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("/Users/lucmcdon/Desktop/workplace/aws-database-encryption-sdk-dynamodb-java/submodules/MaterialProviders/AwsCryptographyPrimitives/src/HKDF/HKDF.dfy(222,13): " + _dafny.string_of(d_245_valueOrError0_))
        d_244_hmac_ = (d_245_valueOrError0_).Extract()
        d_246_hashLength_: int
        d_246_hashLength_ = Digest.default__.Length(digest)
        d_247_nonEmptySalt_: _dafny.Seq = _dafny.Seq({})
        source18_ = salt
        if source18_.is_None:
            d_247_nonEmptySalt_ = StandardLibrary.default__.Fill(0, d_246_hashLength_)
        elif True:
            d_248___mcc_h0_ = source18_.value
            d_249_s_ = d_248___mcc_h0_
            d_247_nonEmptySalt_ = d_249_s_
        d_250_prk_: _dafny.Seq
        out24_: _dafny.Seq
        out24_ = default__.Extract(d_244_hmac_, d_247_nonEmptySalt_, ikm)
        d_250_prk_ = out24_
        out25_: _dafny.Seq
        out25_ = default__.Expand(d_244_hmac_, d_250_prk_, info, L, digest)
        okm = out25_
        return okm

