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
import RSAEncryption
import AwsCryptographyPrimitivesOperations

# Module: software_amazon_cryptography_primitives_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultCryptoConfig():
        return software_amazon_cryptography_primitives_internaldafny_types.CryptoConfig_CryptoConfig()

    @staticmethod
    def AtomicPrimitives(config):
        res: Wrappers.Result = None
        d_309_client_: AtomicPrimitivesClient
        nw0_ = AtomicPrimitivesClient()
        nw0_.ctor__(AwsCryptographyPrimitivesOperations.Config_Config())
        d_309_client_ = nw0_
        res = Wrappers.Result_Success(d_309_client_)
        return res
        return res


class AtomicPrimitivesClient(software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient):
    def  __init__(self):
        self._config: AwsCryptographyPrimitivesOperations.Config = AwsCryptographyPrimitivesOperations.Config.default()()
        pass

    def __dafnystr__(self) -> str:
        return "Aws.Cryptography.Primitives.AtomicPrimitivesClient"
    def ctor__(self, config):
        (self)._config = config

    def GenerateRandomBytes(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out53_: Wrappers.Result
        out53_ = AwsCryptographyPrimitivesOperations.default__.GenerateRandomBytes((self).config, input)
        output = out53_
        return output

    def Digest(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out54_: Wrappers.Result
        out54_ = AwsCryptographyPrimitivesOperations.default__.Digest((self).config, input)
        output = out54_
        return output

    def HMac(self, input):
        return AwsCryptographyPrimitivesOperations.default__.HMac((self).config, input)

    def HkdfExtract(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out55_: Wrappers.Result
        out55_ = AwsCryptographyPrimitivesOperations.default__.HkdfExtract((self).config, input)
        output = out55_
        return output

    def HkdfExpand(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out56_: Wrappers.Result
        out56_ = AwsCryptographyPrimitivesOperations.default__.HkdfExpand((self).config, input)
        output = out56_
        return output

    def Hkdf(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out57_: Wrappers.Result
        out57_ = AwsCryptographyPrimitivesOperations.default__.Hkdf((self).config, input)
        output = out57_
        return output

    def KdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out58_: Wrappers.Result
        out58_ = AwsCryptographyPrimitivesOperations.default__.KdfCounterMode((self).config, input)
        output = out58_
        return output

    def AesKdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out59_: Wrappers.Result
        out59_ = AwsCryptographyPrimitivesOperations.default__.AesKdfCounterMode((self).config, input)
        output = out59_
        return output

    def AESEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out60_: Wrappers.Result
        out60_ = AwsCryptographyPrimitivesOperations.default__.AESEncrypt((self).config, input)
        output = out60_
        return output

    def AESDecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out61_: Wrappers.Result
        out61_ = AwsCryptographyPrimitivesOperations.default__.AESDecrypt((self).config, input)
        output = out61_
        return output

    def GenerateRSAKeyPair(self, input):
        output: Wrappers.Result = None
        out62_: Wrappers.Result
        out62_ = AwsCryptographyPrimitivesOperations.default__.GenerateRSAKeyPair((self).config, input)
        output = out62_
        return output

    def GetRSAKeyModulusLength(self, input):
        return AwsCryptographyPrimitivesOperations.default__.GetRSAKeyModulusLength((self).config, input)

    def RSADecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out63_: Wrappers.Result
        out63_ = AwsCryptographyPrimitivesOperations.default__.RSADecrypt((self).config, input)
        output = out63_
        return output

    def RSAEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out64_: Wrappers.Result
        out64_ = AwsCryptographyPrimitivesOperations.default__.RSAEncrypt((self).config, input)
        output = out64_
        return output

    def GenerateECDSASignatureKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out65_: Wrappers.Result
        out65_ = AwsCryptographyPrimitivesOperations.default__.GenerateECDSASignatureKey((self).config, input)
        output = out65_
        return output

    def ECDSASign(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out66_: Wrappers.Result
        out66_ = AwsCryptographyPrimitivesOperations.default__.ECDSASign((self).config, input)
        output = out66_
        return output

    def ECDSAVerify(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out67_: Wrappers.Result
        out67_ = AwsCryptographyPrimitivesOperations.default__.ECDSAVerify((self).config, input)
        output = out67_
        return output

    @property
    def config(self):
        return self._config
