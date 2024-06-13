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

# Module: TestAwsKmsEncryptedDataKeyFilter

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFailsNonKeyResource():
        d_926_discoveryFilter_: AwsCryptographyMaterialProvidersTypes.DiscoveryFilter
        out347_: AwsCryptographyMaterialProvidersTypes.DiscoveryFilter
        out347_ = default__.GetDiscoveryFilter()
        d_926_discoveryFilter_ = out347_
        d_927_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw8_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw8_.ctor__(Wrappers.Option_Some(d_926_discoveryFilter_))
        d_927_edkFilter_ = nw8_
        d_928_badEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out348_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out348_ = default__.GetNonKeyEncryptedDataKey()
        d_928_badEdk_ = out348_
        d_929_filterResult_: Wrappers.Result
        out349_: Wrappers.Result
        out349_ = Actions.default__.FilterWithResult(d_927_edkFilter_, _dafny.Seq([d_928_badEdk_]))
        d_929_filterResult_ = out349_
        if not((d_929_filterResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(32,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_930_test_: AwsCryptographyMaterialProvidersTypes.Error
        d_930_test_ = (d_929_filterResult_).error
        if not((d_930_test_).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_930_test_).message) == (_dafny.Seq("Only AWS KMS Keys supported"))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestMatchesKeyringsConfiguration():
        d_931_matchingEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out350_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out350_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), TestUtils.default__.SHARED__TEST__KEY__ARN)
        d_931_matchingEdk_ = out350_
        d_932_mismatchEdkPartition_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out351_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out351_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws-cn:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        d_932_mismatchEdkPartition_ = out351_
        d_933_mismatchEdkAccount_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out352_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out352_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws:kms:us-west-2:827585335069:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        d_933_mismatchEdkAccount_ = out352_
        d_934_mismatchEdkProviderId_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out353_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out353_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws"), TestUtils.default__.SHARED__TEST__KEY__ARN)
        d_934_mismatchEdkProviderId_ = out353_
        d_935_discoveryFilter_: AwsCryptographyMaterialProvidersTypes.DiscoveryFilter
        out354_: AwsCryptographyMaterialProvidersTypes.DiscoveryFilter
        out354_ = default__.GetDiscoveryFilter()
        d_935_discoveryFilter_ = out354_
        d_936_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__(Wrappers.Option_Some(d_935_discoveryFilter_))
        d_936_edkFilter_ = nw9_
        d_937_filterResult_: Wrappers.Result
        out355_: Wrappers.Result
        out355_ = Actions.default__.FilterWithResult(d_936_edkFilter_, _dafny.Seq([d_931_matchingEdk_, d_932_mismatchEdkPartition_, d_933_mismatchEdkAccount_, d_934_mismatchEdkProviderId_]))
        d_937_filterResult_ = out355_
        if not((d_937_filterResult_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_937_filterResult_).value)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_937_filterResult_).value)[0]) == (d_931_matchingEdk_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(67,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GetDiscoveryFilter():
        discoveryFilter: AwsCryptographyMaterialProvidersTypes.DiscoveryFilter = AwsCryptographyMaterialProvidersTypes.DiscoveryFilter.default()()
        discoveryFilter = AwsCryptographyMaterialProvidersTypes.DiscoveryFilter_DiscoveryFilter(TestUtils.default__.ACCOUNT__IDS, TestUtils.default__.PARTITION)
        return discoveryFilter
        return discoveryFilter

    @staticmethod
    def GetNonKeyEncryptedDataKey():
        edk: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey.default()()
        out356_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        out356_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws:kms:us-west-2:658956600833:alias/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        edk = out356_
        return edk

