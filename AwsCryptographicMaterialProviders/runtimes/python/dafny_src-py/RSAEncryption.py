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
import KdfCtr

assert "RSAEncryption" == __name__
RSAEncryption = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateKeyPair(lengthBits):
        publicKey: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey = None
        privateKey: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey = None
        d_380_pemPublic_: _dafny.Seq
        d_381_pemPrivate_: _dafny.Seq
        out72_: _dafny.Seq
        out73_: _dafny.Seq
        out72_, out73_ = RSAEncryption.RSA.GenerateKeyPairExtern(lengthBits)
        d_380_pemPublic_ = out72_
        d_381_pemPrivate_ = out73_
        privateKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey_RSAPrivateKey(lengthBits, d_381_pemPrivate_)
        publicKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey_RSAPublicKey(lengthBits, d_380_pemPublic_)
        return publicKey, privateKey

    @staticmethod
    def GetRSAKeyModulusLength(publicKey):
        d_382_valueOrError0_ = RSAEncryption.RSA.GetRSAKeyModulusLengthExtern(publicKey)
        if (d_382_valueOrError0_).IsFailure():
            return (d_382_valueOrError0_).PropagateFailure()
        elif True:
            d_383_length_ = (d_382_valueOrError0_).Extract()
            d_384_valueOrError1_ = Wrappers.default__.Need(((81) <= (d_383_length_)) and ((d_383_length_) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unsupported length for RSA modulus.")))
            if (d_384_valueOrError1_).IsFailure():
                return (d_384_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_383_length_)

    @staticmethod
    def Decrypt(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_385_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_385_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).privateKey))) and ((0) < (len((input).cipherText))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_385_valueOrError0_).IsFailure():
            output = (d_385_valueOrError0_).PropagateFailure()
            return output
        out74_: Wrappers.Result
        out74_ = RSAEncryption.RSA.DecryptExtern((input).padding, (input).privateKey, (input).cipherText)
        output = out74_
        return output

    @staticmethod
    def Encrypt(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_386_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_386_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).publicKey))) and ((0) < (len((input).plaintext))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_386_valueOrError0_).IsFailure():
            output = (d_386_valueOrError0_).PropagateFailure()
            return output
        out75_: Wrappers.Result
        out75_ = RSAEncryption.RSA.EncryptExtern((input).padding, (input).publicKey, (input).plaintext)
        output = out75_
        return output

