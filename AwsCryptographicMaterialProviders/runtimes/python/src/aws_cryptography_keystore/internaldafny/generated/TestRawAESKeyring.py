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

assert "TestRawAESKeyring" == __name__
TestRawAESKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptGenerateDataKey():
        d_1672_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1673_valueOrError0_: Wrappers.Result = None
        out385_: Wrappers.Result
        out385_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1673_valueOrError0_ = out385_
        if not(not((d_1673_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(21,12): " + _dafny.string_of(d_1673_valueOrError0_))
        d_1672_mpl_ = (d_1673_valueOrError0_).Extract()
        d_1674_namespace_: _dafny.Seq
        d_1675_name_: _dafny.Seq
        out386_: _dafny.Seq
        out387_: _dafny.Seq
        out386_, out387_ = TestUtils.default__.NamespaceAndName(0)
        d_1674_namespace_ = out386_
        d_1675_name_ = out387_
        d_1676_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1677_valueOrError1_: Wrappers.Result = None
        out388_: Wrappers.Result
        out388_ = (d_1672_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1674_namespace_, d_1675_name_, _dafny.Seq([0 for d_1678_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1677_valueOrError1_ = out388_
        if not(not((d_1677_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(24,22): " + _dafny.string_of(d_1677_valueOrError1_))
        d_1676_rawAESKeyring_ = (d_1677_valueOrError1_).Extract()
        d_1679_encryptionContext_: _dafny.Map
        out389_: _dafny.Map
        out389_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1679_encryptionContext_ = out389_
        d_1680_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1680_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1681_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1682_valueOrError2_: Wrappers.Result = None
        d_1682_valueOrError2_ = (d_1672_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1680_algorithmSuiteId_, d_1679_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1682_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(33,30): " + _dafny.string_of(d_1682_valueOrError2_))
        d_1681_encryptionMaterialsIn_ = (d_1682_valueOrError2_).Extract()
        d_1683_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1684_valueOrError3_: Wrappers.Result = None
        out390_: Wrappers.Result
        out390_ = (d_1676_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1681_encryptionMaterialsIn_))
        d_1684_valueOrError3_ = out390_
        if not(not((d_1684_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(43,31): " + _dafny.string_of(d_1684_valueOrError3_))
        d_1683_encryptionMaterialsOut_ = (d_1684_valueOrError3_).Extract()
        d_1685___v0_: tuple
        d_1686_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1686_valueOrError4_ = (d_1672_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1683_encryptionMaterialsOut_).materials)
        if not(not((d_1686_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(58,10): " + _dafny.string_of(d_1686_valueOrError4_))
        d_1685___v0_ = (d_1686_valueOrError4_).Extract()
        if not((len(((d_1683_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1687_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1687_edk_ = (((d_1683_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1688_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1689_valueOrError5_: Wrappers.Result = None
        d_1689_valueOrError5_ = (d_1672_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1680_algorithmSuiteId_, d_1679_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1689_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(69,30): " + _dafny.string_of(d_1689_valueOrError5_))
        d_1688_decryptionMaterialsIn_ = (d_1689_valueOrError5_).Extract()
        d_1690_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1691_valueOrError6_: Wrappers.Result = None
        out391_: Wrappers.Result
        out391_ = (d_1676_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1688_decryptionMaterialsIn_, _dafny.Seq([d_1687_edk_])))
        d_1691_valueOrError6_ = out391_
        if not(not((d_1691_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(76,31): " + _dafny.string_of(d_1691_valueOrError6_))
        d_1690_decryptionMaterialsOut_ = (d_1691_valueOrError6_).Extract()
        if not((((d_1683_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1683_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(88,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_1692_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1693_valueOrError0_: Wrappers.Result = None
        out392_: Wrappers.Result
        out392_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1693_valueOrError0_ = out392_
        if not(not((d_1693_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(95,12): " + _dafny.string_of(d_1693_valueOrError0_))
        d_1692_mpl_ = (d_1693_valueOrError0_).Extract()
        d_1694_namespace_: _dafny.Seq
        d_1695_name_: _dafny.Seq
        out393_: _dafny.Seq
        out394_: _dafny.Seq
        out393_, out394_ = TestUtils.default__.NamespaceAndName(0)
        d_1694_namespace_ = out393_
        d_1695_name_ = out394_
        d_1696_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1697_valueOrError1_: Wrappers.Result = None
        out395_: Wrappers.Result
        out395_ = (d_1692_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1694_namespace_, d_1695_name_, _dafny.Seq([0 for d_1698_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1697_valueOrError1_ = out395_
        if not(not((d_1697_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(98,22): " + _dafny.string_of(d_1697_valueOrError1_))
        d_1696_rawAESKeyring_ = (d_1697_valueOrError1_).Extract()
        d_1699_encryptionContext_: _dafny.Map
        out396_: _dafny.Map
        out396_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1699_encryptionContext_ = out396_
        d_1700_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1700_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1701_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1702_valueOrError2_: Wrappers.Result = None
        d_1702_valueOrError2_ = (d_1692_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1700_algorithmSuiteId_, d_1699_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1702_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(107,30): " + _dafny.string_of(d_1702_valueOrError2_))
        d_1701_encryptionMaterialsIn_ = (d_1702_valueOrError2_).Extract()
        d_1703_pdk_: _dafny.Seq
        d_1703_pdk_ = _dafny.Seq([0 for d_1704_i_ in range(32)])
        d_1705_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1706_valueOrError3_: Wrappers.Result = None
        pat_let_tv38_ = d_1703_pdk_
        def iife65_(_pat_let26_0):
            def iife66_(d_1707_dt__update__tmp_h0_):
                def iife67_(_pat_let27_0):
                    def iife68_(d_1708_dt__update_hplaintextDataKey_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((d_1707_dt__update__tmp_h0_).algorithmSuite, (d_1707_dt__update__tmp_h0_).encryptionContext, (d_1707_dt__update__tmp_h0_).encryptedDataKeys, (d_1707_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_1708_dt__update_hplaintextDataKey_h0_, (d_1707_dt__update__tmp_h0_).signingKey, (d_1707_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife68_(_pat_let27_0)
                return iife67_(Wrappers.Option_Some(pat_let_tv38_))
            return iife66_(_pat_let26_0)
        out397_: Wrappers.Result
        out397_ = (d_1696_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(iife65_(d_1701_encryptionMaterialsIn_)))
        d_1706_valueOrError3_ = out397_
        if not(not((d_1706_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(122,31): " + _dafny.string_of(d_1706_valueOrError3_))
        d_1705_encryptionMaterialsOut_ = (d_1706_valueOrError3_).Extract()
        d_1709___v1_: tuple
        d_1710_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1710_valueOrError4_ = (d_1692_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1705_encryptionMaterialsOut_).materials)
        if not(not((d_1710_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(126,10): " + _dafny.string_of(d_1710_valueOrError4_))
        d_1709___v1_ = (d_1710_valueOrError4_).Extract()
        d_1711_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1711_edk_ = (((d_1705_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1712_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1713_valueOrError5_: Wrappers.Result = None
        d_1713_valueOrError5_ = (d_1692_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1700_algorithmSuiteId_, d_1699_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1713_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(130,30): " + _dafny.string_of(d_1713_valueOrError5_))
        d_1712_decryptionMaterialsIn_ = (d_1713_valueOrError5_).Extract()
        d_1714_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1715_valueOrError6_: Wrappers.Result = None
        out398_: Wrappers.Result
        out398_ = (d_1696_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1712_decryptionMaterialsIn_, _dafny.Seq([d_1711_edk_])))
        d_1715_valueOrError6_ = out398_
        if not(not((d_1715_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(138,31): " + _dafny.string_of(d_1715_valueOrError6_))
        d_1714_decryptionMaterialsOut_ = (d_1715_valueOrError6_).Extract()
        if not((((d_1714_decryptionMaterialsOut_).materials).plaintextDataKey) == (Wrappers.Option_Some(d_1703_pdk_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_1716_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1717_valueOrError0_: Wrappers.Result = None
        out399_: Wrappers.Result
        out399_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1717_valueOrError0_ = out399_
        if not(not((d_1717_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(156,12): " + _dafny.string_of(d_1717_valueOrError0_))
        d_1716_mpl_ = (d_1717_valueOrError0_).Extract()
        d_1718_namespace_: _dafny.Seq
        d_1719_name_: _dafny.Seq
        out400_: _dafny.Seq
        out401_: _dafny.Seq
        out400_, out401_ = TestUtils.default__.NamespaceAndName(0)
        d_1718_namespace_ = out400_
        d_1719_name_ = out401_
        d_1720_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1721_valueOrError1_: Wrappers.Result = None
        out402_: Wrappers.Result
        out402_ = (d_1716_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1718_namespace_, d_1719_name_, _dafny.Seq([0 for d_1722_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1721_valueOrError1_ = out402_
        if not(not((d_1721_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(159,22): " + _dafny.string_of(d_1721_valueOrError1_))
        d_1720_rawAESKeyring_ = (d_1721_valueOrError1_).Extract()
        d_1723_mismatchedAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1724_valueOrError2_: Wrappers.Result = None
        out403_: Wrappers.Result
        out403_ = (d_1716_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1718_namespace_, _dafny.Seq("mismatched"), _dafny.Seq([1 for d_1725_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1724_valueOrError2_ = out403_
        if not(not((d_1724_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(166,29): " + _dafny.string_of(d_1724_valueOrError2_))
        d_1723_mismatchedAESKeyring_ = (d_1724_valueOrError2_).Extract()
        d_1726_encryptionContext_: _dafny.Map
        out404_: _dafny.Map
        out404_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1726_encryptionContext_ = out404_
        d_1727_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1727_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1728_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1729_valueOrError3_: Wrappers.Result = None
        d_1729_valueOrError3_ = (d_1716_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1727_algorithmSuiteId_, d_1726_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1729_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(176,30): " + _dafny.string_of(d_1729_valueOrError3_))
        d_1728_encryptionMaterialsIn_ = (d_1729_valueOrError3_).Extract()
        d_1730_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1731_valueOrError4_: Wrappers.Result = None
        out405_: Wrappers.Result
        out405_ = (d_1720_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1728_encryptionMaterialsIn_))
        d_1731_valueOrError4_ = out405_
        if not(not((d_1731_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(186,31): " + _dafny.string_of(d_1731_valueOrError4_))
        d_1730_encryptionMaterialsOut_ = (d_1731_valueOrError4_).Extract()
        d_1732___v2_: tuple
        d_1733_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1733_valueOrError5_ = (d_1716_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1730_encryptionMaterialsOut_).materials)
        if not(not((d_1733_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(190,10): " + _dafny.string_of(d_1733_valueOrError5_))
        d_1732___v2_ = (d_1733_valueOrError5_).Extract()
        d_1734_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1734_edk_ = (((d_1730_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1735_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1736_valueOrError6_: Wrappers.Result = None
        d_1736_valueOrError6_ = (d_1716_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1727_algorithmSuiteId_, d_1726_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1736_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(194,30): " + _dafny.string_of(d_1736_valueOrError6_))
        d_1735_decryptionMaterialsIn_ = (d_1736_valueOrError6_).Extract()
        d_1737_decryptionMaterialsOut_: Wrappers.Result
        out406_: Wrappers.Result
        out406_ = (d_1723_mismatchedAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1735_decryptionMaterialsIn_, _dafny.Seq([d_1734_edk_])))
        d_1737_decryptionMaterialsOut_ = out406_
        if not((d_1737_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_1738_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1739_valueOrError0_: Wrappers.Result = None
        out407_: Wrappers.Result
        out407_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1739_valueOrError0_ = out407_
        if not(not((d_1739_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(213,12): " + _dafny.string_of(d_1739_valueOrError0_))
        d_1738_mpl_ = (d_1739_valueOrError0_).Extract()
        d_1740_namespace_: _dafny.Seq
        d_1741_name_: _dafny.Seq
        out408_: _dafny.Seq
        out409_: _dafny.Seq
        out408_, out409_ = TestUtils.default__.NamespaceAndName(0)
        d_1740_namespace_ = out408_
        d_1741_name_ = out409_
        d_1742_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1743_valueOrError1_: Wrappers.Result = None
        out410_: Wrappers.Result
        out410_ = (d_1738_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1740_namespace_, d_1741_name_, _dafny.Seq([0 for d_1744_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1743_valueOrError1_ = out410_
        if not(not((d_1743_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(216,22): " + _dafny.string_of(d_1743_valueOrError1_))
        d_1742_rawAESKeyring_ = (d_1743_valueOrError1_).Extract()
        d_1745_encryptionContext_: _dafny.Map
        out411_: _dafny.Map
        out411_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1745_encryptionContext_ = out411_
        d_1746_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1746_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1747_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1748_valueOrError2_: Wrappers.Result = None
        d_1748_valueOrError2_ = (d_1738_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1746_algorithmSuiteId_, d_1745_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1748_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(225,30): " + _dafny.string_of(d_1748_valueOrError2_))
        d_1747_encryptionMaterialsIn_ = (d_1748_valueOrError2_).Extract()
        d_1749_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1750_valueOrError3_: Wrappers.Result = None
        out412_: Wrappers.Result
        out412_ = (d_1742_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1747_encryptionMaterialsIn_))
        d_1750_valueOrError3_ = out412_
        if not(not((d_1750_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(235,31): " + _dafny.string_of(d_1750_valueOrError3_))
        d_1749_encryptionMaterialsOut_ = (d_1750_valueOrError3_).Extract()
        d_1751___v3_: tuple
        d_1752_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1752_valueOrError4_ = (d_1738_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1749_encryptionMaterialsOut_).materials)
        if not(not((d_1752_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(239,10): " + _dafny.string_of(d_1752_valueOrError4_))
        d_1751___v3_ = (d_1752_valueOrError4_).Extract()
        d_1753_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1753_edk_ = (((d_1749_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1754_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1755_valueOrError5_: Wrappers.Result = None
        d_1755_valueOrError5_ = (d_1738_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1746_algorithmSuiteId_, d_1745_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1755_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(243,30): " + _dafny.string_of(d_1755_valueOrError5_))
        d_1754_decryptionMaterialsIn_ = (d_1755_valueOrError5_).Extract()
        d_1756_fakeEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1756_fakeEdk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((d_1753_edk_).keyProviderId, (d_1753_edk_).keyProviderInfo, _dafny.Seq([0 for d_1757_i_ in range(len((d_1753_edk_).ciphertext))]))
        d_1758_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1759_valueOrError6_: Wrappers.Result = None
        out413_: Wrappers.Result
        out413_ = (d_1742_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1754_decryptionMaterialsIn_, _dafny.Seq([d_1756_fakeEdk_, d_1753_edk_])))
        d_1759_valueOrError6_ = out413_
        if not(not((d_1759_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(256,31): " + _dafny.string_of(d_1759_valueOrError6_))
        d_1758_decryptionMaterialsOut_ = (d_1759_valueOrError6_).Extract()
        if not((((d_1758_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1749_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(263,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptNoEDKs():
        d_1760_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1761_valueOrError0_: Wrappers.Result = None
        out414_: Wrappers.Result
        out414_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1761_valueOrError0_ = out414_
        if not(not((d_1761_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(269,12): " + _dafny.string_of(d_1761_valueOrError0_))
        d_1760_mpl_ = (d_1761_valueOrError0_).Extract()
        d_1762_namespace_: _dafny.Seq
        d_1763_name_: _dafny.Seq
        out415_: _dafny.Seq
        out416_: _dafny.Seq
        out415_, out416_ = TestUtils.default__.NamespaceAndName(0)
        d_1762_namespace_ = out415_
        d_1763_name_ = out416_
        d_1764_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1765_valueOrError1_: Wrappers.Result = None
        out417_: Wrappers.Result
        out417_ = (d_1760_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1762_namespace_, d_1763_name_, _dafny.Seq([0 for d_1766_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1765_valueOrError1_ = out417_
        if not(not((d_1765_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(272,22): " + _dafny.string_of(d_1765_valueOrError1_))
        d_1764_rawAESKeyring_ = (d_1765_valueOrError1_).Extract()
        d_1767_encryptionContext_: _dafny.Map
        out418_: _dafny.Map
        out418_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1767_encryptionContext_ = out418_
        d_1768_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1768_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1769_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1770_valueOrError2_: Wrappers.Result = None
        d_1770_valueOrError2_ = (d_1760_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1768_algorithmSuiteId_, d_1767_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1770_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(281,30): " + _dafny.string_of(d_1770_valueOrError2_))
        d_1769_decryptionMaterialsIn_ = (d_1770_valueOrError2_).Extract()
        d_1771_decryptionMaterialsOut_: Wrappers.Result
        out419_: Wrappers.Result
        out419_ = (d_1764_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1769_decryptionMaterialsIn_, _dafny.Seq([])))
        d_1771_decryptionMaterialsOut_ = out419_
        if not((d_1771_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(294,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptUnserializableEC():
        d_1772_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1773_valueOrError0_: Wrappers.Result = None
        out420_: Wrappers.Result
        out420_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1773_valueOrError0_ = out420_
        if not(not((d_1773_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(303,12): " + _dafny.string_of(d_1773_valueOrError0_))
        d_1772_mpl_ = (d_1773_valueOrError0_).Extract()
        d_1774_namespace_: _dafny.Seq
        d_1775_name_: _dafny.Seq
        out421_: _dafny.Seq
        out422_: _dafny.Seq
        out421_, out422_ = TestUtils.default__.NamespaceAndName(0)
        d_1774_namespace_ = out421_
        d_1775_name_ = out422_
        d_1776_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1777_valueOrError1_: Wrappers.Result = None
        out423_: Wrappers.Result
        out423_ = (d_1772_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1774_namespace_, d_1775_name_, _dafny.Seq([0 for d_1778_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1777_valueOrError1_ = out423_
        if not(not((d_1777_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(306,22): " + _dafny.string_of(d_1777_valueOrError1_))
        d_1776_rawAESKeyring_ = (d_1777_valueOrError1_).Extract()
        d_1779_unserializableEncryptionContext_: _dafny.Map
        out424_: _dafny.Map
        out424_ = TestRawAESKeyring.default__.generateUnserializableEncryptionContext()
        d_1779_unserializableEncryptionContext_ = out424_
        d_1780_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1780_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1781_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1782_valueOrError2_: Wrappers.Result = None
        d_1782_valueOrError2_ = (d_1772_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1780_algorithmSuiteId_, d_1779_unserializableEncryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1782_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(315,30): " + _dafny.string_of(d_1782_valueOrError2_))
        d_1781_encryptionMaterialsIn_ = (d_1782_valueOrError2_).Extract()
        d_1783_encryptionMaterialsOut_: Wrappers.Result
        out425_: Wrappers.Result
        out425_ = (d_1776_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1781_encryptionMaterialsIn_))
        d_1783_encryptionMaterialsOut_ = out425_
        if not((d_1783_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(327,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptUnserializableEC():
        d_1784_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1785_valueOrError0_: Wrappers.Result = None
        out426_: Wrappers.Result
        out426_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1785_valueOrError0_ = out426_
        if not(not((d_1785_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(337,12): " + _dafny.string_of(d_1785_valueOrError0_))
        d_1784_mpl_ = (d_1785_valueOrError0_).Extract()
        d_1786_namespace_: _dafny.Seq
        d_1787_name_: _dafny.Seq
        out427_: _dafny.Seq
        out428_: _dafny.Seq
        out427_, out428_ = TestUtils.default__.NamespaceAndName(0)
        d_1786_namespace_ = out427_
        d_1787_name_ = out428_
        d_1788_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1789_valueOrError1_: Wrappers.Result = None
        out429_: Wrappers.Result
        out429_ = (d_1784_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1786_namespace_, d_1787_name_, _dafny.Seq([0 for d_1790_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1789_valueOrError1_ = out429_
        if not(not((d_1789_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(340,22): " + _dafny.string_of(d_1789_valueOrError1_))
        d_1788_rawAESKeyring_ = (d_1789_valueOrError1_).Extract()
        d_1791_encryptionContext_: _dafny.Map
        out430_: _dafny.Map
        out430_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1791_encryptionContext_ = out430_
        d_1792_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1792_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1793_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1794_valueOrError2_: Wrappers.Result = None
        d_1794_valueOrError2_ = (d_1784_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1792_algorithmSuiteId_, d_1791_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1794_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(349,30): " + _dafny.string_of(d_1794_valueOrError2_))
        d_1793_encryptionMaterialsIn_ = (d_1794_valueOrError2_).Extract()
        d_1795_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1796_valueOrError3_: Wrappers.Result = None
        out431_: Wrappers.Result
        out431_ = (d_1788_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1793_encryptionMaterialsIn_))
        d_1796_valueOrError3_ = out431_
        if not(not((d_1796_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(359,31): " + _dafny.string_of(d_1796_valueOrError3_))
        d_1795_encryptionMaterialsOut_ = (d_1796_valueOrError3_).Extract()
        d_1797___v4_: tuple
        d_1798_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1798_valueOrError4_ = (d_1784_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1795_encryptionMaterialsOut_).materials)
        if not(not((d_1798_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(362,10): " + _dafny.string_of(d_1798_valueOrError4_))
        d_1797___v4_ = (d_1798_valueOrError4_).Extract()
        d_1799_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1799_edk_ = (((d_1795_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1800_unserializableEncryptionContext_: _dafny.Map
        out432_: _dafny.Map
        out432_ = TestRawAESKeyring.default__.generateUnserializableEncryptionContext()
        d_1800_unserializableEncryptionContext_ = out432_
        d_1801_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1802_valueOrError5_: Wrappers.Result = None
        d_1802_valueOrError5_ = (d_1784_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1792_algorithmSuiteId_, d_1800_unserializableEncryptionContext_, _dafny.Seq([])))
        if not(not((d_1802_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(367,30): " + _dafny.string_of(d_1802_valueOrError5_))
        d_1801_decryptionMaterialsIn_ = (d_1802_valueOrError5_).Extract()
        d_1803_decryptionMaterialsOut_: Wrappers.Result
        out433_: Wrappers.Result
        out433_ = (d_1788_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1801_decryptionMaterialsIn_, _dafny.Seq([d_1799_edk_])))
        d_1803_decryptionMaterialsOut_ = out433_
        if not((d_1803_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(380,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def generateUnserializableEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_1804_keyA_: _dafny.Seq
        d_1805_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1805_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_1805_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(385,13): " + _dafny.string_of(d_1805_valueOrError0_))
        d_1804_keyA_ = (d_1805_valueOrError0_).Extract()
        d_1806_invalidVal_: _dafny.Seq
        d_1806_invalidVal_ = _dafny.Seq([0 for d_1807___v5_ in range(65536)])
        encCtx = _dafny.Map({d_1804_keyA_: d_1806_invalidVal_})
        return encCtx
        return encCtx

