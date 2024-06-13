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

# Module: TestAwsKmsRsaKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestKmsRsaRoundtrip():
        d_768_mpl_: MaterialProviders.MaterialProvidersClient
        d_769_valueOrError0_: Wrappers.Result = None
        out301_: Wrappers.Result
        out301_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_769_valueOrError0_ = out301_
        if not(not((d_769_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(21,15): " + _dafny.string_of(d_769_valueOrError0_))
        d_768_mpl_ = (d_769_valueOrError0_).Extract()
        d_770_publicKey_: _dafny.Seq
        d_771_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_771_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.KMS__RSA__PUBLIC__KEY)
        if not(not((d_771_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(23,21): " + _dafny.string_of(d_771_valueOrError1_))
        d_770_publicKey_ = (d_771_valueOrError1_).Extract()
        d_772_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_773_valueOrError2_: Wrappers.Result = None
        out302_: Wrappers.Result
        out302_ = (d_768_mpl_).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_773_valueOrError2_ = out302_
        if not(not((d_773_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(25,26): " + _dafny.string_of(d_773_valueOrError2_))
        d_772_clientSupplier_ = (d_773_valueOrError2_).Extract()
        d_774_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_775_valueOrError3_: Wrappers.Result = None
        out303_: Wrappers.Result
        out303_ = (d_772_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_775_valueOrError3_ = out303_
        if not(not((d_775_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(26,21): " + _dafny.string_of(d_775_valueOrError3_))
        d_774_kmsClient_ = (d_775_valueOrError3_).Extract()
        d_776_kmsRsaKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_777_valueOrError4_: Wrappers.Result = None
        out304_: Wrappers.Result
        out304_ = (d_768_mpl_).CreateAwsKmsRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_770_publicKey_), TestUtils.default__.KMS__RSA__PRIVATE__KEY__ARN, ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_774_kmsClient_), Wrappers.Option_None()))
        d_777_valueOrError4_ = out304_
        if not(not((d_777_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(28,25): " + _dafny.string_of(d_777_valueOrError4_))
        d_776_kmsRsaKeyring_ = (d_777_valueOrError4_).Extract()
        d_778_encryptionContext_: _dafny.Map
        out305_: _dafny.Map
        out305_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_778_encryptionContext_ = out305_
        d_779_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_779_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_780_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_780_suite_ = AlgorithmSuites.default__.GetSuite(d_779_algorithmSuiteId_)
        d_781_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_782_valueOrError5_: Wrappers.Result = None
        d_782_valueOrError5_ = (d_768_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_779_algorithmSuiteId_, d_778_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_782_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(40,33): " + _dafny.string_of(d_782_valueOrError5_))
        d_781_encryptionMaterialsIn_ = (d_782_valueOrError5_).Extract()
        d_783_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_784_valueOrError6_: Wrappers.Result = None
        out306_: Wrappers.Result
        out306_ = (d_776_kmsRsaKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_781_encryptionMaterialsIn_))
        d_784_valueOrError6_ = out306_
        if not(not((d_784_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(50,34): " + _dafny.string_of(d_784_valueOrError6_))
        d_783_encryptionMaterialsOut_ = (d_784_valueOrError6_).Extract()
        d_785___v0_: tuple
        d_786_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_786_valueOrError7_ = (d_768_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_783_encryptionMaterialsOut_).materials)
        if not(not((d_786_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(54,13): " + _dafny.string_of(d_786_valueOrError7_))
        d_785___v0_ = (d_786_valueOrError7_).Extract()
        if not((len(((d_783_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_787_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_787_edk_ = (((d_783_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_788_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_789_valueOrError8_: Wrappers.Result = None
        d_789_valueOrError8_ = (d_768_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_779_algorithmSuiteId_, d_778_encryptionContext_, _dafny.Seq([])))
        if not(not((d_789_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(60,33): " + _dafny.string_of(d_789_valueOrError8_))
        d_788_decryptionMaterialsIn_ = (d_789_valueOrError8_).Extract()
        d_790_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_791_valueOrError9_: Wrappers.Result = None
        out307_: Wrappers.Result
        out307_ = (d_776_kmsRsaKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_788_decryptionMaterialsIn_, _dafny.Seq([d_787_edk_])))
        d_791_valueOrError9_ = out307_
        if not(not((d_791_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(67,34): " + _dafny.string_of(d_791_valueOrError9_))
        d_790_decryptionMaterialsOut_ = (d_791_valueOrError9_).Extract()
        if not((((d_783_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_790_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsRsaWithAsymmetricSignatureFails():
        d_792_mpl_: MaterialProviders.MaterialProvidersClient
        d_793_valueOrError0_: Wrappers.Result = None
        out308_: Wrappers.Result
        out308_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_793_valueOrError0_ = out308_
        if not(not((d_793_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(79,15): " + _dafny.string_of(d_793_valueOrError0_))
        d_792_mpl_ = (d_793_valueOrError0_).Extract()
        d_794_publicKey_: _dafny.Seq
        d_795_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_795_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.KMS__RSA__PUBLIC__KEY)
        if not(not((d_795_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(81,21): " + _dafny.string_of(d_795_valueOrError1_))
        d_794_publicKey_ = (d_795_valueOrError1_).Extract()
        d_796_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_797_valueOrError2_: Wrappers.Result = None
        out309_: Wrappers.Result
        out309_ = (d_792_mpl_).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_797_valueOrError2_ = out309_
        if not(not((d_797_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(83,26): " + _dafny.string_of(d_797_valueOrError2_))
        d_796_clientSupplier_ = (d_797_valueOrError2_).Extract()
        d_798_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_799_valueOrError3_: Wrappers.Result = None
        out310_: Wrappers.Result
        out310_ = (d_796_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_799_valueOrError3_ = out310_
        if not(not((d_799_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(84,21): " + _dafny.string_of(d_799_valueOrError3_))
        d_798_kmsClient_ = (d_799_valueOrError3_).Extract()
        d_800_kmsRsaKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_801_valueOrError4_: Wrappers.Result = None
        out311_: Wrappers.Result
        out311_ = (d_792_mpl_).CreateAwsKmsRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_794_publicKey_), TestUtils.default__.KMS__RSA__PRIVATE__KEY__ARN, ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_798_kmsClient_), Wrappers.Option_None()))
        d_801_valueOrError4_ = out311_
        if not(not((d_801_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(86,25): " + _dafny.string_of(d_801_valueOrError4_))
        d_800_kmsRsaKeyring_ = (d_801_valueOrError4_).Extract()
        d_802_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_802_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384())
        d_803_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_803_suite_ = AlgorithmSuites.default__.GetSuite(d_802_algorithmSuiteId_)
        d_804_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_805_valueOrError5_: Wrappers.Result = None
        d_805_valueOrError5_ = (d_792_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_802_algorithmSuiteId_, _dafny.Map({}), _dafny.Seq([]), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0])), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0]))))
        if not(not((d_805_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(96,33): " + _dafny.string_of(d_805_valueOrError5_))
        d_804_encryptionMaterialsIn_ = (d_805_valueOrError5_).Extract()
        d_806_encryptionMaterialsOutRes_: Wrappers.Result
        out312_: Wrappers.Result
        out312_ = (d_800_kmsRsaKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_804_encryptionMaterialsIn_))
        d_806_encryptionMaterialsOutRes_ = out312_
        if not((d_806_encryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_806_encryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_806_encryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_807_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_808_valueOrError6_: Wrappers.Result = None
        d_808_valueOrError6_ = (d_792_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_802_algorithmSuiteId_, (d_804_encryptionMaterialsIn_).encryptionContext, _dafny.Seq([])))
        if not(not((d_808_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(115,33): " + _dafny.string_of(d_808_valueOrError6_))
        d_807_decryptionMaterialsIn_ = (d_808_valueOrError6_).Extract()
        d_809_decryptionMaterialsOutRes_: Wrappers.Result
        out313_: Wrappers.Result
        out313_ = (d_800_kmsRsaKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_807_decryptionMaterialsIn_, _dafny.Seq([])))
        d_809_decryptionMaterialsOutRes_ = out313_
        if not((d_809_decryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_809_decryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_809_decryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(131,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

