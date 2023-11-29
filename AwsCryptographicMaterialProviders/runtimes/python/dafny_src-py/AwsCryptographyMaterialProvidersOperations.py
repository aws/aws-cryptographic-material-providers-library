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
import software_amazon_cryptography_keystore_internaldafny
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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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

assert "AwsCryptographyMaterialProvidersOperations" == __name__
AwsCryptographyMaterialProvidersOperations = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAwsKmsKeyring(config, input):
        output: Wrappers.Result = None
        d_1303___v0_: tuple
        d_1304_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1304_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1304_valueOrError0_).IsFailure():
            output = (d_1304_valueOrError0_).PropagateFailure()
            return output
        d_1303___v0_ = (d_1304_valueOrError0_).Extract()
        d_1305_grantTokens_: _dafny.Seq
        d_1306_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1306_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1306_valueOrError1_).IsFailure():
            output = (d_1306_valueOrError1_).PropagateFailure()
            return output
        d_1305_grantTokens_ = (d_1306_valueOrError1_).Extract()
        d_1307_keyring_: AwsKmsKeyring.AwsKmsKeyring
        nw53_ = AwsKmsKeyring.AwsKmsKeyring()
        nw53_.ctor__((input).kmsClient, (input).kmsKeyId, d_1305_grantTokens_)
        d_1307_keyring_ = nw53_
        output = Wrappers.Result_Success(d_1307_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1308___v1_: tuple
            d_1309_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            d_1309_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1309_valueOrError0_).IsFailure():
                output = (d_1309_valueOrError0_).PropagateFailure()
                return output
            d_1308___v1_ = (d_1309_valueOrError0_).Extract()
        d_1310_grantTokens_: _dafny.Seq
        d_1311_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1311_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1311_valueOrError1_).IsFailure():
            output = (d_1311_valueOrError1_).PropagateFailure()
            return output
        d_1310_grantTokens_ = (d_1311_valueOrError1_).Extract()
        d_1312_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
        nw54_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
        nw54_.ctor__((input).kmsClient, (input).discoveryFilter, d_1310_grantTokens_)
        d_1312_keyring_ = nw54_
        output = Wrappers.Result_Success(d_1312_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1313_grantTokens_: _dafny.Seq
        d_1314_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1314_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1314_valueOrError0_).IsFailure():
            output = (d_1314_valueOrError0_).PropagateFailure()
            return output
        d_1313_grantTokens_ = (d_1314_valueOrError0_).Extract()
        if ((input).clientSupplier).is_Some:
            out272_: Wrappers.Result
            out272_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, ((input).clientSupplier).value, Wrappers.Option_Some(d_1313_grantTokens_))
            output = out272_
        elif True:
            d_1315_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
            d_1316_valueOrError1_: Wrappers.Result = None
            out273_: Wrappers.Result
            out273_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1316_valueOrError1_ = out273_
            if (d_1316_valueOrError1_).IsFailure():
                output = (d_1316_valueOrError1_).PropagateFailure()
                return output
            d_1315_clientSupplier_ = (d_1316_valueOrError1_).Extract()
            out274_: Wrappers.Result
            out274_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1315_clientSupplier_, Wrappers.Option_Some(d_1313_grantTokens_))
            output = out274_
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1317_grantTokens_: _dafny.Seq
        d_1318_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1318_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1318_valueOrError0_).IsFailure():
            output = (d_1318_valueOrError0_).PropagateFailure()
            return output
        d_1317_grantTokens_ = (d_1318_valueOrError0_).Extract()
        d_1319_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1320_valueOrError1_: Wrappers.Result = None
            out275_: Wrappers.Result
            out275_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1320_valueOrError1_ = out275_
            if (d_1320_valueOrError1_).IsFailure():
                output = (d_1320_valueOrError1_).PropagateFailure()
                return output
            d_1319_clientSupplier_ = (d_1320_valueOrError1_).Extract()
        elif True:
            d_1319_clientSupplier_ = ((input).clientSupplier).value
        out276_: Wrappers.Result
        out276_ = DiscoveryMultiKeyring.default__.DiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1319_clientSupplier_, Wrappers.Option_Some(d_1317_grantTokens_))
        output = out276_
        return output

    @staticmethod
    def CreateAwsKmsMrkKeyring(config, input):
        output: Wrappers.Result = None
        d_1321___v2_: tuple
        d_1322_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1322_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1322_valueOrError0_).IsFailure():
            output = (d_1322_valueOrError0_).PropagateFailure()
            return output
        d_1321___v2_ = (d_1322_valueOrError0_).Extract()
        d_1323_grantTokens_: _dafny.Seq
        d_1324_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1324_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1324_valueOrError1_).IsFailure():
            output = (d_1324_valueOrError1_).PropagateFailure()
            return output
        d_1323_grantTokens_ = (d_1324_valueOrError1_).Extract()
        d_1325_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
        nw55_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
        nw55_.ctor__((input).kmsClient, (input).kmsKeyId, d_1323_grantTokens_)
        d_1325_keyring_ = nw55_
        output = Wrappers.Result_Success(d_1325_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1326_grantTokens_: _dafny.Seq
        d_1327_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1327_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1327_valueOrError0_).IsFailure():
            output = (d_1327_valueOrError0_).PropagateFailure()
            return output
        d_1326_grantTokens_ = (d_1327_valueOrError0_).Extract()
        d_1328_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1329_valueOrError1_: Wrappers.Result = None
            out277_: Wrappers.Result
            out277_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1329_valueOrError1_ = out277_
            if (d_1329_valueOrError1_).IsFailure():
                output = (d_1329_valueOrError1_).PropagateFailure()
                return output
            d_1328_clientSupplier_ = (d_1329_valueOrError1_).Extract()
        elif True:
            d_1328_clientSupplier_ = ((input).clientSupplier).value
        out278_: Wrappers.Result
        out278_ = MrkAwareStrictMultiKeyring.default__.MrkAwareStrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1328_clientSupplier_, Wrappers.Option_Some(d_1326_grantTokens_))
        output = out278_
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1330___v3_: tuple
            d_1331_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            d_1331_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1331_valueOrError0_).IsFailure():
                output = (d_1331_valueOrError0_).PropagateFailure()
                return output
            d_1330___v3_ = (d_1331_valueOrError0_).Extract()
        d_1332_regionMatch_: Wrappers.Option
        d_1332_regionMatch_ = software_amazon_cryptography_services_kms_internaldafny.default__.RegionMatch((input).kmsClient, (input).region)
        d_1333_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1333_valueOrError1_ = Wrappers.default__.Need((d_1332_regionMatch_) != (Wrappers.Option_Some(False)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Provided client and region do not match")))
        if (d_1333_valueOrError1_).IsFailure():
            output = (d_1333_valueOrError1_).PropagateFailure()
            return output
        d_1334_grantTokens_: _dafny.Seq
        d_1335_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1335_valueOrError2_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1335_valueOrError2_).IsFailure():
            output = (d_1335_valueOrError2_).PropagateFailure()
            return output
        d_1334_grantTokens_ = (d_1335_valueOrError2_).Extract()
        d_1336_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
        nw56_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
        nw56_.ctor__((input).kmsClient, (input).region, (input).discoveryFilter, d_1334_grantTokens_)
        d_1336_keyring_ = nw56_
        output = Wrappers.Result_Success(d_1336_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1337_grantTokens_: _dafny.Seq
        d_1338_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1338_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1338_valueOrError0_).IsFailure():
            output = (d_1338_valueOrError0_).PropagateFailure()
            return output
        d_1337_grantTokens_ = (d_1338_valueOrError0_).Extract()
        d_1339_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1340_valueOrError1_: Wrappers.Result = None
            out279_: Wrappers.Result
            out279_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1340_valueOrError1_ = out279_
            if (d_1340_valueOrError1_).IsFailure():
                output = (d_1340_valueOrError1_).PropagateFailure()
                return output
            d_1339_clientSupplier_ = (d_1340_valueOrError1_).Extract()
        elif True:
            d_1339_clientSupplier_ = ((input).clientSupplier).value
        out280_: Wrappers.Result
        out280_ = MrkAwareDiscoveryMultiKeyring.default__.MrkAwareDiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1339_clientSupplier_, Wrappers.Option_Some(d_1337_grantTokens_))
        output = out280_
        return output

    @staticmethod
    def CreateAwsKmsHierarchicalKeyring(config, input):
        output: Wrappers.Result = None
        d_1341_maxCacheSize_: BoundedInts.int32 = int(0)
        d_1342_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.CacheType
        d_1342_cache_ = (((input).cache).value if ((input).cache).is_Some else software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_Default(software_amazon_cryptography_materialproviders_internaldafny_types.DefaultCache_DefaultCache(1000)))
        d_1343_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1343_valueOrError0_ = Wrappers.default__.Need((((input).branchKeyId).is_None) or (((input).branchKeyIdSupplier).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")))
        if (d_1343_valueOrError0_).IsFailure():
            output = (d_1343_valueOrError0_).PropagateFailure()
            return output
        d_1344_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1344_valueOrError1_ = Wrappers.default__.Need((((input).branchKeyId).is_Some) or (((input).branchKeyIdSupplier).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")))
        if (d_1344_valueOrError1_).IsFailure():
            output = (d_1344_valueOrError1_).PropagateFailure()
            return output
        d_1345_cmc_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache
        d_1346_valueOrError2_: Wrappers.Result = None
        out281_: Wrappers.Result
        out281_ = AwsCryptographyMaterialProvidersOperations.default__.CreateCryptographicMaterialsCache(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(d_1342_cache_))
        d_1346_valueOrError2_ = out281_
        if (d_1346_valueOrError2_).IsFailure():
            output = (d_1346_valueOrError2_).PropagateFailure()
            return output
        d_1345_cmc_ = (d_1346_valueOrError2_).Extract()
        d_1347_keyring_: AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
        nw57_ = AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring()
        nw57_.ctor__((input).keyStore, (input).branchKeyId, (input).branchKeyIdSupplier, (input).ttlSeconds, d_1345_cmc_, (config).crypto)
        d_1347_keyring_ = nw57_
        output = Wrappers.Result_Success(d_1347_keyring_)
        return output
        return output

    @staticmethod
    def CreateMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1348_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1348_valueOrError0_ = Wrappers.default__.Need((((input).generator).is_Some) or ((len((input).childKeyrings)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must include a generator keyring and/or at least one child keyring")))
        if (d_1348_valueOrError0_).IsFailure():
            output = (d_1348_valueOrError0_).PropagateFailure()
            return output
        d_1349_keyring_: MultiKeyring.MultiKeyring
        nw58_ = MultiKeyring.MultiKeyring()
        nw58_.ctor__((input).generator, (input).childKeyrings)
        d_1349_keyring_ = nw58_
        output = Wrappers.Result_Success(d_1349_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawAesKeyring(config, input):
        output: Wrappers.Result = None
        d_1350_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1350_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1350_valueOrError0_).IsFailure():
            output = (d_1350_valueOrError0_).PropagateFailure()
            return output
        d_1351_wrappingAlg_: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM
        def lambda100_(source36_):
            if source36_.is_ALG__AES128__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(16, 16, 12)
            elif source36_.is_ALG__AES192__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(24, 16, 12)
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12)

        d_1351_wrappingAlg_ = lambda100_((input).wrappingAlg)
        d_1352_namespaceAndName_: tuple
        d_1353_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1353_valueOrError1_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1353_valueOrError1_).IsFailure():
            output = (d_1353_valueOrError1_).PropagateFailure()
            return output
        d_1352_namespaceAndName_ = (d_1353_valueOrError1_).Extract()
        let_tmp_rhs11_ = d_1352_namespaceAndName_
        d_1354_namespace_ = let_tmp_rhs11_[0]
        d_1355_name_ = let_tmp_rhs11_[1]
        d_1356_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1356_valueOrError2_ = Wrappers.default__.Need((((len((input).wrappingKey)) == (16)) or ((len((input).wrappingKey)) == (24))) or ((len((input).wrappingKey)) == (32)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid wrapping key length")))
        if (d_1356_valueOrError2_).IsFailure():
            output = (d_1356_valueOrError2_).PropagateFailure()
            return output
        d_1357_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1357_valueOrError3_ = Wrappers.default__.Need((len((input).wrappingKey)) == ((d_1351_wrappingAlg_).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrapping key length does not match specified wrapping algorithm")))
        if (d_1357_valueOrError3_).IsFailure():
            output = (d_1357_valueOrError3_).PropagateFailure()
            return output
        d_1358_keyring_: RawAESKeyring.RawAESKeyring
        nw59_ = RawAESKeyring.RawAESKeyring()
        nw59_.ctor__(d_1354_namespace_, d_1355_name_, (input).wrappingKey, d_1351_wrappingAlg_, (config).crypto)
        d_1358_keyring_ = nw59_
        output = Wrappers.Result_Success(d_1358_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1359_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1359_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1359_valueOrError0_).IsFailure():
            output = (d_1359_valueOrError0_).PropagateFailure()
            return output
        d_1360_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1360_valueOrError1_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).privateKey).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a privateKey is required")))
        if (d_1360_valueOrError1_).IsFailure():
            output = (d_1360_valueOrError1_).PropagateFailure()
            return output
        d_1361_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
        def lambda101_(source37_):
            if source37_.is_PKCS1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_PKCS1()
            elif source37_.is_OAEP__SHA1__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA1()
            elif source37_.is_OAEP__SHA256__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA256()
            elif source37_.is_OAEP__SHA384__MGF1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA384()
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA512()

        d_1361_padding_ = lambda101_((input).paddingScheme)
        d_1362_namespaceAndName_: tuple
        d_1363_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1363_valueOrError2_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1363_valueOrError2_).IsFailure():
            output = (d_1363_valueOrError2_).PropagateFailure()
            return output
        d_1362_namespaceAndName_ = (d_1363_valueOrError2_).Extract()
        let_tmp_rhs12_ = d_1362_namespaceAndName_
        d_1364_namespace_ = let_tmp_rhs12_[0]
        d_1365_name_ = let_tmp_rhs12_[1]
        d_1366_keyring_: RawRSAKeyring.RawRSAKeyring
        nw60_ = RawRSAKeyring.RawRSAKeyring()
        nw60_.ctor__(d_1364_namespace_, d_1365_name_, (input).publicKey, (input).privateKey, d_1361_padding_, (config).crypto)
        d_1366_keyring_ = nw60_
        output = Wrappers.Result_Success(d_1366_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1367_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1367_valueOrError0_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).kmsClient).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a kmsClient is required")))
        if (d_1367_valueOrError0_).IsFailure():
            output = (d_1367_valueOrError0_).PropagateFailure()
            return output
        d_1368_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1368_valueOrError1_ = Wrappers.default__.Need((((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__1) or (((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__256), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unsupported EncryptionAlgorithmSpec")))
        if (d_1368_valueOrError1_).IsFailure():
            output = (d_1368_valueOrError1_).PropagateFailure()
            return output
        d_1369_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1369_valueOrError2_ = Wrappers.default__.Need((software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__KeyIdType((input).kmsKeyId)) and ((AwsArnParsing.default__.ParseAwsKmsArn((input).kmsKeyId)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Kms Key ID must be a KMS Key ARN")))
        if (d_1369_valueOrError2_).IsFailure():
            output = (d_1369_valueOrError2_).PropagateFailure()
            return output
        if ((input).publicKey).is_Some:
            d_1370_lengthOutputRes_: Wrappers.Result
            d_1370_lengthOutputRes_ = ((config).crypto).GetRSAKeyModulusLength(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(((input).publicKey).value))
            d_1371_lengthOutput_: software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput
            d_1372_valueOrError3_: Wrappers.Result = None
            def lambda102_(d_1373_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1373_e_)

            d_1372_valueOrError3_ = (d_1370_lengthOutputRes_).MapFailure(lambda102_)
            if (d_1372_valueOrError3_).IsFailure():
                output = (d_1372_valueOrError3_).PropagateFailure()
                return output
            d_1371_lengthOutput_ = (d_1372_valueOrError3_).Extract()
            d_1374_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1374_valueOrError4_ = Wrappers.default__.Need(((d_1371_lengthOutput_).length) >= ((AwsKmsRsaKeyring.default__).MIN__KMS__RSA__KEY__LEN), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid public key length")))
            if (d_1374_valueOrError4_).IsFailure():
                output = (d_1374_valueOrError4_).PropagateFailure()
                return output
        d_1375___v4_: tuple
        d_1376_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1376_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1376_valueOrError5_).IsFailure():
            output = (d_1376_valueOrError5_).PropagateFailure()
            return output
        d_1375___v4_ = (d_1376_valueOrError5_).Extract()
        d_1377_grantTokens_: _dafny.Seq
        d_1378_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1378_valueOrError6_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1378_valueOrError6_).IsFailure():
            output = (d_1378_valueOrError6_).PropagateFailure()
            return output
        d_1377_grantTokens_ = (d_1378_valueOrError6_).Extract()
        d_1379_keyring_: AwsKmsRsaKeyring.AwsKmsRsaKeyring
        nw61_ = AwsKmsRsaKeyring.AwsKmsRsaKeyring()
        nw61_.ctor__((input).publicKey, (input).kmsKeyId, (input).encryptionAlgorithm, (input).kmsClient, (config).crypto, d_1377_grantTokens_)
        d_1379_keyring_ = nw61_
        output = Wrappers.Result_Success(d_1379_keyring_)
        return output
        return output

    @staticmethod
    def CreateDefaultCryptographicMaterialsManager(config, input):
        output: Wrappers.Result = None
        d_1380_cmm_: DefaultCMM.DefaultCMM
        nw62_ = DefaultCMM.DefaultCMM()
        nw62_.OfKeyring((input).keyring, (config).crypto)
        d_1380_cmm_ = nw62_
        output = Wrappers.Result_Success(d_1380_cmm_)
        return output
        return output

    @staticmethod
    def CmpError(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def CreateRequiredEncryptionContextCMM(config, input):
        output: Wrappers.Result = None
        d_1381_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1381_valueOrError0_ = Wrappers.default__.Need((((input).underlyingCMM).is_Some) and (((input).keyring).is_None), AwsCryptographyMaterialProvidersOperations.default__.CmpError(_dafny.Seq("CreateRequiredEncryptionContextCMM currently only supports cmm.")))
        if (d_1381_valueOrError0_).IsFailure():
            output = (d_1381_valueOrError0_).PropagateFailure()
            return output
        d_1382_keySet_: _dafny.Set
        def iife56_():
            coll10_ = _dafny.Set()
            compr_10_: _dafny.Seq
            for compr_10_ in ((input).requiredEncryptionContextKeys).Elements:
                d_1383_k_: _dafny.Seq = compr_10_
                if (d_1383_k_) in ((input).requiredEncryptionContextKeys):
                    coll10_ = coll10_.union(_dafny.Set([d_1383_k_]))
            return _dafny.Set(coll10_)
        d_1382_keySet_ = iife56_()
        
        d_1384_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1384_valueOrError1_ = Wrappers.default__.Need((0) < (len(d_1382_keySet_)), AwsCryptographyMaterialProvidersOperations.default__.CmpError(_dafny.Seq("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")))
        if (d_1384_valueOrError1_).IsFailure():
            output = (d_1384_valueOrError1_).PropagateFailure()
            return output
        d_1385_cmm_: RequiredEncryptionContextCMM.RequiredEncryptionContextCMM
        nw63_ = RequiredEncryptionContextCMM.RequiredEncryptionContextCMM()
        nw63_.ctor__(((input).underlyingCMM).value, d_1382_keySet_)
        d_1385_cmm_ = nw63_
        output = Wrappers.Result_Success(d_1385_cmm_)
        return output
        return output

    @staticmethod
    def CreateCryptographicMaterialsCache(config, input):
        output: Wrappers.Result = None
        source38_ = (input).cache
        if source38_.is_Default:
            d_1386___mcc_h0_ = source38_.Default
            d_1387_c_ = d_1386___mcc_h0_
            pat_let_tv37_ = d_1387_c_
            d_1388_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache
            def iife57_(_pat_let23_0):
                def iife58_(d_1389_dt__update__tmp_h0_):
                    def iife59_(_pat_let24_0):
                        def iife60_(d_1390_dt__update_hentryCapacity_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache(d_1390_dt__update_hentryCapacity_h0_, (d_1389_dt__update__tmp_h0_).entryPruningTailSize, (d_1389_dt__update__tmp_h0_).gracePeriod, (d_1389_dt__update__tmp_h0_).graceInterval, (d_1389_dt__update__tmp_h0_).fanOut, (d_1389_dt__update__tmp_h0_).inFlightTTL, (d_1389_dt__update__tmp_h0_).sleepMilli)
                        return iife60_(_pat_let24_0)
                    return iife59_((pat_let_tv37_).entryCapacity)
                return iife58_(_pat_let23_0)
            d_1388_cache_ = iife57_(StormTracker.default__.DefaultStorm())
            d_1391_cmc_: StormTracker.StormTracker
            nw64_ = StormTracker.StormTracker()
            nw64_.ctor__(d_1388_cache_)
            d_1391_cmc_ = nw64_
            d_1392_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw65_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1391_cmc_)
            d_1392_synCmc_ = nw65_
            output = Wrappers.Result_Success(d_1392_synCmc_)
            return output
        elif source38_.is_No:
            d_1393___mcc_h1_ = source38_.No
            d_1394_cmc_: LocalCMC.LocalCMC
            nw66_ = LocalCMC.LocalCMC()
            nw66_.ctor__(0, 1)
            d_1394_cmc_ = nw66_
            output = Wrappers.Result_Success(d_1394_cmc_)
            return output
        elif source38_.is_SingleThreaded:
            d_1395___mcc_h2_ = source38_.SingleThreaded
            d_1396_c_ = d_1395___mcc_h2_
            d_1397_cmc_: LocalCMC.LocalCMC
            nw67_ = LocalCMC.LocalCMC()
            nw67_.ctor__((d_1396_c_).entryCapacity, (AwsCryptographyMaterialProvidersOperations.default__.OptionalCountingNumber((d_1396_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1397_cmc_ = nw67_
            output = Wrappers.Result_Success(d_1397_cmc_)
            return output
        elif source38_.is_MultiThreaded:
            d_1398___mcc_h3_ = source38_.MultiThreaded
            d_1399_c_ = d_1398___mcc_h3_
            d_1400_cmc_: LocalCMC.LocalCMC
            nw68_ = LocalCMC.LocalCMC()
            nw68_.ctor__((d_1399_c_).entryCapacity, (AwsCryptographyMaterialProvidersOperations.default__.OptionalCountingNumber((d_1399_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1400_cmc_ = nw68_
            d_1401_synCmc_: software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC
            nw69_ = software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC(d_1400_cmc_)
            d_1401_synCmc_ = nw69_
            output = Wrappers.Result_Success(d_1401_synCmc_)
            return output
        elif True:
            d_1402___mcc_h4_ = source38_.StormTracking
            d_1403_c_ = d_1402___mcc_h4_
            pat_let_tv38_ = d_1403_c_
            d_1404_cmc_: StormTracker.StormTracker
            nw70_ = StormTracker.StormTracker()
            def iife61_(_pat_let25_0):
                def iife62_(d_1405_dt__update__tmp_h1_):
                    def iife63_(_pat_let26_0):
                        def iife64_(d_1406_dt__update_hentryPruningTailSize_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_1405_dt__update__tmp_h1_).entryCapacity, d_1406_dt__update_hentryPruningTailSize_h0_, (d_1405_dt__update__tmp_h1_).gracePeriod, (d_1405_dt__update__tmp_h1_).graceInterval, (d_1405_dt__update__tmp_h1_).fanOut, (d_1405_dt__update__tmp_h1_).inFlightTTL, (d_1405_dt__update__tmp_h1_).sleepMilli)
                        return iife64_(_pat_let26_0)
                    return iife63_(AwsCryptographyMaterialProvidersOperations.default__.OptionalCountingNumber((pat_let_tv38_).entryPruningTailSize))
                return iife62_(_pat_let25_0)
            nw70_.ctor__(iife61_(d_1403_c_))
            d_1404_cmc_ = nw70_
            d_1407_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw71_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1404_cmc_)
            d_1407_synCmc_ = nw71_
            output = Wrappers.Result_Success(d_1407_synCmc_)
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
        d_1408_clientSupplier_: DefaultClientSupplier.DefaultClientSupplier
        nw72_ = DefaultClientSupplier.DefaultClientSupplier()
        nw72_.ctor__()
        d_1408_clientSupplier_ = nw72_
        output = Wrappers.Result_Success(d_1408_clientSupplier_)
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
        d_1409_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Invalid Encryption Materials Transition")))
        if (d_1409_valueOrError0_).IsFailure():
            return (d_1409_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidDecryptionMaterialsTransition(config, input):
        d_1410_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Invalid Decryption Materials Transition")))
        if (d_1410_valueOrError0_).IsFailure():
            return (d_1410_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(config, input):
        d_1411_valueOrError0_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Encryption Materials")))
        if (d_1411_valueOrError0_).IsFailure():
            return (d_1411_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(config, input):
        d_1412_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Decryption Materials")))
        if (d_1412_valueOrError0_).IsFailure():
            return (d_1412_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def GetAlgorithmSuiteInfo(config, input):
        return AlgorithmSuites.default__.GetAlgorithmSuiteInfo(input)

    @staticmethod
    def ValidAlgorithmSuiteInfo(config, input):
        d_1413_valueOrError0_ = Wrappers.default__.Need(AlgorithmSuites.default__.AlgorithmSuite_q(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfo(_dafny.Seq("Invalid AlgorithmSuiteInfo")))
        if (d_1413_valueOrError0_).IsFailure():
            return (d_1413_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(config, input):
        d_1414_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1414_valueOrError0_).IsFailure():
            return (d_1414_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(config, input):
        d_1415_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1415_valueOrError0_).IsFailure():
            return (d_1415_valueOrError0_).PropagateFailure()
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
        return isinstance(self, AwsCryptographyMaterialProvidersOperations.Config_Config)

class Config_Config(Config, NamedTuple('Config', [('crypto', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersOperations.Config.Config({_dafny.string_of(self.crypto)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsCryptographyMaterialProvidersOperations.Config_Config) and self.crypto == __o.crypto
    def __hash__(self) -> int:
        return super().__hash__()

