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
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
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
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
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
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants
import JSON_mZeroCopy_mDeserializer_mValues
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy
import JSON_mAPI
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny

assert "TestVectors" == __name__
TestVectors = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetEncryptionMaterials(test):
        testResult: bool = False
        materials: Wrappers.Option = Wrappers.Option_None.default()()
        _dafny.print(_dafny.string_of(_dafny.Seq("\nTEST===> ")))
        _dafny.print(_dafny.string_of(((test).vector).name))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + ((((test).vector).description).value) if (((test).vector).description).is_Some else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + (((test).vector).errorDescription) if ((test).vector).is_NegativeEncryptKeyringVector else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        d_1705_result_: Wrappers.Result
        out326_: Wrappers.Result
        out326_ = ((test).cmm).GetEncryptionMaterials((test).input)
        d_1705_result_ = out326_
        def lambda112_(source52_):
            if source52_.is_PositiveEncryptKeyringVector:
                d_1706___mcc_h0_ = source52_.name
                d_1707___mcc_h1_ = source52_.description
                d_1708___mcc_h2_ = source52_.encryptionContext
                d_1709___mcc_h3_ = source52_.commitmentPolicy
                d_1710___mcc_h4_ = source52_.algorithmSuite
                d_1711___mcc_h5_ = source52_.maxPlaintextLength
                d_1712___mcc_h6_ = source52_.requiredEncryptionContextKeys
                d_1713___mcc_h7_ = source52_.encryptDescription
                d_1714___mcc_h8_ = source52_.decryptDescription
                return (d_1705_result_).is_Success
            elif True:
                d_1715___mcc_h9_ = source52_.name
                d_1716___mcc_h10_ = source52_.description
                d_1717___mcc_h11_ = source52_.encryptionContext
                d_1718___mcc_h12_ = source52_.commitmentPolicy
                d_1719___mcc_h13_ = source52_.algorithmSuite
                d_1720___mcc_h14_ = source52_.maxPlaintextLength
                d_1721___mcc_h15_ = source52_.requiredEncryptionContextKeys
                d_1722___mcc_h16_ = source52_.errorDescription
                d_1723___mcc_h17_ = source52_.keyDescription
                return not((d_1705_result_).is_Success)

        testResult = lambda112_((test).vector)
        materials = (Wrappers.Option_Some(((d_1705_result_).value).encryptionMaterials) if (((test).vector).is_PositiveEncryptKeyringVector) and ((d_1705_result_).is_Success) else Wrappers.Option_None())
        if not(testResult):
            if ((test).vector).is_PositiveEncryptKeyringVector:
                _dafny.print(_dafny.string_of((d_1705_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return testResult, materials

    @staticmethod
    def TestDecryptMaterials(test):
        output: bool = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\nTEST===> ")))
        _dafny.print(_dafny.string_of(((test).vector).name))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + ((((test).vector).description).value) if (((test).vector).description).is_Some else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + (((test).vector).errorDescription) if ((test).vector).is_NegativeDecryptKeyringTest else _dafny.Seq("\n"))))
        d_1724_result_: Wrappers.Result
        out327_: Wrappers.Result
        out327_ = ((test).cmm).DecryptMaterials((test).input)
        d_1724_result_ = out327_
        def lambda113_(source53_):
            if source53_.is_PositiveDecryptKeyringTest:
                d_1725___mcc_h0_ = source53_.name
                d_1726___mcc_h1_ = source53_.algorithmSuite
                d_1727___mcc_h2_ = source53_.commitmentPolicy
                d_1728___mcc_h3_ = source53_.encryptedDataKeys
                d_1729___mcc_h4_ = source53_.encryptionContext
                d_1730___mcc_h5_ = source53_.keyDescription
                d_1731___mcc_h6_ = source53_.expectedResult
                d_1732___mcc_h7_ = source53_.description
                d_1733___mcc_h8_ = source53_.reproducedEncryptionContext
                return ((((d_1724_result_).is_Success) and (((((d_1724_result_).value).decryptionMaterials).plaintextDataKey) == ((((test).vector).expectedResult).plaintextDataKey))) and (((((d_1724_result_).value).decryptionMaterials).symmetricSigningKey) == ((((test).vector).expectedResult).symmetricSigningKey))) and (((((d_1724_result_).value).decryptionMaterials).requiredEncryptionContextKeys) == ((((test).vector).expectedResult).requiredEncryptionContextKeys))
            elif True:
                d_1734___mcc_h9_ = source53_.name
                d_1735___mcc_h10_ = source53_.algorithmSuite
                d_1736___mcc_h11_ = source53_.commitmentPolicy
                d_1737___mcc_h12_ = source53_.encryptedDataKeys
                d_1738___mcc_h13_ = source53_.encryptionContext
                d_1739___mcc_h14_ = source53_.errorDescription
                d_1740___mcc_h15_ = source53_.keyDescription
                d_1741___mcc_h16_ = source53_.reproducedEncryptionContext
                d_1742___mcc_h17_ = source53_.description
                return not((d_1724_result_).is_Success)

        output = lambda113_((test).vector)
        if not(output):
            if (((test).vector).is_PositiveDecryptKeyringTest) and ((d_1724_result_).is_Failure):
                _dafny.print(_dafny.string_of((d_1724_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return output

    @staticmethod
    def ToEncryptTest(keys, vector):
        output: Wrappers.Result = None
        d_1743_input_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput
        def lambda114_(source54_):
            if source54_.is_PositiveEncryptKeyringVector:
                d_1744___mcc_h0_ = source54_.name
                d_1745___mcc_h1_ = source54_.description
                d_1746___mcc_h2_ = source54_.encryptionContext
                d_1747___mcc_h3_ = source54_.commitmentPolicy
                d_1748___mcc_h4_ = source54_.algorithmSuite
                d_1749___mcc_h5_ = source54_.maxPlaintextLength
                d_1750___mcc_h6_ = source54_.requiredEncryptionContextKeys
                d_1751___mcc_h7_ = source54_.encryptDescription
                d_1752___mcc_h8_ = source54_.decryptDescription
                def iife59_(_pat_let25_0):
                    def iife60_(d_1753_requiredEncryptionContextKeys_):
                        def iife61_(_pat_let26_0):
                            def iife62_(d_1754_maxPlaintextLength_):
                                def iife63_(_pat_let27_0):
                                    def iife64_(d_1755_algorithmSuite_):
                                        def iife65_(_pat_let28_0):
                                            def iife66_(d_1756_commitmentPolicy_):
                                                def iife67_(_pat_let29_0):
                                                    def iife68_(d_1757_encryptionContext_):
                                                        return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(d_1757_encryptionContext_, d_1756_commitmentPolicy_, Wrappers.Option_Some((d_1755_algorithmSuite_).id), d_1754_maxPlaintextLength_, d_1753_requiredEncryptionContextKeys_)
                                                    return iife68_(_pat_let29_0)
                                                return iife67_(d_1746___mcc_h2_)
                                            return iife66_(_pat_let28_0)
                                        return iife65_(d_1747___mcc_h3_)
                                    return iife64_(_pat_let27_0)
                                return iife63_(d_1748___mcc_h4_)
                            return iife62_(_pat_let26_0)
                        return iife61_(d_1749___mcc_h5_)
                    return iife60_(_pat_let25_0)
                return iife59_(d_1750___mcc_h6_)
            elif True:
                d_1758___mcc_h9_ = source54_.name
                d_1759___mcc_h10_ = source54_.description
                d_1760___mcc_h11_ = source54_.encryptionContext
                d_1761___mcc_h12_ = source54_.commitmentPolicy
                d_1762___mcc_h13_ = source54_.algorithmSuite
                d_1763___mcc_h14_ = source54_.maxPlaintextLength
                d_1764___mcc_h15_ = source54_.requiredEncryptionContextKeys
                d_1765___mcc_h16_ = source54_.errorDescription
                d_1766___mcc_h17_ = source54_.keyDescription
                def iife69_(_pat_let30_0):
                    def iife70_(d_1767_requiredEncryptionContextKeys_):
                        def iife71_(_pat_let31_0):
                            def iife72_(d_1768_maxPlaintextLength_):
                                def iife73_(_pat_let32_0):
                                    def iife74_(d_1769_algorithmSuite_):
                                        def iife75_(_pat_let33_0):
                                            def iife76_(d_1770_commitmentPolicy_):
                                                def iife77_(_pat_let34_0):
                                                    def iife78_(d_1771_encryptionContext_):
                                                        return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(d_1771_encryptionContext_, d_1770_commitmentPolicy_, Wrappers.Option_Some((d_1769_algorithmSuite_).id), d_1768_maxPlaintextLength_, d_1767_requiredEncryptionContextKeys_)
                                                    return iife78_(_pat_let34_0)
                                                return iife77_(d_1760___mcc_h11_)
                                            return iife76_(_pat_let33_0)
                                        return iife75_(d_1761___mcc_h12_)
                                    return iife74_(_pat_let32_0)
                                return iife73_(d_1762___mcc_h13_)
                            return iife72_(_pat_let31_0)
                        return iife71_(d_1763___mcc_h14_)
                    return iife70_(_pat_let30_0)
                return iife69_(d_1764___mcc_h15_)

        d_1743_input_ = lambda114_(vector)
        d_1772_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1773_valueOrError0_: Wrappers.Result = None
        out328_: Wrappers.Result
        out328_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1773_valueOrError0_ = out328_
        if not(not((d_1773_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(131,12): " + _dafny.string_of(d_1773_valueOrError0_))
        d_1772_mpl_ = (d_1773_valueOrError0_).Extract()
        d_1774_maybeKeyring_: Wrappers.Result
        out329_: Wrappers.Result
        out329_ = (keys).CreateWappedTestVectorKeyring(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.TestVectorKeyringInput_TestVectorKeyringInput(((vector).encryptDescription if (vector).is_PositiveEncryptKeyringVector else (vector).keyDescription)))
        d_1774_maybeKeyring_ = out329_
        d_1775_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1776_valueOrError1_: Wrappers.Result = None
        def lambda115_(d_1777_e_):
            def iife79_(_pat_let35_0):
                def iife80_(d_1778___v44_):
                    return _dafny.Seq("Keyring failure")
                return iife80_(_pat_let35_0)
            return iife79_(TestVectors.default__.printErr(d_1777_e_))

        d_1776_valueOrError1_ = (d_1774_maybeKeyring_).MapFailure(lambda115_)
        if (d_1776_valueOrError1_).IsFailure():
            output = (d_1776_valueOrError1_).PropagateFailure()
            return output
        d_1775_keyring_ = (d_1776_valueOrError1_).Extract()
        print(f"{d_1775_keyring_=}")
        d_1779_maybeCmm_: Wrappers.Result
        out330_: Wrappers.Result
        print(f"{d_1772_mpl_=}")
        out330_ = (d_1772_mpl_).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_1775_keyring_))
        d_1779_maybeCmm_ = out330_
        d_1780_cmm_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
        d_1781_valueOrError2_: Wrappers.Result = None
        def lambda116_(d_1782_e_):
            return _dafny.Seq("CMM failure")

        print(f"{d_1779_maybeCmm_=}")
        d_1781_valueOrError2_ = (d_1779_maybeCmm_).MapFailure(lambda116_)
        if (d_1781_valueOrError2_).IsFailure():
            output = (d_1781_valueOrError2_).PropagateFailure()
            return output
        d_1780_cmm_ = (d_1781_valueOrError2_).Extract()
        output = Wrappers.Result_Success(TestVectors.EncryptTest_EncryptTest(d_1743_input_, d_1780_cmm_, vector))
        return output
        return output

    @staticmethod
    def ToDecryptTest(keys, test, materials):
        output: Wrappers.Result = None
        d_1783_reproducedEncryptionContext_: Wrappers.Option
        d_1783_reproducedEncryptionContext_ = Wrappers.Option_None()
        d_1784_input_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput
        d_1784_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput_DecryptMaterialsInput(((materials).algorithmSuite).id, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, (materials).encryptionContext, d_1783_reproducedEncryptionContext_)
        d_1785_vector_: TestVectors.DecryptTestVector
        d_1785_vector_ = TestVectors.DecryptTestVector_PositiveDecryptKeyringTest((((test).vector).name) + (_dafny.Seq("->Decryption")), (materials).algorithmSuite, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, (materials).encryptionContext, ((test).vector).decryptDescription, TestVectors.DecryptResult_DecryptResult((materials).plaintextDataKey, (Wrappers.Option_Some((((materials).symmetricSigningKeys).value)[0]) if (((materials).symmetricSigningKeys).is_Some) and ((0) < (len(((materials).symmetricSigningKeys).value))) else Wrappers.Option_None()), (materials).requiredEncryptionContextKeys), (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((test).vector).description).value)) if (((test).vector).description).is_Some else Wrappers.Option_None()), d_1783_reproducedEncryptionContext_)
        d_1786_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1787_valueOrError0_: Wrappers.Result = None
        out331_: Wrappers.Result
        out331_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1787_valueOrError0_ = out331_
        if not(not((d_1787_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(196,12): " + _dafny.string_of(d_1787_valueOrError0_))
        d_1786_mpl_ = (d_1787_valueOrError0_).Extract()
        d_1788_maybeKeyring_: Wrappers.Result
        out332_: Wrappers.Result
        out332_ = (keys).CreateWappedTestVectorKeyring(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.TestVectorKeyringInput_TestVectorKeyringInput((d_1785_vector_).keyDescription))
        d_1788_maybeKeyring_ = out332_
        d_1789_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_1790_valueOrError1_: Wrappers.Result = None
        def lambda117_(d_1791_e_):
            def iife81_(_pat_let36_0):
                def iife82_(d_1792___v45_):
                    return _dafny.Seq("Keyring failure")
                return iife82_(_pat_let36_0)
            return iife81_(TestVectors.default__.printErr(d_1791_e_))

        d_1790_valueOrError1_ = (d_1788_maybeKeyring_).MapFailure(lambda117_)
        if (d_1790_valueOrError1_).IsFailure():
            output = (d_1790_valueOrError1_).PropagateFailure()
            return output
        d_1789_keyring_ = (d_1790_valueOrError1_).Extract()
        d_1793_maybeCmm_: Wrappers.Result
        out333_: Wrappers.Result
        out333_ = (d_1786_mpl_).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_1789_keyring_))
        d_1793_maybeCmm_ = out333_
        d_1794_cmm_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
        d_1795_valueOrError2_: Wrappers.Result = None
        def lambda118_(d_1796_e_):
            return _dafny.Seq("CMM failure")

        print(f"{d_1793_maybeCmm_=}")
        d_1795_valueOrError2_ = (d_1793_maybeCmm_).MapFailure(lambda118_)
        if (d_1795_valueOrError2_).IsFailure():
            output = (d_1795_valueOrError2_).PropagateFailure()
            return output
        d_1794_cmm_ = (d_1795_valueOrError2_).Extract()
        output = Wrappers.Result_Success(TestVectors.DecryptTest_DecryptTest(d_1784_input_, d_1794_cmm_, d_1785_vector_))
        return output
        return output

    @staticmethod
    def printErr(e):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(e))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_


class EncryptTest:
    @classmethod
    def default(cls, ):
        return lambda: EncryptTest_EncryptTest(software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput.default()(), None, TestVectors.EncryptTestVector_PositiveEncryptKeyringVector.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptTest(self) -> bool:
        return isinstance(self, TestVectors.EncryptTest_EncryptTest)

class EncryptTest_EncryptTest(EncryptTest, NamedTuple('EncryptTest', [('input', Any), ('cmm', Any), ('vector', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTest.EncryptTest({_dafny.string_of(self.input)}, {_dafny.string_of(self.cmm)}, {_dafny.string_of(self.vector)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectors.EncryptTest_EncryptTest) and self.input == __o.input and self.cmm == __o.cmm and self.vector == __o.vector
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptTest:
    @classmethod
    def default(cls, ):
        return lambda: DecryptTest_DecryptTest(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput_DecryptMaterialsInput.default()(), None, TestVectors.DecryptTestVector_PositiveDecryptKeyringTest.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptTest(self) -> bool:
        return isinstance(self, TestVectors.DecryptTest_DecryptTest)

class DecryptTest_DecryptTest(DecryptTest, NamedTuple('DecryptTest', [('input', Any), ('cmm', Any), ('vector', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptTest.DecryptTest({_dafny.string_of(self.input)}, {_dafny.string_of(self.cmm)}, {_dafny.string_of(self.vector)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectors.DecryptTest_DecryptTest) and self.input == __o.input and self.cmm == __o.cmm and self.vector == __o.vector
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptTestVector:
    @classmethod
    def default(cls, ):
        return lambda: EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq({}), Wrappers.Option_None.default()(), _dafny.Map({}), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms.default()(), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PositiveEncryptKeyringVector(self) -> bool:
        return isinstance(self, TestVectors.EncryptTestVector_PositiveEncryptKeyringVector)
    @property
    def is_NegativeEncryptKeyringVector(self) -> bool:
        return isinstance(self, TestVectors.EncryptTestVector_NegativeEncryptKeyringVector)

class EncryptTestVector_PositiveEncryptKeyringVector(EncryptTestVector, NamedTuple('PositiveEncryptKeyringVector', [('name', Any), ('description', Any), ('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuite', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any), ('encryptDescription', Any), ('decryptDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTestVector.PositiveEncryptKeyringVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.encryptDescription)}, {_dafny.string_of(self.decryptDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectors.EncryptTestVector_PositiveEncryptKeyringVector) and self.name == __o.name and self.description == __o.description and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuite == __o.algorithmSuite and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.encryptDescription == __o.encryptDescription and self.decryptDescription == __o.decryptDescription
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptTestVector_NegativeEncryptKeyringVector(EncryptTestVector, NamedTuple('NegativeEncryptKeyringVector', [('name', Any), ('description', Any), ('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuite', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any), ('errorDescription', Any), ('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTestVector.NegativeEncryptKeyringVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.errorDescription)}, {_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectors.EncryptTestVector_NegativeEncryptKeyringVector) and self.name == __o.name and self.description == __o.description and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuite == __o.algorithmSuite and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.errorDescription == __o.errorDescription and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptTestVector:
    @classmethod
    def default(cls, ):
        return lambda: DecryptTestVector_PositiveDecryptKeyringTest(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK.default()(), _dafny.Seq({}), _dafny.Map({}), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms.default()(), TestVectors.DecryptResult_DecryptResult.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PositiveDecryptKeyringTest(self) -> bool:
        return isinstance(self, TestVectors.DecryptTestVector_PositiveDecryptKeyringTest)
    @property
    def is_NegativeDecryptKeyringTest(self) -> bool:
        return isinstance(self, TestVectors.DecryptTestVector_NegativeDecryptKeyringTest)

class DecryptTestVector_PositiveDecryptKeyringTest(DecryptTestVector, NamedTuple('PositiveDecryptKeyringTest', [('name', Any), ('algorithmSuite', Any), ('commitmentPolicy', Any), ('encryptedDataKeys', Any), ('encryptionContext', Any), ('keyDescription', Any), ('expectedResult', Any), ('description', Any), ('reproducedEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptTestVector.PositiveDecryptKeyringTest({_dafny.string_of(self.name)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.keyDescription)}, {_dafny.string_of(self.expectedResult)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.reproducedEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectors.DecryptTestVector_PositiveDecryptKeyringTest) and self.name == __o.name and self.algorithmSuite == __o.algorithmSuite and self.commitmentPolicy == __o.commitmentPolicy and self.encryptedDataKeys == __o.encryptedDataKeys and self.encryptionContext == __o.encryptionContext and self.keyDescription == __o.keyDescription and self.expectedResult == __o.expectedResult and self.description == __o.description and self.reproducedEncryptionContext == __o.reproducedEncryptionContext
    def __hash__(self) -> int:
        return super().__hash__()

class DecryptTestVector_NegativeDecryptKeyringTest(DecryptTestVector, NamedTuple('NegativeDecryptKeyringTest', [('name', Any), ('algorithmSuite', Any), ('commitmentPolicy', Any), ('encryptedDataKeys', Any), ('encryptionContext', Any), ('errorDescription', Any), ('keyDescription', Any), ('reproducedEncryptionContext', Any), ('description', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptTestVector.NegativeDecryptKeyringTest({_dafny.string_of(self.name)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.errorDescription)}, {_dafny.string_of(self.keyDescription)}, {_dafny.string_of(self.reproducedEncryptionContext)}, {_dafny.string_of(self.description)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectors.DecryptTestVector_NegativeDecryptKeyringTest) and self.name == __o.name and self.algorithmSuite == __o.algorithmSuite and self.commitmentPolicy == __o.commitmentPolicy and self.encryptedDataKeys == __o.encryptedDataKeys and self.encryptionContext == __o.encryptionContext and self.errorDescription == __o.errorDescription and self.keyDescription == __o.keyDescription and self.reproducedEncryptionContext == __o.reproducedEncryptionContext and self.description == __o.description
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptResult:
    @classmethod
    def default(cls, ):
        return lambda: DecryptResult_DecryptResult(Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptResult(self) -> bool:
        return isinstance(self, TestVectors.DecryptResult_DecryptResult)

class DecryptResult_DecryptResult(DecryptResult, NamedTuple('DecryptResult', [('plaintextDataKey', Any), ('symmetricSigningKey', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptResult.DecryptResult({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectors.DecryptResult_DecryptResult) and self.plaintextDataKey == __o.plaintextDataKey and self.symmetricSigningKey == __o.symmetricSigningKey and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()

