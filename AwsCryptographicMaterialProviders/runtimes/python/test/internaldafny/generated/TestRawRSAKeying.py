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

# Module: TestRawRSAKeying

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_921_mpl_: MaterialProviders.MaterialProvidersClient
        d_922_valueOrError0_: Wrappers.Result = None
        out363_: Wrappers.Result
        out363_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_922_valueOrError0_ = out363_
        if not(not((d_922_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(20,15): " + _dafny.string_of(d_922_valueOrError0_))
        d_921_mpl_ = (d_922_valueOrError0_).Extract()
        d_923_namespace_: _dafny.Seq
        d_924_name_: _dafny.Seq
        out364_: _dafny.Seq
        out365_: _dafny.Seq
        out364_, out365_ = TestUtils.default__.NamespaceAndName(0)
        d_923_namespace_ = out364_
        d_924_name_ = out365_
        d_925_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out366_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out366_ = default__.GenerateKeyPair(2048)
        d_925_keys_ = out366_
        d_926_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_927_valueOrError1_: Wrappers.Result = None
        out367_: Wrappers.Result
        out367_ = (d_921_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_923_namespace_, d_924_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_925_keys_).publicKey).pem), Wrappers.Option_Some(((d_925_keys_).privateKey).pem)))
        d_927_valueOrError1_ = out367_
        if not(not((d_927_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(24,25): " + _dafny.string_of(d_927_valueOrError1_))
        d_926_rawRSAKeyring_ = (d_927_valueOrError1_).Extract()
        d_928_encryptionContext_: _dafny.Map
        out368_: _dafny.Map
        out368_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_928_encryptionContext_ = out368_
        d_929_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_929_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_930_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_931_valueOrError2_: Wrappers.Result = None
        d_931_valueOrError2_ = (d_921_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_929_algorithmSuiteId_, d_928_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_931_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(37,33): " + _dafny.string_of(d_931_valueOrError2_))
        d_930_encryptionMaterialsIn_ = (d_931_valueOrError2_).Extract()
        d_932_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_933_valueOrError3_: Wrappers.Result = None
        out369_: Wrappers.Result
        out369_ = (d_926_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_930_encryptionMaterialsIn_))
        d_933_valueOrError3_ = out369_
        if not(not((d_933_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(47,34): " + _dafny.string_of(d_933_valueOrError3_))
        d_932_encryptionMaterialsOut_ = (d_933_valueOrError3_).Extract()
        d_934___v0_: tuple
        d_935_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_935_valueOrError4_ = (d_921_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_932_encryptionMaterialsOut_).materials)
        if not(not((d_935_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(50,13): " + _dafny.string_of(d_935_valueOrError4_))
        d_934___v0_ = (d_935_valueOrError4_).Extract()
        d_936_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_936_edk_ = (((d_932_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_937_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_938_valueOrError5_: Wrappers.Result = None
        d_938_valueOrError5_ = (d_921_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_929_algorithmSuiteId_, d_928_encryptionContext_, _dafny.Seq([])))
        if not(not((d_938_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(54,33): " + _dafny.string_of(d_938_valueOrError5_))
        d_937_decryptionMaterialsIn_ = (d_938_valueOrError5_).Extract()
        d_939_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_940_valueOrError6_: Wrappers.Result = None
        out370_: Wrappers.Result
        out370_ = (d_926_rawRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_937_decryptionMaterialsIn_, _dafny.Seq([d_936_edk_])))
        d_940_valueOrError6_ = out370_
        if not(not((d_940_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(62,34): " + _dafny.string_of(d_940_valueOrError6_))
        d_939_decryptionMaterialsOut_ = (d_940_valueOrError6_).Extract()
        if not((((d_939_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_932_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_941_mpl_: MaterialProviders.MaterialProvidersClient
        d_942_valueOrError0_: Wrappers.Result = None
        out371_: Wrappers.Result
        out371_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_942_valueOrError0_ = out371_
        if not(not((d_942_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(80,15): " + _dafny.string_of(d_942_valueOrError0_))
        d_941_mpl_ = (d_942_valueOrError0_).Extract()
        d_943_namespace_: _dafny.Seq
        d_944_name_: _dafny.Seq
        out372_: _dafny.Seq
        out373_: _dafny.Seq
        out372_, out373_ = TestUtils.default__.NamespaceAndName(0)
        d_943_namespace_ = out372_
        d_944_name_ = out373_
        d_945_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out374_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out374_ = default__.GenerateKeyPair(2048)
        d_945_keys_ = out374_
        d_946_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_947_valueOrError1_: Wrappers.Result = None
        out375_: Wrappers.Result
        out375_ = (d_941_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_943_namespace_, d_944_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_945_keys_).publicKey).pem), Wrappers.Option_Some(((d_945_keys_).privateKey).pem)))
        d_947_valueOrError1_ = out375_
        if not(not((d_947_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(84,25): " + _dafny.string_of(d_947_valueOrError1_))
        d_946_rawRSAKeyring_ = (d_947_valueOrError1_).Extract()
        d_948_mismatchedRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_949_valueOrError2_: Wrappers.Result = None
        out376_: Wrappers.Result
        out376_ = (d_941_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_943_namespace_, _dafny.Seq("mismatched"), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_945_keys_).publicKey).pem), Wrappers.Option_Some(((d_945_keys_).privateKey).pem)))
        d_949_valueOrError2_ = out376_
        if not(not((d_949_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(92,32): " + _dafny.string_of(d_949_valueOrError2_))
        d_948_mismatchedRSAKeyring_ = (d_949_valueOrError2_).Extract()
        d_950_encryptionContext_: _dafny.Map
        out377_: _dafny.Map
        out377_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_950_encryptionContext_ = out377_
        d_951_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_951_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_952_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_953_valueOrError3_: Wrappers.Result = None
        d_953_valueOrError3_ = (d_941_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_951_algorithmSuiteId_, d_950_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_953_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(105,33): " + _dafny.string_of(d_953_valueOrError3_))
        d_952_encryptionMaterialsIn_ = (d_953_valueOrError3_).Extract()
        d_954_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_955_valueOrError4_: Wrappers.Result = None
        out378_: Wrappers.Result
        out378_ = (d_946_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_952_encryptionMaterialsIn_))
        d_955_valueOrError4_ = out378_
        if not(not((d_955_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(114,34): " + _dafny.string_of(d_955_valueOrError4_))
        d_954_encryptionMaterialsOut_ = (d_955_valueOrError4_).Extract()
        d_956___v1_: tuple
        d_957_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_957_valueOrError5_ = (d_941_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_954_encryptionMaterialsOut_).materials)
        if not(not((d_957_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(117,13): " + _dafny.string_of(d_957_valueOrError5_))
        d_956___v1_ = (d_957_valueOrError5_).Extract()
        d_958_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_958_edk_ = (((d_954_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_959_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_960_valueOrError6_: Wrappers.Result = None
        d_960_valueOrError6_ = (d_941_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_951_algorithmSuiteId_, d_950_encryptionContext_, _dafny.Seq([])))
        if not(not((d_960_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(121,33): " + _dafny.string_of(d_960_valueOrError6_))
        d_959_decryptionMaterialsIn_ = (d_960_valueOrError6_).Extract()
        d_961_decryptionMaterialsOut_: Wrappers.Result
        out379_: Wrappers.Result
        out379_ = (d_948_mismatchedRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_959_decryptionMaterialsIn_, _dafny.Seq([d_958_edk_])))
        d_961_decryptionMaterialsOut_ = out379_
        if not((d_961_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(135,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_961_decryptionMaterialsOut_).error).is_CollectionOfErrors):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_961_decryptionMaterialsOut_).error).list)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_961_decryptionMaterialsOut_).error).list)[0]).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((((d_961_decryptionMaterialsOut_).error).list)[0]).message) == (ErrorMessages.default__.IncorrectRawDataKeys(_dafny.Seq("0"), _dafny.Seq("RSAKeyring"), d_943_namespace_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(139,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptFailure():
        d_962_mpl_: MaterialProviders.MaterialProvidersClient
        d_963_valueOrError0_: Wrappers.Result = None
        out380_: Wrappers.Result
        out380_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_963_valueOrError0_ = out380_
        if not(not((d_963_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(145,15): " + _dafny.string_of(d_963_valueOrError0_))
        d_962_mpl_ = (d_963_valueOrError0_).Extract()
        d_964_namespace_: _dafny.Seq
        d_965_name_: _dafny.Seq
        out381_: _dafny.Seq
        out382_: _dafny.Seq
        out381_, out382_ = TestUtils.default__.NamespaceAndName(0)
        d_964_namespace_ = out381_
        d_965_name_ = out382_
        d_966_encryptKeys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out383_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out383_ = default__.GenerateKeyPair(2048)
        d_966_encryptKeys_ = out383_
        d_967_decryptKeys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out384_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out384_ = default__.GenerateKeyPair(2048)
        d_967_decryptKeys_ = out384_
        d_968_encryptKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_969_valueOrError1_: Wrappers.Result = None
        out385_: Wrappers.Result
        out385_ = (d_962_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_964_namespace_, d_965_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_966_encryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_966_encryptKeys_).privateKey).pem)))
        d_969_valueOrError1_ = out385_
        if not(not((d_969_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(153,26): " + _dafny.string_of(d_969_valueOrError1_))
        d_968_encryptKeyring_ = (d_969_valueOrError1_).Extract()
        d_970_decryptKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_971_valueOrError2_: Wrappers.Result = None
        out386_: Wrappers.Result
        out386_ = (d_962_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_964_namespace_, d_965_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_967_decryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_967_decryptKeys_).privateKey).pem)))
        d_971_valueOrError2_ = out386_
        if not(not((d_971_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(161,26): " + _dafny.string_of(d_971_valueOrError2_))
        d_970_decryptKeyring_ = (d_971_valueOrError2_).Extract()
        d_972_encryptionContext_: _dafny.Map
        out387_: _dafny.Map
        out387_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_972_encryptionContext_ = out387_
        d_973_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_973_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_974_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_975_valueOrError3_: Wrappers.Result = None
        d_975_valueOrError3_ = (d_962_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_973_algorithmSuiteId_, d_972_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_975_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(172,33): " + _dafny.string_of(d_975_valueOrError3_))
        d_974_encryptionMaterialsIn_ = (d_975_valueOrError3_).Extract()
        d_976_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_977_valueOrError4_: Wrappers.Result = None
        out388_: Wrappers.Result
        out388_ = (d_968_encryptKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_974_encryptionMaterialsIn_))
        d_977_valueOrError4_ = out388_
        if not(not((d_977_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(181,34): " + _dafny.string_of(d_977_valueOrError4_))
        d_976_encryptionMaterialsOut_ = (d_977_valueOrError4_).Extract()
        d_978___v2_: tuple
        d_979_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_979_valueOrError5_ = (d_962_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_976_encryptionMaterialsOut_).materials)
        if not(not((d_979_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(184,13): " + _dafny.string_of(d_979_valueOrError5_))
        d_978___v2_ = (d_979_valueOrError5_).Extract()
        d_980_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_980_edk_ = (((d_976_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_981_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_982_valueOrError6_: Wrappers.Result = None
        d_982_valueOrError6_ = (d_962_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_973_algorithmSuiteId_, d_972_encryptionContext_, _dafny.Seq([])))
        if not(not((d_982_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(188,33): " + _dafny.string_of(d_982_valueOrError6_))
        d_981_decryptionMaterialsIn_ = (d_982_valueOrError6_).Extract()
        d_983_decryptionMaterialsOut_: Wrappers.Result
        out389_: Wrappers.Result
        out389_ = (d_970_decryptKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_981_decryptionMaterialsIn_, _dafny.Seq([d_980_edk_])))
        d_983_decryptionMaterialsOut_ = out389_
        if not((d_983_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_984_mpl_: MaterialProviders.MaterialProvidersClient
        d_985_valueOrError0_: Wrappers.Result = None
        out390_: Wrappers.Result
        out390_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_985_valueOrError0_ = out390_
        if not(not((d_985_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(218,15): " + _dafny.string_of(d_985_valueOrError0_))
        d_984_mpl_ = (d_985_valueOrError0_).Extract()
        d_986_namespace_: _dafny.Seq
        d_987_name_: _dafny.Seq
        out391_: _dafny.Seq
        out392_: _dafny.Seq
        out391_, out392_ = TestUtils.default__.NamespaceAndName(0)
        d_986_namespace_ = out391_
        d_987_name_ = out392_
        d_988_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out393_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out393_ = default__.GenerateKeyPair(2048)
        d_988_keys_ = out393_
        d_989_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_990_valueOrError1_: Wrappers.Result = None
        out394_: Wrappers.Result
        out394_ = (d_984_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_986_namespace_, d_987_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_988_keys_).publicKey).pem), Wrappers.Option_Some(((d_988_keys_).privateKey).pem)))
        d_990_valueOrError1_ = out394_
        if not(not((d_990_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(222,25): " + _dafny.string_of(d_990_valueOrError1_))
        d_989_rawRSAKeyring_ = (d_990_valueOrError1_).Extract()
        d_991_encryptionContext_: _dafny.Map
        out395_: _dafny.Map
        out395_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_991_encryptionContext_ = out395_
        d_992_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_992_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_993_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_994_valueOrError2_: Wrappers.Result = None
        d_994_valueOrError2_ = (d_984_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_992_algorithmSuiteId_, d_991_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_994_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(235,33): " + _dafny.string_of(d_994_valueOrError2_))
        d_993_encryptionMaterialsIn_ = (d_994_valueOrError2_).Extract()
        d_995_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_996_valueOrError3_: Wrappers.Result = None
        out396_: Wrappers.Result
        out396_ = (d_989_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_993_encryptionMaterialsIn_))
        d_996_valueOrError3_ = out396_
        if not(not((d_996_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(244,34): " + _dafny.string_of(d_996_valueOrError3_))
        d_995_encryptionMaterialsOut_ = (d_996_valueOrError3_).Extract()
        d_997___v3_: tuple
        d_998_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_998_valueOrError4_ = (d_984_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_995_encryptionMaterialsOut_).materials)
        if not(not((d_998_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(247,13): " + _dafny.string_of(d_998_valueOrError4_))
        d_997___v3_ = (d_998_valueOrError4_).Extract()
        d_999_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_999_edk_ = (((d_995_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1000_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1001_valueOrError5_: Wrappers.Result = None
        d_1001_valueOrError5_ = (d_984_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_992_algorithmSuiteId_, d_991_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1001_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(251,33): " + _dafny.string_of(d_1001_valueOrError5_))
        d_1000_decryptionMaterialsIn_ = (d_1001_valueOrError5_).Extract()
        d_1002_fakeEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1002_fakeEdk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((d_999_edk_).keyProviderId, (d_999_edk_).keyProviderInfo, _dafny.Seq([0 for d_1003_i_ in range(len((d_999_edk_).ciphertext))]))
        d_1004_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_1005_valueOrError6_: Wrappers.Result = None
        out397_: Wrappers.Result
        out397_ = (d_989_rawRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1000_decryptionMaterialsIn_, _dafny.Seq([d_1002_fakeEdk_, d_999_edk_])))
        d_1005_valueOrError6_ = out397_
        if not(not((d_1005_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(268,34): " + _dafny.string_of(d_1005_valueOrError6_))
        d_1004_decryptionMaterialsOut_ = (d_1005_valueOrError6_).Extract()
        if not((((d_1004_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_995_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(279,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GenerateKeyPair(keyModulusLength):
        keys: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput = None
        d_1006_crypto_: AtomicPrimitives.AtomicPrimitivesClient
        d_1007_valueOrError0_: Wrappers.Result = None
        out398_: Wrappers.Result
        out398_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_1007_valueOrError0_ = out398_
        if not(not((d_1007_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(286,18): " + _dafny.string_of(d_1007_valueOrError0_))
        d_1006_crypto_ = (d_1007_valueOrError0_).Extract()
        d_1008_valueOrError1_: Wrappers.Result = None
        out399_: Wrappers.Result
        out399_ = (d_1006_crypto_).GenerateRSAKeyPair(AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(keyModulusLength))
        d_1008_valueOrError1_ = out399_
        if not(not((d_1008_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(288,12): " + _dafny.string_of(d_1008_valueOrError1_))
        keys = (d_1008_valueOrError1_).Extract()
        return keys

