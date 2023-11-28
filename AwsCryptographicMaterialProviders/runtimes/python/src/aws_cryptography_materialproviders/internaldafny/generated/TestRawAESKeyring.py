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
        d_1674_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1675_valueOrError0_: Wrappers.Result = None
        out385_: Wrappers.Result
        out385_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1675_valueOrError0_ = out385_
        if not(not((d_1675_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(21,12): " + _dafny.string_of(d_1675_valueOrError0_))
        d_1674_mpl_ = (d_1675_valueOrError0_).Extract()
        d_1676_namespace_: _dafny.Seq
        d_1677_name_: _dafny.Seq
        out386_: _dafny.Seq
        out387_: _dafny.Seq
        out386_, out387_ = TestUtils.default__.NamespaceAndName(0)
        d_1676_namespace_ = out386_
        d_1677_name_ = out387_
        d_1678_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1679_valueOrError1_: Wrappers.Result = None
        out388_: Wrappers.Result
        out388_ = (d_1674_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1676_namespace_, d_1677_name_, _dafny.Seq([0 for d_1680_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1679_valueOrError1_ = out388_
        if not(not((d_1679_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(24,22): " + _dafny.string_of(d_1679_valueOrError1_))
        d_1678_rawAESKeyring_ = (d_1679_valueOrError1_).Extract()
        d_1681_encryptionContext_: _dafny.Map
        out389_: _dafny.Map
        out389_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1681_encryptionContext_ = out389_
        d_1682_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1682_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1683_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1684_valueOrError2_: Wrappers.Result = None
        d_1684_valueOrError2_ = (d_1674_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1682_algorithmSuiteId_, d_1681_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1684_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(33,30): " + _dafny.string_of(d_1684_valueOrError2_))
        d_1683_encryptionMaterialsIn_ = (d_1684_valueOrError2_).Extract()
        d_1685_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1686_valueOrError3_: Wrappers.Result = None
        out390_: Wrappers.Result
        out390_ = (d_1678_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1683_encryptionMaterialsIn_))
        d_1686_valueOrError3_ = out390_
        if not(not((d_1686_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(43,31): " + _dafny.string_of(d_1686_valueOrError3_))
        d_1685_encryptionMaterialsOut_ = (d_1686_valueOrError3_).Extract()
        d_1687___v0_: tuple
        d_1688_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1688_valueOrError4_ = (d_1674_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1685_encryptionMaterialsOut_).materials)
        if not(not((d_1688_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(58,10): " + _dafny.string_of(d_1688_valueOrError4_))
        d_1687___v0_ = (d_1688_valueOrError4_).Extract()
        if not((len(((d_1685_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1689_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1689_edk_ = (((d_1685_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1690_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1691_valueOrError5_: Wrappers.Result = None
        d_1691_valueOrError5_ = (d_1674_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1682_algorithmSuiteId_, d_1681_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1691_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(69,30): " + _dafny.string_of(d_1691_valueOrError5_))
        d_1690_decryptionMaterialsIn_ = (d_1691_valueOrError5_).Extract()
        d_1692_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1693_valueOrError6_: Wrappers.Result = None
        out391_: Wrappers.Result
        out391_ = (d_1678_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1690_decryptionMaterialsIn_, _dafny.Seq([d_1689_edk_])))
        d_1693_valueOrError6_ = out391_
        if not(not((d_1693_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(76,31): " + _dafny.string_of(d_1693_valueOrError6_))
        d_1692_decryptionMaterialsOut_ = (d_1693_valueOrError6_).Extract()
        if not((((d_1685_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1685_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_1694_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1695_valueOrError0_: Wrappers.Result = None
        out392_: Wrappers.Result
        out392_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1695_valueOrError0_ = out392_
        if not(not((d_1695_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(94,12): " + _dafny.string_of(d_1695_valueOrError0_))
        d_1694_mpl_ = (d_1695_valueOrError0_).Extract()
        d_1696_namespace_: _dafny.Seq
        d_1697_name_: _dafny.Seq
        out393_: _dafny.Seq
        out394_: _dafny.Seq
        out393_, out394_ = TestUtils.default__.NamespaceAndName(0)
        d_1696_namespace_ = out393_
        d_1697_name_ = out394_
        d_1698_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1699_valueOrError1_: Wrappers.Result = None
        out395_: Wrappers.Result
        out395_ = (d_1694_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1696_namespace_, d_1697_name_, _dafny.Seq([0 for d_1700_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1699_valueOrError1_ = out395_
        if not(not((d_1699_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(97,22): " + _dafny.string_of(d_1699_valueOrError1_))
        d_1698_rawAESKeyring_ = (d_1699_valueOrError1_).Extract()
        d_1701_encryptionContext_: _dafny.Map
        out396_: _dafny.Map
        out396_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1701_encryptionContext_ = out396_
        d_1702_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1702_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1703_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1704_valueOrError2_: Wrappers.Result = None
        d_1704_valueOrError2_ = (d_1694_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1702_algorithmSuiteId_, d_1701_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1704_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(106,30): " + _dafny.string_of(d_1704_valueOrError2_))
        d_1703_encryptionMaterialsIn_ = (d_1704_valueOrError2_).Extract()
        d_1705_pdk_: _dafny.Seq
        d_1705_pdk_ = _dafny.Seq([0 for d_1706_i_ in range(32)])
        d_1707_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1708_valueOrError3_: Wrappers.Result = None
        pat_let_tv39_ = d_1705_pdk_
        def iife69_(_pat_let28_0):
            def iife70_(d_1709_dt__update__tmp_h0_):
                def iife71_(_pat_let29_0):
                    def iife72_(d_1710_dt__update_hplaintextDataKey_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((d_1709_dt__update__tmp_h0_).algorithmSuite, (d_1709_dt__update__tmp_h0_).encryptionContext, (d_1709_dt__update__tmp_h0_).encryptedDataKeys, (d_1709_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_1710_dt__update_hplaintextDataKey_h0_, (d_1709_dt__update__tmp_h0_).signingKey, (d_1709_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife72_(_pat_let29_0)
                return iife71_(Wrappers.Option_Some(pat_let_tv39_))
            return iife70_(_pat_let28_0)
        out397_: Wrappers.Result
        out397_ = (d_1698_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(iife69_(d_1703_encryptionMaterialsIn_)))
        d_1708_valueOrError3_ = out397_
        if not(not((d_1708_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(121,31): " + _dafny.string_of(d_1708_valueOrError3_))
        d_1707_encryptionMaterialsOut_ = (d_1708_valueOrError3_).Extract()
        d_1711___v1_: tuple
        d_1712_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1712_valueOrError4_ = (d_1694_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1707_encryptionMaterialsOut_).materials)
        if not(not((d_1712_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(125,10): " + _dafny.string_of(d_1712_valueOrError4_))
        d_1711___v1_ = (d_1712_valueOrError4_).Extract()
        d_1713_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1713_edk_ = (((d_1707_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1714_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1715_valueOrError5_: Wrappers.Result = None
        d_1715_valueOrError5_ = (d_1694_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1702_algorithmSuiteId_, d_1701_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1715_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(129,30): " + _dafny.string_of(d_1715_valueOrError5_))
        d_1714_decryptionMaterialsIn_ = (d_1715_valueOrError5_).Extract()
        d_1716_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1717_valueOrError6_: Wrappers.Result = None
        out398_: Wrappers.Result
        out398_ = (d_1698_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1714_decryptionMaterialsIn_, _dafny.Seq([d_1713_edk_])))
        d_1717_valueOrError6_ = out398_
        if not(not((d_1717_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(137,31): " + _dafny.string_of(d_1717_valueOrError6_))
        d_1716_decryptionMaterialsOut_ = (d_1717_valueOrError6_).Extract()
        if not((((d_1716_decryptionMaterialsOut_).materials).plaintextDataKey) == (Wrappers.Option_Some(d_1705_pdk_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_1718_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1719_valueOrError0_: Wrappers.Result = None
        out399_: Wrappers.Result
        out399_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1719_valueOrError0_ = out399_
        if not(not((d_1719_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(155,12): " + _dafny.string_of(d_1719_valueOrError0_))
        d_1718_mpl_ = (d_1719_valueOrError0_).Extract()
        d_1720_namespace_: _dafny.Seq
        d_1721_name_: _dafny.Seq
        out400_: _dafny.Seq
        out401_: _dafny.Seq
        out400_, out401_ = TestUtils.default__.NamespaceAndName(0)
        d_1720_namespace_ = out400_
        d_1721_name_ = out401_
        d_1722_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1723_valueOrError1_: Wrappers.Result = None
        out402_: Wrappers.Result
        out402_ = (d_1718_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1720_namespace_, d_1721_name_, _dafny.Seq([0 for d_1724_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1723_valueOrError1_ = out402_
        if not(not((d_1723_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(158,22): " + _dafny.string_of(d_1723_valueOrError1_))
        d_1722_rawAESKeyring_ = (d_1723_valueOrError1_).Extract()
        d_1725_mismatchedAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1726_valueOrError2_: Wrappers.Result = None
        out403_: Wrappers.Result
        out403_ = (d_1718_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1720_namespace_, _dafny.Seq("mismatched"), _dafny.Seq([1 for d_1727_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1726_valueOrError2_ = out403_
        if not(not((d_1726_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(165,29): " + _dafny.string_of(d_1726_valueOrError2_))
        d_1725_mismatchedAESKeyring_ = (d_1726_valueOrError2_).Extract()
        d_1728_encryptionContext_: _dafny.Map
        out404_: _dafny.Map
        out404_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1728_encryptionContext_ = out404_
        d_1729_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1729_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1730_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1731_valueOrError3_: Wrappers.Result = None
        d_1731_valueOrError3_ = (d_1718_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1729_algorithmSuiteId_, d_1728_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1731_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(175,30): " + _dafny.string_of(d_1731_valueOrError3_))
        d_1730_encryptionMaterialsIn_ = (d_1731_valueOrError3_).Extract()
        d_1732_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1733_valueOrError4_: Wrappers.Result = None
        out405_: Wrappers.Result
        out405_ = (d_1722_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1730_encryptionMaterialsIn_))
        d_1733_valueOrError4_ = out405_
        if not(not((d_1733_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(185,31): " + _dafny.string_of(d_1733_valueOrError4_))
        d_1732_encryptionMaterialsOut_ = (d_1733_valueOrError4_).Extract()
        d_1734___v2_: tuple
        d_1735_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1735_valueOrError5_ = (d_1718_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1732_encryptionMaterialsOut_).materials)
        if not(not((d_1735_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(189,10): " + _dafny.string_of(d_1735_valueOrError5_))
        d_1734___v2_ = (d_1735_valueOrError5_).Extract()
        d_1736_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1736_edk_ = (((d_1732_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1737_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1738_valueOrError6_: Wrappers.Result = None
        d_1738_valueOrError6_ = (d_1718_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1729_algorithmSuiteId_, d_1728_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1738_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(193,30): " + _dafny.string_of(d_1738_valueOrError6_))
        d_1737_decryptionMaterialsIn_ = (d_1738_valueOrError6_).Extract()
        d_1739_decryptionMaterialsOut_: Wrappers.Result
        out406_: Wrappers.Result
        out406_ = (d_1725_mismatchedAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1737_decryptionMaterialsIn_, _dafny.Seq([d_1736_edk_])))
        d_1739_decryptionMaterialsOut_ = out406_
        if not((d_1739_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_1740_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1741_valueOrError0_: Wrappers.Result = None
        out407_: Wrappers.Result
        out407_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1741_valueOrError0_ = out407_
        if not(not((d_1741_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(212,12): " + _dafny.string_of(d_1741_valueOrError0_))
        d_1740_mpl_ = (d_1741_valueOrError0_).Extract()
        d_1742_namespace_: _dafny.Seq
        d_1743_name_: _dafny.Seq
        out408_: _dafny.Seq
        out409_: _dafny.Seq
        out408_, out409_ = TestUtils.default__.NamespaceAndName(0)
        d_1742_namespace_ = out408_
        d_1743_name_ = out409_
        d_1744_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1745_valueOrError1_: Wrappers.Result = None
        out410_: Wrappers.Result
        out410_ = (d_1740_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1742_namespace_, d_1743_name_, _dafny.Seq([0 for d_1746_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1745_valueOrError1_ = out410_
        if not(not((d_1745_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,22): " + _dafny.string_of(d_1745_valueOrError1_))
        d_1744_rawAESKeyring_ = (d_1745_valueOrError1_).Extract()
        d_1747_encryptionContext_: _dafny.Map
        out411_: _dafny.Map
        out411_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1747_encryptionContext_ = out411_
        d_1748_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1748_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1749_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1750_valueOrError2_: Wrappers.Result = None
        d_1750_valueOrError2_ = (d_1740_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1748_algorithmSuiteId_, d_1747_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1750_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(224,30): " + _dafny.string_of(d_1750_valueOrError2_))
        d_1749_encryptionMaterialsIn_ = (d_1750_valueOrError2_).Extract()
        d_1751_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1752_valueOrError3_: Wrappers.Result = None
        out412_: Wrappers.Result
        out412_ = (d_1744_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1749_encryptionMaterialsIn_))
        d_1752_valueOrError3_ = out412_
        if not(not((d_1752_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(234,31): " + _dafny.string_of(d_1752_valueOrError3_))
        d_1751_encryptionMaterialsOut_ = (d_1752_valueOrError3_).Extract()
        d_1753___v3_: tuple
        d_1754_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1754_valueOrError4_ = (d_1740_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1751_encryptionMaterialsOut_).materials)
        if not(not((d_1754_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(238,10): " + _dafny.string_of(d_1754_valueOrError4_))
        d_1753___v3_ = (d_1754_valueOrError4_).Extract()
        d_1755_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1755_edk_ = (((d_1751_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1756_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1757_valueOrError5_: Wrappers.Result = None
        d_1757_valueOrError5_ = (d_1740_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1748_algorithmSuiteId_, d_1747_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1757_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(242,30): " + _dafny.string_of(d_1757_valueOrError5_))
        d_1756_decryptionMaterialsIn_ = (d_1757_valueOrError5_).Extract()
        d_1758_fakeEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1758_fakeEdk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((d_1755_edk_).keyProviderId, (d_1755_edk_).keyProviderInfo, _dafny.Seq([0 for d_1759_i_ in range(len((d_1755_edk_).ciphertext))]))
        d_1760_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1761_valueOrError6_: Wrappers.Result = None
        out413_: Wrappers.Result
        out413_ = (d_1744_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1756_decryptionMaterialsIn_, _dafny.Seq([d_1758_fakeEdk_, d_1755_edk_])))
        d_1761_valueOrError6_ = out413_
        if not(not((d_1761_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(255,31): " + _dafny.string_of(d_1761_valueOrError6_))
        d_1760_decryptionMaterialsOut_ = (d_1761_valueOrError6_).Extract()
        if not((((d_1760_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1751_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(262,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptNoEDKs():
        d_1762_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1763_valueOrError0_: Wrappers.Result = None
        out414_: Wrappers.Result
        out414_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1763_valueOrError0_ = out414_
        if not(not((d_1763_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(268,12): " + _dafny.string_of(d_1763_valueOrError0_))
        d_1762_mpl_ = (d_1763_valueOrError0_).Extract()
        d_1764_namespace_: _dafny.Seq
        d_1765_name_: _dafny.Seq
        out415_: _dafny.Seq
        out416_: _dafny.Seq
        out415_, out416_ = TestUtils.default__.NamespaceAndName(0)
        d_1764_namespace_ = out415_
        d_1765_name_ = out416_
        d_1766_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1767_valueOrError1_: Wrappers.Result = None
        out417_: Wrappers.Result
        out417_ = (d_1762_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1764_namespace_, d_1765_name_, _dafny.Seq([0 for d_1768_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1767_valueOrError1_ = out417_
        if not(not((d_1767_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,22): " + _dafny.string_of(d_1767_valueOrError1_))
        d_1766_rawAESKeyring_ = (d_1767_valueOrError1_).Extract()
        d_1769_encryptionContext_: _dafny.Map
        out418_: _dafny.Map
        out418_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1769_encryptionContext_ = out418_
        d_1770_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1770_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1771_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1772_valueOrError2_: Wrappers.Result = None
        d_1772_valueOrError2_ = (d_1762_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1770_algorithmSuiteId_, d_1769_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1772_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(280,30): " + _dafny.string_of(d_1772_valueOrError2_))
        d_1771_decryptionMaterialsIn_ = (d_1772_valueOrError2_).Extract()
        d_1773_decryptionMaterialsOut_: Wrappers.Result
        out419_: Wrappers.Result
        out419_ = (d_1766_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1771_decryptionMaterialsIn_, _dafny.Seq([])))
        d_1773_decryptionMaterialsOut_ = out419_
        if not((d_1773_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(293,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptUnserializableEC():
        d_1774_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1775_valueOrError0_: Wrappers.Result = None
        out420_: Wrappers.Result
        out420_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1775_valueOrError0_ = out420_
        if not(not((d_1775_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(302,12): " + _dafny.string_of(d_1775_valueOrError0_))
        d_1774_mpl_ = (d_1775_valueOrError0_).Extract()
        d_1776_namespace_: _dafny.Seq
        d_1777_name_: _dafny.Seq
        out421_: _dafny.Seq
        out422_: _dafny.Seq
        out421_, out422_ = TestUtils.default__.NamespaceAndName(0)
        d_1776_namespace_ = out421_
        d_1777_name_ = out422_
        d_1778_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1779_valueOrError1_: Wrappers.Result = None
        out423_: Wrappers.Result
        out423_ = (d_1774_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1776_namespace_, d_1777_name_, _dafny.Seq([0 for d_1780_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1779_valueOrError1_ = out423_
        if not(not((d_1779_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,22): " + _dafny.string_of(d_1779_valueOrError1_))
        d_1778_rawAESKeyring_ = (d_1779_valueOrError1_).Extract()
        d_1781_unserializableEncryptionContext_: _dafny.Map
        out424_: _dafny.Map
        out424_ = TestRawAESKeyring.default__.generateUnserializableEncryptionContext()
        d_1781_unserializableEncryptionContext_ = out424_
        d_1782_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1782_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1783_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1784_valueOrError2_: Wrappers.Result = None
        d_1784_valueOrError2_ = (d_1774_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1782_algorithmSuiteId_, d_1781_unserializableEncryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1784_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(314,30): " + _dafny.string_of(d_1784_valueOrError2_))
        d_1783_encryptionMaterialsIn_ = (d_1784_valueOrError2_).Extract()
        d_1785_encryptionMaterialsOut_: Wrappers.Result
        out425_: Wrappers.Result
        out425_ = (d_1778_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1783_encryptionMaterialsIn_))
        d_1785_encryptionMaterialsOut_ = out425_
        if not((d_1785_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(326,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptUnserializableEC():
        d_1786_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1787_valueOrError0_: Wrappers.Result = None
        out426_: Wrappers.Result
        out426_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1787_valueOrError0_ = out426_
        if not(not((d_1787_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(336,12): " + _dafny.string_of(d_1787_valueOrError0_))
        d_1786_mpl_ = (d_1787_valueOrError0_).Extract()
        d_1788_namespace_: _dafny.Seq
        d_1789_name_: _dafny.Seq
        out427_: _dafny.Seq
        out428_: _dafny.Seq
        out427_, out428_ = TestUtils.default__.NamespaceAndName(0)
        d_1788_namespace_ = out427_
        d_1789_name_ = out428_
        d_1790_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1791_valueOrError1_: Wrappers.Result = None
        out429_: Wrappers.Result
        out429_ = (d_1786_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1788_namespace_, d_1789_name_, _dafny.Seq([0 for d_1792_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_1791_valueOrError1_ = out429_
        if not(not((d_1791_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,22): " + _dafny.string_of(d_1791_valueOrError1_))
        d_1790_rawAESKeyring_ = (d_1791_valueOrError1_).Extract()
        d_1793_encryptionContext_: _dafny.Map
        out430_: _dafny.Map
        out430_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1793_encryptionContext_ = out430_
        d_1794_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1794_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1795_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1796_valueOrError2_: Wrappers.Result = None
        d_1796_valueOrError2_ = (d_1786_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1794_algorithmSuiteId_, d_1793_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1796_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(348,30): " + _dafny.string_of(d_1796_valueOrError2_))
        d_1795_encryptionMaterialsIn_ = (d_1796_valueOrError2_).Extract()
        d_1797_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1798_valueOrError3_: Wrappers.Result = None
        out431_: Wrappers.Result
        out431_ = (d_1790_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1795_encryptionMaterialsIn_))
        d_1798_valueOrError3_ = out431_
        if not(not((d_1798_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(358,31): " + _dafny.string_of(d_1798_valueOrError3_))
        d_1797_encryptionMaterialsOut_ = (d_1798_valueOrError3_).Extract()
        d_1799___v4_: tuple
        d_1800_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_1800_valueOrError4_ = (d_1786_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1797_encryptionMaterialsOut_).materials)
        if not(not((d_1800_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(361,10): " + _dafny.string_of(d_1800_valueOrError4_))
        d_1799___v4_ = (d_1800_valueOrError4_).Extract()
        d_1801_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1801_edk_ = (((d_1797_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1802_unserializableEncryptionContext_: _dafny.Map
        out432_: _dafny.Map
        out432_ = TestRawAESKeyring.default__.generateUnserializableEncryptionContext()
        d_1802_unserializableEncryptionContext_ = out432_
        d_1803_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1804_valueOrError5_: Wrappers.Result = None
        d_1804_valueOrError5_ = (d_1786_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1794_algorithmSuiteId_, d_1802_unserializableEncryptionContext_, _dafny.Seq([])))
        if not(not((d_1804_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(366,30): " + _dafny.string_of(d_1804_valueOrError5_))
        d_1803_decryptionMaterialsIn_ = (d_1804_valueOrError5_).Extract()
        d_1805_decryptionMaterialsOut_: Wrappers.Result
        out433_: Wrappers.Result
        out433_ = (d_1790_rawAESKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1803_decryptionMaterialsIn_, _dafny.Seq([d_1801_edk_])))
        d_1805_decryptionMaterialsOut_ = out433_
        if not((d_1805_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(379,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def generateUnserializableEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_1806_keyA_: _dafny.Seq
        d_1807_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1807_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_1807_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(384,13): " + _dafny.string_of(d_1807_valueOrError0_))
        d_1806_keyA_ = (d_1807_valueOrError0_).Extract()
        d_1808_invalidVal_: _dafny.Seq
        d_1808_invalidVal_ = _dafny.Seq([0 for d_1809___v5_ in range(65536)])
        encCtx = _dafny.Map({d_1806_keyA_: d_1808_invalidVal_})
        return encCtx
        return encCtx

