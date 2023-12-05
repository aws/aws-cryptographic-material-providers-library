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

# Module: AwsCryptographyMaterialProvidersOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAwsKmsKeyring(config, input):
        output: Wrappers.Result = None
        d_1116___v0_: tuple
        d_1117_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1117_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1117_valueOrError0_).IsFailure():
            output = (d_1117_valueOrError0_).PropagateFailure()
            return output
        d_1116___v0_ = (d_1117_valueOrError0_).Extract()
        d_1118_grantTokens_: _dafny.Seq
        d_1119_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1119_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1119_valueOrError1_).IsFailure():
            output = (d_1119_valueOrError1_).PropagateFailure()
            return output
        d_1118_grantTokens_ = (d_1119_valueOrError1_).Extract()
        d_1120_keyring_: AwsKmsKeyring.AwsKmsKeyring
        nw52_ = AwsKmsKeyring.AwsKmsKeyring()
        nw52_.ctor__((input).kmsClient, (input).kmsKeyId, d_1118_grantTokens_)
        d_1120_keyring_ = nw52_
        output = Wrappers.Result_Success(d_1120_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1121___v1_: tuple
            d_1122_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1122_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1122_valueOrError0_).IsFailure():
                output = (d_1122_valueOrError0_).PropagateFailure()
                return output
            d_1121___v1_ = (d_1122_valueOrError0_).Extract()
        d_1123_grantTokens_: _dafny.Seq
        d_1124_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1124_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1124_valueOrError1_).IsFailure():
            output = (d_1124_valueOrError1_).PropagateFailure()
            return output
        d_1123_grantTokens_ = (d_1124_valueOrError1_).Extract()
        d_1125_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
        nw53_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
        nw53_.ctor__((input).kmsClient, (input).discoveryFilter, d_1123_grantTokens_)
        d_1125_keyring_ = nw53_
        output = Wrappers.Result_Success(d_1125_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1126_grantTokens_: _dafny.Seq
        d_1127_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1127_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1127_valueOrError0_).IsFailure():
            output = (d_1127_valueOrError0_).PropagateFailure()
            return output
        d_1126_grantTokens_ = (d_1127_valueOrError0_).Extract()
        if ((input).clientSupplier).is_Some:
            out228_: Wrappers.Result
            out228_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, ((input).clientSupplier).value, Wrappers.Option_Some(d_1126_grantTokens_))
            output = out228_
        elif True:
            d_1128_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
            d_1129_valueOrError1_: Wrappers.Result = None
            out229_: Wrappers.Result
            out229_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1129_valueOrError1_ = out229_
            if (d_1129_valueOrError1_).IsFailure():
                output = (d_1129_valueOrError1_).PropagateFailure()
                return output
            d_1128_clientSupplier_ = (d_1129_valueOrError1_).Extract()
            out230_: Wrappers.Result
            out230_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1128_clientSupplier_, Wrappers.Option_Some(d_1126_grantTokens_))
            output = out230_
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1130_grantTokens_: _dafny.Seq
        d_1131_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1131_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1131_valueOrError0_).IsFailure():
            output = (d_1131_valueOrError0_).PropagateFailure()
            return output
        d_1130_grantTokens_ = (d_1131_valueOrError0_).Extract()
        d_1132_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1133_valueOrError1_: Wrappers.Result = None
            out231_: Wrappers.Result
            out231_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1133_valueOrError1_ = out231_
            if (d_1133_valueOrError1_).IsFailure():
                output = (d_1133_valueOrError1_).PropagateFailure()
                return output
            d_1132_clientSupplier_ = (d_1133_valueOrError1_).Extract()
        elif True:
            d_1132_clientSupplier_ = ((input).clientSupplier).value
        out232_: Wrappers.Result
        out232_ = DiscoveryMultiKeyring.default__.DiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1132_clientSupplier_, Wrappers.Option_Some(d_1130_grantTokens_))
        output = out232_
        return output

    @staticmethod
    def CreateAwsKmsMrkKeyring(config, input):
        output: Wrappers.Result = None
        d_1134___v2_: tuple
        d_1135_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1135_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1135_valueOrError0_).IsFailure():
            output = (d_1135_valueOrError0_).PropagateFailure()
            return output
        d_1134___v2_ = (d_1135_valueOrError0_).Extract()
        d_1136_grantTokens_: _dafny.Seq
        d_1137_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1137_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1137_valueOrError1_).IsFailure():
            output = (d_1137_valueOrError1_).PropagateFailure()
            return output
        d_1136_grantTokens_ = (d_1137_valueOrError1_).Extract()
        d_1138_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
        nw54_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
        nw54_.ctor__((input).kmsClient, (input).kmsKeyId, d_1136_grantTokens_)
        d_1138_keyring_ = nw54_
        output = Wrappers.Result_Success(d_1138_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1139_grantTokens_: _dafny.Seq
        d_1140_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1140_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1140_valueOrError0_).IsFailure():
            output = (d_1140_valueOrError0_).PropagateFailure()
            return output
        d_1139_grantTokens_ = (d_1140_valueOrError0_).Extract()
        d_1141_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1142_valueOrError1_: Wrappers.Result = None
            out233_: Wrappers.Result
            out233_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1142_valueOrError1_ = out233_
            if (d_1142_valueOrError1_).IsFailure():
                output = (d_1142_valueOrError1_).PropagateFailure()
                return output
            d_1141_clientSupplier_ = (d_1142_valueOrError1_).Extract()
        elif True:
            d_1141_clientSupplier_ = ((input).clientSupplier).value
        out234_: Wrappers.Result
        out234_ = MrkAwareStrictMultiKeyring.default__.MrkAwareStrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1141_clientSupplier_, Wrappers.Option_Some(d_1139_grantTokens_))
        output = out234_
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1143___v3_: tuple
            d_1144_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1144_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1144_valueOrError0_).IsFailure():
                output = (d_1144_valueOrError0_).PropagateFailure()
                return output
            d_1143___v3_ = (d_1144_valueOrError0_).Extract()
        d_1145_regionMatch_: Wrappers.Option
        d_1145_regionMatch_ = software_amazon_cryptography_services_kms_internaldafny.default__.RegionMatch((input).kmsClient, (input).region)
        d_1146_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1146_valueOrError1_ = Wrappers.default__.Need((d_1145_regionMatch_) != (Wrappers.Option_Some(False)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Provided client and region do not match")))
        if (d_1146_valueOrError1_).IsFailure():
            output = (d_1146_valueOrError1_).PropagateFailure()
            return output
        d_1147_grantTokens_: _dafny.Seq
        d_1148_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1148_valueOrError2_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1148_valueOrError2_).IsFailure():
            output = (d_1148_valueOrError2_).PropagateFailure()
            return output
        d_1147_grantTokens_ = (d_1148_valueOrError2_).Extract()
        d_1149_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
        nw55_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
        nw55_.ctor__((input).kmsClient, (input).region, (input).discoveryFilter, d_1147_grantTokens_)
        d_1149_keyring_ = nw55_
        output = Wrappers.Result_Success(d_1149_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1150_grantTokens_: _dafny.Seq
        d_1151_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1151_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1151_valueOrError0_).IsFailure():
            output = (d_1151_valueOrError0_).PropagateFailure()
            return output
        d_1150_grantTokens_ = (d_1151_valueOrError0_).Extract()
        d_1152_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1153_valueOrError1_: Wrappers.Result = None
            out235_: Wrappers.Result
            out235_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1153_valueOrError1_ = out235_
            if (d_1153_valueOrError1_).IsFailure():
                output = (d_1153_valueOrError1_).PropagateFailure()
                return output
            d_1152_clientSupplier_ = (d_1153_valueOrError1_).Extract()
        elif True:
            d_1152_clientSupplier_ = ((input).clientSupplier).value
        out236_: Wrappers.Result
        out236_ = MrkAwareDiscoveryMultiKeyring.default__.MrkAwareDiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1152_clientSupplier_, Wrappers.Option_Some(d_1150_grantTokens_))
        output = out236_
        return output

    @staticmethod
    def CreateAwsKmsHierarchicalKeyring(config, input):
        output: Wrappers.Result = None
        d_1154_maxCacheSize_: int = int(0)
        d_1155_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.CacheType
        d_1155_cache_ = (((input).cache).value if ((input).cache).is_Some else software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_Default(software_amazon_cryptography_materialproviders_internaldafny_types.DefaultCache_DefaultCache(1000)))
        d_1156_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1156_valueOrError0_ = Wrappers.default__.Need((((input).branchKeyId).is_None) or (((input).branchKeyIdSupplier).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")))
        if (d_1156_valueOrError0_).IsFailure():
            output = (d_1156_valueOrError0_).PropagateFailure()
            return output
        d_1157_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1157_valueOrError1_ = Wrappers.default__.Need((((input).branchKeyId).is_Some) or (((input).branchKeyIdSupplier).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")))
        if (d_1157_valueOrError1_).IsFailure():
            output = (d_1157_valueOrError1_).PropagateFailure()
            return output
        d_1158_cmc_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache
        d_1159_valueOrError2_: Wrappers.Result = None
        out237_: Wrappers.Result
        out237_ = default__.CreateCryptographicMaterialsCache(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(d_1155_cache_))
        d_1159_valueOrError2_ = out237_
        if (d_1159_valueOrError2_).IsFailure():
            output = (d_1159_valueOrError2_).PropagateFailure()
            return output
        d_1158_cmc_ = (d_1159_valueOrError2_).Extract()
        d_1160_keyring_: AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
        nw56_ = AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring()
        nw56_.ctor__((input).keyStore, (input).branchKeyId, (input).branchKeyIdSupplier, (input).ttlSeconds, d_1158_cmc_, (config).crypto)
        d_1160_keyring_ = nw56_
        output = Wrappers.Result_Success(d_1160_keyring_)
        return output
        return output

    @staticmethod
    def CreateMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1161_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1161_valueOrError0_ = Wrappers.default__.Need((((input).generator).is_Some) or ((len((input).childKeyrings)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must include a generator keyring and/or at least one child keyring")))
        if (d_1161_valueOrError0_).IsFailure():
            output = (d_1161_valueOrError0_).PropagateFailure()
            return output
        d_1162_keyring_: MultiKeyring.MultiKeyring
        nw57_ = MultiKeyring.MultiKeyring()
        nw57_.ctor__((input).generator, (input).childKeyrings)
        d_1162_keyring_ = nw57_
        output = Wrappers.Result_Success(d_1162_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawAesKeyring(config, input):
        output: Wrappers.Result = None
        d_1163_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1163_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1163_valueOrError0_).IsFailure():
            output = (d_1163_valueOrError0_).PropagateFailure()
            return output
        d_1164_wrappingAlg_: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM
        def lambda78_(source34_):
            if source34_.is_ALG__AES128__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(16, 16, 12)
            elif source34_.is_ALG__AES192__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(24, 16, 12)
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12)

        d_1164_wrappingAlg_ = lambda78_((input).wrappingAlg)
        d_1165_namespaceAndName_: tuple
        d_1166_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1166_valueOrError1_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1166_valueOrError1_).IsFailure():
            output = (d_1166_valueOrError1_).PropagateFailure()
            return output
        d_1165_namespaceAndName_ = (d_1166_valueOrError1_).Extract()
        let_tmp_rhs11_ = d_1165_namespaceAndName_
        d_1167_namespace_ = let_tmp_rhs11_[0]
        d_1168_name_ = let_tmp_rhs11_[1]
        d_1169_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1169_valueOrError2_ = Wrappers.default__.Need((((len((input).wrappingKey)) == (16)) or ((len((input).wrappingKey)) == (24))) or ((len((input).wrappingKey)) == (32)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid wrapping key length")))
        if (d_1169_valueOrError2_).IsFailure():
            output = (d_1169_valueOrError2_).PropagateFailure()
            return output
        d_1170_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1170_valueOrError3_ = Wrappers.default__.Need((len((input).wrappingKey)) == ((d_1164_wrappingAlg_).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrapping key length does not match specified wrapping algorithm")))
        if (d_1170_valueOrError3_).IsFailure():
            output = (d_1170_valueOrError3_).PropagateFailure()
            return output
        d_1171_keyring_: RawAESKeyring.RawAESKeyring
        nw58_ = RawAESKeyring.RawAESKeyring()
        nw58_.ctor__(d_1167_namespace_, d_1168_name_, (input).wrappingKey, d_1164_wrappingAlg_, (config).crypto)
        d_1171_keyring_ = nw58_
        output = Wrappers.Result_Success(d_1171_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1172_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1172_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1172_valueOrError0_).IsFailure():
            output = (d_1172_valueOrError0_).PropagateFailure()
            return output
        d_1173_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1173_valueOrError1_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).privateKey).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a privateKey is required")))
        if (d_1173_valueOrError1_).IsFailure():
            output = (d_1173_valueOrError1_).PropagateFailure()
            return output
        d_1174_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
        def lambda79_(source35_):
            if source35_.is_PKCS1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_PKCS1()
            elif source35_.is_OAEP__SHA1__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA1()
            elif source35_.is_OAEP__SHA256__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA256()
            elif source35_.is_OAEP__SHA384__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA384()
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA512()

        d_1174_padding_ = lambda79_((input).paddingScheme)
        d_1175_namespaceAndName_: tuple
        d_1176_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1176_valueOrError2_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1176_valueOrError2_).IsFailure():
            output = (d_1176_valueOrError2_).PropagateFailure()
            return output
        d_1175_namespaceAndName_ = (d_1176_valueOrError2_).Extract()
        let_tmp_rhs12_ = d_1175_namespaceAndName_
        d_1177_namespace_ = let_tmp_rhs12_[0]
        d_1178_name_ = let_tmp_rhs12_[1]
        d_1179_keyring_: RawRSAKeyring.RawRSAKeyring
        nw59_ = RawRSAKeyring.RawRSAKeyring()
        nw59_.ctor__(d_1177_namespace_, d_1178_name_, (input).publicKey, (input).privateKey, d_1174_padding_, (config).crypto)
        d_1179_keyring_ = nw59_
        output = Wrappers.Result_Success(d_1179_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1180_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1180_valueOrError0_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).kmsClient).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a kmsClient is required")))
        if (d_1180_valueOrError0_).IsFailure():
            output = (d_1180_valueOrError0_).PropagateFailure()
            return output
        d_1181_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1181_valueOrError1_ = Wrappers.default__.Need((((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__1) or (((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__256), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unsupported EncryptionAlgorithmSpec")))
        if (d_1181_valueOrError1_).IsFailure():
            output = (d_1181_valueOrError1_).PropagateFailure()
            return output
        d_1182_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1182_valueOrError2_ = Wrappers.default__.Need((software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__KeyIdType((input).kmsKeyId)) and ((AwsArnParsing.default__.ParseAwsKmsArn((input).kmsKeyId)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Kms Key ID must be a KMS Key ARN")))
        if (d_1182_valueOrError2_).IsFailure():
            output = (d_1182_valueOrError2_).PropagateFailure()
            return output
        if ((input).publicKey).is_Some:
            d_1183_lengthOutputRes_: Wrappers.Result
            d_1183_lengthOutputRes_ = ((config).crypto).GetRSAKeyModulusLength(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(((input).publicKey).value))
            d_1184_lengthOutput_: software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput
            d_1185_valueOrError3_: Wrappers.Result = None
            def lambda80_(d_1186_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1186_e_)

            d_1185_valueOrError3_ = (d_1183_lengthOutputRes_).MapFailure(lambda80_)
            if (d_1185_valueOrError3_).IsFailure():
                output = (d_1185_valueOrError3_).PropagateFailure()
                return output
            d_1184_lengthOutput_ = (d_1185_valueOrError3_).Extract()
            d_1187_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_1187_valueOrError4_ = Wrappers.default__.Need(((d_1184_lengthOutput_).length) >= (AwsKmsRsaKeyring.default__.MIN__KMS__RSA__KEY__LEN), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid public key length")))
            if (d_1187_valueOrError4_).IsFailure():
                output = (d_1187_valueOrError4_).PropagateFailure()
                return output
        d_1188___v4_: tuple
        d_1189_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1189_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1189_valueOrError5_).IsFailure():
            output = (d_1189_valueOrError5_).PropagateFailure()
            return output
        d_1188___v4_ = (d_1189_valueOrError5_).Extract()
        d_1190_grantTokens_: _dafny.Seq
        d_1191_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1191_valueOrError6_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1191_valueOrError6_).IsFailure():
            output = (d_1191_valueOrError6_).PropagateFailure()
            return output
        d_1190_grantTokens_ = (d_1191_valueOrError6_).Extract()
        d_1192_keyring_: AwsKmsRsaKeyring.AwsKmsRsaKeyring
        nw60_ = AwsKmsRsaKeyring.AwsKmsRsaKeyring()
        nw60_.ctor__((input).publicKey, (input).kmsKeyId, (input).encryptionAlgorithm, (input).kmsClient, (config).crypto, d_1190_grantTokens_)
        d_1192_keyring_ = nw60_
        output = Wrappers.Result_Success(d_1192_keyring_)
        return output
        return output

    @staticmethod
    def CreateDefaultCryptographicMaterialsManager(config, input):
        output: Wrappers.Result = None
        d_1193_cmm_: DefaultCMM.DefaultCMM
        nw61_ = DefaultCMM.DefaultCMM()
        nw61_.OfKeyring((input).keyring, (config).crypto)
        d_1193_cmm_ = nw61_
        output = Wrappers.Result_Success(d_1193_cmm_)
        return output
        return output

    @staticmethod
    def CmpError(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def CreateRequiredEncryptionContextCMM(config, input):
        output: Wrappers.Result = None
        d_1194_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1194_valueOrError0_ = Wrappers.default__.Need((((input).underlyingCMM).is_Some) and (((input).keyring).is_None), default__.CmpError(_dafny.Seq("CreateRequiredEncryptionContextCMM currently only supports cmm.")))
        if (d_1194_valueOrError0_).IsFailure():
            output = (d_1194_valueOrError0_).PropagateFailure()
            return output
        d_1195_keySet_: _dafny.Set
        def iife23_():
            coll3_ = _dafny.Set()
            compr_3_: _dafny.Seq
            for compr_3_ in ((input).requiredEncryptionContextKeys).Elements:
                d_1196_k_: _dafny.Seq = compr_3_
                if (d_1196_k_) in ((input).requiredEncryptionContextKeys):
                    coll3_ = coll3_.union(_dafny.Set([d_1196_k_]))
            return _dafny.Set(coll3_)
        d_1195_keySet_ = iife23_()
        
        d_1197_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1197_valueOrError1_ = Wrappers.default__.Need((0) < (len(d_1195_keySet_)), default__.CmpError(_dafny.Seq("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")))
        if (d_1197_valueOrError1_).IsFailure():
            output = (d_1197_valueOrError1_).PropagateFailure()
            return output
        d_1198_cmm_: RequiredEncryptionContextCMM.RequiredEncryptionContextCMM
        nw62_ = RequiredEncryptionContextCMM.RequiredEncryptionContextCMM()
        nw62_.ctor__(((input).underlyingCMM).value, d_1195_keySet_)
        d_1198_cmm_ = nw62_
        output = Wrappers.Result_Success(d_1198_cmm_)
        return output
        return output

    @staticmethod
    def CreateCryptographicMaterialsCache(config, input):
        output: Wrappers.Result = None
        source36_ = (input).cache
        if source36_.is_Default:
            d_1199___mcc_h0_ = source36_.Default
            d_1200_c_ = d_1199___mcc_h0_
            pat_let_tv162_ = d_1200_c_
            d_1201_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache
            def iife24_(_pat_let10_0):
                def iife25_(d_1202_dt__update__tmp_h0_):
                    def iife26_(_pat_let11_0):
                        def iife27_(d_1203_dt__update_hentryCapacity_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache(d_1203_dt__update_hentryCapacity_h0_, (d_1202_dt__update__tmp_h0_).entryPruningTailSize, (d_1202_dt__update__tmp_h0_).gracePeriod, (d_1202_dt__update__tmp_h0_).graceInterval, (d_1202_dt__update__tmp_h0_).fanOut, (d_1202_dt__update__tmp_h0_).inFlightTTL, (d_1202_dt__update__tmp_h0_).sleepMilli)
                        return iife27_(_pat_let11_0)
                    return iife26_((pat_let_tv162_).entryCapacity)
                return iife25_(_pat_let10_0)
            d_1201_cache_ = iife24_(StormTracker.default__.DefaultStorm())
            d_1204_cmc_: StormTracker.StormTracker
            nw63_ = StormTracker.StormTracker()
            nw63_.ctor__(d_1201_cache_)
            d_1204_cmc_ = nw63_
            d_1205_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw64_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1204_cmc_)
            d_1205_synCmc_ = nw64_
            output = Wrappers.Result_Success(d_1205_synCmc_)
            return output
        elif source36_.is_No:
            d_1206___mcc_h1_ = source36_.No
            d_1207_cmc_: LocalCMC.LocalCMC
            nw65_ = LocalCMC.LocalCMC()
            nw65_.ctor__(0, 1)
            d_1207_cmc_ = nw65_
            output = Wrappers.Result_Success(d_1207_cmc_)
            return output
        elif source36_.is_SingleThreaded:
            d_1208___mcc_h2_ = source36_.SingleThreaded
            d_1209_c_ = d_1208___mcc_h2_
            d_1210_cmc_: LocalCMC.LocalCMC
            nw66_ = LocalCMC.LocalCMC()
            nw66_.ctor__((d_1209_c_).entryCapacity, (default__.OptionalCountingNumber((d_1209_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1210_cmc_ = nw66_
            output = Wrappers.Result_Success(d_1210_cmc_)
            return output
        elif source36_.is_MultiThreaded:
            d_1211___mcc_h3_ = source36_.MultiThreaded
            d_1212_c_ = d_1211___mcc_h3_
            d_1213_cmc_: LocalCMC.LocalCMC
            nw67_ = LocalCMC.LocalCMC()
            nw67_.ctor__((d_1212_c_).entryCapacity, (default__.OptionalCountingNumber((d_1212_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1213_cmc_ = nw67_
            d_1214_synCmc_: software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC
            nw68_ = software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC(d_1213_cmc_)
            d_1214_synCmc_ = nw68_
            output = Wrappers.Result_Success(d_1214_synCmc_)
            return output
        elif True:
            d_1215___mcc_h4_ = source36_.StormTracking
            d_1216_c_ = d_1215___mcc_h4_
            pat_let_tv163_ = d_1216_c_
            d_1217_cmc_: StormTracker.StormTracker
            nw69_ = StormTracker.StormTracker()
            def iife28_(_pat_let12_0):
                def iife29_(d_1218_dt__update__tmp_h1_):
                    def iife30_(_pat_let13_0):
                        def iife31_(d_1219_dt__update_hentryPruningTailSize_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_1218_dt__update__tmp_h1_).entryCapacity, d_1219_dt__update_hentryPruningTailSize_h0_, (d_1218_dt__update__tmp_h1_).gracePeriod, (d_1218_dt__update__tmp_h1_).graceInterval, (d_1218_dt__update__tmp_h1_).fanOut, (d_1218_dt__update__tmp_h1_).inFlightTTL, (d_1218_dt__update__tmp_h1_).sleepMilli)
                        return iife31_(_pat_let13_0)
                    return iife30_(default__.OptionalCountingNumber((pat_let_tv163_).entryPruningTailSize))
                return iife29_(_pat_let12_0)
            nw69_.ctor__(iife28_(d_1216_c_))
            d_1217_cmc_ = nw69_
            d_1220_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw70_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1217_cmc_)
            d_1220_synCmc_ = nw70_
            output = Wrappers.Result_Success(d_1220_synCmc_)
            return output
        return output

    @staticmethod
    def OptionalCountingNumber(c):
        if ((c).is_Some) and (((c).value) <= (0)):
            return Wrappers.Option_None()
        elif True:
            return c

    @staticmethod
    def CreateDefaultClientSupplier(config, input):
        output: Wrappers.Result = None
        d_1221_clientSupplier_: DefaultClientSupplier.DefaultClientSupplier
        nw71_ = DefaultClientSupplier.DefaultClientSupplier()
        nw71_.ctor__()
        d_1221_clientSupplier_ = nw71_
        output = Wrappers.Result_Success(d_1221_clientSupplier_)
        return output
        return output

    @staticmethod
    def InitializeEncryptionMaterials(config, input):
        return Materials.default__.InitializeEncryptionMaterials(input)

    @staticmethod
    def InitializeDecryptionMaterials(config, input):
        return Materials.default__.InitializeDecryptionMaterials(input)

    @staticmethod
    def ValidEncryptionMaterialsTransition(config, input):
        d_1222_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Invalid Encryption Materials Transition")))
        if (d_1222_valueOrError0_).IsFailure():
            return (d_1222_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidDecryptionMaterialsTransition(config, input):
        d_1223_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Invalid Decryption Materials Transition")))
        if (d_1223_valueOrError0_).IsFailure():
            return (d_1223_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(config, input):
        d_1224_valueOrError0_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Encryption Materials")))
        if (d_1224_valueOrError0_).IsFailure():
            return (d_1224_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(config, input):
        d_1225_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Decryption Materials")))
        if (d_1225_valueOrError0_).IsFailure():
            return (d_1225_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def GetAlgorithmSuiteInfo(config, input):
        return AlgorithmSuites.default__.GetAlgorithmSuiteInfo(input)

    @staticmethod
    def ValidAlgorithmSuiteInfo(config, input):
        d_1226_valueOrError0_ = Wrappers.default__.Need(AlgorithmSuites.default__.AlgorithmSuite_q(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfo(_dafny.Seq("Invalid AlgorithmSuiteInfo")))
        if (d_1226_valueOrError0_).IsFailure():
            return (d_1226_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(config, input):
        d_1227_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1227_valueOrError0_).IsFailure():
            return (d_1227_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(config, input):
        d_1228_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1228_valueOrError0_).IsFailure():
            return (d_1228_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())


class Config:
    @classmethod
    def default(cls, ):
        return lambda: Config_Config(None)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Config(self) -> bool:
        return isinstance(self, Config_Config)

class Config_Config(Config, NamedTuple('Config', [('crypto', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersOperations.Config.Config({_dafny.string_of(self.crypto)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Config_Config) and self.crypto == __o.crypto
    def __hash__(self) -> int:
        return super().__hash__()

