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
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
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

# Module: software_amazon_cryptography_materialproviders_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultMaterialProvidersConfig():
        return software_amazon_cryptography_materialproviders_internaldafny_types.MaterialProvidersConfig_MaterialProvidersConfig()

    @staticmethod
    def MaterialProviders(config):
        res: Wrappers.Result = None
        d_1229_maybeCrypto_: Wrappers.Result
        out238_: Wrappers.Result
        out238_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1229_maybeCrypto_ = out238_
        d_1230_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1231_valueOrError0_: Wrappers.Result = None
        def lambda81_(d_1232_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1232_e_)

        d_1231_valueOrError0_ = (d_1229_maybeCrypto_).MapFailure(lambda81_)
        if (d_1231_valueOrError0_).IsFailure():
            res = (d_1231_valueOrError0_).PropagateFailure()
            return res
        d_1230_crypto_ = (d_1231_valueOrError0_).Extract()
        d_1233_client_: MaterialProvidersClient
        nw72_ = MaterialProvidersClient()
        nw72_.ctor__(AwsCryptographyMaterialProvidersOperations.Config_Config(d_1230_crypto_))
        d_1233_client_ = nw72_
        res = Wrappers.Result_Success(d_1233_client_)
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
        out239_: Wrappers.Result
        out239_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsKeyring((self).config, input)
        output = out239_
        return output

    def CreateAwsKmsDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out240_: Wrappers.Result
        out240_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryKeyring((self).config, input)
        output = out240_
        return output

    def CreateAwsKmsMultiKeyring(self, input):
        output: Wrappers.Result = None
        out241_: Wrappers.Result
        out241_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMultiKeyring((self).config, input)
        output = out241_
        return output

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out242_: Wrappers.Result
        out242_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsDiscoveryMultiKeyring((self).config, input)
        output = out242_
        return output

    def CreateAwsKmsMrkKeyring(self, input):
        output: Wrappers.Result = None
        out243_: Wrappers.Result
        out243_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkKeyring((self).config, input)
        output = out243_
        return output

    def CreateAwsKmsMrkMultiKeyring(self, input):
        output: Wrappers.Result = None
        out244_: Wrappers.Result
        out244_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkMultiKeyring((self).config, input)
        output = out244_
        return output

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        output: Wrappers.Result = None
        out245_: Wrappers.Result
        out245_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryKeyring((self).config, input)
        output = out245_
        return output

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        output: Wrappers.Result = None
        out246_: Wrappers.Result
        out246_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsMrkDiscoveryMultiKeyring((self).config, input)
        output = out246_
        return output

    def CreateAwsKmsHierarchicalKeyring(self, input):
        output: Wrappers.Result = None
        out247_: Wrappers.Result
        out247_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsHierarchicalKeyring((self).config, input)
        output = out247_
        return output

    def CreateMultiKeyring(self, input):
        output: Wrappers.Result = None
        out248_: Wrappers.Result
        out248_ = AwsCryptographyMaterialProvidersOperations.default__.CreateMultiKeyring((self).config, input)
        output = out248_
        return output

    def CreateRawAesKeyring(self, input):
        output: Wrappers.Result = None
        out249_: Wrappers.Result
        out249_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawAesKeyring((self).config, input)
        output = out249_
        return output

    def CreateRawRsaKeyring(self, input):
        output: Wrappers.Result = None
        out250_: Wrappers.Result
        out250_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRawRsaKeyring((self).config, input)
        output = out250_
        return output

    def CreateAwsKmsRsaKeyring(self, input):
        output: Wrappers.Result = None
        out251_: Wrappers.Result
        out251_ = AwsCryptographyMaterialProvidersOperations.default__.CreateAwsKmsRsaKeyring((self).config, input)
        output = out251_
        return output

    def CreateDefaultCryptographicMaterialsManager(self, input):
        output: Wrappers.Result = None
        out252_: Wrappers.Result
        out252_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultCryptographicMaterialsManager((self).config, input)
        output = out252_
        return output

    def CreateRequiredEncryptionContextCMM(self, input):
        output: Wrappers.Result = None
        out253_: Wrappers.Result
        out253_ = AwsCryptographyMaterialProvidersOperations.default__.CreateRequiredEncryptionContextCMM((self).config, input)
        output = out253_
        return output

    def CreateCryptographicMaterialsCache(self, input):
        output: Wrappers.Result = None
        out254_: Wrappers.Result
        out254_ = AwsCryptographyMaterialProvidersOperations.default__.CreateCryptographicMaterialsCache((self).config, input)
        output = out254_
        return output

    def CreateDefaultClientSupplier(self, input):
        output: Wrappers.Result = None
        out255_: Wrappers.Result
        out255_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier((self).config, input)
        output = out255_
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
