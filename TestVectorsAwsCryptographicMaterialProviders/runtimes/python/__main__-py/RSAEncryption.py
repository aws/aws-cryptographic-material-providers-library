import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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
import WrappedHKDF
import Signature
import KdfCtr

# Module: RSAEncryption

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateKeyPair(lengthBits):
        publicKey: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey = None
        privateKey: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey = None
        d_298_pemPublic_: _dafny.Seq
        d_299_pemPrivate_: _dafny.Seq
        out35_: _dafny.Seq
        out36_: _dafny.Seq
        out35_, out36_ = RSAEncryption.RSA.GenerateKeyPairExtern(lengthBits)
        d_298_pemPublic_ = out35_
        d_299_pemPrivate_ = out36_
        privateKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey_RSAPrivateKey(lengthBits, d_299_pemPrivate_)
        publicKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey_RSAPublicKey(lengthBits, d_298_pemPublic_)
        return publicKey, privateKey

    @staticmethod
    def GetRSAKeyModulusLength(publicKey):
        d_300_valueOrError0_ = RSAEncryption.RSA_GetRSAKeyModulusLengthExtern(publicKey)
        if (d_300_valueOrError0_).IsFailure():
            return (d_300_valueOrError0_).PropagateFailure()
        elif True:
            d_301_length_ = (d_300_valueOrError0_).Extract()
            d_302_valueOrError1_ = Wrappers.default__.Need(((81) <= (d_301_length_)) and ((d_301_length_) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unsupported length for RSA modulus.")))
            if (d_302_valueOrError1_).IsFailure():
                return (d_302_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_301_length_)

    @staticmethod
    def Decrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_303_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_303_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).privateKey))) and ((0) < (len((input).cipherText))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_303_valueOrError0_).IsFailure():
            output = (d_303_valueOrError0_).PropagateFailure()
            return output
        out37_: Wrappers.Result
        out37_ = RSAEncryption.RSA.DecryptExtern((input).padding, (input).privateKey, (input).cipherText)
        output = out37_
        return output

    @staticmethod
    def Encrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_304_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_304_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).publicKey))) and ((0) < (len((input).plaintext))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_304_valueOrError0_).IsFailure():
            output = (d_304_valueOrError0_).PropagateFailure()
            return output
        out38_: Wrappers.Result
        out38_ = RSAEncryption.RSA.EncryptExtern((input).padding, (input).publicKey, (input).plaintext)
        output = out38_
        return output

