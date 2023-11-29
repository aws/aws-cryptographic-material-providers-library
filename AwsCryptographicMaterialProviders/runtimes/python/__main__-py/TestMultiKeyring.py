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
        d_1810_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1811_valueOrError0_: Wrappers.Result = None
        out434_: Wrappers.Result
        out434_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1811_valueOrError0_ = out434_
        if not(not((d_1811_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(18,12): " + _dafny.string_of(d_1811_valueOrError0_))
        d_1810_mpl_ = (d_1811_valueOrError0_).Extract()
        d_1812_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1812_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1813_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1814_valueOrError1_: Wrappers.Result = None
        d_1814_valueOrError1_ = (d_1810_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1812_algorithmSuiteId_, encryptionContext, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1814_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(21,30): " + _dafny.string_of(d_1814_valueOrError1_))
        d_1813_encryptionMaterialsIn_ = (d_1814_valueOrError1_).Extract()
        res = d_1813_encryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def getInputDecryptionMaterials(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        d_1815_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1816_valueOrError0_: Wrappers.Result = None
        out435_: Wrappers.Result
        out435_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1816_valueOrError0_ = out435_
        if not(not((d_1816_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(35,12): " + _dafny.string_of(d_1816_valueOrError0_))
        d_1815_mpl_ = (d_1816_valueOrError0_).Extract()
        d_1817_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1817_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1818_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1819_valueOrError1_: Wrappers.Result = None
        d_1819_valueOrError1_ = (d_1815_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1817_algorithmSuiteId_, encryptionContext, _dafny.Seq([])))
        if not(not((d_1819_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(38,30): " + _dafny.string_of(d_1819_valueOrError1_))
        d_1818_decryptionMaterialsIn_ = (d_1819_valueOrError1_).Extract()
        res = d_1818_decryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def TestHappyCase():
        d_1820_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1821_valueOrError0_: Wrappers.Result = None
        out436_: Wrappers.Result
        out436_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1821_valueOrError0_ = out436_
        if not(not((d_1821_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(51,12): " + _dafny.string_of(d_1821_valueOrError0_))
        d_1820_mpl_ = (d_1821_valueOrError0_).Extract()
        d_1822_encryptionContext_: _dafny.Map
        out437_: _dafny.Map
        out437_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1822_encryptionContext_ = out437_
        d_1823_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out438_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out438_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1822_encryptionContext_)
        d_1823_encryptionMaterials_ = out438_
        d_1824_decryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out439_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out439_ = TestMultiKeyring.default__.getInputDecryptionMaterials(d_1822_encryptionContext_)
        d_1824_decryptionMaterials_ = out439_
        d_1825_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out440_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out440_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1822_encryptionContext_)
        d_1825_rawAESKeyring_ = out440_
        d_1826_expectedEncryptionMaterials_: Wrappers.Result
        out441_: Wrappers.Result
        out441_ = (d_1825_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1823_encryptionMaterials_))
        d_1826_expectedEncryptionMaterials_ = out441_
        if not((d_1826_expectedEncryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1827_expectedPlaintextDataKey_: Wrappers.Option
        d_1827_expectedPlaintextDataKey_ = (((d_1826_expectedEncryptionMaterials_).value).materials).plaintextDataKey
        if not((d_1827_expectedPlaintextDataKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1828_staticKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out442_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out442_ = TestMultiKeyring.default__.SetupStaticKeyring(Wrappers.Option_Some(((d_1826_expectedEncryptionMaterials_).value).materials), Wrappers.Option_None())
        d_1828_staticKeyring_ = out442_
        d_1829_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1830_valueOrError1_: Wrappers.Result = None
        out443_: Wrappers.Result
        out443_ = (d_1820_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1828_staticKeyring_), _dafny.Seq([d_1825_rawAESKeyring_])))
        d_1830_valueOrError1_ = out443_
        if not(not((d_1830_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(69,21): " + _dafny.string_of(d_1830_valueOrError1_))
        d_1829_multiKeyring_ = (d_1830_valueOrError1_).Extract()
        d_1831_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1832_valueOrError2_: Wrappers.Result = None
        out444_: Wrappers.Result
        out444_ = (d_1829_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1823_encryptionMaterials_))
        d_1832_valueOrError2_ = out444_
        if not(not((d_1832_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(74,31): " + _dafny.string_of(d_1832_valueOrError2_))
        d_1831_encryptionMaterialsOut_ = (d_1832_valueOrError2_).Extract()
        d_1833___v0_: tuple
        d_1834_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1834_valueOrError3_ = (d_1820_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1831_encryptionMaterialsOut_).materials)
        if not(not((d_1834_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(76,10): " + _dafny.string_of(d_1834_valueOrError3_))
        d_1833___v0_ = (d_1834_valueOrError3_).Extract()
        if not(((((d_1831_encryptionMaterialsOut_).materials).plaintextDataKey).value) == ((d_1827_expectedPlaintextDataKey_).value)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_1831_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (2)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestChildKeyringFailureEncrypt():
        d_1835_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1836_valueOrError0_: Wrappers.Result = None
        out445_: Wrappers.Result
        out445_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1836_valueOrError0_ = out445_
        if not(not((d_1836_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(106,12): " + _dafny.string_of(d_1836_valueOrError0_))
        d_1835_mpl_ = (d_1836_valueOrError0_).Extract()
        d_1837_encryptionContext_: _dafny.Map
        out446_: _dafny.Map
        out446_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1837_encryptionContext_ = out446_
        d_1838_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out447_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out447_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1837_encryptionContext_)
        d_1838_rawAESKeyring_ = out447_
        d_1839_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out448_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out448_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1839_failingKeyring_ = out448_
        d_1840_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1841_valueOrError1_: Wrappers.Result = None
        out449_: Wrappers.Result
        out449_ = (d_1835_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1838_rawAESKeyring_), _dafny.Seq([d_1839_failingKeyring_])))
        d_1841_valueOrError1_ = out449_
        if not(not((d_1841_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(116,21): " + _dafny.string_of(d_1841_valueOrError1_))
        d_1840_multiKeyring_ = (d_1841_valueOrError1_).Extract()
        d_1842_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out450_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out450_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1837_encryptionContext_)
        d_1842_encryptionMaterials_ = out450_
        d_1843_result_: Wrappers.Result
        out451_: Wrappers.Result
        out451_ = (d_1840_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1842_encryptionMaterials_))
        d_1843_result_ = out451_
        if not((d_1843_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringFails():
        d_1844_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1845_valueOrError0_: Wrappers.Result = None
        out452_: Wrappers.Result
        out452_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1845_valueOrError0_ = out452_
        if not(not((d_1845_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(129,12): " + _dafny.string_of(d_1845_valueOrError0_))
        d_1844_mpl_ = (d_1845_valueOrError0_).Extract()
        d_1846_encryptionContext_: _dafny.Map
        out453_: _dafny.Map
        out453_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1846_encryptionContext_ = out453_
        d_1847_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out454_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out454_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1847_failingKeyring_ = out454_
        d_1848_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out455_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out455_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1846_encryptionContext_)
        d_1848_rawAESKeyring_ = out455_
        d_1849_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1850_valueOrError1_: Wrappers.Result = None
        out456_: Wrappers.Result
        out456_ = (d_1844_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1847_failingKeyring_), _dafny.Seq([d_1848_rawAESKeyring_])))
        d_1850_valueOrError1_ = out456_
        if not(not((d_1850_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(142,21): " + _dafny.string_of(d_1850_valueOrError1_))
        d_1849_multiKeyring_ = (d_1850_valueOrError1_).Extract()
        d_1851_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out457_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out457_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1846_encryptionContext_)
        d_1851_encryptionMaterials_ = out457_
        d_1852_result_: Wrappers.Result
        out458_: Wrappers.Result
        out458_ = (d_1849_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1851_encryptionMaterials_))
        d_1852_result_ = out458_
        if not((d_1852_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringDoesNotReturnPlaintextDataKey():
        d_1853_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1854_valueOrError0_: Wrappers.Result = None
        out459_: Wrappers.Result
        out459_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1854_valueOrError0_ = out459_
        if not(not((d_1854_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(155,12): " + _dafny.string_of(d_1854_valueOrError0_))
        d_1853_mpl_ = (d_1854_valueOrError0_).Extract()
        d_1855_encryptionContext_: _dafny.Map
        out460_: _dafny.Map
        out460_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1855_encryptionContext_ = out460_
        d_1856_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out461_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out461_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1855_encryptionContext_)
        d_1856_encryptionMaterials_ = out461_
        d_1857_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out462_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out462_ = TestMultiKeyring.default__.SetupStaticKeyring(Wrappers.Option_Some(d_1856_encryptionMaterials_), Wrappers.Option_None())
        d_1857_failingKeyring_ = out462_
        d_1858_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1859_valueOrError1_: Wrappers.Result = None
        out463_: Wrappers.Result
        out463_ = (d_1853_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1857_failingKeyring_), _dafny.Seq([])))
        d_1859_valueOrError1_ = out463_
        if not(not((d_1859_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(165,21): " + _dafny.string_of(d_1859_valueOrError1_))
        d_1858_multiKeyring_ = (d_1859_valueOrError1_).Extract()
        d_1860_result_: Wrappers.Result
        out464_: Wrappers.Result
        out464_ = (d_1858_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1856_encryptionMaterials_))
        d_1860_result_ = out464_
        if not((d_1860_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorAbleToDecrypt():
        d_1861_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1862_valueOrError0_: Wrappers.Result = None
        out465_: Wrappers.Result
        out465_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1862_valueOrError0_ = out465_
        if not(not((d_1862_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(176,12): " + _dafny.string_of(d_1862_valueOrError0_))
        d_1861_mpl_ = (d_1862_valueOrError0_).Extract()
        d_1863_encryptionContext_: _dafny.Map
        out466_: _dafny.Map
        out466_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1863_encryptionContext_ = out466_
        d_1864_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out467_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out467_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1863_encryptionContext_)
        d_1864_rawAESKeyring_ = out467_
        d_1865_inputEncryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out468_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out468_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1863_encryptionContext_)
        d_1865_inputEncryptionMaterials_ = out468_
        d_1866_encryptionMaterials_: Wrappers.Result
        out469_: Wrappers.Result
        out469_ = (d_1864_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1865_inputEncryptionMaterials_))
        d_1866_encryptionMaterials_ = out469_
        if not((d_1866_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1867_inputDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out470_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out470_ = TestMultiKeyring.default__.getInputDecryptionMaterials(d_1863_encryptionContext_)
        d_1867_inputDecryptionMaterials_ = out470_
        d_1868_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out471_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out471_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1868_failingKeyring_ = out471_
        d_1869_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1870_valueOrError1_: Wrappers.Result = None
        out472_: Wrappers.Result
        out472_ = (d_1861_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1864_rawAESKeyring_), _dafny.Seq([d_1868_failingKeyring_])))
        d_1870_valueOrError1_ = out472_
        if not(not((d_1870_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(196,21): " + _dafny.string_of(d_1870_valueOrError1_))
        d_1869_multiKeyring_ = (d_1870_valueOrError1_).Extract()
        d_1871_onDecryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput
        d_1871_onDecryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1867_inputDecryptionMaterials_, (((d_1866_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_1872_decryptionMaterials_: Wrappers.Result
        out473_: Wrappers.Result
        out473_ = (d_1869_multiKeyring_).OnDecrypt(d_1871_onDecryptInput_)
        d_1872_decryptionMaterials_ = out473_
        if not((d_1872_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_1872_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_1866_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorUnableToDecrypt():
        d_1873_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1874_valueOrError0_: Wrappers.Result = None
        out474_: Wrappers.Result
        out474_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1874_valueOrError0_ = out474_
        if not(not((d_1874_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(212,12): " + _dafny.string_of(d_1874_valueOrError0_))
        d_1873_mpl_ = (d_1874_valueOrError0_).Extract()
        d_1875_encryptionContext_: _dafny.Map
        out475_: _dafny.Map
        out475_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1875_encryptionContext_ = out475_
        d_1876_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out476_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out476_ = TestMultiKeyring.default__.setupRawAesKeyring(d_1875_encryptionContext_)
        d_1876_rawAESKeyring_ = out476_
        d_1877_inputEncryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out477_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out477_ = TestMultiKeyring.default__.getInputEncryptionMaterials(d_1875_encryptionContext_)
        d_1877_inputEncryptionMaterials_ = out477_
        d_1878_encryptionMaterials_: Wrappers.Result
        out478_: Wrappers.Result
        out478_ = (d_1876_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1877_inputEncryptionMaterials_))
        d_1878_encryptionMaterials_ = out478_
        if not((d_1878_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(237,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1879_inputDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out479_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out479_ = TestMultiKeyring.default__.getInputDecryptionMaterials(d_1875_encryptionContext_)
        d_1879_inputDecryptionMaterials_ = out479_
        d_1880_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out480_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out480_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1880_failingKeyring_ = out480_
        d_1881_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1882_valueOrError1_: Wrappers.Result = None
        out481_: Wrappers.Result
        out481_ = (d_1873_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_1880_failingKeyring_), _dafny.Seq([d_1880_failingKeyring_, d_1876_rawAESKeyring_, d_1880_failingKeyring_])))
        d_1882_valueOrError1_ = out481_
        if not(not((d_1882_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(245,21): " + _dafny.string_of(d_1882_valueOrError1_))
        d_1881_multiKeyring_ = (d_1882_valueOrError1_).Extract()
        d_1883_onDecryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput
        d_1883_onDecryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1879_inputDecryptionMaterials_, (((d_1878_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_1884_decryptionMaterials_: Wrappers.Result
        out482_: Wrappers.Result
        out482_ = (d_1881_multiKeyring_).OnDecrypt(d_1883_onDecryptInput_)
        d_1884_decryptionMaterials_ = out482_
        if not((d_1884_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_1884_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_1878_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(266,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCollectFailuresDecrypt():
        d_1885_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1886_valueOrError0_: Wrappers.Result = None
        out483_: Wrappers.Result
        out483_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1886_valueOrError0_ = out483_
        if not(not((d_1886_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(272,12): " + _dafny.string_of(d_1886_valueOrError0_))
        d_1885_mpl_ = (d_1886_valueOrError0_).Extract()
        d_1887_encryptionContext_: _dafny.Map
        out484_: _dafny.Map
        out484_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1887_encryptionContext_ = out484_
        d_1888_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out485_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out485_ = TestMultiKeyring.default__.SetupFailingKeyring()
        d_1888_failingKeyring_ = out485_
        d_1889_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1890_valueOrError1_: Wrappers.Result = None
        out486_: Wrappers.Result
        out486_ = (d_1885_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_None(), _dafny.Seq([d_1888_failingKeyring_, d_1888_failingKeyring_])))
        d_1890_valueOrError1_ = out486_
        if not(not((d_1890_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(291,21): " + _dafny.string_of(d_1890_valueOrError1_))
        d_1889_multiKeyring_ = (d_1890_valueOrError1_).Extract()
        d_1891_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1892_valueOrError2_: Wrappers.Result = None
        d_1892_valueOrError2_ = (d_1885_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), d_1887_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1892_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(296,18): " + _dafny.string_of(d_1892_valueOrError2_))
        d_1891_materials_ = (d_1892_valueOrError2_).Extract()
        d_1893_result_: Wrappers.Result
        out487_: Wrappers.Result
        out487_ = (d_1889_multiKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1891_materials_, _dafny.Seq([])))
        d_1893_result_ = out487_
        if not((d_1893_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def setupRawAesKeyring(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        d_1894_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1895_valueOrError0_: Wrappers.Result = None
        out488_: Wrappers.Result
        out488_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1895_valueOrError0_ = out488_
        if not(not((d_1895_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(313,12): " + _dafny.string_of(d_1895_valueOrError0_))
        d_1894_mpl_ = (d_1895_valueOrError0_).Extract()
        d_1896_namespace_: _dafny.Seq
        d_1897_name_: _dafny.Seq
        out489_: _dafny.Seq
        out490_: _dafny.Seq
        out489_, out490_ = TestUtils.default__.NamespaceAndName(0)
        d_1896_namespace_ = out489_
        d_1897_name_ = out490_
        d_1898_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1899_valueOrError1_: Wrappers.Result = None
        out491_: Wrappers.Result
        out491_ = (d_1894_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1896_namespace_, d_1897_name_, _dafny.Seq([0 for d_1900_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1899_valueOrError1_ = out491_
        if not(not((d_1899_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(316,22): " + _dafny.string_of(d_1899_valueOrError1_))
        d_1898_rawAESKeyring_ = (d_1899_valueOrError1_).Extract()
        res = d_1898_rawAESKeyring_
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
            d_1901_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
            d_1901_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_1901_exception_)
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).decryptionMaterials).is_Some:
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(((self).decryptionMaterials).value))
            return res
        elif True:
            d_1902_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
            d_1902_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_1902_exception_)
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
        d_1903_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_1903_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_1903_exception_)
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_1904_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_1904_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_1904_exception_)
        return res
        return res

