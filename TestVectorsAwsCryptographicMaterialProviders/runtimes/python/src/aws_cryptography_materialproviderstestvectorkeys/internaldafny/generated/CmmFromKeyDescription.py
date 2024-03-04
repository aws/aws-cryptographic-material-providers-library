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

# Module: CmmFromKeyDescription

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ToCmm(mpl, keys, description, forOperation):
        output: Wrappers.Result = None
        d_435_material_: Wrappers.Option
        d_435_material_ = KeyringFromKeyDescription.default__.GetKeyMaterial(keys, description)
        source15_ = description
        if source15_.is_Kms:
            d_436___mcc_h0_ = source15_.Kms
            if True:
                d_437_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_438_valueOrError1_: Wrappers.Result = None
                out20_: Wrappers.Result
                out20_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_438_valueOrError1_ = out20_
                if (d_438_valueOrError1_).IsFailure():
                    output = (d_438_valueOrError1_).PropagateFailure()
                    return output
                d_437_keyring_ = (d_438_valueOrError1_).Extract()
                d_439_output_k_: Wrappers.Result
                out21_: Wrappers.Result
                out21_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_437_keyring_))
                d_439_output_k_ = out21_
                def lambda32_(d_440_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_440_e_)

                output = (d_439_output_k_).MapFailure(lambda32_)
        elif source15_.is_KmsMrk:
            d_441___mcc_h2_ = source15_.KmsMrk
            if True:
                d_442_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_443_valueOrError1_: Wrappers.Result = None
                out22_: Wrappers.Result
                out22_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_443_valueOrError1_ = out22_
                if (d_443_valueOrError1_).IsFailure():
                    output = (d_443_valueOrError1_).PropagateFailure()
                    return output
                d_442_keyring_ = (d_443_valueOrError1_).Extract()
                d_444_output_k_: Wrappers.Result
                out23_: Wrappers.Result
                out23_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_442_keyring_))
                d_444_output_k_ = out23_
                def lambda33_(d_445_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_445_e_)

                output = (d_444_output_k_).MapFailure(lambda33_)
        elif source15_.is_KmsMrkDiscovery:
            d_446___mcc_h4_ = source15_.KmsMrkDiscovery
            if True:
                d_447_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_448_valueOrError1_: Wrappers.Result = None
                out24_: Wrappers.Result
                out24_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_448_valueOrError1_ = out24_
                if (d_448_valueOrError1_).IsFailure():
                    output = (d_448_valueOrError1_).PropagateFailure()
                    return output
                d_447_keyring_ = (d_448_valueOrError1_).Extract()
                d_449_output_k_: Wrappers.Result
                out25_: Wrappers.Result
                out25_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_447_keyring_))
                d_449_output_k_ = out25_
                def lambda34_(d_450_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_450_e_)

                output = (d_449_output_k_).MapFailure(lambda34_)
        elif source15_.is_RSA:
            d_451___mcc_h6_ = source15_.RSA
            if True:
                d_452_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_453_valueOrError1_: Wrappers.Result = None
                out26_: Wrappers.Result
                out26_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_453_valueOrError1_ = out26_
                if (d_453_valueOrError1_).IsFailure():
                    output = (d_453_valueOrError1_).PropagateFailure()
                    return output
                d_452_keyring_ = (d_453_valueOrError1_).Extract()
                d_454_output_k_: Wrappers.Result
                out27_: Wrappers.Result
                out27_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_452_keyring_))
                d_454_output_k_ = out27_
                def lambda35_(d_455_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_455_e_)

                output = (d_454_output_k_).MapFailure(lambda35_)
        elif source15_.is_AES:
            d_456___mcc_h8_ = source15_.AES
            if True:
                d_457_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_458_valueOrError1_: Wrappers.Result = None
                out28_: Wrappers.Result
                out28_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_458_valueOrError1_ = out28_
                if (d_458_valueOrError1_).IsFailure():
                    output = (d_458_valueOrError1_).PropagateFailure()
                    return output
                d_457_keyring_ = (d_458_valueOrError1_).Extract()
                d_459_output_k_: Wrappers.Result
                out29_: Wrappers.Result
                out29_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_457_keyring_))
                d_459_output_k_ = out29_
                def lambda36_(d_460_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_460_e_)

                output = (d_459_output_k_).MapFailure(lambda36_)
        elif source15_.is_Static:
            d_461___mcc_h10_ = source15_.Static
            if True:
                d_462_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_463_valueOrError1_: Wrappers.Result = None
                out30_: Wrappers.Result
                out30_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_463_valueOrError1_ = out30_
                if (d_463_valueOrError1_).IsFailure():
                    output = (d_463_valueOrError1_).PropagateFailure()
                    return output
                d_462_keyring_ = (d_463_valueOrError1_).Extract()
                d_464_output_k_: Wrappers.Result
                out31_: Wrappers.Result
                out31_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_462_keyring_))
                d_464_output_k_ = out31_
                def lambda37_(d_465_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_465_e_)

                output = (d_464_output_k_).MapFailure(lambda37_)
        elif source15_.is_KmsRsa:
            d_466___mcc_h12_ = source15_.KmsRsa
            if True:
                d_467_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_468_valueOrError1_: Wrappers.Result = None
                out32_: Wrappers.Result
                out32_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_468_valueOrError1_ = out32_
                if (d_468_valueOrError1_).IsFailure():
                    output = (d_468_valueOrError1_).PropagateFailure()
                    return output
                d_467_keyring_ = (d_468_valueOrError1_).Extract()
                d_469_output_k_: Wrappers.Result
                out33_: Wrappers.Result
                out33_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_467_keyring_))
                d_469_output_k_ = out33_
                def lambda38_(d_470_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_470_e_)

                output = (d_469_output_k_).MapFailure(lambda38_)
        elif source15_.is_Hierarchy:
            d_471___mcc_h14_ = source15_.Hierarchy
            if True:
                d_472_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_473_valueOrError1_: Wrappers.Result = None
                out34_: Wrappers.Result
                out34_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_473_valueOrError1_ = out34_
                if (d_473_valueOrError1_).IsFailure():
                    output = (d_473_valueOrError1_).PropagateFailure()
                    return output
                d_472_keyring_ = (d_473_valueOrError1_).Extract()
                d_474_output_k_: Wrappers.Result
                out35_: Wrappers.Result
                out35_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_472_keyring_))
                d_474_output_k_ = out35_
                def lambda39_(d_475_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_475_e_)

                output = (d_474_output_k_).MapFailure(lambda39_)
        elif source15_.is_Multi:
            d_476___mcc_h16_ = source15_.Multi
            if True:
                d_477_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_478_valueOrError1_: Wrappers.Result = None
                out36_: Wrappers.Result
                out36_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_478_valueOrError1_ = out36_
                if (d_478_valueOrError1_).IsFailure():
                    output = (d_478_valueOrError1_).PropagateFailure()
                    return output
                d_477_keyring_ = (d_478_valueOrError1_).Extract()
                d_479_output_k_: Wrappers.Result
                out37_: Wrappers.Result
                out37_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_477_keyring_))
                d_479_output_k_ = out37_
                def lambda40_(d_480_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_480_e_)

                output = (d_479_output_k_).MapFailure(lambda40_)
        elif True:
            d_481___mcc_h18_ = source15_.RequiredEncryptionContext
            d_482_cmm_ = d_481___mcc_h18_
            if True:
                d_483_underlying_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
                d_484_valueOrError0_: Wrappers.Result = None
                out38_: Wrappers.Result
                out38_ = default__.ToCmm(mpl, keys, (d_482_cmm_).underlying, forOperation)
                d_484_valueOrError0_ = out38_
                if (d_484_valueOrError0_).IsFailure():
                    output = (d_484_valueOrError0_).PropagateFailure()
                    return output
                d_483_underlying_ = (d_484_valueOrError0_).Extract()
                d_485_output_k_: Wrappers.Result
                out39_: Wrappers.Result
                out39_ = (mpl).CreateRequiredEncryptionContextCMM(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput(Wrappers.Option_Some(d_483_underlying_), Wrappers.Option_None(), (d_482_cmm_).requiredEncryptionContextKeys))
                d_485_output_k_ = out39_
                def lambda41_(d_486_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_486_e_)

                output = (d_485_output_k_).MapFailure(lambda41_)
        return output

