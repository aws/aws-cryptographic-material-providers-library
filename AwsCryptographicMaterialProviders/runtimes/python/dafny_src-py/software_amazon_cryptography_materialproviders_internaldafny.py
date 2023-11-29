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
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations

assert "software_amazon_cryptography_materialproviders_internaldafny" == __name__
software_amazon_cryptography_materialproviders_internaldafny = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultMaterialProvidersConfig():
        return software_amazon_cryptography_materialproviders_internaldafny_types.MaterialProvidersConfig_MaterialProvidersConfig()

    @staticmethod
    def MaterialProviders(config):
        res: Wrappers.Result = None
        d_1416_maybeCrypto_: Wrappers.Result
        out282_: Wrappers.Result
        out282_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1416_maybeCrypto_ = out282_
        d_1417_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1418_valueOrError0_: Wrappers.Result = None
        def lambda103_(d_1419_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1419_e_)

        d_1418_valueOrError0_ = (d_1416_maybeCrypto_).MapFailure(lambda103_)
        if (d_1418_valueOrError0_).IsFailure():
            res = (d_1418_valueOrError0_).PropagateFailure()
            return res
        d_1417_crypto_ = (d_1418_valueOrError0_).Extract()
        d_1420_client_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        nw73_ = software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient()
        nw73_.ctor__(AwsCryptographyMaterialProvidersOperations.Config_Config(d_1417_crypto_))
        d_1420_client_ = nw73_
        res = Wrappers.Result_Success(d_1420_client_)
        return res
        return res


class MaterialProvidersClient(software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient):
    def  __init__(self):
        self._config: AwsCryptographyMaterialProvidersOperations.Config = None
        pass

    def __dafnystr__(self) -> str:
        return "MaterialProviders.MaterialProvidersClient"
    def ctor__(self, config):
        (self)._config = config

    def CreateAwsKmsKeyring(self, input):
        output: Wrappers.Result = None
        out283_: Wrappers.Result
        out283_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsKeyring((self).config, input)
        output = out283_
        return output

    def CreateAwsKmsDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out284_: Wrappers.Result
        out284_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryKeyring((self).config, input)
        output = out284_
        return output

    def CreateAwsKmsMultiKeyring(self, input):
        output: Wrappers.Result = None
        out285_: Wrappers.Result
        out285_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMultiKeyring((self).config, input)
        output = out285_
        return output

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out286_: Wrappers.Result
        out286_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryMultiKeyring((self).config, input)
        output = out286_
        return output

    def CreateAwsKmsMrkKeyring(self, input):
        output: Wrappers.Result = None
        out287_: Wrappers.Result
        out287_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkKeyring((self).config, input)
        output = out287_
        return output

    def CreateAwsKmsMrkMultiKeyring(self, input):
        output: Wrappers.Result = None
        out288_: Wrappers.Result
        out288_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkMultiKeyring((self).config, input)
        output = out288_
        return output

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out289_: Wrappers.Result
        out289_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryKeyring((self).config, input)
        output = out289_
        return output

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out290_: Wrappers.Result
        out290_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryMultiKeyring((self).config, input)
        output = out290_
        return output

    def CreateAwsKmsHierarchicalKeyring(self, input):
        output: Wrappers.Result = None
        out291_: Wrappers.Result
        out291_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsHierarchicalKeyring((self).config, input)
        output = out291_
        return output

    def CreateMultiKeyring(self, input):
        output: Wrappers.Result = None
        out292_: Wrappers.Result
        out292_ = AwsCryptographyMaterialProvidersOperations.default__.CreateMultiKeyring((self).config, input)
        output = out292_
        return output

    def CreateRawAesKeyring(self, input):
        output: Wrappers.Result = None
        out293_: Wrappers.Result
        out293_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawAesKeyring((self).config, input)
        output = out293_
        return output

    def CreateRawRsaKeyring(self, input):
        output: Wrappers.Result = None
        out294_: Wrappers.Result
        out294_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawRsaKeyring((self).config, input)
        output = out294_
        return output

    def CreateAwsKmsRsaKeyring(self, input):
        output: Wrappers.Result = None
        out295_: Wrappers.Result
        out295_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsRsaKeyring((self).config, input)
        output = out295_
        return output

    def CreateDefaultCryptographicMaterialsManager(self, input):
        output: Wrappers.Result = None
        out296_: Wrappers.Result
        out296_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultCryptographicMaterialsManager((self).config, input)
        output = out296_
        return output

    def CreateRequiredEncryptionContextCMM(self, input):
        output: Wrappers.Result = None
        out297_: Wrappers.Result
        out297_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRequiredEncryptionContextCMM((self).config, input)
        output = out297_
        return output

    def CreateCryptographicMaterialsCache(self, input):
        output: Wrappers.Result = None
        out298_: Wrappers.Result
        out298_ = AwsCryptographyMaterialProvidersOperations.default__.CreateCryptographicMaterialsCache((self).config, input)
        output = out298_
        return output

    def CreateDefaultClientSupplier(self, input):
        output: Wrappers.Result = None
        out299_: Wrappers.Result
        out299_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier((self).config, input)
        output = out299_
        return output

    def InitializeEncryptionMaterials(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.InitializeEncryptionMaterials((self).config, input)

    def InitializeDecryptionMaterials(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.InitializeDecryptionMaterials((self).config, input)

    def ValidEncryptionMaterialsTransition(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidEncryptionMaterialsTransition((self).config, input)

    def ValidDecryptionMaterialsTransition(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidDecryptionMaterialsTransition((self).config, input)

    def EncryptionMaterialsHasPlaintextDataKey(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.EncryptionMaterialsHasPlaintextDataKey((self).config, input)

    def DecryptionMaterialsWithPlaintextDataKey(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.DecryptionMaterialsWithPlaintextDataKey((self).config, input)

    def GetAlgorithmSuiteInfo(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.GetAlgorithmSuiteInfo((self).config, input)

    def ValidAlgorithmSuiteInfo(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidAlgorithmSuiteInfo((self).config, input)

    def ValidateCommitmentPolicyOnEncrypt(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidateCommitmentPolicyOnEncrypt((self).config, input)

    def ValidateCommitmentPolicyOnDecrypt(self, input):
        return AwsCryptographyMaterialProvidersOperations.default__.ValidateCommitmentPolicyOnDecrypt((self).config, input)

    @property
    def config(self):
        return self._config
