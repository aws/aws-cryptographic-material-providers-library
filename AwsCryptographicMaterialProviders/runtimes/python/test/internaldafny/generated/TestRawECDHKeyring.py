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

# Module: TestRawECDHKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestRawEcdhDiscoveryOnEncryptFailure():
        d_499_mpl_: MaterialProviders.MaterialProvidersClient
        d_500_valueOrError0_: Wrappers.Result = None
        out173_: Wrappers.Result
        out173_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_500_valueOrError0_ = out173_
        if not(not((d_500_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(30,15): " + _dafny.string_of(d_500_valueOrError0_))
        d_499_mpl_ = (d_500_valueOrError0_).Extract()
        d_501_primitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_502_valueOrError1_: Wrappers.Result = None
        out174_: Wrappers.Result
        out174_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_502_valueOrError1_ = out174_
        if not(not((d_502_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(31,22): " + _dafny.string_of(d_502_valueOrError1_))
        d_501_primitives_ = (d_502_valueOrError1_).Extract()
        d_503_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_504_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out175_: Wrappers.Result
        out175_ = (d_501_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_504_valueOrError2_ = out175_
        if not(not((d_504_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(33,19): " + _dafny.string_of(d_504_valueOrError2_))
        d_503_keypair_ = (d_504_valueOrError2_).Extract()
        d_505_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_506_valueOrError3_: Wrappers.Result = None
        out176_: Wrappers.Result
        out176_ = (d_499_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_PublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.PublicKeyDiscoveryInput_PublicKeyDiscoveryInput(((d_503_keypair_).privateKey).pem)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_506_valueOrError3_ = out176_
        if not(not((d_506_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(39,19): " + _dafny.string_of(d_506_valueOrError3_))
        d_505_keyring_ = (d_506_valueOrError3_).Extract()
        d_507_encryptionContext_: _dafny.Map
        out177_: _dafny.Map
        out177_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_507_encryptionContext_ = out177_
        d_508_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_508_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_509_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_510_valueOrError4_: Wrappers.Result = None
        d_510_valueOrError4_ = (d_499_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_508_algorithmSuiteId_, d_507_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_510_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(51,33): " + _dafny.string_of(d_510_valueOrError4_))
        d_509_encryptionMaterialsIn_ = (d_510_valueOrError4_).Extract()
        d_511_encryptionMaterialsOut_: Wrappers.Result
        out178_: Wrappers.Result
        out178_ = (d_505_keyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_509_encryptionMaterialsIn_))
        d_511_encryptionMaterialsOut_ = out178_
        if not((d_511_encryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_511_encryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_512_expectedErrorMessage_: _dafny.Seq
        d_512_expectedErrorMessage_ = ErrorMessages.default__.RAW__ECDH__DISCOVERY__ENCRYPT__ERROR
        if not((((d_511_encryptionMaterialsOut_).error).message) == (d_512_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhEphemeralOnDecryptFailure():
        d_513_mpl_: MaterialProviders.MaterialProvidersClient
        d_514_valueOrError0_: Wrappers.Result = None
        out179_: Wrappers.Result
        out179_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_514_valueOrError0_ = out179_
        if not(not((d_514_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(73,15): " + _dafny.string_of(d_514_valueOrError0_))
        d_513_mpl_ = (d_514_valueOrError0_).Extract()
        d_515_primitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_516_valueOrError1_: Wrappers.Result = None
        out180_: Wrappers.Result
        out180_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_516_valueOrError1_ = out180_
        if not(not((d_516_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(74,22): " + _dafny.string_of(d_516_valueOrError1_))
        d_515_primitives_ = (d_516_valueOrError1_).Extract()
        d_517_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_518_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out181_: Wrappers.Result
        out181_ = (d_515_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_518_valueOrError2_ = out181_
        if not(not((d_518_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(76,19): " + _dafny.string_of(d_518_valueOrError2_))
        d_517_keypair_ = (d_518_valueOrError2_).Extract()
        d_519_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_520_valueOrError3_: Wrappers.Result = None
        out182_: Wrappers.Result
        out182_ = (d_513_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(((d_517_keypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_520_valueOrError3_ = out182_
        if not(not((d_520_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(82,19): " + _dafny.string_of(d_520_valueOrError3_))
        d_519_keyring_ = (d_520_valueOrError3_).Extract()
        d_521_encryptionContext_: _dafny.Map
        out183_: _dafny.Map
        out183_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_521_encryptionContext_ = out183_
        d_522_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_522_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_523_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_524_valueOrError4_: Wrappers.Result = None
        d_524_valueOrError4_ = (d_513_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_522_algorithmSuiteId_, _dafny.Map({}), _dafny.Seq([])))
        if not(not((d_524_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(96,33): " + _dafny.string_of(d_524_valueOrError4_))
        d_523_decryptionMaterialsIn_ = (d_524_valueOrError4_).Extract()
        d_525_decryptionMaterialsOutRes_: Wrappers.Result
        out184_: Wrappers.Result
        out184_ = (d_519_keyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_523_decryptionMaterialsIn_, _dafny.Seq([])))
        d_525_decryptionMaterialsOutRes_ = out184_
        if not((d_525_decryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_525_decryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_525_decryptionMaterialsOutRes_).error).message) == (ErrorMessages.default__.RAW__ECDH__EPHEMERAL__DECRYPT__ERROR)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure():
        d_526_mpl_: MaterialProviders.MaterialProvidersClient
        d_527_valueOrError0_: Wrappers.Result = None
        out185_: Wrappers.Result
        out185_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_527_valueOrError0_ = out185_
        if not(not((d_527_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(117,15): " + _dafny.string_of(d_527_valueOrError0_))
        d_526_mpl_ = (d_527_valueOrError0_).Extract()
        d_528_primitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_529_valueOrError1_: Wrappers.Result = None
        out186_: Wrappers.Result
        out186_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_529_valueOrError1_ = out186_
        if not(not((d_529_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(118,22): " + _dafny.string_of(d_529_valueOrError1_))
        d_528_primitives_ = (d_529_valueOrError1_).Extract()
        d_530_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_531_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out187_: Wrappers.Result
        out187_ = (d_528_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_531_valueOrError2_ = out187_
        if not(not((d_531_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(120,19): " + _dafny.string_of(d_531_valueOrError2_))
        d_530_keypair_ = (d_531_valueOrError2_).Extract()
        d_532_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_533_valueOrError3_: Wrappers.Result = None
        out188_: Wrappers.Result
        out188_ = (d_526_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(((d_530_keypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_533_valueOrError3_ = out188_
        if not(not((d_533_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(126,19): " + _dafny.string_of(d_533_valueOrError3_))
        d_532_keyring_ = (d_533_valueOrError3_).Extract()
        d_534_encryptionContext_: _dafny.Map
        out189_: _dafny.Map
        out189_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_534_encryptionContext_ = out189_
        d_535_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_535_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_536_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_537_valueOrError4_: Wrappers.Result = None
        d_537_valueOrError4_ = (d_526_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_535_algorithmSuiteId_, d_534_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_537_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(140,33): " + _dafny.string_of(d_537_valueOrError4_))
        d_536_encryptionMaterialsIn_ = (d_537_valueOrError4_).Extract()
        d_538_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_539_valueOrError5_: Wrappers.Result = None
        out190_: Wrappers.Result
        out190_ = (d_532_keyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_536_encryptionMaterialsIn_))
        d_539_valueOrError5_ = out190_
        if not(not((d_539_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(150,34): " + _dafny.string_of(d_539_valueOrError5_))
        d_538_encryptionMaterialsOut_ = (d_539_valueOrError5_).Extract()
        d_540___v0_: tuple
        d_541_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_541_valueOrError6_ = (d_526_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_538_encryptionMaterialsOut_).materials)
        if not(not((d_541_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(154,13): " + _dafny.string_of(d_541_valueOrError6_))
        d_540___v0_ = (d_541_valueOrError6_).Extract()
        if not((len(((d_538_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(156,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_542_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_542_edk_ = (((d_538_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_543_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_544_valueOrError7_: Wrappers.Result = None
        d_544_valueOrError7_ = (d_526_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_535_algorithmSuiteId_, d_534_encryptionContext_, _dafny.Seq([])))
        if not(not((d_544_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(159,33): " + _dafny.string_of(d_544_valueOrError7_))
        d_543_decryptionMaterialsIn_ = (d_544_valueOrError7_).Extract()
        d_545_decryptionMaterialsOut_: Wrappers.Result
        out191_: Wrappers.Result
        out191_ = (d_532_keyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_543_decryptionMaterialsIn_, _dafny.Seq([d_542_edk_])))
        d_545_decryptionMaterialsOut_ = out191_
        if not((d_545_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(173,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_545_decryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(174,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_546_expectedErrorMessage_: _dafny.Seq
        d_546_expectedErrorMessage_ = ErrorMessages.default__.RAW__ECDH__EPHEMERAL__DECRYPT__ERROR
        if not((((d_545_decryptionMaterialsOut_).error).message) == (d_546_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhKeyringStaticSuccess():
        d_547_mpl_: MaterialProviders.MaterialProvidersClient
        d_548_valueOrError0_: Wrappers.Result = None
        out192_: Wrappers.Result
        out192_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_548_valueOrError0_ = out192_
        if not(not((d_548_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(181,15): " + _dafny.string_of(d_548_valueOrError0_))
        d_547_mpl_ = (d_548_valueOrError0_).Extract()
        d_549_primitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_550_valueOrError1_: Wrappers.Result = None
        out193_: Wrappers.Result
        out193_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_550_valueOrError1_ = out193_
        if not(not((d_550_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(182,22): " + _dafny.string_of(d_550_valueOrError1_))
        d_549_primitives_ = (d_550_valueOrError1_).Extract()
        d_551_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_552_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out194_: Wrappers.Result
        out194_ = (d_549_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_552_valueOrError2_ = out194_
        if not(not((d_552_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(184,25): " + _dafny.string_of(d_552_valueOrError2_))
        d_551_senderKeypair_ = (d_552_valueOrError2_).Extract()
        d_553_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_554_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out195_: Wrappers.Result
        out195_ = (d_549_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_554_valueOrError3_ = out195_
        if not(not((d_554_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(190,28): " + _dafny.string_of(d_554_valueOrError3_))
        d_553_recipientKeypair_ = (d_554_valueOrError3_).Extract()
        d_555_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_556_valueOrError4_: Wrappers.Result = None
        out196_: Wrappers.Result
        out196_ = (d_547_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_551_senderKeypair_).privateKey).pem, ((d_553_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_556_valueOrError4_ = out196_
        if not(not((d_556_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(196,19): " + _dafny.string_of(d_556_valueOrError4_))
        d_555_keyring_ = (d_556_valueOrError4_).Extract()
        d_557_encryptionContext_: _dafny.Map
        out197_: _dafny.Map
        out197_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_557_encryptionContext_ = out197_
        d_558_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_558_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_559_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_560_valueOrError5_: Wrappers.Result = None
        d_560_valueOrError5_ = (d_547_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_558_algorithmSuiteId_, d_557_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_560_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(211,33): " + _dafny.string_of(d_560_valueOrError5_))
        d_559_encryptionMaterialsIn_ = (d_560_valueOrError5_).Extract()
        d_561_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_562_valueOrError6_: Wrappers.Result = None
        out198_: Wrappers.Result
        out198_ = (d_555_keyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_559_encryptionMaterialsIn_))
        d_562_valueOrError6_ = out198_
        if not(not((d_562_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(221,34): " + _dafny.string_of(d_562_valueOrError6_))
        d_561_encryptionMaterialsOut_ = (d_562_valueOrError6_).Extract()
        d_563___v1_: tuple
        d_564_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_564_valueOrError7_ = (d_547_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_561_encryptionMaterialsOut_).materials)
        if not(not((d_564_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(225,13): " + _dafny.string_of(d_564_valueOrError7_))
        d_563___v1_ = (d_564_valueOrError7_).Extract()
        if not((len(((d_561_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(227,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_565_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_565_edk_ = (((d_561_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_566_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_567_valueOrError8_: Wrappers.Result = None
        d_567_valueOrError8_ = (d_547_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_558_algorithmSuiteId_, d_557_encryptionContext_, _dafny.Seq([])))
        if not(not((d_567_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(230,33): " + _dafny.string_of(d_567_valueOrError8_))
        d_566_decryptionMaterialsIn_ = (d_567_valueOrError8_).Extract()
        d_568_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_569_valueOrError9_: Wrappers.Result = None
        out199_: Wrappers.Result
        out199_ = (d_555_keyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_566_decryptionMaterialsIn_, _dafny.Seq([d_565_edk_])))
        d_569_valueOrError9_ = out199_
        if not(not((d_569_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(237,34): " + _dafny.string_of(d_569_valueOrError9_))
        d_568_decryptionMaterialsOut_ = (d_569_valueOrError9_).Extract()
        if not((((d_561_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_568_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(244,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestTwoRawEcdhKeyringStaticSuccess():
        d_570_mpl_: MaterialProviders.MaterialProvidersClient
        d_571_valueOrError0_: Wrappers.Result = None
        out200_: Wrappers.Result
        out200_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_571_valueOrError0_ = out200_
        if not(not((d_571_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(250,15): " + _dafny.string_of(d_571_valueOrError0_))
        d_570_mpl_ = (d_571_valueOrError0_).Extract()
        d_572_primitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_573_valueOrError1_: Wrappers.Result = None
        out201_: Wrappers.Result
        out201_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_573_valueOrError1_ = out201_
        if not(not((d_573_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(251,22): " + _dafny.string_of(d_573_valueOrError1_))
        d_572_primitives_ = (d_573_valueOrError1_).Extract()
        d_574_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_575_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out202_: Wrappers.Result
        out202_ = (d_572_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_575_valueOrError2_ = out202_
        if not(not((d_575_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(253,25): " + _dafny.string_of(d_575_valueOrError2_))
        d_574_senderKeypair_ = (d_575_valueOrError2_).Extract()
        d_576_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_577_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out203_: Wrappers.Result
        out203_ = (d_572_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_577_valueOrError3_ = out203_
        if not(not((d_577_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(259,28): " + _dafny.string_of(d_577_valueOrError3_))
        d_576_recipientKeypair_ = (d_577_valueOrError3_).Extract()
        d_578_senderKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_579_valueOrError4_: Wrappers.Result = None
        out204_: Wrappers.Result
        out204_ = (d_570_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_574_senderKeypair_).privateKey).pem, ((d_576_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_579_valueOrError4_ = out204_
        if not(not((d_579_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(265,25): " + _dafny.string_of(d_579_valueOrError4_))
        d_578_senderKeyring_ = (d_579_valueOrError4_).Extract()
        d_580_recipientKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_581_valueOrError5_: Wrappers.Result = None
        out205_: Wrappers.Result
        out205_ = (d_570_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_576_recipientKeypair_).privateKey).pem, ((d_574_senderKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_581_valueOrError5_ = out205_
        if not(not((d_581_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(277,28): " + _dafny.string_of(d_581_valueOrError5_))
        d_580_recipientKeyring_ = (d_581_valueOrError5_).Extract()
        d_582_encryptionContext_: _dafny.Map
        out206_: _dafny.Map
        out206_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_582_encryptionContext_ = out206_
        d_583_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_583_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_584_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_585_valueOrError6_: Wrappers.Result = None
        d_585_valueOrError6_ = (d_570_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_583_algorithmSuiteId_, d_582_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_585_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(292,33): " + _dafny.string_of(d_585_valueOrError6_))
        d_584_encryptionMaterialsIn_ = (d_585_valueOrError6_).Extract()
        d_586_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_587_valueOrError7_: Wrappers.Result = None
        out207_: Wrappers.Result
        out207_ = (d_578_senderKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_584_encryptionMaterialsIn_))
        d_587_valueOrError7_ = out207_
        if not(not((d_587_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(302,34): " + _dafny.string_of(d_587_valueOrError7_))
        d_586_encryptionMaterialsOut_ = (d_587_valueOrError7_).Extract()
        d_588___v2_: tuple
        d_589_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_589_valueOrError8_ = (d_570_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_586_encryptionMaterialsOut_).materials)
        if not(not((d_589_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(306,13): " + _dafny.string_of(d_589_valueOrError8_))
        d_588___v2_ = (d_589_valueOrError8_).Extract()
        if not((len(((d_586_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(308,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_590_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_590_edk_ = (((d_586_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_591_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_592_valueOrError9_: Wrappers.Result = None
        d_592_valueOrError9_ = (d_570_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_583_algorithmSuiteId_, d_582_encryptionContext_, _dafny.Seq([])))
        if not(not((d_592_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(311,33): " + _dafny.string_of(d_592_valueOrError9_))
        d_591_decryptionMaterialsIn_ = (d_592_valueOrError9_).Extract()
        d_593_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_594_valueOrError10_: Wrappers.Result = None
        out208_: Wrappers.Result
        out208_ = (d_580_recipientKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_591_decryptionMaterialsIn_, _dafny.Seq([d_590_edk_])))
        d_594_valueOrError10_ = out208_
        if not(not((d_594_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(318,34): " + _dafny.string_of(d_594_valueOrError10_))
        d_593_decryptionMaterialsOut_ = (d_594_valueOrError10_).Extract()
        if not((((d_586_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_593_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(325,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestTwoEcdhKeyringStaticSuccess():
        d_595_mpl_: MaterialProviders.MaterialProvidersClient
        d_596_valueOrError0_: Wrappers.Result = None
        out209_: Wrappers.Result
        out209_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_596_valueOrError0_ = out209_
        if not(not((d_596_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(331,15): " + _dafny.string_of(d_596_valueOrError0_))
        d_595_mpl_ = (d_596_valueOrError0_).Extract()
        d_597_primitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_598_valueOrError1_: Wrappers.Result = None
        out210_: Wrappers.Result
        out210_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_598_valueOrError1_ = out210_
        if not(not((d_598_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(332,22): " + _dafny.string_of(d_598_valueOrError1_))
        d_597_primitives_ = (d_598_valueOrError1_).Extract()
        d_599_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_600_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out211_: Wrappers.Result
        out211_ = (d_597_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_600_valueOrError2_ = out211_
        if not(not((d_600_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(334,25): " + _dafny.string_of(d_600_valueOrError2_))
        d_599_senderKeypair_ = (d_600_valueOrError2_).Extract()
        d_601_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_602_valueOrError3_: Wrappers.Result = None
        out212_: Wrappers.Result
        out212_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_602_valueOrError3_ = out212_
        if not(not((d_602_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(340,21): " + _dafny.string_of(d_602_valueOrError3_))
        d_601_kmsClient_ = (d_602_valueOrError3_).Extract()
        d_603_publicKeyResponse_: Wrappers.Result
        out213_: Wrappers.Result
        out213_ = (d_601_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(TestUtils.default__.KMS__ECC__256__KEY__ARN__R, Wrappers.Option_None()))
        d_603_publicKeyResponse_ = out213_
        if not((d_603_publicKeyResponse_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(347,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs0_ = (d_603_publicKeyResponse_).value
        d_604___v3_ = let_tmp_rhs0_.KeyId
        d_605_PublicKey_ = let_tmp_rhs0_.PublicKey
        d_606___v4_ = let_tmp_rhs0_.CustomerMasterKeySpec
        d_607___v5_ = let_tmp_rhs0_.KeySpec
        d_608___v6_ = let_tmp_rhs0_.KeyUsage
        d_609___v7_ = let_tmp_rhs0_.EncryptionAlgorithms
        d_610___v8_ = let_tmp_rhs0_.SigningAlgorithms
        d_611___v9_ = let_tmp_rhs0_.KeyAgreementAlgorithms
        if not((d_605_PublicKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(350,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_612_senderKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_613_valueOrError4_: Wrappers.Result = None
        out214_: Wrappers.Result
        out214_ = (d_595_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_599_senderKeypair_).privateKey).pem, (d_605_PublicKey_).value)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_613_valueOrError4_ = out214_
        if not(not((d_613_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(352,25): " + _dafny.string_of(d_613_valueOrError4_))
        d_612_senderKeyring_ = (d_613_valueOrError4_).Extract()
        d_614_recipientKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_615_valueOrError5_: Wrappers.Result = None
        out215_: Wrappers.Result
        out215_ = (d_595_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__R, Wrappers.Option_None(), ((d_599_senderKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), d_601_kmsClient_, Wrappers.Option_None()))
        d_615_valueOrError5_ = out215_
        if not(not((d_615_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(364,35): " + _dafny.string_of(d_615_valueOrError5_))
        d_614_recipientKmsEcdhKeyring_ = (d_615_valueOrError5_).Extract()
        d_616_encryptionContext_: _dafny.Map
        out216_: _dafny.Map
        out216_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_616_encryptionContext_ = out216_
        d_617_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_617_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_618_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_619_valueOrError6_: Wrappers.Result = None
        d_619_valueOrError6_ = (d_595_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_617_algorithmSuiteId_, d_616_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_619_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(381,33): " + _dafny.string_of(d_619_valueOrError6_))
        d_618_encryptionMaterialsIn_ = (d_619_valueOrError6_).Extract()
        d_620_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_621_valueOrError7_: Wrappers.Result = None
        out217_: Wrappers.Result
        out217_ = (d_612_senderKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_618_encryptionMaterialsIn_))
        d_621_valueOrError7_ = out217_
        if not(not((d_621_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(391,34): " + _dafny.string_of(d_621_valueOrError7_))
        d_620_encryptionMaterialsOut_ = (d_621_valueOrError7_).Extract()
        d_622___v10_: tuple
        d_623_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_623_valueOrError8_ = (d_595_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_620_encryptionMaterialsOut_).materials)
        if not(not((d_623_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(395,13): " + _dafny.string_of(d_623_valueOrError8_))
        d_622___v10_ = (d_623_valueOrError8_).Extract()
        if not((len(((d_620_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(397,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_624_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_624_edk_ = (((d_620_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_625_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_626_valueOrError9_: Wrappers.Result = None
        d_626_valueOrError9_ = (d_595_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_617_algorithmSuiteId_, d_616_encryptionContext_, _dafny.Seq([])))
        if not(not((d_626_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(400,33): " + _dafny.string_of(d_626_valueOrError9_))
        d_625_decryptionMaterialsIn_ = (d_626_valueOrError9_).Extract()
        d_627_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_628_valueOrError10_: Wrappers.Result = None
        out218_: Wrappers.Result
        out218_ = (d_614_recipientKmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_625_decryptionMaterialsIn_, _dafny.Seq([d_624_edk_])))
        d_628_valueOrError10_ = out218_
        if not(not((d_628_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(407,34): " + _dafny.string_of(d_628_valueOrError10_))
        d_627_decryptionMaterialsOut_ = (d_628_valueOrError10_).Extract()
        if not((((d_620_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_627_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(414,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite():
        d_629_mpl_: MaterialProviders.MaterialProvidersClient
        d_630_valueOrError0_: Wrappers.Result = None
        out219_: Wrappers.Result
        out219_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_630_valueOrError0_ = out219_
        if not(not((d_630_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(420,15): " + _dafny.string_of(d_630_valueOrError0_))
        d_629_mpl_ = (d_630_valueOrError0_).Extract()
        d_631_primitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_632_valueOrError1_: Wrappers.Result = None
        out220_: Wrappers.Result
        out220_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_632_valueOrError1_ = out220_
        if not(not((d_632_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(421,22): " + _dafny.string_of(d_632_valueOrError1_))
        d_631_primitives_ = (d_632_valueOrError1_).Extract()
        d_633_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_634_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out221_: Wrappers.Result
        out221_ = (d_631_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_634_valueOrError2_ = out221_
        if not(not((d_634_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(423,25): " + _dafny.string_of(d_634_valueOrError2_))
        d_633_senderKeypair_ = (d_634_valueOrError2_).Extract()
        d_635_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_636_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out222_: Wrappers.Result
        out222_ = (d_631_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_636_valueOrError3_ = out222_
        if not(not((d_636_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(429,28): " + _dafny.string_of(d_636_valueOrError3_))
        d_635_recipientKeypair_ = (d_636_valueOrError3_).Extract()
        d_637_senderKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_638_valueOrError4_: Wrappers.Result = None
        out223_: Wrappers.Result
        out223_ = (d_629_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_633_senderKeypair_).privateKey).pem, ((d_635_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_638_valueOrError4_ = out223_
        if not(not((d_638_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(435,25): " + _dafny.string_of(d_638_valueOrError4_))
        d_637_senderKeyring_ = (d_638_valueOrError4_).Extract()
        d_639_recipientKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_640_valueOrError5_: Wrappers.Result = None
        out224_: Wrappers.Result
        out224_ = (d_629_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_635_recipientKeypair_).privateKey).pem, ((d_633_senderKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_640_valueOrError5_ = out224_
        if not(not((d_640_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(447,28): " + _dafny.string_of(d_640_valueOrError5_))
        d_639_recipientKeyring_ = (d_640_valueOrError5_).Extract()
        d_641_encryptionContext_: _dafny.Map
        out225_: _dafny.Map
        out225_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_641_encryptionContext_ = out225_
        d_642_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out226_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out226_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_642_materials_ = out226_
        d_643_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_644_valueOrError6_: Wrappers.Result = None
        out227_: Wrappers.Result
        out227_ = (d_637_senderKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_642_materials_))
        d_644_valueOrError6_ = out227_
        if not(not((d_644_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(463,34): " + _dafny.string_of(d_644_valueOrError6_))
        d_643_encryptionMaterialsOut_ = (d_644_valueOrError6_).Extract()
        d_645___v11_: tuple
        d_646_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_646_valueOrError7_ = (d_629_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_643_encryptionMaterialsOut_).materials)
        if not(not((d_646_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(467,13): " + _dafny.string_of(d_646_valueOrError7_))
        d_645___v11_ = (d_646_valueOrError7_).Extract()
        if not((len(((d_643_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(469,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_647_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_647_edk_ = (((d_643_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_648_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_649_valueOrError8_: Wrappers.Result = None
        d_649_valueOrError8_ = (d_629_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(default__.TEST__DBE__ALG__SUITE__ID, d_641_encryptionContext_, _dafny.Seq([])))
        if not(not((d_649_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(472,33): " + _dafny.string_of(d_649_valueOrError8_))
        d_648_decryptionMaterialsIn_ = (d_649_valueOrError8_).Extract()
        d_650_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_651_valueOrError9_: Wrappers.Result = None
        out228_: Wrappers.Result
        out228_ = (d_639_recipientKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_648_decryptionMaterialsIn_, _dafny.Seq([d_647_edk_])))
        d_651_valueOrError9_ = out228_
        if not(not((d_651_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(479,34): " + _dafny.string_of(d_651_valueOrError9_))
        d_650_decryptionMaterialsOut_ = (d_651_valueOrError9_).Extract()
        if not((((d_643_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_650_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(486,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionFailure():
        d_652_mpl_: MaterialProviders.MaterialProvidersClient
        d_653_valueOrError0_: Wrappers.Result = None
        out229_: Wrappers.Result
        out229_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_653_valueOrError0_ = out229_
        if not(not((d_653_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(492,15): " + _dafny.string_of(d_653_valueOrError0_))
        d_652_mpl_ = (d_653_valueOrError0_).Extract()
        d_654_senderPrivateKey_: _dafny.Seq
        d_655_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_655_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE)
        if not(not((d_655_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(494,28): " + _dafny.string_of(d_655_valueOrError1_))
        d_654_senderPrivateKey_ = (d_655_valueOrError1_).Extract()
        d_656_recipientPrivateKey_: _dafny.Seq
        d_657_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_657_valueOrError2_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE__R)
        if not(not((d_657_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(495,31): " + _dafny.string_of(d_657_valueOrError2_))
        d_656_recipientPrivateKey_ = (d_657_valueOrError2_).Extract()
        d_658_recipientPublicKey_: _dafny.Seq
        d_659_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_659_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_659_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(496,30): " + _dafny.string_of(d_659_valueOrError3_))
        d_658_recipientPublicKey_ = (d_659_valueOrError3_).Extract()
        d_660_rawEcdhKeyring_: Wrappers.Result
        out230_: Wrappers.Result
        out230_ = (d_652_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_654_senderPrivateKey_, d_658_recipientPublicKey_)), default__.P384))
        d_660_rawEcdhKeyring_ = out230_
        if not((d_660_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(509,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionCombinationsFailure():
        d_661_mpl_: MaterialProviders.MaterialProvidersClient
        d_662_valueOrError0_: Wrappers.Result = None
        out231_: Wrappers.Result
        out231_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_662_valueOrError0_ = out231_
        if not(not((d_662_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(514,15): " + _dafny.string_of(d_662_valueOrError0_))
        d_661_mpl_ = (d_662_valueOrError0_).Extract()
        d_663_senderPrivateKey256_: _dafny.Seq
        d_664_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_664_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE)
        if not(not((d_664_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(516,31): " + _dafny.string_of(d_664_valueOrError1_))
        d_663_senderPrivateKey256_ = (d_664_valueOrError1_).Extract()
        d_665_recipientPrivateKey256_: _dafny.Seq
        d_666_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_666_valueOrError2_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE__R)
        if not(not((d_666_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(517,34): " + _dafny.string_of(d_666_valueOrError2_))
        d_665_recipientPrivateKey256_ = (d_666_valueOrError2_).Extract()
        d_667_recipientPublicKey256_: _dafny.Seq
        d_668_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_668_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_668_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(518,33): " + _dafny.string_of(d_668_valueOrError3_))
        d_667_recipientPublicKey256_ = (d_668_valueOrError3_).Extract()
        d_669_senderPrivateKey384_: _dafny.Seq
        d_670_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_670_valueOrError4_ = UTF8.default__.Encode(TestUtils.default__.ECC__P384__PRIVATE)
        if not(not((d_670_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(520,31): " + _dafny.string_of(d_670_valueOrError4_))
        d_669_senderPrivateKey384_ = (d_670_valueOrError4_).Extract()
        d_671_recipientPrivateKey384_: _dafny.Seq
        d_672_valueOrError5_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_672_valueOrError5_ = UTF8.default__.Encode(TestUtils.default__.ECC__P384__PRIVATE__R)
        if not(not((d_672_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(521,34): " + _dafny.string_of(d_672_valueOrError5_))
        d_671_recipientPrivateKey384_ = (d_672_valueOrError5_).Extract()
        d_673_recipientPublicKey384_: _dafny.Seq
        d_674_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_674_valueOrError6_ = Base64.default__.Decode(TestUtils.default__.ECC__P384__PUBLIC__R)
        if not(not((d_674_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(522,33): " + _dafny.string_of(d_674_valueOrError6_))
        d_673_recipientPublicKey384_ = (d_674_valueOrError6_).Extract()
        d_675_senderPrivateKey521_: _dafny.Seq
        d_676_valueOrError7_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_676_valueOrError7_ = UTF8.default__.Encode(TestUtils.default__.ECC__P521__PRIVATE)
        if not(not((d_676_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(524,31): " + _dafny.string_of(d_676_valueOrError7_))
        d_675_senderPrivateKey521_ = (d_676_valueOrError7_).Extract()
        d_677_recipientPrivateKey521_: _dafny.Seq
        d_678_valueOrError8_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_678_valueOrError8_ = UTF8.default__.Encode(TestUtils.default__.ECC__P521__PRIVATE__R)
        if not(not((d_678_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(525,34): " + _dafny.string_of(d_678_valueOrError8_))
        d_677_recipientPrivateKey521_ = (d_678_valueOrError8_).Extract()
        d_679_recipientPublicKey521_: _dafny.Seq
        d_680_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_680_valueOrError9_ = Base64.default__.Decode(TestUtils.default__.ECC__P521__PUBLIC__R)
        if not(not((d_680_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(526,33): " + _dafny.string_of(d_680_valueOrError9_))
        d_679_recipientPublicKey521_ = (d_680_valueOrError9_).Extract()
        d_681_rawEcdhKeyring_: Wrappers.Result
        out232_: Wrappers.Result
        out232_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_663_senderPrivateKey256_, d_667_recipientPublicKey256_)), default__.P384))
        d_681_rawEcdhKeyring_ = out232_
        if not((d_681_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(542,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out233_: Wrappers.Result
        out233_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_663_senderPrivateKey256_, d_667_recipientPublicKey256_)), default__.P521))
        d_681_rawEcdhKeyring_ = out233_
        if not((d_681_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(555,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out234_: Wrappers.Result
        out234_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_669_senderPrivateKey384_, d_673_recipientPublicKey384_)), default__.P256))
        d_681_rawEcdhKeyring_ = out234_
        if not((d_681_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(569,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out235_: Wrappers.Result
        out235_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_669_senderPrivateKey384_, d_673_recipientPublicKey384_)), default__.P521))
        d_681_rawEcdhKeyring_ = out235_
        if not((d_681_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(582,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out236_: Wrappers.Result
        out236_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_675_senderPrivateKey521_, d_679_recipientPublicKey521_)), default__.P256))
        d_681_rawEcdhKeyring_ = out236_
        if not((d_681_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(596,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out237_: Wrappers.Result
        out237_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_675_senderPrivateKey521_, d_679_recipientPublicKey521_)), default__.P384))
        d_681_rawEcdhKeyring_ = out237_
        if not((d_681_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(609,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_682_rawEcdhKeyringT2_: Wrappers.Result
        out238_: Wrappers.Result
        out238_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_663_senderPrivateKey256_, d_673_recipientPublicKey384_)), default__.P256))
        d_682_rawEcdhKeyringT2_ = out238_
        if not((d_682_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(623,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out239_: Wrappers.Result
        out239_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_663_senderPrivateKey256_, d_679_recipientPublicKey521_)), default__.P256))
        d_682_rawEcdhKeyringT2_ = out239_
        if not((d_682_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(636,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out240_: Wrappers.Result
        out240_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_669_senderPrivateKey384_, d_667_recipientPublicKey256_)), default__.P384))
        d_682_rawEcdhKeyringT2_ = out240_
        if not((d_682_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(649,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out241_: Wrappers.Result
        out241_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_669_senderPrivateKey384_, d_679_recipientPublicKey521_)), default__.P384))
        d_682_rawEcdhKeyringT2_ = out241_
        if not((d_682_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(662,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out242_: Wrappers.Result
        out242_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_675_senderPrivateKey521_, d_667_recipientPublicKey256_)), default__.P521))
        d_682_rawEcdhKeyringT2_ = out242_
        if not((d_682_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(675,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out243_: Wrappers.Result
        out243_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_675_senderPrivateKey521_, d_673_recipientPublicKey384_)), default__.P521))
        d_682_rawEcdhKeyringT2_ = out243_
        if not((d_682_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(688,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_683_rawEcdhKeyringT3_: Wrappers.Result
        out244_: Wrappers.Result
        out244_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_669_senderPrivateKey384_, d_667_recipientPublicKey256_)), default__.P256))
        d_683_rawEcdhKeyringT3_ = out244_
        if not((d_683_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(703,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out245_: Wrappers.Result
        out245_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_675_senderPrivateKey521_, d_667_recipientPublicKey256_)), default__.P256))
        d_683_rawEcdhKeyringT3_ = out245_
        if not((d_683_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(716,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out246_: Wrappers.Result
        out246_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_663_senderPrivateKey256_, d_673_recipientPublicKey384_)), default__.P384))
        d_683_rawEcdhKeyringT3_ = out246_
        if not((d_683_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(729,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out247_: Wrappers.Result
        out247_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_675_senderPrivateKey521_, d_673_recipientPublicKey384_)), default__.P384))
        d_683_rawEcdhKeyringT3_ = out247_
        if not((d_683_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(742,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out248_: Wrappers.Result
        out248_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_663_senderPrivateKey256_, d_679_recipientPublicKey521_)), default__.P521))
        d_683_rawEcdhKeyringT3_ = out248_
        if not((d_683_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(755,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out249_: Wrappers.Result
        out249_ = (d_661_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_669_senderPrivateKey384_, d_679_recipientPublicKey521_)), default__.P521))
        d_683_rawEcdhKeyringT3_ = out249_
        if not((d_683_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(768,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GetTestMaterials(suiteId):
        out: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_684_mpl_: MaterialProviders.MaterialProvidersClient
        d_685_valueOrError0_: Wrappers.Result = None
        out250_: Wrappers.Result
        out250_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_685_valueOrError0_ = out250_
        if not(not((d_685_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(773,15): " + _dafny.string_of(d_685_valueOrError0_))
        d_684_mpl_ = (d_685_valueOrError0_).Extract()
        d_686_encryptionContext_: _dafny.Map
        out251_: _dafny.Map
        out251_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_686_encryptionContext_ = out251_
        d_687_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_687_suite_ = AlgorithmSuites.default__.GetSuite(suiteId)
        d_688_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_689_valueOrError1_: Wrappers.Result = None
        d_689_valueOrError1_ = (d_684_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(suiteId, d_686_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_689_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(778,33): " + _dafny.string_of(d_689_valueOrError1_))
        d_688_encryptionMaterialsIn_ = (d_689_valueOrError1_).Extract()
        out = d_688_encryptionMaterialsIn_
        return out
        return out

    @_dafny.classproperty
    def P256(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()
    @_dafny.classproperty
    def TEST__DBE__ALG__SUITE__ID(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384())
    @_dafny.classproperty
    def P384(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384()
    @_dafny.classproperty
    def P521(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()
