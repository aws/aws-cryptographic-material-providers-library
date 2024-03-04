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
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import AllHierarchy
import AllKms
import AllKmsMrkAware
import AllKmsMrkAwareDiscovery
import AllKmsRsa
import AllRawAES
import AllRawRSA
import AllDefaultCmm
import AllRequiredEncryptionContextCmm
import AllMulti
import WriteJsonManifests
import CompleteVectors

# Module: ParseJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildEncryptTestVector(keys, obj):
        hresult_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_909_i_: int
        d_909_i_ = len(obj)
        d_910_vectors_: _dafny.Seq
        d_910_vectors_ = _dafny.Seq([])
        while (d_909_i_) != (0):
            d_909_i_ = (d_909_i_) - (1)
            d_911_test_: Wrappers.Result
            d_911_test_ = default__.ToEncryptTestVector(keys, ((obj)[d_909_i_])[0], ((obj)[d_909_i_])[1])
            if (d_911_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_911_test_).error)
                return hresult_
            d_910_vectors_ = (_dafny.Seq([(d_911_test_).value])) + (d_910_vectors_)
        hresult_ = Wrappers.Result_Success(d_910_vectors_)
        return hresult_
        return hresult_

    @staticmethod
    def ToEncryptTestVector(keys, name, obj):
        d_912_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("EncryptTestVector not an object"))
        if (d_912_valueOrError0_).IsFailure():
            return (d_912_valueOrError0_).PropagateFailure()
        elif True:
            d_913_obj_ = (obj).obj
            d_914_typString_ = _dafny.Seq("type")
            d_915_valueOrError1_ = JSONHelpers.default__.GetString(d_914_typString_, d_913_obj_)
            if (d_915_valueOrError1_).IsFailure():
                return (d_915_valueOrError1_).PropagateFailure()
            elif True:
                d_916_typ_ = (d_915_valueOrError1_).Extract()
                d_917_description_ = (JSONHelpers.default__.GetString(_dafny.Seq("description"), d_913_obj_)).ToOption()
                d_918_valueOrError2_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_913_obj_)
                if (d_918_valueOrError2_).IsFailure():
                    return (d_918_valueOrError2_).PropagateFailure()
                elif True:
                    d_919_encryptionContextStrings_ = (d_918_valueOrError2_).Extract()
                    d_920_valueOrError3_ = JSONHelpers.default__.utf8EncodeMap(d_919_encryptionContextStrings_)
                    if (d_920_valueOrError3_).IsFailure():
                        return (d_920_valueOrError3_).PropagateFailure()
                    elif True:
                        d_921_encryptionContext_ = (d_920_valueOrError3_).Extract()
                        d_922_valueOrError4_ = default__.GetAlgorithmSuiteInfo(d_913_obj_)
                        if (d_922_valueOrError4_).IsFailure():
                            return (d_922_valueOrError4_).PropagateFailure()
                        elif True:
                            d_923_algorithmSuite_ = (d_922_valueOrError4_).Extract()
                            d_924_valueOrError5_ = default__.GetRequiredEncryptionContextKeys(d_913_obj_)
                            if (d_924_valueOrError5_).IsFailure():
                                return (d_924_valueOrError5_).PropagateFailure()
                            elif True:
                                d_925_requiredEncryptionContextKeys_ = (d_924_valueOrError5_).Extract()
                                d_926_valueOrError6_ = default__.GetReproducedEncryptionContext(d_913_obj_)
                                if (d_926_valueOrError6_).IsFailure():
                                    return (d_926_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_927_reproducedEncryptionContext_ = (d_926_valueOrError6_).Extract()
                                    d_928_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_923_algorithmSuite_)
                                    d_929_maxPlaintextLength_ = (JSONHelpers.default__.GetPositiveLong(_dafny.Seq("maxPlaintextLength"), d_913_obj_)).ToOption()
                                    if (d_916_typ_) == (_dafny.Seq("positive-keyring")):
                                        d_930_valueOrError7_ = default__.GetKeyDescription(keys, _dafny.Seq("encryptKeyDescription"), d_913_obj_)
                                        if (d_930_valueOrError7_).IsFailure():
                                            return (d_930_valueOrError7_).PropagateFailure()
                                        elif True:
                                            d_931_encryptKeyDescription_ = (d_930_valueOrError7_).Extract()
                                            d_932_valueOrError8_ = default__.GetKeyDescription(keys, _dafny.Seq("decryptKeyDescription"), d_913_obj_)
                                            if (d_932_valueOrError8_).IsFailure():
                                                return (d_932_valueOrError8_).PropagateFailure()
                                            elif True:
                                                d_933_decryptKeyDescription_ = (d_932_valueOrError8_).Extract()
                                                return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(name, d_917_description_, d_921_encryptionContext_, d_928_commitmentPolicy_, d_923_algorithmSuite_, d_929_maxPlaintextLength_, d_925_requiredEncryptionContextKeys_, d_931_encryptKeyDescription_, d_933_decryptKeyDescription_, d_927_reproducedEncryptionContext_))
                                    elif (d_916_typ_) == (_dafny.Seq("negative-encrypt-keyring")):
                                        d_934_valueOrError9_ = default__.GetKeyDescription(keys, _dafny.Seq("keyDescription"), d_913_obj_)
                                        if (d_934_valueOrError9_).IsFailure():
                                            return (d_934_valueOrError9_).PropagateFailure()
                                        elif True:
                                            d_935_keyDescription_ = (d_934_valueOrError9_).Extract()
                                            d_936_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_913_obj_)
                                            if (d_936_valueOrError10_).IsFailure():
                                                return (d_936_valueOrError10_).PropagateFailure()
                                            elif True:
                                                d_937_errorDescription_ = (d_936_valueOrError10_).Extract()
                                                d_938_valueOrError11_ = Wrappers.default__.Need((d_927_reproducedEncryptionContext_).is_None, _dafny.Seq("reproducedEncryptionContext not supported"))
                                                if (d_938_valueOrError11_).IsFailure():
                                                    return (d_938_valueOrError11_).PropagateFailure()
                                                elif True:
                                                    return Wrappers.Result_Success(TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(name, d_917_description_, d_921_encryptionContext_, d_928_commitmentPolicy_, d_923_algorithmSuite_, d_929_maxPlaintextLength_, d_925_requiredEncryptionContextKeys_, d_937_errorDescription_, d_935_keyDescription_))
                                    elif (d_916_typ_) == (_dafny.Seq("negative-decrypt-keyring")):
                                        d_939_valueOrError12_ = default__.GetKeyDescription(keys, _dafny.Seq("encryptKeyDescription"), d_913_obj_)
                                        if (d_939_valueOrError12_).IsFailure():
                                            return (d_939_valueOrError12_).PropagateFailure()
                                        elif True:
                                            d_940_encryptKeyDescription_ = (d_939_valueOrError12_).Extract()
                                            d_941_valueOrError13_ = default__.GetKeyDescription(keys, _dafny.Seq("decryptKeyDescription"), d_913_obj_)
                                            if (d_941_valueOrError13_).IsFailure():
                                                return (d_941_valueOrError13_).PropagateFailure()
                                            elif True:
                                                d_942_decryptKeyDescription_ = (d_941_valueOrError13_).Extract()
                                                d_943_valueOrError14_ = JSONHelpers.default__.GetString(_dafny.Seq("decryptErrorDescription"), d_913_obj_)
                                                if (d_943_valueOrError14_).IsFailure():
                                                    return (d_943_valueOrError14_).PropagateFailure()
                                                elif True:
                                                    d_944_decryptErrorDescription_ = (d_943_valueOrError14_).Extract()
                                                    return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(name, d_917_description_, d_921_encryptionContext_, d_928_commitmentPolicy_, d_923_algorithmSuite_, d_929_maxPlaintextLength_, d_925_requiredEncryptionContextKeys_, d_944_decryptErrorDescription_, d_940_encryptKeyDescription_, d_942_decryptKeyDescription_, d_927_reproducedEncryptionContext_))
                                    elif True:
                                        return Wrappers.Result_Failure((_dafny.Seq("Unsupported EncryptTestVector type:")) + (d_916_typ_))

    @staticmethod
    def GetKeyDescription(keyVectorClient, key, obj):
        d_945_valueOrError0_ = JSONHelpers.default__.Get(key, obj)
        if (d_945_valueOrError0_).IsFailure():
            return (d_945_valueOrError0_).PropagateFailure()
        elif True:
            d_946_keyDescriptionObject_ = (d_945_valueOrError0_).Extract()
            def lambda103_(d_948_e_):
                return (d_948_e_).ToString()

            d_947_valueOrError1_ = (JSON_API.default__.Serialize(d_946_keyDescriptionObject_)).MapFailure(lambda103_)
            if (d_947_valueOrError1_).IsFailure():
                return (d_947_valueOrError1_).PropagateFailure()
            elif True:
                d_949_descriptionStr_ = (d_947_valueOrError1_).Extract()
                d_950_valueOrError2_ = ((keyVectorClient).GetKeyDescription(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionInput_GetKeyDescriptionInput(d_949_descriptionStr_))).MapFailure(default__.ErrorToString)
                if (d_950_valueOrError2_).IsFailure():
                    return (d_950_valueOrError2_).PropagateFailure()
                elif True:
                    d_951_keyDescriptionOutput_ = (d_950_valueOrError2_).Extract()
                    return Wrappers.Result_Success((d_951_keyDescriptionOutput_).keyDescription)

    @staticmethod
    def GetAlgorithmSuiteInfo(obj):
        d_952_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), obj)
        if (d_952_valueOrError0_).IsFailure():
            return (d_952_valueOrError0_).PropagateFailure()
        elif True:
            d_953_algorithmSuiteHex_ = (d_952_valueOrError0_).Extract()
            d_954_valueOrError1_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_953_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binary"))
            if (d_954_valueOrError1_).IsFailure():
                return (d_954_valueOrError1_).PropagateFailure()
            elif True:
                d_955_binaryId_ = HexStrings.default__.FromHexString(d_953_algorithmSuiteHex_)
                def lambda104_(d_956_algorithmSuiteHex_):
                    def lambda105_(d_957_e_):
                        return (_dafny.Seq("Invalid Suite:")) + (d_956_algorithmSuiteHex_)

                    return lambda105_

                return (AlgorithmSuites.default__.GetAlgorithmSuiteInfo(d_955_binaryId_)).MapFailure(lambda104_(d_953_algorithmSuiteHex_))

    @staticmethod
    def GetRequiredEncryptionContextKeys(obj):
        d_958_keysAsStrings_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), obj)).ToOption()
        source24_ = d_958_keysAsStrings_
        if source24_.is_None:
            return Wrappers.Result_Success(Wrappers.Option_None())
        elif True:
            d_959___mcc_h0_ = source24_.value
            d_960_s_ = d_959___mcc_h0_
            d_961_valueOrError0_ = JSONHelpers.default__.utf8EncodeSeq((d_958_keysAsStrings_).value)
            if (d_961_valueOrError0_).IsFailure():
                return (d_961_valueOrError0_).PropagateFailure()
            elif True:
                d_962_k_ = (d_961_valueOrError0_).Extract()
                return Wrappers.Result_Success(Wrappers.Option_Some(d_962_k_))

    @staticmethod
    def GetReproducedEncryptionContext(obj):
        d_963_valueOrError0_ = JSONHelpers.default__.GetOptionalSmallObjectToStringStringMap(_dafny.Seq("reproducedEncryptionContext"), obj)
        if (d_963_valueOrError0_).IsFailure():
            return (d_963_valueOrError0_).PropagateFailure()
        elif True:
            d_964_reproducedEncryptionContextStrings_ = (d_963_valueOrError0_).Extract()
            source25_ = d_964_reproducedEncryptionContextStrings_
            if source25_.is_None:
                return Wrappers.Result_Success(Wrappers.Option_None())
            elif True:
                d_965___mcc_h0_ = source25_.value
                d_966_r_ = d_965___mcc_h0_
                d_967_valueOrError1_ = JSONHelpers.default__.utf8EncodeMap(d_966_r_)
                if (d_967_valueOrError1_).IsFailure():
                    return (d_967_valueOrError1_).PropagateFailure()
                elif True:
                    d_968_e_ = (d_967_valueOrError1_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_968_e_))

    @staticmethod
    def ErrorToString(e):
        source26_ = e
        if source26_.is_KeyVectorException:
            d_969___mcc_h0_ = source26_.message
            d_970_message_ = d_969___mcc_h0_
            return d_970_message_
        elif source26_.is_AwsCryptographyMaterialProviders:
            d_971___mcc_h2_ = source26_.AwsCryptographyMaterialProviders
            d_972_mplError_ = d_971___mcc_h2_
            source27_ = d_972_mplError_
            if source27_.is_AwsCryptographicMaterialProvidersException:
                d_973___mcc_h12_ = source27_.message
                d_974_message_ = d_973___mcc_h12_
                return d_974_message_
            elif source27_.is_EntryAlreadyExists:
                d_975___mcc_h14_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_EntryDoesNotExist:
                d_976___mcc_h16_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_InvalidAlgorithmSuiteInfo:
                d_977___mcc_h18_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_InvalidAlgorithmSuiteInfoOnDecrypt:
                d_978___mcc_h20_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_InvalidAlgorithmSuiteInfoOnEncrypt:
                d_979___mcc_h22_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_InvalidDecryptionMaterials:
                d_980___mcc_h24_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_InvalidDecryptionMaterialsTransition:
                d_981___mcc_h26_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_InvalidEncryptionMaterials:
                d_982___mcc_h28_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_InvalidEncryptionMaterialsTransition:
                d_983___mcc_h30_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_AwsCryptographyKeyStore:
                d_984___mcc_h32_ = source27_.AwsCryptographyKeyStore
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_AwsCryptographyPrimitives:
                d_985___mcc_h34_ = source27_.AwsCryptographyPrimitives
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_ComAmazonawsDynamodb:
                d_986___mcc_h36_ = source27_.ComAmazonawsDynamodb
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_ComAmazonawsKms:
                d_987___mcc_h38_ = source27_.ComAmazonawsKms
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source27_.is_CollectionOfErrors:
                d_988___mcc_h40_ = source27_.list
                d_989___mcc_h41_ = source27_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif True:
                d_990___mcc_h44_ = source27_.obj
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
        elif source26_.is_ComAmazonawsKms:
            d_991___mcc_h4_ = source26_.ComAmazonawsKms
            return _dafny.Seq("Unmapped KeyVectorException")
        elif source26_.is_CollectionOfErrors:
            d_992___mcc_h6_ = source26_.list
            d_993___mcc_h7_ = source26_.message
            return _dafny.Seq("Unmapped KeyVectorException")
        elif True:
            d_994___mcc_h10_ = source26_.obj
            return _dafny.Seq("Unmapped KeyVectorException")

    @staticmethod
    def BuildDecryptTestVector(keys, obj):
        hresult_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_995_i_: int
        d_995_i_ = len(obj)
        d_996_vectors_: _dafny.Seq
        d_996_vectors_ = _dafny.Seq([])
        while (d_995_i_) != (0):
            d_995_i_ = (d_995_i_) - (1)
            d_997_test_: Wrappers.Result
            d_997_test_ = default__.ToDecryptTestVector(keys, ((obj)[d_995_i_])[0], ((obj)[d_995_i_])[1])
            if (d_997_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_997_test_).error)
                return hresult_
            d_996_vectors_ = (_dafny.Seq([(d_997_test_).value])) + (d_996_vectors_)
        hresult_ = Wrappers.Result_Success(d_996_vectors_)
        return hresult_
        return hresult_

    @staticmethod
    def printJson(j):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(j))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def GetEncryptedDataKeys(obj):
        d_998_valueOrError0_ = JSONHelpers.default__.GetArray(_dafny.Seq("encryptedDataKeys"), obj)
        if (d_998_valueOrError0_).IsFailure():
            return (d_998_valueOrError0_).PropagateFailure()
        elif True:
            d_999_encryptedDataKeysJson_ = (d_998_valueOrError0_).Extract()
            return Seq.default__.MapWithResult(default__.GetEncryptedDataKey, d_999_encryptedDataKeysJson_)

    @staticmethod
    def GetEncryptedDataKey(json):
        d_1000_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("Encrypted data key is not an object"))
        if (d_1000_valueOrError0_).IsFailure():
            return (d_1000_valueOrError0_).PropagateFailure()
        elif True:
            d_1001_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), (json).obj)
            if (d_1001_valueOrError1_).IsFailure():
                return (d_1001_valueOrError1_).PropagateFailure()
            elif True:
                d_1002_keyProviderId_ = (d_1001_valueOrError1_).Extract()
                d_1003_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), (json).obj)
                if (d_1003_valueOrError2_).IsFailure():
                    return (d_1003_valueOrError2_).PropagateFailure()
                elif True:
                    d_1004_keyProviderInfo_ = (d_1003_valueOrError2_).Extract()
                    d_1005_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), (json).obj)
                    if (d_1005_valueOrError3_).IsFailure():
                        return (d_1005_valueOrError3_).PropagateFailure()
                    elif True:
                        d_1006_ciphertext_ = (d_1005_valueOrError3_).Extract()
                        d_1007_valueOrError4_ = UTF8.default__.Encode(d_1002_keyProviderId_)
                        if (d_1007_valueOrError4_).IsFailure():
                            return (d_1007_valueOrError4_).PropagateFailure()
                        elif True:
                            d_1008_keyProviderId_ = (d_1007_valueOrError4_).Extract()
                            d_1009_valueOrError5_ = Base64.default__.Decode(d_1004_keyProviderInfo_)
                            if (d_1009_valueOrError5_).IsFailure():
                                return (d_1009_valueOrError5_).PropagateFailure()
                            elif True:
                                d_1010_keyProviderInfo_ = (d_1009_valueOrError5_).Extract()
                                d_1011_valueOrError6_ = Base64.default__.Decode(d_1006_ciphertext_)
                                if (d_1011_valueOrError6_).IsFailure():
                                    return (d_1011_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_1012_ciphertext_ = (d_1011_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(d_1008_keyProviderId_, d_1010_keyProviderInfo_, d_1012_ciphertext_))

    @staticmethod
    def GetExpectedResult(obj):
        d_1013_valueOrError0_ = JSONHelpers.default__.GetObject(_dafny.Seq("result"), obj)
        if (d_1013_valueOrError0_).IsFailure():
            return (d_1013_valueOrError0_).PropagateFailure()
        elif True:
            d_1014_result_ = (d_1013_valueOrError0_).Extract()
            d_1015_valueOrError1_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), d_1014_result_)
            if (d_1015_valueOrError1_).IsFailure():
                return (d_1015_valueOrError1_).PropagateFailure()
            elif True:
                d_1016_plaintextDataKey_ = (d_1015_valueOrError1_).Extract()
                d_1017_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("symmetricSigningKey"), d_1014_result_)
                if (d_1017_valueOrError2_).IsFailure():
                    return (d_1017_valueOrError2_).PropagateFailure()
                elif True:
                    d_1018_symmetricSigningKey_ = (d_1017_valueOrError2_).Extract()
                    d_1019_valueOrError3_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_1014_result_)
                    if (d_1019_valueOrError3_).IsFailure():
                        return (d_1019_valueOrError3_).PropagateFailure()
                    elif True:
                        d_1020_requiredEncryptionContextKeys_ = (d_1019_valueOrError3_).Extract()
                        def iife95_(_pat_let22_0):
                            def iife96_(d_1022_valueOrError5_):
                                def iife97_(_pat_let23_0):
                                    def iife98_(d_1023_p_):
                                        return Wrappers.Result_Success(Wrappers.Option_Some(d_1023_p_))
                                    return iife98_(_pat_let23_0)
                                return ((d_1022_valueOrError5_).PropagateFailure() if (d_1022_valueOrError5_).IsFailure() else iife97_((d_1022_valueOrError5_).Extract()))
                            return iife96_(_pat_let22_0)
                        d_1021_valueOrError4_ = (iife95_(Base64.default__.Decode((d_1016_plaintextDataKey_).value)) if (d_1016_plaintextDataKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                        if (d_1021_valueOrError4_).IsFailure():
                            return (d_1021_valueOrError4_).PropagateFailure()
                        elif True:
                            d_1024_plaintextDataKey_ = (d_1021_valueOrError4_).Extract()
                            def iife99_(_pat_let24_0):
                                def iife100_(d_1026_valueOrError7_):
                                    def iife101_(_pat_let25_0):
                                        def iife102_(d_1027_p_):
                                            return Wrappers.Result_Success(Wrappers.Option_Some(d_1027_p_))
                                        return iife102_(_pat_let25_0)
                                    return ((d_1026_valueOrError7_).PropagateFailure() if (d_1026_valueOrError7_).IsFailure() else iife101_((d_1026_valueOrError7_).Extract()))
                                return iife100_(_pat_let24_0)
                            d_1025_valueOrError6_ = (iife99_(Base64.default__.Decode((d_1018_symmetricSigningKey_).value)) if (d_1018_symmetricSigningKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                            if (d_1025_valueOrError6_).IsFailure():
                                return (d_1025_valueOrError6_).PropagateFailure()
                            elif True:
                                d_1028_symmetricSigningKey_ = (d_1025_valueOrError6_).Extract()
                                d_1029_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_1020_requiredEncryptionContextKeys_)
                                if (d_1029_valueOrError8_).IsFailure():
                                    return (d_1029_valueOrError8_).PropagateFailure()
                                elif True:
                                    d_1030_requiredEncryptionContextKeys_ = (d_1029_valueOrError8_).Extract()
                                    return Wrappers.Result_Success(TestVectors.DecryptResult_DecryptResult(d_1024_plaintextDataKey_, d_1028_symmetricSigningKey_, d_1030_requiredEncryptionContextKeys_))

    @staticmethod
    def ToDecryptTestVector(keys, name, json):
        d_1031_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("DecryptTestVector not an object"))
        if (d_1031_valueOrError0_).IsFailure():
            return (d_1031_valueOrError0_).PropagateFailure()
        elif True:
            d_1032_obj_ = (json).obj
            d_1033_typString_ = _dafny.Seq("type")
            d_1034_valueOrError1_ = JSONHelpers.default__.GetString(d_1033_typString_, d_1032_obj_)
            if (d_1034_valueOrError1_).IsFailure():
                return (d_1034_valueOrError1_).PropagateFailure()
            elif True:
                d_1035_typ_ = (d_1034_valueOrError1_).Extract()
                d_1036_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("description"), d_1032_obj_)
                if (d_1036_valueOrError2_).IsFailure():
                    return (d_1036_valueOrError2_).PropagateFailure()
                elif True:
                    d_1037_description_ = (d_1036_valueOrError2_).Extract()
                    d_1038_valueOrError3_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_1032_obj_)
                    if (d_1038_valueOrError3_).IsFailure():
                        return (d_1038_valueOrError3_).PropagateFailure()
                    elif True:
                        d_1039_encryptionContextStrings_ = (d_1038_valueOrError3_).Extract()
                        d_1040_valueOrError4_ = JSONHelpers.default__.utf8EncodeMap(d_1039_encryptionContextStrings_)
                        if (d_1040_valueOrError4_).IsFailure():
                            return (d_1040_valueOrError4_).PropagateFailure()
                        elif True:
                            d_1041_encryptionContext_ = (d_1040_valueOrError4_).Extract()
                            d_1042_valueOrError5_ = default__.GetAlgorithmSuiteInfo(d_1032_obj_)
                            if (d_1042_valueOrError5_).IsFailure():
                                return (d_1042_valueOrError5_).PropagateFailure()
                            elif True:
                                d_1043_algorithmSuite_ = (d_1042_valueOrError5_).Extract()
                                d_1044_valueOrError6_ = default__.GetReproducedEncryptionContext(d_1032_obj_)
                                if (d_1044_valueOrError6_).IsFailure():
                                    return (d_1044_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_1045_reproducedEncryptionContext_ = (d_1044_valueOrError6_).Extract()
                                    d_1046_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_1043_algorithmSuite_)
                                    d_1047_valueOrError7_ = default__.GetKeyDescription(keys, _dafny.Seq("keyDescription"), d_1032_obj_)
                                    if (d_1047_valueOrError7_).IsFailure():
                                        return (d_1047_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_1048_keyDescription_ = (d_1047_valueOrError7_).Extract()
                                        d_1049_valueOrError8_ = default__.GetEncryptedDataKeys(d_1032_obj_)
                                        if (d_1049_valueOrError8_).IsFailure():
                                            return (d_1049_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_1050_encryptedDataKeys_ = (d_1049_valueOrError8_).Extract()
                                            if (d_1035_typ_) == (_dafny.Seq("positive-keyring")):
                                                d_1051_valueOrError9_ = default__.GetExpectedResult(d_1032_obj_)
                                                if (d_1051_valueOrError9_).IsFailure():
                                                    return (d_1051_valueOrError9_).PropagateFailure()
                                                elif True:
                                                    d_1052_expectedResult_ = (d_1051_valueOrError9_).Extract()
                                                    return Wrappers.Result_Success(TestVectors.DecryptTestVector_PositiveDecryptKeyringTest(name, d_1043_algorithmSuite_, d_1046_commitmentPolicy_, d_1050_encryptedDataKeys_, d_1041_encryptionContext_, d_1048_keyDescription_, d_1052_expectedResult_, d_1037_description_, d_1045_reproducedEncryptionContext_))
                                            elif (d_1035_typ_) == (_dafny.Seq("negative-keyring")):
                                                d_1053_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_1032_obj_)
                                                if (d_1053_valueOrError10_).IsFailure():
                                                    return (d_1053_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_1054_errorDescription_ = (d_1053_valueOrError10_).Extract()
                                                    return Wrappers.Result_Success(TestVectors.DecryptTestVector_NegativeDecryptKeyringTest(name, d_1043_algorithmSuite_, d_1046_commitmentPolicy_, d_1050_encryptedDataKeys_, d_1041_encryptionContext_, d_1054_errorDescription_, d_1048_keyDescription_, d_1045_reproducedEncryptionContext_, d_1037_description_))
                                            elif True:
                                                return Wrappers.Result_Failure((_dafny.Seq("Unsupported DecryptTestVector type:")) + (d_1035_typ_))

