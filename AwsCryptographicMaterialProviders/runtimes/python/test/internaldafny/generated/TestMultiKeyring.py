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
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestDefaultClientProvider as TestDefaultClientProvider
import TestRawAESKeyring as TestRawAESKeyring

# Module: TestMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getInputEncryptionMaterials(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_389_mpl_: MaterialProviders.MaterialProvidersClient
        d_390_valueOrError0_: Wrappers.Result = None
        out134_: Wrappers.Result
        out134_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_390_valueOrError0_ = out134_
        if not(not((d_390_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(18,15): " + _dafny.string_of(d_390_valueOrError0_))
        d_389_mpl_ = (d_390_valueOrError0_).Extract()
        d_391_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_391_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_392_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_393_valueOrError1_: Wrappers.Result = None
        d_393_valueOrError1_ = (d_389_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_391_algorithmSuiteId_, encryptionContext, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_393_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(21,33): " + _dafny.string_of(d_393_valueOrError1_))
        d_392_encryptionMaterialsIn_ = (d_393_valueOrError1_).Extract()
        res = d_392_encryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def getInputDecryptionMaterials(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        d_394_mpl_: MaterialProviders.MaterialProvidersClient
        d_395_valueOrError0_: Wrappers.Result = None
        out135_: Wrappers.Result
        out135_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_395_valueOrError0_ = out135_
        if not(not((d_395_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(35,15): " + _dafny.string_of(d_395_valueOrError0_))
        d_394_mpl_ = (d_395_valueOrError0_).Extract()
        d_396_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_396_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_397_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_398_valueOrError1_: Wrappers.Result = None
        d_398_valueOrError1_ = (d_394_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_396_algorithmSuiteId_, encryptionContext, _dafny.Seq([])))
        if not(not((d_398_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(38,33): " + _dafny.string_of(d_398_valueOrError1_))
        d_397_decryptionMaterialsIn_ = (d_398_valueOrError1_).Extract()
        res = d_397_decryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def TestHappyCase():
        d_399_mpl_: MaterialProviders.MaterialProvidersClient
        d_400_valueOrError0_: Wrappers.Result = None
        out136_: Wrappers.Result
        out136_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_400_valueOrError0_ = out136_
        if not(not((d_400_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(51,15): " + _dafny.string_of(d_400_valueOrError0_))
        d_399_mpl_ = (d_400_valueOrError0_).Extract()
        d_401_encryptionContext_: _dafny.Map
        out137_: _dafny.Map
        out137_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_401_encryptionContext_ = out137_
        d_402_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out138_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out138_ = default__.getInputEncryptionMaterials(d_401_encryptionContext_)
        d_402_encryptionMaterials_ = out138_
        d_403_decryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out139_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out139_ = default__.getInputDecryptionMaterials(d_401_encryptionContext_)
        d_403_decryptionMaterials_ = out139_
        d_404_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out140_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out140_ = default__.setupRawAesKeyring(d_401_encryptionContext_)
        d_404_rawAESKeyring_ = out140_
        d_405_expectedEncryptionMaterials_: Wrappers.Result
        out141_: Wrappers.Result
        out141_ = (d_404_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_402_encryptionMaterials_))
        d_405_expectedEncryptionMaterials_ = out141_
        if not((d_405_expectedEncryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_406_expectedPlaintextDataKey_: Wrappers.Option
        d_406_expectedPlaintextDataKey_ = (((d_405_expectedEncryptionMaterials_).value).materials).plaintextDataKey
        if not((d_406_expectedPlaintextDataKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_407_staticKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out142_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out142_ = default__.SetupStaticKeyring(Wrappers.Option_Some(((d_405_expectedEncryptionMaterials_).value).materials), Wrappers.Option_None())
        d_407_staticKeyring_ = out142_
        d_408_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_409_valueOrError1_: Wrappers.Result = None
        out143_: Wrappers.Result
        out143_ = (d_399_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_407_staticKeyring_), _dafny.Seq([d_404_rawAESKeyring_])))
        d_409_valueOrError1_ = out143_
        if not(not((d_409_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(69,24): " + _dafny.string_of(d_409_valueOrError1_))
        d_408_multiKeyring_ = (d_409_valueOrError1_).Extract()
        d_410_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_411_valueOrError2_: Wrappers.Result = None
        out144_: Wrappers.Result
        out144_ = (d_408_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_402_encryptionMaterials_))
        d_411_valueOrError2_ = out144_
        if not(not((d_411_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(74,34): " + _dafny.string_of(d_411_valueOrError2_))
        d_410_encryptionMaterialsOut_ = (d_411_valueOrError2_).Extract()
        d_412___v0_: tuple
        d_413_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_413_valueOrError3_ = (d_399_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_410_encryptionMaterialsOut_).materials)
        if not(not((d_413_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(76,13): " + _dafny.string_of(d_413_valueOrError3_))
        d_412___v0_ = (d_413_valueOrError3_).Extract()
        if not(((((d_410_encryptionMaterialsOut_).materials).plaintextDataKey).value) == ((d_406_expectedPlaintextDataKey_).value)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_410_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (2)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestChildKeyringFailureEncrypt():
        d_414_mpl_: MaterialProviders.MaterialProvidersClient
        d_415_valueOrError0_: Wrappers.Result = None
        out145_: Wrappers.Result
        out145_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_415_valueOrError0_ = out145_
        if not(not((d_415_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(106,15): " + _dafny.string_of(d_415_valueOrError0_))
        d_414_mpl_ = (d_415_valueOrError0_).Extract()
        d_416_encryptionContext_: _dafny.Map
        out146_: _dafny.Map
        out146_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_416_encryptionContext_ = out146_
        d_417_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out147_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out147_ = default__.setupRawAesKeyring(d_416_encryptionContext_)
        d_417_rawAESKeyring_ = out147_
        d_418_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out148_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out148_ = default__.SetupFailingKeyring()
        d_418_failingKeyring_ = out148_
        d_419_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_420_valueOrError1_: Wrappers.Result = None
        out149_: Wrappers.Result
        out149_ = (d_414_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_417_rawAESKeyring_), _dafny.Seq([d_418_failingKeyring_])))
        d_420_valueOrError1_ = out149_
        if not(not((d_420_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(116,24): " + _dafny.string_of(d_420_valueOrError1_))
        d_419_multiKeyring_ = (d_420_valueOrError1_).Extract()
        d_421_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out150_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out150_ = default__.getInputEncryptionMaterials(d_416_encryptionContext_)
        d_421_encryptionMaterials_ = out150_
        d_422_result_: Wrappers.Result
        out151_: Wrappers.Result
        out151_ = (d_419_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_421_encryptionMaterials_))
        d_422_result_ = out151_
        if not((d_422_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringFails():
        d_423_mpl_: MaterialProviders.MaterialProvidersClient
        d_424_valueOrError0_: Wrappers.Result = None
        out152_: Wrappers.Result
        out152_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_424_valueOrError0_ = out152_
        if not(not((d_424_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(129,15): " + _dafny.string_of(d_424_valueOrError0_))
        d_423_mpl_ = (d_424_valueOrError0_).Extract()
        d_425_encryptionContext_: _dafny.Map
        out153_: _dafny.Map
        out153_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_425_encryptionContext_ = out153_
        d_426_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out154_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out154_ = default__.SetupFailingKeyring()
        d_426_failingKeyring_ = out154_
        d_427_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out155_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out155_ = default__.setupRawAesKeyring(d_425_encryptionContext_)
        d_427_rawAESKeyring_ = out155_
        d_428_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_429_valueOrError1_: Wrappers.Result = None
        out156_: Wrappers.Result
        out156_ = (d_423_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_426_failingKeyring_), _dafny.Seq([d_427_rawAESKeyring_])))
        d_429_valueOrError1_ = out156_
        if not(not((d_429_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(142,24): " + _dafny.string_of(d_429_valueOrError1_))
        d_428_multiKeyring_ = (d_429_valueOrError1_).Extract()
        d_430_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out157_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out157_ = default__.getInputEncryptionMaterials(d_425_encryptionContext_)
        d_430_encryptionMaterials_ = out157_
        d_431_result_: Wrappers.Result
        out158_: Wrappers.Result
        out158_ = (d_428_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_430_encryptionMaterials_))
        d_431_result_ = out158_
        if not((d_431_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringDoesNotReturnPlaintextDataKey():
        d_432_mpl_: MaterialProviders.MaterialProvidersClient
        d_433_valueOrError0_: Wrappers.Result = None
        out159_: Wrappers.Result
        out159_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_433_valueOrError0_ = out159_
        if not(not((d_433_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(155,15): " + _dafny.string_of(d_433_valueOrError0_))
        d_432_mpl_ = (d_433_valueOrError0_).Extract()
        d_434_encryptionContext_: _dafny.Map
        out160_: _dafny.Map
        out160_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_434_encryptionContext_ = out160_
        d_435_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out161_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out161_ = default__.getInputEncryptionMaterials(d_434_encryptionContext_)
        d_435_encryptionMaterials_ = out161_
        d_436_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out162_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out162_ = default__.SetupStaticKeyring(Wrappers.Option_Some(d_435_encryptionMaterials_), Wrappers.Option_None())
        d_436_failingKeyring_ = out162_
        d_437_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_438_valueOrError1_: Wrappers.Result = None
        out163_: Wrappers.Result
        out163_ = (d_432_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_436_failingKeyring_), _dafny.Seq([])))
        d_438_valueOrError1_ = out163_
        if not(not((d_438_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(165,24): " + _dafny.string_of(d_438_valueOrError1_))
        d_437_multiKeyring_ = (d_438_valueOrError1_).Extract()
        d_439_result_: Wrappers.Result
        out164_: Wrappers.Result
        out164_ = (d_437_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_435_encryptionMaterials_))
        d_439_result_ = out164_
        if not((d_439_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorAbleToDecrypt():
        d_440_mpl_: MaterialProviders.MaterialProvidersClient
        d_441_valueOrError0_: Wrappers.Result = None
        out165_: Wrappers.Result
        out165_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_441_valueOrError0_ = out165_
        if not(not((d_441_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(176,15): " + _dafny.string_of(d_441_valueOrError0_))
        d_440_mpl_ = (d_441_valueOrError0_).Extract()
        d_442_encryptionContext_: _dafny.Map
        out166_: _dafny.Map
        out166_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_442_encryptionContext_ = out166_
        d_443_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out167_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out167_ = default__.setupRawAesKeyring(d_442_encryptionContext_)
        d_443_rawAESKeyring_ = out167_
        d_444_inputEncryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out168_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out168_ = default__.getInputEncryptionMaterials(d_442_encryptionContext_)
        d_444_inputEncryptionMaterials_ = out168_
        d_445_encryptionMaterials_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = (d_443_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_444_inputEncryptionMaterials_))
        d_445_encryptionMaterials_ = out169_
        if not((d_445_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_446_inputDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out170_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out170_ = default__.getInputDecryptionMaterials(d_442_encryptionContext_)
        d_446_inputDecryptionMaterials_ = out170_
        d_447_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out171_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out171_ = default__.SetupFailingKeyring()
        d_447_failingKeyring_ = out171_
        d_448_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_449_valueOrError1_: Wrappers.Result = None
        out172_: Wrappers.Result
        out172_ = (d_440_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_443_rawAESKeyring_), _dafny.Seq([d_447_failingKeyring_])))
        d_449_valueOrError1_ = out172_
        if not(not((d_449_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(196,24): " + _dafny.string_of(d_449_valueOrError1_))
        d_448_multiKeyring_ = (d_449_valueOrError1_).Extract()
        d_450_onDecryptInput_: AwsCryptographyMaterialProvidersTypes.OnDecryptInput
        d_450_onDecryptInput_ = AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_446_inputDecryptionMaterials_, (((d_445_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_451_decryptionMaterials_: Wrappers.Result
        out173_: Wrappers.Result
        out173_ = (d_448_multiKeyring_).OnDecrypt(d_450_onDecryptInput_)
        d_451_decryptionMaterials_ = out173_
        if not((d_451_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_451_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_445_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorUnableToDecrypt():
        d_452_mpl_: MaterialProviders.MaterialProvidersClient
        d_453_valueOrError0_: Wrappers.Result = None
        out174_: Wrappers.Result
        out174_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_453_valueOrError0_ = out174_
        if not(not((d_453_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(212,15): " + _dafny.string_of(d_453_valueOrError0_))
        d_452_mpl_ = (d_453_valueOrError0_).Extract()
        d_454_encryptionContext_: _dafny.Map
        out175_: _dafny.Map
        out175_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_454_encryptionContext_ = out175_
        d_455_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out176_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out176_ = default__.setupRawAesKeyring(d_454_encryptionContext_)
        d_455_rawAESKeyring_ = out176_
        d_456_inputEncryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out177_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out177_ = default__.getInputEncryptionMaterials(d_454_encryptionContext_)
        d_456_inputEncryptionMaterials_ = out177_
        d_457_encryptionMaterials_: Wrappers.Result
        out178_: Wrappers.Result
        out178_ = (d_455_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_456_inputEncryptionMaterials_))
        d_457_encryptionMaterials_ = out178_
        if not((d_457_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(237,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_458_inputDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out179_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out179_ = default__.getInputDecryptionMaterials(d_454_encryptionContext_)
        d_458_inputDecryptionMaterials_ = out179_
        d_459_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out180_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out180_ = default__.SetupFailingKeyring()
        d_459_failingKeyring_ = out180_
        d_460_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_461_valueOrError1_: Wrappers.Result = None
        out181_: Wrappers.Result
        out181_ = (d_452_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_459_failingKeyring_), _dafny.Seq([d_459_failingKeyring_, d_455_rawAESKeyring_, d_459_failingKeyring_])))
        d_461_valueOrError1_ = out181_
        if not(not((d_461_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(245,24): " + _dafny.string_of(d_461_valueOrError1_))
        d_460_multiKeyring_ = (d_461_valueOrError1_).Extract()
        d_462_onDecryptInput_: AwsCryptographyMaterialProvidersTypes.OnDecryptInput
        d_462_onDecryptInput_ = AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_458_inputDecryptionMaterials_, (((d_457_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_463_decryptionMaterials_: Wrappers.Result
        out182_: Wrappers.Result
        out182_ = (d_460_multiKeyring_).OnDecrypt(d_462_onDecryptInput_)
        d_463_decryptionMaterials_ = out182_
        if not((d_463_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_463_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_457_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(266,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCollectFailuresDecrypt():
        d_464_mpl_: MaterialProviders.MaterialProvidersClient
        d_465_valueOrError0_: Wrappers.Result = None
        out183_: Wrappers.Result
        out183_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_465_valueOrError0_ = out183_
        if not(not((d_465_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(272,15): " + _dafny.string_of(d_465_valueOrError0_))
        d_464_mpl_ = (d_465_valueOrError0_).Extract()
        d_466_encryptionContext_: _dafny.Map
        out184_: _dafny.Map
        out184_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_466_encryptionContext_ = out184_
        d_467_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out185_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out185_ = default__.SetupFailingKeyring()
        d_467_failingKeyring_ = out185_
        d_468_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_469_valueOrError1_: Wrappers.Result = None
        out186_: Wrappers.Result
        out186_ = (d_464_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_None(), _dafny.Seq([d_467_failingKeyring_, d_467_failingKeyring_])))
        d_469_valueOrError1_ = out186_
        if not(not((d_469_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(291,24): " + _dafny.string_of(d_469_valueOrError1_))
        d_468_multiKeyring_ = (d_469_valueOrError1_).Extract()
        d_470_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_471_valueOrError2_: Wrappers.Result = None
        d_471_valueOrError2_ = (d_464_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), d_466_encryptionContext_, _dafny.Seq([])))
        if not(not((d_471_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(296,21): " + _dafny.string_of(d_471_valueOrError2_))
        d_470_materials_ = (d_471_valueOrError2_).Extract()
        d_472_result_: Wrappers.Result
        out187_: Wrappers.Result
        out187_ = (d_468_multiKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_470_materials_, _dafny.Seq([])))
        d_472_result_ = out187_
        if not((d_472_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def setupRawAesKeyring(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        d_473_mpl_: MaterialProviders.MaterialProvidersClient
        d_474_valueOrError0_: Wrappers.Result = None
        out188_: Wrappers.Result
        out188_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_474_valueOrError0_ = out188_
        if not(not((d_474_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(313,15): " + _dafny.string_of(d_474_valueOrError0_))
        d_473_mpl_ = (d_474_valueOrError0_).Extract()
        d_475_namespace_: _dafny.Seq
        d_476_name_: _dafny.Seq
        out189_: _dafny.Seq
        out190_: _dafny.Seq
        out189_, out190_ = TestUtils.default__.NamespaceAndName(0)
        d_475_namespace_ = out189_
        d_476_name_ = out190_
        d_477_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_478_valueOrError1_: Wrappers.Result = None
        out191_: Wrappers.Result
        out191_ = (d_473_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_475_namespace_, d_476_name_, _dafny.Seq([0 for d_479_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_478_valueOrError1_ = out191_
        if not(not((d_478_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(316,25): " + _dafny.string_of(d_478_valueOrError1_))
        d_477_rawAESKeyring_ = (d_478_valueOrError1_).Extract()
        res = d_477_rawAESKeyring_
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
        out192_: Wrappers.Result
        out192_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out192_

    def OnEncrypt(self, input):
        out193_: Wrappers.Result
        out193_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out193_

    def ctor__(self, encryptionMaterials, decryptionMaterials):
        (self)._encryptionMaterials = encryptionMaterials
        (self)._decryptionMaterials = decryptionMaterials

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).encryptionMaterials).is_Some:
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(((self).encryptionMaterials).value))
            return res
        elif True:
            d_480_exception_: AwsCryptographyMaterialProvidersTypes.Error
            d_480_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_480_exception_)
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).decryptionMaterials).is_Some:
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(((self).decryptionMaterials).value))
            return res
        elif True:
            d_481_exception_: AwsCryptographyMaterialProvidersTypes.Error
            d_481_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_481_exception_)
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
        out194_: Wrappers.Result
        out194_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out194_

    def OnEncrypt(self, input):
        out195_: Wrappers.Result
        out195_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out195_

    def ctor__(self):
        pass
        pass

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_482_exception_: AwsCryptographyMaterialProvidersTypes.Error
        d_482_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_482_exception_)
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_483_exception_: AwsCryptographyMaterialProvidersTypes.Error
        d_483_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_483_exception_)
        return res
        return res

