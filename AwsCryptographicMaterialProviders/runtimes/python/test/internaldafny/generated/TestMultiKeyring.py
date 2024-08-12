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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
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

# Module: TestMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getInputEncryptionMaterials(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_826_mpl_: MaterialProviders.MaterialProvidersClient
        d_827_valueOrError0_: Wrappers.Result = None
        out301_: Wrappers.Result
        out301_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_827_valueOrError0_ = out301_
        if not(not((d_827_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(18,15): " + _dafny.string_of(d_827_valueOrError0_))
        d_826_mpl_ = (d_827_valueOrError0_).Extract()
        d_828_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_828_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_829_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_830_valueOrError1_: Wrappers.Result = None
        d_830_valueOrError1_ = (d_826_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_828_algorithmSuiteId_, encryptionContext, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_830_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(21,33): " + _dafny.string_of(d_830_valueOrError1_))
        d_829_encryptionMaterialsIn_ = (d_830_valueOrError1_).Extract()
        res = d_829_encryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def getInputDecryptionMaterials(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        d_831_mpl_: MaterialProviders.MaterialProvidersClient
        d_832_valueOrError0_: Wrappers.Result = None
        out302_: Wrappers.Result
        out302_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_832_valueOrError0_ = out302_
        if not(not((d_832_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(35,15): " + _dafny.string_of(d_832_valueOrError0_))
        d_831_mpl_ = (d_832_valueOrError0_).Extract()
        d_833_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_833_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_834_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_835_valueOrError1_: Wrappers.Result = None
        d_835_valueOrError1_ = (d_831_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_833_algorithmSuiteId_, encryptionContext, _dafny.Seq([])))
        if not(not((d_835_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(38,33): " + _dafny.string_of(d_835_valueOrError1_))
        d_834_decryptionMaterialsIn_ = (d_835_valueOrError1_).Extract()
        res = d_834_decryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def TestHappyCase():
        d_836_mpl_: MaterialProviders.MaterialProvidersClient
        d_837_valueOrError0_: Wrappers.Result = None
        out303_: Wrappers.Result
        out303_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_837_valueOrError0_ = out303_
        if not(not((d_837_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(51,15): " + _dafny.string_of(d_837_valueOrError0_))
        d_836_mpl_ = (d_837_valueOrError0_).Extract()
        d_838_encryptionContext_: _dafny.Map
        out304_: _dafny.Map
        out304_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_838_encryptionContext_ = out304_
        d_839_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out305_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out305_ = default__.getInputEncryptionMaterials(d_838_encryptionContext_)
        d_839_encryptionMaterials_ = out305_
        d_840_decryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out306_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out306_ = default__.getInputDecryptionMaterials(d_838_encryptionContext_)
        d_840_decryptionMaterials_ = out306_
        d_841_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out307_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out307_ = default__.setupRawAesKeyring(d_838_encryptionContext_)
        d_841_rawAESKeyring_ = out307_
        d_842_expectedEncryptionMaterials_: Wrappers.Result
        out308_: Wrappers.Result
        out308_ = (d_841_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_839_encryptionMaterials_))
        d_842_expectedEncryptionMaterials_ = out308_
        if not((d_842_expectedEncryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_843_expectedPlaintextDataKey_: Wrappers.Option
        d_843_expectedPlaintextDataKey_ = (((d_842_expectedEncryptionMaterials_).value).materials).plaintextDataKey
        if not((d_843_expectedPlaintextDataKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_844_staticKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out309_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out309_ = default__.SetupStaticKeyring(Wrappers.Option_Some(((d_842_expectedEncryptionMaterials_).value).materials), Wrappers.Option_None())
        d_844_staticKeyring_ = out309_
        d_845_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_846_valueOrError1_: Wrappers.Result = None
        out310_: Wrappers.Result
        out310_ = (d_836_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_844_staticKeyring_), _dafny.Seq([d_841_rawAESKeyring_])))
        d_846_valueOrError1_ = out310_
        if not(not((d_846_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(69,24): " + _dafny.string_of(d_846_valueOrError1_))
        d_845_multiKeyring_ = (d_846_valueOrError1_).Extract()
        d_847_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_848_valueOrError2_: Wrappers.Result = None
        out311_: Wrappers.Result
        out311_ = (d_845_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_839_encryptionMaterials_))
        d_848_valueOrError2_ = out311_
        if not(not((d_848_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(74,34): " + _dafny.string_of(d_848_valueOrError2_))
        d_847_encryptionMaterialsOut_ = (d_848_valueOrError2_).Extract()
        d_849___v0_: tuple
        d_850_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_850_valueOrError3_ = (d_836_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_847_encryptionMaterialsOut_).materials)
        if not(not((d_850_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(76,13): " + _dafny.string_of(d_850_valueOrError3_))
        d_849___v0_ = (d_850_valueOrError3_).Extract()
        if not(((((d_847_encryptionMaterialsOut_).materials).plaintextDataKey).value) == ((d_843_expectedPlaintextDataKey_).value)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_847_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (2)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestChildKeyringFailureEncrypt():
        d_851_mpl_: MaterialProviders.MaterialProvidersClient
        d_852_valueOrError0_: Wrappers.Result = None
        out312_: Wrappers.Result
        out312_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_852_valueOrError0_ = out312_
        if not(not((d_852_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(106,15): " + _dafny.string_of(d_852_valueOrError0_))
        d_851_mpl_ = (d_852_valueOrError0_).Extract()
        d_853_encryptionContext_: _dafny.Map
        out313_: _dafny.Map
        out313_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_853_encryptionContext_ = out313_
        d_854_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out314_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out314_ = default__.setupRawAesKeyring(d_853_encryptionContext_)
        d_854_rawAESKeyring_ = out314_
        d_855_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out315_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out315_ = default__.SetupFailingKeyring()
        d_855_failingKeyring_ = out315_
        d_856_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_857_valueOrError1_: Wrappers.Result = None
        out316_: Wrappers.Result
        out316_ = (d_851_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_854_rawAESKeyring_), _dafny.Seq([d_855_failingKeyring_])))
        d_857_valueOrError1_ = out316_
        if not(not((d_857_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(116,24): " + _dafny.string_of(d_857_valueOrError1_))
        d_856_multiKeyring_ = (d_857_valueOrError1_).Extract()
        d_858_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out317_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out317_ = default__.getInputEncryptionMaterials(d_853_encryptionContext_)
        d_858_encryptionMaterials_ = out317_
        d_859_result_: Wrappers.Result
        out318_: Wrappers.Result
        out318_ = (d_856_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_858_encryptionMaterials_))
        d_859_result_ = out318_
        if not((d_859_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringFails():
        d_860_mpl_: MaterialProviders.MaterialProvidersClient
        d_861_valueOrError0_: Wrappers.Result = None
        out319_: Wrappers.Result
        out319_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_861_valueOrError0_ = out319_
        if not(not((d_861_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(129,15): " + _dafny.string_of(d_861_valueOrError0_))
        d_860_mpl_ = (d_861_valueOrError0_).Extract()
        d_862_encryptionContext_: _dafny.Map
        out320_: _dafny.Map
        out320_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_862_encryptionContext_ = out320_
        d_863_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out321_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out321_ = default__.SetupFailingKeyring()
        d_863_failingKeyring_ = out321_
        d_864_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out322_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out322_ = default__.setupRawAesKeyring(d_862_encryptionContext_)
        d_864_rawAESKeyring_ = out322_
        d_865_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_866_valueOrError1_: Wrappers.Result = None
        out323_: Wrappers.Result
        out323_ = (d_860_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_863_failingKeyring_), _dafny.Seq([d_864_rawAESKeyring_])))
        d_866_valueOrError1_ = out323_
        if not(not((d_866_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(142,24): " + _dafny.string_of(d_866_valueOrError1_))
        d_865_multiKeyring_ = (d_866_valueOrError1_).Extract()
        d_867_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out324_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out324_ = default__.getInputEncryptionMaterials(d_862_encryptionContext_)
        d_867_encryptionMaterials_ = out324_
        d_868_result_: Wrappers.Result
        out325_: Wrappers.Result
        out325_ = (d_865_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_867_encryptionMaterials_))
        d_868_result_ = out325_
        if not((d_868_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringDoesNotReturnPlaintextDataKey():
        d_869_mpl_: MaterialProviders.MaterialProvidersClient
        d_870_valueOrError0_: Wrappers.Result = None
        out326_: Wrappers.Result
        out326_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_870_valueOrError0_ = out326_
        if not(not((d_870_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(155,15): " + _dafny.string_of(d_870_valueOrError0_))
        d_869_mpl_ = (d_870_valueOrError0_).Extract()
        d_871_encryptionContext_: _dafny.Map
        out327_: _dafny.Map
        out327_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_871_encryptionContext_ = out327_
        d_872_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out328_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out328_ = default__.getInputEncryptionMaterials(d_871_encryptionContext_)
        d_872_encryptionMaterials_ = out328_
        d_873_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out329_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out329_ = default__.SetupStaticKeyring(Wrappers.Option_Some(d_872_encryptionMaterials_), Wrappers.Option_None())
        d_873_failingKeyring_ = out329_
        d_874_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_875_valueOrError1_: Wrappers.Result = None
        out330_: Wrappers.Result
        out330_ = (d_869_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_873_failingKeyring_), _dafny.Seq([])))
        d_875_valueOrError1_ = out330_
        if not(not((d_875_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(165,24): " + _dafny.string_of(d_875_valueOrError1_))
        d_874_multiKeyring_ = (d_875_valueOrError1_).Extract()
        d_876_result_: Wrappers.Result
        out331_: Wrappers.Result
        out331_ = (d_874_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_872_encryptionMaterials_))
        d_876_result_ = out331_
        if not((d_876_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorAbleToDecrypt():
        d_877_mpl_: MaterialProviders.MaterialProvidersClient
        d_878_valueOrError0_: Wrappers.Result = None
        out332_: Wrappers.Result
        out332_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_878_valueOrError0_ = out332_
        if not(not((d_878_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(176,15): " + _dafny.string_of(d_878_valueOrError0_))
        d_877_mpl_ = (d_878_valueOrError0_).Extract()
        d_879_encryptionContext_: _dafny.Map
        out333_: _dafny.Map
        out333_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_879_encryptionContext_ = out333_
        d_880_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out334_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out334_ = default__.setupRawAesKeyring(d_879_encryptionContext_)
        d_880_rawAESKeyring_ = out334_
        d_881_inputEncryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out335_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out335_ = default__.getInputEncryptionMaterials(d_879_encryptionContext_)
        d_881_inputEncryptionMaterials_ = out335_
        d_882_encryptionMaterials_: Wrappers.Result
        out336_: Wrappers.Result
        out336_ = (d_880_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_881_inputEncryptionMaterials_))
        d_882_encryptionMaterials_ = out336_
        if not((d_882_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_883_inputDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out337_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out337_ = default__.getInputDecryptionMaterials(d_879_encryptionContext_)
        d_883_inputDecryptionMaterials_ = out337_
        d_884_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out338_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out338_ = default__.SetupFailingKeyring()
        d_884_failingKeyring_ = out338_
        d_885_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_886_valueOrError1_: Wrappers.Result = None
        out339_: Wrappers.Result
        out339_ = (d_877_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_880_rawAESKeyring_), _dafny.Seq([d_884_failingKeyring_])))
        d_886_valueOrError1_ = out339_
        if not(not((d_886_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(196,24): " + _dafny.string_of(d_886_valueOrError1_))
        d_885_multiKeyring_ = (d_886_valueOrError1_).Extract()
        d_887_onDecryptInput_: AwsCryptographyMaterialProvidersTypes.OnDecryptInput
        d_887_onDecryptInput_ = AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_883_inputDecryptionMaterials_, (((d_882_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_888_decryptionMaterials_: Wrappers.Result
        out340_: Wrappers.Result
        out340_ = (d_885_multiKeyring_).OnDecrypt(d_887_onDecryptInput_)
        d_888_decryptionMaterials_ = out340_
        if not((d_888_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_888_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_882_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorUnableToDecrypt():
        d_889_mpl_: MaterialProviders.MaterialProvidersClient
        d_890_valueOrError0_: Wrappers.Result = None
        out341_: Wrappers.Result
        out341_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_890_valueOrError0_ = out341_
        if not(not((d_890_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(212,15): " + _dafny.string_of(d_890_valueOrError0_))
        d_889_mpl_ = (d_890_valueOrError0_).Extract()
        d_891_encryptionContext_: _dafny.Map
        out342_: _dafny.Map
        out342_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_891_encryptionContext_ = out342_
        d_892_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out343_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out343_ = default__.setupRawAesKeyring(d_891_encryptionContext_)
        d_892_rawAESKeyring_ = out343_
        d_893_inputEncryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out344_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out344_ = default__.getInputEncryptionMaterials(d_891_encryptionContext_)
        d_893_inputEncryptionMaterials_ = out344_
        d_894_encryptionMaterials_: Wrappers.Result
        out345_: Wrappers.Result
        out345_ = (d_892_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_893_inputEncryptionMaterials_))
        d_894_encryptionMaterials_ = out345_
        if not((d_894_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(237,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_895_inputDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out346_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out346_ = default__.getInputDecryptionMaterials(d_891_encryptionContext_)
        d_895_inputDecryptionMaterials_ = out346_
        d_896_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out347_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out347_ = default__.SetupFailingKeyring()
        d_896_failingKeyring_ = out347_
        d_897_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_898_valueOrError1_: Wrappers.Result = None
        out348_: Wrappers.Result
        out348_ = (d_889_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_896_failingKeyring_), _dafny.Seq([d_896_failingKeyring_, d_892_rawAESKeyring_, d_896_failingKeyring_])))
        d_898_valueOrError1_ = out348_
        if not(not((d_898_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(245,24): " + _dafny.string_of(d_898_valueOrError1_))
        d_897_multiKeyring_ = (d_898_valueOrError1_).Extract()
        d_899_onDecryptInput_: AwsCryptographyMaterialProvidersTypes.OnDecryptInput
        d_899_onDecryptInput_ = AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_895_inputDecryptionMaterials_, (((d_894_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_900_decryptionMaterials_: Wrappers.Result
        out349_: Wrappers.Result
        out349_ = (d_897_multiKeyring_).OnDecrypt(d_899_onDecryptInput_)
        d_900_decryptionMaterials_ = out349_
        if not((d_900_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_900_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_894_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(266,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCollectFailuresDecrypt():
        d_901_mpl_: MaterialProviders.MaterialProvidersClient
        d_902_valueOrError0_: Wrappers.Result = None
        out350_: Wrappers.Result
        out350_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_902_valueOrError0_ = out350_
        if not(not((d_902_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(272,15): " + _dafny.string_of(d_902_valueOrError0_))
        d_901_mpl_ = (d_902_valueOrError0_).Extract()
        d_903_encryptionContext_: _dafny.Map
        out351_: _dafny.Map
        out351_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_903_encryptionContext_ = out351_
        d_904_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out352_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out352_ = default__.SetupFailingKeyring()
        d_904_failingKeyring_ = out352_
        d_905_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_906_valueOrError1_: Wrappers.Result = None
        out353_: Wrappers.Result
        out353_ = (d_901_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_None(), _dafny.Seq([d_904_failingKeyring_, d_904_failingKeyring_])))
        d_906_valueOrError1_ = out353_
        if not(not((d_906_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(291,24): " + _dafny.string_of(d_906_valueOrError1_))
        d_905_multiKeyring_ = (d_906_valueOrError1_).Extract()
        d_907_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_908_valueOrError2_: Wrappers.Result = None
        d_908_valueOrError2_ = (d_901_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), d_903_encryptionContext_, _dafny.Seq([])))
        if not(not((d_908_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(296,21): " + _dafny.string_of(d_908_valueOrError2_))
        d_907_materials_ = (d_908_valueOrError2_).Extract()
        d_909_result_: Wrappers.Result
        out354_: Wrappers.Result
        out354_ = (d_905_multiKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_907_materials_, _dafny.Seq([])))
        d_909_result_ = out354_
        if not((d_909_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def setupRawAesKeyring(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        d_910_mpl_: MaterialProviders.MaterialProvidersClient
        d_911_valueOrError0_: Wrappers.Result = None
        out355_: Wrappers.Result
        out355_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_911_valueOrError0_ = out355_
        if not(not((d_911_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(313,15): " + _dafny.string_of(d_911_valueOrError0_))
        d_910_mpl_ = (d_911_valueOrError0_).Extract()
        d_912_namespace_: _dafny.Seq
        d_913_name_: _dafny.Seq
        out356_: _dafny.Seq
        out357_: _dafny.Seq
        out356_, out357_ = TestUtils.default__.NamespaceAndName(0)
        d_912_namespace_ = out356_
        d_913_name_ = out357_
        d_914_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_915_valueOrError1_: Wrappers.Result = None
        out358_: Wrappers.Result
        out358_ = (d_910_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_912_namespace_, d_913_name_, _dafny.Seq([0 for d_916_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_915_valueOrError1_ = out358_
        if not(not((d_915_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(316,25): " + _dafny.string_of(d_915_valueOrError1_))
        d_914_rawAESKeyring_ = (d_915_valueOrError1_).Extract()
        res = d_914_rawAESKeyring_
        return res
        return res

    @staticmethod
    def SetupStaticKeyring(encryptionMaterials, decryptionMaterials):
        res: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        nw4_ = StaticKeyring()
        nw4_.ctor__(encryptionMaterials, decryptionMaterials)
        res = nw4_
        return res
        return res

    @staticmethod
    def SetupFailingKeyring():
        res: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        nw5_ = FailingKeyring()
        nw5_.ctor__()
        res = nw5_
        return res
        return res


class StaticKeyring(AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._encryptionMaterials: Wrappers.Option = Wrappers.Option.default()()
        self._decryptionMaterials: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.StaticKeyring"
    def OnDecrypt(self, input):
        out359_: Wrappers.Result
        out359_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out359_

    def OnEncrypt(self, input):
        out360_: Wrappers.Result
        out360_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out360_

    def ctor__(self, encryptionMaterials, decryptionMaterials):
        (self)._encryptionMaterials = encryptionMaterials
        (self)._decryptionMaterials = decryptionMaterials

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).encryptionMaterials).is_Some:
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(((self).encryptionMaterials).value))
            return res
        elif True:
            d_917_exception_: AwsCryptographyMaterialProvidersTypes.Error
            d_917_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_917_exception_)
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).decryptionMaterials).is_Some:
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(((self).decryptionMaterials).value))
            return res
        elif True:
            d_918_exception_: AwsCryptographyMaterialProvidersTypes.Error
            d_918_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_918_exception_)
            return res
        return res

    @property
    def encryptionMaterials(self):
        return self._encryptionMaterials
    @property
    def decryptionMaterials(self):
        return self._decryptionMaterials

class FailingKeyring(AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.FailingKeyring"
    def OnDecrypt(self, input):
        out361_: Wrappers.Result
        out361_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out361_

    def OnEncrypt(self, input):
        out362_: Wrappers.Result
        out362_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out362_

    def ctor__(self):
        pass
        pass

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_919_exception_: AwsCryptographyMaterialProvidersTypes.Error
        d_919_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_919_exception_)
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_920_exception_: AwsCryptographyMaterialProvidersTypes.Error
        d_920_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_920_exception_)
        return res
        return res

