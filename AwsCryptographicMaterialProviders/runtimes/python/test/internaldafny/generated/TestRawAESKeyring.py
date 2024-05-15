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

# Module: TestRawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptGenerateDataKey():
        d_253_mpl_: MaterialProviders.MaterialProvidersClient
        d_254_valueOrError0_: Wrappers.Result = None
        out85_: Wrappers.Result
        out85_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_254_valueOrError0_ = out85_
        if not(not((d_254_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(21,15): " + _dafny.string_of(d_254_valueOrError0_))
        d_253_mpl_ = (d_254_valueOrError0_).Extract()
        d_255_namespace_: _dafny.Seq
        d_256_name_: _dafny.Seq
        out86_: _dafny.Seq
        out87_: _dafny.Seq
        out86_, out87_ = TestUtils.default__.NamespaceAndName(0)
        d_255_namespace_ = out86_
        d_256_name_ = out87_
        d_257_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_258_valueOrError1_: Wrappers.Result = None
        out88_: Wrappers.Result
        out88_ = (d_253_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_255_namespace_, d_256_name_, _dafny.Seq([0 for d_259_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_258_valueOrError1_ = out88_
        if not(not((d_258_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(24,25): " + _dafny.string_of(d_258_valueOrError1_))
        d_257_rawAESKeyring_ = (d_258_valueOrError1_).Extract()
        d_260_encryptionContext_: _dafny.Map
        out89_: _dafny.Map
        out89_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_260_encryptionContext_ = out89_
        d_261_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_261_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_262_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_263_valueOrError2_: Wrappers.Result = None
        d_263_valueOrError2_ = (d_253_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_261_algorithmSuiteId_, d_260_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_263_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(33,33): " + _dafny.string_of(d_263_valueOrError2_))
        d_262_encryptionMaterialsIn_ = (d_263_valueOrError2_).Extract()
        d_264_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_265_valueOrError3_: Wrappers.Result = None
        out90_: Wrappers.Result
        out90_ = (d_257_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_262_encryptionMaterialsIn_))
        d_265_valueOrError3_ = out90_
        if not(not((d_265_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(43,34): " + _dafny.string_of(d_265_valueOrError3_))
        d_264_encryptionMaterialsOut_ = (d_265_valueOrError3_).Extract()
        d_266___v0_: tuple
        d_267_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_267_valueOrError4_ = (d_253_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_264_encryptionMaterialsOut_).materials)
        if not(not((d_267_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(58,13): " + _dafny.string_of(d_267_valueOrError4_))
        d_266___v0_ = (d_267_valueOrError4_).Extract()
        if not((len(((d_264_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_268_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_268_edk_ = (((d_264_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_269_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_270_valueOrError5_: Wrappers.Result = None
        d_270_valueOrError5_ = (d_253_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_261_algorithmSuiteId_, d_260_encryptionContext_, _dafny.Seq([])))
        if not(not((d_270_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(69,33): " + _dafny.string_of(d_270_valueOrError5_))
        d_269_decryptionMaterialsIn_ = (d_270_valueOrError5_).Extract()
        d_271_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_272_valueOrError6_: Wrappers.Result = None
        out91_: Wrappers.Result
        out91_ = (d_257_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_269_decryptionMaterialsIn_, _dafny.Seq([d_268_edk_])))
        d_272_valueOrError6_ = out91_
        if not(not((d_272_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(76,34): " + _dafny.string_of(d_272_valueOrError6_))
        d_271_decryptionMaterialsOut_ = (d_272_valueOrError6_).Extract()
        if not((((d_264_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_264_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_273_mpl_: MaterialProviders.MaterialProvidersClient
        d_274_valueOrError0_: Wrappers.Result = None
        out92_: Wrappers.Result
        out92_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_274_valueOrError0_ = out92_
        if not(not((d_274_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(94,15): " + _dafny.string_of(d_274_valueOrError0_))
        d_273_mpl_ = (d_274_valueOrError0_).Extract()
        d_275_namespace_: _dafny.Seq
        d_276_name_: _dafny.Seq
        out93_: _dafny.Seq
        out94_: _dafny.Seq
        out93_, out94_ = TestUtils.default__.NamespaceAndName(0)
        d_275_namespace_ = out93_
        d_276_name_ = out94_
        d_277_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_278_valueOrError1_: Wrappers.Result = None
        out95_: Wrappers.Result
        out95_ = (d_273_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_275_namespace_, d_276_name_, _dafny.Seq([0 for d_279_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_278_valueOrError1_ = out95_
        if not(not((d_278_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(97,25): " + _dafny.string_of(d_278_valueOrError1_))
        d_277_rawAESKeyring_ = (d_278_valueOrError1_).Extract()
        d_280_encryptionContext_: _dafny.Map
        out96_: _dafny.Map
        out96_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_280_encryptionContext_ = out96_
        d_281_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_281_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_282_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_283_valueOrError2_: Wrappers.Result = None
        d_283_valueOrError2_ = (d_273_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_281_algorithmSuiteId_, d_280_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_283_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(106,33): " + _dafny.string_of(d_283_valueOrError2_))
        d_282_encryptionMaterialsIn_ = (d_283_valueOrError2_).Extract()
        d_284_pdk_: _dafny.Seq
        d_284_pdk_ = _dafny.Seq([0 for d_285_i_ in range(32)])
        d_286_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_287_valueOrError3_: Wrappers.Result = None
        pat_let_tv0_ = d_284_pdk_
        out97_: Wrappers.Result
        def iife4_(_pat_let1_0):
            def iife5_(d_288_dt__update__tmp_h0_):
                def iife6_(_pat_let2_0):
                    def iife7_(d_289_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_288_dt__update__tmp_h0_).algorithmSuite, (d_288_dt__update__tmp_h0_).encryptionContext, (d_288_dt__update__tmp_h0_).encryptedDataKeys, (d_288_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_289_dt__update_hplaintextDataKey_h0_, (d_288_dt__update__tmp_h0_).signingKey, (d_288_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife7_(_pat_let2_0)
                return iife6_(Wrappers.Option_Some(pat_let_tv0_))
            return iife5_(_pat_let1_0)
        out97_ = (d_277_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(iife4_(d_282_encryptionMaterialsIn_)))
        d_287_valueOrError3_ = out97_
        if not(not((d_287_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(121,34): " + _dafny.string_of(d_287_valueOrError3_))
        d_286_encryptionMaterialsOut_ = (d_287_valueOrError3_).Extract()
        d_290___v1_: tuple
        d_291_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_291_valueOrError4_ = (d_273_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_286_encryptionMaterialsOut_).materials)
        if not(not((d_291_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(125,13): " + _dafny.string_of(d_291_valueOrError4_))
        d_290___v1_ = (d_291_valueOrError4_).Extract()
        d_292_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_292_edk_ = (((d_286_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_293_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_294_valueOrError5_: Wrappers.Result = None
        d_294_valueOrError5_ = (d_273_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_281_algorithmSuiteId_, d_280_encryptionContext_, _dafny.Seq([])))
        if not(not((d_294_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(129,33): " + _dafny.string_of(d_294_valueOrError5_))
        d_293_decryptionMaterialsIn_ = (d_294_valueOrError5_).Extract()
        d_295_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_296_valueOrError6_: Wrappers.Result = None
        out98_: Wrappers.Result
        out98_ = (d_277_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_293_decryptionMaterialsIn_, _dafny.Seq([d_292_edk_])))
        d_296_valueOrError6_ = out98_
        if not(not((d_296_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(137,34): " + _dafny.string_of(d_296_valueOrError6_))
        d_295_decryptionMaterialsOut_ = (d_296_valueOrError6_).Extract()
        if not((((d_295_decryptionMaterialsOut_).materials).plaintextDataKey) == (Wrappers.Option_Some(d_284_pdk_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_297_mpl_: MaterialProviders.MaterialProvidersClient
        d_298_valueOrError0_: Wrappers.Result = None
        out99_: Wrappers.Result
        out99_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_298_valueOrError0_ = out99_
        if not(not((d_298_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(155,15): " + _dafny.string_of(d_298_valueOrError0_))
        d_297_mpl_ = (d_298_valueOrError0_).Extract()
        d_299_namespace_: _dafny.Seq
        d_300_name_: _dafny.Seq
        out100_: _dafny.Seq
        out101_: _dafny.Seq
        out100_, out101_ = TestUtils.default__.NamespaceAndName(0)
        d_299_namespace_ = out100_
        d_300_name_ = out101_
        d_301_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_302_valueOrError1_: Wrappers.Result = None
        out102_: Wrappers.Result
        out102_ = (d_297_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_299_namespace_, d_300_name_, _dafny.Seq([0 for d_303_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_302_valueOrError1_ = out102_
        if not(not((d_302_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(158,25): " + _dafny.string_of(d_302_valueOrError1_))
        d_301_rawAESKeyring_ = (d_302_valueOrError1_).Extract()
        d_304_mismatchedAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_305_valueOrError2_: Wrappers.Result = None
        out103_: Wrappers.Result
        out103_ = (d_297_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_299_namespace_, _dafny.Seq("mismatched"), _dafny.Seq([1 for d_306_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_305_valueOrError2_ = out103_
        if not(not((d_305_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(165,32): " + _dafny.string_of(d_305_valueOrError2_))
        d_304_mismatchedAESKeyring_ = (d_305_valueOrError2_).Extract()
        d_307_encryptionContext_: _dafny.Map
        out104_: _dafny.Map
        out104_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_307_encryptionContext_ = out104_
        d_308_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_308_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_309_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_310_valueOrError3_: Wrappers.Result = None
        d_310_valueOrError3_ = (d_297_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_308_algorithmSuiteId_, d_307_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_310_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(175,33): " + _dafny.string_of(d_310_valueOrError3_))
        d_309_encryptionMaterialsIn_ = (d_310_valueOrError3_).Extract()
        d_311_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_312_valueOrError4_: Wrappers.Result = None
        out105_: Wrappers.Result
        out105_ = (d_301_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_309_encryptionMaterialsIn_))
        d_312_valueOrError4_ = out105_
        if not(not((d_312_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(185,34): " + _dafny.string_of(d_312_valueOrError4_))
        d_311_encryptionMaterialsOut_ = (d_312_valueOrError4_).Extract()
        d_313___v2_: tuple
        d_314_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_314_valueOrError5_ = (d_297_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_311_encryptionMaterialsOut_).materials)
        if not(not((d_314_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(189,13): " + _dafny.string_of(d_314_valueOrError5_))
        d_313___v2_ = (d_314_valueOrError5_).Extract()
        d_315_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_315_edk_ = (((d_311_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_316_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_317_valueOrError6_: Wrappers.Result = None
        d_317_valueOrError6_ = (d_297_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_308_algorithmSuiteId_, d_307_encryptionContext_, _dafny.Seq([])))
        if not(not((d_317_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(193,33): " + _dafny.string_of(d_317_valueOrError6_))
        d_316_decryptionMaterialsIn_ = (d_317_valueOrError6_).Extract()
        d_318_decryptionMaterialsOut_: Wrappers.Result
        out106_: Wrappers.Result
        out106_ = (d_304_mismatchedAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_316_decryptionMaterialsIn_, _dafny.Seq([d_315_edk_])))
        d_318_decryptionMaterialsOut_ = out106_
        if not((d_318_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_319_mpl_: MaterialProviders.MaterialProvidersClient
        d_320_valueOrError0_: Wrappers.Result = None
        out107_: Wrappers.Result
        out107_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_320_valueOrError0_ = out107_
        if not(not((d_320_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(212,15): " + _dafny.string_of(d_320_valueOrError0_))
        d_319_mpl_ = (d_320_valueOrError0_).Extract()
        d_321_namespace_: _dafny.Seq
        d_322_name_: _dafny.Seq
        out108_: _dafny.Seq
        out109_: _dafny.Seq
        out108_, out109_ = TestUtils.default__.NamespaceAndName(0)
        d_321_namespace_ = out108_
        d_322_name_ = out109_
        d_323_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_324_valueOrError1_: Wrappers.Result = None
        out110_: Wrappers.Result
        out110_ = (d_319_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_321_namespace_, d_322_name_, _dafny.Seq([0 for d_325_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_324_valueOrError1_ = out110_
        if not(not((d_324_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,25): " + _dafny.string_of(d_324_valueOrError1_))
        d_323_rawAESKeyring_ = (d_324_valueOrError1_).Extract()
        d_326_encryptionContext_: _dafny.Map
        out111_: _dafny.Map
        out111_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_326_encryptionContext_ = out111_
        d_327_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_327_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_328_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_329_valueOrError2_: Wrappers.Result = None
        d_329_valueOrError2_ = (d_319_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_327_algorithmSuiteId_, d_326_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_329_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(224,33): " + _dafny.string_of(d_329_valueOrError2_))
        d_328_encryptionMaterialsIn_ = (d_329_valueOrError2_).Extract()
        d_330_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_331_valueOrError3_: Wrappers.Result = None
        out112_: Wrappers.Result
        out112_ = (d_323_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_328_encryptionMaterialsIn_))
        d_331_valueOrError3_ = out112_
        if not(not((d_331_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(234,34): " + _dafny.string_of(d_331_valueOrError3_))
        d_330_encryptionMaterialsOut_ = (d_331_valueOrError3_).Extract()
        d_332___v3_: tuple
        d_333_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_333_valueOrError4_ = (d_319_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_330_encryptionMaterialsOut_).materials)
        if not(not((d_333_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(238,13): " + _dafny.string_of(d_333_valueOrError4_))
        d_332___v3_ = (d_333_valueOrError4_).Extract()
        d_334_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_334_edk_ = (((d_330_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_335_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_336_valueOrError5_: Wrappers.Result = None
        d_336_valueOrError5_ = (d_319_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_327_algorithmSuiteId_, d_326_encryptionContext_, _dafny.Seq([])))
        if not(not((d_336_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(242,33): " + _dafny.string_of(d_336_valueOrError5_))
        d_335_decryptionMaterialsIn_ = (d_336_valueOrError5_).Extract()
        d_337_fakeEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_337_fakeEdk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((d_334_edk_).keyProviderId, (d_334_edk_).keyProviderInfo, _dafny.Seq([0 for d_338_i_ in range(len((d_334_edk_).ciphertext))]))
        d_339_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_340_valueOrError6_: Wrappers.Result = None
        out113_: Wrappers.Result
        out113_ = (d_323_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_335_decryptionMaterialsIn_, _dafny.Seq([d_337_fakeEdk_, d_334_edk_])))
        d_340_valueOrError6_ = out113_
        if not(not((d_340_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(255,34): " + _dafny.string_of(d_340_valueOrError6_))
        d_339_decryptionMaterialsOut_ = (d_340_valueOrError6_).Extract()
        if not((((d_339_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_330_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(262,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptNoEDKs():
        d_341_mpl_: MaterialProviders.MaterialProvidersClient
        d_342_valueOrError0_: Wrappers.Result = None
        out114_: Wrappers.Result
        out114_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_342_valueOrError0_ = out114_
        if not(not((d_342_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(268,15): " + _dafny.string_of(d_342_valueOrError0_))
        d_341_mpl_ = (d_342_valueOrError0_).Extract()
        d_343_namespace_: _dafny.Seq
        d_344_name_: _dafny.Seq
        out115_: _dafny.Seq
        out116_: _dafny.Seq
        out115_, out116_ = TestUtils.default__.NamespaceAndName(0)
        d_343_namespace_ = out115_
        d_344_name_ = out116_
        d_345_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_346_valueOrError1_: Wrappers.Result = None
        out117_: Wrappers.Result
        out117_ = (d_341_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_343_namespace_, d_344_name_, _dafny.Seq([0 for d_347_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_346_valueOrError1_ = out117_
        if not(not((d_346_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,25): " + _dafny.string_of(d_346_valueOrError1_))
        d_345_rawAESKeyring_ = (d_346_valueOrError1_).Extract()
        d_348_encryptionContext_: _dafny.Map
        out118_: _dafny.Map
        out118_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_348_encryptionContext_ = out118_
        d_349_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_349_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_350_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_351_valueOrError2_: Wrappers.Result = None
        d_351_valueOrError2_ = (d_341_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_349_algorithmSuiteId_, d_348_encryptionContext_, _dafny.Seq([])))
        if not(not((d_351_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(280,33): " + _dafny.string_of(d_351_valueOrError2_))
        d_350_decryptionMaterialsIn_ = (d_351_valueOrError2_).Extract()
        d_352_decryptionMaterialsOut_: Wrappers.Result
        out119_: Wrappers.Result
        out119_ = (d_345_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_350_decryptionMaterialsIn_, _dafny.Seq([])))
        d_352_decryptionMaterialsOut_ = out119_
        if not((d_352_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(293,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptUnserializableEC():
        d_353_mpl_: MaterialProviders.MaterialProvidersClient
        d_354_valueOrError0_: Wrappers.Result = None
        out120_: Wrappers.Result
        out120_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_354_valueOrError0_ = out120_
        if not(not((d_354_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(302,15): " + _dafny.string_of(d_354_valueOrError0_))
        d_353_mpl_ = (d_354_valueOrError0_).Extract()
        d_355_namespace_: _dafny.Seq
        d_356_name_: _dafny.Seq
        out121_: _dafny.Seq
        out122_: _dafny.Seq
        out121_, out122_ = TestUtils.default__.NamespaceAndName(0)
        d_355_namespace_ = out121_
        d_356_name_ = out122_
        d_357_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_358_valueOrError1_: Wrappers.Result = None
        out123_: Wrappers.Result
        out123_ = (d_353_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_355_namespace_, d_356_name_, _dafny.Seq([0 for d_359_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_358_valueOrError1_ = out123_
        if not(not((d_358_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,25): " + _dafny.string_of(d_358_valueOrError1_))
        d_357_rawAESKeyring_ = (d_358_valueOrError1_).Extract()
        d_360_unserializableEncryptionContext_: _dafny.Map
        out124_: _dafny.Map
        out124_ = default__.generateUnserializableEncryptionContext()
        d_360_unserializableEncryptionContext_ = out124_
        d_361_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_361_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_362_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_363_valueOrError2_: Wrappers.Result = None
        d_363_valueOrError2_ = (d_353_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_361_algorithmSuiteId_, d_360_unserializableEncryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_363_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(314,33): " + _dafny.string_of(d_363_valueOrError2_))
        d_362_encryptionMaterialsIn_ = (d_363_valueOrError2_).Extract()
        d_364_encryptionMaterialsOut_: Wrappers.Result
        out125_: Wrappers.Result
        out125_ = (d_357_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_362_encryptionMaterialsIn_))
        d_364_encryptionMaterialsOut_ = out125_
        if not((d_364_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(326,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptUnserializableEC():
        d_365_mpl_: MaterialProviders.MaterialProvidersClient
        d_366_valueOrError0_: Wrappers.Result = None
        out126_: Wrappers.Result
        out126_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_366_valueOrError0_ = out126_
        if not(not((d_366_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(336,15): " + _dafny.string_of(d_366_valueOrError0_))
        d_365_mpl_ = (d_366_valueOrError0_).Extract()
        d_367_namespace_: _dafny.Seq
        d_368_name_: _dafny.Seq
        out127_: _dafny.Seq
        out128_: _dafny.Seq
        out127_, out128_ = TestUtils.default__.NamespaceAndName(0)
        d_367_namespace_ = out127_
        d_368_name_ = out128_
        d_369_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_370_valueOrError1_: Wrappers.Result = None
        out129_: Wrappers.Result
        out129_ = (d_365_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_367_namespace_, d_368_name_, _dafny.Seq([0 for d_371_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_370_valueOrError1_ = out129_
        if not(not((d_370_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,25): " + _dafny.string_of(d_370_valueOrError1_))
        d_369_rawAESKeyring_ = (d_370_valueOrError1_).Extract()
        d_372_encryptionContext_: _dafny.Map
        out130_: _dafny.Map
        out130_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_372_encryptionContext_ = out130_
        d_373_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_373_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_374_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_375_valueOrError2_: Wrappers.Result = None
        d_375_valueOrError2_ = (d_365_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_373_algorithmSuiteId_, d_372_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_375_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(348,33): " + _dafny.string_of(d_375_valueOrError2_))
        d_374_encryptionMaterialsIn_ = (d_375_valueOrError2_).Extract()
        d_376_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_377_valueOrError3_: Wrappers.Result = None
        out131_: Wrappers.Result
        out131_ = (d_369_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_374_encryptionMaterialsIn_))
        d_377_valueOrError3_ = out131_
        if not(not((d_377_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(358,34): " + _dafny.string_of(d_377_valueOrError3_))
        d_376_encryptionMaterialsOut_ = (d_377_valueOrError3_).Extract()
        d_378___v4_: tuple
        d_379_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_379_valueOrError4_ = (d_365_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_376_encryptionMaterialsOut_).materials)
        if not(not((d_379_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(361,13): " + _dafny.string_of(d_379_valueOrError4_))
        d_378___v4_ = (d_379_valueOrError4_).Extract()
        d_380_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_380_edk_ = (((d_376_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_381_unserializableEncryptionContext_: _dafny.Map
        out132_: _dafny.Map
        out132_ = default__.generateUnserializableEncryptionContext()
        d_381_unserializableEncryptionContext_ = out132_
        d_382_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_383_valueOrError5_: Wrappers.Result = None
        d_383_valueOrError5_ = (d_365_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_373_algorithmSuiteId_, d_381_unserializableEncryptionContext_, _dafny.Seq([])))
        if not(not((d_383_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(366,33): " + _dafny.string_of(d_383_valueOrError5_))
        d_382_decryptionMaterialsIn_ = (d_383_valueOrError5_).Extract()
        d_384_decryptionMaterialsOut_: Wrappers.Result
        out133_: Wrappers.Result
        out133_ = (d_369_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_382_decryptionMaterialsIn_, _dafny.Seq([d_380_edk_])))
        d_384_decryptionMaterialsOut_ = out133_
        if not((d_384_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(379,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def generateUnserializableEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_385_keyA_: _dafny.Seq
        d_386_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_386_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_386_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(384,16): " + _dafny.string_of(d_386_valueOrError0_))
        d_385_keyA_ = (d_386_valueOrError0_).Extract()
        d_387_invalidVal_: _dafny.Seq
        d_387_invalidVal_ = _dafny.Seq([0 for d_388___v5_ in range(65536)])
        encCtx = _dafny.Map({d_385_keyA_: d_387_invalidVal_})
        return encCtx
        return encCtx

