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
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants
import JSON_mZeroCopy_mDeserializer_mValues
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy
import JSON_mAPI
import JSON

assert "software_amazon_cryptography_primitives_internaldafny" == __name__
software_amazon_cryptography_primitives_internaldafny = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultCryptoConfig():
        return software_amazon_cryptography_primitives_internaldafny_types.CryptoConfig_CryptoConfig()

    @staticmethod
    def AtomicPrimitives(config):
        res: Wrappers.Result = None
        d_104_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        nw0_ = software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient()
        nw0_.ctor__(AwsCryptographyPrimitivesOperations.Config_Config())
        d_104_client_ = nw0_
        res = Wrappers.Result_Success(d_104_client_)
        return res
        return res


class AtomicPrimitivesClient(software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient):
    def  __init__(self):
        self._config: AwsCryptographyPrimitivesOperations.Config = AwsCryptographyPrimitivesOperations.Config_Config.default()()
        pass

    def __dafnystr__(self) -> str:
        return "Aws.Cryptography.Primitives.AtomicPrimitivesClient"
    def ctor__(self, config):
        (self)._config = config

    def GenerateRandomBytes(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out36_: Wrappers.Result
        out36_ = AwsCryptographyPrimitivesOperations.default__.GenerateRandomBytes((self).config, input)
        output = out36_
        return output

    def Digest(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out37_: Wrappers.Result
        out37_ = AwsCryptographyPrimitivesOperations.default__.Digest((self).config, input)
        output = out37_
        return output

    def HMac(self, input):
        return AwsCryptographyPrimitivesOperations.default__.HMac((self).config, input)

    def HkdfExtract(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out38_: Wrappers.Result
        out38_ = AwsCryptographyPrimitivesOperations.default__.HkdfExtract((self).config, input)
        output = out38_
        return output

    def HkdfExpand(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out39_: Wrappers.Result
        out39_ = AwsCryptographyPrimitivesOperations.default__.HkdfExpand((self).config, input)
        output = out39_
        return output

    def Hkdf(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out40_: Wrappers.Result
        out40_ = AwsCryptographyPrimitivesOperations.default__.Hkdf((self).config, input)
        output = out40_
        return output

    def KdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out41_: Wrappers.Result
        out41_ = AwsCryptographyPrimitivesOperations.default__.KdfCounterMode((self).config, input)
        output = out41_
        return output

    def AesKdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out42_: Wrappers.Result
        out42_ = AwsCryptographyPrimitivesOperations.default__.AesKdfCounterMode((self).config, input)
        output = out42_
        return output

    def AESEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out43_: Wrappers.Result
        out43_ = AwsCryptographyPrimitivesOperations.default__.AESEncrypt((self).config, input)
        output = out43_
        return output

    def AESDecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out44_: Wrappers.Result
        out44_ = AwsCryptographyPrimitivesOperations.default__.AESDecrypt((self).config, input)
        output = out44_
        return output

    def GenerateRSAKeyPair(self, input):
        output: Wrappers.Result = None
        out45_: Wrappers.Result
        out45_ = AwsCryptographyPrimitivesOperations.default__.GenerateRSAKeyPair((self).config, input)
        output = out45_
        return output

    def GetRSAKeyModulusLength(self, input):
        return AwsCryptographyPrimitivesOperations.default__.GetRSAKeyModulusLength((self).config, input)

    def RSADecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out46_: Wrappers.Result
        out46_ = AwsCryptographyPrimitivesOperations.default__.RSADecrypt((self).config, input)
        output = out46_
        return output

    def RSAEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out47_: Wrappers.Result
        out47_ = AwsCryptographyPrimitivesOperations.default__.RSAEncrypt((self).config, input)
        output = out47_
        return output

    def GenerateECDSASignatureKey(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out48_: Wrappers.Result
        out48_ = AwsCryptographyPrimitivesOperations.default__.GenerateECDSASignatureKey((self).config, input)
        output = out48_
        return output

    def ECDSASign(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out49_: Wrappers.Result
        out49_ = AwsCryptographyPrimitivesOperations.default__.ECDSASign((self).config, input)
        output = out49_
        return output

    def ECDSAVerify(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        out50_: Wrappers.Result
        out50_ = AwsCryptographyPrimitivesOperations.default__.ECDSAVerify((self).config, input)
        output = out50_
        return output

    @property
    def config(self):
        return self._config
