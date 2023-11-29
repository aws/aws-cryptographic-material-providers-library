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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
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
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants

# assert "software_amazon_cryptography_primitives_internaldafny" == __name__
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
        d_696_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        nw1_ = software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient()
        nw1_.ctor__(AwsCryptographyPrimitivesOperations.Config_Config())
        d_696_client_ = nw1_
        res = Wrappers.Result_Success(d_696_client_)
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
        out174_: Wrappers.Result
        out174_ = AwsCryptographyPrimitivesOperations.default__.GenerateRandomBytes((self).config, input)
        output = out174_
        return output

    def Digest(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out175_: Wrappers.Result
        out175_ = AwsCryptographyPrimitivesOperations.default__.Digest((self).config, input)
        output = out175_
        return output

    def HMac(self, input):
        return AwsCryptographyPrimitivesOperations.default__.HMac((self).config, input)

    def HkdfExtract(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out176_: Wrappers.Result
        out176_ = AwsCryptographyPrimitivesOperations.default__.HkdfExtract((self).config, input)
        output = out176_
        return output

    def HkdfExpand(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out177_: Wrappers.Result
        out177_ = AwsCryptographyPrimitivesOperations.default__.HkdfExpand((self).config, input)
        output = out177_
        return output

    def Hkdf(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out178_: Wrappers.Result
        out178_ = AwsCryptographyPrimitivesOperations.default__.Hkdf((self).config, input)
        output = out178_
        return output

    def KdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out179_: Wrappers.Result
        out179_ = AwsCryptographyPrimitivesOperations.default__.KdfCounterMode((self).config, input)
        output = out179_
        return output

    def AesKdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out180_: Wrappers.Result
        out180_ = AwsCryptographyPrimitivesOperations.default__.AesKdfCounterMode((self).config, input)
        output = out180_
        return output

    def AESEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out181_: Wrappers.Result
        out181_ = AwsCryptographyPrimitivesOperations.default__.AESEncrypt((self).config, input)
        output = out181_
        return output

    def AESDecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out182_: Wrappers.Result
        out182_ = AwsCryptographyPrimitivesOperations.default__.AESDecrypt((self).config, input)
        output = out182_
        return output

    def GenerateRSAKeyPair(self, input):
        output: Wrappers.Result = None
        out183_: Wrappers.Result
        out183_ = AwsCryptographyPrimitivesOperations.default__.GenerateRSAKeyPair((self).config, input)
        output = out183_
        return output

    def GetRSAKeyModulusLength(self, input):
        return AwsCryptographyPrimitivesOperations.default__.GetRSAKeyModulusLength((self).config, input)

    def RSADecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out184_: Wrappers.Result
        out184_ = AwsCryptographyPrimitivesOperations.default__.RSADecrypt((self).config, input)
        output = out184_
        return output

    def RSAEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out185_: Wrappers.Result
        out185_ = AwsCryptographyPrimitivesOperations.default__.RSAEncrypt((self).config, input)
        output = out185_
        return output

    def GenerateECDSASignatureKey(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out186_: Wrappers.Result
        out186_ = AwsCryptographyPrimitivesOperations.default__.GenerateECDSASignatureKey((self).config, input)
        output = out186_
        return output

    def ECDSASign(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out187_: Wrappers.Result
        out187_ = AwsCryptographyPrimitivesOperations.default__.ECDSASign((self).config, input)
        output = out187_
        return output

    def ECDSAVerify(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        out188_: Wrappers.Result
        out188_ = AwsCryptographyPrimitivesOperations.default__.ECDSAVerify((self).config, input)
        output = out188_
        return output

    @property
    def config(self):
        return self._config
