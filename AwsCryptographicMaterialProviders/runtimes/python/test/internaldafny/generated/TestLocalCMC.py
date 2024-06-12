import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
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
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
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
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
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
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring
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
        d_938_st_: LocalCMC.LocalCMC
        nw10_ = LocalCMC.LocalCMC()
        nw10_.ctor__(100, 1)
        d_938_st_ = nw10_
        d_939_abc_: _dafny.Seq
        d_939_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_940_cde_: _dafny.Seq
        d_940_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_941_res_: Wrappers.Result
        out357_: Wrappers.Result
        out357_ = (d_938_st_).GetCacheEntryWithTime(default__.MakeGet(d_939_abc_), 10000)
        d_941_res_ = out357_
        if not((d_941_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_941_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(57,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_942_res2_: tuple
        d_943_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out358_: Wrappers.Result
        out358_ = (d_938_st_).PutCacheEntry_k(default__.MakePut(d_939_abc_, 10000))
        d_943_valueOrError0_ = out358_
        if not(not((d_943_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(59,16): " + _dafny.string_of(d_943_valueOrError0_))
        d_942_res2_ = (d_943_valueOrError0_).Extract()
        d_944_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out359_: Wrappers.Result
        out359_ = (d_938_st_).PutCacheEntry_k(default__.MakePut(d_940_cde_, 10000))
        d_944_valueOrError1_ = out359_
        if not(not((d_944_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(60,12): " + _dafny.string_of(d_944_valueOrError1_))
        d_942_res2_ = (d_944_valueOrError1_).Extract()
        d_945_res3_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput
        d_946_valueOrError2_: Wrappers.Result = None
        out360_: Wrappers.Result
        out360_ = (d_938_st_).GetCacheEntryWithTime(default__.MakeGet(d_939_abc_), 9999)
        d_946_valueOrError2_ = out360_
        if not(not((d_946_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(62,16): " + _dafny.string_of(d_946_valueOrError2_))
        d_945_res3_ = (d_946_valueOrError2_).Extract()
        d_947_valueOrError3_: Wrappers.Result = None
        out361_: Wrappers.Result
        out361_ = (d_938_st_).GetCacheEntryWithTime(default__.MakeGet(d_939_abc_), 10000)
        d_947_valueOrError3_ = out361_
        if not(not((d_947_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(63,12): " + _dafny.string_of(d_947_valueOrError3_))
        d_945_res3_ = (d_947_valueOrError3_).Extract()
        out362_: Wrappers.Result
        out362_ = (d_938_st_).GetCacheEntryWithTime(default__.MakeGet(d_939_abc_), 10001)
        d_941_res_ = out362_
        if not((d_941_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_941_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_948_valueOrError4_: Wrappers.Result = None
        out363_: Wrappers.Result
        out363_ = (d_938_st_).GetCacheEntryWithTime(default__.MakeGet(d_940_cde_), 9999)
        d_948_valueOrError4_ = out363_
        if not(not((d_948_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(68,12): " + _dafny.string_of(d_948_valueOrError4_))
        d_945_res3_ = (d_948_valueOrError4_).Extract()
        d_949_res5_: tuple
        d_950_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out364_: Wrappers.Result
        out364_ = (d_938_st_).DeleteCacheEntry_k(default__.MakeDel(d_940_cde_))
        d_950_valueOrError5_ = out364_
        if not(not((d_950_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(69,16): " + _dafny.string_of(d_950_valueOrError5_))
        d_949_res5_ = (d_950_valueOrError5_).Extract()
        out365_: Wrappers.Result
        out365_ = (d_938_st_).GetCacheEntryWithTime(default__.MakeGet(d_939_abc_), 9999)
        d_941_res_ = out365_
        if not((d_941_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_941_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_951_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out366_: Wrappers.Result
        out366_ = (d_938_st_).DeleteCacheEntry_k(default__.MakeDel(d_940_cde_))
        d_951_valueOrError6_ = out366_
        if not(not((d_951_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(73,12): " + _dafny.string_of(d_951_valueOrError6_))
        d_949_res5_ = (d_951_valueOrError6_).Extract()

