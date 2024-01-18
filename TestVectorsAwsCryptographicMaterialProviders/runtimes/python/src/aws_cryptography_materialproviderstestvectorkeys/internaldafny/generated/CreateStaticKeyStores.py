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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
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
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings

# Module: CreateStaticKeyStores

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateStaticKeyStore(staticKeyMaterial):
        keyStore: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient = None
        nw1_ = StaticKeyStore()
        nw1_.ctor__(staticKeyMaterial)
        keyStore = nw1_
        return keyStore
        return keyStore


class StaticKeyStore(software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient):
    def  __init__(self):
        self._staticKeyMaterial: KeyMaterial.KeyMaterial = KeyMaterial.KeyMaterial.default()()
        pass

    def __dafnystr__(self) -> str:
        return "CreateStaticKeyStores.StaticKeyStore"
    def ctor__(self, staticKeyMaterial):
        (self)._staticKeyMaterial = staticKeyMaterial

    def GetActiveBranchKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials_BranchKeyMaterials((input).branchKeyIdentifier, ((self).staticKeyMaterial).branchKeyVersion, _dafny.Map({}), ((self).staticKeyMaterial).branchKey)))
        return output

    def GetBranchKeyVersion(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials_BranchKeyMaterials((input).branchKeyIdentifier, ((self).staticKeyMaterial).branchKeyVersion, _dafny.Map({}), ((self).staticKeyMaterial).branchKey)))
        return output

    def GetBeaconKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput_GetBeaconKeyOutput(software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials_BeaconKeyMaterials((input).branchKeyIdentifier, _dafny.Map({}), Wrappers.Option_Some(((self).staticKeyMaterial).beaconKey), Wrappers.Option_None())))
        return output

    def GetKeyStoreInfo(self):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Not Supported")))
        return output

    def CreateKeyStore(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput.default())()
        output = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Not Supported")))
        return output

    def CreateKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        output = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Not Supported")))
        return output

    def VersionKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        output = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Not Supported")))
        return output

    @property
    def staticKeyMaterial(self):
        return self._staticKeyMaterial
