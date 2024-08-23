import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM

# Module: AwsCryptographyMaterialProvidersOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAwsKmsKeyring(config, input):
        output: Wrappers.Result = None
        d_1529___v0_: tuple
        d_1530_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1530_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1530_valueOrError0_).IsFailure():
            output = (d_1530_valueOrError0_).PropagateFailure()
            return output
        d_1529___v0_ = (d_1530_valueOrError0_).Extract()
        d_1531_grantTokens_: _dafny.Seq
        d_1532_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1532_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1532_valueOrError1_).IsFailure():
            output = (d_1532_valueOrError1_).PropagateFailure()
            return output
        d_1531_grantTokens_ = (d_1532_valueOrError1_).Extract()
        d_1533_keyring_: AwsKmsKeyring.AwsKmsKeyring
        nw63_ = AwsKmsKeyring.AwsKmsKeyring()
        nw63_.ctor__((input).kmsClient, (input).kmsKeyId, d_1531_grantTokens_)
        d_1533_keyring_ = nw63_
        output = Wrappers.Result_Success(d_1533_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1534___v1_: tuple
            d_1535_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1535_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1535_valueOrError0_).IsFailure():
                output = (d_1535_valueOrError0_).PropagateFailure()
                return output
            d_1534___v1_ = (d_1535_valueOrError0_).Extract()
        d_1536_grantTokens_: _dafny.Seq
        d_1537_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1537_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1537_valueOrError1_).IsFailure():
            output = (d_1537_valueOrError1_).PropagateFailure()
            return output
        d_1536_grantTokens_ = (d_1537_valueOrError1_).Extract()
        d_1538_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
        nw64_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
        nw64_.ctor__((input).kmsClient, (input).discoveryFilter, d_1536_grantTokens_)
        d_1538_keyring_ = nw64_
        output = Wrappers.Result_Success(d_1538_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1539_grantTokens_: _dafny.Seq
        d_1540_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1540_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1540_valueOrError0_).IsFailure():
            output = (d_1540_valueOrError0_).PropagateFailure()
            return output
        d_1539_grantTokens_ = (d_1540_valueOrError0_).Extract()
        if ((input).clientSupplier).is_Some:
            out269_: Wrappers.Result
            out269_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, ((input).clientSupplier).value, Wrappers.Option_Some(d_1539_grantTokens_))
            output = out269_
        elif True:
            d_1541_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
            d_1542_valueOrError1_: Wrappers.Result = None
            out270_: Wrappers.Result
            out270_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1542_valueOrError1_ = out270_
            if (d_1542_valueOrError1_).IsFailure():
                output = (d_1542_valueOrError1_).PropagateFailure()
                return output
            d_1541_clientSupplier_ = (d_1542_valueOrError1_).Extract()
            out271_: Wrappers.Result
            out271_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1541_clientSupplier_, Wrappers.Option_Some(d_1539_grantTokens_))
            output = out271_
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1543_grantTokens_: _dafny.Seq
        d_1544_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1544_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1544_valueOrError0_).IsFailure():
            output = (d_1544_valueOrError0_).PropagateFailure()
            return output
        d_1543_grantTokens_ = (d_1544_valueOrError0_).Extract()
        d_1545_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1546_valueOrError1_: Wrappers.Result = None
            out272_: Wrappers.Result
            out272_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1546_valueOrError1_ = out272_
            if (d_1546_valueOrError1_).IsFailure():
                output = (d_1546_valueOrError1_).PropagateFailure()
                return output
            d_1545_clientSupplier_ = (d_1546_valueOrError1_).Extract()
        elif True:
            d_1545_clientSupplier_ = ((input).clientSupplier).value
        out273_: Wrappers.Result
        out273_ = DiscoveryMultiKeyring.default__.DiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1545_clientSupplier_, Wrappers.Option_Some(d_1543_grantTokens_))
        output = out273_
        return output

    @staticmethod
    def CreateAwsKmsMrkKeyring(config, input):
        output: Wrappers.Result = None
        d_1547___v2_: tuple
        d_1548_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1548_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1548_valueOrError0_).IsFailure():
            output = (d_1548_valueOrError0_).PropagateFailure()
            return output
        d_1547___v2_ = (d_1548_valueOrError0_).Extract()
        d_1549_grantTokens_: _dafny.Seq
        d_1550_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1550_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1550_valueOrError1_).IsFailure():
            output = (d_1550_valueOrError1_).PropagateFailure()
            return output
        d_1549_grantTokens_ = (d_1550_valueOrError1_).Extract()
        d_1551_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
        nw65_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
        nw65_.ctor__((input).kmsClient, (input).kmsKeyId, d_1549_grantTokens_)
        d_1551_keyring_ = nw65_
        output = Wrappers.Result_Success(d_1551_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1552_grantTokens_: _dafny.Seq
        d_1553_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1553_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1553_valueOrError0_).IsFailure():
            output = (d_1553_valueOrError0_).PropagateFailure()
            return output
        d_1552_grantTokens_ = (d_1553_valueOrError0_).Extract()
        d_1554_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1555_valueOrError1_: Wrappers.Result = None
            out274_: Wrappers.Result
            out274_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1555_valueOrError1_ = out274_
            if (d_1555_valueOrError1_).IsFailure():
                output = (d_1555_valueOrError1_).PropagateFailure()
                return output
            d_1554_clientSupplier_ = (d_1555_valueOrError1_).Extract()
        elif True:
            d_1554_clientSupplier_ = ((input).clientSupplier).value
        out275_: Wrappers.Result
        out275_ = MrkAwareStrictMultiKeyring.default__.MrkAwareStrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1554_clientSupplier_, Wrappers.Option_Some(d_1552_grantTokens_))
        output = out275_
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1556___v3_: tuple
            d_1557_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1557_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1557_valueOrError0_).IsFailure():
                output = (d_1557_valueOrError0_).PropagateFailure()
                return output
            d_1556___v3_ = (d_1557_valueOrError0_).Extract()
        d_1558_regionMatch_: Wrappers.Option
        d_1558_regionMatch_ = Com_Amazonaws_Kms.default__.RegionMatch((input).kmsClient, (input).region)
        d_1559_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1559_valueOrError1_ = Wrappers.default__.Need((d_1558_regionMatch_) != (Wrappers.Option_Some(False)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Provided client and region do not match")))
        if (d_1559_valueOrError1_).IsFailure():
            output = (d_1559_valueOrError1_).PropagateFailure()
            return output
        d_1560_grantTokens_: _dafny.Seq
        d_1561_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1561_valueOrError2_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1561_valueOrError2_).IsFailure():
            output = (d_1561_valueOrError2_).PropagateFailure()
            return output
        d_1560_grantTokens_ = (d_1561_valueOrError2_).Extract()
        d_1562_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
        nw66_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
        nw66_.ctor__((input).kmsClient, (input).region, (input).discoveryFilter, d_1560_grantTokens_)
        d_1562_keyring_ = nw66_
        output = Wrappers.Result_Success(d_1562_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1563_grantTokens_: _dafny.Seq
        d_1564_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1564_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1564_valueOrError0_).IsFailure():
            output = (d_1564_valueOrError0_).PropagateFailure()
            return output
        d_1563_grantTokens_ = (d_1564_valueOrError0_).Extract()
        d_1565_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1566_valueOrError1_: Wrappers.Result = None
            out276_: Wrappers.Result
            out276_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1566_valueOrError1_ = out276_
            if (d_1566_valueOrError1_).IsFailure():
                output = (d_1566_valueOrError1_).PropagateFailure()
                return output
            d_1565_clientSupplier_ = (d_1566_valueOrError1_).Extract()
        elif True:
            d_1565_clientSupplier_ = ((input).clientSupplier).value
        out277_: Wrappers.Result
        out277_ = MrkAwareDiscoveryMultiKeyring.default__.MrkAwareDiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1565_clientSupplier_, Wrappers.Option_Some(d_1563_grantTokens_))
        output = out277_
        return output

    @staticmethod
    def CreateAwsKmsHierarchicalKeyring(config, input):
        output: Wrappers.Result = None
        d_1567_maxCacheSize_: int = int(0)
        d_1568_cache_: AwsCryptographyMaterialProvidersTypes.CacheType
        d_1568_cache_ = (((input).cache).value if ((input).cache).is_Some else AwsCryptographyMaterialProvidersTypes.CacheType_Default(AwsCryptographyMaterialProvidersTypes.DefaultCache_DefaultCache(1000)))
        d_1569_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1569_valueOrError0_ = Wrappers.default__.Need((((input).branchKeyId).is_None) or (((input).branchKeyIdSupplier).is_None), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")))
        if (d_1569_valueOrError0_).IsFailure():
            output = (d_1569_valueOrError0_).PropagateFailure()
            return output
        d_1570_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1570_valueOrError1_ = Wrappers.default__.Need((((input).branchKeyId).is_Some) or (((input).branchKeyIdSupplier).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")))
        if (d_1570_valueOrError1_).IsFailure():
            output = (d_1570_valueOrError1_).PropagateFailure()
            return output
        d_1571_cmc_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
        d_1572_valueOrError2_: Wrappers.Result = None
        out278_: Wrappers.Result
        out278_ = default__.CreateCryptographicMaterialsCache(config, AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(d_1568_cache_))
        d_1572_valueOrError2_ = out278_
        if (d_1572_valueOrError2_).IsFailure():
            output = (d_1572_valueOrError2_).PropagateFailure()
            return output
        d_1571_cmc_ = (d_1572_valueOrError2_).Extract()
        d_1573_keyring_: AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
        nw67_ = AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring()
        nw67_.ctor__((input).keyStore, (input).branchKeyId, (input).branchKeyIdSupplier, (input).ttlSeconds, d_1571_cmc_, (config).crypto)
        d_1573_keyring_ = nw67_
        output = Wrappers.Result_Success(d_1573_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsEcdhKeyring(config, input):
        output: Wrappers.Result = None
        d_1574_grantTokens_: _dafny.Seq
        d_1575_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1575_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1575_valueOrError0_).IsFailure():
            output = (d_1575_valueOrError0_).PropagateFailure()
            return output
        d_1574_grantTokens_ = (d_1575_valueOrError0_).Extract()
        d_1576_recipientPublicKey_: _dafny.Seq = None
        d_1577_senderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        d_1578_compressedSenderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        if ((input).KeyAgreementScheme).is_KmsPublicKeyDiscovery:
            d_1579___v4_: tuple
            d_1580_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1580_valueOrError1_ = AwsKmsUtils.default__.ValidateKmsKeyId((((input).KeyAgreementScheme).KmsPublicKeyDiscovery).recipientKmsIdentifier)
            if (d_1580_valueOrError1_).IsFailure():
                output = (d_1580_valueOrError1_).PropagateFailure()
                return output
            d_1579___v4_ = (d_1580_valueOrError1_).Extract()
            d_1581_valueOrError2_: Wrappers.Result = None
            out279_: Wrappers.Result
            out279_ = AwsKmsUtils.default__.GetEcdhPublicKey((input).kmsClient, (((input).KeyAgreementScheme).KmsPublicKeyDiscovery).recipientKmsIdentifier)
            d_1581_valueOrError2_ = out279_
            if (d_1581_valueOrError2_).IsFailure():
                output = (d_1581_valueOrError2_).PropagateFailure()
                return output
            d_1576_recipientPublicKey_ = (d_1581_valueOrError2_).Extract()
            d_1577_senderPublicKey_ = Wrappers.Option_None()
            d_1578_compressedSenderPublicKey_ = Wrappers.Option_None()
        elif ((input).KeyAgreementScheme).is_KmsPrivateKeyToStaticPublicKey:
            if ((((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderPublicKey).is_Some:
                d_1582_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_1582_valueOrError3_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType(((((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderPublicKey).value), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid SenderPublicKey length.")))
                if (d_1582_valueOrError3_).IsFailure():
                    output = (d_1582_valueOrError3_).PropagateFailure()
                    return output
                d_1577_senderPublicKey_ = Wrappers.Option_Some(((((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderPublicKey).value)
                d_1583_compressedPKU_: _dafny.Seq
                d_1584_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                out280_: Wrappers.Result
                out280_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_1577_senderPublicKey_).value), (input).curveSpec, (config).crypto)
                d_1584_valueOrError4_ = out280_
                if (d_1584_valueOrError4_).IsFailure():
                    output = (d_1584_valueOrError4_).PropagateFailure()
                    return output
                d_1583_compressedPKU_ = (d_1584_valueOrError4_).Extract()
                d_1578_compressedSenderPublicKey_ = Wrappers.Option_Some(d_1583_compressedPKU_)
            elif True:
                d_1585___v5_: tuple
                d_1586_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                d_1586_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderKmsIdentifier)
                if (d_1586_valueOrError5_).IsFailure():
                    output = (d_1586_valueOrError5_).PropagateFailure()
                    return output
                d_1585___v5_ = (d_1586_valueOrError5_).Extract()
                d_1587_senderPublicKeyResponse_: _dafny.Seq
                d_1588_valueOrError6_: Wrappers.Result = None
                out281_: Wrappers.Result
                out281_ = AwsKmsUtils.default__.GetEcdhPublicKey((input).kmsClient, (((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderKmsIdentifier)
                d_1588_valueOrError6_ = out281_
                if (d_1588_valueOrError6_).IsFailure():
                    output = (d_1588_valueOrError6_).PropagateFailure()
                    return output
                d_1587_senderPublicKeyResponse_ = (d_1588_valueOrError6_).Extract()
                d_1589_compressedPKU_: _dafny.Seq
                d_1590_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                out282_: Wrappers.Result
                out282_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1587_senderPublicKeyResponse_), (input).curveSpec, (config).crypto)
                d_1590_valueOrError7_ = out282_
                if (d_1590_valueOrError7_).IsFailure():
                    output = (d_1590_valueOrError7_).PropagateFailure()
                    return output
                d_1589_compressedPKU_ = (d_1590_valueOrError7_).Extract()
                d_1577_senderPublicKey_ = Wrappers.Option_Some(d_1587_senderPublicKeyResponse_)
                d_1578_compressedSenderPublicKey_ = Wrappers.Option_Some(d_1589_compressedPKU_)
            d_1591_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_1591_valueOrError8_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType((((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).recipientPublicKey), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid RecipientPublicKey length.")))
            if (d_1591_valueOrError8_).IsFailure():
                output = (d_1591_valueOrError8_).PropagateFailure()
                return output
            d_1576_recipientPublicKey_ = (((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).recipientPublicKey
        elif True:
            raise Exception("unreachable alternative")
        d_1592___v6_: bool
        d_1593_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out283_: Wrappers.Result
        out283_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, d_1576_recipientPublicKey_)
        d_1593_valueOrError9_ = out283_
        if (d_1593_valueOrError9_).IsFailure():
            output = (d_1593_valueOrError9_).PropagateFailure()
            return output
        d_1592___v6_ = (d_1593_valueOrError9_).Extract()
        d_1594_compressedRecipientPublicKey_: _dafny.Seq
        d_1595_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out284_: Wrappers.Result
        out284_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1576_recipientPublicKey_), (input).curveSpec, (config).crypto)
        d_1595_valueOrError10_ = out284_
        if (d_1595_valueOrError10_).IsFailure():
            output = (d_1595_valueOrError10_).PropagateFailure()
            return output
        d_1594_compressedRecipientPublicKey_ = (d_1595_valueOrError10_).Extract()
        d_1596_senderKmsKeyId_: Wrappers.Option
        d_1596_senderKmsKeyId_ = (Wrappers.Option_None() if ((input).KeyAgreementScheme).is_KmsPublicKeyDiscovery else Wrappers.Option_Some((((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderKmsIdentifier))
        if (d_1596_senderKmsKeyId_).is_Some:
            d_1597___v7_: tuple
            d_1598_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1598_valueOrError11_ = AwsKmsUtils.default__.ValidateKmsKeyId((d_1596_senderKmsKeyId_).value)
            if (d_1598_valueOrError11_).IsFailure():
                output = (d_1598_valueOrError11_).PropagateFailure()
                return output
            d_1597___v7_ = (d_1598_valueOrError11_).Extract()
        if (d_1577_senderPublicKey_).is_Some:
            d_1599___v8_: bool
            d_1600_valueOrError12_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
            out285_: Wrappers.Result
            out285_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, (d_1577_senderPublicKey_).value)
            d_1600_valueOrError12_ = out285_
            if (d_1600_valueOrError12_).IsFailure():
                output = (d_1600_valueOrError12_).PropagateFailure()
                return output
            d_1599___v8_ = (d_1600_valueOrError12_).Extract()
        d_1601_keyring_: AwsKmsEcdhKeyring.AwsKmsEcdhKeyring
        nw68_ = AwsKmsEcdhKeyring.AwsKmsEcdhKeyring()
        nw68_.ctor__((input).KeyAgreementScheme, (input).curveSpec, (input).kmsClient, d_1574_grantTokens_, d_1596_senderKmsKeyId_, d_1577_senderPublicKey_, d_1576_recipientPublicKey_, d_1578_compressedSenderPublicKey_, d_1594_compressedRecipientPublicKey_, (config).crypto)
        d_1601_keyring_ = nw68_
        output = Wrappers.Result_Success(d_1601_keyring_)
        return output
        return output

    @staticmethod
    def CreateMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1602_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1602_valueOrError0_ = Wrappers.default__.Need((((input).generator).is_Some) or ((len((input).childKeyrings)) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must include a generator keyring and/or at least one child keyring")))
        if (d_1602_valueOrError0_).IsFailure():
            output = (d_1602_valueOrError0_).PropagateFailure()
            return output
        d_1603_keyring_: MultiKeyring.MultiKeyring
        nw69_ = MultiKeyring.MultiKeyring()
        nw69_.ctor__((input).generator, (input).childKeyrings)
        d_1603_keyring_ = nw69_
        output = Wrappers.Result_Success(d_1603_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawAesKeyring(config, input):
        output: Wrappers.Result = None
        d_1604_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1604_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1604_valueOrError0_).IsFailure():
            output = (d_1604_valueOrError0_).PropagateFailure()
            return output
        d_1605_wrappingAlg_: AwsCryptographyPrimitivesTypes.AES__GCM
        def lambda123_():
            source35_ = (input).wrappingAlg
            unmatched35 = True
            if unmatched35:
                if source35_.is_ALG__AES128__GCM__IV12__TAG16:
                    unmatched35 = False
                    return AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(16, 16, 12)
            if unmatched35:
                if source35_.is_ALG__AES192__GCM__IV12__TAG16:
                    unmatched35 = False
                    return AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(24, 16, 12)
            if unmatched35:
                unmatched35 = False
                return AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(32, 16, 12)
            raise Exception("unexpected control point")

        d_1605_wrappingAlg_ = lambda123_()
        d_1606_namespaceAndName_: tuple
        d_1607_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1607_valueOrError1_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1607_valueOrError1_).IsFailure():
            output = (d_1607_valueOrError1_).PropagateFailure()
            return output
        d_1606_namespaceAndName_ = (d_1607_valueOrError1_).Extract()
        let_tmp_rhs5_ = d_1606_namespaceAndName_
        d_1608_namespace_ = let_tmp_rhs5_[0]
        d_1609_name_ = let_tmp_rhs5_[1]
        d_1610_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1610_valueOrError2_ = Wrappers.default__.Need((((len((input).wrappingKey)) == (16)) or ((len((input).wrappingKey)) == (24))) or ((len((input).wrappingKey)) == (32)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid wrapping key length")))
        if (d_1610_valueOrError2_).IsFailure():
            output = (d_1610_valueOrError2_).PropagateFailure()
            return output
        d_1611_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1611_valueOrError3_ = Wrappers.default__.Need((len((input).wrappingKey)) == ((d_1605_wrappingAlg_).keyLength), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrapping key length does not match specified wrapping algorithm")))
        if (d_1611_valueOrError3_).IsFailure():
            output = (d_1611_valueOrError3_).PropagateFailure()
            return output
        d_1612_keyring_: RawAESKeyring.RawAESKeyring
        nw70_ = RawAESKeyring.RawAESKeyring()
        nw70_.ctor__(d_1608_namespace_, d_1609_name_, (input).wrappingKey, d_1605_wrappingAlg_, (config).crypto)
        d_1612_keyring_ = nw70_
        output = Wrappers.Result_Success(d_1612_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1613_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1613_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1613_valueOrError0_).IsFailure():
            output = (d_1613_valueOrError0_).PropagateFailure()
            return output
        d_1614_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1614_valueOrError1_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).privateKey).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a privateKey is required")))
        if (d_1614_valueOrError1_).IsFailure():
            output = (d_1614_valueOrError1_).PropagateFailure()
            return output
        d_1615_padding_: AwsCryptographyPrimitivesTypes.RSAPaddingMode
        def lambda124_():
            source36_ = (input).paddingScheme
            unmatched36 = True
            if unmatched36:
                if source36_.is_PKCS1:
                    unmatched36 = False
                    return AwsCryptographyPrimitivesTypes.RSAPaddingMode_PKCS1()
            if unmatched36:
                if source36_.is_OAEP__SHA1__MGF1:
                    unmatched36 = False
                    return AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA1()
            if unmatched36:
                if source36_.is_OAEP__SHA256__MGF1:
                    unmatched36 = False
                    return AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA256()
            if unmatched36:
                if source36_.is_OAEP__SHA384__MGF1:
                    unmatched36 = False
                    return AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA384()
            if unmatched36:
                unmatched36 = False
                return AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA512()
            raise Exception("unexpected control point")

        d_1615_padding_ = lambda124_()
        d_1616_namespaceAndName_: tuple
        d_1617_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1617_valueOrError2_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1617_valueOrError2_).IsFailure():
            output = (d_1617_valueOrError2_).PropagateFailure()
            return output
        d_1616_namespaceAndName_ = (d_1617_valueOrError2_).Extract()
        let_tmp_rhs6_ = d_1616_namespaceAndName_
        d_1618_namespace_ = let_tmp_rhs6_[0]
        d_1619_name_ = let_tmp_rhs6_[1]
        d_1620_keyring_: RawRSAKeyring.RawRSAKeyring
        nw71_ = RawRSAKeyring.RawRSAKeyring()
        nw71_.ctor__(d_1618_namespace_, d_1619_name_, (input).publicKey, (input).privateKey, d_1615_padding_, (config).crypto)
        d_1620_keyring_ = nw71_
        output = Wrappers.Result_Success(d_1620_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawEcdhKeyring(config, input):
        output: Wrappers.Result = None
        d_1621_recipientPublicKey_: _dafny.Seq = _dafny.Seq({})
        d_1622_senderPrivateKey_: Wrappers.Option = Wrappers.Option.default()()
        d_1623_senderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        d_1624_compressedSenderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        if ((input).KeyAgreementScheme).is_RawPrivateKeyToStaticPublicKey:
            d_1621_recipientPublicKey_ = (((input).KeyAgreementScheme).RawPrivateKeyToStaticPublicKey).recipientPublicKey
            d_1622_senderPrivateKey_ = Wrappers.Option_Some((((input).KeyAgreementScheme).RawPrivateKeyToStaticPublicKey).senderStaticPrivateKey)
            d_1625_reproducedPublicKey_: _dafny.Seq
            d_1626_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out286_: Wrappers.Result
            out286_ = Utils.default__.GetPublicKey((input).curveSpec, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey((d_1622_senderPrivateKey_).value), (config).crypto)
            d_1626_valueOrError0_ = out286_
            if (d_1626_valueOrError0_).IsFailure():
                output = (d_1626_valueOrError0_).PropagateFailure()
                return output
            d_1625_reproducedPublicKey_ = (d_1626_valueOrError0_).Extract()
            d_1627___v9_: bool
            d_1628_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
            out287_: Wrappers.Result
            out287_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, d_1625_reproducedPublicKey_)
            d_1628_valueOrError1_ = out287_
            if (d_1628_valueOrError1_).IsFailure():
                output = (d_1628_valueOrError1_).PropagateFailure()
                return output
            d_1627___v9_ = (d_1628_valueOrError1_).Extract()
            d_1623_senderPublicKey_ = Wrappers.Option_Some(d_1625_reproducedPublicKey_)
            d_1629_compressedSenderPublicKey_q_: _dafny.Seq
            d_1630_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out288_: Wrappers.Result
            out288_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1625_reproducedPublicKey_), (input).curveSpec, (config).crypto)
            d_1630_valueOrError2_ = out288_
            if (d_1630_valueOrError2_).IsFailure():
                output = (d_1630_valueOrError2_).PropagateFailure()
                return output
            d_1629_compressedSenderPublicKey_q_ = (d_1630_valueOrError2_).Extract()
            d_1624_compressedSenderPublicKey_ = Wrappers.Option_Some(d_1629_compressedSenderPublicKey_q_)
        elif ((input).KeyAgreementScheme).is_EphemeralPrivateKeyToStaticPublicKey:
            d_1621_recipientPublicKey_ = (((input).KeyAgreementScheme).EphemeralPrivateKeyToStaticPublicKey).recipientPublicKey
            d_1622_senderPrivateKey_ = Wrappers.Option_None()
            d_1623_senderPublicKey_ = Wrappers.Option_None()
            d_1624_compressedSenderPublicKey_ = Wrappers.Option_None()
        elif ((input).KeyAgreementScheme).is_PublicKeyDiscovery:
            d_1631_reproducedPublicKey_: _dafny.Seq
            d_1632_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out289_: Wrappers.Result
            out289_ = Utils.default__.GetPublicKey((input).curveSpec, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey((((input).KeyAgreementScheme).PublicKeyDiscovery).recipientStaticPrivateKey), (config).crypto)
            d_1632_valueOrError3_ = out289_
            if (d_1632_valueOrError3_).IsFailure():
                output = (d_1632_valueOrError3_).PropagateFailure()
                return output
            d_1631_reproducedPublicKey_ = (d_1632_valueOrError3_).Extract()
            d_1621_recipientPublicKey_ = d_1631_reproducedPublicKey_
            d_1622_senderPrivateKey_ = Wrappers.Option_None()
            d_1623_senderPublicKey_ = Wrappers.Option_None()
            d_1624_compressedSenderPublicKey_ = Wrappers.Option_None()
        elif True:
            raise Exception("unreachable alternative")
        d_1633_compressedRecipientPublicKey_: _dafny.Seq
        d_1634_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out290_: Wrappers.Result
        out290_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1621_recipientPublicKey_), (input).curveSpec, (config).crypto)
        d_1634_valueOrError4_ = out290_
        if (d_1634_valueOrError4_).IsFailure():
            output = (d_1634_valueOrError4_).PropagateFailure()
            return output
        d_1633_compressedRecipientPublicKey_ = (d_1634_valueOrError4_).Extract()
        d_1635___v10_: bool
        d_1636_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out291_: Wrappers.Result
        out291_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, d_1621_recipientPublicKey_)
        d_1636_valueOrError5_ = out291_
        if (d_1636_valueOrError5_).IsFailure():
            output = (d_1636_valueOrError5_).PropagateFailure()
            return output
        d_1635___v10_ = (d_1636_valueOrError5_).Extract()
        if (d_1623_senderPublicKey_).is_Some:
            d_1637___v11_: bool
            d_1638_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
            out292_: Wrappers.Result
            out292_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, (d_1623_senderPublicKey_).value)
            d_1638_valueOrError6_ = out292_
            if (d_1638_valueOrError6_).IsFailure():
                output = (d_1638_valueOrError6_).PropagateFailure()
                return output
            d_1637___v11_ = (d_1638_valueOrError6_).Extract()
            d_1639_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_1639_valueOrError7_ = Wrappers.default__.Need(RawECDHKeyring.default__.ValidPublicKeyLength((d_1623_senderPublicKey_).value), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid sender public key length")))
            if (d_1639_valueOrError7_).IsFailure():
                output = (d_1639_valueOrError7_).PropagateFailure()
                return output
        d_1640_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1640_valueOrError8_ = Wrappers.default__.Need(RawECDHKeyring.default__.ValidPublicKeyLength(d_1621_recipientPublicKey_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid recipient public key length")))
        if (d_1640_valueOrError8_).IsFailure():
            output = (d_1640_valueOrError8_).PropagateFailure()
            return output
        d_1641_keyring_: RawECDHKeyring.RawEcdhKeyring
        nw72_ = RawECDHKeyring.RawEcdhKeyring()
        nw72_.ctor__((input).KeyAgreementScheme, (input).curveSpec, d_1622_senderPrivateKey_, d_1623_senderPublicKey_, d_1621_recipientPublicKey_, d_1624_compressedSenderPublicKey_, d_1633_compressedRecipientPublicKey_, (config).crypto)
        d_1641_keyring_ = nw72_
        output = Wrappers.Result_Success(d_1641_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1642_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1642_valueOrError0_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).kmsClient).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a kmsClient is required")))
        if (d_1642_valueOrError0_).IsFailure():
            output = (d_1642_valueOrError0_).PropagateFailure()
            return output
        d_1643_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1643_valueOrError1_ = Wrappers.default__.Need((((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__1) or (((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__256), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unsupported EncryptionAlgorithmSpec")))
        if (d_1643_valueOrError1_).IsFailure():
            output = (d_1643_valueOrError1_).PropagateFailure()
            return output
        d_1644_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1644_valueOrError2_ = Wrappers.default__.Need((ComAmazonawsKmsTypes.default__.IsValid__KeyIdType((input).kmsKeyId)) and ((AwsArnParsing.default__.ParseAwsKmsArn((input).kmsKeyId)).is_Success), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Kms Key ID must be a KMS Key ARN")))
        if (d_1644_valueOrError2_).IsFailure():
            output = (d_1644_valueOrError2_).PropagateFailure()
            return output
        if ((input).publicKey).is_Some:
            d_1645_lengthOutputRes_: Wrappers.Result
            d_1645_lengthOutputRes_ = ((config).crypto).GetRSAKeyModulusLength(AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(((input).publicKey).value))
            d_1646_lengthOutput_: AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput
            d_1647_valueOrError3_: Wrappers.Result = None
            def lambda125_(d_1648_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1648_e_)

            d_1647_valueOrError3_ = (d_1645_lengthOutputRes_).MapFailure(lambda125_)
            if (d_1647_valueOrError3_).IsFailure():
                output = (d_1647_valueOrError3_).PropagateFailure()
                return output
            d_1646_lengthOutput_ = (d_1647_valueOrError3_).Extract()
            d_1649_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_1649_valueOrError4_ = Wrappers.default__.Need(((d_1646_lengthOutput_).length) >= (AwsKmsRsaKeyring.default__.MIN__KMS__RSA__KEY__LEN), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid public key length")))
            if (d_1649_valueOrError4_).IsFailure():
                output = (d_1649_valueOrError4_).PropagateFailure()
                return output
        d_1650___v12_: tuple
        d_1651_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1651_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1651_valueOrError5_).IsFailure():
            output = (d_1651_valueOrError5_).PropagateFailure()
            return output
        d_1650___v12_ = (d_1651_valueOrError5_).Extract()
        d_1652_grantTokens_: _dafny.Seq
        d_1653_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1653_valueOrError6_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1653_valueOrError6_).IsFailure():
            output = (d_1653_valueOrError6_).PropagateFailure()
            return output
        d_1652_grantTokens_ = (d_1653_valueOrError6_).Extract()
        d_1654_keyring_: AwsKmsRsaKeyring.AwsKmsRsaKeyring
        nw73_ = AwsKmsRsaKeyring.AwsKmsRsaKeyring()
        nw73_.ctor__((input).publicKey, (input).kmsKeyId, (input).encryptionAlgorithm, (input).kmsClient, (config).crypto, d_1652_grantTokens_)
        d_1654_keyring_ = nw73_
        output = Wrappers.Result_Success(d_1654_keyring_)
        return output
        return output

    @staticmethod
    def CreateDefaultCryptographicMaterialsManager(config, input):
        output: Wrappers.Result = None
        d_1655_cmm_: DefaultCMM.DefaultCMM
        nw74_ = DefaultCMM.DefaultCMM()
        nw74_.OfKeyring((input).keyring, (config).crypto)
        d_1655_cmm_ = nw74_
        output = Wrappers.Result_Success(d_1655_cmm_)
        return output
        return output

    @staticmethod
    def CmpError(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def CreateRequiredEncryptionContextCMM(config, input):
        output: Wrappers.Result = None
        d_1656_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1656_valueOrError0_ = Wrappers.default__.Need((((input).underlyingCMM).is_Some) and (((input).keyring).is_None), default__.CmpError(_dafny.Seq("CreateRequiredEncryptionContextCMM currently only supports cmm.")))
        if (d_1656_valueOrError0_).IsFailure():
            output = (d_1656_valueOrError0_).PropagateFailure()
            return output
        d_1657_keySet_: _dafny.Set
        def iife34_():
            coll10_ = _dafny.Set()
            compr_10_: _dafny.Seq
            for compr_10_ in ((input).requiredEncryptionContextKeys).Elements:
                d_1658_k_: _dafny.Seq = compr_10_
                if UTF8.ValidUTF8Bytes._Is(d_1658_k_):
                    if (d_1658_k_) in ((input).requiredEncryptionContextKeys):
                        coll10_ = coll10_.union(_dafny.Set([d_1658_k_]))
            return _dafny.Set(coll10_)
        d_1657_keySet_ = iife34_()
        
        d_1659_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1659_valueOrError1_ = Wrappers.default__.Need((0) < (len(d_1657_keySet_)), default__.CmpError(_dafny.Seq("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")))
        if (d_1659_valueOrError1_).IsFailure():
            output = (d_1659_valueOrError1_).PropagateFailure()
            return output
        d_1660_cmm_: RequiredEncryptionContextCMM.RequiredEncryptionContextCMM
        nw75_ = RequiredEncryptionContextCMM.RequiredEncryptionContextCMM()
        nw75_.ctor__(((input).underlyingCMM).value, d_1657_keySet_)
        d_1660_cmm_ = nw75_
        output = Wrappers.Result_Success(d_1660_cmm_)
        return output
        return output

    @staticmethod
    def CreateCryptographicMaterialsCache(config, input):
        output: Wrappers.Result = None
        source37_ = (input).cache
        unmatched37 = True
        if unmatched37:
            if source37_.is_Default:
                d_1661_c_ = source37_.Default
                unmatched37 = False
                pat_let_tv172_ = d_1661_c_
                d_1662_cache_: AwsCryptographyMaterialProvidersTypes.StormTrackingCache
                def iife35_(_pat_let12_0):
                    def iife36_(d_1663_dt__update__tmp_h0_):
                        def iife37_(_pat_let13_0):
                            def iife38_(d_1664_dt__update_hentryCapacity_h0_):
                                return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache(d_1664_dt__update_hentryCapacity_h0_, (d_1663_dt__update__tmp_h0_).entryPruningTailSize, (d_1663_dt__update__tmp_h0_).gracePeriod, (d_1663_dt__update__tmp_h0_).graceInterval, (d_1663_dt__update__tmp_h0_).fanOut, (d_1663_dt__update__tmp_h0_).inFlightTTL, (d_1663_dt__update__tmp_h0_).sleepMilli)
                            return iife38_(_pat_let13_0)
                        return iife37_((pat_let_tv172_).entryCapacity)
                    return iife36_(_pat_let12_0)
                d_1662_cache_ = iife35_(StormTracker.default__.DefaultStorm())
                d_1665_cmc_: StormTracker.StormTracker
                nw76_ = StormTracker.StormTracker()
                nw76_.ctor__(d_1662_cache_)
                d_1665_cmc_ = nw76_
                d_1666_synCmc_: StormTrackingCMC.StormTrackingCMC
                nw77_ = StormTrackingCMC.StormTrackingCMC(d_1665_cmc_)
                d_1666_synCmc_ = nw77_
                output = Wrappers.Result_Success(d_1666_synCmc_)
                return output
        if unmatched37:
            if source37_.is_No:
                unmatched37 = False
                d_1667_cmc_: LocalCMC.LocalCMC
                nw78_ = LocalCMC.LocalCMC()
                nw78_.ctor__(0, 1)
                d_1667_cmc_ = nw78_
                output = Wrappers.Result_Success(d_1667_cmc_)
                return output
        if unmatched37:
            if source37_.is_SingleThreaded:
                d_1668_c_ = source37_.SingleThreaded
                unmatched37 = False
                d_1669_cmc_: LocalCMC.LocalCMC
                nw79_ = LocalCMC.LocalCMC()
                nw79_.ctor__((d_1668_c_).entryCapacity, (default__.OptionalCountingNumber((d_1668_c_).entryPruningTailSize)).UnwrapOr(1))
                d_1669_cmc_ = nw79_
                output = Wrappers.Result_Success(d_1669_cmc_)
                return output
        if unmatched37:
            if source37_.is_MultiThreaded:
                d_1670_c_ = source37_.MultiThreaded
                unmatched37 = False
                d_1671_cmc_: LocalCMC.LocalCMC
                nw80_ = LocalCMC.LocalCMC()
                nw80_.ctor__((d_1670_c_).entryCapacity, (default__.OptionalCountingNumber((d_1670_c_).entryPruningTailSize)).UnwrapOr(1))
                d_1671_cmc_ = nw80_
                d_1672_synCmc_: SynchronizedLocalCMC.SynchronizedLocalCMC
                nw81_ = SynchronizedLocalCMC.SynchronizedLocalCMC(d_1671_cmc_)
                d_1672_synCmc_ = nw81_
                output = Wrappers.Result_Success(d_1672_synCmc_)
                return output
        if unmatched37:
            d_1673_c_ = source37_.StormTracking
            unmatched37 = False
            pat_let_tv173_ = d_1673_c_
            d_1674_cmc_: StormTracker.StormTracker
            nw82_ = StormTracker.StormTracker()
            def iife39_(_pat_let14_0):
                def iife40_(d_1675_dt__update__tmp_h1_):
                    def iife41_(_pat_let15_0):
                        def iife42_(d_1676_dt__update_hentryPruningTailSize_h0_):
                            return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_1675_dt__update__tmp_h1_).entryCapacity, d_1676_dt__update_hentryPruningTailSize_h0_, (d_1675_dt__update__tmp_h1_).gracePeriod, (d_1675_dt__update__tmp_h1_).graceInterval, (d_1675_dt__update__tmp_h1_).fanOut, (d_1675_dt__update__tmp_h1_).inFlightTTL, (d_1675_dt__update__tmp_h1_).sleepMilli)
                        return iife42_(_pat_let15_0)
                    return iife41_(default__.OptionalCountingNumber((pat_let_tv173_).entryPruningTailSize))
                return iife40_(_pat_let14_0)
            nw82_.ctor__(iife39_(d_1673_c_))
            d_1674_cmc_ = nw82_
            d_1677_synCmc_: StormTrackingCMC.StormTrackingCMC
            nw83_ = StormTrackingCMC.StormTrackingCMC(d_1674_cmc_)
            d_1677_synCmc_ = nw83_
            output = Wrappers.Result_Success(d_1677_synCmc_)
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
        d_1678_clientSupplier_: DefaultClientSupplier.DefaultClientSupplier
        nw84_ = DefaultClientSupplier.DefaultClientSupplier()
        nw84_.ctor__()
        d_1678_clientSupplier_ = nw84_
        output = Wrappers.Result_Success(d_1678_clientSupplier_)
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
        d_1679_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).start, (input).stop), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Invalid Encryption Materials Transition")))
        if (d_1679_valueOrError0_).IsFailure():
            return (d_1679_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidDecryptionMaterialsTransition(config, input):
        d_1680_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).start, (input).stop), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Invalid Decryption Materials Transition")))
        if (d_1680_valueOrError0_).IsFailure():
            return (d_1680_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(config, input):
        d_1681_valueOrError0_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Encryption Materials")))
        if (d_1681_valueOrError0_).IsFailure():
            return (d_1681_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(config, input):
        d_1682_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Decryption Materials")))
        if (d_1682_valueOrError0_).IsFailure():
            return (d_1682_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def GetAlgorithmSuiteInfo(config, input):
        return AlgorithmSuites.default__.GetAlgorithmSuiteInfo(input)

    @staticmethod
    def ValidAlgorithmSuiteInfo(config, input):
        d_1683_valueOrError0_ = Wrappers.default__.Need(AlgorithmSuites.default__.AlgorithmSuite_q(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidAlgorithmSuiteInfo(_dafny.Seq("Invalid AlgorithmSuiteInfo")))
        if (d_1683_valueOrError0_).IsFailure():
            return (d_1683_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(config, input):
        d_1684_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1684_valueOrError0_).IsFailure():
            return (d_1684_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(config, input):
        d_1685_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1685_valueOrError0_).IsFailure():
            return (d_1685_valueOrError0_).PropagateFailure()
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

