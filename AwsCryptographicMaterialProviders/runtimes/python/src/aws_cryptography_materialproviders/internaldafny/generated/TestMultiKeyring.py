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

assert "TestMultiKeyring" == __name__
TestMultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getInputEncryptionMaterials(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        d_1808_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1809_valueOrError0_: Wrappers.Result = None
        out434_: Wrappers.Result
        out434_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1809_valueOrError0_ = out434_
        if not(not((d_1809_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(18,12): " + _dafny.string_of(d_1809_valueOrError0_))
        d_1808_mpl_ = (d_1809_valueOrError0_).Extract()
        d_1810_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1810_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1811_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1812_valueOrError1_: Wrappers.Result = None
        d_1812_valueOrError1_ = (d_1808_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1810_algorithmSuiteId_, encryptionContext, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1812_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(21,30): " + _dafny.string_of(d_1812_valueOrError1_))
        d_1811_encryptionMaterialsIn_ = (d_1812_valueOrError1_).Extract()
        res = d_1811_encryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def getInputDecryptionMaterials(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        d_1813_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1814_valueOrError0_: Wrappers.Result = None
        out435_: Wrappers.Result
        out435_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1814_valueOrError0_ = out435_
        if not(not((d_1814_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(35,12): " + _dafny.string_of(d_1814_valueOrError0_))
        d_1813_mpl_ = (d_1814_valueOrError0_).Extract()
        d_1815_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1815_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1816_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1817_valueOrError1_: Wrappers.Result = None
        d_1817_valueOrError1_ = (d_1813_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1815_algorithmSuiteId_, encryptionContext, _dafny.Seq([])))
        if not(not((d_1817_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(38,30): " + _dafny.string_of(d_1817_valueOrError1_))
        d_1816_decryptionMaterialsIn_ = (d_1817_valueOrError1_).Extract()
        res = d_1816_decryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def TestHappyCase():
        d_1818_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1819_valueOrError0_: Wrappers.Result = None
        out436_: Wrappers.Result
        out436_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1819_valueOrError0_ = out436_
        if not(not((d_1819_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(51,12): " + _dafny.string_of(d_1819_valueOrError0_))
        d_1818_mpl_ = (d_1819_valueOrError0_).Extract()
        d_1820_encryptionContext_: _dafny.Map
        out437_: _dafny.Map
        out437_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1820_encryptionContext_ = out437_
        d_1821_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out438_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out438_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1820_encryptionContext_)
        d_1821_encryptionMaterials_ = out438_
        d_1822_decryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out439_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out439_ = TestMultiKeyring.default__.getInputDecryptionMaterials(d_1820_encryptionContext_)
        d_1822_decryptionMaterials_ = out439_
        d_1823_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out440_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out440_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1820_encryptionContext_)
        d_1823_rawAESKeyring_ = out440_
        d_1824_expectedEncryptionMaterials_: Wrappers.Result
        out441_: Wrappers.Result
        out441_ = (d_1823_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1821_encryptionMaterials_))
        d_1824_expectedEncryptionMaterials_ = out441_
        if not((d_1824_expectedEncryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1825_expectedPlaintextDataKey_: Wrappers.Option
        d_1825_expectedPlaintextDataKey_ = (((d_1824_expectedEncryptionMaterials_).value).materials).plaintextDataKey
        if not((d_1825_expectedPlaintextDataKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1826_staticKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out442_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out442_ = TestMultiKeyring.default__.SetupStaticKeyring(Wrappers.Option_Some(((d_1824_expectedEncryptionMaterials_).value).materials), Wrappers.Option_None())
        d_1826_staticKeyring_ = out442_
        d_1827_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1828_valueOrError1_: Wrappers.Result = None
        out443_: Wrappers.Result
        out443_ = (d_1818_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1826_staticKeyring_), _dafny.Seq([d_1823_rawAESKeyring_])))
        d_1828_valueOrError1_ = out443_
        if not(not((d_1828_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(69,21): " + _dafny.string_of(d_1828_valueOrError1_))
        d_1827_multiKeyring_ = (d_1828_valueOrError1_).Extract()
        d_1829_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1830_valueOrError2_: Wrappers.Result = None
        out444_: Wrappers.Result
        out444_ = (d_1827_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1821_encryptionMaterials_))
        d_1830_valueOrError2_ = out444_
        if not(not((d_1830_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(74,31): " + _dafny.string_of(d_1830_valueOrError2_))
        d_1829_encryptionMaterialsOut_ = (d_1830_valueOrError2_).Extract()
        d_1831___v0_: tuple
        d_1832_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1832_valueOrError3_ = (d_1818_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1829_encryptionMaterialsOut_).materials)
        if not(not((d_1832_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(76,10): " + _dafny.string_of(d_1832_valueOrError3_))
        d_1831___v0_ = (d_1832_valueOrError3_).Extract()
        if not(((((d_1829_encryptionMaterialsOut_).materials).plaintextDataKey).value) == ((d_1825_expectedPlaintextDataKey_).value)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_1829_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (2)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestChildKeyringFailureEncrypt():
        d_1833_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1834_valueOrError0_: Wrappers.Result = None
        out445_: Wrappers.Result
        out445_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1834_valueOrError0_ = out445_
        if not(not((d_1834_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(106,12): " + _dafny.string_of(d_1834_valueOrError0_))
        d_1833_mpl_ = (d_1834_valueOrError0_).Extract()
        d_1835_encryptionContext_: _dafny.Map
        out446_: _dafny.Map
        out446_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1835_encryptionContext_ = out446_
        d_1836_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out447_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out447_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1835_encryptionContext_)
        d_1836_rawAESKeyring_ = out447_
        d_1837_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out448_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out448_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1837_failingKeyring_ = out448_
        d_1838_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1839_valueOrError1_: Wrappers.Result = None
        out449_: Wrappers.Result
        out449_ = (d_1833_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1836_rawAESKeyring_), _dafny.Seq([d_1837_failingKeyring_])))
        d_1839_valueOrError1_ = out449_
        if not(not((d_1839_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(116,21): " + _dafny.string_of(d_1839_valueOrError1_))
        d_1838_multiKeyring_ = (d_1839_valueOrError1_).Extract()
        d_1840_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out450_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out450_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1835_encryptionContext_)
        d_1840_encryptionMaterials_ = out450_
        d_1841_result_: Wrappers.Result
        out451_: Wrappers.Result
        out451_ = (d_1838_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1840_encryptionMaterials_))
        d_1841_result_ = out451_
        if not((d_1841_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringFails():
        d_1842_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1843_valueOrError0_: Wrappers.Result = None
        out452_: Wrappers.Result
        out452_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1843_valueOrError0_ = out452_
        if not(not((d_1843_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(129,12): " + _dafny.string_of(d_1843_valueOrError0_))
        d_1842_mpl_ = (d_1843_valueOrError0_).Extract()
        d_1844_encryptionContext_: _dafny.Map
        out453_: _dafny.Map
        out453_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1844_encryptionContext_ = out453_
        d_1845_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out454_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out454_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1845_failingKeyring_ = out454_
        d_1846_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out455_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out455_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1844_encryptionContext_)
        d_1846_rawAESKeyring_ = out455_
        d_1847_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1848_valueOrError1_: Wrappers.Result = None
        out456_: Wrappers.Result
        out456_ = (d_1842_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1845_failingKeyring_), _dafny.Seq([d_1846_rawAESKeyring_])))
        d_1848_valueOrError1_ = out456_
        if not(not((d_1848_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(142,21): " + _dafny.string_of(d_1848_valueOrError1_))
        d_1847_multiKeyring_ = (d_1848_valueOrError1_).Extract()
        d_1849_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out457_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out457_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1844_encryptionContext_)
        d_1849_encryptionMaterials_ = out457_
        d_1850_result_: Wrappers.Result
        out458_: Wrappers.Result
        out458_ = (d_1847_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1849_encryptionMaterials_))
        d_1850_result_ = out458_
        if not((d_1850_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringDoesNotReturnPlaintextDataKey():
        d_1851_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1852_valueOrError0_: Wrappers.Result = None
        out459_: Wrappers.Result
        out459_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1852_valueOrError0_ = out459_
        if not(not((d_1852_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(155,12): " + _dafny.string_of(d_1852_valueOrError0_))
        d_1851_mpl_ = (d_1852_valueOrError0_).Extract()
        d_1853_encryptionContext_: _dafny.Map
        out460_: _dafny.Map
        out460_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1853_encryptionContext_ = out460_
        d_1854_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out461_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out461_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1853_encryptionContext_)
        d_1854_encryptionMaterials_ = out461_
        d_1855_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out462_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out462_ = TestMultiKeyring.default__.SetupStaticKeyring(Wrappers.Option_Some(d_1854_encryptionMaterials_), Wrappers.Option_None())
        d_1855_failingKeyring_ = out462_
        d_1856_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1857_valueOrError1_: Wrappers.Result = None
        out463_: Wrappers.Result
        out463_ = (d_1851_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1855_failingKeyring_), _dafny.Seq([])))
        d_1857_valueOrError1_ = out463_
        if not(not((d_1857_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(165,21): " + _dafny.string_of(d_1857_valueOrError1_))
        d_1856_multiKeyring_ = (d_1857_valueOrError1_).Extract()
        d_1858_result_: Wrappers.Result
        out464_: Wrappers.Result
        out464_ = (d_1856_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1854_encryptionMaterials_))
        d_1858_result_ = out464_
        if not((d_1858_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorAbleToDecrypt():
        d_1859_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1860_valueOrError0_: Wrappers.Result = None
        out465_: Wrappers.Result
        out465_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1860_valueOrError0_ = out465_
        if not(not((d_1860_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(176,12): " + _dafny.string_of(d_1860_valueOrError0_))
        d_1859_mpl_ = (d_1860_valueOrError0_).Extract()
        d_1861_encryptionContext_: _dafny.Map
        out466_: _dafny.Map
        out466_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1861_encryptionContext_ = out466_
        d_1862_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out467_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out467_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1861_encryptionContext_)
        d_1862_rawAESKeyring_ = out467_
        d_1863_inputEncryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out468_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out468_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1861_encryptionContext_)
        d_1863_inputEncryptionMaterials_ = out468_
        d_1864_encryptionMaterials_: Wrappers.Result
        out469_: Wrappers.Result
        out469_ = (d_1862_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1863_inputEncryptionMaterials_))
        d_1864_encryptionMaterials_ = out469_
        if not((d_1864_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1865_inputDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out470_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out470_ = TestMultiKeyring.default__.getInputDecryptionMaterials(d_1861_encryptionContext_)
        d_1865_inputDecryptionMaterials_ = out470_
        d_1866_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out471_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out471_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1866_failingKeyring_ = out471_
        d_1867_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1868_valueOrError1_: Wrappers.Result = None
        out472_: Wrappers.Result
        out472_ = (d_1859_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1862_rawAESKeyring_), _dafny.Seq([d_1866_failingKeyring_])))
        d_1868_valueOrError1_ = out472_
        if not(not((d_1868_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(196,21): " + _dafny.string_of(d_1868_valueOrError1_))
        d_1867_multiKeyring_ = (d_1868_valueOrError1_).Extract()
        d_1869_onDecryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput
        d_1869_onDecryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1865_inputDecryptionMaterials_, (((d_1864_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_1870_decryptionMaterials_: Wrappers.Result
        out473_: Wrappers.Result
        out473_ = (d_1867_multiKeyring_).OnDecrypt(d_1869_onDecryptInput_)
        d_1870_decryptionMaterials_ = out473_
        if not((d_1870_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_1870_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_1864_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorUnableToDecrypt():
        d_1871_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1872_valueOrError0_: Wrappers.Result = None
        out474_: Wrappers.Result
        out474_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1872_valueOrError0_ = out474_
        if not(not((d_1872_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(212,12): " + _dafny.string_of(d_1872_valueOrError0_))
        d_1871_mpl_ = (d_1872_valueOrError0_).Extract()
        d_1873_encryptionContext_: _dafny.Map
        out475_: _dafny.Map
        out475_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1873_encryptionContext_ = out475_
        d_1874_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out476_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out476_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1873_encryptionContext_)
        d_1874_rawAESKeyring_ = out476_
        d_1875_inputEncryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out477_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out477_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1873_encryptionContext_)
        d_1875_inputEncryptionMaterials_ = out477_
        d_1876_encryptionMaterials_: Wrappers.Result
        out478_: Wrappers.Result
        out478_ = (d_1874_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1875_inputEncryptionMaterials_))
        d_1876_encryptionMaterials_ = out478_
        if not((d_1876_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(237,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1877_inputDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out479_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out479_ = TestMultiKeyring.default__.getInputDecryptionMaterials(d_1873_encryptionContext_)
        d_1877_inputDecryptionMaterials_ = out479_
        d_1878_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out480_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out480_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1878_failingKeyring_ = out480_
        d_1879_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1880_valueOrError1_: Wrappers.Result = None
        out481_: Wrappers.Result
        out481_ = (d_1871_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1878_failingKeyring_), _dafny.Seq([d_1878_failingKeyring_, d_1874_rawAESKeyring_, d_1878_failingKeyring_])))
        d_1880_valueOrError1_ = out481_
        if not(not((d_1880_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(245,21): " + _dafny.string_of(d_1880_valueOrError1_))
        d_1879_multiKeyring_ = (d_1880_valueOrError1_).Extract()
        d_1881_onDecryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput
        d_1881_onDecryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1877_inputDecryptionMaterials_, (((d_1876_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_1882_decryptionMaterials_: Wrappers.Result
        out482_: Wrappers.Result
        out482_ = (d_1879_multiKeyring_).OnDecrypt(d_1881_onDecryptInput_)
        d_1882_decryptionMaterials_ = out482_
        if not((d_1882_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_1882_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_1876_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(266,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCollectFailuresDecrypt():
        d_1883_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1884_valueOrError0_: Wrappers.Result = None
        out483_: Wrappers.Result
        out483_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1884_valueOrError0_ = out483_
        if not(not((d_1884_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(272,12): " + _dafny.string_of(d_1884_valueOrError0_))
        d_1883_mpl_ = (d_1884_valueOrError0_).Extract()
        d_1885_encryptionContext_: _dafny.Map
        out484_: _dafny.Map
        out484_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1885_encryptionContext_ = out484_
        d_1886_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out485_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out485_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1886_failingKeyring_ = out485_
        d_1887_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1888_valueOrError1_: Wrappers.Result = None
        out486_: Wrappers.Result
        out486_ = (d_1883_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_None(), _dafny.Seq([d_1886_failingKeyring_, d_1886_failingKeyring_])))
        d_1888_valueOrError1_ = out486_
        if not(not((d_1888_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(291,21): " + _dafny.string_of(d_1888_valueOrError1_))
        d_1887_multiKeyring_ = (d_1888_valueOrError1_).Extract()
        d_1889_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1890_valueOrError2_: Wrappers.Result = None
        d_1890_valueOrError2_ = (d_1883_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), d_1885_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1890_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(296,18): " + _dafny.string_of(d_1890_valueOrError2_))
        d_1889_materials_ = (d_1890_valueOrError2_).Extract()
        d_1891_result_: Wrappers.Result
        out487_: Wrappers.Result
        out487_ = (d_1887_multiKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1889_materials_, _dafny.Seq([])))
        d_1891_result_ = out487_
        if not((d_1891_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def setupRawAesKeyring(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        d_1892_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1893_valueOrError0_: Wrappers.Result = None
        out488_: Wrappers.Result
        out488_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1893_valueOrError0_ = out488_
        if not(not((d_1893_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(313,12): " + _dafny.string_of(d_1893_valueOrError0_))
        d_1892_mpl_ = (d_1893_valueOrError0_).Extract()
        d_1894_namespace_: _dafny.Seq
        d_1895_name_: _dafny.Seq
        out489_: _dafny.Seq
        out490_: _dafny.Seq
        out489_, out490_ = TestUtils.default__.NamespaceAndName(0)
        d_1894_namespace_ = out489_
        d_1895_name_ = out490_
        d_1896_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1897_valueOrError1_: Wrappers.Result = None
        out491_: Wrappers.Result
        out491_ = (d_1892_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1894_namespace_, d_1895_name_, _dafny.Seq([0 for d_1898_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1897_valueOrError1_ = out491_
        if not(not((d_1897_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(316,22): " + _dafny.string_of(d_1897_valueOrError1_))
        d_1896_rawAESKeyring_ = (d_1897_valueOrError1_).Extract()
        res = d_1896_rawAESKeyring_
        return res
        return res

    @staticmethod
    def SetupStaticKeyring(encryptionMaterials, decryptionMaterials):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        nw78_ = TestMultiKeyring.StaticKeyring()
        nw78_.ctor__(encryptionMaterials, decryptionMaterials)
        res = nw78_
        return res
        return res

    @staticmethod
    def SetupFailingKeyring():
        res: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        nw79_ = TestMultiKeyring.FailingKeyring()
        nw79_.ctor__()
        res = nw79_
        return res
        return res


class StaticKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._encryptionMaterials: Wrappers.Option = Wrappers.Option_None.default()()
        self._decryptionMaterials: Wrappers.Option = Wrappers.Option_None.default()()
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.StaticKeyring"
    def OnEncrypt(self, input):
        out492_: Wrappers.Result
        out492_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out492_

    def OnDecrypt(self, input):
        out493_: Wrappers.Result
        out493_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out493_

    def ctor__(self, encryptionMaterials, decryptionMaterials):
        (self)._encryptionMaterials = encryptionMaterials
        (self)._decryptionMaterials = decryptionMaterials

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).encryptionMaterials).is_Some:
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(((self).encryptionMaterials).value))
            return res
        elif True:
            d_1899_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
            d_1899_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_1899_exception_)
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).decryptionMaterials).is_Some:
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(((self).decryptionMaterials).value))
            return res
        elif True:
            d_1900_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
            d_1900_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_1900_exception_)
            return res
        return res

    @property
    def encryptionMaterials(self):
        return self._encryptionMaterials
    @property
    def decryptionMaterials(self):
        return self._decryptionMaterials

class FailingKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.FailingKeyring"
    def OnEncrypt(self, input):
        out494_: Wrappers.Result
        out494_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out494_

    def OnDecrypt(self, input):
        out495_: Wrappers.Result
        out495_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out495_

    def ctor__(self):
        pass
        pass

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_1901_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_1901_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_1901_exception_)
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_1902_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_1902_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_1902_exception_)
        return res
        return res

