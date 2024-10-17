import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
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
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
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
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
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
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
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
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
import TestLyingBranchKey as TestLyingBranchKey
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestErrorMessages as TestErrorMessages
import TestDefaultClientProvider as TestDefaultClientProvider
import TestRawECDHKeyring as TestRawECDHKeyring
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring
import TestAwsKmsEcdhKeyring as TestAwsKmsEcdhKeyring
import TestAwsKmsEncryptedDataKeyFilter as TestAwsKmsEncryptedDataKeyFilter

# Module: TestLocalCMC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MakeMat(data):
        return AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(AwsCryptographyKeyStoreTypes.BranchKeyMaterials_BranchKeyMaterials(_dafny.Seq("spoo"), data, _dafny.Map({}), data))

    @staticmethod
    def MakeGet(data):
        return AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(data, Wrappers.Option_None())

    @staticmethod
    def MakeDel(data):
        return AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput_DeleteCacheEntryInput(data)

    @staticmethod
    def MakePut(data, expiryTime):
        return AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(data, default__.MakeMat(data), 123456789, expiryTime, Wrappers.Option_None(), Wrappers.Option_None())

    @staticmethod
    def LocalCMCBasics():
        d_0_st_: LocalCMC.LocalCMC
        nw0_ = LocalCMC.LocalCMC()
        nw0_.ctor__(100, 1)
        d_0_st_ = nw0_
        d_1_abc_: _dafny.Seq
        d_1_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_2_cde_: _dafny.Seq
        d_2_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_3_res_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (d_0_st_).GetCacheEntryWithTime(default__.MakeGet(d_1_abc_), 10000)
        d_3_res_ = out0_
        if not((d_3_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_3_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(57,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_4_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out1_: Wrappers.Result
        out1_ = (d_0_st_).PutCacheEntry_k(default__.MakePut(d_1_abc_, 10000))
        d_4_valueOrError0_ = out1_
        if not(not((d_4_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(59,16): " + _dafny.string_of(d_4_valueOrError0_))
        d_5_res2_: tuple
        d_5_res2_ = (d_4_valueOrError0_).Extract()
        d_6_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out2_: Wrappers.Result
        out2_ = (d_0_st_).PutCacheEntry_k(default__.MakePut(d_2_cde_, 10000))
        d_6_valueOrError1_ = out2_
        if not(not((d_6_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(60,12): " + _dafny.string_of(d_6_valueOrError1_))
        d_5_res2_ = (d_6_valueOrError1_).Extract()
        d_7_valueOrError2_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_0_st_).GetCacheEntryWithTime(default__.MakeGet(d_1_abc_), 9999)
        d_7_valueOrError2_ = out3_
        if not(not((d_7_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(62,16): " + _dafny.string_of(d_7_valueOrError2_))
        d_8_res3_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput
        d_8_res3_ = (d_7_valueOrError2_).Extract()
        d_9_valueOrError3_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_0_st_).GetCacheEntryWithTime(default__.MakeGet(d_1_abc_), 10000)
        d_9_valueOrError3_ = out4_
        if not(not((d_9_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(63,12): " + _dafny.string_of(d_9_valueOrError3_))
        d_8_res3_ = (d_9_valueOrError3_).Extract()
        out5_: Wrappers.Result
        out5_ = (d_0_st_).GetCacheEntryWithTime(default__.MakeGet(d_1_abc_), 10001)
        d_3_res_ = out5_
        if not((d_3_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_3_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_10_valueOrError4_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_0_st_).GetCacheEntryWithTime(default__.MakeGet(d_2_cde_), 9999)
        d_10_valueOrError4_ = out6_
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(68,12): " + _dafny.string_of(d_10_valueOrError4_))
        d_8_res3_ = (d_10_valueOrError4_).Extract()
        d_11_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out7_: Wrappers.Result
        out7_ = (d_0_st_).DeleteCacheEntry_k(default__.MakeDel(d_2_cde_))
        d_11_valueOrError5_ = out7_
        if not(not((d_11_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(69,16): " + _dafny.string_of(d_11_valueOrError5_))
        d_12_res5_: tuple
        d_12_res5_ = (d_11_valueOrError5_).Extract()
        out8_: Wrappers.Result
        out8_ = (d_0_st_).GetCacheEntryWithTime(default__.MakeGet(d_1_abc_), 9999)
        d_3_res_ = out8_
        if not((d_3_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_3_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_13_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out9_: Wrappers.Result
        out9_ = (d_0_st_).DeleteCacheEntry_k(default__.MakeDel(d_2_cde_))
        d_13_valueOrError6_ = out9_
        if not(not((d_13_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(73,12): " + _dafny.string_of(d_13_valueOrError6_))
        d_12_res5_ = (d_13_valueOrError6_).Extract()

