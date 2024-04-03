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
        d_437_material_: Wrappers.Option
        d_437_material_ = KeyringFromKeyDescription.default__.GetKeyMaterial(keys, description)
        source15_ = description
        print(f"{source15_=}")
        if source15_.is_Kms:
            d_438___mcc_h0_ = source15_.Kms
            if True:
                d_439_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_440_valueOrError1_: Wrappers.Result = None
                out20_: Wrappers.Result
                out20_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_440_valueOrError1_ = out20_
                if (d_440_valueOrError1_).IsFailure():
                    output = (d_440_valueOrError1_).PropagateFailure()
                    return output
                d_439_keyring_ = (d_440_valueOrError1_).Extract()
                d_441_output_k_: Wrappers.Result
                out21_: Wrappers.Result
                out21_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_439_keyring_))
                d_441_output_k_ = out21_
                def lambda32_(d_442_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_442_e_)

                output = (d_441_output_k_).MapFailure(lambda32_)
        elif source15_.is_KmsMrk:
            d_443___mcc_h2_ = source15_.KmsMrk
            if True:
                d_444_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_445_valueOrError1_: Wrappers.Result = None
                out22_: Wrappers.Result
                out22_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_445_valueOrError1_ = out22_
                if (d_445_valueOrError1_).IsFailure():
                    output = (d_445_valueOrError1_).PropagateFailure()
                    return output
                d_444_keyring_ = (d_445_valueOrError1_).Extract()
                d_446_output_k_: Wrappers.Result
                out23_: Wrappers.Result
                out23_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_444_keyring_))
                d_446_output_k_ = out23_
                def lambda33_(d_447_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_447_e_)

                output = (d_446_output_k_).MapFailure(lambda33_)
        elif source15_.is_KmsMrkDiscovery:
            d_448___mcc_h4_ = source15_.KmsMrkDiscovery
            if True:
                d_449_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_450_valueOrError1_: Wrappers.Result = None
                out24_: Wrappers.Result
                out24_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_450_valueOrError1_ = out24_
                if (d_450_valueOrError1_).IsFailure():
                    output = (d_450_valueOrError1_).PropagateFailure()
                    return output
                d_449_keyring_ = (d_450_valueOrError1_).Extract()
                d_451_output_k_: Wrappers.Result
                out25_: Wrappers.Result
                out25_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_449_keyring_))
                d_451_output_k_ = out25_
                def lambda34_(d_452_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_452_e_)

                output = (d_451_output_k_).MapFailure(lambda34_)
        elif source15_.is_RSA:
            d_453___mcc_h6_ = source15_.RSA
            if True:
                d_454_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_455_valueOrError1_: Wrappers.Result = None
                out26_: Wrappers.Result
                out26_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_455_valueOrError1_ = out26_
                if (d_455_valueOrError1_).IsFailure():
                    output = (d_455_valueOrError1_).PropagateFailure()
                    return output
                d_454_keyring_ = (d_455_valueOrError1_).Extract()
                d_456_output_k_: Wrappers.Result
                out27_: Wrappers.Result
                out27_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_454_keyring_))
                d_456_output_k_ = out27_
                def lambda35_(d_457_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_457_e_)

                output = (d_456_output_k_).MapFailure(lambda35_)
        elif source15_.is_AES:
            d_458___mcc_h8_ = source15_.AES
            if True:
                d_459_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_460_valueOrError1_: Wrappers.Result = None
                out28_: Wrappers.Result
                out28_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_460_valueOrError1_ = out28_
                if (d_460_valueOrError1_).IsFailure():
                    output = (d_460_valueOrError1_).PropagateFailure()
                    return output
                d_459_keyring_ = (d_460_valueOrError1_).Extract()
                d_461_output_k_: Wrappers.Result
                out29_: Wrappers.Result
                out29_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_459_keyring_))
                d_461_output_k_ = out29_
                def lambda36_(d_462_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_462_e_)

                output = (d_461_output_k_).MapFailure(lambda36_)
        elif source15_.is_Static:
            d_463___mcc_h10_ = source15_.Static
            if True:
                d_464_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_465_valueOrError1_: Wrappers.Result = None
                out30_: Wrappers.Result
                out30_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_465_valueOrError1_ = out30_
                if (d_465_valueOrError1_).IsFailure():
                    output = (d_465_valueOrError1_).PropagateFailure()
                    return output
                d_464_keyring_ = (d_465_valueOrError1_).Extract()
                d_466_output_k_: Wrappers.Result
                out31_: Wrappers.Result
                out31_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_464_keyring_))
                d_466_output_k_ = out31_
                def lambda37_(d_467_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_467_e_)

                output = (d_466_output_k_).MapFailure(lambda37_)
        elif source15_.is_KmsRsa:
            d_468___mcc_h12_ = source15_.KmsRsa
            if True:
                d_469_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_470_valueOrError1_: Wrappers.Result = None
                out32_: Wrappers.Result
                out32_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_470_valueOrError1_ = out32_
                if (d_470_valueOrError1_).IsFailure():
                    output = (d_470_valueOrError1_).PropagateFailure()
                    return output
                d_469_keyring_ = (d_470_valueOrError1_).Extract()
                d_471_output_k_: Wrappers.Result
                out33_: Wrappers.Result
                out33_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_469_keyring_))
                d_471_output_k_ = out33_
                def lambda38_(d_472_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_472_e_)

                output = (d_471_output_k_).MapFailure(lambda38_)
        elif source15_.is_Hierarchy:
            d_473___mcc_h14_ = source15_.Hierarchy
            if True:
                d_474_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_475_valueOrError1_: Wrappers.Result = None
                out34_: Wrappers.Result
                print(f"{mpl=}")
                print(f"{keys=}")
                print(f"{description=}")
                print(f"{source15_.Hierarchy.keyId.Elements=}")
                out34_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                print(f"{out34_=}")
                d_475_valueOrError1_ = out34_
                if (d_475_valueOrError1_).IsFailure():
                    output = (d_475_valueOrError1_).PropagateFailure()
                    return output
                d_474_keyring_ = (d_475_valueOrError1_).Extract()
                d_476_output_k_: Wrappers.Result
                try:
                    out35_: Wrappers.Result
                    out35_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_474_keyring_))
                    print(f"{out35_=}")
                    d_476_output_k_ = out35_
                    def lambda39_(d_477_e_):
                        return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_477_e_)
                except Exception as e:
                    print(e)

                output = (d_476_output_k_).MapFailure(lambda39_)
        elif source15_.is_Multi:
            d_478___mcc_h16_ = source15_.Multi
            if True:
                d_479_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                d_480_valueOrError1_: Wrappers.Result = None
                out36_: Wrappers.Result
                out36_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_480_valueOrError1_ = out36_
                if (d_480_valueOrError1_).IsFailure():
                    output = (d_480_valueOrError1_).PropagateFailure()
                    return output
                d_479_keyring_ = (d_480_valueOrError1_).Extract()
                d_481_output_k_: Wrappers.Result
                out37_: Wrappers.Result
                out37_ = (mpl).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_479_keyring_))
                d_481_output_k_ = out37_
                def lambda40_(d_482_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_482_e_)

                output = (d_481_output_k_).MapFailure(lambda40_)
        elif True:
            d_483___mcc_h18_ = source15_.RequiredEncryptionContext
            d_484_cmm_ = d_483___mcc_h18_
            if True:
                d_485_underlying_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
                d_486_valueOrError0_: Wrappers.Result = None
                out38_: Wrappers.Result
                out38_ = default__.ToCmm(mpl, keys, (d_484_cmm_).underlying, forOperation)
                d_486_valueOrError0_ = out38_
                if (d_486_valueOrError0_).IsFailure():
                    output = (d_486_valueOrError0_).PropagateFailure()
                    return output
                d_485_underlying_ = (d_486_valueOrError0_).Extract()
                d_487_output_k_: Wrappers.Result
                out39_: Wrappers.Result
                out39_ = (mpl).CreateRequiredEncryptionContextCMM(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput(Wrappers.Option_Some(d_485_underlying_), Wrappers.Option_None(), (d_484_cmm_).requiredEncryptionContextKeys))
                d_487_output_k_ = out39_
                def lambda41_(d_488_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_488_e_)

                output = (d_487_output_k_).MapFailure(lambda41_)
        return output

