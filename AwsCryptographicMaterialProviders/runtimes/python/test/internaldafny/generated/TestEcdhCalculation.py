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
import TestLocalCMC as TestLocalCMC
import TestStormTracker as TestStormTracker

# Module: TestEcdhCalculation

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestKmsDeriveSharedSecretOfflineCalculation():
        d_1523_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1524_valueOrError0_: Wrappers.Result = None
        out590_: Wrappers.Result
        out590_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1524_valueOrError0_ = out590_
        if not(not((d_1524_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(32,21): " + _dafny.string_of(d_1524_valueOrError0_))
        d_1523_kmsClient_ = (d_1524_valueOrError0_).Extract()
        d_1525_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_1526_valueOrError1_: Wrappers.Result = None
        out591_: Wrappers.Result
        out591_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_1526_valueOrError1_ = out591_
        if not(not((d_1526_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(33,22): " + _dafny.string_of(d_1526_valueOrError1_))
        d_1525_primitives_ = (d_1526_valueOrError1_).Extract()
        d_1527_keyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_1528_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out592_: Wrappers.Result
        out592_ = (d_1525_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_1528_valueOrError2_ = out592_
        if not(not((d_1528_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(35,19): " + _dafny.string_of(d_1528_valueOrError2_))
        d_1527_keyPair_ = (d_1528_valueOrError2_).Extract()
        if not(((1) <= (len(((d_1527_keyPair_).publicKey).der))) and ((len(((d_1527_keyPair_).publicKey).der)) <= (8192))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(41,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1529_kmsSharedSecret_: Wrappers.Result
        out593_: Wrappers.Result
        out593_ = (d_1523_kmsClient_).DeriveSharedSecret(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(default__.senderKmsKey, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), ((d_1527_keyPair_).publicKey).der, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_1529_kmsSharedSecret_ = out593_
        if not((d_1529_kmsSharedSecret_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(50,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_1529_kmsSharedSecret_).value).SharedSecret).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1530_publicKeyResponse_: Wrappers.Result
        out594_: Wrappers.Result
        out594_ = (d_1523_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(default__.senderKmsKey, Wrappers.Option_None()))
        d_1530_publicKeyResponse_ = out594_
        if not((d_1530_publicKeyResponse_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(59,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs5_ = (d_1530_publicKeyResponse_).value
        d_1531___v0_ = let_tmp_rhs5_.KeyId
        d_1532_PublicKey_ = let_tmp_rhs5_.PublicKey
        d_1533___v1_ = let_tmp_rhs5_.CustomerMasterKeySpec
        d_1534___v2_ = let_tmp_rhs5_.KeySpec
        d_1535___v3_ = let_tmp_rhs5_.KeyUsage
        d_1536___v4_ = let_tmp_rhs5_.EncryptionAlgorithms
        d_1537___v5_ = let_tmp_rhs5_.SigningAlgorithms
        d_1538___v6_ = let_tmp_rhs5_.KeyAgreementAlgorithms
        if not((d_1532_PublicKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1539_offlineSharedSecret_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
        d_1540_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
        out595_: Wrappers.Result
        out595_ = (d_1525_primitives_).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), (d_1527_keyPair_).privateKey, AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_1532_PublicKey_).value)))
        d_1540_valueOrError3_ = out595_
        if not(not((d_1540_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(64,31): " + _dafny.string_of(d_1540_valueOrError3_))
        d_1539_offlineSharedSecret_ = (d_1540_valueOrError3_).Extract()
        if not(((((d_1529_kmsSharedSecret_).value).SharedSecret).value) == ((d_1539_offlineSharedSecret_).sharedSecret)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsDeriveSharedSecretOfflineCalculationCurves():
        d_1541_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1542_valueOrError0_: Wrappers.Result = None
        out596_: Wrappers.Result
        out596_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1542_valueOrError0_ = out596_
        if not(not((d_1542_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(77,21): " + _dafny.string_of(d_1542_valueOrError0_))
        d_1541_kmsClient_ = (d_1542_valueOrError0_).Extract()
        d_1543_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_1544_valueOrError1_: Wrappers.Result = None
        out597_: Wrappers.Result
        out597_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_1544_valueOrError1_ = out597_
        if not(not((d_1544_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(78,22): " + _dafny.string_of(d_1544_valueOrError1_))
        d_1543_primitives_ = (d_1544_valueOrError1_).Extract()
        hi5_ = len(default__.senderArns)
        for d_1545_i_ in range(0, hi5_):
            d_1546_keyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_1547_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out598_: Wrappers.Result
            out598_ = (d_1543_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput((default__.curveSpecs)[d_1545_i_]))
            d_1547_valueOrError2_ = out598_
            if not(not((d_1547_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(82,21): " + _dafny.string_of(d_1547_valueOrError2_))
            d_1546_keyPair_ = (d_1547_valueOrError2_).Extract()
            if not(((1) <= (len(((d_1546_keyPair_).publicKey).der))) and ((len(((d_1546_keyPair_).publicKey).der)) <= (8192))):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(87,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1548_kmsSharedSecret_: Wrappers.Result
            out599_: Wrappers.Result
            out599_ = (d_1541_kmsClient_).DeriveSharedSecret(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest((default__.senderArns)[d_1545_i_], ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), ((d_1546_keyPair_).publicKey).der, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
            d_1548_kmsSharedSecret_ = out599_
            if not((d_1548_kmsSharedSecret_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(96,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not((((d_1548_kmsSharedSecret_).value).SharedSecret).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(97,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1549_publicKeyResponse_: Wrappers.Result
            out600_: Wrappers.Result
            out600_ = (d_1541_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((default__.senderArns)[d_1545_i_], Wrappers.Option_None()))
            d_1549_publicKeyResponse_ = out600_
            if not((d_1549_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(105,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs6_ = (d_1549_publicKeyResponse_).value
            d_1550___v7_ = let_tmp_rhs6_.KeyId
            d_1551_PublicKey_ = let_tmp_rhs6_.PublicKey
            d_1552___v8_ = let_tmp_rhs6_.CustomerMasterKeySpec
            d_1553___v9_ = let_tmp_rhs6_.KeySpec
            d_1554___v10_ = let_tmp_rhs6_.KeyUsage
            d_1555___v11_ = let_tmp_rhs6_.EncryptionAlgorithms
            d_1556___v12_ = let_tmp_rhs6_.SigningAlgorithms
            d_1557___v13_ = let_tmp_rhs6_.KeyAgreementAlgorithms
            if not((d_1551_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(108,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1558_offlineSharedSecret_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_1559_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out601_: Wrappers.Result
            out601_ = (d_1543_primitives_).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput((default__.curveSpecs)[d_1545_i_], (d_1546_keyPair_).privateKey, AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_1551_PublicKey_).value)))
            d_1559_valueOrError3_ = out601_
            if not(not((d_1559_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(110,33): " + _dafny.string_of(d_1559_valueOrError3_))
            d_1558_offlineSharedSecret_ = (d_1559_valueOrError3_).Extract()
            if not(((((d_1548_kmsSharedSecret_).value).SharedSecret).value) == ((d_1558_offlineSharedSecret_).sharedSecret)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(118,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOfflineDeriveSharedSecretStaticKeys():
        d_1560_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1561_valueOrError0_: Wrappers.Result = None
        out602_: Wrappers.Result
        out602_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1561_valueOrError0_ = out602_
        if not(not((d_1561_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(125,21): " + _dafny.string_of(d_1561_valueOrError0_))
        d_1560_kmsClient_ = (d_1561_valueOrError0_).Extract()
        d_1562_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_1563_valueOrError1_: Wrappers.Result = None
        out603_: Wrappers.Result
        out603_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_1563_valueOrError1_ = out603_
        if not(not((d_1563_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(126,22): " + _dafny.string_of(d_1563_valueOrError1_))
        d_1562_primitives_ = (d_1563_valueOrError1_).Extract()
        hi6_ = len(default__.curveSpecs)
        for d_1564_i_ in range(0, hi6_):
            d_1565_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_1565_curve_ = (default__.curveSpecs)[d_1564_i_]
            d_1566_senderArn_: _dafny.Seq
            d_1566_senderArn_ = (default__.senderArns)[d_1564_i_]
            d_1567_senderPublicKey_: _dafny.Seq
            d_1568_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1568_valueOrError2_ = Base64.default__.Decode((default__.senderArnPublicKeys)[d_1564_i_])
            if not(not((d_1568_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(132,29): " + _dafny.string_of(d_1568_valueOrError2_))
            d_1567_senderPublicKey_ = (d_1568_valueOrError2_).Extract()
            d_1569_recipientPrivateKey_: _dafny.Seq
            d_1570_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
            d_1570_valueOrError3_ = UTF8.default__.Encode((default__.privateKeyReceivers)[d_1564_i_])
            if not(not((d_1570_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(133,33): " + _dafny.string_of(d_1570_valueOrError3_))
            d_1569_recipientPrivateKey_ = (d_1570_valueOrError3_).Extract()
            d_1571_recipientPublicKey_: _dafny.Seq
            d_1572_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1572_valueOrError4_ = Base64.default__.Decode((default__.publicKeyReceivers)[d_1564_i_])
            if not(not((d_1572_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(134,32): " + _dafny.string_of(d_1572_valueOrError4_))
            d_1571_recipientPublicKey_ = (d_1572_valueOrError4_).Extract()
            d_1573_kmsSharedSecret_: Wrappers.Result
            out604_: Wrappers.Result
            out604_ = (d_1560_kmsClient_).DeriveSharedSecret(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(d_1566_senderArn_, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), d_1571_recipientPublicKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
            d_1573_kmsSharedSecret_ = out604_
            if not((d_1573_kmsSharedSecret_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(143,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not((((d_1573_kmsSharedSecret_).value).SharedSecret).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(144,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1574_offlineSharedSecret_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_1575_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out605_: Wrappers.Result
            out605_ = (d_1562_primitives_).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput((default__.curveSpecs)[d_1564_i_], AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_1569_recipientPrivateKey_), AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1567_senderPublicKey_)))
            d_1575_valueOrError5_ = out605_
            if not(not((d_1575_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(146,33): " + _dafny.string_of(d_1575_valueOrError5_))
            d_1574_offlineSharedSecret_ = (d_1575_valueOrError5_).Extract()
            if not(((((d_1573_kmsSharedSecret_).value).SharedSecret).value) == ((d_1574_offlineSharedSecret_).sharedSecret)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(155,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def senderKmsKey(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9")
    @_dafny.classproperty
    def senderArns(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
    @_dafny.classproperty
    def curveSpecs(instance):
        return _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
    @_dafny.classproperty
    def senderArnPublicKeys(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S])
    @_dafny.classproperty
    def privateKeyReceivers(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PRIVATE, TestUtils.default__.ECC__P384__PRIVATE, TestUtils.default__.ECC__P521__PRIVATE])
    @_dafny.classproperty
    def publicKeyReceivers(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PUBLIC, TestUtils.default__.ECC__P384__PUBLIC, TestUtils.default__.ECC__P521__PUBLIC])
    @_dafny.classproperty
    def recipientKmsKey(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5")
