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

# assert "software_amazon_cryptography_materialproviders_internaldafny" == __name__
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
        d_1615_maybeCrypto_: Wrappers.Result
        out359_: Wrappers.Result
        out359_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1615_maybeCrypto_ = out359_
        d_1616_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1617_valueOrError0_: Wrappers.Result = None
        def lambda104_(d_1618_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1618_e_)

        d_1617_valueOrError0_ = (d_1615_maybeCrypto_).MapFailure(lambda104_)
        if (d_1617_valueOrError0_).IsFailure():
            res = (d_1617_valueOrError0_).PropagateFailure()
            return res
        d_1616_crypto_ = (d_1617_valueOrError0_).Extract()
        d_1619_client_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        nw73_ = software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient()
        nw73_.ctor__(AwsCryptographyMaterialProvidersOperations.Config_Config(d_1616_crypto_))
        d_1619_client_ = nw73_
        res = Wrappers.Result_Success(d_1619_client_)
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
        out360_: Wrappers.Result
        out360_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsKeyring((self).config, input)
        output = out360_
        return output

    def CreateAwsKmsDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out361_: Wrappers.Result
        out361_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryKeyring((self).config, input)
        output = out361_
        return output

    def CreateAwsKmsMultiKeyring(self, input):
        output: Wrappers.Result = None
        out362_: Wrappers.Result
        out362_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMultiKeyring((self).config, input)
        output = out362_
        return output

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out363_: Wrappers.Result
        out363_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryMultiKeyring((self).config, input)
        output = out363_
        return output

    def CreateAwsKmsMrkKeyring(self, input):
        output: Wrappers.Result = None
        out364_: Wrappers.Result
        out364_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkKeyring((self).config, input)
        output = out364_
        return output

    def CreateAwsKmsMrkMultiKeyring(self, input):
        output: Wrappers.Result = None
        out365_: Wrappers.Result
        out365_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkMultiKeyring((self).config, input)
        output = out365_
        return output

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out366_: Wrappers.Result
        out366_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryKeyring((self).config, input)
        output = out366_
        return output

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out367_: Wrappers.Result
        out367_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryMultiKeyring((self).config, input)
        output = out367_
        return output

    def CreateAwsKmsHierarchicalKeyring(self, input):
        output: Wrappers.Result = None
        out368_: Wrappers.Result
        out368_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsHierarchicalKeyring((self).config, input)
        output = out368_
        return output

    def CreateMultiKeyring(self, input):
        output: Wrappers.Result = None
        out369_: Wrappers.Result
        out369_ = AwsCryptographyMaterialProvidersOperations.default__.CreateMultiKeyring((self).config, input)
        output = out369_
        return output

    def CreateRawAesKeyring(self, input):
        output: Wrappers.Result = None
        out370_: Wrappers.Result
        out370_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawAesKeyring((self).config, input)
        output = out370_
        return output

    def CreateRawRsaKeyring(self, input):
        output: Wrappers.Result = None
        out371_: Wrappers.Result
        out371_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawRsaKeyring((self).config, input)
        output = out371_
        return output

    def CreateAwsKmsRsaKeyring(self, input):
        output: Wrappers.Result = None
        out372_: Wrappers.Result
        out372_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsRsaKeyring((self).config, input)
        output = out372_
        return output

    def CreateDefaultCryptographicMaterialsManager(self, input):
        output: Wrappers.Result = None
        out373_: Wrappers.Result
        out373_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultCryptographicMaterialsManager((self).config, input)
        output = out373_
        return output

    def CreateRequiredEncryptionContextCMM(self, input):
        output: Wrappers.Result = None
        out374_: Wrappers.Result
        out374_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRequiredEncryptionContextCMM((self).config, input)
        output = out374_
        return output

    def CreateCryptographicMaterialsCache(self, input):
        output: Wrappers.Result = None
        out375_: Wrappers.Result
        out375_ = AwsCryptographyMaterialProvidersOperations.default__.CreateCryptographicMaterialsCache((self).config, input)
        output = out375_
        return output

    def CreateDefaultClientSupplier(self, input):
        output: Wrappers.Result = None
        out376_: Wrappers.Result
        out376_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier((self).config, input)
        output = out376_
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
