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
import StandardLibraryInterop
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
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_primitives_internaldafny_types
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
        d_100_pemPublic_: _dafny.Seq
        d_101_pemPrivate_: _dafny.Seq
        out18_: _dafny.Seq
        out19_: _dafny.Seq
        out18_, out19_ = RSA.GenerateKeyPairExtern(lengthBits)
        d_100_pemPublic_ = out18_
        d_101_pemPrivate_ = out19_
        privateKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey_RSAPrivateKey(lengthBits, d_101_pemPrivate_)
        publicKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey_RSAPublicKey(lengthBits, d_100_pemPublic_)
        return publicKey, privateKey

    @staticmethod
    def GetRSAKeyModulusLength(publicKey):
        d_102_valueOrError0_ = RSA_GetRSAKeyModulusLengthExtern(publicKey)
        if (d_102_valueOrError0_).IsFailure():
            return (d_102_valueOrError0_).PropagateFailure()
        elif True:
            d_103_length_ = (d_102_valueOrError0_).Extract()
            d_104_valueOrError1_ = Wrappers.default__.Need(((81) <= (d_103_length_)) and ((d_103_length_) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unsupported length for RSA modulus.")))
            if (d_104_valueOrError1_).IsFailure():
                return (d_104_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_103_length_)

    @staticmethod
    def Decrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_105_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_105_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).privateKey))) and ((0) < (len((input).cipherText))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_105_valueOrError0_).IsFailure():
            output = (d_105_valueOrError0_).PropagateFailure()
            return output
        out20_: Wrappers.Result
        out20_ = RSA.DecryptExtern((input).padding, (input).privateKey, (input).cipherText)
        output = out20_
        return output

    @staticmethod
    def Encrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_106_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_106_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).publicKey))) and ((0) < (len((input).plaintext))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_106_valueOrError0_).IsFailure():
            output = (d_106_valueOrError0_).PropagateFailure()
            return output
        out21_: Wrappers.Result
        out21_ = RSA.EncryptExtern((input).padding, (input).publicKey, (input).plaintext)
        output = out21_
        return output

    @staticmethod
    def CreateGetRSAKeyModulusLengthExternSuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateGetRSAKeyModulusLengthExternFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateBytesSuccess(bytes):
        return Wrappers.Result_Success(bytes)

    @staticmethod
    def CreateBytesFailure(error):
        return Wrappers.Result_Failure(error)

