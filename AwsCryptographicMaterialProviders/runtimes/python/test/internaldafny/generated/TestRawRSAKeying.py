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

# Module: TestRawRSAKeying

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_680_mpl_: MaterialProviders.MaterialProvidersClient
        d_681_valueOrError0_: Wrappers.Result = None
        out264_: Wrappers.Result
        out264_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_681_valueOrError0_ = out264_
        if not(not((d_681_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(20,15): " + _dafny.string_of(d_681_valueOrError0_))
        d_680_mpl_ = (d_681_valueOrError0_).Extract()
        d_682_namespace_: _dafny.Seq
        d_683_name_: _dafny.Seq
        out265_: _dafny.Seq
        out266_: _dafny.Seq
        out265_, out266_ = TestUtils.default__.NamespaceAndName(0)
        d_682_namespace_ = out265_
        d_683_name_ = out266_
        d_684_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out267_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out267_ = default__.GenerateKeyPair(2048)
        d_684_keys_ = out267_
        d_685_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_686_valueOrError1_: Wrappers.Result = None
        out268_: Wrappers.Result
        out268_ = (d_680_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_682_namespace_, d_683_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_684_keys_).publicKey).pem), Wrappers.Option_Some(((d_684_keys_).privateKey).pem)))
        d_686_valueOrError1_ = out268_
        if not(not((d_686_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(24,25): " + _dafny.string_of(d_686_valueOrError1_))
        d_685_rawRSAKeyring_ = (d_686_valueOrError1_).Extract()
        d_687_encryptionContext_: _dafny.Map
        out269_: _dafny.Map
        out269_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_687_encryptionContext_ = out269_
        d_688_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_688_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_689_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_690_valueOrError2_: Wrappers.Result = None
        d_690_valueOrError2_ = (d_680_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_688_algorithmSuiteId_, d_687_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_690_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(37,33): " + _dafny.string_of(d_690_valueOrError2_))
        d_689_encryptionMaterialsIn_ = (d_690_valueOrError2_).Extract()
        d_691_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_692_valueOrError3_: Wrappers.Result = None
        out270_: Wrappers.Result
        out270_ = (d_685_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_689_encryptionMaterialsIn_))
        d_692_valueOrError3_ = out270_
        if not(not((d_692_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(47,34): " + _dafny.string_of(d_692_valueOrError3_))
        d_691_encryptionMaterialsOut_ = (d_692_valueOrError3_).Extract()
        d_693___v0_: tuple
        d_694_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_694_valueOrError4_ = (d_680_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_691_encryptionMaterialsOut_).materials)
        if not(not((d_694_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(50,13): " + _dafny.string_of(d_694_valueOrError4_))
        d_693___v0_ = (d_694_valueOrError4_).Extract()
        d_695_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_695_edk_ = (((d_691_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_696_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_697_valueOrError5_: Wrappers.Result = None
        d_697_valueOrError5_ = (d_680_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_688_algorithmSuiteId_, d_687_encryptionContext_, _dafny.Seq([])))
        if not(not((d_697_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(54,33): " + _dafny.string_of(d_697_valueOrError5_))
        d_696_decryptionMaterialsIn_ = (d_697_valueOrError5_).Extract()
        d_698_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_699_valueOrError6_: Wrappers.Result = None
        out271_: Wrappers.Result
        out271_ = (d_685_rawRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_696_decryptionMaterialsIn_, _dafny.Seq([d_695_edk_])))
        d_699_valueOrError6_ = out271_
        if not(not((d_699_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(62,34): " + _dafny.string_of(d_699_valueOrError6_))
        d_698_decryptionMaterialsOut_ = (d_699_valueOrError6_).Extract()
        if not((((d_698_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_691_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_700_mpl_: MaterialProviders.MaterialProvidersClient
        d_701_valueOrError0_: Wrappers.Result = None
        out272_: Wrappers.Result
        out272_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_701_valueOrError0_ = out272_
        if not(not((d_701_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(80,15): " + _dafny.string_of(d_701_valueOrError0_))
        d_700_mpl_ = (d_701_valueOrError0_).Extract()
        d_702_namespace_: _dafny.Seq
        d_703_name_: _dafny.Seq
        out273_: _dafny.Seq
        out274_: _dafny.Seq
        out273_, out274_ = TestUtils.default__.NamespaceAndName(0)
        d_702_namespace_ = out273_
        d_703_name_ = out274_
        d_704_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out275_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out275_ = default__.GenerateKeyPair(2048)
        d_704_keys_ = out275_
        d_705_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_706_valueOrError1_: Wrappers.Result = None
        out276_: Wrappers.Result
        out276_ = (d_700_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_702_namespace_, d_703_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_704_keys_).publicKey).pem), Wrappers.Option_Some(((d_704_keys_).privateKey).pem)))
        d_706_valueOrError1_ = out276_
        if not(not((d_706_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(84,25): " + _dafny.string_of(d_706_valueOrError1_))
        d_705_rawRSAKeyring_ = (d_706_valueOrError1_).Extract()
        d_707_mismatchedRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_708_valueOrError2_: Wrappers.Result = None
        out277_: Wrappers.Result
        out277_ = (d_700_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_702_namespace_, _dafny.Seq("mismatched"), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_704_keys_).publicKey).pem), Wrappers.Option_Some(((d_704_keys_).privateKey).pem)))
        d_708_valueOrError2_ = out277_
        if not(not((d_708_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(92,32): " + _dafny.string_of(d_708_valueOrError2_))
        d_707_mismatchedRSAKeyring_ = (d_708_valueOrError2_).Extract()
        d_709_encryptionContext_: _dafny.Map
        out278_: _dafny.Map
        out278_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_709_encryptionContext_ = out278_
        d_710_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_710_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_711_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_712_valueOrError3_: Wrappers.Result = None
        d_712_valueOrError3_ = (d_700_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_710_algorithmSuiteId_, d_709_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_712_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(105,33): " + _dafny.string_of(d_712_valueOrError3_))
        d_711_encryptionMaterialsIn_ = (d_712_valueOrError3_).Extract()
        d_713_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_714_valueOrError4_: Wrappers.Result = None
        out279_: Wrappers.Result
        out279_ = (d_705_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_711_encryptionMaterialsIn_))
        d_714_valueOrError4_ = out279_
        if not(not((d_714_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(114,34): " + _dafny.string_of(d_714_valueOrError4_))
        d_713_encryptionMaterialsOut_ = (d_714_valueOrError4_).Extract()
        d_715___v1_: tuple
        d_716_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_716_valueOrError5_ = (d_700_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_713_encryptionMaterialsOut_).materials)
        if not(not((d_716_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(117,13): " + _dafny.string_of(d_716_valueOrError5_))
        d_715___v1_ = (d_716_valueOrError5_).Extract()
        d_717_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_717_edk_ = (((d_713_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_718_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_719_valueOrError6_: Wrappers.Result = None
        d_719_valueOrError6_ = (d_700_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_710_algorithmSuiteId_, d_709_encryptionContext_, _dafny.Seq([])))
        if not(not((d_719_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(121,33): " + _dafny.string_of(d_719_valueOrError6_))
        d_718_decryptionMaterialsIn_ = (d_719_valueOrError6_).Extract()
        d_720_decryptionMaterialsOut_: Wrappers.Result
        out280_: Wrappers.Result
        out280_ = (d_707_mismatchedRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_718_decryptionMaterialsIn_, _dafny.Seq([d_717_edk_])))
        d_720_decryptionMaterialsOut_ = out280_
        if not((d_720_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(135,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_720_decryptionMaterialsOut_).error).is_CollectionOfErrors):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_720_decryptionMaterialsOut_).error).list)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_720_decryptionMaterialsOut_).error).list)[0]).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((((d_720_decryptionMaterialsOut_).error).list)[0]).message) == (ErrorMessages.default__.IncorrectRawDataKeys(_dafny.Seq("0"), _dafny.Seq("RSAKeyring"), d_702_namespace_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(139,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptFailure():
        d_721_mpl_: MaterialProviders.MaterialProvidersClient
        d_722_valueOrError0_: Wrappers.Result = None
        out281_: Wrappers.Result
        out281_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_722_valueOrError0_ = out281_
        if not(not((d_722_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(145,15): " + _dafny.string_of(d_722_valueOrError0_))
        d_721_mpl_ = (d_722_valueOrError0_).Extract()
        d_723_namespace_: _dafny.Seq
        d_724_name_: _dafny.Seq
        out282_: _dafny.Seq
        out283_: _dafny.Seq
        out282_, out283_ = TestUtils.default__.NamespaceAndName(0)
        d_723_namespace_ = out282_
        d_724_name_ = out283_
        d_725_encryptKeys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out284_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out284_ = default__.GenerateKeyPair(2048)
        d_725_encryptKeys_ = out284_
        d_726_decryptKeys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out285_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out285_ = default__.GenerateKeyPair(2048)
        d_726_decryptKeys_ = out285_
        d_727_encryptKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_728_valueOrError1_: Wrappers.Result = None
        out286_: Wrappers.Result
        out286_ = (d_721_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_723_namespace_, d_724_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_725_encryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_725_encryptKeys_).privateKey).pem)))
        d_728_valueOrError1_ = out286_
        if not(not((d_728_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(153,26): " + _dafny.string_of(d_728_valueOrError1_))
        d_727_encryptKeyring_ = (d_728_valueOrError1_).Extract()
        d_729_decryptKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_730_valueOrError2_: Wrappers.Result = None
        out287_: Wrappers.Result
        out287_ = (d_721_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_723_namespace_, d_724_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_726_decryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_726_decryptKeys_).privateKey).pem)))
        d_730_valueOrError2_ = out287_
        if not(not((d_730_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(161,26): " + _dafny.string_of(d_730_valueOrError2_))
        d_729_decryptKeyring_ = (d_730_valueOrError2_).Extract()
        d_731_encryptionContext_: _dafny.Map
        out288_: _dafny.Map
        out288_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_731_encryptionContext_ = out288_
        d_732_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_732_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_733_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_734_valueOrError3_: Wrappers.Result = None
        d_734_valueOrError3_ = (d_721_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_732_algorithmSuiteId_, d_731_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_734_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(172,33): " + _dafny.string_of(d_734_valueOrError3_))
        d_733_encryptionMaterialsIn_ = (d_734_valueOrError3_).Extract()
        d_735_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_736_valueOrError4_: Wrappers.Result = None
        out289_: Wrappers.Result
        out289_ = (d_727_encryptKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_733_encryptionMaterialsIn_))
        d_736_valueOrError4_ = out289_
        if not(not((d_736_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(181,34): " + _dafny.string_of(d_736_valueOrError4_))
        d_735_encryptionMaterialsOut_ = (d_736_valueOrError4_).Extract()
        d_737___v2_: tuple
        d_738_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_738_valueOrError5_ = (d_721_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_735_encryptionMaterialsOut_).materials)
        if not(not((d_738_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(184,13): " + _dafny.string_of(d_738_valueOrError5_))
        d_737___v2_ = (d_738_valueOrError5_).Extract()
        d_739_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_739_edk_ = (((d_735_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_740_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_741_valueOrError6_: Wrappers.Result = None
        d_741_valueOrError6_ = (d_721_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_732_algorithmSuiteId_, d_731_encryptionContext_, _dafny.Seq([])))
        if not(not((d_741_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(188,33): " + _dafny.string_of(d_741_valueOrError6_))
        d_740_decryptionMaterialsIn_ = (d_741_valueOrError6_).Extract()
        d_742_decryptionMaterialsOut_: Wrappers.Result
        out290_: Wrappers.Result
        out290_ = (d_729_decryptKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_740_decryptionMaterialsIn_, _dafny.Seq([d_739_edk_])))
        d_742_decryptionMaterialsOut_ = out290_
        if not((d_742_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_743_mpl_: MaterialProviders.MaterialProvidersClient
        d_744_valueOrError0_: Wrappers.Result = None
        out291_: Wrappers.Result
        out291_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_744_valueOrError0_ = out291_
        if not(not((d_744_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(218,15): " + _dafny.string_of(d_744_valueOrError0_))
        d_743_mpl_ = (d_744_valueOrError0_).Extract()
        d_745_namespace_: _dafny.Seq
        d_746_name_: _dafny.Seq
        out292_: _dafny.Seq
        out293_: _dafny.Seq
        out292_, out293_ = TestUtils.default__.NamespaceAndName(0)
        d_745_namespace_ = out292_
        d_746_name_ = out293_
        d_747_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out294_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out294_ = default__.GenerateKeyPair(2048)
        d_747_keys_ = out294_
        d_748_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_749_valueOrError1_: Wrappers.Result = None
        out295_: Wrappers.Result
        out295_ = (d_743_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_745_namespace_, d_746_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_747_keys_).publicKey).pem), Wrappers.Option_Some(((d_747_keys_).privateKey).pem)))
        d_749_valueOrError1_ = out295_
        if not(not((d_749_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(222,25): " + _dafny.string_of(d_749_valueOrError1_))
        d_748_rawRSAKeyring_ = (d_749_valueOrError1_).Extract()
        d_750_encryptionContext_: _dafny.Map
        out296_: _dafny.Map
        out296_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_750_encryptionContext_ = out296_
        d_751_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_751_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_752_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_753_valueOrError2_: Wrappers.Result = None
        d_753_valueOrError2_ = (d_743_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_751_algorithmSuiteId_, d_750_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_753_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(235,33): " + _dafny.string_of(d_753_valueOrError2_))
        d_752_encryptionMaterialsIn_ = (d_753_valueOrError2_).Extract()
        d_754_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_755_valueOrError3_: Wrappers.Result = None
        out297_: Wrappers.Result
        out297_ = (d_748_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_752_encryptionMaterialsIn_))
        d_755_valueOrError3_ = out297_
        if not(not((d_755_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(244,34): " + _dafny.string_of(d_755_valueOrError3_))
        d_754_encryptionMaterialsOut_ = (d_755_valueOrError3_).Extract()
        d_756___v3_: tuple
        d_757_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_757_valueOrError4_ = (d_743_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_754_encryptionMaterialsOut_).materials)
        if not(not((d_757_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(247,13): " + _dafny.string_of(d_757_valueOrError4_))
        d_756___v3_ = (d_757_valueOrError4_).Extract()
        d_758_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_758_edk_ = (((d_754_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_759_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_760_valueOrError5_: Wrappers.Result = None
        d_760_valueOrError5_ = (d_743_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_751_algorithmSuiteId_, d_750_encryptionContext_, _dafny.Seq([])))
        if not(not((d_760_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(251,33): " + _dafny.string_of(d_760_valueOrError5_))
        d_759_decryptionMaterialsIn_ = (d_760_valueOrError5_).Extract()
        d_761_fakeEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_761_fakeEdk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((d_758_edk_).keyProviderId, (d_758_edk_).keyProviderInfo, _dafny.Seq([0 for d_762_i_ in range(len((d_758_edk_).ciphertext))]))
        d_763_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_764_valueOrError6_: Wrappers.Result = None
        out298_: Wrappers.Result
        out298_ = (d_748_rawRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_759_decryptionMaterialsIn_, _dafny.Seq([d_761_fakeEdk_, d_758_edk_])))
        d_764_valueOrError6_ = out298_
        if not(not((d_764_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(268,34): " + _dafny.string_of(d_764_valueOrError6_))
        d_763_decryptionMaterialsOut_ = (d_764_valueOrError6_).Extract()
        if not((((d_763_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_754_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(279,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GenerateKeyPair(keyModulusLength):
        keys: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput = None
        d_765_crypto_: AtomicPrimitives.AtomicPrimitivesClient
        d_766_valueOrError0_: Wrappers.Result = None
        out299_: Wrappers.Result
        out299_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_766_valueOrError0_ = out299_
        if not(not((d_766_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(286,18): " + _dafny.string_of(d_766_valueOrError0_))
        d_765_crypto_ = (d_766_valueOrError0_).Extract()
        d_767_valueOrError1_: Wrappers.Result = None
        out300_: Wrappers.Result
        out300_ = (d_765_crypto_).GenerateRSAKeyPair(AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(keyModulusLength))
        d_767_valueOrError1_ = out300_
        if not(not((d_767_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(288,12): " + _dafny.string_of(d_767_valueOrError1_))
        keys = (d_767_valueOrError1_).Extract()
        return keys

