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
import DafnyLibraries
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
        d_93_pemPublic_: _dafny.Seq
        d_94_pemPrivate_: _dafny.Seq
        out18_: _dafny.Seq
        out19_: _dafny.Seq
        out18_, out19_ = RSA.GenerateKeyPairExtern(lengthBits)
        d_93_pemPublic_ = out18_
        d_94_pemPrivate_ = out19_
        privateKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey_RSAPrivateKey(lengthBits, d_94_pemPrivate_)
        publicKey = software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey_RSAPublicKey(lengthBits, d_93_pemPublic_)
        return publicKey, privateKey

    @staticmethod
    def GetRSAKeyModulusLength(publicKey):
        d_95_valueOrError0_ = RSA_GetRSAKeyModulusLengthExtern(publicKey)
        if (d_95_valueOrError0_).IsFailure():
            return (d_95_valueOrError0_).PropagateFailure()
        elif True:
            d_96_length_ = (d_95_valueOrError0_).Extract()
            d_97_valueOrError1_ = Wrappers.default__.Need(((81) <= (d_96_length_)) and ((d_96_length_) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unsupported length for RSA modulus.")))
            if (d_97_valueOrError1_).IsFailure():
                return (d_97_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_96_length_)

    @staticmethod
    def Decrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_98_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_98_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).privateKey))) and ((0) < (len((input).cipherText))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_98_valueOrError0_).IsFailure():
            output = (d_98_valueOrError0_).PropagateFailure()
            return output
        out20_: Wrappers.Result
        out20_ = RSA.DecryptExtern((input).padding, (input).privateKey, (input).cipherText)
        output = out20_
        return output

    @staticmethod
    def Encrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_99_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_99_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).publicKey))) and ((0) < (len((input).plaintext))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_99_valueOrError0_).IsFailure():
            output = (d_99_valueOrError0_).PropagateFailure()
            return output
        out21_: Wrappers.Result
        out21_ = RSA.EncryptExtern((input).padding, (input).publicKey, (input).plaintext)
        output = out21_
        return output

