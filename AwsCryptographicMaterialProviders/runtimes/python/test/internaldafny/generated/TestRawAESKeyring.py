import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import Relations
import Seq_MergeSort
import Math
import Seq
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import UUID
import Time
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import Base64
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import AesKdfCtr
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import Fixtures
import TestCreateKeyStore
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider

# Module: TestRawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptGenerateDataKey():
        d_253_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_254_valueOrError0_: Wrappers.Result = None
        out85_: Wrappers.Result
        out85_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
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
        d_257_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_258_valueOrError1_: Wrappers.Result = None
        out88_: Wrappers.Result
        out88_ = (d_253_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_255_namespace_, d_256_name_, _dafny.Seq([0 for d_259_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_258_valueOrError1_ = out88_
        if not(not((d_258_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(24,25): " + _dafny.string_of(d_258_valueOrError1_))
        d_257_rawAESKeyring_ = (d_258_valueOrError1_).Extract()
        d_260_encryptionContext_: _dafny.Map
        out89_: _dafny.Map
        out89_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_260_encryptionContext_ = out89_
        d_261_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_261_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_262_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_263_valueOrError2_: Wrappers.Result = None
        d_263_valueOrError2_ = (d_253_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_261_algorithmSuiteId_, d_260_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_263_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(33,33): " + _dafny.string_of(d_263_valueOrError2_))
        d_262_encryptionMaterialsIn_ = (d_263_valueOrError2_).Extract()
        d_264_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_265_valueOrError3_: Wrappers.Result = None
        out90_: Wrappers.Result
        out90_ = (d_257_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_262_encryptionMaterialsIn_))
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
        d_268_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_268_edk_ = (((d_264_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_269_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_270_valueOrError5_: Wrappers.Result = None
        d_270_valueOrError5_ = (d_253_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_261_algorithmSuiteId_, d_260_encryptionContext_, _dafny.Seq([])))
        if not(not((d_270_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(69,33): " + _dafny.string_of(d_270_valueOrError5_))
        d_269_decryptionMaterialsIn_ = (d_270_valueOrError5_).Extract()
        d_271_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_272_valueOrError6_: Wrappers.Result = None
        out91_: Wrappers.Result
        out91_ = (d_257_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_269_decryptionMaterialsIn_, _dafny.Seq([d_268_edk_])))
        d_272_valueOrError6_ = out91_
        if not(not((d_272_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(76,34): " + _dafny.string_of(d_272_valueOrError6_))
        d_271_decryptionMaterialsOut_ = (d_272_valueOrError6_).Extract()
        if not((((d_264_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_264_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_273_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_274_valueOrError0_: Wrappers.Result = None
        out92_: Wrappers.Result
        out92_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
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
        d_277_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_278_valueOrError1_: Wrappers.Result = None
        out95_: Wrappers.Result
        out95_ = (d_273_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_275_namespace_, d_276_name_, _dafny.Seq([0 for d_279_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_278_valueOrError1_ = out95_
        if not(not((d_278_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(97,25): " + _dafny.string_of(d_278_valueOrError1_))
        d_277_rawAESKeyring_ = (d_278_valueOrError1_).Extract()
        d_280_encryptionContext_: _dafny.Map
        out96_: _dafny.Map
        out96_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_280_encryptionContext_ = out96_
        d_281_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_281_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_282_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_283_valueOrError2_: Wrappers.Result = None
        d_283_valueOrError2_ = (d_273_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_281_algorithmSuiteId_, d_280_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_283_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(106,33): " + _dafny.string_of(d_283_valueOrError2_))
        d_282_encryptionMaterialsIn_ = (d_283_valueOrError2_).Extract()
        d_284_pdk_: _dafny.Seq
        d_284_pdk_ = _dafny.Seq([0 for d_285_i_ in range(32)])
        d_286_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_287_valueOrError3_: Wrappers.Result = None
        pat_let_tv0_ = d_284_pdk_
        out97_: Wrappers.Result
        def iife4_(_pat_let1_0):
            def iife5_(d_288_dt__update__tmp_h0_):
                def iife6_(_pat_let2_0):
                    def iife7_(d_289_dt__update_hplaintextDataKey_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((d_288_dt__update__tmp_h0_).algorithmSuite, (d_288_dt__update__tmp_h0_).encryptionContext, (d_288_dt__update__tmp_h0_).encryptedDataKeys, (d_288_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_289_dt__update_hplaintextDataKey_h0_, (d_288_dt__update__tmp_h0_).signingKey, (d_288_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife7_(_pat_let2_0)
                return iife6_(Wrappers.Option_Some(pat_let_tv0_))
            return iife5_(_pat_let1_0)
        out97_ = (d_277_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(iife4_(d_282_encryptionMaterialsIn_)))
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
        d_292_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_292_edk_ = (((d_286_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_293_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_294_valueOrError5_: Wrappers.Result = None
        d_294_valueOrError5_ = (d_273_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_281_algorithmSuiteId_, d_280_encryptionContext_, _dafny.Seq([])))
        if not(not((d_294_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(129,33): " + _dafny.string_of(d_294_valueOrError5_))
        d_293_decryptionMaterialsIn_ = (d_294_valueOrError5_).Extract()
        d_295_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_296_valueOrError6_: Wrappers.Result = None
        out98_: Wrappers.Result
        out98_ = (d_277_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_293_decryptionMaterialsIn_, _dafny.Seq([d_292_edk_])))
        d_296_valueOrError6_ = out98_
        if not(not((d_296_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(137,34): " + _dafny.string_of(d_296_valueOrError6_))
        d_295_decryptionMaterialsOut_ = (d_296_valueOrError6_).Extract()
        if not((((d_295_decryptionMaterialsOut_).materials).plaintextDataKey) == (Wrappers.Option_Some(d_284_pdk_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_297_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_298_valueOrError0_: Wrappers.Result = None
        out99_: Wrappers.Result
        out99_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
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
        d_301_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_302_valueOrError1_: Wrappers.Result = None
        out102_: Wrappers.Result
        out102_ = (d_297_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_299_namespace_, d_300_name_, _dafny.Seq([0 for d_303_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_302_valueOrError1_ = out102_
        if not(not((d_302_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(158,25): " + _dafny.string_of(d_302_valueOrError1_))
        d_301_rawAESKeyring_ = (d_302_valueOrError1_).Extract()
        d_304_mismatchedAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_305_valueOrError2_: Wrappers.Result = None
        out103_: Wrappers.Result
        out103_ = (d_297_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_299_namespace_, _dafny.Seq("mismatched"), _dafny.Seq([1 for d_306_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_305_valueOrError2_ = out103_
        if not(not((d_305_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(165,32): " + _dafny.string_of(d_305_valueOrError2_))
        d_304_mismatchedAESKeyring_ = (d_305_valueOrError2_).Extract()
        d_307_encryptionContext_: _dafny.Map
        out104_: _dafny.Map
        out104_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_307_encryptionContext_ = out104_
        d_308_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_308_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_309_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_310_valueOrError3_: Wrappers.Result = None
        d_310_valueOrError3_ = (d_297_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_308_algorithmSuiteId_, d_307_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_310_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(175,33): " + _dafny.string_of(d_310_valueOrError3_))
        d_309_encryptionMaterialsIn_ = (d_310_valueOrError3_).Extract()
        d_311_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_312_valueOrError4_: Wrappers.Result = None
        out105_: Wrappers.Result
        out105_ = (d_301_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_309_encryptionMaterialsIn_))
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
        d_315_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_315_edk_ = (((d_311_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_316_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_317_valueOrError6_: Wrappers.Result = None
        d_317_valueOrError6_ = (d_297_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_308_algorithmSuiteId_, d_307_encryptionContext_, _dafny.Seq([])))
        if not(not((d_317_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(193,33): " + _dafny.string_of(d_317_valueOrError6_))
        d_316_decryptionMaterialsIn_ = (d_317_valueOrError6_).Extract()
        d_318_decryptionMaterialsOut_: Wrappers.Result
        out106_: Wrappers.Result
        out106_ = (d_304_mismatchedAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_316_decryptionMaterialsIn_, _dafny.Seq([d_315_edk_])))
        d_318_decryptionMaterialsOut_ = out106_
        if not((d_318_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_319_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_320_valueOrError0_: Wrappers.Result = None
        out107_: Wrappers.Result
        out107_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
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
        d_323_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_324_valueOrError1_: Wrappers.Result = None
        out110_: Wrappers.Result
        out110_ = (d_319_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_321_namespace_, d_322_name_, _dafny.Seq([0 for d_325_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_324_valueOrError1_ = out110_
        if not(not((d_324_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,25): " + _dafny.string_of(d_324_valueOrError1_))
        d_323_rawAESKeyring_ = (d_324_valueOrError1_).Extract()
        d_326_encryptionContext_: _dafny.Map
        out111_: _dafny.Map
        out111_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_326_encryptionContext_ = out111_
        d_327_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_327_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_328_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_329_valueOrError2_: Wrappers.Result = None
        d_329_valueOrError2_ = (d_319_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_327_algorithmSuiteId_, d_326_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_329_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(224,33): " + _dafny.string_of(d_329_valueOrError2_))
        d_328_encryptionMaterialsIn_ = (d_329_valueOrError2_).Extract()
        d_330_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_331_valueOrError3_: Wrappers.Result = None
        out112_: Wrappers.Result
        out112_ = (d_323_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_328_encryptionMaterialsIn_))
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
        d_334_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_334_edk_ = (((d_330_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_335_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_336_valueOrError5_: Wrappers.Result = None
        d_336_valueOrError5_ = (d_319_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_327_algorithmSuiteId_, d_326_encryptionContext_, _dafny.Seq([])))
        if not(not((d_336_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(242,33): " + _dafny.string_of(d_336_valueOrError5_))
        d_335_decryptionMaterialsIn_ = (d_336_valueOrError5_).Extract()
        d_337_fakeEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_337_fakeEdk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((d_334_edk_).keyProviderId, (d_334_edk_).keyProviderInfo, _dafny.Seq([0 for d_338_i_ in range(len((d_334_edk_).ciphertext))]))
        d_339_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_340_valueOrError6_: Wrappers.Result = None
        out113_: Wrappers.Result
        out113_ = (d_323_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_335_decryptionMaterialsIn_, _dafny.Seq([d_337_fakeEdk_, d_334_edk_])))
        d_340_valueOrError6_ = out113_
        if not(not((d_340_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(255,34): " + _dafny.string_of(d_340_valueOrError6_))
        d_339_decryptionMaterialsOut_ = (d_340_valueOrError6_).Extract()
        if not((((d_339_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_330_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(262,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptNoEDKs():
        d_341_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_342_valueOrError0_: Wrappers.Result = None
        out114_: Wrappers.Result
        out114_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
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
        d_345_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_346_valueOrError1_: Wrappers.Result = None
        out117_: Wrappers.Result
        out117_ = (d_341_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_343_namespace_, d_344_name_, _dafny.Seq([0 for d_347_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_346_valueOrError1_ = out117_
        if not(not((d_346_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,25): " + _dafny.string_of(d_346_valueOrError1_))
        d_345_rawAESKeyring_ = (d_346_valueOrError1_).Extract()
        d_348_encryptionContext_: _dafny.Map
        out118_: _dafny.Map
        out118_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_348_encryptionContext_ = out118_
        d_349_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_349_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_350_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_351_valueOrError2_: Wrappers.Result = None
        d_351_valueOrError2_ = (d_341_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_349_algorithmSuiteId_, d_348_encryptionContext_, _dafny.Seq([])))
        if not(not((d_351_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(280,33): " + _dafny.string_of(d_351_valueOrError2_))
        d_350_decryptionMaterialsIn_ = (d_351_valueOrError2_).Extract()
        d_352_decryptionMaterialsOut_: Wrappers.Result
        out119_: Wrappers.Result
        out119_ = (d_345_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_350_decryptionMaterialsIn_, _dafny.Seq([])))
        d_352_decryptionMaterialsOut_ = out119_
        if not((d_352_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(293,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptUnserializableEC():
        d_353_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_354_valueOrError0_: Wrappers.Result = None
        out120_: Wrappers.Result
        out120_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
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
        d_357_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_358_valueOrError1_: Wrappers.Result = None
        out123_: Wrappers.Result
        out123_ = (d_353_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_355_namespace_, d_356_name_, _dafny.Seq([0 for d_359_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_358_valueOrError1_ = out123_
        if not(not((d_358_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,25): " + _dafny.string_of(d_358_valueOrError1_))
        d_357_rawAESKeyring_ = (d_358_valueOrError1_).Extract()
        d_360_unserializableEncryptionContext_: _dafny.Map
        out124_: _dafny.Map
        out124_ = default__.generateUnserializableEncryptionContext()
        d_360_unserializableEncryptionContext_ = out124_
        d_361_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_361_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_362_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_363_valueOrError2_: Wrappers.Result = None
        d_363_valueOrError2_ = (d_353_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_361_algorithmSuiteId_, d_360_unserializableEncryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_363_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(314,33): " + _dafny.string_of(d_363_valueOrError2_))
        d_362_encryptionMaterialsIn_ = (d_363_valueOrError2_).Extract()
        d_364_encryptionMaterialsOut_: Wrappers.Result
        out125_: Wrappers.Result
        out125_ = (d_357_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_362_encryptionMaterialsIn_))
        d_364_encryptionMaterialsOut_ = out125_
        if not((d_364_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(326,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptUnserializableEC():
        d_365_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_366_valueOrError0_: Wrappers.Result = None
        out126_: Wrappers.Result
        out126_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
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
        d_369_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_370_valueOrError1_: Wrappers.Result = None
        out129_: Wrappers.Result
        out129_ = (d_365_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_367_namespace_, d_368_name_, _dafny.Seq([0 for d_371_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_370_valueOrError1_ = out129_
        if not(not((d_370_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,25): " + _dafny.string_of(d_370_valueOrError1_))
        d_369_rawAESKeyring_ = (d_370_valueOrError1_).Extract()
        d_372_encryptionContext_: _dafny.Map
        out130_: _dafny.Map
        out130_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_372_encryptionContext_ = out130_
        d_373_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_373_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_374_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_375_valueOrError2_: Wrappers.Result = None
        d_375_valueOrError2_ = (d_365_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_373_algorithmSuiteId_, d_372_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_375_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(348,33): " + _dafny.string_of(d_375_valueOrError2_))
        d_374_encryptionMaterialsIn_ = (d_375_valueOrError2_).Extract()
        d_376_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_377_valueOrError3_: Wrappers.Result = None
        out131_: Wrappers.Result
        out131_ = (d_369_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_374_encryptionMaterialsIn_))
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
        d_380_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_380_edk_ = (((d_376_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_381_unserializableEncryptionContext_: _dafny.Map
        out132_: _dafny.Map
        out132_ = default__.generateUnserializableEncryptionContext()
        d_381_unserializableEncryptionContext_ = out132_
        d_382_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_383_valueOrError5_: Wrappers.Result = None
        d_383_valueOrError5_ = (d_365_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_373_algorithmSuiteId_, d_381_unserializableEncryptionContext_, _dafny.Seq([])))
        if not(not((d_383_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(366,33): " + _dafny.string_of(d_383_valueOrError5_))
        d_382_decryptionMaterialsIn_ = (d_383_valueOrError5_).Extract()
        d_384_decryptionMaterialsOut_: Wrappers.Result
        out133_: Wrappers.Result
        out133_ = (d_369_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_382_decryptionMaterialsIn_, _dafny.Seq([d_380_edk_])))
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

