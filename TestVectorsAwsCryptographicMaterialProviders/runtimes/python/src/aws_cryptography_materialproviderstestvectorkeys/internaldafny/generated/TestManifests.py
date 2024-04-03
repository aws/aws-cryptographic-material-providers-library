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
import ParseJsonManifests

# Module: TestManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StartEncrypt(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1057_encryptManifest_: ManifestData
        d_1058_valueOrError0_: Wrappers.Result = None
        out63_: Wrappers.Result
        out63_ = default__.GetManifest((op).manifestPath, _dafny.Seq("manifest.json"))
        d_1058_valueOrError0_ = out63_
        if (d_1058_valueOrError0_).IsFailure():
            output = (d_1058_valueOrError0_).PropagateFailure()
            return output
        d_1057_encryptManifest_ = (d_1058_valueOrError0_).Extract()
        d_1059_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1059_valueOrError1_ = Wrappers.default__.Need((d_1057_encryptManifest_).is_EncryptManifest, _dafny.Seq("Not a encrypt manifest"))
        if (d_1059_valueOrError1_).IsFailure():
            output = (d_1059_valueOrError1_).PropagateFailure()
            return output
        d_1060_encryptVectors_: _dafny.Seq
        d_1061_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1061_valueOrError2_ = ParseJsonManifests.default__.BuildEncryptTestVector((d_1057_encryptManifest_).keys, (d_1057_encryptManifest_).jsonTests)
        if (d_1061_valueOrError2_).IsFailure():
            output = (d_1061_valueOrError2_).PropagateFailure()
            return output
        d_1060_encryptVectors_ = (d_1061_valueOrError2_).Extract()
        d_1062_encryptTests_: _dafny.Seq
        d_1063_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out64_: Wrappers.Result
        out64_ = default__.ToEncryptTests((d_1057_encryptManifest_).keys, d_1060_encryptVectors_)
        d_1063_valueOrError3_ = out64_
        if (d_1063_valueOrError3_).IsFailure():
            output = (d_1063_valueOrError3_).PropagateFailure()
            return output
        d_1062_encryptTests_ = (d_1063_valueOrError3_).Extract()
        d_1064_decryptVectors_: _dafny.Seq
        out65_: _dafny.Seq
        out65_ = default__.TestEncrypts(d_1062_encryptTests_, (d_1057_encryptManifest_).keys)
        d_1064_decryptVectors_ = out65_
        d_1065___v0_: tuple
        d_1066_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out66_: Wrappers.Result
        out66_ = CompleteVectors.default__.WriteDecryptManifest(op, (d_1057_encryptManifest_).keys, d_1064_decryptVectors_)
        d_1066_valueOrError4_ = out66_
        if (d_1066_valueOrError4_).IsFailure():
            output = (d_1066_valueOrError4_).PropagateFailure()
            return output
        d_1065___v0_ = (d_1066_valueOrError4_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def TestEncrypts(tests, keys):
        output: _dafny.Seq = _dafny.Seq({})
        d_1067_hasFailure_: bool
        d_1067_hasFailure_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Encrypt Tests =================== \n\n")))
        d_1068_decryptableTests_: _dafny.Seq
        d_1068_decryptableTests_ = _dafny.Seq([])
        hi3_ = len(tests)
        for d_1069_i_ in range(0, hi3_):
            d_1070_test_: TestVectors.EncryptTest
            d_1070_test_ = (tests)[d_1069_i_]
            d_1071_pass_: bool
            d_1072_maybeEncryptionMaterials_: Wrappers.Option
            out67_: bool
            out68_: Wrappers.Option
            out67_, out68_ = TestVectors.default__.TestGetEncryptionMaterials(d_1070_test_)
            d_1071_pass_ = out67_
            d_1072_maybeEncryptionMaterials_ = out68_
            if (d_1071_pass_) and (not(((d_1070_test_).vector).is_NegativeEncryptKeyringVector)):
                d_1068_decryptableTests_ = (d_1068_decryptableTests_) + (_dafny.Seq([(d_1070_test_, (d_1072_maybeEncryptionMaterials_).value)]))
            elif not(d_1071_pass_):
                d_1067_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Encrypt Tests =================== \n\n")))
        if not(not(d_1067_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1073_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out69_: Wrappers.Result
        out69_ = default__.ToDecryptTestVectors(keys, d_1068_decryptableTests_)
        d_1073_valueOrError0_ = out69_
        if not(not((d_1073_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(75,14): " + _dafny.string_of(d_1073_valueOrError0_))
        output = (d_1073_valueOrError0_).Extract()
        return output

    @staticmethod
    def StartDecrypt(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1074_decryptManifest_: ManifestData
        d_1075_valueOrError0_: Wrappers.Result = None
        out70_: Wrappers.Result
        out70_ = default__.GetManifest((op).manifestPath, _dafny.Seq("manifest.json"))
        d_1075_valueOrError0_ = out70_
        if (d_1075_valueOrError0_).IsFailure():
            output = (d_1075_valueOrError0_).PropagateFailure()
            return output
        d_1074_decryptManifest_ = (d_1075_valueOrError0_).Extract()
        d_1076_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1076_valueOrError1_ = Wrappers.default__.Need((d_1074_decryptManifest_).is_DecryptManifest, _dafny.Seq("Not a encrypt manifest"))
        if (d_1076_valueOrError1_).IsFailure():
            output = (d_1076_valueOrError1_).PropagateFailure()
            return output
        d_1077_decryptVectors_: _dafny.Seq
        d_1078_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1078_valueOrError2_ = ParseJsonManifests.default__.BuildDecryptTestVector((d_1074_decryptManifest_).keys, (d_1074_decryptManifest_).jsonTests)
        if (d_1078_valueOrError2_).IsFailure():
            output = (d_1078_valueOrError2_).PropagateFailure()
            return output
        d_1077_decryptVectors_ = (d_1078_valueOrError2_).Extract()
        d_1079_decryptTests_: _dafny.Seq
        d_1080_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out71_: Wrappers.Result
        out71_ = default__.ToDecryptTests((d_1074_decryptManifest_).keys, d_1077_decryptVectors_)
        d_1080_valueOrError3_ = out71_
        if (d_1080_valueOrError3_).IsFailure():
            output = (d_1080_valueOrError3_).PropagateFailure()
            return output
        d_1079_decryptTests_ = (d_1080_valueOrError3_).Extract()
        default__.TestDecrypts(d_1079_decryptTests_)
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def TestDecrypts(tests):
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Decrypt Tests =================== \n\n")))
        d_1081_hasFailure_: bool
        d_1081_hasFailure_ = False
        hi4_ = len(tests)
        for d_1082_i_ in range(0, hi4_):
            d_1083_pass_: bool
            out72_: bool
            out72_ = TestVectors.default__.TestDecryptMaterials((tests)[d_1082_i_])
            d_1083_pass_ = out72_
            if not(d_1083_pass_):
                d_1081_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Decrypt Tests =================== \n\n")))
        if not(not(d_1081_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def ToEncryptTests(keys, encryptVectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1084_encryptTests_: _dafny.Seq
        d_1084_encryptTests_ = _dafny.Seq([])
        hi5_ = len(encryptVectors)
        for d_1085_i_ in range(0, hi5_):
            d_1086_test_: TestVectors.EncryptTest
            d_1087_valueOrError0_: Wrappers.Result = None
            out73_: Wrappers.Result
            out73_ = TestVectors.default__.ToEncryptTest(keys, (encryptVectors)[d_1085_i_])
            d_1087_valueOrError0_ = out73_
            if (d_1087_valueOrError0_).IsFailure():
                output = (d_1087_valueOrError0_).PropagateFailure()
                return output
            d_1086_test_ = (d_1087_valueOrError0_).Extract()
            d_1084_encryptTests_ = (d_1084_encryptTests_) + (_dafny.Seq([d_1086_test_]))
        output = Wrappers.Result_Success(d_1084_encryptTests_)
        return output
        return output

    @staticmethod
    def ToDecryptTestVectors(keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1088_successfulEncrypt_: _dafny.Seq
        def lambda106_(d_1089_r_):
            return ((((d_1089_r_)[0]).vector).is_PositiveEncryptKeyringVector) or ((((d_1089_r_)[0]).vector).is_PositiveEncryptNegativeDecryptKeyringVector)

        d_1088_successfulEncrypt_ = Seq.default__.Filter(lambda106_, tests)
        d_1090_decryptTestVectors_: _dafny.Seq
        d_1090_decryptTestVectors_ = _dafny.Seq([])
        hi6_ = len(d_1088_successfulEncrypt_)
        for d_1091_i_ in range(0, hi6_):
            d_1092_vector_: TestVectors.DecryptTestVector
            d_1092_vector_ = TestVectors.default__.EncryptTestToDecryptVector(((d_1088_successfulEncrypt_)[d_1091_i_])[0], ((d_1088_successfulEncrypt_)[d_1091_i_])[1])
            d_1090_decryptTestVectors_ = (d_1090_decryptTestVectors_) + (_dafny.Seq([d_1092_vector_]))
        output = Wrappers.Result_Success(d_1090_decryptTestVectors_)
        return output

    @staticmethod
    def ToDecryptTests(keys, vectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1093_decryptTests_: _dafny.Seq
        d_1093_decryptTests_ = _dafny.Seq([])
        hi7_ = len(vectors)
        for d_1094_i_ in range(0, hi7_):
            d_1095_test_: TestVectors.DecryptTest
            d_1096_valueOrError0_: Wrappers.Result = None
            out74_: Wrappers.Result
            out74_ = TestVectors.default__.DecryptVectorToDecryptTest(keys, (vectors)[d_1094_i_])
            d_1096_valueOrError0_ = out74_
            if (d_1096_valueOrError0_).IsFailure():
                output = (d_1096_valueOrError0_).PropagateFailure()
                return output
            d_1095_test_ = (d_1096_valueOrError0_).Extract()
            d_1093_decryptTests_ = (d_1093_decryptTests_) + (_dafny.Seq([d_1095_test_]))
        output = Wrappers.Result_Success(d_1093_decryptTests_)
        return output
        return output

    @staticmethod
    def GetManifest(manifestPath, manifestFileName):
        manifestData: Wrappers.Result = None
        d_1097_decryptManifestBv_: _dafny.Seq
        d_1098_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out75_: Wrappers.Result
        out75_ = FileIO.default__.ReadBytesFromFile((manifestPath) + (manifestFileName))
        d_1098_valueOrError0_ = out75_
        if (d_1098_valueOrError0_).IsFailure():
            manifestData = (d_1098_valueOrError0_).PropagateFailure()
            return manifestData
        d_1097_decryptManifestBv_ = (d_1098_valueOrError0_).Extract()
        d_1099_decryptManifestBytes_: _dafny.Seq
        d_1099_decryptManifestBytes_ = JSONHelpers.default__.BvToBytes(d_1097_decryptManifestBv_)
        d_1100_manifestJson_: JSON_Values.JSON
        d_1101_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
        def lambda107_(d_1102_e_):
            return (d_1102_e_).ToString()

        d_1101_valueOrError1_ = (JSON_API.default__.Deserialize(d_1099_decryptManifestBytes_)).MapFailure(lambda107_)
        if (d_1101_valueOrError1_).IsFailure():
            manifestData = (d_1101_valueOrError1_).PropagateFailure()
            return manifestData
        d_1100_manifestJson_ = (d_1101_valueOrError1_).Extract()
        d_1103_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1103_valueOrError2_ = Wrappers.default__.Need((d_1100_manifestJson_).is_Object, _dafny.Seq("Not a JSON object"))
        if (d_1103_valueOrError2_).IsFailure():
            manifestData = (d_1103_valueOrError2_).PropagateFailure()
            return manifestData
        d_1104_manifest_: _dafny.Seq
        d_1105_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1105_valueOrError3_ = JSONHelpers.default__.GetObject(_dafny.Seq("manifest"), (d_1100_manifestJson_).obj)
        if (d_1105_valueOrError3_).IsFailure():
            manifestData = (d_1105_valueOrError3_).PropagateFailure()
            return manifestData
        d_1104_manifest_ = (d_1105_valueOrError3_).Extract()
        d_1106_version_: int
        d_1107_valueOrError4_: Wrappers.Result = Wrappers.Result.default(System_.nat.default)()
        d_1107_valueOrError4_ = JSONHelpers.default__.GetNat(_dafny.Seq("version"), d_1104_manifest_)
        if (d_1107_valueOrError4_).IsFailure():
            manifestData = (d_1107_valueOrError4_).PropagateFailure()
            return manifestData
        d_1106_version_ = (d_1107_valueOrError4_).Extract()
        d_1108_typ_: _dafny.Seq
        d_1109_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1109_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("type"), d_1104_manifest_)
        if (d_1109_valueOrError5_).IsFailure():
            manifestData = (d_1109_valueOrError5_).PropagateFailure()
            return manifestData
        d_1108_typ_ = (d_1109_valueOrError5_).Extract()
        d_1110_keyManifestUri_: _dafny.Seq
        d_1111_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1111_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("keys"), (d_1100_manifestJson_).obj)
        if (d_1111_valueOrError6_).IsFailure():
            manifestData = (d_1111_valueOrError6_).PropagateFailure()
            return manifestData
        d_1110_keyManifestUri_ = (d_1111_valueOrError6_).Extract()
        d_1112_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1112_valueOrError7_ = Wrappers.default__.Need((_dafny.Seq("file://")) < (d_1110_keyManifestUri_), _dafny.Seq("Unexpected URI prefix"))
        if (d_1112_valueOrError7_).IsFailure():
            manifestData = (d_1112_valueOrError7_).PropagateFailure()
            return manifestData
        d_1113_keyManifestPath_: _dafny.Seq
        d_1113_keyManifestPath_ = (manifestPath) + (_dafny.Seq((d_1110_keyManifestUri_)[7::]))
        d_1114_keys_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny.KeyVectorsClient
        d_1115_valueOrError8_: Wrappers.Result = None
        out76_: Wrappers.Result
        out76_ = software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny.default__.KeyVectors(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyVectorsConfig_KeyVectorsConfig(d_1113_keyManifestPath_))
        d_1115_valueOrError8_ = out76_
        if not(not((d_1115_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(222,16): " + _dafny.string_of(d_1115_valueOrError8_))
        d_1114_keys_ = (d_1115_valueOrError8_).Extract()
        d_1116_jsonTests_: _dafny.Seq
        d_1117_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1117_valueOrError9_ = JSONHelpers.default__.GetObject(_dafny.Seq("tests"), (d_1100_manifestJson_).obj)
        if (d_1117_valueOrError9_).IsFailure():
            manifestData = (d_1117_valueOrError9_).PropagateFailure()
            return manifestData
        d_1116_jsonTests_ = (d_1117_valueOrError9_).Extract()
        if (d_1108_typ_) == (_dafny.Seq("awses-mpl-decrypt")):
            d_1118_client_: JSON_Values.JSON
            d_1119_valueOrError10_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
            d_1119_valueOrError10_ = JSONHelpers.default__.Get(_dafny.Seq("client"), (d_1100_manifestJson_).obj)
            if (d_1119_valueOrError10_).IsFailure():
                manifestData = (d_1119_valueOrError10_).PropagateFailure()
                return manifestData
            d_1118_client_ = (d_1119_valueOrError10_).Extract()
            manifestData = Wrappers.Result_Success(ManifestData_DecryptManifest(d_1106_version_, d_1114_keys_, d_1118_client_, d_1116_jsonTests_))
        elif (d_1108_typ_) == (_dafny.Seq("awses-mpl-encrypt")):
            manifestData = Wrappers.Result_Success(ManifestData_EncryptManifest(d_1106_version_, d_1114_keys_, d_1116_jsonTests_))
        elif True:
            manifestData = Wrappers.Result_Failure((_dafny.Seq("Unsupported manifest type:")) + (d_1108_typ_))
        return manifestData


class ManifestData:
    @classmethod
    def default(cls, ):
        return lambda: ManifestData_DecryptManifest(int(0), None, JSON_Values.JSON.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptManifest(self) -> bool:
        return isinstance(self, ManifestData_DecryptManifest)
    @property
    def is_EncryptManifest(self) -> bool:
        return isinstance(self, ManifestData_EncryptManifest)

class ManifestData_DecryptManifest(ManifestData, NamedTuple('DecryptManifest', [('version', Any), ('keys', Any), ('client', Any), ('jsonTests', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestManifests.ManifestData.DecryptManifest({_dafny.string_of(self.version)}, {_dafny.string_of(self.keys)}, {_dafny.string_of(self.client)}, {_dafny.string_of(self.jsonTests)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ManifestData_DecryptManifest) and self.version == __o.version and self.keys == __o.keys and self.client == __o.client and self.jsonTests == __o.jsonTests
    def __hash__(self) -> int:
        return super().__hash__()

class ManifestData_EncryptManifest(ManifestData, NamedTuple('EncryptManifest', [('version', Any), ('keys', Any), ('jsonTests', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestManifests.ManifestData.EncryptManifest({_dafny.string_of(self.version)}, {_dafny.string_of(self.keys)}, {_dafny.string_of(self.jsonTests)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ManifestData_EncryptManifest) and self.version == __o.version and self.keys == __o.keys and self.jsonTests == __o.jsonTests
    def __hash__(self) -> int:
        return super().__hash__()

