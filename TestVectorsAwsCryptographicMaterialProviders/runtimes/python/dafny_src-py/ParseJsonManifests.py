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
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
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
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
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
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import CompleteVectors

# Module: ParseJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildEncryptTestVector(keys, obj):
        if (len(obj)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_599_name_ = ((obj)[0])[0]
            d_600_valueOrError0_ = default__.ToEncryptTestVector(keys, d_599_name_, ((obj)[0])[1])
            if (d_600_valueOrError0_).IsFailure():
                return (d_600_valueOrError0_).PropagateFailure()
            elif True:
                d_601_encryptVector_ = (d_600_valueOrError0_).Extract()
                d_602_valueOrError1_ = default__.BuildEncryptTestVector(keys, _dafny.Seq((obj)[1::]))
                if (d_602_valueOrError1_).IsFailure():
                    return (d_602_valueOrError1_).PropagateFailure()
                elif True:
                    d_603_tail_ = (d_602_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_601_encryptVector_])) + (d_603_tail_))

    @staticmethod
    def ToEncryptTestVector(keys, name, obj):
        d_604_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("EncryptTestVector not an object"))
        if (d_604_valueOrError0_).IsFailure():
            return (d_604_valueOrError0_).PropagateFailure()
        elif True:
            d_605_obj_ = (obj).obj
            d_606_typString_ = _dafny.Seq("type")
            d_607_valueOrError1_ = JSONHelpers.default__.GetString(d_606_typString_, d_605_obj_)
            if (d_607_valueOrError1_).IsFailure():
                return (d_607_valueOrError1_).PropagateFailure()
            elif True:
                d_608_typ_ = (d_607_valueOrError1_).Extract()
                d_609_description_ = (JSONHelpers.default__.GetString(_dafny.Seq("description"), d_605_obj_)).ToOption()
                d_610_valueOrError2_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_605_obj_)
                if (d_610_valueOrError2_).IsFailure():
                    return (d_610_valueOrError2_).PropagateFailure()
                elif True:
                    d_611_encryptionContextStrings_ = (d_610_valueOrError2_).Extract()
                    d_612_valueOrError3_ = JSONHelpers.default__.utf8EncodeMap(d_611_encryptionContextStrings_)
                    if (d_612_valueOrError3_).IsFailure():
                        return (d_612_valueOrError3_).PropagateFailure()
                    elif True:
                        d_613_encryptionContext_ = (d_612_valueOrError3_).Extract()
                        d_614_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), d_605_obj_)
                        if (d_614_valueOrError4_).IsFailure():
                            return (d_614_valueOrError4_).PropagateFailure()
                        elif True:
                            d_615_algorithmSuiteHex_ = (d_614_valueOrError4_).Extract()
                            d_616_valueOrError5_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_615_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binnary"))
                            if (d_616_valueOrError5_).IsFailure():
                                return (d_616_valueOrError5_).PropagateFailure()
                            elif True:
                                d_617_binaryId_ = HexStrings.default__.FromHexString(d_615_algorithmSuiteHex_)
                                def lambda42_(d_619_algorithmSuiteHex_):
                                    def lambda43_(d_620_e_):
                                        return (_dafny.Seq("Invalid Suite:")) + (d_619_algorithmSuiteHex_)

                                    return lambda43_

                                d_618_valueOrError6_ = (AlgorithmSuites.default__.GetAlgorithmSuiteInfo(d_617_binaryId_)).MapFailure(lambda42_(d_615_algorithmSuiteHex_))
                                if (d_618_valueOrError6_).IsFailure():
                                    return (d_618_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_621_algorithmSuite_ = (d_618_valueOrError6_).Extract()
                                    d_622_keysAsStrings_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_605_obj_)).ToOption()
                                    def iife30_(_pat_let7_0):
                                        def iife31_(d_624_result_):
                                            return (Wrappers.Result_Success(Wrappers.Option_Some((d_624_result_).value)) if (d_624_result_).is_Success else Wrappers.Result_Failure((d_624_result_).error))
                                        return iife31_(_pat_let7_0)
                                    d_623_valueOrError7_ = (iife30_(JSONHelpers.default__.utf8EncodeSeq((d_622_keysAsStrings_).value)) if (d_622_keysAsStrings_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                                    if (d_623_valueOrError7_).IsFailure():
                                        return (d_623_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_625_requiredEncryptionContextKeys_ = (d_623_valueOrError7_).Extract()
                                        d_626_commitmentPolicy_ = CompleteVectors.default__.GetCompatableCommitmentPolicy(d_621_algorithmSuite_)
                                        d_627_maxPlaintextLength_ = Wrappers.Option_None()
                                        if (d_608_typ_) == (_dafny.Seq("positive-keyring")):
                                            d_628_valueOrError8_ = JSONHelpers.default__.Get(_dafny.Seq("encryptKeyDescription"), d_605_obj_)
                                            if (d_628_valueOrError8_).IsFailure():
                                                return (d_628_valueOrError8_).PropagateFailure()
                                            elif True:
                                                d_629_encryptKeyDescriptionObject_ = (d_628_valueOrError8_).Extract()
                                                d_630_valueOrError9_ = JSONHelpers.default__.Get(_dafny.Seq("decryptKeyDescription"), d_605_obj_)
                                                if (d_630_valueOrError9_).IsFailure():
                                                    return (d_630_valueOrError9_).PropagateFailure()
                                                elif True:
                                                    d_631_decryptKeyDescriptionObject_ = (d_630_valueOrError9_).Extract()
                                                    def lambda44_(d_633_e_):
                                                        return (d_633_e_).ToString()

                                                    d_632_valueOrError10_ = (JSON_API.default__.Serialize(d_629_encryptKeyDescriptionObject_)).MapFailure(lambda44_)
                                                    if (d_632_valueOrError10_).IsFailure():
                                                        return (d_632_valueOrError10_).PropagateFailure()
                                                    elif True:
                                                        d_634_encryptStr_ = (d_632_valueOrError10_).Extract()
                                                        def lambda45_(d_636_e_):
                                                            return (d_636_e_).ToString()

                                                        d_635_valueOrError11_ = (JSON_API.default__.Serialize(d_631_decryptKeyDescriptionObject_)).MapFailure(lambda45_)
                                                        if (d_635_valueOrError11_).IsFailure():
                                                            return (d_635_valueOrError11_).PropagateFailure()
                                                        elif True:
                                                            d_637_decryptStr_ = (d_635_valueOrError11_).Extract()
                                                            d_638_valueOrError12_ = ((keys).GetKeyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionInput_GetKeyDescriptionInput(d_634_encryptStr_))).MapFailure(default__.ErrorToString)
                                                            if (d_638_valueOrError12_).IsFailure():
                                                                return (d_638_valueOrError12_).PropagateFailure()
                                                            elif True:
                                                                d_639_encryptKeyDescription_ = (d_638_valueOrError12_).Extract()
                                                                d_640_valueOrError13_ = ((keys).GetKeyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionInput_GetKeyDescriptionInput(d_637_decryptStr_))).MapFailure(default__.ErrorToString)
                                                                if (d_640_valueOrError13_).IsFailure():
                                                                    return (d_640_valueOrError13_).PropagateFailure()
                                                                elif True:
                                                                    d_641_decryptKeyDescription_ = (d_640_valueOrError13_).Extract()
                                                                    return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(name, d_609_description_, d_613_encryptionContext_, d_626_commitmentPolicy_, d_621_algorithmSuite_, d_627_maxPlaintextLength_, d_625_requiredEncryptionContextKeys_, (d_639_encryptKeyDescription_).keyDescription, (d_641_decryptKeyDescription_).keyDescription))
                                        elif (d_608_typ_) == (_dafny.Seq("negative-keyring")):
                                            d_642_valueOrError14_ = JSONHelpers.default__.Get(_dafny.Seq("keyDescription"), d_605_obj_)
                                            if (d_642_valueOrError14_).IsFailure():
                                                return (d_642_valueOrError14_).PropagateFailure()
                                            elif True:
                                                d_643_keyDescriptionObject_ = (d_642_valueOrError14_).Extract()
                                                def lambda46_(d_645_e_):
                                                    return (d_645_e_).ToString()

                                                d_644_valueOrError15_ = (JSON_API.default__.Serialize(d_643_keyDescriptionObject_)).MapFailure(lambda46_)
                                                if (d_644_valueOrError15_).IsFailure():
                                                    return (d_644_valueOrError15_).PropagateFailure()
                                                elif True:
                                                    d_646_keyStr_ = (d_644_valueOrError15_).Extract()
                                                    d_647_valueOrError16_ = ((keys).GetKeyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionInput_GetKeyDescriptionInput(d_646_keyStr_))).MapFailure(default__.ErrorToString)
                                                    if (d_647_valueOrError16_).IsFailure():
                                                        return (d_647_valueOrError16_).PropagateFailure()
                                                    elif True:
                                                        d_648_keyDescription_ = (d_647_valueOrError16_).Extract()
                                                        d_649_valueOrError17_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_605_obj_)
                                                        if (d_649_valueOrError17_).IsFailure():
                                                            return (d_649_valueOrError17_).PropagateFailure()
                                                        elif True:
                                                            d_650_errorDescription_ = (d_649_valueOrError17_).Extract()
                                                            return Wrappers.Result_Success(TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(name, d_609_description_, d_613_encryptionContext_, d_626_commitmentPolicy_, d_621_algorithmSuite_, d_627_maxPlaintextLength_, d_625_requiredEncryptionContextKeys_, d_650_errorDescription_, (d_648_keyDescription_).keyDescription))
                                        elif True:
                                            return Wrappers.Result_Failure((_dafny.Seq("Unsupported EncryptTestVector type:")) + (d_608_typ_))

    @staticmethod
    def ErrorToString(e):
        source23_ = e
        if source23_.is_KeyVectorException:
            d_651___mcc_h0_ = source23_.message
            d_652_message_ = d_651___mcc_h0_
            return d_652_message_
        elif source23_.is_AwsCryptographyMaterialProviders:
            d_653___mcc_h2_ = source23_.AwsCryptographyMaterialProviders
            d_654_mplError_ = d_653___mcc_h2_
            source24_ = d_654_mplError_
            if source24_.is_AwsCryptographicMaterialProvidersException:
                d_655___mcc_h12_ = source24_.message
                d_656_message_ = d_655___mcc_h12_
                return d_656_message_
            elif source24_.is_EntryAlreadyExists:
                d_657___mcc_h14_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_EntryDoesNotExist:
                d_658___mcc_h16_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_InvalidAlgorithmSuiteInfo:
                d_659___mcc_h18_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_InvalidAlgorithmSuiteInfoOnDecrypt:
                d_660___mcc_h20_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_InvalidAlgorithmSuiteInfoOnEncrypt:
                d_661___mcc_h22_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_InvalidDecryptionMaterials:
                d_662___mcc_h24_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_InvalidDecryptionMaterialsTransition:
                d_663___mcc_h26_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_InvalidEncryptionMaterials:
                d_664___mcc_h28_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_InvalidEncryptionMaterialsTransition:
                d_665___mcc_h30_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_AwsCryptographyKeyStore:
                d_666___mcc_h32_ = source24_.AwsCryptographyKeyStore
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_AwsCryptographyPrimitives:
                d_667___mcc_h34_ = source24_.AwsCryptographyPrimitives
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_ComAmazonawsDynamodb:
                d_668___mcc_h36_ = source24_.ComAmazonawsDynamodb
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_ComAmazonawsKms:
                d_669___mcc_h38_ = source24_.ComAmazonawsKms
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source24_.is_CollectionOfErrors:
                d_670___mcc_h40_ = source24_.list
                d_671___mcc_h41_ = source24_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif True:
                d_672___mcc_h44_ = source24_.obj
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
        elif source23_.is_ComAmazonawsKms:
            d_673___mcc_h4_ = source23_.ComAmazonawsKms
            return _dafny.Seq("Umapped KeyVectorException")
        elif source23_.is_CollectionOfErrors:
            d_674___mcc_h6_ = source23_.list
            d_675___mcc_h7_ = source23_.message
            return _dafny.Seq("Umapped KeyVectorException")
        elif True:
            d_676___mcc_h10_ = source23_.obj
            return _dafny.Seq("Umapped KeyVectorException")

