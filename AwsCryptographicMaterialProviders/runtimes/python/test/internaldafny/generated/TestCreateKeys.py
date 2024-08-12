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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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
import TestLyingBranchKey as TestLyingBranchKey
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems

# Module: TestCreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCreateBranchAndBeaconKeys():
        d_252_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_253_valueOrError0_: Wrappers.Result = None
        out102_: Wrappers.Result
        out102_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_253_valueOrError0_ = out102_
        if not(not((d_253_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(68,21): " + _dafny.string_of(d_253_valueOrError0_))
        d_252_kmsClient_ = (d_253_valueOrError0_).Extract()
        d_254_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_255_valueOrError1_: Wrappers.Result = None
        out103_: Wrappers.Result
        out103_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_255_valueOrError1_ = out103_
        if not(not((d_255_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(69,21): " + _dafny.string_of(d_255_valueOrError1_))
        d_254_ddbClient_ = (d_255_valueOrError1_).Extract()
        d_256_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_256_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_257_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_257_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_256_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_254_ddbClient_), Wrappers.Option_Some(d_252_kmsClient_))
        d_258_keyStore_: KeyStore.KeyStoreClient
        d_259_valueOrError2_: Wrappers.Result = None
        out104_: Wrappers.Result
        out104_ = KeyStore.default__.KeyStore(d_257_keyStoreConfig_)
        d_259_valueOrError2_ = out104_
        if not(not((d_259_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(82,20): " + _dafny.string_of(d_259_valueOrError2_))
        d_258_keyStore_ = (d_259_valueOrError2_).Extract()
        d_260_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_261_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out105_: Wrappers.Result
        out105_ = (d_258_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_261_valueOrError3_ = out105_
        if not(not((d_261_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(84,23): " + _dafny.string_of(d_261_valueOrError3_))
        d_260_branchKeyId_ = (d_261_valueOrError3_).Extract()
        d_262_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_263_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out106_: Wrappers.Result
        out106_ = (d_258_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput((d_260_branchKeyId_).branchKeyIdentifier))
        d_263_valueOrError4_ = out106_
        if not(not((d_263_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(88,27): " + _dafny.string_of(d_263_valueOrError4_))
        d_262_beaconKeyResult_ = (d_263_valueOrError4_).Extract()
        d_264_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_265_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out107_: Wrappers.Result
        out107_ = (d_258_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_260_branchKeyId_).branchKeyIdentifier))
        d_265_valueOrError5_ = out107_
        if not(not((d_265_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(93,24): " + _dafny.string_of(d_265_valueOrError5_))
        d_264_activeResult_ = (d_265_valueOrError5_).Extract()
        d_266_branchKeyVersion_: _dafny.Seq
        d_267_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_267_valueOrError6_ = UTF8.default__.Decode(((d_264_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_267_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(98,28): " + _dafny.string_of(d_267_valueOrError6_))
        d_266_branchKeyVersion_ = (d_267_valueOrError6_).Extract()
        d_268_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_269_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out108_: Wrappers.Result
        out108_ = (d_258_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_260_branchKeyId_).branchKeyIdentifier, d_266_branchKeyVersion_))
        d_269_valueOrError7_ = out108_
        if not(not((d_269_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(99,25): " + _dafny.string_of(d_269_valueOrError7_))
        d_268_versionResult_ = (d_269_valueOrError7_).Extract()
        CleanupItems.default__.DeleteVersion((d_260_branchKeyId_).branchKeyIdentifier, d_266_branchKeyVersion_, d_254_ddbClient_)
        CleanupItems.default__.DeleteActive((d_260_branchKeyId_).branchKeyIdentifier, d_254_ddbClient_)
        if not((((d_262_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_262_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_264_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_268_versionResult_).branchKeyMaterials).branchKey) == (((d_264_activeResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_268_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_264_activeResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_264_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_262_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(115,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_268_versionResult_).branchKeyMaterials).branchKeyVersion) == (((d_264_activeResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_270_idByteUUID_: _dafny.Seq
        d_271_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_271_valueOrError8_ = UUID.default__.ToByteArray(((d_264_activeResult_).branchKeyMaterials).branchKeyIdentifier)
        if not(not((d_271_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(125,22): " + _dafny.string_of(d_271_valueOrError8_))
        d_270_idByteUUID_ = (d_271_valueOrError8_).Extract()
        d_272_idRoundTrip_: _dafny.Seq
        d_273_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_273_valueOrError9_ = UUID.default__.FromByteArray(d_270_idByteUUID_)
        if not(not((d_273_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(126,23): " + _dafny.string_of(d_273_valueOrError9_))
        d_272_idRoundTrip_ = (d_273_valueOrError9_).Extract()
        if not((d_272_idRoundTrip_) == (((d_264_activeResult_).branchKeyMaterials).branchKeyIdentifier)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(127,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_274_versionString_: _dafny.Seq
        d_275_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_275_valueOrError10_ = UTF8.default__.Decode(((d_264_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_275_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(133,25): " + _dafny.string_of(d_275_valueOrError10_))
        d_274_versionString_ = (d_275_valueOrError10_).Extract()
        d_276_versionByteUUID_: _dafny.Seq
        d_277_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_277_valueOrError11_ = UUID.default__.ToByteArray(d_274_versionString_)
        if not(not((d_277_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(134,27): " + _dafny.string_of(d_277_valueOrError11_))
        d_276_versionByteUUID_ = (d_277_valueOrError11_).Extract()
        d_278_versionRoundTrip_: _dafny.Seq
        d_279_valueOrError12_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_279_valueOrError12_ = UUID.default__.FromByteArray(d_276_versionByteUUID_)
        if not(not((d_279_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(135,28): " + _dafny.string_of(d_279_valueOrError12_))
        d_278_versionRoundTrip_ = (d_279_valueOrError12_).Extract()
        if not((d_278_versionRoundTrip_) == (d_274_versionString_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateOptions():
        d_280_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_281_valueOrError0_: Wrappers.Result = None
        out109_: Wrappers.Result
        out109_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_281_valueOrError0_ = out109_
        if not(not((d_281_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(142,21): " + _dafny.string_of(d_281_valueOrError0_))
        d_280_kmsClient_ = (d_281_valueOrError0_).Extract()
        d_282_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_283_valueOrError1_: Wrappers.Result = None
        out110_: Wrappers.Result
        out110_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_283_valueOrError1_ = out110_
        if not(not((d_283_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(143,21): " + _dafny.string_of(d_283_valueOrError1_))
        d_282_ddbClient_ = (d_283_valueOrError1_).Extract()
        d_284_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_284_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_285_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_285_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_284_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_282_ddbClient_), Wrappers.Option_Some(d_280_kmsClient_))
        d_286_keyStore_: KeyStore.KeyStoreClient
        d_287_valueOrError2_: Wrappers.Result = None
        out111_: Wrappers.Result
        out111_ = KeyStore.default__.KeyStore(d_285_keyStoreConfig_)
        d_287_valueOrError2_ = out111_
        if not(not((d_287_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(156,20): " + _dafny.string_of(d_287_valueOrError2_))
        d_286_keyStore_ = (d_287_valueOrError2_).Extract()
        d_288_id_: _dafny.Seq
        d_289_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out112_: Wrappers.Result
        out112_ = UUID.default__.GenerateUUID()
        d_289_valueOrError3_ = out112_
        if not(not((d_289_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(159,14): " + _dafny.string_of(d_289_valueOrError3_))
        d_288_id_ = (d_289_valueOrError3_).Extract()
        d_290_encryptionContext_: _dafny.Map
        d_291_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out113_: Wrappers.Result
        out113_ = Fixtures.default__.EncodeEncryptionContext(_dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")}))
        d_291_valueOrError4_ = out113_
        if not(not((d_291_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(161,29): " + _dafny.string_of(d_291_valueOrError4_))
        d_290_encryptionContext_ = (d_291_valueOrError4_).Extract()
        d_292_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_293_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out114_: Wrappers.Result
        out114_ = (d_286_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_288_id_), Wrappers.Option_Some(d_290_encryptionContext_)))
        d_293_valueOrError5_ = out114_
        if not(not((d_293_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(166,23): " + _dafny.string_of(d_293_valueOrError5_))
        d_292_branchKeyId_ = (d_293_valueOrError5_).Extract()
        d_294_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_295_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out115_: Wrappers.Result
        out115_ = (d_286_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput((d_292_branchKeyId_).branchKeyIdentifier))
        d_295_valueOrError6_ = out115_
        if not(not((d_295_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(171,27): " + _dafny.string_of(d_295_valueOrError6_))
        d_294_beaconKeyResult_ = (d_295_valueOrError6_).Extract()
        d_296_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_297_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out116_: Wrappers.Result
        out116_ = (d_286_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_292_branchKeyId_).branchKeyIdentifier))
        d_297_valueOrError7_ = out116_
        if not(not((d_297_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(176,24): " + _dafny.string_of(d_297_valueOrError7_))
        d_296_activeResult_ = (d_297_valueOrError7_).Extract()
        d_298_branchKeyVersion_: _dafny.Seq
        d_299_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_299_valueOrError8_ = UTF8.default__.Decode(((d_296_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_299_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(181,28): " + _dafny.string_of(d_299_valueOrError8_))
        d_298_branchKeyVersion_ = (d_299_valueOrError8_).Extract()
        d_300_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_301_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out117_: Wrappers.Result
        out117_ = (d_286_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_292_branchKeyId_).branchKeyIdentifier, d_298_branchKeyVersion_))
        d_301_valueOrError9_ = out117_
        if not(not((d_301_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(182,25): " + _dafny.string_of(d_301_valueOrError9_))
        d_300_versionResult_ = (d_301_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_292_branchKeyId_).branchKeyIdentifier, d_298_branchKeyVersion_, d_282_ddbClient_)
        CleanupItems.default__.DeleteActive((d_292_branchKeyId_).branchKeyIdentifier, d_282_ddbClient_)
        if not((((d_288_id_) == (((d_300_versionResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_300_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_296_activeResult_).branchKeyMaterials).branchKeyIdentifier))) and ((((d_296_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_294_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(195,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_290_encryptionContext_) == (((d_300_versionResult_).branchKeyMaterials).encryptionContext)) and ((((d_300_versionResult_).branchKeyMaterials).encryptionContext) == (((d_296_activeResult_).branchKeyMaterials).encryptionContext))) and ((((d_296_activeResult_).branchKeyMaterials).encryptionContext) == (((d_294_beaconKeyResult_).beaconKeyMaterials).encryptionContext))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(200,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateDuplicate():
        d_302_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_303_valueOrError0_: Wrappers.Result = None
        out118_: Wrappers.Result
        out118_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_303_valueOrError0_ = out118_
        if not(not((d_303_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(209,21): " + _dafny.string_of(d_303_valueOrError0_))
        d_302_kmsClient_ = (d_303_valueOrError0_).Extract()
        d_304_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_305_valueOrError1_: Wrappers.Result = None
        out119_: Wrappers.Result
        out119_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_305_valueOrError1_ = out119_
        if not(not((d_305_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(210,21): " + _dafny.string_of(d_305_valueOrError1_))
        d_304_ddbClient_ = (d_305_valueOrError1_).Extract()
        d_306_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_306_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_307_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_307_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_306_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_304_ddbClient_), Wrappers.Option_Some(d_302_kmsClient_))
        d_308_keyStore_: KeyStore.KeyStoreClient
        d_309_valueOrError2_: Wrappers.Result = None
        out120_: Wrappers.Result
        out120_ = KeyStore.default__.KeyStore(d_307_keyStoreConfig_)
        d_309_valueOrError2_ = out120_
        if not(not((d_309_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(223,20): " + _dafny.string_of(d_309_valueOrError2_))
        d_308_keyStore_ = (d_309_valueOrError2_).Extract()
        d_310_attempt_: Wrappers.Result
        out121_: Wrappers.Result
        out121_ = (d_308_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(Fixtures.default__.branchKeyId), Wrappers.Option_None()))
        d_310_attempt_ = out121_
        if not((d_310_attempt_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(230,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillFail():
        d_311_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_312_valueOrError0_: Wrappers.Result = None
        out122_: Wrappers.Result
        out122_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_312_valueOrError0_ = out122_
        if not(not((d_312_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(236,21): " + _dafny.string_of(d_312_valueOrError0_))
        d_311_ddbClient_ = (d_312_valueOrError0_).Extract()
        d_313_encryptionContext_: _dafny.Map
        d_313_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_314_output_: Wrappers.Result
        out123_: Wrappers.Result
        out123_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_313_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_313_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_313_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_311_ddbClient_)
        d_314_output_ = out123_
        if not((d_314_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(255,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillWithADifferentVersionFail():
        d_315_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_316_valueOrError0_: Wrappers.Result = None
        out124_: Wrappers.Result
        out124_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_316_valueOrError0_ = out124_
        if not(not((d_316_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(261,21): " + _dafny.string_of(d_316_valueOrError0_))
        d_315_ddbClient_ = (d_316_valueOrError0_).Extract()
        d_317_encryptionContext_: _dafny.Map
        d_317_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, _dafny.Seq("!= branchKeyIdActiveVersion"), _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_318_output_: Wrappers.Result
        out125_: Wrappers.Result
        out125_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_317_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_317_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_317_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_315_ddbClient_)
        d_318_output_ = out125_
        if not((d_318_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(280,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

