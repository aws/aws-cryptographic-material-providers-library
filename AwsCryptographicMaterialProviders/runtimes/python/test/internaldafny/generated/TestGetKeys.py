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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
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
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
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
import TestConfig as TestConfig

# Module: TestGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKey():
        d_37_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_38_valueOrError0_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_38_valueOrError0_ = out16_
        if not(not((d_38_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(21,21): " + _dafny.string_of(d_38_valueOrError0_))
        d_37_kmsClient_ = (d_38_valueOrError0_).Extract()
        d_39_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_40_valueOrError1_: Wrappers.Result = None
        out17_: Wrappers.Result
        out17_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_40_valueOrError1_ = out17_
        if not(not((d_40_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(22,21): " + _dafny.string_of(d_40_valueOrError1_))
        d_39_ddbClient_ = (d_40_valueOrError1_).Extract()
        d_41_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_41_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_42_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_42_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_41_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_39_ddbClient_), Wrappers.Option_Some(d_37_kmsClient_))
        d_43_keyStore_: KeyStore.KeyStoreClient
        d_44_valueOrError2_: Wrappers.Result = None
        out18_: Wrappers.Result
        out18_ = KeyStore.default__.KeyStore(d_42_keyStoreConfig_)
        d_44_valueOrError2_ = out18_
        if not(not((d_44_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(35,20): " + _dafny.string_of(d_44_valueOrError2_))
        d_43_keyStore_ = (d_44_valueOrError2_).Extract()
        d_45_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_46_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out19_: Wrappers.Result
        out19_ = (d_43_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_46_valueOrError3_ = out19_
        if not(not((d_46_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(37,27): " + _dafny.string_of(d_46_valueOrError3_))
        d_45_beaconKeyResult_ = (d_46_valueOrError3_).Extract()
        if not((((d_45_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(41,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_45_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(42,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_45_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKey():
        d_47_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_48_valueOrError0_: Wrappers.Result = None
        out20_: Wrappers.Result
        out20_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_48_valueOrError0_ = out20_
        if not(not((d_48_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(48,21): " + _dafny.string_of(d_48_valueOrError0_))
        d_47_kmsClient_ = (d_48_valueOrError0_).Extract()
        d_49_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_50_valueOrError1_: Wrappers.Result = None
        out21_: Wrappers.Result
        out21_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_50_valueOrError1_ = out21_
        if not(not((d_50_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(49,21): " + _dafny.string_of(d_50_valueOrError1_))
        d_49_ddbClient_ = (d_50_valueOrError1_).Extract()
        d_51_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_51_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_52_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_52_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_51_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_49_ddbClient_), Wrappers.Option_Some(d_47_kmsClient_))
        d_53_keyStore_: KeyStore.KeyStoreClient
        d_54_valueOrError2_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = KeyStore.default__.KeyStore(d_52_keyStoreConfig_)
        d_54_valueOrError2_ = out22_
        if not(not((d_54_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(62,20): " + _dafny.string_of(d_54_valueOrError2_))
        d_53_keyStore_ = (d_54_valueOrError2_).Extract()
        d_55_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_56_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out23_: Wrappers.Result
        out23_ = (d_53_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_56_valueOrError3_ = out23_
        if not(not((d_56_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(64,24): " + _dafny.string_of(d_56_valueOrError3_))
        d_55_activeResult_ = (d_56_valueOrError3_).Extract()
        if not((((d_55_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_55_activeResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_55_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersion():
        d_57_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_58_valueOrError0_: Wrappers.Result = None
        out24_: Wrappers.Result
        out24_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_58_valueOrError0_ = out24_
        if not(not((d_58_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(76,21): " + _dafny.string_of(d_58_valueOrError0_))
        d_57_kmsClient_ = (d_58_valueOrError0_).Extract()
        d_59_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_60_valueOrError1_: Wrappers.Result = None
        out25_: Wrappers.Result
        out25_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_60_valueOrError1_ = out25_
        if not(not((d_60_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(77,21): " + _dafny.string_of(d_60_valueOrError1_))
        d_59_ddbClient_ = (d_60_valueOrError1_).Extract()
        d_61_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_61_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_62_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_62_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_61_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_59_ddbClient_), Wrappers.Option_Some(d_57_kmsClient_))
        d_63_keyStore_: KeyStore.KeyStoreClient
        d_64_valueOrError2_: Wrappers.Result = None
        out26_: Wrappers.Result
        out26_ = KeyStore.default__.KeyStore(d_62_keyStoreConfig_)
        d_64_valueOrError2_ = out26_
        if not(not((d_64_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(90,20): " + _dafny.string_of(d_64_valueOrError2_))
        d_63_keyStore_ = (d_64_valueOrError2_).Extract()
        d_65_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_66_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out27_: Wrappers.Result
        out27_ = (d_63_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_66_valueOrError3_ = out27_
        if not(not((d_66_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(92,25): " + _dafny.string_of(d_66_valueOrError3_))
        d_65_versionResult_ = (d_66_valueOrError3_).Extract()
        d_67_testBytes_: _dafny.Seq
        d_68_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_68_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_68_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(98,21): " + _dafny.string_of(d_68_valueOrError4_))
        d_67_testBytes_ = (d_68_valueOrError4_).Extract()
        if not((((d_65_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(100,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_65_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_67_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_65_versionResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithIncorrectKmsKeyArn():
        d_69_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_70_valueOrError0_: Wrappers.Result = None
        out28_: Wrappers.Result
        out28_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_70_valueOrError0_ = out28_
        if not(not((d_70_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(107,21): " + _dafny.string_of(d_70_valueOrError0_))
        d_69_kmsClient_ = (d_70_valueOrError0_).Extract()
        d_71_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_72_valueOrError1_: Wrappers.Result = None
        out29_: Wrappers.Result
        out29_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_72_valueOrError1_ = out29_
        if not(not((d_72_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(108,21): " + _dafny.string_of(d_72_valueOrError1_))
        d_71_ddbClient_ = (d_72_valueOrError1_).Extract()
        d_73_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_73_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.mkrKeyArn)
        d_74_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_74_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_73_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_71_ddbClient_), Wrappers.Option_Some(d_69_kmsClient_))
        d_75_keyStore_: KeyStore.KeyStoreClient
        d_76_valueOrError2_: Wrappers.Result = None
        out30_: Wrappers.Result
        out30_ = KeyStore.default__.KeyStore(d_74_keyStoreConfig_)
        d_76_valueOrError2_ = out30_
        if not(not((d_76_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(121,20): " + _dafny.string_of(d_76_valueOrError2_))
        d_75_keyStore_ = (d_76_valueOrError2_).Extract()
        d_77_activeResult_: Wrappers.Result
        out31_: Wrappers.Result
        out31_ = (d_75_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_77_activeResult_ = out31_
        if not((d_77_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWrongLogicalKeyStoreName():
        d_78_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_79_valueOrError0_: Wrappers.Result = None
        out32_: Wrappers.Result
        out32_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_79_valueOrError0_ = out32_
        if not(not((d_79_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(132,21): " + _dafny.string_of(d_79_valueOrError0_))
        d_78_kmsClient_ = (d_79_valueOrError0_).Extract()
        d_80_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_81_valueOrError1_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_81_valueOrError1_ = out33_
        if not(not((d_81_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(133,21): " + _dafny.string_of(d_81_valueOrError1_))
        d_80_ddbClient_ = (d_81_valueOrError1_).Extract()
        d_82_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_82_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_83_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_83_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_82_kmsConfig_, default__.incorrectLogicalName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_80_ddbClient_), Wrappers.Option_Some(d_78_kmsClient_))
        d_84_keyStore_: KeyStore.KeyStoreClient
        d_85_valueOrError2_: Wrappers.Result = None
        out34_: Wrappers.Result
        out34_ = KeyStore.default__.KeyStore(d_83_keyStoreConfig_)
        d_85_valueOrError2_ = out34_
        if not(not((d_85_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(146,20): " + _dafny.string_of(d_85_valueOrError2_))
        d_84_keyStore_ = (d_85_valueOrError2_).Extract()
        d_86_activeResult_: Wrappers.Result
        out35_: Wrappers.Result
        out35_ = (d_84_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_86_activeResult_ = out35_
        if not((d_86_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithNoClients():
        d_87_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_87_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_88_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_88_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_87_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_89_keyStore_: KeyStore.KeyStoreClient
        d_90_valueOrError0_: Wrappers.Result = None
        out36_: Wrappers.Result
        out36_ = KeyStore.default__.KeyStore(d_88_keyStoreConfig_)
        d_90_valueOrError0_ = out36_
        if not(not((d_90_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(169,20): " + _dafny.string_of(d_90_valueOrError0_))
        d_89_keyStore_ = (d_90_valueOrError0_).Extract()
        d_91_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_92_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out37_: Wrappers.Result
        out37_ = (d_89_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_92_valueOrError1_ = out37_
        if not(not((d_92_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(171,24): " + _dafny.string_of(d_92_valueOrError1_))
        d_91_activeResult_ = (d_92_valueOrError1_).Extract()
        if not((len(((d_91_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(176,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def incorrectLogicalName(instance):
        return _dafny.Seq("MySuperAwesomeTableName")
