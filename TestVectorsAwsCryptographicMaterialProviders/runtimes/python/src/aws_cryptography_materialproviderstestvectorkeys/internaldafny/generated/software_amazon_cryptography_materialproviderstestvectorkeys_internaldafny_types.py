import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
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
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
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
import software_amazon_cryptography_materialproviders_internaldafny
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import AesKdfCtr
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
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import MplManifestOptions
import AllAlgorithmSuites
import software_amazon_cryptography_materialproviders_internaldafny_wrapped

# Module: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types


class DafnyCallEvent:
    @classmethod
    def default(cls, default_I, default_O):
        return lambda: DafnyCallEvent_DafnyCallEvent(default_I(), default_O())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DafnyCallEvent(self) -> bool:
        return isinstance(self, DafnyCallEvent_DafnyCallEvent)

class DafnyCallEvent_DafnyCallEvent(DafnyCallEvent, NamedTuple('DafnyCallEvent', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class CmmOperation:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CmmOperation_ENCRYPT(), CmmOperation_DECRYPT()]
    @classmethod
    def default(cls, ):
        return lambda: CmmOperation_ENCRYPT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENCRYPT(self) -> bool:
        return isinstance(self, CmmOperation_ENCRYPT)
    @property
    def is_DECRYPT(self) -> bool:
        return isinstance(self, CmmOperation_DECRYPT)

class CmmOperation_ENCRYPT(CmmOperation, NamedTuple('ENCRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.ENCRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CmmOperation_ENCRYPT)
    def __hash__(self) -> int:
        return super().__hash__()

class CmmOperation_DECRYPT(CmmOperation, NamedTuple('DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CmmOperation_DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyDescriptionInput:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyDescriptionInput_GetKeyDescriptionInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyDescriptionInput(self) -> bool:
        return isinstance(self, GetKeyDescriptionInput_GetKeyDescriptionInput)

class GetKeyDescriptionInput_GetKeyDescriptionInput(GetKeyDescriptionInput, NamedTuple('GetKeyDescriptionInput', [('json', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput.GetKeyDescriptionInput({_dafny.string_of(self.json)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyDescriptionInput_GetKeyDescriptionInput) and self.json == __o.json
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyDescriptionOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyDescriptionOutput_GetKeyDescriptionOutput(KeyDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyDescriptionOutput(self) -> bool:
        return isinstance(self, GetKeyDescriptionOutput_GetKeyDescriptionOutput)

class GetKeyDescriptionOutput_GetKeyDescriptionOutput(GetKeyDescriptionOutput, NamedTuple('GetKeyDescriptionOutput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput.GetKeyDescriptionOutput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyDescriptionOutput_GetKeyDescriptionOutput) and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class HierarchyKeyring:
    @classmethod
    def default(cls, ):
        return lambda: HierarchyKeyring_HierarchyKeyring(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HierarchyKeyring(self) -> bool:
        return isinstance(self, HierarchyKeyring_HierarchyKeyring)

class HierarchyKeyring_HierarchyKeyring(HierarchyKeyring, NamedTuple('HierarchyKeyring', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring.HierarchyKeyring({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HierarchyKeyring_HierarchyKeyring) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KeyDescription:
    @classmethod
    def default(cls, ):
        return lambda: KeyDescription_Kms(KMSInfo.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Kms(self) -> bool:
        return isinstance(self, KeyDescription_Kms)
    @property
    def is_KmsMrk(self) -> bool:
        return isinstance(self, KeyDescription_KmsMrk)
    @property
    def is_KmsMrkDiscovery(self) -> bool:
        return isinstance(self, KeyDescription_KmsMrkDiscovery)
    @property
    def is_RSA(self) -> bool:
        return isinstance(self, KeyDescription_RSA)
    @property
    def is_AES(self) -> bool:
        return isinstance(self, KeyDescription_AES)
    @property
    def is_Static(self) -> bool:
        return isinstance(self, KeyDescription_Static)
    @property
    def is_KmsRsa(self) -> bool:
        return isinstance(self, KeyDescription_KmsRsa)
    @property
    def is_Hierarchy(self) -> bool:
        return isinstance(self, KeyDescription_Hierarchy)
    @property
    def is_Multi(self) -> bool:
        return isinstance(self, KeyDescription_Multi)
    @property
    def is_RequiredEncryptionContext(self) -> bool:
        return isinstance(self, KeyDescription_RequiredEncryptionContext)

class KeyDescription_Kms(KeyDescription, NamedTuple('Kms', [('Kms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Kms({_dafny.string_of(self.Kms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Kms) and self.Kms == __o.Kms
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsMrk(KeyDescription, NamedTuple('KmsMrk', [('KmsMrk', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrk({_dafny.string_of(self.KmsMrk)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_KmsMrk) and self.KmsMrk == __o.KmsMrk
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsMrkDiscovery(KeyDescription, NamedTuple('KmsMrkDiscovery', [('KmsMrkDiscovery', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrkDiscovery({_dafny.string_of(self.KmsMrkDiscovery)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_KmsMrkDiscovery) and self.KmsMrkDiscovery == __o.KmsMrkDiscovery
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_RSA(KeyDescription, NamedTuple('RSA', [('RSA', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RSA({_dafny.string_of(self.RSA)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_RSA) and self.RSA == __o.RSA
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_AES(KeyDescription, NamedTuple('AES', [('AES', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.AES({_dafny.string_of(self.AES)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_AES) and self.AES == __o.AES
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Static(KeyDescription, NamedTuple('Static', [('Static', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Static({_dafny.string_of(self.Static)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Static) and self.Static == __o.Static
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsRsa(KeyDescription, NamedTuple('KmsRsa', [('KmsRsa', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsRsa({_dafny.string_of(self.KmsRsa)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_KmsRsa) and self.KmsRsa == __o.KmsRsa
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Hierarchy(KeyDescription, NamedTuple('Hierarchy', [('Hierarchy', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Hierarchy({_dafny.string_of(self.Hierarchy)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Hierarchy) and self.Hierarchy == __o.Hierarchy
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Multi(KeyDescription, NamedTuple('Multi', [('Multi', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Multi({_dafny.string_of(self.Multi)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Multi) and self.Multi == __o.Multi
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_RequiredEncryptionContext(KeyDescription, NamedTuple('RequiredEncryptionContext', [('RequiredEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RequiredEncryptionContext({_dafny.string_of(self.RequiredEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_RequiredEncryptionContext) and self.RequiredEncryptionContext == __o.RequiredEncryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class IKeyVectorsClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.IKeyVectorsClientCallHistory"

class IKeyVectorsClient:
    pass
    def CreateTestVectorKeyring(self, input):
        pass

    def CreateWrappedTestVectorKeyring(self, input):
        pass

    def CreateWrappedTestVectorCmm(self, input):
        pass


class KeyVectorsConfig:
    @classmethod
    def default(cls, ):
        return lambda: KeyVectorsConfig_KeyVectorsConfig(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyVectorsConfig(self) -> bool:
        return isinstance(self, KeyVectorsConfig_KeyVectorsConfig)

class KeyVectorsConfig_KeyVectorsConfig(KeyVectorsConfig, NamedTuple('KeyVectorsConfig', [('keyManifestPath', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig.KeyVectorsConfig({_dafny.string_of(self.keyManifestPath)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyVectorsConfig_KeyVectorsConfig) and self.keyManifestPath == __o.keyManifestPath
    def __hash__(self) -> int:
        return super().__hash__()


class KMSInfo:
    @classmethod
    def default(cls, ):
        return lambda: KMSInfo_KMSInfo(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KMSInfo(self) -> bool:
        return isinstance(self, KMSInfo_KMSInfo)

class KMSInfo_KMSInfo(KMSInfo, NamedTuple('KMSInfo', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo.KMSInfo({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KMSInfo_KMSInfo) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KmsMrkAware:
    @classmethod
    def default(cls, ):
        return lambda: KmsMrkAware_KmsMrkAware(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsMrkAware(self) -> bool:
        return isinstance(self, KmsMrkAware_KmsMrkAware)

class KmsMrkAware_KmsMrkAware(KmsMrkAware, NamedTuple('KmsMrkAware', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware.KmsMrkAware({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsMrkAware_KmsMrkAware) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KmsMrkAwareDiscovery:
    @classmethod
    def default(cls, ):
        return lambda: KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq({}), _dafny.Seq({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsMrkAwareDiscovery(self) -> bool:
        return isinstance(self, KmsMrkAwareDiscovery_KmsMrkAwareDiscovery)

class KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(KmsMrkAwareDiscovery, NamedTuple('KmsMrkAwareDiscovery', [('keyId', Any), ('defaultMrkRegion', Any), ('awsKmsDiscoveryFilter', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery.KmsMrkAwareDiscovery({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.defaultMrkRegion)}, {_dafny.string_of(self.awsKmsDiscoveryFilter)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsMrkAwareDiscovery_KmsMrkAwareDiscovery) and self.keyId == __o.keyId and self.defaultMrkRegion == __o.defaultMrkRegion and self.awsKmsDiscoveryFilter == __o.awsKmsDiscoveryFilter
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaKeyring:
    @classmethod
    def default(cls, ):
        return lambda: KmsRsaKeyring_KmsRsaKeyring(_dafny.Seq({}), software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsRsaKeyring(self) -> bool:
        return isinstance(self, KmsRsaKeyring_KmsRsaKeyring)

class KmsRsaKeyring_KmsRsaKeyring(KmsRsaKeyring, NamedTuple('KmsRsaKeyring', [('keyId', Any), ('encryptionAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring.KmsRsaKeyring({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.encryptionAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsRsaKeyring_KmsRsaKeyring) and self.keyId == __o.keyId and self.encryptionAlgorithm == __o.encryptionAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class MultiKeyring:
    @classmethod
    def default(cls, ):
        return lambda: MultiKeyring_MultiKeyring(Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MultiKeyring(self) -> bool:
        return isinstance(self, MultiKeyring_MultiKeyring)

class MultiKeyring_MultiKeyring(MultiKeyring, NamedTuple('MultiKeyring', [('generator', Any), ('childKeyrings', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring.MultiKeyring({_dafny.string_of(self.generator)}, {_dafny.string_of(self.childKeyrings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MultiKeyring_MultiKeyring) and self.generator == __o.generator and self.childKeyrings == __o.childKeyrings
    def __hash__(self) -> int:
        return super().__hash__()


class RawAES:
    @classmethod
    def default(cls, ):
        return lambda: RawAES_RawAES(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RawAES(self) -> bool:
        return isinstance(self, RawAES_RawAES)

class RawAES_RawAES(RawAES, NamedTuple('RawAES', [('keyId', Any), ('providerId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES.RawAES({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.providerId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawAES_RawAES) and self.keyId == __o.keyId and self.providerId == __o.providerId
    def __hash__(self) -> int:
        return super().__hash__()


class RawRSA:
    @classmethod
    def default(cls, ):
        return lambda: RawRSA_RawRSA(_dafny.Seq({}), _dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RawRSA(self) -> bool:
        return isinstance(self, RawRSA_RawRSA)

class RawRSA_RawRSA(RawRSA, NamedTuple('RawRSA', [('keyId', Any), ('providerId', Any), ('padding', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA.RawRSA({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.providerId)}, {_dafny.string_of(self.padding)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawRSA_RawRSA) and self.keyId == __o.keyId and self.providerId == __o.providerId and self.padding == __o.padding
    def __hash__(self) -> int:
        return super().__hash__()


class RequiredEncryptionContextCMM:
    @classmethod
    def default(cls, ):
        return lambda: RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(KeyDescription.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RequiredEncryptionContextCMM(self) -> bool:
        return isinstance(self, RequiredEncryptionContextCMM_RequiredEncryptionContextCMM)

class RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(RequiredEncryptionContextCMM, NamedTuple('RequiredEncryptionContextCMM', [('underlying', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM.RequiredEncryptionContextCMM({_dafny.string_of(self.underlying)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RequiredEncryptionContextCMM_RequiredEncryptionContextCMM) and self.underlying == __o.underlying and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class SerializeKeyDescriptionInput:
    @classmethod
    def default(cls, ):
        return lambda: SerializeKeyDescriptionInput_SerializeKeyDescriptionInput(KeyDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SerializeKeyDescriptionInput(self) -> bool:
        return isinstance(self, SerializeKeyDescriptionInput_SerializeKeyDescriptionInput)

class SerializeKeyDescriptionInput_SerializeKeyDescriptionInput(SerializeKeyDescriptionInput, NamedTuple('SerializeKeyDescriptionInput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionInput.SerializeKeyDescriptionInput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializeKeyDescriptionInput_SerializeKeyDescriptionInput) and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class SerializeKeyDescriptionOutput:
    @classmethod
    def default(cls, ):
        return lambda: SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SerializeKeyDescriptionOutput(self) -> bool:
        return isinstance(self, SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput)

class SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(SerializeKeyDescriptionOutput, NamedTuple('SerializeKeyDescriptionOutput', [('json', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput.SerializeKeyDescriptionOutput({_dafny.string_of(self.json)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput) and self.json == __o.json
    def __hash__(self) -> int:
        return super().__hash__()


class StaticKeyring:
    @classmethod
    def default(cls, ):
        return lambda: StaticKeyring_StaticKeyring(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_StaticKeyring(self) -> bool:
        return isinstance(self, StaticKeyring_StaticKeyring)

class StaticKeyring_StaticKeyring(StaticKeyring, NamedTuple('StaticKeyring', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring.StaticKeyring({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StaticKeyring_StaticKeyring) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class TestVectorCmmInput:
    @classmethod
    def default(cls, ):
        return lambda: TestVectorCmmInput_TestVectorCmmInput(KeyDescription.default()(), CmmOperation.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TestVectorCmmInput(self) -> bool:
        return isinstance(self, TestVectorCmmInput_TestVectorCmmInput)

class TestVectorCmmInput_TestVectorCmmInput(TestVectorCmmInput, NamedTuple('TestVectorCmmInput', [('keyDescription', Any), ('forOperation', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput.TestVectorCmmInput({_dafny.string_of(self.keyDescription)}, {_dafny.string_of(self.forOperation)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorCmmInput_TestVectorCmmInput) and self.keyDescription == __o.keyDescription and self.forOperation == __o.forOperation
    def __hash__(self) -> int:
        return super().__hash__()


class TestVectorKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: TestVectorKeyringInput_TestVectorKeyringInput(KeyDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TestVectorKeyringInput(self) -> bool:
        return isinstance(self, TestVectorKeyringInput_TestVectorKeyringInput)

class TestVectorKeyringInput_TestVectorKeyringInput(TestVectorKeyringInput, NamedTuple('TestVectorKeyringInput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorKeyringInput.TestVectorKeyringInput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorKeyringInput_TestVectorKeyringInput) and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_KeyVectorException(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyVectorException(self) -> bool:
        return isinstance(self, Error_KeyVectorException)
    @property
    def is_AwsCryptographyMaterialProviders(self) -> bool:
        return isinstance(self, Error_AwsCryptographyMaterialProviders)
    @property
    def is_ComAmazonawsKms(self) -> bool:
        return isinstance(self, Error_ComAmazonawsKms)
    @property
    def is_CollectionOfErrors(self) -> bool:
        return isinstance(self, Error_CollectionOfErrors)
    @property
    def is_Opaque(self) -> bool:
        return isinstance(self, Error_Opaque)

class Error_KeyVectorException(Error, NamedTuple('KeyVectorException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.KeyVectorException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KeyVectorException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_AwsCryptographyMaterialProviders(Error, NamedTuple('AwsCryptographyMaterialProviders', [('AwsCryptographyMaterialProviders', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.AwsCryptographyMaterialProviders({_dafny.string_of(self.AwsCryptographyMaterialProviders)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_AwsCryptographyMaterialProviders) and self.AwsCryptographyMaterialProviders == __o.AwsCryptographyMaterialProviders
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsKms(Error, NamedTuple('ComAmazonawsKms', [('ComAmazonawsKms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.ComAmazonawsKms({_dafny.string_of(self.ComAmazonawsKms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ComAmazonawsKms) and self.ComAmazonawsKms == __o.ComAmazonawsKms
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CollectionOfErrors(Error, NamedTuple('CollectionOfErrors', [('list', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.CollectionOfErrors({_dafny.string_of(self.list)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CollectionOfErrors) and self.list == __o.list and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.Opaque({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Error.default()()
