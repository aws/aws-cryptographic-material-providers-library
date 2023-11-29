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
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants

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
        d_497_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        nw1_ = software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient()
        nw1_.ctor__(AwsCryptographyPrimitivesOperations.Config_Config())
        d_497_client_ = nw1_
        res = Wrappers.Result_Success(d_497_client_)
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
        out97_: Wrappers.Result
        out97_ = AwsCryptographyPrimitivesOperations.default__.GenerateRandomBytes((self).config, input)
        output = out97_
        return output

    def Digest(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out98_: Wrappers.Result
        out98_ = AwsCryptographyPrimitivesOperations.default__.Digest((self).config, input)
        output = out98_
        return output

    def HMac(self, input):
        return AwsCryptographyPrimitivesOperations.default__.HMac((self).config, input)

    def HkdfExtract(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out99_: Wrappers.Result
        out99_ = AwsCryptographyPrimitivesOperations.default__.HkdfExtract((self).config, input)
        output = out99_
        return output

    def HkdfExpand(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out100_: Wrappers.Result
        out100_ = AwsCryptographyPrimitivesOperations.default__.HkdfExpand((self).config, input)
        output = out100_
        return output

    def Hkdf(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out101_: Wrappers.Result
        out101_ = AwsCryptographyPrimitivesOperations.default__.Hkdf((self).config, input)
        output = out101_
        return output

    def KdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out102_: Wrappers.Result
        out102_ = AwsCryptographyPrimitivesOperations.default__.KdfCounterMode((self).config, input)
        output = out102_
        return output

    def AesKdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out103_: Wrappers.Result
        out103_ = AwsCryptographyPrimitivesOperations.default__.AesKdfCounterMode((self).config, input)
        output = out103_
        return output

    def AESEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out104_: Wrappers.Result
        out104_ = AwsCryptographyPrimitivesOperations.default__.AESEncrypt((self).config, input)
        output = out104_
        return output

    def AESDecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out105_: Wrappers.Result
        out105_ = AwsCryptographyPrimitivesOperations.default__.AESDecrypt((self).config, input)
        output = out105_
        return output

    def GenerateRSAKeyPair(self, input):
        output: Wrappers.Result = None
        out106_: Wrappers.Result
        out106_ = AwsCryptographyPrimitivesOperations.default__.GenerateRSAKeyPair((self).config, input)
        output = out106_
        return output

    def GetRSAKeyModulusLength(self, input):
        return AwsCryptographyPrimitivesOperations.default__.GetRSAKeyModulusLength((self).config, input)

    def RSADecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out107_: Wrappers.Result
        out107_ = AwsCryptographyPrimitivesOperations.default__.RSADecrypt((self).config, input)
        output = out107_
        return output

    def RSAEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out108_: Wrappers.Result
        out108_ = AwsCryptographyPrimitivesOperations.default__.RSAEncrypt((self).config, input)
        output = out108_
        return output

    def GenerateECDSASignatureKey(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out109_: Wrappers.Result
        out109_ = AwsCryptographyPrimitivesOperations.default__.GenerateECDSASignatureKey((self).config, input)
        output = out109_
        return output

    def ECDSASign(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out110_: Wrappers.Result
        out110_ = AwsCryptographyPrimitivesOperations.default__.ECDSASign((self).config, input)
        output = out110_
        return output

    def ECDSAVerify(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        out111_: Wrappers.Result
        out111_ = AwsCryptographyPrimitivesOperations.default__.ECDSAVerify((self).config, input)
        output = out111_
        return output

    @property
    def config(self):
        return self._config
