import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
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
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
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
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider
import TestRawAESKeyring
import TestMultiKeyring
import TestRawRSAKeying

# assert "TestAwsKmsRsaKeyring" == __name__
TestAwsKmsRsaKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestKmsRsaRoundtrip():
        d_1993_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1994_valueOrError0_: Wrappers.Result = None
        out533_: Wrappers.Result
        out533_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1994_valueOrError0_ = out533_
        if not(not((d_1994_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(21,12): " + _dafny.string_of(d_1994_valueOrError0_))
        d_1993_mpl_ = (d_1994_valueOrError0_).Extract()
        d_1995_publicKey_: _dafny.Seq
        d_1996_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1996_valueOrError1_ = UTF8.default__.Encode((TestUtils.default__).KMS__RSA__PUBLIC__KEY)
        if not(not((d_1996_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(23,18): " + _dafny.string_of(d_1996_valueOrError1_))
        d_1995_publicKey_ = (d_1996_valueOrError1_).Extract()
        d_1997_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_1998_valueOrError2_: Wrappers.Result = None
        out534_: Wrappers.Result
        out534_ = (d_1993_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_1998_valueOrError2_ = out534_
        if not(not((d_1998_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(25,23): " + _dafny.string_of(d_1998_valueOrError2_))
        d_1997_clientSupplier_ = (d_1998_valueOrError2_).Extract()
        d_1999_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_2000_valueOrError3_: Wrappers.Result = None
        out535_: Wrappers.Result
        out535_ = (d_1997_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_2000_valueOrError3_ = out535_
        if not(not((d_2000_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(26,18): " + _dafny.string_of(d_2000_valueOrError3_))
        d_1999_kmsClient_ = (d_2000_valueOrError3_).Extract()
        d_2001_kmsRsaKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_2002_valueOrError4_: Wrappers.Result = None
        out536_: Wrappers.Result
        out536_ = (d_1993_mpl_).CreateAwsKmsRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_1995_publicKey_), (TestUtils.default__).KMS__RSA__PRIVATE__KEY__ARN, software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_1999_kmsClient_), Wrappers.Option_None()))
        d_2002_valueOrError4_ = out536_
        if not(not((d_2002_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(28,22): " + _dafny.string_of(d_2002_valueOrError4_))
        d_2001_kmsRsaKeyring_ = (d_2002_valueOrError4_).Extract()
        d_2003_encryptionContext_: _dafny.Map
        out537_: _dafny.Map
        out537_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_2003_encryptionContext_ = out537_
        d_2004_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_2004_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_2005_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_2005_suite_ = AlgorithmSuites.default__.GetSuite(d_2004_algorithmSuiteId_)
        d_2006_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_2007_valueOrError5_: Wrappers.Result = None
        d_2007_valueOrError5_ = (d_1993_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_2004_algorithmSuiteId_, d_2003_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_2007_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(40,30): " + _dafny.string_of(d_2007_valueOrError5_))
        d_2006_encryptionMaterialsIn_ = (d_2007_valueOrError5_).Extract()
        d_2008_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_2009_valueOrError6_: Wrappers.Result = None
        out538_: Wrappers.Result
        out538_ = (d_2001_kmsRsaKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_2006_encryptionMaterialsIn_))
        d_2009_valueOrError6_ = out538_
        if not(not((d_2009_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(50,31): " + _dafny.string_of(d_2009_valueOrError6_))
        d_2008_encryptionMaterialsOut_ = (d_2009_valueOrError6_).Extract()
        d_2010___v0_: tuple
        d_2011_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_2011_valueOrError7_ = (d_1993_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_2008_encryptionMaterialsOut_).materials)
        if not(not((d_2011_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(54,10): " + _dafny.string_of(d_2011_valueOrError7_))
        d_2010___v0_ = (d_2011_valueOrError7_).Extract()
        if not((len(((d_2008_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2012_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_2012_edk_ = (((d_2008_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_2013_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_2014_valueOrError8_: Wrappers.Result = None
        d_2014_valueOrError8_ = (d_1993_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_2004_algorithmSuiteId_, d_2003_encryptionContext_, _dafny.Seq([])))
        if not(not((d_2014_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(60,30): " + _dafny.string_of(d_2014_valueOrError8_))
        d_2013_decryptionMaterialsIn_ = (d_2014_valueOrError8_).Extract()
        d_2015_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_2016_valueOrError9_: Wrappers.Result = None
        out539_: Wrappers.Result
        out539_ = (d_2001_kmsRsaKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_2013_decryptionMaterialsIn_, _dafny.Seq([d_2012_edk_])))
        d_2016_valueOrError9_ = out539_
        if not(not((d_2016_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(67,31): " + _dafny.string_of(d_2016_valueOrError9_))
        d_2015_decryptionMaterialsOut_ = (d_2016_valueOrError9_).Extract()
        if not((((d_2008_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_2015_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsRsaWithAsymmetricSignatureFails():
        d_2017_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_2018_valueOrError0_: Wrappers.Result = None
        out540_: Wrappers.Result
        out540_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_2018_valueOrError0_ = out540_
        if not(not((d_2018_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(79,12): " + _dafny.string_of(d_2018_valueOrError0_))
        d_2017_mpl_ = (d_2018_valueOrError0_).Extract()
        d_2019_publicKey_: _dafny.Seq
        d_2020_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_2020_valueOrError1_ = UTF8.default__.Encode((TestUtils.default__).KMS__RSA__PUBLIC__KEY)
        if not(not((d_2020_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(81,18): " + _dafny.string_of(d_2020_valueOrError1_))
        d_2019_publicKey_ = (d_2020_valueOrError1_).Extract()
        d_2021_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_2022_valueOrError2_: Wrappers.Result = None
        out541_: Wrappers.Result
        out541_ = (d_2017_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_2022_valueOrError2_ = out541_
        if not(not((d_2022_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(83,23): " + _dafny.string_of(d_2022_valueOrError2_))
        d_2021_clientSupplier_ = (d_2022_valueOrError2_).Extract()
        d_2023_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_2024_valueOrError3_: Wrappers.Result = None
        out542_: Wrappers.Result
        out542_ = (d_2021_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_2024_valueOrError3_ = out542_
        if not(not((d_2024_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(84,18): " + _dafny.string_of(d_2024_valueOrError3_))
        d_2023_kmsClient_ = (d_2024_valueOrError3_).Extract()
        d_2025_kmsRsaKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_2026_valueOrError4_: Wrappers.Result = None
        out543_: Wrappers.Result
        out543_ = (d_2017_mpl_).CreateAwsKmsRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_2019_publicKey_), (TestUtils.default__).KMS__RSA__PRIVATE__KEY__ARN, software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_2023_kmsClient_), Wrappers.Option_None()))
        d_2026_valueOrError4_ = out543_
        if not(not((d_2026_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(86,22): " + _dafny.string_of(d_2026_valueOrError4_))
        d_2025_kmsRsaKeyring_ = (d_2026_valueOrError4_).Extract()
        d_2027_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_2027_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384())
        d_2028_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_2028_suite_ = AlgorithmSuites.default__.GetSuite(d_2027_algorithmSuiteId_)
        d_2029_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_2030_valueOrError5_: Wrappers.Result = None
        d_2030_valueOrError5_ = (d_2017_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_2027_algorithmSuiteId_, _dafny.Map({}), _dafny.Seq([]), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0])), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0]))))
        if not(not((d_2030_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(96,30): " + _dafny.string_of(d_2030_valueOrError5_))
        d_2029_encryptionMaterialsIn_ = (d_2030_valueOrError5_).Extract()
        d_2031_encryptionMaterialsOutRes_: Wrappers.Result
        out544_: Wrappers.Result
        out544_ = (d_2025_kmsRsaKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_2029_encryptionMaterialsIn_))
        d_2031_encryptionMaterialsOutRes_ = out544_
        if not((d_2031_encryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_2031_encryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_2031_encryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2032_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_2033_valueOrError6_: Wrappers.Result = None
        d_2033_valueOrError6_ = (d_2017_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_2027_algorithmSuiteId_, (d_2029_encryptionMaterialsIn_).encryptionContext, _dafny.Seq([])))
        if not(not((d_2033_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(115,30): " + _dafny.string_of(d_2033_valueOrError6_))
        d_2032_decryptionMaterialsIn_ = (d_2033_valueOrError6_).Extract()
        d_2034_decryptionMaterialsOutRes_: Wrappers.Result
        out545_: Wrappers.Result
        out545_ = (d_2025_kmsRsaKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_2032_decryptionMaterialsIn_, _dafny.Seq([])))
        d_2034_decryptionMaterialsOutRes_ = out545_
        if not((d_2034_decryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_2034_decryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_2034_decryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(131,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

