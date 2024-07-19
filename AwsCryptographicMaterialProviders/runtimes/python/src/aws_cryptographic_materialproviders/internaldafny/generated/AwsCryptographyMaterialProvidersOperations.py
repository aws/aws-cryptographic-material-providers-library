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
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM

# Module: AwsCryptographyMaterialProvidersOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAwsKmsKeyring(config, input):
        output: Wrappers.Result = None
        d_1248_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1248_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1248_valueOrError0_).IsFailure():
            output = (d_1248_valueOrError0_).PropagateFailure()
            return output
        d_1249___v0_: tuple
        d_1249___v0_ = (d_1248_valueOrError0_).Extract()
        d_1250_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1250_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1250_valueOrError1_).IsFailure():
            output = (d_1250_valueOrError1_).PropagateFailure()
            return output
        d_1251_grantTokens_: _dafny.Seq
        d_1251_grantTokens_ = (d_1250_valueOrError1_).Extract()
        d_1252_keyring_: AwsKmsKeyring.AwsKmsKeyring
        nw52_ = AwsKmsKeyring.AwsKmsKeyring()
        nw52_.ctor__((input).kmsClient, (input).kmsKeyId, d_1251_grantTokens_)
        d_1252_keyring_ = nw52_
        output = Wrappers.Result_Success(d_1252_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1253_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1253_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1253_valueOrError0_).IsFailure():
                output = (d_1253_valueOrError0_).PropagateFailure()
                return output
            d_1254___v1_: tuple
            d_1254___v1_ = (d_1253_valueOrError0_).Extract()
        d_1255_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1255_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1255_valueOrError1_).IsFailure():
            output = (d_1255_valueOrError1_).PropagateFailure()
            return output
        d_1256_grantTokens_: _dafny.Seq
        d_1256_grantTokens_ = (d_1255_valueOrError1_).Extract()
        d_1257_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
        nw53_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
        nw53_.ctor__((input).kmsClient, (input).discoveryFilter, d_1256_grantTokens_)
        d_1257_keyring_ = nw53_
        output = Wrappers.Result_Success(d_1257_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1258_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1258_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1258_valueOrError0_).IsFailure():
            output = (d_1258_valueOrError0_).PropagateFailure()
            return output
        d_1259_grantTokens_: _dafny.Seq
        d_1259_grantTokens_ = (d_1258_valueOrError0_).Extract()
        if ((input).clientSupplier).is_Some:
            out223_: Wrappers.Result
            out223_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, ((input).clientSupplier).value, Wrappers.Option_Some(d_1259_grantTokens_))
            output = out223_
        elif True:
            d_1260_valueOrError1_: Wrappers.Result = None
            out224_: Wrappers.Result
            out224_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1260_valueOrError1_ = out224_
            if (d_1260_valueOrError1_).IsFailure():
                output = (d_1260_valueOrError1_).PropagateFailure()
                return output
            d_1261_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
            d_1261_clientSupplier_ = (d_1260_valueOrError1_).Extract()
            out225_: Wrappers.Result
            out225_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1261_clientSupplier_, Wrappers.Option_Some(d_1259_grantTokens_))
            output = out225_
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1262_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1262_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1262_valueOrError0_).IsFailure():
            output = (d_1262_valueOrError0_).PropagateFailure()
            return output
        d_1263_grantTokens_: _dafny.Seq
        d_1263_grantTokens_ = (d_1262_valueOrError0_).Extract()
        d_1264_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1265_valueOrError1_: Wrappers.Result = None
            out226_: Wrappers.Result
            out226_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1265_valueOrError1_ = out226_
            if (d_1265_valueOrError1_).IsFailure():
                output = (d_1265_valueOrError1_).PropagateFailure()
                return output
            d_1264_clientSupplier_ = (d_1265_valueOrError1_).Extract()
        elif True:
            d_1264_clientSupplier_ = ((input).clientSupplier).value
        out227_: Wrappers.Result
        out227_ = DiscoveryMultiKeyring.default__.DiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1264_clientSupplier_, Wrappers.Option_Some(d_1263_grantTokens_))
        output = out227_
        return output

    @staticmethod
    def CreateAwsKmsMrkKeyring(config, input):
        output: Wrappers.Result = None
        d_1266_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1266_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1266_valueOrError0_).IsFailure():
            output = (d_1266_valueOrError0_).PropagateFailure()
            return output
        d_1267___v2_: tuple
        d_1267___v2_ = (d_1266_valueOrError0_).Extract()
        d_1268_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1268_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1268_valueOrError1_).IsFailure():
            output = (d_1268_valueOrError1_).PropagateFailure()
            return output
        d_1269_grantTokens_: _dafny.Seq
        d_1269_grantTokens_ = (d_1268_valueOrError1_).Extract()
        d_1270_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
        nw54_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
        nw54_.ctor__((input).kmsClient, (input).kmsKeyId, d_1269_grantTokens_)
        d_1270_keyring_ = nw54_
        output = Wrappers.Result_Success(d_1270_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1271_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1271_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1271_valueOrError0_).IsFailure():
            output = (d_1271_valueOrError0_).PropagateFailure()
            return output
        d_1272_grantTokens_: _dafny.Seq
        d_1272_grantTokens_ = (d_1271_valueOrError0_).Extract()
        d_1273_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1274_valueOrError1_: Wrappers.Result = None
            out228_: Wrappers.Result
            out228_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1274_valueOrError1_ = out228_
            if (d_1274_valueOrError1_).IsFailure():
                output = (d_1274_valueOrError1_).PropagateFailure()
                return output
            d_1273_clientSupplier_ = (d_1274_valueOrError1_).Extract()
        elif True:
            d_1273_clientSupplier_ = ((input).clientSupplier).value
        out229_: Wrappers.Result
        out229_ = MrkAwareStrictMultiKeyring.default__.MrkAwareStrictMultiKeyring((input).generator, (input).kmsKeyIds, d_1273_clientSupplier_, Wrappers.Option_Some(d_1272_grantTokens_))
        output = out229_
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_1275_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1275_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_1275_valueOrError0_).IsFailure():
                output = (d_1275_valueOrError0_).PropagateFailure()
                return output
            d_1276___v3_: tuple
            d_1276___v3_ = (d_1275_valueOrError0_).Extract()
        d_1277_regionMatch_: Wrappers.Option
        d_1277_regionMatch_ = Com_Amazonaws_Kms.default__.RegionMatch((input).kmsClient, (input).region)
        d_1278_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1278_valueOrError1_ = Wrappers.default__.Need((d_1277_regionMatch_) != (Wrappers.Option_Some(False)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Provided client and region do not match")))
        if (d_1278_valueOrError1_).IsFailure():
            output = (d_1278_valueOrError1_).PropagateFailure()
            return output
        d_1279_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1279_valueOrError2_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1279_valueOrError2_).IsFailure():
            output = (d_1279_valueOrError2_).PropagateFailure()
            return output
        d_1280_grantTokens_: _dafny.Seq
        d_1280_grantTokens_ = (d_1279_valueOrError2_).Extract()
        d_1281_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
        nw55_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
        nw55_.ctor__((input).kmsClient, (input).region, (input).discoveryFilter, d_1280_grantTokens_)
        d_1281_keyring_ = nw55_
        output = Wrappers.Result_Success(d_1281_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1282_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1282_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1282_valueOrError0_).IsFailure():
            output = (d_1282_valueOrError0_).PropagateFailure()
            return output
        d_1283_grantTokens_: _dafny.Seq
        d_1283_grantTokens_ = (d_1282_valueOrError0_).Extract()
        d_1284_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_1285_valueOrError1_: Wrappers.Result = None
            out230_: Wrappers.Result
            out230_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_1285_valueOrError1_ = out230_
            if (d_1285_valueOrError1_).IsFailure():
                output = (d_1285_valueOrError1_).PropagateFailure()
                return output
            d_1284_clientSupplier_ = (d_1285_valueOrError1_).Extract()
        elif True:
            d_1284_clientSupplier_ = ((input).clientSupplier).value
        out231_: Wrappers.Result
        out231_ = MrkAwareDiscoveryMultiKeyring.default__.MrkAwareDiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_1284_clientSupplier_, Wrappers.Option_Some(d_1283_grantTokens_))
        output = out231_
        return output

    @staticmethod
    def CreateAwsKmsHierarchicalKeyring(config, input):
        output: Wrappers.Result = None
        d_1286_maxCacheSize_: int = int(0)
        d_1287_cache_: AwsCryptographyMaterialProvidersTypes.CacheType
        if ((input).cache).is_Some:
            d_1287_cache_ = ((input).cache).value
        elif True:
            d_1287_cache_ = AwsCryptographyMaterialProvidersTypes.CacheType_Default(AwsCryptographyMaterialProvidersTypes.DefaultCache_DefaultCache(1000))
        d_1288_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1288_valueOrError0_ = Wrappers.default__.Need((((input).branchKeyId).is_None) or (((input).branchKeyIdSupplier).is_None), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")))
        if (d_1288_valueOrError0_).IsFailure():
            output = (d_1288_valueOrError0_).PropagateFailure()
            return output
        d_1289_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1289_valueOrError1_ = Wrappers.default__.Need((((input).branchKeyId).is_Some) or (((input).branchKeyIdSupplier).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")))
        if (d_1289_valueOrError1_).IsFailure():
            output = (d_1289_valueOrError1_).PropagateFailure()
            return output
        d_1290_valueOrError2_: Wrappers.Result = None
        out232_: Wrappers.Result
        out232_ = default__.CreateCryptographicMaterialsCache(config, AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(d_1287_cache_))
        d_1290_valueOrError2_ = out232_
        if (d_1290_valueOrError2_).IsFailure():
            output = (d_1290_valueOrError2_).PropagateFailure()
            return output
        d_1291_cmc_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
        d_1291_cmc_ = (d_1290_valueOrError2_).Extract()
        d_1292_keyring_: AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
        nw56_ = AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring()
        nw56_.ctor__((input).keyStore, (input).branchKeyId, (input).branchKeyIdSupplier, (input).ttlSeconds, d_1291_cmc_, (config).crypto)
        d_1292_keyring_ = nw56_
        output = Wrappers.Result_Success(d_1292_keyring_)
        return output
        return output

    @staticmethod
    def CreateMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_1293_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1293_valueOrError0_ = Wrappers.default__.Need((((input).generator).is_Some) or ((len((input).childKeyrings)) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must include a generator keyring and/or at least one child keyring")))
        if (d_1293_valueOrError0_).IsFailure():
            output = (d_1293_valueOrError0_).PropagateFailure()
            return output
        d_1294_keyring_: MultiKeyring.MultiKeyring
        nw57_ = MultiKeyring.MultiKeyring()
        nw57_.ctor__((input).generator, (input).childKeyrings)
        d_1294_keyring_ = nw57_
        output = Wrappers.Result_Success(d_1294_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawAesKeyring(config, input):
        output: Wrappers.Result = None
        d_1295_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1295_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1295_valueOrError0_).IsFailure():
            output = (d_1295_valueOrError0_).PropagateFailure()
            return output
        d_1296_wrappingAlg_: AwsCryptographyPrimitivesTypes.AES__GCM
        source33_ = (input).wrappingAlg
        with _dafny.label("match9"):
            if True:
                if source33_.is_ALG__AES128__GCM__IV12__TAG16:
                    d_1296_wrappingAlg_ = AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(16, 16, 12)
                    raise _dafny.Break("match9")
            if True:
                if source33_.is_ALG__AES192__GCM__IV12__TAG16:
                    d_1296_wrappingAlg_ = AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(24, 16, 12)
                    raise _dafny.Break("match9")
            if True:
                d_1296_wrappingAlg_ = AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(32, 16, 12)
            pass
        d_1297_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1297_valueOrError1_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1297_valueOrError1_).IsFailure():
            output = (d_1297_valueOrError1_).PropagateFailure()
            return output
        d_1298_namespaceAndName_: tuple
        d_1298_namespaceAndName_ = (d_1297_valueOrError1_).Extract()
        let_tmp_rhs5_ = d_1298_namespaceAndName_
        d_1299_namespace_ = let_tmp_rhs5_[0]
        d_1300_name_ = let_tmp_rhs5_[1]
        d_1301_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1301_valueOrError2_ = Wrappers.default__.Need((((len((input).wrappingKey)) == (16)) or ((len((input).wrappingKey)) == (24))) or ((len((input).wrappingKey)) == (32)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid wrapping key length")))
        if (d_1301_valueOrError2_).IsFailure():
            output = (d_1301_valueOrError2_).PropagateFailure()
            return output
        d_1302_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1302_valueOrError3_ = Wrappers.default__.Need((len((input).wrappingKey)) == ((d_1296_wrappingAlg_).keyLength), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrapping key length does not match specified wrapping algorithm")))
        if (d_1302_valueOrError3_).IsFailure():
            output = (d_1302_valueOrError3_).PropagateFailure()
            return output
        d_1303_keyring_: RawAESKeyring.RawAESKeyring
        nw58_ = RawAESKeyring.RawAESKeyring()
        nw58_.ctor__(d_1299_namespace_, d_1300_name_, (input).wrappingKey, d_1296_wrappingAlg_, (config).crypto)
        d_1303_keyring_ = nw58_
        output = Wrappers.Result_Success(d_1303_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1304_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1304_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_1304_valueOrError0_).IsFailure():
            output = (d_1304_valueOrError0_).PropagateFailure()
            return output
        d_1305_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1305_valueOrError1_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).privateKey).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a privateKey is required")))
        if (d_1305_valueOrError1_).IsFailure():
            output = (d_1305_valueOrError1_).PropagateFailure()
            return output
        d_1306_padding_: AwsCryptographyPrimitivesTypes.RSAPaddingMode
        source34_ = (input).paddingScheme
        with _dafny.label("match10"):
            if True:
                if source34_.is_PKCS1:
                    d_1306_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_PKCS1()
                    raise _dafny.Break("match10")
            if True:
                if source34_.is_OAEP__SHA1__MGF1:
                    d_1306_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA1()
                    raise _dafny.Break("match10")
            if True:
                if source34_.is_OAEP__SHA256__MGF1:
                    d_1306_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA256()
                    raise _dafny.Break("match10")
            if True:
                if source34_.is_OAEP__SHA384__MGF1:
                    d_1306_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA384()
                    raise _dafny.Break("match10")
            if True:
                d_1306_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA512()
            pass
        d_1307_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_1307_valueOrError2_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_1307_valueOrError2_).IsFailure():
            output = (d_1307_valueOrError2_).PropagateFailure()
            return output
        d_1308_namespaceAndName_: tuple
        d_1308_namespaceAndName_ = (d_1307_valueOrError2_).Extract()
        let_tmp_rhs6_ = d_1308_namespaceAndName_
        d_1309_namespace_ = let_tmp_rhs6_[0]
        d_1310_name_ = let_tmp_rhs6_[1]
        d_1311_keyring_: RawRSAKeyring.RawRSAKeyring
        nw59_ = RawRSAKeyring.RawRSAKeyring()
        nw59_.ctor__(d_1309_namespace_, d_1310_name_, (input).publicKey, (input).privateKey, d_1306_padding_, (config).crypto)
        d_1311_keyring_ = nw59_
        output = Wrappers.Result_Success(d_1311_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_1312_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1312_valueOrError0_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).kmsClient).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a kmsClient is required")))
        if (d_1312_valueOrError0_).IsFailure():
            output = (d_1312_valueOrError0_).PropagateFailure()
            return output
        d_1313_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1313_valueOrError1_ = Wrappers.default__.Need((((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__1) or (((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__256), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unsupported EncryptionAlgorithmSpec")))
        if (d_1313_valueOrError1_).IsFailure():
            output = (d_1313_valueOrError1_).PropagateFailure()
            return output
        d_1314_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1314_valueOrError2_ = Wrappers.default__.Need((ComAmazonawsKmsTypes.default__.IsValid__KeyIdType((input).kmsKeyId)) and ((AwsArnParsing.default__.ParseAwsKmsArn((input).kmsKeyId)).is_Success), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Kms Key ID must be a KMS Key ARN")))
        if (d_1314_valueOrError2_).IsFailure():
            output = (d_1314_valueOrError2_).PropagateFailure()
            return output
        if ((input).publicKey).is_Some:
            d_1315_lengthOutputRes_: Wrappers.Result
            d_1315_lengthOutputRes_ = ((config).crypto).GetRSAKeyModulusLength(AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(((input).publicKey).value))
            d_1316_valueOrError3_: Wrappers.Result = None
            def lambda103_(d_1317_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1317_e_)

            d_1316_valueOrError3_ = (d_1315_lengthOutputRes_).MapFailure(lambda103_)
            if (d_1316_valueOrError3_).IsFailure():
                output = (d_1316_valueOrError3_).PropagateFailure()
                return output
            d_1318_lengthOutput_: AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput
            d_1318_lengthOutput_ = (d_1316_valueOrError3_).Extract()
            d_1319_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_1319_valueOrError4_ = Wrappers.default__.Need(((d_1318_lengthOutput_).length) >= (AwsKmsRsaKeyring.default__.MIN__KMS__RSA__KEY__LEN), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid public key length")))
            if (d_1319_valueOrError4_).IsFailure():
                output = (d_1319_valueOrError4_).PropagateFailure()
                return output
        d_1320_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1320_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_1320_valueOrError5_).IsFailure():
            output = (d_1320_valueOrError5_).PropagateFailure()
            return output
        d_1321___v4_: tuple
        d_1321___v4_ = (d_1320_valueOrError5_).Extract()
        d_1322_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1322_valueOrError6_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_1322_valueOrError6_).IsFailure():
            output = (d_1322_valueOrError6_).PropagateFailure()
            return output
        d_1323_grantTokens_: _dafny.Seq
        d_1323_grantTokens_ = (d_1322_valueOrError6_).Extract()
        d_1324_keyring_: AwsKmsRsaKeyring.AwsKmsRsaKeyring
        nw60_ = AwsKmsRsaKeyring.AwsKmsRsaKeyring()
        nw60_.ctor__((input).publicKey, (input).kmsKeyId, (input).encryptionAlgorithm, (input).kmsClient, (config).crypto, d_1323_grantTokens_)
        d_1324_keyring_ = nw60_
        output = Wrappers.Result_Success(d_1324_keyring_)
        return output
        return output

    @staticmethod
    def CreateDefaultCryptographicMaterialsManager(config, input):
        output: Wrappers.Result = None
        d_1325_cmm_: DefaultCMM.DefaultCMM
        nw61_ = DefaultCMM.DefaultCMM()
        nw61_.OfKeyring((input).keyring, (config).crypto)
        d_1325_cmm_ = nw61_
        output = Wrappers.Result_Success(d_1325_cmm_)
        return output
        return output

    @staticmethod
    def CmpError(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def CreateRequiredEncryptionContextCMM(config, input):
        output: Wrappers.Result = None
        d_1326_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1326_valueOrError0_ = Wrappers.default__.Need((((input).underlyingCMM).is_Some) and (((input).keyring).is_None), default__.CmpError(_dafny.Seq("CreateRequiredEncryptionContextCMM currently only supports cmm.")))
        if (d_1326_valueOrError0_).IsFailure():
            output = (d_1326_valueOrError0_).PropagateFailure()
            return output
        d_1327_keySet_: _dafny.Set
        def iife30_():
            coll10_ = _dafny.Set()
            compr_10_: _dafny.Seq
            for compr_10_ in ((input).requiredEncryptionContextKeys).Elements:
                d_1328_k_: _dafny.Seq = compr_10_
                if UTF8.ValidUTF8Bytes._Is(d_1328_k_):
                    if (d_1328_k_) in ((input).requiredEncryptionContextKeys):
                        coll10_ = coll10_.union(_dafny.Set([d_1328_k_]))
            return _dafny.Set(coll10_)
        d_1327_keySet_ = iife30_()
        
        d_1329_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1329_valueOrError1_ = Wrappers.default__.Need((0) < (len(d_1327_keySet_)), default__.CmpError(_dafny.Seq("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")))
        if (d_1329_valueOrError1_).IsFailure():
            output = (d_1329_valueOrError1_).PropagateFailure()
            return output
        d_1330_cmm_: RequiredEncryptionContextCMM.RequiredEncryptionContextCMM
        nw62_ = RequiredEncryptionContextCMM.RequiredEncryptionContextCMM()
        nw62_.ctor__(((input).underlyingCMM).value, d_1327_keySet_)
        d_1330_cmm_ = nw62_
        output = Wrappers.Result_Success(d_1330_cmm_)
        return output
        return output

    @staticmethod
    def CreateCryptographicMaterialsCache(config, input):
        output: Wrappers.Result = None
        source35_ = (input).cache
        with _dafny.label("match11"):
            if True:
                if source35_.is_Default:
                    d_1331_c_ = source35_.Default
                    d_1332_cache_: AwsCryptographyMaterialProvidersTypes.StormTrackingCache
                    d_1333_dt__update__tmp_h0_ = StormTracker.default__.DefaultStorm()
                    d_1334_dt__update_hentryCapacity_h0_ = (d_1331_c_).entryCapacity
                    d_1332_cache_ = AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache(d_1334_dt__update_hentryCapacity_h0_, (d_1333_dt__update__tmp_h0_).entryPruningTailSize, (d_1333_dt__update__tmp_h0_).gracePeriod, (d_1333_dt__update__tmp_h0_).graceInterval, (d_1333_dt__update__tmp_h0_).fanOut, (d_1333_dt__update__tmp_h0_).inFlightTTL, (d_1333_dt__update__tmp_h0_).sleepMilli)
                    d_1335_cmc_: StormTracker.StormTracker
                    nw63_ = StormTracker.StormTracker()
                    nw63_.ctor__(d_1332_cache_)
                    d_1335_cmc_ = nw63_
                    d_1336_synCmc_: StormTrackingCMC.StormTrackingCMC
                    nw64_ = StormTrackingCMC.StormTrackingCMC(d_1335_cmc_)
                    d_1336_synCmc_ = nw64_
                    output = Wrappers.Result_Success(d_1336_synCmc_)
                    return output
                    raise _dafny.Break("match11")
            if True:
                if source35_.is_No:
                    d_1337_cmc_: LocalCMC.LocalCMC
                    nw65_ = LocalCMC.LocalCMC()
                    nw65_.ctor__(0, 1)
                    d_1337_cmc_ = nw65_
                    output = Wrappers.Result_Success(d_1337_cmc_)
                    return output
                    raise _dafny.Break("match11")
            if True:
                if source35_.is_SingleThreaded:
                    d_1338_c_ = source35_.SingleThreaded
                    d_1339_cmc_: LocalCMC.LocalCMC
                    nw66_ = LocalCMC.LocalCMC()
                    nw66_.ctor__((d_1338_c_).entryCapacity, (default__.OptionalCountingNumber((d_1338_c_).entryPruningTailSize)).UnwrapOr(1))
                    d_1339_cmc_ = nw66_
                    output = Wrappers.Result_Success(d_1339_cmc_)
                    return output
                    raise _dafny.Break("match11")
            if True:
                if source35_.is_MultiThreaded:
                    d_1340_c_ = source35_.MultiThreaded
                    d_1341_cmc_: LocalCMC.LocalCMC
                    nw67_ = LocalCMC.LocalCMC()
                    nw67_.ctor__((d_1340_c_).entryCapacity, (default__.OptionalCountingNumber((d_1340_c_).entryPruningTailSize)).UnwrapOr(1))
                    d_1341_cmc_ = nw67_
                    d_1342_synCmc_: SynchronizedLocalCMC.SynchronizedLocalCMC
                    nw68_ = SynchronizedLocalCMC.SynchronizedLocalCMC(d_1341_cmc_)
                    d_1342_synCmc_ = nw68_
                    output = Wrappers.Result_Success(d_1342_synCmc_)
                    return output
                    raise _dafny.Break("match11")
            if True:
                d_1343_c_ = source35_.StormTracking
                pat_let_tv28_ = d_1343_c_
                d_1344_cmc_: StormTracker.StormTracker
                nw69_ = StormTracker.StormTracker()
                def iife31_(_pat_let10_0):
                    def iife32_(d_1345_dt__update__tmp_h1_):
                        def iife33_(_pat_let11_0):
                            def iife34_(d_1346_dt__update_hentryPruningTailSize_h0_):
                                return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_1345_dt__update__tmp_h1_).entryCapacity, d_1346_dt__update_hentryPruningTailSize_h0_, (d_1345_dt__update__tmp_h1_).gracePeriod, (d_1345_dt__update__tmp_h1_).graceInterval, (d_1345_dt__update__tmp_h1_).fanOut, (d_1345_dt__update__tmp_h1_).inFlightTTL, (d_1345_dt__update__tmp_h1_).sleepMilli)
                            return iife34_(_pat_let11_0)
                        return iife33_(default__.OptionalCountingNumber((pat_let_tv28_).entryPruningTailSize))
                    return iife32_(_pat_let10_0)
                nw69_.ctor__(iife31_(d_1343_c_))
                d_1344_cmc_ = nw69_
                d_1347_synCmc_: StormTrackingCMC.StormTrackingCMC
                nw70_ = StormTrackingCMC.StormTrackingCMC(d_1344_cmc_)
                d_1347_synCmc_ = nw70_
                output = Wrappers.Result_Success(d_1347_synCmc_)
                return output
            pass
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
        d_1348_clientSupplier_: DefaultClientSupplier.DefaultClientSupplier
        nw71_ = DefaultClientSupplier.DefaultClientSupplier()
        nw71_.ctor__()
        d_1348_clientSupplier_ = nw71_
        output = Wrappers.Result_Success(d_1348_clientSupplier_)
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
        d_1349_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).start, (input).stop), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Invalid Encryption Materials Transition")))
        if (d_1349_valueOrError0_).IsFailure():
            return (d_1349_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidDecryptionMaterialsTransition(config, input):
        d_1350_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).start, (input).stop), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Invalid Decryption Materials Transition")))
        if (d_1350_valueOrError0_).IsFailure():
            return (d_1350_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(config, input):
        d_1351_valueOrError0_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Encryption Materials")))
        if (d_1351_valueOrError0_).IsFailure():
            return (d_1351_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(config, input):
        d_1352_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Decryption Materials")))
        if (d_1352_valueOrError0_).IsFailure():
            return (d_1352_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def GetAlgorithmSuiteInfo(config, input):
        return AlgorithmSuites.default__.GetAlgorithmSuiteInfo(input)

    @staticmethod
    def ValidAlgorithmSuiteInfo(config, input):
        d_1353_valueOrError0_ = Wrappers.default__.Need(AlgorithmSuites.default__.AlgorithmSuite_q(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidAlgorithmSuiteInfo(_dafny.Seq("Invalid AlgorithmSuiteInfo")))
        if (d_1353_valueOrError0_).IsFailure():
            return (d_1353_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(config, input):
        d_1354_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1354_valueOrError0_).IsFailure():
            return (d_1354_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(config, input):
        d_1355_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithm, (input).commitmentPolicy)
        if (d_1355_valueOrError0_).IsFailure():
            return (d_1355_valueOrError0_).PropagateFailure()
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

