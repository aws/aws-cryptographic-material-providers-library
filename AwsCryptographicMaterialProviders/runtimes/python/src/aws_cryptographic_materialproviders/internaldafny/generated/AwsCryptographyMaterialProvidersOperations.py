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
import software_amazon_cryptography_primitives_internaldafny_types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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
        d_1220___v0_: tuple
        d_1221_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1221_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1221_valueOrError0_).IsFailure():
            output = (d_1221_valueOrError0_).PropagateFailure()
            return output
        d_1220___v0_ = (d_1221_valueOrError0_).Extract()
        d_1222_grantTokens_: _dafny.Seq
        d_1223_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1223_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1223_valueOrError1_).IsFailure():
            output = (d_1223_valueOrError1_).PropagateFailure()
            return output
        d_1222_grantTokens_ = (d_1223_valueOrError1_).Extract()
        d_1224_keyring_: AwsKmsKeyring.AwsKmsKeyring
        nw52_ = AwsKmsKeyring.AwsKmsKeyring()
        nw52_.ctor__((input).kmsClient, (input).kmsKeyId, d_1222_grantTokens_)
        d_1224_keyring_ = nw52_
        output = Wrappers.Result_Success(d_1224_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1225___v1_: tuple
            d_1226_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1226_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1226_valueOrError0_).IsFailure():
                output = (d_1226_valueOrError0_).PropagateFailure()
                return output
            d_1225___v1_ = (d_1226_valueOrError0_).Extract()
        d_1227_grantTokens_: _dafny.Seq
        d_1228_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1228_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1228_valueOrError1_).IsFailure():
            output = (d_1228_valueOrError1_).PropagateFailure()
            return output
        d_1227_grantTokens_ = (d_1228_valueOrError1_).Extract()
        d_1229_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
        nw53_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
        nw53_.ctor__((input).kmsClient, (input).discoveryFilter, d_1227_grantTokens_)
        d_1229_keyring_ = nw53_
        output = Wrappers.Result_Success(d_1229_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1230_grantTokens_: _dafny.Seq
        d_1231_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1231_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1231_valueOrError0_).IsFailure():
            output = (d_1231_valueOrError0_).PropagateFailure()
            return output
        d_1230_grantTokens_ = (d_1231_valueOrError0_).Extract()
        if ((input).clientSupplier).is_Some:
            out221_: Wrappers.Result
            out221_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, ((input).clientSupplier).value, Wrappers.Option_Some(d_1230_grantTokens_))
            output = out221_
        elif True:
            d_1232_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
            d_1233_valueOrError1_: Wrappers.Result = None
            out222_: Wrappers.Result
            out222_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1233_valueOrError1_ = out222_
            if (d_1233_valueOrError1_).IsFailure():
                output = (d_1233_valueOrError1_).PropagateFailure()
                return output
            d_1232_clientSupplier_ = (d_1233_valueOrError1_).Extract()
            out223_: Wrappers.Result
            out223_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1232_clientSupplier_, Wrappers.Option_Some(d_1230_grantTokens_))
            output = out223_
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1234_grantTokens_: _dafny.Seq
        d_1235_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1235_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1235_valueOrError0_).IsFailure():
            output = (d_1235_valueOrError0_).PropagateFailure()
            return output
        d_1234_grantTokens_ = (d_1235_valueOrError0_).Extract()
        d_1236_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1237_valueOrError1_: Wrappers.Result = None
            out224_: Wrappers.Result
            out224_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1237_valueOrError1_ = out224_
            if (d_1237_valueOrError1_).IsFailure():
                output = (d_1237_valueOrError1_).PropagateFailure()
                return output
            d_1236_clientSupplier_ = (d_1237_valueOrError1_).Extract()
        elif True:
            d_1236_clientSupplier_ = ((input).clientSupplier).value
        out225_: Wrappers.Result
        out225_ = DiscoveryMultiKeyring.default__.DiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1236_clientSupplier_, Wrappers.Option_Some(d_1234_grantTokens_))
        output = out225_
        return output

    @staticmethod
    def CreateAwsKmsMrkKeyring(config, input):
        output: Wrappers.Result = None
        d_1238___v2_: tuple
        d_1239_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1239_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1239_valueOrError0_).IsFailure():
            output = (d_1239_valueOrError0_).PropagateFailure()
            return output
        d_1238___v2_ = (d_1239_valueOrError0_).Extract()
        d_1240_grantTokens_: _dafny.Seq
        d_1241_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1241_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1241_valueOrError1_).IsFailure():
            output = (d_1241_valueOrError1_).PropagateFailure()
            return output
        d_1240_grantTokens_ = (d_1241_valueOrError1_).Extract()
        d_1242_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
        nw54_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
        nw54_.ctor__((input).kmsClient, (input).kmsKeyId, d_1240_grantTokens_)
        d_1242_keyring_ = nw54_
        output = Wrappers.Result_Success(d_1242_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1243_grantTokens_: _dafny.Seq
        d_1244_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1244_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1244_valueOrError0_).IsFailure():
            output = (d_1244_valueOrError0_).PropagateFailure()
            return output
        d_1243_grantTokens_ = (d_1244_valueOrError0_).Extract()
        d_1245_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1246_valueOrError1_: Wrappers.Result = None
            out226_: Wrappers.Result
            out226_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1246_valueOrError1_ = out226_
            if (d_1246_valueOrError1_).IsFailure():
                output = (d_1246_valueOrError1_).PropagateFailure()
                return output
            d_1245_clientSupplier_ = (d_1246_valueOrError1_).Extract()
        elif True:
            d_1245_clientSupplier_ = ((input).clientSupplier).value
        out227_: Wrappers.Result
        out227_ = MrkAwareStrictMultiKeyring.default__.MrkAwareStrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1245_clientSupplier_, Wrappers.Option_Some(d_1243_grantTokens_))
        output = out227_
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1247___v3_: tuple
            d_1248_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1248_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1248_valueOrError0_).IsFailure():
                output = (d_1248_valueOrError0_).PropagateFailure()
                return output
            d_1247___v3_ = (d_1248_valueOrError0_).Extract()
        d_1249_regionMatch_: Wrappers.Option
        d_1249_regionMatch_ = software_amazon_cryptography_services_kms_internaldafny.default__.RegionMatch((input).kmsClient, (input).region)
        d_1250_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1250_valueOrError1_ = Wrappers.default__.Need((d_1249_regionMatch_) != (Wrappers.Option_Some(False)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Provided client and region do not match")))
        if (d_1250_valueOrError1_).IsFailure():
            output = (d_1250_valueOrError1_).PropagateFailure()
            return output
        d_1251_grantTokens_: _dafny.Seq
        d_1252_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1252_valueOrError2_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1252_valueOrError2_).IsFailure():
            output = (d_1252_valueOrError2_).PropagateFailure()
            return output
        d_1251_grantTokens_ = (d_1252_valueOrError2_).Extract()
        d_1253_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
        nw55_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
        nw55_.ctor__((input).kmsClient, (input).region, (input).discoveryFilter, d_1251_grantTokens_)
        d_1253_keyring_ = nw55_
        output = Wrappers.Result_Success(d_1253_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1254_grantTokens_: _dafny.Seq
        d_1255_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1255_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1255_valueOrError0_).IsFailure():
            output = (d_1255_valueOrError0_).PropagateFailure()
            return output
        d_1254_grantTokens_ = (d_1255_valueOrError0_).Extract()
        d_1256_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1257_valueOrError1_: Wrappers.Result = None
            out228_: Wrappers.Result
            out228_ = default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1257_valueOrError1_ = out228_
            if (d_1257_valueOrError1_).IsFailure():
                output = (d_1257_valueOrError1_).PropagateFailure()
                return output
            d_1256_clientSupplier_ = (d_1257_valueOrError1_).Extract()
        elif True:
            d_1256_clientSupplier_ = ((input).clientSupplier).value
        out229_: Wrappers.Result
        out229_ = MrkAwareDiscoveryMultiKeyring.default__.MrkAwareDiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1256_clientSupplier_, Wrappers.Option_Some(d_1254_grantTokens_))
        output = out229_
        return output

    @staticmethod
    def CreateAwsKmsHierarchicalKeyring(config, input):
        output: Wrappers.Result = None
        d_1258_maxCacheSize_: int = int(0)
        d_1259_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.CacheType
        d_1259_cache_ = (((input).cache).value if ((input).cache).is_Some else software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_Default(software_amazon_cryptography_materialproviders_internaldafny_types.DefaultCache_DefaultCache(1000)))
        d_1260_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1260_valueOrError0_ = Wrappers.default__.Need((((input).branchKeyId).is_None) or (((input).branchKeyIdSupplier).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")))
        if (d_1260_valueOrError0_).IsFailure():
            output = (d_1260_valueOrError0_).PropagateFailure()
            return output
        d_1261_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1261_valueOrError1_ = Wrappers.default__.Need((((input).branchKeyId).is_Some) or (((input).branchKeyIdSupplier).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")))
        if (d_1261_valueOrError1_).IsFailure():
            output = (d_1261_valueOrError1_).PropagateFailure()
            return output
        d_1262_cmc_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache
        d_1263_valueOrError2_: Wrappers.Result = None
        out230_: Wrappers.Result
        out230_ = default__.CreateCryptographicMaterialsCache(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(d_1259_cache_))
        d_1263_valueOrError2_ = out230_
        if (d_1263_valueOrError2_).IsFailure():
            output = (d_1263_valueOrError2_).PropagateFailure()
            return output
        d_1262_cmc_ = (d_1263_valueOrError2_).Extract()
        d_1264_keyring_: AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
        nw56_ = AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring()
        nw56_.ctor__((input).keyStore, (input).branchKeyId, (input).branchKeyIdSupplier, (input).ttlSeconds, d_1262_cmc_, (config).crypto)
        d_1264_keyring_ = nw56_
        output = Wrappers.Result_Success(d_1264_keyring_)
        return output
        return output

    @staticmethod
    def CreateMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1265_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1265_valueOrError0_ = Wrappers.default__.Need((((input).generator).is_Some) or ((len((input).childKeyrings)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must include a generator keyring and/or at least one child keyring")))
        if (d_1265_valueOrError0_).IsFailure():
            output = (d_1265_valueOrError0_).PropagateFailure()
            return output
        d_1266_keyring_: MultiKeyring.MultiKeyring
        nw57_ = MultiKeyring.MultiKeyring()
        nw57_.ctor__((input).generator, (input).childKeyrings)
        d_1266_keyring_ = nw57_
        output = Wrappers.Result_Success(d_1266_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawAesKeyring(config, input):
        output: Wrappers.Result = None
        d_1267_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1267_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1267_valueOrError0_).IsFailure():
            output = (d_1267_valueOrError0_).PropagateFailure()
            return output
        d_1268_wrappingAlg_: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM
        def lambda100_(source32_):
            if source32_.is_ALG__AES128__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(16, 16, 12)
            elif source32_.is_ALG__AES192__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(24, 16, 12)
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12)

        d_1268_wrappingAlg_ = lambda100_((input).wrappingAlg)
        d_1269_namespaceAndName_: tuple
        d_1270_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1270_valueOrError1_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1270_valueOrError1_).IsFailure():
            output = (d_1270_valueOrError1_).PropagateFailure()
            return output
        d_1269_namespaceAndName_ = (d_1270_valueOrError1_).Extract()
        let_tmp_rhs5_ = d_1269_namespaceAndName_
        d_1271_namespace_ = let_tmp_rhs5_[0]
        d_1272_name_ = let_tmp_rhs5_[1]
        d_1273_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1273_valueOrError2_ = Wrappers.default__.Need((((len((input).wrappingKey)) == (16)) or ((len((input).wrappingKey)) == (24))) or ((len((input).wrappingKey)) == (32)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid wrapping key length")))
        if (d_1273_valueOrError2_).IsFailure():
            output = (d_1273_valueOrError2_).PropagateFailure()
            return output
        d_1274_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1274_valueOrError3_ = Wrappers.default__.Need((len((input).wrappingKey)) == ((d_1268_wrappingAlg_).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrapping key length does not match specified wrapping algorithm")))
        if (d_1274_valueOrError3_).IsFailure():
            output = (d_1274_valueOrError3_).PropagateFailure()
            return output
        d_1275_keyring_: RawAESKeyring.RawAESKeyring
        nw58_ = RawAESKeyring.RawAESKeyring()
        nw58_.ctor__(d_1271_namespace_, d_1272_name_, (input).wrappingKey, d_1268_wrappingAlg_, (config).crypto)
        d_1275_keyring_ = nw58_
        output = Wrappers.Result_Success(d_1275_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1276_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1276_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1276_valueOrError0_).IsFailure():
            output = (d_1276_valueOrError0_).PropagateFailure()
            return output
        d_1277_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1277_valueOrError1_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).privateKey).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a privateKey is required")))
        if (d_1277_valueOrError1_).IsFailure():
            output = (d_1277_valueOrError1_).PropagateFailure()
            return output
        d_1278_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
        def lambda101_(source33_):
            if source33_.is_PKCS1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_PKCS1()
            elif source33_.is_OAEP__SHA1__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA1()
            elif source33_.is_OAEP__SHA256__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA256()
            elif source33_.is_OAEP__SHA384__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA384()
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA512()

        d_1278_padding_ = lambda101_((input).paddingScheme)
        d_1279_namespaceAndName_: tuple
        d_1280_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1280_valueOrError2_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1280_valueOrError2_).IsFailure():
            output = (d_1280_valueOrError2_).PropagateFailure()
            return output
        d_1279_namespaceAndName_ = (d_1280_valueOrError2_).Extract()
        let_tmp_rhs6_ = d_1279_namespaceAndName_
        d_1281_namespace_ = let_tmp_rhs6_[0]
        d_1282_name_ = let_tmp_rhs6_[1]
        d_1283_keyring_: RawRSAKeyring.RawRSAKeyring
        nw59_ = RawRSAKeyring.RawRSAKeyring()
        nw59_.ctor__(d_1281_namespace_, d_1282_name_, (input).publicKey, (input).privateKey, d_1278_padding_, (config).crypto)
        d_1283_keyring_ = nw59_
        output = Wrappers.Result_Success(d_1283_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1284_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1284_valueOrError0_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).kmsClient).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a kmsClient is required")))
        if (d_1284_valueOrError0_).IsFailure():
            output = (d_1284_valueOrError0_).PropagateFailure()
            return output
        d_1285_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1285_valueOrError1_ = Wrappers.default__.Need((((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__1) or (((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__256), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unsupported EncryptionAlgorithmSpec")))
        if (d_1285_valueOrError1_).IsFailure():
            output = (d_1285_valueOrError1_).PropagateFailure()
            return output
        d_1286_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1286_valueOrError2_ = Wrappers.default__.Need((software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__KeyIdType((input).kmsKeyId)) and ((AwsArnParsing.default__.ParseAwsKmsArn((input).kmsKeyId)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Kms Key ID must be a KMS Key ARN")))
        if (d_1286_valueOrError2_).IsFailure():
            output = (d_1286_valueOrError2_).PropagateFailure()
            return output
        if ((input).publicKey).is_Some:
            d_1287_lengthOutputRes_: Wrappers.Result
            d_1287_lengthOutputRes_ = ((config).crypto).GetRSAKeyModulusLength(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(((input).publicKey).value))
            d_1288_lengthOutput_: software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput
            d_1289_valueOrError3_: Wrappers.Result = None
            def lambda102_(d_1290_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1290_e_)

            d_1289_valueOrError3_ = (d_1287_lengthOutputRes_).MapFailure(lambda102_)
            if (d_1289_valueOrError3_).IsFailure():
                output = (d_1289_valueOrError3_).PropagateFailure()
                return output
            d_1288_lengthOutput_ = (d_1289_valueOrError3_).Extract()
            d_1291_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_1291_valueOrError4_ = Wrappers.default__.Need(((d_1288_lengthOutput_).length) >= (AwsKmsRsaKeyring.default__.MIN__KMS__RSA__KEY__LEN), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid public key length")))
            if (d_1291_valueOrError4_).IsFailure():
                output = (d_1291_valueOrError4_).PropagateFailure()
                return output
        d_1292___v4_: tuple
        d_1293_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1293_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1293_valueOrError5_).IsFailure():
            output = (d_1293_valueOrError5_).PropagateFailure()
            return output
        d_1292___v4_ = (d_1293_valueOrError5_).Extract()
        d_1294_grantTokens_: _dafny.Seq
        d_1295_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1295_valueOrError6_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1295_valueOrError6_).IsFailure():
            output = (d_1295_valueOrError6_).PropagateFailure()
            return output
        d_1294_grantTokens_ = (d_1295_valueOrError6_).Extract()
        d_1296_keyring_: AwsKmsRsaKeyring.AwsKmsRsaKeyring
        nw60_ = AwsKmsRsaKeyring.AwsKmsRsaKeyring()
        nw60_.ctor__((input).publicKey, (input).kmsKeyId, (input).encryptionAlgorithm, (input).kmsClient, (config).crypto, d_1294_grantTokens_)
        d_1296_keyring_ = nw60_
        output = Wrappers.Result_Success(d_1296_keyring_)
        return output
        return output

    @staticmethod
    def CreateDefaultCryptographicMaterialsManager(config, input):
        output: Wrappers.Result = None
        d_1297_cmm_: DefaultCMM.DefaultCMM
        nw61_ = DefaultCMM.DefaultCMM()
        nw61_.OfKeyring((input).keyring, (config).crypto)
        d_1297_cmm_ = nw61_
        output = Wrappers.Result_Success(d_1297_cmm_)
        return output
        return output

    @staticmethod
    def CmpError(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def CreateRequiredEncryptionContextCMM(config, input):
        output: Wrappers.Result = None
        d_1298_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1298_valueOrError0_ = Wrappers.default__.Need((((input).underlyingCMM).is_Some) and (((input).keyring).is_None), default__.CmpError(_dafny.Seq("CreateRequiredEncryptionContextCMM currently only supports cmm.")))
        if (d_1298_valueOrError0_).IsFailure():
            output = (d_1298_valueOrError0_).PropagateFailure()
            return output
        d_1299_keySet_: _dafny.Set
        def iife32_():
            coll10_ = _dafny.Set()
            compr_10_: _dafny.Seq
            for compr_10_ in ((input).requiredEncryptionContextKeys).Elements:
                d_1300_k_: _dafny.Seq = compr_10_
                if UTF8.ValidUTF8Bytes._Is(d_1300_k_):
                    if (d_1300_k_) in ((input).requiredEncryptionContextKeys):
                        coll10_ = coll10_.union(_dafny.Set([d_1300_k_]))
            return _dafny.Set(coll10_)
        d_1299_keySet_ = iife32_()
        
        d_1301_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1301_valueOrError1_ = Wrappers.default__.Need((0) < (len(d_1299_keySet_)), default__.CmpError(_dafny.Seq("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")))
        if (d_1301_valueOrError1_).IsFailure():
            output = (d_1301_valueOrError1_).PropagateFailure()
            return output
        d_1302_cmm_: RequiredEncryptionContextCMM.RequiredEncryptionContextCMM
        nw62_ = RequiredEncryptionContextCMM.RequiredEncryptionContextCMM()
        nw62_.ctor__(((input).underlyingCMM).value, d_1299_keySet_)
        d_1302_cmm_ = nw62_
        output = Wrappers.Result_Success(d_1302_cmm_)
        return output
        return output

    @staticmethod
    def CreateCryptographicMaterialsCache(config, input):
        output: Wrappers.Result = None
        source34_ = (input).cache
        if source34_.is_Default:
            d_1303___mcc_h0_ = source34_.Default
            d_1304_c_ = d_1303___mcc_h0_
            pat_let_tv162_ = d_1304_c_
            d_1305_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache
            def iife33_(_pat_let11_0):
                def iife34_(d_1306_dt__update__tmp_h0_):
                    def iife35_(_pat_let12_0):
                        def iife36_(d_1307_dt__update_hentryCapacity_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache(d_1307_dt__update_hentryCapacity_h0_, (d_1306_dt__update__tmp_h0_).entryPruningTailSize, (d_1306_dt__update__tmp_h0_).gracePeriod, (d_1306_dt__update__tmp_h0_).graceInterval, (d_1306_dt__update__tmp_h0_).fanOut, (d_1306_dt__update__tmp_h0_).inFlightTTL, (d_1306_dt__update__tmp_h0_).sleepMilli)
                        return iife36_(_pat_let12_0)
                    return iife35_((pat_let_tv162_).entryCapacity)
                return iife34_(_pat_let11_0)
            d_1305_cache_ = iife33_(StormTracker.default__.DefaultStorm())
            d_1308_cmc_: StormTracker.StormTracker
            nw63_ = StormTracker.StormTracker()
            nw63_.ctor__(d_1305_cache_)
            d_1308_cmc_ = nw63_
            d_1309_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw64_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1308_cmc_)
            d_1309_synCmc_ = nw64_
            output = Wrappers.Result_Success(d_1309_synCmc_)
            return output
        elif source34_.is_No:
            d_1310___mcc_h1_ = source34_.No
            d_1311_cmc_: LocalCMC.LocalCMC
            nw65_ = LocalCMC.LocalCMC()
            nw65_.ctor__(0, 1)
            d_1311_cmc_ = nw65_
            output = Wrappers.Result_Success(d_1311_cmc_)
            return output
        elif source34_.is_SingleThreaded:
            d_1312___mcc_h2_ = source34_.SingleThreaded
            d_1313_c_ = d_1312___mcc_h2_
            d_1314_cmc_: LocalCMC.LocalCMC
            nw66_ = LocalCMC.LocalCMC()
            nw66_.ctor__((d_1313_c_).entryCapacity, (default__.OptionalCountingNumber((d_1313_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1314_cmc_ = nw66_
            output = Wrappers.Result_Success(d_1314_cmc_)
            return output
        elif source34_.is_MultiThreaded:
            d_1315___mcc_h3_ = source34_.MultiThreaded
            d_1316_c_ = d_1315___mcc_h3_
            d_1317_cmc_: LocalCMC.LocalCMC
            nw67_ = LocalCMC.LocalCMC()
            nw67_.ctor__((d_1316_c_).entryCapacity, (default__.OptionalCountingNumber((d_1316_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1317_cmc_ = nw67_
            d_1318_synCmc_: software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC
            nw68_ = software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC(d_1317_cmc_)
            d_1318_synCmc_ = nw68_
            output = Wrappers.Result_Success(d_1318_synCmc_)
            return output
        elif True:
            d_1319___mcc_h4_ = source34_.StormTracking
            d_1320_c_ = d_1319___mcc_h4_
            pat_let_tv163_ = d_1320_c_
            d_1321_cmc_: StormTracker.StormTracker
            nw69_ = StormTracker.StormTracker()
            def iife37_(_pat_let13_0):
                def iife38_(d_1322_dt__update__tmp_h1_):
                    def iife39_(_pat_let14_0):
                        def iife40_(d_1323_dt__update_hentryPruningTailSize_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_1322_dt__update__tmp_h1_).entryCapacity, d_1323_dt__update_hentryPruningTailSize_h0_, (d_1322_dt__update__tmp_h1_).gracePeriod, (d_1322_dt__update__tmp_h1_).graceInterval, (d_1322_dt__update__tmp_h1_).fanOut, (d_1322_dt__update__tmp_h1_).inFlightTTL, (d_1322_dt__update__tmp_h1_).sleepMilli)
                        return iife40_(_pat_let14_0)
                    return iife39_(default__.OptionalCountingNumber((pat_let_tv163_).entryPruningTailSize))
                return iife38_(_pat_let13_0)
            nw69_.ctor__(iife37_(d_1320_c_))
            d_1321_cmc_ = nw69_
            d_1324_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw70_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1321_cmc_)
            d_1324_synCmc_ = nw70_
            output = Wrappers.Result_Success(d_1324_synCmc_)
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
        d_1325_clientSupplier_: DefaultClientSupplier.DefaultClientSupplier
        nw71_ = DefaultClientSupplier.DefaultClientSupplier()
        nw71_.ctor__()
        d_1325_clientSupplier_ = nw71_
        output = Wrappers.Result_Success(d_1325_clientSupplier_)
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
        d_1326_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Invalid Encryption Materials Transition")))
        if (d_1326_valueOrError0_).IsFailure():
            return (d_1326_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidDecryptionMaterialsTransition(config, input):
        d_1327_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Invalid Decryption Materials Transition")))
        if (d_1327_valueOrError0_).IsFailure():
            return (d_1327_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(config, input):
        d_1328_valueOrError0_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Encryption Materials")))
        if (d_1328_valueOrError0_).IsFailure():
            return (d_1328_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(config, input):
        d_1329_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Decryption Materials")))
        if (d_1329_valueOrError0_).IsFailure():
            return (d_1329_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def GetAlgorithmSuiteInfo(config, input):
        return AlgorithmSuites.default__.GetAlgorithmSuiteInfo(input)

    @staticmethod
    def ValidAlgorithmSuiteInfo(config, input):
        d_1330_valueOrError0_ = Wrappers.default__.Need(AlgorithmSuites.default__.AlgorithmSuite_q(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfo(_dafny.Seq("Invalid AlgorithmSuiteInfo")))
        if (d_1330_valueOrError0_).IsFailure():
            return (d_1330_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(config, input):
        d_1331_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1331_valueOrError0_).IsFailure():
            return (d_1331_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(config, input):
        d_1332_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1332_valueOrError0_).IsFailure():
            return (d_1332_valueOrError0_).PropagateFailure()
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

