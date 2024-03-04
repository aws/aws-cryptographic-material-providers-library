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
import TestRawAESKeyring
import TestMultiKeyring
import TestRawRSAKeying

# Module: TestAwsKmsRsaKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestKmsRsaRoundtrip():
        d_572_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_573_valueOrError0_: Wrappers.Result = None
        out233_: Wrappers.Result
        out233_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_573_valueOrError0_ = out233_
        if not(not((d_573_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(21,12): " + _dafny.string_of(d_573_valueOrError0_))
        d_572_mpl_ = (d_573_valueOrError0_).Extract()
        d_574_publicKey_: _dafny.Seq
        d_575_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_575_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.KMS__RSA__PUBLIC__KEY)
        if not(not((d_575_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(23,18): " + _dafny.string_of(d_575_valueOrError1_))
        d_574_publicKey_ = (d_575_valueOrError1_).Extract()
        d_576_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_577_valueOrError2_: Wrappers.Result = None
        out234_: Wrappers.Result
        out234_ = (d_572_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_577_valueOrError2_ = out234_
        if not(not((d_577_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(25,23): " + _dafny.string_of(d_577_valueOrError2_))
        d_576_clientSupplier_ = (d_577_valueOrError2_).Extract()
        d_578_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_579_valueOrError3_: Wrappers.Result = None
        out235_: Wrappers.Result
        out235_ = (d_576_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_579_valueOrError3_ = out235_
        if not(not((d_579_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(26,18): " + _dafny.string_of(d_579_valueOrError3_))
        d_578_kmsClient_ = (d_579_valueOrError3_).Extract()
        d_580_kmsRsaKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_581_valueOrError4_: Wrappers.Result = None
        out236_: Wrappers.Result
        out236_ = (d_572_mpl_).CreateAwsKmsRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_574_publicKey_), TestUtils.default__.KMS__RSA__PRIVATE__KEY__ARN, software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_578_kmsClient_), Wrappers.Option_None()))
        d_581_valueOrError4_ = out236_
        if not(not((d_581_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(28,22): " + _dafny.string_of(d_581_valueOrError4_))
        d_580_kmsRsaKeyring_ = (d_581_valueOrError4_).Extract()
        d_582_encryptionContext_: _dafny.Map
        out237_: _dafny.Map
        out237_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_582_encryptionContext_ = out237_
        d_583_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_583_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_584_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_584_suite_ = AlgorithmSuites.default__.GetSuite(d_583_algorithmSuiteId_)
        d_585_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_586_valueOrError5_: Wrappers.Result = None
        d_586_valueOrError5_ = (d_572_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_583_algorithmSuiteId_, d_582_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_586_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(40,30): " + _dafny.string_of(d_586_valueOrError5_))
        d_585_encryptionMaterialsIn_ = (d_586_valueOrError5_).Extract()
        d_587_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_588_valueOrError6_: Wrappers.Result = None
        out238_: Wrappers.Result
        out238_ = (d_580_kmsRsaKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_585_encryptionMaterialsIn_))
        d_588_valueOrError6_ = out238_
        if not(not((d_588_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(50,31): " + _dafny.string_of(d_588_valueOrError6_))
        d_587_encryptionMaterialsOut_ = (d_588_valueOrError6_).Extract()
        d_589___v0_: tuple
        d_590_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_590_valueOrError7_ = (d_572_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_587_encryptionMaterialsOut_).materials)
        if not(not((d_590_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(54,10): " + _dafny.string_of(d_590_valueOrError7_))
        d_589___v0_ = (d_590_valueOrError7_).Extract()
        if not((len(((d_587_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_591_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_591_edk_ = (((d_587_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_592_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_593_valueOrError8_: Wrappers.Result = None
        d_593_valueOrError8_ = (d_572_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_583_algorithmSuiteId_, d_582_encryptionContext_, _dafny.Seq([])))
        if not(not((d_593_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(60,30): " + _dafny.string_of(d_593_valueOrError8_))
        d_592_decryptionMaterialsIn_ = (d_593_valueOrError8_).Extract()
        d_594_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_595_valueOrError9_: Wrappers.Result = None
        out239_: Wrappers.Result
        out239_ = (d_580_kmsRsaKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_592_decryptionMaterialsIn_, _dafny.Seq([d_591_edk_])))
        d_595_valueOrError9_ = out239_
        if not(not((d_595_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(67,31): " + _dafny.string_of(d_595_valueOrError9_))
        d_594_decryptionMaterialsOut_ = (d_595_valueOrError9_).Extract()
        if not((((d_587_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_594_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsRsaWithAsymmetricSignatureFails():
        d_596_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_597_valueOrError0_: Wrappers.Result = None
        out240_: Wrappers.Result
        out240_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_597_valueOrError0_ = out240_
        if not(not((d_597_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(79,12): " + _dafny.string_of(d_597_valueOrError0_))
        d_596_mpl_ = (d_597_valueOrError0_).Extract()
        d_598_publicKey_: _dafny.Seq
        d_599_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_599_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.KMS__RSA__PUBLIC__KEY)
        if not(not((d_599_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(81,18): " + _dafny.string_of(d_599_valueOrError1_))
        d_598_publicKey_ = (d_599_valueOrError1_).Extract()
        d_600_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_601_valueOrError2_: Wrappers.Result = None
        out241_: Wrappers.Result
        out241_ = (d_596_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_601_valueOrError2_ = out241_
        if not(not((d_601_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(83,23): " + _dafny.string_of(d_601_valueOrError2_))
        d_600_clientSupplier_ = (d_601_valueOrError2_).Extract()
        d_602_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_603_valueOrError3_: Wrappers.Result = None
        out242_: Wrappers.Result
        out242_ = (d_600_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_603_valueOrError3_ = out242_
        if not(not((d_603_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(84,18): " + _dafny.string_of(d_603_valueOrError3_))
        d_602_kmsClient_ = (d_603_valueOrError3_).Extract()
        d_604_kmsRsaKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_605_valueOrError4_: Wrappers.Result = None
        out243_: Wrappers.Result
        out243_ = (d_596_mpl_).CreateAwsKmsRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_598_publicKey_), TestUtils.default__.KMS__RSA__PRIVATE__KEY__ARN, software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_602_kmsClient_), Wrappers.Option_None()))
        d_605_valueOrError4_ = out243_
        if not(not((d_605_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(86,22): " + _dafny.string_of(d_605_valueOrError4_))
        d_604_kmsRsaKeyring_ = (d_605_valueOrError4_).Extract()
        d_606_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_606_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384())
        d_607_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_607_suite_ = AlgorithmSuites.default__.GetSuite(d_606_algorithmSuiteId_)
        d_608_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_609_valueOrError5_: Wrappers.Result = None
        d_609_valueOrError5_ = (d_596_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_606_algorithmSuiteId_, _dafny.Map({}), _dafny.Seq([]), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0])), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0]))))
        if not(not((d_609_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(96,30): " + _dafny.string_of(d_609_valueOrError5_))
        d_608_encryptionMaterialsIn_ = (d_609_valueOrError5_).Extract()
        d_610_encryptionMaterialsOutRes_: Wrappers.Result
        out244_: Wrappers.Result
        out244_ = (d_604_kmsRsaKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_608_encryptionMaterialsIn_))
        d_610_encryptionMaterialsOutRes_ = out244_
        if not((d_610_encryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_610_encryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_610_encryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_611_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_612_valueOrError6_: Wrappers.Result = None
        d_612_valueOrError6_ = (d_596_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_606_algorithmSuiteId_, (d_608_encryptionMaterialsIn_).encryptionContext, _dafny.Seq([])))
        if not(not((d_612_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(115,30): " + _dafny.string_of(d_612_valueOrError6_))
        d_611_decryptionMaterialsIn_ = (d_612_valueOrError6_).Extract()
        d_613_decryptionMaterialsOutRes_: Wrappers.Result
        out245_: Wrappers.Result
        out245_ = (d_604_kmsRsaKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_611_decryptionMaterialsIn_, _dafny.Seq([])))
        d_613_decryptionMaterialsOutRes_ = out245_
        if not((d_613_decryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_613_decryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_613_decryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(131,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

