import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.CacheConstants as CacheConstants
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM

# Module: AwsCryptographyMaterialProvidersOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAwsKmsKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_0_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1___v0_: tuple
        d_1___v0_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_2_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_2_valueOrError1_).IsFailure():
            output = (d_2_valueOrError1_).PropagateFailure()
            return output
        d_3_grantTokens_: _dafny.Seq
        d_3_grantTokens_ = (d_2_valueOrError1_).Extract()
        d_4_keyring_: AwsKmsKeyring.AwsKmsKeyring
        nw0_ = AwsKmsKeyring.AwsKmsKeyring()
        nw0_.ctor__((input).kmsClient, (input).kmsKeyId, d_3_grantTokens_)
        d_4_keyring_ = nw0_
        output = Wrappers.Result_Success(d_4_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_0_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_0_valueOrError0_).IsFailure():
                output = (d_0_valueOrError0_).PropagateFailure()
                return output
            d_1___v1_: tuple
            d_1___v1_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_2_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_2_valueOrError1_).IsFailure():
            output = (d_2_valueOrError1_).PropagateFailure()
            return output
        d_3_grantTokens_: _dafny.Seq
        d_3_grantTokens_ = (d_2_valueOrError1_).Extract()
        d_4_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
        nw0_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
        nw0_.ctor__((input).kmsClient, (input).discoveryFilter, d_3_grantTokens_)
        d_4_keyring_ = nw0_
        output = Wrappers.Result_Success(d_4_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_grantTokens_: _dafny.Seq
        d_1_grantTokens_ = (d_0_valueOrError0_).Extract()
        if ((input).clientSupplier).is_Some:
            out0_: Wrappers.Result
            out0_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, ((input).clientSupplier).value, Wrappers.Option_Some(d_1_grantTokens_))
            output = out0_
        elif True:
            d_2_valueOrError1_: Wrappers.Result = None
            out1_: Wrappers.Result
            out1_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_2_valueOrError1_ = out1_
            if (d_2_valueOrError1_).IsFailure():
                output = (d_2_valueOrError1_).PropagateFailure()
                return output
            d_3_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
            d_3_clientSupplier_ = (d_2_valueOrError1_).Extract()
            out2_: Wrappers.Result
            out2_ = StrictMultiKeyring.default__.StrictMultiKeyring((input).generator, (input).kmsKeyIds, d_3_clientSupplier_, Wrappers.Option_Some(d_1_grantTokens_))
            output = out2_
        return output

    @staticmethod
    def CreateAwsKmsDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_grantTokens_: _dafny.Seq
        d_1_grantTokens_ = (d_0_valueOrError0_).Extract()
        d_2_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_3_valueOrError1_: Wrappers.Result = None
            out0_: Wrappers.Result
            out0_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_3_valueOrError1_ = out0_
            if (d_3_valueOrError1_).IsFailure():
                output = (d_3_valueOrError1_).PropagateFailure()
                return output
            d_2_clientSupplier_ = (d_3_valueOrError1_).Extract()
        elif True:
            d_2_clientSupplier_ = ((input).clientSupplier).value
        out1_: Wrappers.Result
        out1_ = DiscoveryMultiKeyring.default__.DiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_2_clientSupplier_, Wrappers.Option_Some(d_1_grantTokens_))
        output = out1_
        return output

    @staticmethod
    def CreateAwsKmsMrkKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_0_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1___v2_: tuple
        d_1___v2_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_2_valueOrError1_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_2_valueOrError1_).IsFailure():
            output = (d_2_valueOrError1_).PropagateFailure()
            return output
        d_3_grantTokens_: _dafny.Seq
        d_3_grantTokens_ = (d_2_valueOrError1_).Extract()
        d_4_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
        nw0_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
        nw0_.ctor__((input).kmsClient, (input).kmsKeyId, d_3_grantTokens_)
        d_4_keyring_ = nw0_
        output = Wrappers.Result_Success(d_4_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_grantTokens_: _dafny.Seq
        d_1_grantTokens_ = (d_0_valueOrError0_).Extract()
        d_2_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_3_valueOrError1_: Wrappers.Result = None
            out0_: Wrappers.Result
            out0_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_3_valueOrError1_ = out0_
            if (d_3_valueOrError1_).IsFailure():
                output = (d_3_valueOrError1_).PropagateFailure()
                return output
            d_2_clientSupplier_ = (d_3_valueOrError1_).Extract()
        elif True:
            d_2_clientSupplier_ = ((input).clientSupplier).value
        out1_: Wrappers.Result
        out1_ = MrkAwareStrictMultiKeyring.default__.MrkAwareStrictMultiKeyring((input).generator, (input).kmsKeyIds, d_2_clientSupplier_, Wrappers.Option_Some(d_1_grantTokens_))
        output = out1_
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryKeyring(config, input):
        output: Wrappers.Result = None
        if ((input).discoveryFilter).is_Some:
            d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_0_valueOrError0_ = AwsKmsUtils.default__.ValidateDiscoveryFilter(((input).discoveryFilter).value)
            if (d_0_valueOrError0_).IsFailure():
                output = (d_0_valueOrError0_).PropagateFailure()
                return output
            d_1___v3_: tuple
            d_1___v3_ = (d_0_valueOrError0_).Extract()
        d_2_regionMatch_: Wrappers.Option
        d_2_regionMatch_ = Com_Amazonaws_Kms.default__.RegionMatch((input).kmsClient, (input).region)
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need((d_2_regionMatch_) != (Wrappers.Option_Some(False)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Provided client and region do not match")))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_4_valueOrError2_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5_grantTokens_: _dafny.Seq
        d_5_grantTokens_ = (d_4_valueOrError2_).Extract()
        d_6_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
        nw0_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
        nw0_.ctor__((input).kmsClient, (input).region, (input).discoveryFilter, d_5_grantTokens_)
        d_6_keyring_ = nw0_
        output = Wrappers.Result_Success(d_6_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsMrkDiscoveryMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_grantTokens_: _dafny.Seq
        d_1_grantTokens_ = (d_0_valueOrError0_).Extract()
        d_2_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier = None
        if ((input).clientSupplier).is_None:
            d_3_valueOrError1_: Wrappers.Result = None
            out0_: Wrappers.Result
            out0_ = default__.CreateDefaultClientSupplier(config, AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
            d_3_valueOrError1_ = out0_
            if (d_3_valueOrError1_).IsFailure():
                output = (d_3_valueOrError1_).PropagateFailure()
                return output
            d_2_clientSupplier_ = (d_3_valueOrError1_).Extract()
        elif True:
            d_2_clientSupplier_ = ((input).clientSupplier).value
        out1_: Wrappers.Result
        out1_ = MrkAwareDiscoveryMultiKeyring.default__.MrkAwareDiscoveryMultiKeyring((input).regions, (input).discoveryFilter, d_2_clientSupplier_, Wrappers.Option_Some(d_1_grantTokens_))
        output = out1_
        return output

    @staticmethod
    def N(n):
        return StandardLibrary_String.default__.Base10Int2String(n)

    @staticmethod
    def CheckCache(cache, ttlSeconds):
        output: Wrappers.Outcome = Wrappers.Outcome.default()()
        if (cache).is_StormTracking:
            d_0_gracePeriod_: int
            if ((((cache).StormTracking).timeUnits).UnwrapOr(AwsCryptographyMaterialProvidersTypes.TimeUnits_Seconds())).is_Seconds:
                d_0_gracePeriod_ = ((cache).StormTracking).gracePeriod
            elif True:
                d_0_gracePeriod_ = _dafny.euclidian_division(((cache).StormTracking).gracePeriod, 1000)
            d_1_storm_: AwsCryptographyMaterialProvidersTypes.StormTrackingCache
            d_1_storm_ = (cache).StormTracking
            if (ttlSeconds) <= (d_0_gracePeriod_):
                d_2_msg_: _dafny.Seq
                d_2_msg_ = ((((((_dafny.Seq("When creating an AwsKmsHierarchicalKeyring with a StormCache, ")) + (_dafny.Seq("the ttlSeconds of the KeyRing must be greater than the gracePeriod of the StormCache "))) + (_dafny.Seq("yet the ttlSeconds is "))) + (default__.N(ttlSeconds))) + (_dafny.Seq(" and the gracePeriod is "))) + (default__.N(d_0_gracePeriod_))) + (_dafny.Seq("."))
                output = Wrappers.Outcome_Fail(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_2_msg_))
                return output
            output = Wrappers.Outcome_Pass()
            return output
        elif True:
            output = Wrappers.Outcome_Pass()
            return output
        return output

    @staticmethod
    def CreateAwsKmsHierarchicalKeyring(config, input):
        output: Wrappers.Result = None
        d_0_cmc_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache = None
        if ((input).cache).is_Some:
            d_1_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
            out0_: Wrappers.Outcome
            out0_ = default__.CheckCache(((input).cache).value, (input).ttlSeconds)
            d_1_valueOrError0_ = out0_
            if (d_1_valueOrError0_).IsFailure():
                output = (d_1_valueOrError0_).PropagateFailure()
                return output
            source0_ = ((input).cache).value
            with _dafny.label("match0"):
                if True:
                    if source0_.is_Shared:
                        d_2_c_ = source0_.Shared
                        d_0_cmc_ = d_2_c_
                        raise _dafny.Break("match0")
                if True:
                    d_3_valueOrError1_: Wrappers.Result = None
                    out1_: Wrappers.Result
                    out1_ = default__.CreateCryptographicMaterialsCache(config, AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(((input).cache).value))
                    d_3_valueOrError1_ = out1_
                    if (d_3_valueOrError1_).IsFailure():
                        output = (d_3_valueOrError1_).PropagateFailure()
                        return output
                    d_0_cmc_ = (d_3_valueOrError1_).Extract()
                pass
        elif True:
            d_4_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            out2_: Wrappers.Outcome
            out2_ = default__.CheckCache(AwsCryptographyMaterialProvidersTypes.CacheType_StormTracking(StormTracker.default__.DefaultStorm()), (input).ttlSeconds)
            d_4_valueOrError2_ = out2_
            if (d_4_valueOrError2_).IsFailure():
                output = (d_4_valueOrError2_).PropagateFailure()
                return output
            d_5_valueOrError3_: Wrappers.Result = None
            out3_: Wrappers.Result
            out3_ = default__.CreateCryptographicMaterialsCache(config, AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(AwsCryptographyMaterialProvidersTypes.CacheType_Default(AwsCryptographyMaterialProvidersTypes.DefaultCache_DefaultCache(1000))))
            d_5_valueOrError3_ = out3_
            if (d_5_valueOrError3_).IsFailure():
                output = (d_5_valueOrError3_).PropagateFailure()
                return output
            d_0_cmc_ = (d_5_valueOrError3_).Extract()
        d_6_partitionIdBytes_: _dafny.Seq = _dafny.Seq({})
        if ((input).partitionId).is_Some:
            d_7_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
            def lambda0_(d_8_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Could not UTF-8 Encode Partition ID: ")) + (d_8_e_))

            d_7_valueOrError4_ = (UTF8.default__.Encode(((input).partitionId).value)).MapFailure(lambda0_)
            if (d_7_valueOrError4_).IsFailure():
                output = (d_7_valueOrError4_).PropagateFailure()
                return output
            d_6_partitionIdBytes_ = (d_7_valueOrError4_).Extract()
        elif True:
            d_9_uuid_q_: Wrappers.Result
            out4_: Wrappers.Result
            out4_ = UUID.default__.GenerateUUID()
            d_9_uuid_q_ = out4_
            d_10_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda1_(d_11_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_11_e_)

            d_10_valueOrError5_ = (d_9_uuid_q_).MapFailure(lambda1_)
            if (d_10_valueOrError5_).IsFailure():
                output = (d_10_valueOrError5_).PropagateFailure()
                return output
            d_12_uuid_: _dafny.Seq
            d_12_uuid_ = (d_10_valueOrError5_).Extract()
            d_13_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda2_(d_14_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_14_e_)

            d_13_valueOrError6_ = (UUID.default__.ToByteArray(d_12_uuid_)).MapFailure(lambda2_)
            if (d_13_valueOrError6_).IsFailure():
                output = (d_13_valueOrError6_).PropagateFailure()
                return output
            d_6_partitionIdBytes_ = (d_13_valueOrError6_).Extract()
        d_15_getKeyStoreInfoOutput_q_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = ((input).keyStore).GetKeyStoreInfo()
        d_15_getKeyStoreInfoOutput_q_ = out5_
        d_16_valueOrError7_: Wrappers.Result = None
        def lambda3_(d_17_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_17_e_)

        d_16_valueOrError7_ = (d_15_getKeyStoreInfoOutput_q_).MapFailure(lambda3_)
        if (d_16_valueOrError7_).IsFailure():
            output = (d_16_valueOrError7_).PropagateFailure()
            return output
        d_18_getKeyStoreInfoOutput_: AwsCryptographyKeyStoreTypes.GetKeyStoreInfoOutput
        d_18_getKeyStoreInfoOutput_ = (d_16_valueOrError7_).Extract()
        d_19_logicalKeyStoreName_: _dafny.Seq
        d_19_logicalKeyStoreName_ = (d_18_getKeyStoreInfoOutput_).logicalKeyStoreName
        d_20_valueOrError8_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        def lambda4_(d_21_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Could not UTF-8 Encode Logical Key Store Name: ")) + (d_21_e_))

        d_20_valueOrError8_ = (UTF8.default__.Encode(d_19_logicalKeyStoreName_)).MapFailure(lambda4_)
        if (d_20_valueOrError8_).IsFailure():
            output = (d_20_valueOrError8_).PropagateFailure()
            return output
        d_22_logicalKeyStoreNameBytes_: _dafny.Seq
        d_22_logicalKeyStoreNameBytes_ = (d_20_valueOrError8_).Extract()
        d_23_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_23_valueOrError9_ = Wrappers.default__.Need((((input).branchKeyId).is_None) or (((input).branchKeyIdSupplier).is_None), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")))
        if (d_23_valueOrError9_).IsFailure():
            output = (d_23_valueOrError9_).PropagateFailure()
            return output
        d_24_valueOrError10_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_24_valueOrError10_ = Wrappers.default__.Need((((input).branchKeyId).is_Some) or (((input).branchKeyIdSupplier).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")))
        if (d_24_valueOrError10_).IsFailure():
            output = (d_24_valueOrError10_).PropagateFailure()
            return output
        d_25_keyring_: AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
        nw0_ = AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring()
        nw0_.ctor__((input).keyStore, (input).branchKeyId, (input).branchKeyIdSupplier, (input).ttlSeconds, d_0_cmc_, d_6_partitionIdBytes_, d_22_logicalKeyStoreNameBytes_, (config).crypto)
        d_25_keyring_ = nw0_
        output = Wrappers.Result_Success(d_25_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsEcdhKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_grantTokens_: _dafny.Seq
        d_1_grantTokens_ = (d_0_valueOrError0_).Extract()
        d_2_recipientPublicKey_: _dafny.Seq = None
        d_3_senderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        d_4_compressedSenderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        source0_ = (input).KeyAgreementScheme
        with _dafny.label("match0"):
            if True:
                if source0_.is_KmsPublicKeyDiscovery:
                    d_5_kmsPublicKeyDiscovery_ = source0_.KmsPublicKeyDiscovery
                    if True:
                        d_6_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                        d_6_valueOrError1_ = AwsKmsUtils.default__.ValidateKmsKeyId((d_5_kmsPublicKeyDiscovery_).recipientKmsIdentifier)
                        if (d_6_valueOrError1_).IsFailure():
                            output = (d_6_valueOrError1_).PropagateFailure()
                            return output
                        d_7___v5_: tuple
                        d_7___v5_ = (d_6_valueOrError1_).Extract()
                        d_8_valueOrError2_: Wrappers.Result = None
                        out0_: Wrappers.Result
                        out0_ = AwsKmsUtils.default__.GetEcdhPublicKey((input).kmsClient, (d_5_kmsPublicKeyDiscovery_).recipientKmsIdentifier)
                        d_8_valueOrError2_ = out0_
                        if (d_8_valueOrError2_).IsFailure():
                            output = (d_8_valueOrError2_).PropagateFailure()
                            return output
                        d_2_recipientPublicKey_ = (d_8_valueOrError2_).Extract()
                        d_3_senderPublicKey_ = Wrappers.Option_None()
                        d_4_compressedSenderPublicKey_ = Wrappers.Option_None()
                    raise _dafny.Break("match0")
            if True:
                d_9_kmsPrivateKeyToStaticPublicKey_ = source0_.KmsPrivateKeyToStaticPublicKey
                if True:
                    if ((d_9_kmsPrivateKeyToStaticPublicKey_).senderPublicKey).is_Some:
                        d_10_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_10_valueOrError3_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType(((d_9_kmsPrivateKeyToStaticPublicKey_).senderPublicKey).value), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid SenderPublicKey length.")))
                        if (d_10_valueOrError3_).IsFailure():
                            output = (d_10_valueOrError3_).PropagateFailure()
                            return output
                        d_3_senderPublicKey_ = Wrappers.Option_Some(((d_9_kmsPrivateKeyToStaticPublicKey_).senderPublicKey).value)
                        d_11_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                        out1_: Wrappers.Result
                        out1_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_3_senderPublicKey_).value), (input).curveSpec, (config).crypto)
                        d_11_valueOrError4_ = out1_
                        if (d_11_valueOrError4_).IsFailure():
                            output = (d_11_valueOrError4_).PropagateFailure()
                            return output
                        d_12_compressedPKU_: _dafny.Seq
                        d_12_compressedPKU_ = (d_11_valueOrError4_).Extract()
                        d_4_compressedSenderPublicKey_ = Wrappers.Option_Some(d_12_compressedPKU_)
                    elif True:
                        d_13_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                        d_13_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((d_9_kmsPrivateKeyToStaticPublicKey_).senderKmsIdentifier)
                        if (d_13_valueOrError5_).IsFailure():
                            output = (d_13_valueOrError5_).PropagateFailure()
                            return output
                        d_14___v6_: tuple
                        d_14___v6_ = (d_13_valueOrError5_).Extract()
                        d_15_valueOrError6_: Wrappers.Result = None
                        out2_: Wrappers.Result
                        out2_ = AwsKmsUtils.default__.GetEcdhPublicKey((input).kmsClient, (d_9_kmsPrivateKeyToStaticPublicKey_).senderKmsIdentifier)
                        d_15_valueOrError6_ = out2_
                        if (d_15_valueOrError6_).IsFailure():
                            output = (d_15_valueOrError6_).PropagateFailure()
                            return output
                        d_16_senderPublicKeyResponse_: _dafny.Seq
                        d_16_senderPublicKeyResponse_ = (d_15_valueOrError6_).Extract()
                        d_17_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                        out3_: Wrappers.Result
                        out3_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_16_senderPublicKeyResponse_), (input).curveSpec, (config).crypto)
                        d_17_valueOrError7_ = out3_
                        if (d_17_valueOrError7_).IsFailure():
                            output = (d_17_valueOrError7_).PropagateFailure()
                            return output
                        d_18_compressedPKU_: _dafny.Seq
                        d_18_compressedPKU_ = (d_17_valueOrError7_).Extract()
                        d_3_senderPublicKey_ = Wrappers.Option_Some(d_16_senderPublicKeyResponse_)
                        d_4_compressedSenderPublicKey_ = Wrappers.Option_Some(d_18_compressedPKU_)
                    d_19_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_19_valueOrError8_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType((d_9_kmsPrivateKeyToStaticPublicKey_).recipientPublicKey), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid RecipientPublicKey length.")))
                    if (d_19_valueOrError8_).IsFailure():
                        output = (d_19_valueOrError8_).PropagateFailure()
                        return output
                    d_2_recipientPublicKey_ = (d_9_kmsPrivateKeyToStaticPublicKey_).recipientPublicKey
            pass
        d_20_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out4_: Wrappers.Result
        out4_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, d_2_recipientPublicKey_)
        d_20_valueOrError9_ = out4_
        if (d_20_valueOrError9_).IsFailure():
            output = (d_20_valueOrError9_).PropagateFailure()
            return output
        d_21___v7_: bool
        d_21___v7_ = (d_20_valueOrError9_).Extract()
        d_22_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out5_: Wrappers.Result
        out5_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_2_recipientPublicKey_), (input).curveSpec, (config).crypto)
        d_22_valueOrError10_ = out5_
        if (d_22_valueOrError10_).IsFailure():
            output = (d_22_valueOrError10_).PropagateFailure()
            return output
        d_23_compressedRecipientPublicKey_: _dafny.Seq
        d_23_compressedRecipientPublicKey_ = (d_22_valueOrError10_).Extract()
        d_24_senderKmsKeyId_: Wrappers.Option
        if ((input).KeyAgreementScheme).is_KmsPublicKeyDiscovery:
            d_24_senderKmsKeyId_ = Wrappers.Option_None()
        elif True:
            d_24_senderKmsKeyId_ = Wrappers.Option_Some((((input).KeyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderKmsIdentifier)
        if (d_24_senderKmsKeyId_).is_Some:
            d_25_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_25_valueOrError11_ = AwsKmsUtils.default__.ValidateKmsKeyId((d_24_senderKmsKeyId_).value)
            if (d_25_valueOrError11_).IsFailure():
                output = (d_25_valueOrError11_).PropagateFailure()
                return output
            d_26___v8_: tuple
            d_26___v8_ = (d_25_valueOrError11_).Extract()
        if (d_3_senderPublicKey_).is_Some:
            d_27_valueOrError12_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
            out6_: Wrappers.Result
            out6_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, (d_3_senderPublicKey_).value)
            d_27_valueOrError12_ = out6_
            if (d_27_valueOrError12_).IsFailure():
                output = (d_27_valueOrError12_).PropagateFailure()
                return output
            d_28___v9_: bool
            d_28___v9_ = (d_27_valueOrError12_).Extract()
        d_29_keyring_: AwsKmsEcdhKeyring.AwsKmsEcdhKeyring
        nw0_ = AwsKmsEcdhKeyring.AwsKmsEcdhKeyring()
        nw0_.ctor__((input).KeyAgreementScheme, (input).curveSpec, (input).kmsClient, d_1_grantTokens_, d_24_senderKmsKeyId_, d_3_senderPublicKey_, d_2_recipientPublicKey_, d_4_compressedSenderPublicKey_, d_23_compressedRecipientPublicKey_, (config).crypto)
        d_29_keyring_ = nw0_
        output = Wrappers.Result_Success(d_29_keyring_)
        return output
        return output

    @staticmethod
    def CreateMultiKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need((((input).generator).is_Some) or ((len((input).childKeyrings)) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Must include a generator keyring and/or at least one child keyring")))
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_keyring_: MultiKeyring.MultiKeyring
        nw0_ = MultiKeyring.MultiKeyring()
        nw0_.ctor__((input).generator, (input).childKeyrings)
        d_1_keyring_ = nw0_
        output = Wrappers.Result_Success(d_1_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawAesKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_wrappingAlg_: AwsCryptographyPrimitivesTypes.AES__GCM
        source0_ = (input).wrappingAlg
        with _dafny.label("match0"):
            if True:
                if source0_.is_ALG__AES128__GCM__IV12__TAG16:
                    d_1_wrappingAlg_ = AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(16, 16, 12)
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_ALG__AES192__GCM__IV12__TAG16:
                    d_1_wrappingAlg_ = AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(24, 16, 12)
                    raise _dafny.Break("match0")
            if True:
                d_1_wrappingAlg_ = AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(32, 16, 12)
            pass
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_2_valueOrError1_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_2_valueOrError1_).IsFailure():
            output = (d_2_valueOrError1_).PropagateFailure()
            return output
        d_3_namespaceAndName_: tuple
        d_3_namespaceAndName_ = (d_2_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_3_namespaceAndName_
        d_4_namespace_ = let_tmp_rhs0_[0]
        d_5_name_ = let_tmp_rhs0_[1]
        d_6_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError2_ = Wrappers.default__.Need((((len((input).wrappingKey)) == (16)) or ((len((input).wrappingKey)) == (24))) or ((len((input).wrappingKey)) == (32)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid wrapping key length")))
        if (d_6_valueOrError2_).IsFailure():
            output = (d_6_valueOrError2_).PropagateFailure()
            return output
        d_7_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError3_ = Wrappers.default__.Need((len((input).wrappingKey)) == ((d_1_wrappingAlg_).keyLength), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Wrapping key length does not match specified wrapping algorithm")))
        if (d_7_valueOrError3_).IsFailure():
            output = (d_7_valueOrError3_).PropagateFailure()
            return output
        d_8_keyring_: RawAESKeyring.RawAESKeyring
        nw0_ = RawAESKeyring.RawAESKeyring()
        nw0_.ctor__(d_4_namespace_, d_5_name_, (input).wrappingKey, d_1_wrappingAlg_, (config).crypto)
        d_8_keyring_ = nw0_
        output = Wrappers.Result_Success(d_8_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(((input).keyNamespace) != (_dafny.Seq("aws-kms")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("keyNamespace must not be `aws-kms`")))
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError1_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).privateKey).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a privateKey is required")))
        if (d_1_valueOrError1_).IsFailure():
            output = (d_1_valueOrError1_).PropagateFailure()
            return output
        d_2_padding_: AwsCryptographyPrimitivesTypes.RSAPaddingMode
        source0_ = (input).paddingScheme
        with _dafny.label("match0"):
            if True:
                if source0_.is_PKCS1:
                    d_2_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_PKCS1()
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_OAEP__SHA1__MGF1:
                    d_2_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA1()
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_OAEP__SHA256__MGF1:
                    d_2_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA256()
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_OAEP__SHA384__MGF1:
                    d_2_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA384()
                    raise _dafny.Break("match0")
            if True:
                d_2_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA512()
            pass
        d_3_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple(UTF8.ValidUTF8Bytes.default, UTF8.ValidUTF8Bytes.default))()
        d_3_valueOrError2_ = AwsKmsUtils.default__.ParseKeyNamespaceAndName((input).keyNamespace, (input).keyName)
        if (d_3_valueOrError2_).IsFailure():
            output = (d_3_valueOrError2_).PropagateFailure()
            return output
        d_4_namespaceAndName_: tuple
        d_4_namespaceAndName_ = (d_3_valueOrError2_).Extract()
        let_tmp_rhs0_ = d_4_namespaceAndName_
        d_5_namespace_ = let_tmp_rhs0_[0]
        d_6_name_ = let_tmp_rhs0_[1]
        d_7_keyring_: RawRSAKeyring.RawRSAKeyring
        nw0_ = RawRSAKeyring.RawRSAKeyring()
        nw0_.ctor__(d_5_namespace_, d_6_name_, (input).publicKey, (input).privateKey, d_2_padding_, (config).crypto)
        d_7_keyring_ = nw0_
        output = Wrappers.Result_Success(d_7_keyring_)
        return output
        return output

    @staticmethod
    def CreateRawEcdhKeyring(config, input):
        output: Wrappers.Result = None
        d_0_recipientPublicKey_: _dafny.Seq = _dafny.Seq({})
        d_1_senderPrivateKey_: Wrappers.Option = Wrappers.Option.default()()
        d_2_senderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        d_3_compressedSenderPublicKey_: Wrappers.Option = Wrappers.Option.default()()
        source0_ = (input).KeyAgreementScheme
        with _dafny.label("match0"):
            if True:
                if source0_.is_RawPrivateKeyToStaticPublicKey:
                    d_4_rawPrivateKeyToStaticPublicKey_ = source0_.RawPrivateKeyToStaticPublicKey
                    if True:
                        d_0_recipientPublicKey_ = (d_4_rawPrivateKeyToStaticPublicKey_).recipientPublicKey
                        d_1_senderPrivateKey_ = Wrappers.Option_Some((d_4_rawPrivateKeyToStaticPublicKey_).senderStaticPrivateKey)
                        d_5_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                        out0_: Wrappers.Result
                        out0_ = Utils.default__.GetPublicKey((input).curveSpec, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey((d_1_senderPrivateKey_).value), (config).crypto)
                        d_5_valueOrError0_ = out0_
                        if (d_5_valueOrError0_).IsFailure():
                            output = (d_5_valueOrError0_).PropagateFailure()
                            return output
                        d_6_reproducedPublicKey_: _dafny.Seq
                        d_6_reproducedPublicKey_ = (d_5_valueOrError0_).Extract()
                        d_7_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
                        out1_: Wrappers.Result
                        out1_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, d_6_reproducedPublicKey_)
                        d_7_valueOrError1_ = out1_
                        if (d_7_valueOrError1_).IsFailure():
                            output = (d_7_valueOrError1_).PropagateFailure()
                            return output
                        d_8___v10_: bool
                        d_8___v10_ = (d_7_valueOrError1_).Extract()
                        d_2_senderPublicKey_ = Wrappers.Option_Some(d_6_reproducedPublicKey_)
                        d_9_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                        out2_: Wrappers.Result
                        out2_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_6_reproducedPublicKey_), (input).curveSpec, (config).crypto)
                        d_9_valueOrError2_ = out2_
                        if (d_9_valueOrError2_).IsFailure():
                            output = (d_9_valueOrError2_).PropagateFailure()
                            return output
                        d_10_compressedSenderPublicKey_q_: _dafny.Seq
                        d_10_compressedSenderPublicKey_q_ = (d_9_valueOrError2_).Extract()
                        d_3_compressedSenderPublicKey_ = Wrappers.Option_Some(d_10_compressedSenderPublicKey_q_)
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_EphemeralPrivateKeyToStaticPublicKey:
                    d_11_ephemeralPrivateKeyToStaticPublicKey_ = source0_.EphemeralPrivateKeyToStaticPublicKey
                    if True:
                        d_0_recipientPublicKey_ = (d_11_ephemeralPrivateKeyToStaticPublicKey_).recipientPublicKey
                        d_1_senderPrivateKey_ = Wrappers.Option_None()
                        d_2_senderPublicKey_ = Wrappers.Option_None()
                        d_3_compressedSenderPublicKey_ = Wrappers.Option_None()
                    raise _dafny.Break("match0")
            if True:
                d_12_publicKeyDiscovery_ = source0_.PublicKeyDiscovery
                if True:
                    d_13_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                    out3_: Wrappers.Result
                    out3_ = Utils.default__.GetPublicKey((input).curveSpec, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey((d_12_publicKeyDiscovery_).recipientStaticPrivateKey), (config).crypto)
                    d_13_valueOrError3_ = out3_
                    if (d_13_valueOrError3_).IsFailure():
                        output = (d_13_valueOrError3_).PropagateFailure()
                        return output
                    d_14_reproducedPublicKey_: _dafny.Seq
                    d_14_reproducedPublicKey_ = (d_13_valueOrError3_).Extract()
                    d_0_recipientPublicKey_ = d_14_reproducedPublicKey_
                    d_1_senderPrivateKey_ = Wrappers.Option_None()
                    d_2_senderPublicKey_ = Wrappers.Option_None()
                    d_3_compressedSenderPublicKey_ = Wrappers.Option_None()
            pass
        d_15_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out4_: Wrappers.Result
        out4_ = RawECDHKeyring.default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_0_recipientPublicKey_), (input).curveSpec, (config).crypto)
        d_15_valueOrError4_ = out4_
        if (d_15_valueOrError4_).IsFailure():
            output = (d_15_valueOrError4_).PropagateFailure()
            return output
        d_16_compressedRecipientPublicKey_: _dafny.Seq
        d_16_compressedRecipientPublicKey_ = (d_15_valueOrError4_).Extract()
        d_17_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out5_: Wrappers.Result
        out5_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, d_0_recipientPublicKey_)
        d_17_valueOrError5_ = out5_
        if (d_17_valueOrError5_).IsFailure():
            output = (d_17_valueOrError5_).PropagateFailure()
            return output
        d_18___v11_: bool
        d_18___v11_ = (d_17_valueOrError5_).Extract()
        if (d_2_senderPublicKey_).is_Some:
            d_19_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
            out6_: Wrappers.Result
            out6_ = RawECDHKeyring.default__.ValidatePublicKey((config).crypto, (input).curveSpec, (d_2_senderPublicKey_).value)
            d_19_valueOrError6_ = out6_
            if (d_19_valueOrError6_).IsFailure():
                output = (d_19_valueOrError6_).PropagateFailure()
                return output
            d_20___v12_: bool
            d_20___v12_ = (d_19_valueOrError6_).Extract()
            d_21_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_21_valueOrError7_ = Wrappers.default__.Need(RawECDHKeyring.default__.ValidPublicKeyLength((d_2_senderPublicKey_).value), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid sender public key length")))
            if (d_21_valueOrError7_).IsFailure():
                output = (d_21_valueOrError7_).PropagateFailure()
                return output
        d_22_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_22_valueOrError8_ = Wrappers.default__.Need(RawECDHKeyring.default__.ValidPublicKeyLength(d_0_recipientPublicKey_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid recipient public key length")))
        if (d_22_valueOrError8_).IsFailure():
            output = (d_22_valueOrError8_).PropagateFailure()
            return output
        d_23_keyring_: RawECDHKeyring.RawEcdhKeyring
        nw0_ = RawECDHKeyring.RawEcdhKeyring()
        nw0_.ctor__((input).KeyAgreementScheme, (input).curveSpec, d_1_senderPrivateKey_, d_2_senderPublicKey_, d_0_recipientPublicKey_, d_3_compressedSenderPublicKey_, d_16_compressedRecipientPublicKey_, (config).crypto)
        d_23_keyring_ = nw0_
        output = Wrappers.Result_Success(d_23_keyring_)
        return output
        return output

    @staticmethod
    def CreateAwsKmsRsaKeyring(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need((((input).publicKey).is_Some) or (((input).kmsClient).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A publicKey or a kmsClient is required")))
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError1_ = Wrappers.default__.Need((((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__1) or (((input).encryptionAlgorithm).is_RSAES__OAEP__SHA__256), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unsupported EncryptionAlgorithmSpec")))
        if (d_1_valueOrError1_).IsFailure():
            output = (d_1_valueOrError1_).PropagateFailure()
            return output
        d_2_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError2_ = Wrappers.default__.Need((ComAmazonawsKmsTypes.default__.IsValid__KeyIdType((input).kmsKeyId)) and ((AwsArnParsing.default__.ParseAwsKmsArn((input).kmsKeyId)).is_Success), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Kms Key ID must be a KMS Key ARN")))
        if (d_2_valueOrError2_).IsFailure():
            output = (d_2_valueOrError2_).PropagateFailure()
            return output
        if ((input).publicKey).is_Some:
            d_3_lengthOutputRes_: Wrappers.Result
            d_3_lengthOutputRes_ = ((config).crypto).GetRSAKeyModulusLength(AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput(((input).publicKey).value))
            d_4_valueOrError3_: Wrappers.Result = None
            def lambda0_(d_5_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_5_e_)

            d_4_valueOrError3_ = (d_3_lengthOutputRes_).MapFailure(lambda0_)
            if (d_4_valueOrError3_).IsFailure():
                output = (d_4_valueOrError3_).PropagateFailure()
                return output
            d_6_lengthOutput_: AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput
            d_6_lengthOutput_ = (d_4_valueOrError3_).Extract()
            d_7_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_7_valueOrError4_ = Wrappers.default__.Need(((d_6_lengthOutput_).length) >= (AwsKmsRsaKeyring.default__.MIN__KMS__RSA__KEY__LEN), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid public key length")))
            if (d_7_valueOrError4_).IsFailure():
                output = (d_7_valueOrError4_).PropagateFailure()
                return output
        d_8_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_8_valueOrError5_ = AwsKmsUtils.default__.ValidateKmsKeyId((input).kmsKeyId)
        if (d_8_valueOrError5_).IsFailure():
            output = (d_8_valueOrError5_).PropagateFailure()
            return output
        d_9___v13_: tuple
        d_9___v13_ = (d_8_valueOrError5_).Extract()
        d_10_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_10_valueOrError6_ = AwsKmsUtils.default__.GetValidGrantTokens((input).grantTokens)
        if (d_10_valueOrError6_).IsFailure():
            output = (d_10_valueOrError6_).PropagateFailure()
            return output
        d_11_grantTokens_: _dafny.Seq
        d_11_grantTokens_ = (d_10_valueOrError6_).Extract()
        d_12_keyring_: AwsKmsRsaKeyring.AwsKmsRsaKeyring
        nw0_ = AwsKmsRsaKeyring.AwsKmsRsaKeyring()
        nw0_.ctor__((input).publicKey, (input).kmsKeyId, (input).encryptionAlgorithm, (input).kmsClient, (config).crypto, d_11_grantTokens_)
        d_12_keyring_ = nw0_
        output = Wrappers.Result_Success(d_12_keyring_)
        return output
        return output

    @staticmethod
    def CreateDefaultCryptographicMaterialsManager(config, input):
        output: Wrappers.Result = None
        d_0_cmm_: DefaultCMM.DefaultCMM
        nw0_ = DefaultCMM.DefaultCMM()
        nw0_.OfKeyring((input).keyring, (config).crypto)
        d_0_cmm_ = nw0_
        output = Wrappers.Result_Success(d_0_cmm_)
        return output
        return output

    @staticmethod
    def CmpError(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def CreateRequiredEncryptionContextCMM(config, input):
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need((((input).underlyingCMM).is_Some) and (((input).keyring).is_None), default__.CmpError(_dafny.Seq("CreateRequiredEncryptionContextCMM currently only supports cmm.")))
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_keySet_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Seq
            for compr_0_ in ((input).requiredEncryptionContextKeys).Elements:
                d_2_k_: _dafny.Seq = compr_0_
                if UTF8.ValidUTF8Bytes._Is(d_2_k_):
                    if (d_2_k_) in ((input).requiredEncryptionContextKeys):
                        coll0_ = coll0_.union(_dafny.Set([d_2_k_]))
            return _dafny.Set(coll0_)
        d_1_keySet_ = iife0_()
        
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need((0) < (len(d_1_keySet_)), default__.CmpError(_dafny.Seq("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_cmm_: RequiredEncryptionContextCMM.RequiredEncryptionContextCMM
        nw0_ = RequiredEncryptionContextCMM.RequiredEncryptionContextCMM()
        nw0_.ctor__(((input).underlyingCMM).value, d_1_keySet_)
        d_4_cmm_ = nw0_
        output = Wrappers.Result_Success(d_4_cmm_)
        return output
        return output

    @staticmethod
    def CreateCryptographicMaterialsCache(config, input):
        output: Wrappers.Result = None
        source0_ = (input).cache
        with _dafny.label("match0"):
            if True:
                if source0_.is_Default:
                    d_0_c_ = source0_.Default
                    d_1_cache_: AwsCryptographyMaterialProvidersTypes.StormTrackingCache
                    d_2_dt__update__tmp_h0_ = StormTracker.default__.DefaultStorm()
                    d_3_dt__update_hentryCapacity_h0_ = (d_0_c_).entryCapacity
                    d_1_cache_ = AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache(d_3_dt__update_hentryCapacity_h0_, (d_2_dt__update__tmp_h0_).entryPruningTailSize, (d_2_dt__update__tmp_h0_).gracePeriod, (d_2_dt__update__tmp_h0_).graceInterval, (d_2_dt__update__tmp_h0_).fanOut, (d_2_dt__update__tmp_h0_).inFlightTTL, (d_2_dt__update__tmp_h0_).sleepMilli, (d_2_dt__update__tmp_h0_).timeUnits)
                    d_4_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_4_valueOrError0_ = StormTracker.default__.CheckSettings(d_1_cache_)
                    if (d_4_valueOrError0_).IsFailure():
                        output = (d_4_valueOrError0_).PropagateFailure()
                        return output
                    d_5_cmc_: StormTracker.StormTracker
                    nw0_ = StormTracker.StormTracker()
                    nw0_.ctor__(d_1_cache_)
                    d_5_cmc_ = nw0_
                    d_6_synCmc_: StormTrackingCMC.StormTrackingCMC
                    nw1_ = StormTrackingCMC.StormTrackingCMC(d_5_cmc_)
                    d_6_synCmc_ = nw1_
                    output = Wrappers.Result_Success(d_6_synCmc_)
                    return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_No:
                    d_7_cmc_: LocalCMC.LocalCMC
                    nw2_ = LocalCMC.LocalCMC()
                    nw2_.ctor__(0, 1)
                    d_7_cmc_ = nw2_
                    output = Wrappers.Result_Success(d_7_cmc_)
                    return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_SingleThreaded:
                    d_8_c_ = source0_.SingleThreaded
                    d_9_cmc_: LocalCMC.LocalCMC
                    nw3_ = LocalCMC.LocalCMC()
                    nw3_.ctor__((d_8_c_).entryCapacity, (default__.OptionalCountingNumber((d_8_c_).entryPruningTailSize)).UnwrapOr(1))
                    d_9_cmc_ = nw3_
                    output = Wrappers.Result_Success(d_9_cmc_)
                    return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_MultiThreaded:
                    d_10_c_ = source0_.MultiThreaded
                    d_11_cmc_: LocalCMC.LocalCMC
                    nw4_ = LocalCMC.LocalCMC()
                    nw4_.ctor__((d_10_c_).entryCapacity, (default__.OptionalCountingNumber((d_10_c_).entryPruningTailSize)).UnwrapOr(1))
                    d_11_cmc_ = nw4_
                    d_12_synCmc_: SynchronizedLocalCMC.SynchronizedLocalCMC
                    nw5_ = SynchronizedLocalCMC.SynchronizedLocalCMC(d_11_cmc_)
                    d_12_synCmc_ = nw5_
                    output = Wrappers.Result_Success(d_12_synCmc_)
                    return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_StormTracking:
                    d_13_c_ = source0_.StormTracking
                    d_14_cache_: AwsCryptographyMaterialProvidersTypes.StormTrackingCache
                    d_15_dt__update__tmp_h1_ = d_13_c_
                    d_16_dt__update_hentryPruningTailSize_h0_ = default__.OptionalCountingNumber((d_13_c_).entryPruningTailSize)
                    d_14_cache_ = AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_15_dt__update__tmp_h1_).entryCapacity, d_16_dt__update_hentryPruningTailSize_h0_, (d_15_dt__update__tmp_h1_).gracePeriod, (d_15_dt__update__tmp_h1_).graceInterval, (d_15_dt__update__tmp_h1_).fanOut, (d_15_dt__update__tmp_h1_).inFlightTTL, (d_15_dt__update__tmp_h1_).sleepMilli, (d_15_dt__update__tmp_h1_).timeUnits)
                    d_17_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_17_valueOrError1_ = StormTracker.default__.CheckSettings(d_14_cache_)
                    if (d_17_valueOrError1_).IsFailure():
                        output = (d_17_valueOrError1_).PropagateFailure()
                        return output
                    d_18_cmc_: StormTracker.StormTracker
                    nw6_ = StormTracker.StormTracker()
                    nw6_.ctor__(d_14_cache_)
                    d_18_cmc_ = nw6_
                    d_19_synCmc_: StormTrackingCMC.StormTrackingCMC
                    nw7_ = StormTrackingCMC.StormTrackingCMC(d_18_cmc_)
                    d_19_synCmc_ = nw7_
                    output = Wrappers.Result_Success(d_19_synCmc_)
                    return output
                    raise _dafny.Break("match0")
            if True:
                d_20_c_ = source0_.Shared
                d_21_exception_: AwsCryptographyMaterialProvidersTypes.Error
                d_21_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("CreateCryptographicMaterialsCache should never be called with Shared CacheType."))
                output = Wrappers.Result_Failure(d_21_exception_)
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
        d_0_clientSupplier_: DefaultClientSupplier.DefaultClientSupplier
        nw0_ = DefaultClientSupplier.DefaultClientSupplier()
        nw0_.ctor__()
        d_0_clientSupplier_ = nw0_
        output = Wrappers.Result_Success(d_0_clientSupplier_)
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
        d_0_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).start, (input).stop), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Invalid Encryption Materials Transition")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidDecryptionMaterialsTransition(config, input):
        d_0_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).start, (input).stop), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Invalid Decryption Materials Transition")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(config, input):
        d_0_valueOrError0_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Encryption Materials")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(config, input):
        d_0_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterials(_dafny.Seq("Invalid Decryption Materials")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def GetAlgorithmSuiteInfo(config, input):
        return AlgorithmSuites.default__.GetAlgorithmSuiteInfo(input)

    @staticmethod
    def ValidAlgorithmSuiteInfo(config, input):
        d_0_valueOrError0_ = Wrappers.default__.Need(AlgorithmSuites.default__.AlgorithmSuite_q(input), AwsCryptographyMaterialProvidersTypes.Error_InvalidAlgorithmSuiteInfo(_dafny.Seq("Invalid AlgorithmSuiteInfo")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(config, input):
        d_0_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt((input).algorithm, (input).commitmentPolicy)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(())

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(config, input):
        d_0_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithm, (input).commitmentPolicy)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
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

