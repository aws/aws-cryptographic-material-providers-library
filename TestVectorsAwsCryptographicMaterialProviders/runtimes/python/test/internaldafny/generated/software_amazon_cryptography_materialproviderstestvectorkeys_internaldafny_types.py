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
import Aws_mCryptography
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
import software_amazon_cryptography_materialproviders_internaldafny
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings

assert "software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types" == __name__
software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types = sys.modules[__name__]


class DafnyCallEvent:
    @classmethod
    def default(cls, default_I, default_O):
        return lambda: DafnyCallEvent_DafnyCallEvent(default_I(), default_O())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DafnyCallEvent(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.DafnyCallEvent_DafnyCallEvent)

class DafnyCallEvent_DafnyCallEvent(DafnyCallEvent, NamedTuple('DafnyCallEvent', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionInput_GetKeyDescriptionInput)

class GetKeyDescriptionInput_GetKeyDescriptionInput(GetKeyDescriptionInput, NamedTuple('GetKeyDescriptionInput', [('json', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput.GetKeyDescriptionInput({_dafny.string_of(self.json)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionInput_GetKeyDescriptionInput) and self.json == __o.json
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyDescriptionOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyDescriptionOutput_GetKeyDescriptionOutput(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyDescriptionOutput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionOutput_GetKeyDescriptionOutput)

class GetKeyDescriptionOutput_GetKeyDescriptionOutput(GetKeyDescriptionOutput, NamedTuple('GetKeyDescriptionOutput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput.GetKeyDescriptionOutput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionOutput_GetKeyDescriptionOutput) and self.keyDescription == __o.keyDescription
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.HierarchyKeyring_HierarchyKeyring)

class HierarchyKeyring_HierarchyKeyring(HierarchyKeyring, NamedTuple('HierarchyKeyring', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring.HierarchyKeyring({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.HierarchyKeyring_HierarchyKeyring) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KeyDescription:
    @classmethod
    def default(cls, ):
        return lambda: KeyDescription_Kms(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KMSInfo_KMSInfo.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Kms(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms)
    @property
    def is_KmsMrk(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrk)
    @property
    def is_KmsMrkDiscovery(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrkDiscovery)
    @property
    def is_RSA(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA)
    @property
    def is_AES(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES)
    @property
    def is_Static(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Static)
    @property
    def is_KmsRsa(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsRsa)
    @property
    def is_Hierarchy(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Hierarchy)

class KeyDescription_Kms(KeyDescription, NamedTuple('Kms', [('Kms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Kms({_dafny.string_of(self.Kms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms) and self.Kms == __o.Kms
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsMrk(KeyDescription, NamedTuple('KmsMrk', [('KmsMrk', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrk({_dafny.string_of(self.KmsMrk)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrk) and self.KmsMrk == __o.KmsMrk
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsMrkDiscovery(KeyDescription, NamedTuple('KmsMrkDiscovery', [('KmsMrkDiscovery', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrkDiscovery({_dafny.string_of(self.KmsMrkDiscovery)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrkDiscovery) and self.KmsMrkDiscovery == __o.KmsMrkDiscovery
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_RSA(KeyDescription, NamedTuple('RSA', [('RSA', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RSA({_dafny.string_of(self.RSA)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA) and self.RSA == __o.RSA
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_AES(KeyDescription, NamedTuple('AES', [('AES', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.AES({_dafny.string_of(self.AES)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES) and self.AES == __o.AES
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Static(KeyDescription, NamedTuple('Static', [('Static', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Static({_dafny.string_of(self.Static)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Static) and self.Static == __o.Static
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsRsa(KeyDescription, NamedTuple('KmsRsa', [('KmsRsa', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsRsa({_dafny.string_of(self.KmsRsa)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsRsa) and self.KmsRsa == __o.KmsRsa
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Hierarchy(KeyDescription, NamedTuple('Hierarchy', [('Hierarchy', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Hierarchy({_dafny.string_of(self.Hierarchy)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Hierarchy) and self.Hierarchy == __o.Hierarchy
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

    def CreateWappedTestVectorKeyring(self, input):
        pass


class KeyVectorsConfig:
    @classmethod
    def default(cls, ):
        return lambda: KeyVectorsConfig_KeyVectorsConfig(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyVectorsConfig(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyVectorsConfig_KeyVectorsConfig)

class KeyVectorsConfig_KeyVectorsConfig(KeyVectorsConfig, NamedTuple('KeyVectorsConfig', [('keyManifiestPath', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig.KeyVectorsConfig({_dafny.string_of(self.keyManifiestPath)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyVectorsConfig_KeyVectorsConfig) and self.keyManifiestPath == __o.keyManifiestPath
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KMSInfo_KMSInfo)

class KMSInfo_KMSInfo(KMSInfo, NamedTuple('KMSInfo', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo.KMSInfo({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KMSInfo_KMSInfo) and self.keyId == __o.keyId
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAware_KmsMrkAware)

class KmsMrkAware_KmsMrkAware(KmsMrkAware, NamedTuple('KmsMrkAware', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware.KmsMrkAware({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAware_KmsMrkAware) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KmsMrkAwareDiscovery:
    @classmethod
    def default(cls, ):
        return lambda: KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq({}), _dafny.Seq({}), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsMrkAwareDiscovery(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery)

class KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(KmsMrkAwareDiscovery, NamedTuple('KmsMrkAwareDiscovery', [('keyId', Any), ('defaultMrkRegion', Any), ('awsKmsDiscoveryFilter', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery.KmsMrkAwareDiscovery({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.defaultMrkRegion)}, {_dafny.string_of(self.awsKmsDiscoveryFilter)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery) and self.keyId == __o.keyId and self.defaultMrkRegion == __o.defaultMrkRegion and self.awsKmsDiscoveryFilter == __o.awsKmsDiscoveryFilter
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaKeyring:
    @classmethod
    def default(cls, ):
        return lambda: KmsRsaKeyring_KmsRsaKeyring(_dafny.Seq({}), software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsRsaKeyring(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsRsaKeyring_KmsRsaKeyring)

class KmsRsaKeyring_KmsRsaKeyring(KmsRsaKeyring, NamedTuple('KmsRsaKeyring', [('keyId', Any), ('encryptionAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring.KmsRsaKeyring({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.encryptionAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsRsaKeyring_KmsRsaKeyring) and self.keyId == __o.keyId and self.encryptionAlgorithm == __o.encryptionAlgorithm
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES)

class RawAES_RawAES(RawAES, NamedTuple('RawAES', [('keyId', Any), ('providerId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES.RawAES({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.providerId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES) and self.keyId == __o.keyId and self.providerId == __o.providerId
    def __hash__(self) -> int:
        return super().__hash__()


class RawRSA:
    @classmethod
    def default(cls, ):
        return lambda: RawRSA_RawRSA(_dafny.Seq({}), _dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_PKCS1.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RawRSA(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA)

class RawRSA_RawRSA(RawRSA, NamedTuple('RawRSA', [('keyId', Any), ('providerId', Any), ('padding', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA.RawRSA({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.providerId)}, {_dafny.string_of(self.padding)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA) and self.keyId == __o.keyId and self.providerId == __o.providerId and self.padding == __o.padding
    def __hash__(self) -> int:
        return super().__hash__()


class SerializeKeyDescriptionInput:
    @classmethod
    def default(cls, ):
        return lambda: SerializeKeyDescriptionInput_SerializeKeyDescriptionInput(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SerializeKeyDescriptionInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.SerializeKeyDescriptionInput_SerializeKeyDescriptionInput)

class SerializeKeyDescriptionInput_SerializeKeyDescriptionInput(SerializeKeyDescriptionInput, NamedTuple('SerializeKeyDescriptionInput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionInput.SerializeKeyDescriptionInput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.SerializeKeyDescriptionInput_SerializeKeyDescriptionInput) and self.keyDescription == __o.keyDescription
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput)

class SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(SerializeKeyDescriptionOutput, NamedTuple('SerializeKeyDescriptionOutput', [('json', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput.SerializeKeyDescriptionOutput({_dafny.string_of(self.json)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput) and self.json == __o.json
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.StaticKeyring_StaticKeyring)

class StaticKeyring_StaticKeyring(StaticKeyring, NamedTuple('StaticKeyring', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring.StaticKeyring({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.StaticKeyring_StaticKeyring) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class TestVectorKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: TestVectorKeyringInput_TestVectorKeyringInput(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TestVectorKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.TestVectorKeyringInput_TestVectorKeyringInput)

class TestVectorKeyringInput_TestVectorKeyringInput(TestVectorKeyringInput, NamedTuple('TestVectorKeyringInput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorKeyringInput.TestVectorKeyringInput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.TestVectorKeyringInput_TestVectorKeyringInput) and self.keyDescription == __o.keyDescription
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
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException)
    @property
    def is_AwsCryptographyMaterialProviders(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders)
    @property
    def is_ComAmazonawsKms(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_ComAmazonawsKms)
    @property
    def is_CollectionOfErrors(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_CollectionOfErrors)
    @property
    def is_Opaque(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_Opaque)

class Error_KeyVectorException(Error, NamedTuple('KeyVectorException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.KeyVectorException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_AwsCryptographyMaterialProviders(Error, NamedTuple('AwsCryptographyMaterialProviders', [('AwsCryptographyMaterialProviders', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.AwsCryptographyMaterialProviders({_dafny.string_of(self.AwsCryptographyMaterialProviders)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders) and self.AwsCryptographyMaterialProviders == __o.AwsCryptographyMaterialProviders
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsKms(Error, NamedTuple('ComAmazonawsKms', [('ComAmazonawsKms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.ComAmazonawsKms({_dafny.string_of(self.ComAmazonawsKms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_ComAmazonawsKms) and self.ComAmazonawsKms == __o.ComAmazonawsKms
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CollectionOfErrors(Error, NamedTuple('CollectionOfErrors', [('list', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.CollectionOfErrors({_dafny.string_of(self.list)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_CollectionOfErrors) and self.list == __o.list and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.Opaque({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_Opaque) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException.default()()
