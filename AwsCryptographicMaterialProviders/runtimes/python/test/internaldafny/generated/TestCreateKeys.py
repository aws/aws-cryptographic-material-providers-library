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

# Module: TestCreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCreateBranchAndBeaconKeys():
        d_217_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_218_valueOrError0_: Wrappers.Result = None
        out86_: Wrappers.Result
        out86_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_218_valueOrError0_ = out86_
        if not(not((d_218_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(68,21): " + _dafny.string_of(d_218_valueOrError0_))
        d_217_kmsClient_ = (d_218_valueOrError0_).Extract()
        d_219_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_220_valueOrError1_: Wrappers.Result = None
        out87_: Wrappers.Result
        out87_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_220_valueOrError1_ = out87_
        if not(not((d_220_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(69,21): " + _dafny.string_of(d_220_valueOrError1_))
        d_219_ddbClient_ = (d_220_valueOrError1_).Extract()
        d_221_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_221_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_222_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_222_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_221_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_219_ddbClient_), Wrappers.Option_Some(d_217_kmsClient_))
        d_223_keyStore_: KeyStore.KeyStoreClient
        d_224_valueOrError2_: Wrappers.Result = None
        out88_: Wrappers.Result
        out88_ = KeyStore.default__.KeyStore(d_222_keyStoreConfig_)
        d_224_valueOrError2_ = out88_
        if not(not((d_224_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(82,20): " + _dafny.string_of(d_224_valueOrError2_))
        d_223_keyStore_ = (d_224_valueOrError2_).Extract()
        d_225_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_226_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out89_: Wrappers.Result
        out89_ = (d_223_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_226_valueOrError3_ = out89_
        if not(not((d_226_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(84,23): " + _dafny.string_of(d_226_valueOrError3_))
        d_225_branchKeyId_ = (d_226_valueOrError3_).Extract()
        d_227_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_228_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out90_: Wrappers.Result
        out90_ = (d_223_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput((d_225_branchKeyId_).branchKeyIdentifier))
        d_228_valueOrError4_ = out90_
        if not(not((d_228_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(88,27): " + _dafny.string_of(d_228_valueOrError4_))
        d_227_beaconKeyResult_ = (d_228_valueOrError4_).Extract()
        d_229_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_230_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out91_: Wrappers.Result
        out91_ = (d_223_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_225_branchKeyId_).branchKeyIdentifier))
        d_230_valueOrError5_ = out91_
        if not(not((d_230_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(93,24): " + _dafny.string_of(d_230_valueOrError5_))
        d_229_activeResult_ = (d_230_valueOrError5_).Extract()
        d_231_branchKeyVersion_: _dafny.Seq
        d_232_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_232_valueOrError6_ = UTF8.default__.Decode(((d_229_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_232_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(98,28): " + _dafny.string_of(d_232_valueOrError6_))
        d_231_branchKeyVersion_ = (d_232_valueOrError6_).Extract()
        d_233_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_234_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out92_: Wrappers.Result
        out92_ = (d_223_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_225_branchKeyId_).branchKeyIdentifier, d_231_branchKeyVersion_))
        d_234_valueOrError7_ = out92_
        if not(not((d_234_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(99,25): " + _dafny.string_of(d_234_valueOrError7_))
        d_233_versionResult_ = (d_234_valueOrError7_).Extract()
        CleanupItems.default__.DeleteVersion((d_225_branchKeyId_).branchKeyIdentifier, d_231_branchKeyVersion_, d_219_ddbClient_)
        CleanupItems.default__.DeleteActive((d_225_branchKeyId_).branchKeyIdentifier, d_219_ddbClient_)
        if not((((d_227_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_227_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_229_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_233_versionResult_).branchKeyMaterials).branchKey) == (((d_229_activeResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_233_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_229_activeResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_229_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_227_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(115,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_233_versionResult_).branchKeyMaterials).branchKeyVersion) == (((d_229_activeResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_235_idByteUUID_: _dafny.Seq
        d_236_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_236_valueOrError8_ = UUID.default__.ToByteArray(((d_229_activeResult_).branchKeyMaterials).branchKeyIdentifier)
        if not(not((d_236_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(125,22): " + _dafny.string_of(d_236_valueOrError8_))
        d_235_idByteUUID_ = (d_236_valueOrError8_).Extract()
        d_237_idRoundTrip_: _dafny.Seq
        d_238_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_238_valueOrError9_ = UUID.default__.FromByteArray(d_235_idByteUUID_)
        if not(not((d_238_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(126,23): " + _dafny.string_of(d_238_valueOrError9_))
        d_237_idRoundTrip_ = (d_238_valueOrError9_).Extract()
        if not((d_237_idRoundTrip_) == (((d_229_activeResult_).branchKeyMaterials).branchKeyIdentifier)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(127,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_239_versionString_: _dafny.Seq
        d_240_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_240_valueOrError10_ = UTF8.default__.Decode(((d_229_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_240_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(133,25): " + _dafny.string_of(d_240_valueOrError10_))
        d_239_versionString_ = (d_240_valueOrError10_).Extract()
        d_241_versionByteUUID_: _dafny.Seq
        d_242_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_242_valueOrError11_ = UUID.default__.ToByteArray(d_239_versionString_)
        if not(not((d_242_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(134,27): " + _dafny.string_of(d_242_valueOrError11_))
        d_241_versionByteUUID_ = (d_242_valueOrError11_).Extract()
        d_243_versionRoundTrip_: _dafny.Seq
        d_244_valueOrError12_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_244_valueOrError12_ = UUID.default__.FromByteArray(d_241_versionByteUUID_)
        if not(not((d_244_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(135,28): " + _dafny.string_of(d_244_valueOrError12_))
        d_243_versionRoundTrip_ = (d_244_valueOrError12_).Extract()
        if not((d_243_versionRoundTrip_) == (d_239_versionString_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateOptions():
        d_245_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_246_valueOrError0_: Wrappers.Result = None
        out93_: Wrappers.Result
        out93_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_246_valueOrError0_ = out93_
        if not(not((d_246_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(142,21): " + _dafny.string_of(d_246_valueOrError0_))
        d_245_kmsClient_ = (d_246_valueOrError0_).Extract()
        d_247_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_248_valueOrError1_: Wrappers.Result = None
        out94_: Wrappers.Result
        out94_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_248_valueOrError1_ = out94_
        if not(not((d_248_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(143,21): " + _dafny.string_of(d_248_valueOrError1_))
        d_247_ddbClient_ = (d_248_valueOrError1_).Extract()
        d_249_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_249_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_250_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_250_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_249_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_247_ddbClient_), Wrappers.Option_Some(d_245_kmsClient_))
        d_251_keyStore_: KeyStore.KeyStoreClient
        d_252_valueOrError2_: Wrappers.Result = None
        out95_: Wrappers.Result
        out95_ = KeyStore.default__.KeyStore(d_250_keyStoreConfig_)
        d_252_valueOrError2_ = out95_
        if not(not((d_252_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(156,20): " + _dafny.string_of(d_252_valueOrError2_))
        d_251_keyStore_ = (d_252_valueOrError2_).Extract()
        d_253_id_: _dafny.Seq
        d_254_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out96_: Wrappers.Result
        out96_ = UUID.default__.GenerateUUID()
        d_254_valueOrError3_ = out96_
        if not(not((d_254_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(159,14): " + _dafny.string_of(d_254_valueOrError3_))
        d_253_id_ = (d_254_valueOrError3_).Extract()
        d_255_encryptionContext_: _dafny.Map
        d_256_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out97_: Wrappers.Result
        out97_ = Fixtures.default__.EncodeEncryptionContext(_dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")}))
        d_256_valueOrError4_ = out97_
        if not(not((d_256_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(161,29): " + _dafny.string_of(d_256_valueOrError4_))
        d_255_encryptionContext_ = (d_256_valueOrError4_).Extract()
        d_257_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_258_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out98_: Wrappers.Result
        out98_ = (d_251_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_253_id_), Wrappers.Option_Some(d_255_encryptionContext_)))
        d_258_valueOrError5_ = out98_
        if not(not((d_258_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(166,23): " + _dafny.string_of(d_258_valueOrError5_))
        d_257_branchKeyId_ = (d_258_valueOrError5_).Extract()
        d_259_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_260_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out99_: Wrappers.Result
        out99_ = (d_251_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput((d_257_branchKeyId_).branchKeyIdentifier))
        d_260_valueOrError6_ = out99_
        if not(not((d_260_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(171,27): " + _dafny.string_of(d_260_valueOrError6_))
        d_259_beaconKeyResult_ = (d_260_valueOrError6_).Extract()
        d_261_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_262_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out100_: Wrappers.Result
        out100_ = (d_251_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_257_branchKeyId_).branchKeyIdentifier))
        d_262_valueOrError7_ = out100_
        if not(not((d_262_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(176,24): " + _dafny.string_of(d_262_valueOrError7_))
        d_261_activeResult_ = (d_262_valueOrError7_).Extract()
        d_263_branchKeyVersion_: _dafny.Seq
        d_264_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_264_valueOrError8_ = UTF8.default__.Decode(((d_261_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_264_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(181,28): " + _dafny.string_of(d_264_valueOrError8_))
        d_263_branchKeyVersion_ = (d_264_valueOrError8_).Extract()
        d_265_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_266_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out101_: Wrappers.Result
        out101_ = (d_251_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_257_branchKeyId_).branchKeyIdentifier, d_263_branchKeyVersion_))
        d_266_valueOrError9_ = out101_
        if not(not((d_266_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(182,25): " + _dafny.string_of(d_266_valueOrError9_))
        d_265_versionResult_ = (d_266_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_257_branchKeyId_).branchKeyIdentifier, d_263_branchKeyVersion_, d_247_ddbClient_)
        CleanupItems.default__.DeleteActive((d_257_branchKeyId_).branchKeyIdentifier, d_247_ddbClient_)
        if not((((d_253_id_) == (((d_265_versionResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_265_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_261_activeResult_).branchKeyMaterials).branchKeyIdentifier))) and ((((d_261_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_259_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(195,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_255_encryptionContext_) == (((d_265_versionResult_).branchKeyMaterials).encryptionContext)) and ((((d_265_versionResult_).branchKeyMaterials).encryptionContext) == (((d_261_activeResult_).branchKeyMaterials).encryptionContext))) and ((((d_261_activeResult_).branchKeyMaterials).encryptionContext) == (((d_259_beaconKeyResult_).beaconKeyMaterials).encryptionContext))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(200,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateDuplicate():
        d_267_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_268_valueOrError0_: Wrappers.Result = None
        out102_: Wrappers.Result
        out102_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_268_valueOrError0_ = out102_
        if not(not((d_268_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(209,21): " + _dafny.string_of(d_268_valueOrError0_))
        d_267_kmsClient_ = (d_268_valueOrError0_).Extract()
        d_269_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_270_valueOrError1_: Wrappers.Result = None
        out103_: Wrappers.Result
        out103_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_270_valueOrError1_ = out103_
        if not(not((d_270_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(210,21): " + _dafny.string_of(d_270_valueOrError1_))
        d_269_ddbClient_ = (d_270_valueOrError1_).Extract()
        d_271_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_271_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_272_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_272_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_271_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_269_ddbClient_), Wrappers.Option_Some(d_267_kmsClient_))
        d_273_keyStore_: KeyStore.KeyStoreClient
        d_274_valueOrError2_: Wrappers.Result = None
        out104_: Wrappers.Result
        out104_ = KeyStore.default__.KeyStore(d_272_keyStoreConfig_)
        d_274_valueOrError2_ = out104_
        if not(not((d_274_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(223,20): " + _dafny.string_of(d_274_valueOrError2_))
        d_273_keyStore_ = (d_274_valueOrError2_).Extract()
        d_275_attempt_: Wrappers.Result
        out105_: Wrappers.Result
        out105_ = (d_273_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(Fixtures.default__.branchKeyId), Wrappers.Option_None()))
        d_275_attempt_ = out105_
        if not((d_275_attempt_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(230,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillFail():
        d_276_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_277_valueOrError0_: Wrappers.Result = None
        out106_: Wrappers.Result
        out106_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_277_valueOrError0_ = out106_
        if not(not((d_277_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(236,21): " + _dafny.string_of(d_277_valueOrError0_))
        d_276_ddbClient_ = (d_277_valueOrError0_).Extract()
        d_278_encryptionContext_: _dafny.Map
        d_278_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_279_output_: Wrappers.Result
        out107_: Wrappers.Result
        out107_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_278_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_278_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_278_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_276_ddbClient_)
        d_279_output_ = out107_
        if not((d_279_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(255,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillWithADifferentVersionFail():
        d_280_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_281_valueOrError0_: Wrappers.Result = None
        out108_: Wrappers.Result
        out108_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_281_valueOrError0_ = out108_
        if not(not((d_281_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(261,21): " + _dafny.string_of(d_281_valueOrError0_))
        d_280_ddbClient_ = (d_281_valueOrError0_).Extract()
        d_282_encryptionContext_: _dafny.Map
        d_282_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, _dafny.Seq("!= branchKeyIdActiveVersion"), _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_283_output_: Wrappers.Result
        out109_: Wrappers.Result
        out109_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_282_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_282_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_282_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_280_ddbClient_)
        d_283_output_ = out109_
        if not((d_283_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(280,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

