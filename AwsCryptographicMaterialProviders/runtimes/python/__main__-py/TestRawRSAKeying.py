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

assert "TestRawRSAKeying" == __name__
TestRawRSAKeying = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_1905_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1906_valueOrError0_: Wrappers.Result = None
        out496_: Wrappers.Result
        out496_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1906_valueOrError0_ = out496_
        if not(not((d_1906_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(18,12): " + _dafny.string_of(d_1906_valueOrError0_))
        d_1905_mpl_ = (d_1906_valueOrError0_).Extract()
        d_1907_namespace_: _dafny.Seq
        d_1908_name_: _dafny.Seq
        out497_: _dafny.Seq
        out498_: _dafny.Seq
        out497_, out498_ = TestUtils.default__.NamespaceAndName(0)
        d_1907_namespace_ = out497_
        d_1908_name_ = out498_
        d_1909_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out499_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out499_ = TestRawRSAKeying.default__.GenerateKeyPair(2048)
        d_1909_keys_ = out499_
        d_1910_rawRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1911_valueOrError1_: Wrappers.Result = None
        out500_: Wrappers.Result
        out500_ = (d_1905_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1907_namespace_, d_1908_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_1909_keys_).publicKey).pem), Wrappers.Option_Some(((d_1909_keys_).privateKey).pem)))
        d_1911_valueOrError1_ = out500_
        if not(not((d_1911_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(22,22): " + _dafny.string_of(d_1911_valueOrError1_))
        d_1910_rawRSAKeyring_ = (d_1911_valueOrError1_).Extract()
        d_1912_encryptionContext_: _dafny.Map
        out501_: _dafny.Map
        out501_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1912_encryptionContext_ = out501_
        d_1913_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1913_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1914_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1915_valueOrError2_: Wrappers.Result = None
        d_1915_valueOrError2_ = (d_1905_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1913_algorithmSuiteId_, d_1912_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1915_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(35,30): " + _dafny.string_of(d_1915_valueOrError2_))
        d_1914_encryptionMaterialsIn_ = (d_1915_valueOrError2_).Extract()
        d_1916_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1917_valueOrError3_: Wrappers.Result = None
        out502_: Wrappers.Result
        out502_ = (d_1910_rawRSAKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1914_encryptionMaterialsIn_))
        d_1917_valueOrError3_ = out502_
        if not(not((d_1917_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(45,31): " + _dafny.string_of(d_1917_valueOrError3_))
        d_1916_encryptionMaterialsOut_ = (d_1917_valueOrError3_).Extract()
        d_1918___v0_: tuple
        d_1919_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1919_valueOrError4_ = (d_1905_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1916_encryptionMaterialsOut_).materials)
        if not(not((d_1919_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(48,10): " + _dafny.string_of(d_1919_valueOrError4_))
        d_1918___v0_ = (d_1919_valueOrError4_).Extract()
        d_1920_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1920_edk_ = (((d_1916_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1921_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1922_valueOrError5_: Wrappers.Result = None
        d_1922_valueOrError5_ = (d_1905_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1913_algorithmSuiteId_, d_1912_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1922_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(52,30): " + _dafny.string_of(d_1922_valueOrError5_))
        d_1921_decryptionMaterialsIn_ = (d_1922_valueOrError5_).Extract()
        d_1923_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1924_valueOrError6_: Wrappers.Result = None
        out503_: Wrappers.Result
        out503_ = (d_1910_rawRSAKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1921_decryptionMaterialsIn_, _dafny.Seq([d_1920_edk_])))
        d_1924_valueOrError6_ = out503_
        if not(not((d_1924_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(60,31): " + _dafny.string_of(d_1924_valueOrError6_))
        d_1923_decryptionMaterialsOut_ = (d_1924_valueOrError6_).Extract()
        if not((((d_1923_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1916_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_1925_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1926_valueOrError0_: Wrappers.Result = None
        out504_: Wrappers.Result
        out504_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1926_valueOrError0_ = out504_
        if not(not((d_1926_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(78,12): " + _dafny.string_of(d_1926_valueOrError0_))
        d_1925_mpl_ = (d_1926_valueOrError0_).Extract()
        d_1927_namespace_: _dafny.Seq
        d_1928_name_: _dafny.Seq
        out505_: _dafny.Seq
        out506_: _dafny.Seq
        out505_, out506_ = TestUtils.default__.NamespaceAndName(0)
        d_1927_namespace_ = out505_
        d_1928_name_ = out506_
        d_1929_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out507_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out507_ = TestRawRSAKeying.default__.GenerateKeyPair(2048)
        d_1929_keys_ = out507_
        d_1930_rawRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1931_valueOrError1_: Wrappers.Result = None
        out508_: Wrappers.Result
        out508_ = (d_1925_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1927_namespace_, d_1928_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_1929_keys_).publicKey).pem), Wrappers.Option_Some(((d_1929_keys_).privateKey).pem)))
        d_1931_valueOrError1_ = out508_
        if not(not((d_1931_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(82,22): " + _dafny.string_of(d_1931_valueOrError1_))
        d_1930_rawRSAKeyring_ = (d_1931_valueOrError1_).Extract()
        d_1932_mismatchedRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1933_valueOrError2_: Wrappers.Result = None
        out509_: Wrappers.Result
        out509_ = (d_1925_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1927_namespace_, _dafny.Seq("mismatched"), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_1929_keys_).publicKey).pem), Wrappers.Option_Some(((d_1929_keys_).privateKey).pem)))
        d_1933_valueOrError2_ = out509_
        if not(not((d_1933_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(90,29): " + _dafny.string_of(d_1933_valueOrError2_))
        d_1932_mismatchedRSAKeyring_ = (d_1933_valueOrError2_).Extract()
        d_1934_encryptionContext_: _dafny.Map
        out510_: _dafny.Map
        out510_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1934_encryptionContext_ = out510_
        d_1935_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1935_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1936_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1937_valueOrError3_: Wrappers.Result = None
        d_1937_valueOrError3_ = (d_1925_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1935_algorithmSuiteId_, d_1934_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1937_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(103,30): " + _dafny.string_of(d_1937_valueOrError3_))
        d_1936_encryptionMaterialsIn_ = (d_1937_valueOrError3_).Extract()
        d_1938_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1939_valueOrError4_: Wrappers.Result = None
        out511_: Wrappers.Result
        out511_ = (d_1930_rawRSAKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1936_encryptionMaterialsIn_))
        d_1939_valueOrError4_ = out511_
        if not(not((d_1939_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(112,31): " + _dafny.string_of(d_1939_valueOrError4_))
        d_1938_encryptionMaterialsOut_ = (d_1939_valueOrError4_).Extract()
        d_1940___v1_: tuple
        d_1941_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1941_valueOrError5_ = (d_1925_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1938_encryptionMaterialsOut_).materials)
        if not(not((d_1941_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(115,10): " + _dafny.string_of(d_1941_valueOrError5_))
        d_1940___v1_ = (d_1941_valueOrError5_).Extract()
        d_1942_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1942_edk_ = (((d_1938_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1943_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1944_valueOrError6_: Wrappers.Result = None
        d_1944_valueOrError6_ = (d_1925_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1935_algorithmSuiteId_, d_1934_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1944_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(119,30): " + _dafny.string_of(d_1944_valueOrError6_))
        d_1943_decryptionMaterialsIn_ = (d_1944_valueOrError6_).Extract()
        d_1945_decryptionMaterialsOut_: Wrappers.Result
        out512_: Wrappers.Result
        out512_ = (d_1932_mismatchedRSAKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1943_decryptionMaterialsIn_, _dafny.Seq([d_1942_edk_])))
        d_1945_decryptionMaterialsOut_ = out512_
        if not((d_1945_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(133,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptFailure():
        d_1946_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1947_valueOrError0_: Wrappers.Result = None
        out513_: Wrappers.Result
        out513_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1947_valueOrError0_ = out513_
        if not(not((d_1947_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(139,12): " + _dafny.string_of(d_1947_valueOrError0_))
        d_1946_mpl_ = (d_1947_valueOrError0_).Extract()
        d_1948_namespace_: _dafny.Seq
        d_1949_name_: _dafny.Seq
        out514_: _dafny.Seq
        out515_: _dafny.Seq
        out514_, out515_ = TestUtils.default__.NamespaceAndName(0)
        d_1948_namespace_ = out514_
        d_1949_name_ = out515_
        d_1950_encryptKeys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out516_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out516_ = TestRawRSAKeying.default__.GenerateKeyPair(2048)
        d_1950_encryptKeys_ = out516_
        d_1951_decryptKeys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out517_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out517_ = TestRawRSAKeying.default__.GenerateKeyPair(2048)
        d_1951_decryptKeys_ = out517_
        d_1952_encryptKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1953_valueOrError1_: Wrappers.Result = None
        out518_: Wrappers.Result
        out518_ = (d_1946_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1948_namespace_, d_1949_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_1950_encryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_1950_encryptKeys_).privateKey).pem)))
        d_1953_valueOrError1_ = out518_
        if not(not((d_1953_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(147,23): " + _dafny.string_of(d_1953_valueOrError1_))
        d_1952_encryptKeyring_ = (d_1953_valueOrError1_).Extract()
        d_1954_decryptKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1955_valueOrError2_: Wrappers.Result = None
        out519_: Wrappers.Result
        out519_ = (d_1946_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1948_namespace_, d_1949_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_1951_decryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_1951_decryptKeys_).privateKey).pem)))
        d_1955_valueOrError2_ = out519_
        if not(not((d_1955_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(155,23): " + _dafny.string_of(d_1955_valueOrError2_))
        d_1954_decryptKeyring_ = (d_1955_valueOrError2_).Extract()
        d_1956_encryptionContext_: _dafny.Map
        out520_: _dafny.Map
        out520_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1956_encryptionContext_ = out520_
        d_1957_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1957_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1958_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1959_valueOrError3_: Wrappers.Result = None
        d_1959_valueOrError3_ = (d_1946_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1957_algorithmSuiteId_, d_1956_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1959_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(166,30): " + _dafny.string_of(d_1959_valueOrError3_))
        d_1958_encryptionMaterialsIn_ = (d_1959_valueOrError3_).Extract()
        d_1960_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1961_valueOrError4_: Wrappers.Result = None
        out521_: Wrappers.Result
        out521_ = (d_1952_encryptKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1958_encryptionMaterialsIn_))
        d_1961_valueOrError4_ = out521_
        if not(not((d_1961_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(175,31): " + _dafny.string_of(d_1961_valueOrError4_))
        d_1960_encryptionMaterialsOut_ = (d_1961_valueOrError4_).Extract()
        d_1962___v2_: tuple
        d_1963_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1963_valueOrError5_ = (d_1946_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1960_encryptionMaterialsOut_).materials)
        if not(not((d_1963_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(178,10): " + _dafny.string_of(d_1963_valueOrError5_))
        d_1962___v2_ = (d_1963_valueOrError5_).Extract()
        d_1964_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1964_edk_ = (((d_1960_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1965_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1966_valueOrError6_: Wrappers.Result = None
        d_1966_valueOrError6_ = (d_1946_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1957_algorithmSuiteId_, d_1956_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1966_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(182,30): " + _dafny.string_of(d_1966_valueOrError6_))
        d_1965_decryptionMaterialsIn_ = (d_1966_valueOrError6_).Extract()
        d_1967_decryptionMaterialsOut_: Wrappers.Result
        out522_: Wrappers.Result
        out522_ = (d_1954_decryptKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1965_decryptionMaterialsIn_, _dafny.Seq([d_1964_edk_])))
        d_1967_decryptionMaterialsOut_ = out522_
        if not((d_1967_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(200,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_1968_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1969_valueOrError0_: Wrappers.Result = None
        out523_: Wrappers.Result
        out523_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1969_valueOrError0_ = out523_
        if not(not((d_1969_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(212,12): " + _dafny.string_of(d_1969_valueOrError0_))
        d_1968_mpl_ = (d_1969_valueOrError0_).Extract()
        d_1970_namespace_: _dafny.Seq
        d_1971_name_: _dafny.Seq
        out524_: _dafny.Seq
        out525_: _dafny.Seq
        out524_, out525_ = TestUtils.default__.NamespaceAndName(0)
        d_1970_namespace_ = out524_
        d_1971_name_ = out525_
        d_1972_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out526_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out526_ = TestRawRSAKeying.default__.GenerateKeyPair(2048)
        d_1972_keys_ = out526_
        d_1973_rawRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1974_valueOrError1_: Wrappers.Result = None
        out527_: Wrappers.Result
        out527_ = (d_1968_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1970_namespace_, d_1971_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_1972_keys_).publicKey).pem), Wrappers.Option_Some(((d_1972_keys_).privateKey).pem)))
        d_1974_valueOrError1_ = out527_
        if not(not((d_1974_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(216,22): " + _dafny.string_of(d_1974_valueOrError1_))
        d_1973_rawRSAKeyring_ = (d_1974_valueOrError1_).Extract()
        d_1975_encryptionContext_: _dafny.Map
        out528_: _dafny.Map
        out528_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1975_encryptionContext_ = out528_
        d_1976_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1976_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1977_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1978_valueOrError2_: Wrappers.Result = None
        d_1978_valueOrError2_ = (d_1968_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1976_algorithmSuiteId_, d_1975_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1978_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(229,30): " + _dafny.string_of(d_1978_valueOrError2_))
        d_1977_encryptionMaterialsIn_ = (d_1978_valueOrError2_).Extract()
        d_1979_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1980_valueOrError3_: Wrappers.Result = None
        out529_: Wrappers.Result
        out529_ = (d_1973_rawRSAKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1977_encryptionMaterialsIn_))
        d_1980_valueOrError3_ = out529_
        if not(not((d_1980_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(238,31): " + _dafny.string_of(d_1980_valueOrError3_))
        d_1979_encryptionMaterialsOut_ = (d_1980_valueOrError3_).Extract()
        d_1981___v3_: tuple
        d_1982_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1982_valueOrError4_ = (d_1968_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1979_encryptionMaterialsOut_).materials)
        if not(not((d_1982_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(241,10): " + _dafny.string_of(d_1982_valueOrError4_))
        d_1981___v3_ = (d_1982_valueOrError4_).Extract()
        d_1983_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1983_edk_ = (((d_1979_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1984_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1985_valueOrError5_: Wrappers.Result = None
        d_1985_valueOrError5_ = (d_1968_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1976_algorithmSuiteId_, d_1975_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1985_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(245,30): " + _dafny.string_of(d_1985_valueOrError5_))
        d_1984_decryptionMaterialsIn_ = (d_1985_valueOrError5_).Extract()
        d_1986_fakeEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1986_fakeEdk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((d_1983_edk_).keyProviderId, (d_1983_edk_).keyProviderInfo, _dafny.Seq([0 for d_1987_i_ in range(len((d_1983_edk_).ciphertext))]))
        d_1988_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1989_valueOrError6_: Wrappers.Result = None
        out530_: Wrappers.Result
        out530_ = (d_1973_rawRSAKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1984_decryptionMaterialsIn_, _dafny.Seq([d_1986_fakeEdk_, d_1983_edk_])))
        d_1989_valueOrError6_ = out530_
        if not(not((d_1989_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(262,31): " + _dafny.string_of(d_1989_valueOrError6_))
        d_1988_decryptionMaterialsOut_ = (d_1989_valueOrError6_).Extract()
        if not((((d_1988_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1979_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(273,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GenerateKeyPair(keyModulusLength):
        keys: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput = None
        d_1990_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1991_valueOrError0_: Wrappers.Result = None
        out531_: Wrappers.Result
        out531_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1991_valueOrError0_ = out531_
        if not(not((d_1991_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(280,15): " + _dafny.string_of(d_1991_valueOrError0_))
        d_1990_crypto_ = (d_1991_valueOrError0_).Extract()
        d_1992_valueOrError1_: Wrappers.Result = None
        out532_: Wrappers.Result
        out532_ = (d_1990_crypto_).GenerateRSAKeyPair(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(keyModulusLength))
        d_1992_valueOrError1_ = out532_
        if not(not((d_1992_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(282,9): " + _dafny.string_of(d_1992_valueOrError1_))
        keys = (d_1992_valueOrError1_).Extract()
        return keys

