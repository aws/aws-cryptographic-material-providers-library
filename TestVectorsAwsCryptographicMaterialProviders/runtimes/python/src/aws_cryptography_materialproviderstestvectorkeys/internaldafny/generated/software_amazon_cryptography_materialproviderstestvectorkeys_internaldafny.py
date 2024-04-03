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
import CreateStaticKeyStores
import KeyringFromKeyDescription
import CmmFromKeyDescription
import KeysVectorOperations

# Module: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultKeyVectorsConfig():
        return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyVectorsConfig_KeyVectorsConfig(_dafny.Seq(""))

    @staticmethod
    def KeyVectors(config):
        res: Wrappers.Result = None
        d_515_keysManifestBv_: _dafny.Seq
        d_516_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out46_: Wrappers.Result
        out46_ = FileIO.default__.ReadBytesFromFile((config).keyManifestPath)
        d_516_valueOrError0_ = out46_
        if not(not((d_516_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/KeyVectors/src/Index.dfy(30,26): " + _dafny.string_of(d_516_valueOrError0_))
        d_515_keysManifestBv_ = (d_516_valueOrError0_).Extract()
        d_517_keysManifestBytes_: _dafny.Seq
        d_517_keysManifestBytes_ = JSONHelpers.default__.BvToBytes(d_515_keysManifestBv_)
        d_518_keysManifestJSON_: JSON_Values.JSON
        d_519_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
        def lambda49_(d_520_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException((d_520_e_).ToString())

        d_519_valueOrError1_ = (JSON_API.default__.Deserialize(d_517_keysManifestBytes_)).MapFailure(lambda49_)
        if (d_519_valueOrError1_).IsFailure():
            res = (d_519_valueOrError1_).PropagateFailure()
            return res
        d_518_keysManifestJSON_ = (d_519_valueOrError1_).Extract()
        if not((d_518_keysManifestJSON_).is_Object):
            raise _dafny.HaltException("dafny/KeyVectors/src/Index.dfy(36,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_521_keysObject_: JSON_Values.JSON
        d_522_valueOrError2_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
        d_522_valueOrError2_ = JSONHelpers.default__.Get(_dafny.Seq("keys"), (d_518_keysManifestJSON_).obj)
        if not(not((d_522_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/KeyVectors/src/Index.dfy(37,22): " + _dafny.string_of(d_522_valueOrError2_))
        d_521_keysObject_ = (d_522_valueOrError2_).Extract()
        if not((d_521_keysObject_).is_Object):
            raise _dafny.HaltException("dafny/KeyVectors/src/Index.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_523_maybeMpl_: Wrappers.Result
        out47_: Wrappers.Result
        out47_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_523_maybeMpl_ = out47_
        d_524_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_525_valueOrError3_: Wrappers.Result = None
        def lambda50_(d_526_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_526_e_)

        d_525_valueOrError3_ = (d_523_maybeMpl_).MapFailure(lambda50_)
        if (d_525_valueOrError3_).IsFailure():
            res = (d_525_valueOrError3_).PropagateFailure()
            return res
        d_524_mpl_ = (d_525_valueOrError3_).Extract()
        d_527_keys_: _dafny.Map
        d_528_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        def lambda51_(d_529_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_529_e_)

        d_528_valueOrError4_ = (KeyMaterial.default__.BuildKeyMaterials(d_524_mpl_, (d_521_keysObject_).obj)).MapFailure(lambda51_)
        if (d_528_valueOrError4_).IsFailure():
            res = (d_528_valueOrError4_).PropagateFailure()
            return res
        d_527_keys_ = (d_528_valueOrError4_).Extract()
        d_530_config_: KeysVectorOperations.Config
        d_530_config_ = KeysVectorOperations.Config_Config(d_527_keys_, d_518_keysManifestJSON_)
        d_531_client_: KeyVectorsClient
        nw2_ = KeyVectorsClient()
        nw2_.ctor__(d_530_config_)
        d_531_client_ = nw2_
        res = Wrappers.Result_Success(d_531_client_)
        return res

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class KeyVectorsClient(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.IKeyVectorsClient):
    def  __init__(self):
        self._config: KeysVectorOperations.Config = KeysVectorOperations.Config.default()()
        pass

    def __dafnystr__(self) -> str:
        return "KeyVectors.KeyVectorsClient"
    def ctor__(self, config):
        (self)._config = config

    def CreateTestVectorKeyring(self, input):
        output: Wrappers.Result = None
        out48_: Wrappers.Result
        out48_ = KeysVectorOperations.default__.CreateTestVectorKeyring((self).config, input)
        output = out48_
        return output

    def CreateWrappedTestVectorKeyring(self, input):
        output: Wrappers.Result = None
        out49_: Wrappers.Result
        out49_ = KeysVectorOperations.default__.CreateWrappedTestVectorKeyring((self).config, input)
        output = out49_
        return output

    def CreateWrappedTestVectorCmm(self, input):
        output: Wrappers.Result = None
        out50_: Wrappers.Result
        out50_ = KeysVectorOperations.default__.CreateWrappedTestVectorCmm((self).config, input)
        output = out50_
        return output

    def GetKeyDescription(self, input):
        return KeysVectorOperations.default__.GetKeyDescription((self).config, input)

    def SerializeKeyDescription(self, input):
        return KeysVectorOperations.default__.SerializeKeyDescription((self).config, input)

    @property
    def config(self):
        return self._config
