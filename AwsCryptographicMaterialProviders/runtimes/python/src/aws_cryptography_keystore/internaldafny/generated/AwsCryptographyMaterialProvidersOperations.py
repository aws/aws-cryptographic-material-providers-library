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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
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
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
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

# assert "AwsCryptographyMaterialProvidersOperations" == __name__
AwsCryptographyMaterialProvidersOperations = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAwsKmsKeyring(config, input):
        output: Wrappers.Result = None
        d_1502___v0_: tuple
        d_1503_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1503_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1503_valueOrError0_).IsFailure():
            output = (d_1503_valueOrError0_).PropagateFailure()
            return output
        d_1502___v0_ = (d_1503_valueOrError0_).Extract()
        d_1504_grantTokens_: _dafny.Seq
        d_1505_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1505_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1505_valueOrError1_).IsFailure():
            output = (d_1505_valueOrError1_).PropagateFailure()
            return output
        d_1504_grantTokens_ = (d_1505_valueOrError1_).Extract()
        d_1506_keyring_: AwsKmsKeyring.AwsKmsKeyring
        nw53_ = AwsKmsKeyring.AwsKmsKeyring()
        nw53_.ctor__((input).kmsClient, (input).kmsKeyId, d_1504_grantTokens_)
        d_1506_keyring_ = nw53_
        output = Wrappers.Result_Success(d_1506_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1507___v1_: tuple
            d_1508_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            d_1508_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1508_valueOrError0_).IsFailure():
                output = (d_1508_valueOrError0_).PropagateFailure()
                return output
            d_1507___v1_ = (d_1508_valueOrError0_).Extract()
        d_1509_grantTokens_: _dafny.Seq
        d_1510_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1510_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1510_valueOrError1_).IsFailure():
            output = (d_1510_valueOrError1_).PropagateFailure()
            return output
        d_1509_grantTokens_ = (d_1510_valueOrError1_).Extract()
        d_1511_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
        nw54_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
        nw54_.ctor__((input).kmsClient, (input).discoveryFilter, d_1509_grantTokens_)
        d_1511_keyring_ = nw54_
        output = Wrappers.Result_Success(d_1511_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1512_grantTokens_: _dafny.Seq
        d_1513_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1513_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1513_valueOrError0_).IsFailure():
            output = (d_1513_valueOrError0_).PropagateFailure()
            return output
        d_1512_grantTokens_ = (d_1513_valueOrError0_).Extract()
        if ((input).clientSupplier).is_Some:
            out349_: Wrappers.Result
            out349_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, ((input).clientSupplier).value, Wrappers.Option_Some(d_1512_grantTokens_))
            output = out349_
        elif True:
            d_1514_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
            d_1515_valueOrError1_: Wrappers.Result = None
            out350_: Wrappers.Result
            out350_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1515_valueOrError1_ = out350_
            if (d_1515_valueOrError1_).IsFailure():
                output = (d_1515_valueOrError1_).PropagateFailure()
                return output
            d_1514_clientSupplier_ = (d_1515_valueOrError1_).Extract()
            out351_: Wrappers.Result
            out351_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1514_clientSupplier_, Wrappers.Option_Some(d_1512_grantTokens_))
            output = out351_
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1516_grantTokens_: _dafny.Seq
        d_1517_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1517_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1517_valueOrError0_).IsFailure():
            output = (d_1517_valueOrError0_).PropagateFailure()
            return output
        d_1516_grantTokens_ = (d_1517_valueOrError0_).Extract()
        d_1518_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1519_valueOrError1_: Wrappers.Result = None
            out352_: Wrappers.Result
            out352_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1519_valueOrError1_ = out352_
            if (d_1519_valueOrError1_).IsFailure():
                output = (d_1519_valueOrError1_).PropagateFailure()
                return output
            d_1518_clientSupplier_ = (d_1519_valueOrError1_).Extract()
        elif True:
            d_1518_clientSupplier_ = ((input).clientSupplier).value
        out353_: Wrappers.Result
        out353_ = DiscoveryMultiKeyring.default__.DiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1518_clientSupplier_, Wrappers.Option_Some(d_1516_grantTokens_))
        output = out353_
        return output

    @staticmethod
    def CreateAwsKmsMrkKeyring(config, input):
        output: Wrappers.Result = None
        d_1520___v2_: tuple
        d_1521_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1521_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1521_valueOrError0_).IsFailure():
            output = (d_1521_valueOrError0_).PropagateFailure()
            return output
        d_1520___v2_ = (d_1521_valueOrError0_).Extract()
        d_1522_grantTokens_: _dafny.Seq
        d_1523_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1523_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1523_valueOrError1_).IsFailure():
            output = (d_1523_valueOrError1_).PropagateFailure()
            return output
        d_1522_grantTokens_ = (d_1523_valueOrError1_).Extract()
        d_1524_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
        nw55_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
        nw55_.ctor__((input).kmsClient, (input).kmsKeyId, d_1522_grantTokens_)
        d_1524_keyring_ = nw55_
        output = Wrappers.Result_Success(d_1524_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1525_grantTokens_: _dafny.Seq
        d_1526_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1526_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1526_valueOrError0_).IsFailure():
            output = (d_1526_valueOrError0_).PropagateFailure()
            return output
        d_1525_grantTokens_ = (d_1526_valueOrError0_).Extract()
        d_1527_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1528_valueOrError1_: Wrappers.Result = None
            out354_: Wrappers.Result
            out354_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1528_valueOrError1_ = out354_
            if (d_1528_valueOrError1_).IsFailure():
                output = (d_1528_valueOrError1_).PropagateFailure()
                return output
            d_1527_clientSupplier_ = (d_1528_valueOrError1_).Extract()
        elif True:
            d_1527_clientSupplier_ = ((input).clientSupplier).value
        out355_: Wrappers.Result
        out355_ = MrkAwareStrictMultiKeyring.default__.MrkAwareStrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1527_clientSupplier_, Wrappers.Option_Some(d_1525_grantTokens_))
        output = out355_
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1529___v3_: tuple
            d_1530_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            d_1530_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1530_valueOrError0_).IsFailure():
                output = (d_1530_valueOrError0_).PropagateFailure()
                return output
            d_1529___v3_ = (d_1530_valueOrError0_).Extract()
        d_1531_regionMatch_: Wrappers.Option
        d_1531_regionMatch_ = software_amazon_cryptography_services_kms_internaldafny.default__.RegionMatch((input).kmsClient, (input).region)
        d_1532_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1532_valueOrError1_ = Wrappers.default__.Need((d_1531_regionMatch_) != (Wrappers.Option_Some(False)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Provided client and region do not match")))
        if (d_1532_valueOrError1_).IsFailure():
            output = (d_1532_valueOrError1_).PropagateFailure()
            return output
        d_1533_grantTokens_: _dafny.Seq
        d_1534_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1534_valueOrError2_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1534_valueOrError2_).IsFailure():
            output = (d_1534_valueOrError2_).PropagateFailure()
            return output
        d_1533_grantTokens_ = (d_1534_valueOrError2_).Extract()
        d_1535_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
        nw56_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
        nw56_.ctor__((input).kmsClient, (input).region, (input).discoveryFilter, d_1533_grantTokens_)
        d_1535_keyring_ = nw56_
        output = Wrappers.Result_Success(d_1535_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1536_grantTokens_: _dafny.Seq
        d_1537_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1537_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1537_valueOrError0_).IsFailure():
            output = (d_1537_valueOrError0_).PropagateFailure()
            return output
        d_1536_grantTokens_ = (d_1537_valueOrError0_).Extract()
        d_1538_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1539_valueOrError1_: Wrappers.Result = None
            out356_: Wrappers.Result
            out356_ = AwsCryptographyMaterialProvidersOperations.default__.CreateDefaultClientSupplier(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1539_valueOrError1_ = out356_
            if (d_1539_valueOrError1_).IsFailure():
                output = (d_1539_valueOrError1_).PropagateFailure()
                return output
            d_1538_clientSupplier_ = (d_1539_valueOrError1_).Extract()
        elif True:
            d_1538_clientSupplier_ = ((input).clientSupplier).value
        out357_: Wrappers.Result
        out357_ = MrkAwareDiscoveryMultiKeyring.default__.MrkAwareDiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1538_clientSupplier_, Wrappers.Option_Some(d_1536_grantTokens_))
        output = out357_
        return output

    @staticmethod
    def CreateAwsKmsHierarchicalKeyring(config, input):
        output: Wrappers.Result = None
        d_1540_maxCacheSize_: BoundedInts.int32 = int(0)
        d_1541_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.CacheType
        d_1541_cache_ = (((input).cache).value if ((input).cache).is_Some else software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_Default(software_amazon_cryptography_materialproviders_internaldafny_types.DefaultCache_DefaultCache(1000)))
        d_1542_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1542_valueOrError0_ = Wrappers.default__.Need((((input).branchKeyId).is_None) or (((input).branchKeyIdSupplier).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")))
        if (d_1542_valueOrError0_).IsFailure():
            output = (d_1542_valueOrError0_).PropagateFailure()
            return output
        d_1543_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1543_valueOrError1_ = Wrappers.default__.Need((((input).branchKeyId).is_Some) or (((input).branchKeyIdSupplier).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")))
        if (d_1543_valueOrError1_).IsFailure():
            output = (d_1543_valueOrError1_).PropagateFailure()
            return output
        d_1544_cmc_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache
        d_1545_valueOrError2_: Wrappers.Result = None
        out358_: Wrappers.Result
        out358_ = AwsCryptographyMaterialProvidersOperations.default__.CreateCryptographicMaterialsCache(config, software_amazon_cryptography_materialproviders_internaldafny_types.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(d_1541_cache_))
        d_1545_valueOrError2_ = out358_
        if (d_1545_valueOrError2_).IsFailure():
            output = (d_1545_valueOrError2_).PropagateFailure()
            return output
        d_1544_cmc_ = (d_1545_valueOrError2_).Extract()
        d_1546_keyring_: AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
        nw57_ = AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring()
        nw57_.ctor__((input).keyStore, (input).branchKeyId, (input).branchKeyIdSupplier, (input).ttlSeconds, d_1544_cmc_, (config).crypto)
        d_1546_keyring_ = nw57_
        output = Wrappers.Result_Success(d_1546_keyring_)
        return output
        return output

    @staticmethod
    def CreateMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1547_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1547_valueOrError0_ = Wrappers.default__.Need((((input).generator).is_Some) or ((len((input).childKeyrings)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must include a generator keyring and/or at least one child keyring")))
        if (d_1547_valueOrError0_).IsFailure():
            output = (d_1547_valueOrError0_).PropagateFailure()
            return output
        d_1548_keyring_: MultiKeyring.MultiKeyring
        nw58_ = MultiKeyring.MultiKeyring()
        nw58_.ctor__((input).generator, (input).childKeyrings)
        d_1548_keyring_ = nw58_
        output = Wrappers.Result_Success(d_1548_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawAesKeyring(config, input):
        output: Wrappers.Result = None
        d_1549_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1549_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1549_valueOrError0_).IsFailure():
            output = (d_1549_valueOrError0_).PropagateFailure()
            return output
        d_1550_wrappingAlg_: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM
        def lambda101_(source36_):
            if source36_.is_ALG__AES128__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(16, 16, 12)
            elif source36_.is_ALG__AES192__GCM__IV12__TAG16:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(24, 16, 12)
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12)

        d_1550_wrappingAlg_ = lambda101_((input).wrappingAlg)
        d_1551_namespaceAndName_: tuple
        d_1552_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1552_valueOrError1_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1552_valueOrError1_).IsFailure():
            output = (d_1552_valueOrError1_).PropagateFailure()
            return output
        d_1551_namespaceAndName_ = (d_1552_valueOrError1_).Extract()
        let_tmp_rhs11_ = d_1551_namespaceAndName_
        d_1553_namespace_ = let_tmp_rhs11_[0]
        d_1554_name_ = let_tmp_rhs11_[1]
        d_1555_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1555_valueOrError2_ = Wrappers.default__.Need((((len((input).wrappingKey)) == (16)) or ((len((input).wrappingKey)) == (24))) or ((len((input).wrappingKey)) == (32)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid wrapping key length")))
        if (d_1555_valueOrError2_).IsFailure():
            output = (d_1555_valueOrError2_).PropagateFailure()
            return output
        d_1556_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1556_valueOrError3_ = Wrappers.default__.Need((len((input).wrappingKey)) == ((d_1550_wrappingAlg_).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrapping key length does not match specified wrapping algorithm")))
        if (d_1556_valueOrError3_).IsFailure():
            output = (d_1556_valueOrError3_).PropagateFailure()
            return output
        d_1557_keyring_: RawAESKeyring.RawAESKeyring
        nw59_ = RawAESKeyring.RawAESKeyring()
        nw59_.ctor__(d_1553_namespace_, d_1554_name_, (input).wrappingKey, d_1550_wrappingAlg_, (config).crypto)
        d_1557_keyring_ = nw59_
        output = Wrappers.Result_Success(d_1557_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1558_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1558_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1558_valueOrError0_).IsFailure():
            output = (d_1558_valueOrError0_).PropagateFailure()
            return output
        d_1559_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1559_valueOrError1_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).privateKey).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a privateKey is required")))
        if (d_1559_valueOrError1_).IsFailure():
            output = (d_1559_valueOrError1_).PropagateFailure()
            return output
        d_1560_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
        def lambda102_(source37_):
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

        d_1560_padding_ = lambda102_((input).paddingScheme)
        d_1561_namespaceAndName_: tuple
        d_1562_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1562_valueOrError2_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1562_valueOrError2_).IsFailure():
            output = (d_1562_valueOrError2_).PropagateFailure()
            return output
        d_1561_namespaceAndName_ = (d_1562_valueOrError2_).Extract()
        let_tmp_rhs12_ = d_1561_namespaceAndName_
        d_1563_namespace_ = let_tmp_rhs12_[0]
        d_1564_name_ = let_tmp_rhs12_[1]
        d_1565_keyring_: RawRSAKeyring.RawRSAKeyring
        nw60_ = RawRSAKeyring.RawRSAKeyring()
        nw60_.ctor__(d_1563_namespace_, d_1564_name_, (input).publicKey, (input).privateKey, d_1560_padding_, (config).crypto)
        d_1565_keyring_ = nw60_
        output = Wrappers.Result_Success(d_1565_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1566_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1566_valueOrError0_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).kmsClient).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a kmsClient is required")))
        if (d_1566_valueOrError0_).IsFailure():
            output = (d_1566_valueOrError0_).PropagateFailure()
            return output
        d_1567_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1567_valueOrError1_ = Wrappers.default__.Need((((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__1) or (((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__256), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unsupported EncryptionAlgorithmSpec")))
        if (d_1567_valueOrError1_).IsFailure():
            output = (d_1567_valueOrError1_).PropagateFailure()
            return output
        d_1568_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1568_valueOrError2_ = Wrappers.default__.Need((software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__KeyIdType((input).kmsKeyId)) and ((AwsArnParsing.default__.ParseAwsKmsArn((input).kmsKeyId)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Kms Key ID must be a KMS Key ARN")))
        if (d_1568_valueOrError2_).IsFailure():
            output = (d_1568_valueOrError2_).PropagateFailure()
            return output
        if ((input).publicKey).is_Some:
            d_1569_lengthOutputRes_: Wrappers.Result
            d_1569_lengthOutputRes_ = ((config).crypto).GetRSAKeyModulusLength(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(((input).publicKey).value))
            d_1570_lengthOutput_: software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput
            d_1571_valueOrError3_: Wrappers.Result = None
            def lambda103_(d_1572_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1572_e_)

            d_1571_valueOrError3_ = (d_1569_lengthOutputRes_).MapFailure(lambda103_)
            if (d_1571_valueOrError3_).IsFailure():
                output = (d_1571_valueOrError3_).PropagateFailure()
                return output
            d_1570_lengthOutput_ = (d_1571_valueOrError3_).Extract()
            d_1573_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1573_valueOrError4_ = Wrappers.default__.Need(((d_1570_lengthOutput_).length) >= ((AwsKmsRsaKeyring.default__).MIN__KMS__RSA__KEY__LEN), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid public key length")))
            if (d_1573_valueOrError4_).IsFailure():
                output = (d_1573_valueOrError4_).PropagateFailure()
                return output
        d_1574___v4_: tuple
        d_1575_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1575_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1575_valueOrError5_).IsFailure():
            output = (d_1575_valueOrError5_).PropagateFailure()
            return output
        d_1574___v4_ = (d_1575_valueOrError5_).Extract()
        d_1576_grantTokens_: _dafny.Seq
        d_1577_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1577_valueOrError6_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1577_valueOrError6_).IsFailure():
            output = (d_1577_valueOrError6_).PropagateFailure()
            return output
        d_1576_grantTokens_ = (d_1577_valueOrError6_).Extract()
        d_1578_keyring_: AwsKmsRsaKeyring.AwsKmsRsaKeyring
        nw61_ = AwsKmsRsaKeyring.AwsKmsRsaKeyring()
        nw61_.ctor__((input).publicKey, (input).kmsKeyId, (input).encryptionAlgorithm, (input).kmsClient, (config).crypto, d_1576_grantTokens_)
        d_1578_keyring_ = nw61_
        output = Wrappers.Result_Success(d_1578_keyring_)
        return output
        return output

    @staticmethod
    def CreateDefaultCryptographicMaterialsManager(config, input):
        output: Wrappers.Result = None
        d_1579_cmm_: DefaultCMM.DefaultCMM
        nw62_ = DefaultCMM.DefaultCMM()
        nw62_.OfKeyring((input).keyring, (config).crypto)
        d_1579_cmm_ = nw62_
        output = Wrappers.Result_Success(d_1579_cmm_)
        return output
        return output

    @staticmethod
    def CmpError(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def CreateRequiredEncryptionContextCMM(config, input):
        output: Wrappers.Result = None
        d_1580_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1580_valueOrError0_ = Wrappers.default__.Need((((input).underlyingCMM).is_Some) and (((input).keyring).is_None), AwsCryptographyMaterialProvidersOperations.default__.CmpError(_dafny.Seq("CreateRequiredEncryptionContextCMM currently only supports cmm.")))
        if (d_1580_valueOrError0_).IsFailure():
            output = (d_1580_valueOrError0_).PropagateFailure()
            return output
        d_1581_keySet_: _dafny.Set
        def iife60_():
            coll12_ = _dafny.Set()
            compr_12_: _dafny.Seq
            for compr_12_ in ((input).requiredEncryptionContextKeys).Elements:
                d_1582_k_: _dafny.Seq = compr_12_
                if (d_1582_k_) in ((input).requiredEncryptionContextKeys):
                    coll12_ = coll12_.union(_dafny.Set([d_1582_k_]))
            return _dafny.Set(coll12_)
        d_1581_keySet_ = iife60_()
        
        d_1583_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1583_valueOrError1_ = Wrappers.default__.Need((0) < (len(d_1581_keySet_)), AwsCryptographyMaterialProvidersOperations.default__.CmpError(_dafny.Seq("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")))
        if (d_1583_valueOrError1_).IsFailure():
            output = (d_1583_valueOrError1_).PropagateFailure()
            return output
        d_1584_cmm_: RequiredEncryptionContextCMM.RequiredEncryptionContextCMM
        nw63_ = RequiredEncryptionContextCMM.RequiredEncryptionContextCMM()
        nw63_.ctor__(((input).underlyingCMM).value, d_1581_keySet_)
        d_1584_cmm_ = nw63_
        output = Wrappers.Result_Success(d_1584_cmm_)
        return output
        return output

    @staticmethod
    def CreateCryptographicMaterialsCache(config, input):
        output: Wrappers.Result = None
        source38_ = (input).cache
        if source38_.is_Default:
            d_1585___mcc_h0_ = source38_.Default
            d_1586_c_ = d_1585___mcc_h0_
            pat_let_tv37_ = d_1586_c_
            d_1587_cache_: software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache
            def iife61_(_pat_let24_0):
                def iife62_(d_1588_dt__update__tmp_h0_):
                    def iife63_(_pat_let25_0):
                        def iife64_(d_1589_dt__update_hentryCapacity_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache(d_1589_dt__update_hentryCapacity_h0_, (d_1588_dt__update__tmp_h0_).entryPruningTailSize, (d_1588_dt__update__tmp_h0_).gracePeriod, (d_1588_dt__update__tmp_h0_).graceInterval, (d_1588_dt__update__tmp_h0_).fanOut, (d_1588_dt__update__tmp_h0_).inFlightTTL, (d_1588_dt__update__tmp_h0_).sleepMilli)
                        return iife64_(_pat_let25_0)
                    return iife63_((pat_let_tv37_).entryCapacity)
                return iife62_(_pat_let24_0)
            d_1587_cache_ = iife61_(StormTracker.default__.DefaultStorm())
            d_1590_cmc_: StormTracker.StormTracker
            nw64_ = StormTracker.StormTracker()
            nw64_.ctor__(d_1587_cache_)
            d_1590_cmc_ = nw64_
            d_1591_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw65_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1590_cmc_)
            d_1591_synCmc_ = nw65_
            output = Wrappers.Result_Success(d_1591_synCmc_)
            return output
        elif source38_.is_No:
            d_1592___mcc_h1_ = source38_.No
            d_1593_cmc_: LocalCMC.LocalCMC
            nw66_ = LocalCMC.LocalCMC()
            nw66_.ctor__(0, 1)
            d_1593_cmc_ = nw66_
            output = Wrappers.Result_Success(d_1593_cmc_)
            return output
        elif source38_.is_SingleThreaded:
            d_1594___mcc_h2_ = source38_.SingleThreaded
            d_1595_c_ = d_1594___mcc_h2_
            d_1596_cmc_: LocalCMC.LocalCMC
            nw67_ = LocalCMC.LocalCMC()
            nw67_.ctor__((d_1595_c_).entryCapacity, (AwsCryptographyMaterialProvidersOperations.default__.OptionalCountingNumber((d_1595_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1596_cmc_ = nw67_
            output = Wrappers.Result_Success(d_1596_cmc_)
            return output
        elif source38_.is_MultiThreaded:
            d_1597___mcc_h3_ = source38_.MultiThreaded
            d_1598_c_ = d_1597___mcc_h3_
            d_1599_cmc_: LocalCMC.LocalCMC
            nw68_ = LocalCMC.LocalCMC()
            nw68_.ctor__((d_1598_c_).entryCapacity, (AwsCryptographyMaterialProvidersOperations.default__.OptionalCountingNumber((d_1598_c_).entryPruningTailSize)).UnwrapOr(1))
            d_1599_cmc_ = nw68_
            d_1600_synCmc_: software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC
            nw69_ = software_amazon_cryptography_internaldafny_SynchronizedLocalCMC.SynchronizedLocalCMC(d_1599_cmc_)
            d_1600_synCmc_ = nw69_
            output = Wrappers.Result_Success(d_1600_synCmc_)
            return output
        elif True:
            d_1601___mcc_h4_ = source38_.StormTracking
            d_1602_c_ = d_1601___mcc_h4_
            pat_let_tv38_ = d_1602_c_
            d_1603_cmc_: StormTracker.StormTracker
            nw70_ = StormTracker.StormTracker()
            def iife65_(_pat_let26_0):
                def iife66_(d_1604_dt__update__tmp_h1_):
                    def iife67_(_pat_let27_0):
                        def iife68_(d_1605_dt__update_hentryPruningTailSize_h0_):
                            return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_1604_dt__update__tmp_h1_).entryCapacity, d_1605_dt__update_hentryPruningTailSize_h0_, (d_1604_dt__update__tmp_h1_).gracePeriod, (d_1604_dt__update__tmp_h1_).graceInterval, (d_1604_dt__update__tmp_h1_).fanOut, (d_1604_dt__update__tmp_h1_).inFlightTTL, (d_1604_dt__update__tmp_h1_).sleepMilli)
                        return iife68_(_pat_let27_0)
                    return iife67_(AwsCryptographyMaterialProvidersOperations.default__.OptionalCountingNumber((pat_let_tv38_).entryPruningTailSize))
                return iife66_(_pat_let26_0)
            nw70_.ctor__(iife65_(d_1602_c_))
            d_1603_cmc_ = nw70_
            d_1606_synCmc_: software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC
            nw71_ = software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC(d_1603_cmc_)
            d_1606_synCmc_ = nw71_
            output = Wrappers.Result_Success(d_1606_synCmc_)
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
        d_1607_clientSupplier_: DefaultClientSupplier.DefaultClientSupplier
        nw72_ = DefaultClientSupplier.DefaultClientSupplier()
        nw72_.ctor__()
        d_1607_clientSupplier_ = nw72_
        output = Wrappers.Result_Success(d_1607_clientSupplier_)
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
        d_1608_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Invalid Encryption Materials Transition")))
        if (d_1608_valueOrError0_).IsFailure():
            return (d_1608_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidDecryptionMaterialsTransition(config, input):
        d_1609_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).start, (input).stop), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Invalid Decryption Materials Transition")))
        if (d_1609_valueOrError0_).IsFailure():
            return (d_1609_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(config, input):
        d_1610_valueOrError0_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Encryption Materials")))
        if (d_1610_valueOrError0_).IsFailure():
            return (d_1610_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(config, input):
        d_1611_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Decryption Materials")))
        if (d_1611_valueOrError0_).IsFailure():
            return (d_1611_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def GetAlgorithmSuiteInfo(config, input):
        return AlgorithmSuites.default__.GetAlgorithmSuiteInfo(input)

    @staticmethod
    def ValidAlgorithmSuiteInfo(config, input):
        d_1612_valueOrError0_ = Wrappers.default__.Need(AlgorithmSuites.default__.AlgorithmSuite_q(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfo(_dafny.Seq("Invalid AlgorithmSuiteInfo")))
        if (d_1612_valueOrError0_).IsFailure():
            return (d_1612_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(config, input):
        d_1613_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1613_valueOrError0_).IsFailure():
            return (d_1613_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(config, input):
        d_1614_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1614_valueOrError0_).IsFailure():
            return (d_1614_valueOrError0_).PropagateFailure()
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

