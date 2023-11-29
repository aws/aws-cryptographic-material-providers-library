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
import TestVectors
import CompleteVectors

# Module: ParseJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildEncryptTestVector(keys, obj):
        if (len(obj)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_1833_name_ = ((obj)[0])[0]
            d_1834_valueOrError0_ = default__.ToEncryptTestVector(keys, d_1833_name_, ((obj)[0])[1])
            if (d_1834_valueOrError0_).IsFailure():
                return (d_1834_valueOrError0_).PropagateFailure()
            elif True:
                d_1835_encryptVector_ = (d_1834_valueOrError0_).Extract()
                d_1836_valueOrError1_ = default__.BuildEncryptTestVector(keys, _dafny.Seq((obj)[1::]))
                if (d_1836_valueOrError1_).IsFailure():
                    return (d_1836_valueOrError1_).PropagateFailure()
                elif True:
                    d_1837_tail_ = (d_1836_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_1835_encryptVector_])) + (d_1837_tail_))

    @staticmethod
    def ToEncryptTestVector(keys, name, obj):
        d_1838_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("EncryptTestVector not an object"))
        if (d_1838_valueOrError0_).IsFailure():
            return (d_1838_valueOrError0_).PropagateFailure()
        elif True:
            d_1839_obj_ = (obj).obj
            d_1840_typString_ = _dafny.Seq("type")
            d_1841_valueOrError1_ = JSONHelpers.default__.GetString(d_1840_typString_, d_1839_obj_)
            if (d_1841_valueOrError1_).IsFailure():
                return (d_1841_valueOrError1_).PropagateFailure()
            elif True:
                d_1842_typ_ = (d_1841_valueOrError1_).Extract()
                d_1843_description_ = (JSONHelpers.default__.GetString(_dafny.Seq("description"), d_1839_obj_)).ToOption()
                d_1844_valueOrError2_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_1839_obj_)
                if (d_1844_valueOrError2_).IsFailure():
                    return (d_1844_valueOrError2_).PropagateFailure()
                elif True:
                    d_1845_encryptionContextStrings_ = (d_1844_valueOrError2_).Extract()
                    d_1846_valueOrError3_ = JSONHelpers.default__.utf8EncodeMap(d_1845_encryptionContextStrings_)
                    if (d_1846_valueOrError3_).IsFailure():
                        return (d_1846_valueOrError3_).PropagateFailure()
                    elif True:
                        d_1847_encryptionContext_ = (d_1846_valueOrError3_).Extract()
                        d_1848_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), d_1839_obj_)
                        if (d_1848_valueOrError4_).IsFailure():
                            return (d_1848_valueOrError4_).PropagateFailure()
                        elif True:
                            d_1849_algorithmSuiteHex_ = (d_1848_valueOrError4_).Extract()
                            d_1850_valueOrError5_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_1849_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binnary"))
                            if (d_1850_valueOrError5_).IsFailure():
                                return (d_1850_valueOrError5_).PropagateFailure()
                            elif True:
                                d_1851_binaryId_ = HexStrings.default__.FromHexString(d_1849_algorithmSuiteHex_)
                                def lambda124_(d_1853_algorithmSuiteHex_):
                                    def lambda125_(d_1854_e_):
                                        return (_dafny.Seq("Invalid Suite:")) + (d_1853_algorithmSuiteHex_)

                                    return lambda125_

                                d_1852_valueOrError6_ = (AlgorithmSuites.default__.GetAlgorithmSuiteInfo(d_1851_binaryId_)).MapFailure(lambda124_(d_1849_algorithmSuiteHex_))
                                if (d_1852_valueOrError6_).IsFailure():
                                    return (d_1852_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_1855_algorithmSuite_ = (d_1852_valueOrError6_).Extract()
                                    d_1856_keysAsStrings_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_1839_obj_)).ToOption()
                                    def iife106_(_pat_let43_0):
                                        def iife107_(d_1858_result_):
                                            return (Wrappers.Result_Success(Wrappers.Option_Some((d_1858_result_).value)) if (d_1858_result_).is_Success else Wrappers.Result_Failure((d_1858_result_).error))
                                        return iife107_(_pat_let43_0)
                                    d_1857_valueOrError7_ = (iife106_(JSONHelpers.default__.utf8EncodeSeq((d_1856_keysAsStrings_).value)) if (d_1856_keysAsStrings_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                                    if (d_1857_valueOrError7_).IsFailure():
                                        return (d_1857_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_1859_requiredEncryptionContextKeys_ = (d_1857_valueOrError7_).Extract()
                                        d_1860_commitmentPolicy_ = CompleteVectors.default__.GetCompatableCommitmentPolicy(d_1855_algorithmSuite_)
                                        d_1861_maxPlaintextLength_ = Wrappers.Option_None()
                                        if (d_1842_typ_) == (_dafny.Seq("positive-keyring")):
                                            d_1862_valueOrError8_ = JSONHelpers.default__.Get(_dafny.Seq("encryptKeyDescription"), d_1839_obj_)
                                            if (d_1862_valueOrError8_).IsFailure():
                                                return (d_1862_valueOrError8_).PropagateFailure()
                                            elif True:
                                                d_1863_encryptKeyDescriptionObject_ = (d_1862_valueOrError8_).Extract()
                                                d_1864_valueOrError9_ = JSONHelpers.default__.Get(_dafny.Seq("decryptKeyDescription"), d_1839_obj_)
                                                if (d_1864_valueOrError9_).IsFailure():
                                                    return (d_1864_valueOrError9_).PropagateFailure()
                                                elif True:
                                                    d_1865_decryptKeyDescriptionObject_ = (d_1864_valueOrError9_).Extract()
                                                    def lambda126_(d_1867_e_):
                                                        return (d_1867_e_).ToString()

                                                    d_1866_valueOrError10_ = (JSON_mAPI.default__.Serialize(d_1863_encryptKeyDescriptionObject_)).MapFailure(lambda126_)
                                                    if (d_1866_valueOrError10_).IsFailure():
                                                        return (d_1866_valueOrError10_).PropagateFailure()
                                                    elif True:
                                                        d_1868_encryptStr_ = (d_1866_valueOrError10_).Extract()
                                                        def lambda127_(d_1870_e_):
                                                            return (d_1870_e_).ToString()

                                                        d_1869_valueOrError11_ = (JSON_mAPI.default__.Serialize(d_1865_decryptKeyDescriptionObject_)).MapFailure(lambda127_)
                                                        if (d_1869_valueOrError11_).IsFailure():
                                                            return (d_1869_valueOrError11_).PropagateFailure()
                                                        elif True:
                                                            d_1871_decryptStr_ = (d_1869_valueOrError11_).Extract()
                                                            d_1872_valueOrError12_ = ((keys).GetKeyDescription(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionInput_GetKeyDescriptionInput(d_1868_encryptStr_))).MapFailure(default__.ErrorToString)
                                                            if (d_1872_valueOrError12_).IsFailure():
                                                                return (d_1872_valueOrError12_).PropagateFailure()
                                                            elif True:
                                                                d_1873_encryptKeyDescription_ = (d_1872_valueOrError12_).Extract()
                                                                d_1874_valueOrError13_ = ((keys).GetKeyDescription(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionInput_GetKeyDescriptionInput(d_1871_decryptStr_))).MapFailure(default__.ErrorToString)
                                                                if (d_1874_valueOrError13_).IsFailure():
                                                                    return (d_1874_valueOrError13_).PropagateFailure()
                                                                elif True:
                                                                    d_1875_decryptKeyDescription_ = (d_1874_valueOrError13_).Extract()
                                                                    return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(name, d_1843_description_, d_1847_encryptionContext_, d_1860_commitmentPolicy_, d_1855_algorithmSuite_, d_1861_maxPlaintextLength_, d_1859_requiredEncryptionContextKeys_, (d_1873_encryptKeyDescription_).keyDescription, (d_1875_decryptKeyDescription_).keyDescription))
                                        elif (d_1842_typ_) == (_dafny.Seq("negative-keyring")):
                                            d_1876_valueOrError14_ = JSONHelpers.default__.Get(_dafny.Seq("keyDescription"), d_1839_obj_)
                                            if (d_1876_valueOrError14_).IsFailure():
                                                return (d_1876_valueOrError14_).PropagateFailure()
                                            elif True:
                                                d_1877_keyDescriptionObject_ = (d_1876_valueOrError14_).Extract()
                                                def lambda128_(d_1879_e_):
                                                    return (d_1879_e_).ToString()

                                                d_1878_valueOrError15_ = (JSON_mAPI.default__.Serialize(d_1877_keyDescriptionObject_)).MapFailure(lambda128_)
                                                if (d_1878_valueOrError15_).IsFailure():
                                                    return (d_1878_valueOrError15_).PropagateFailure()
                                                elif True:
                                                    d_1880_keyStr_ = (d_1878_valueOrError15_).Extract()
                                                    d_1881_valueOrError16_ = ((keys).GetKeyDescription(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionInput_GetKeyDescriptionInput(d_1880_keyStr_))).MapFailure(default__.ErrorToString)
                                                    if (d_1881_valueOrError16_).IsFailure():
                                                        return (d_1881_valueOrError16_).PropagateFailure()
                                                    elif True:
                                                        d_1882_keyDescription_ = (d_1881_valueOrError16_).Extract()
                                                        d_1883_valueOrError17_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_1839_obj_)
                                                        if (d_1883_valueOrError17_).IsFailure():
                                                            return (d_1883_valueOrError17_).PropagateFailure()
                                                        elif True:
                                                            d_1884_errorDescription_ = (d_1883_valueOrError17_).Extract()
                                                            return Wrappers.Result_Success(TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(name, d_1843_description_, d_1847_encryptionContext_, d_1860_commitmentPolicy_, d_1855_algorithmSuite_, d_1861_maxPlaintextLength_, d_1859_requiredEncryptionContextKeys_, d_1884_errorDescription_, (d_1882_keyDescription_).keyDescription))
                                        elif True:
                                            return Wrappers.Result_Failure((_dafny.Seq("Unsupported EncryptTestVector type:")) + (d_1842_typ_))

    @staticmethod
    def ErrorToString(e):
        source60_ = e
        if source60_.is_KeyVectorException:
            d_1885___mcc_h0_ = source60_.message
            d_1886_message_ = d_1885___mcc_h0_
            return d_1886_message_
        elif source60_.is_AwsCryptographyMaterialProviders:
            d_1887___mcc_h2_ = source60_.AwsCryptographyMaterialProviders
            d_1888_mplError_ = d_1887___mcc_h2_
            source61_ = d_1888_mplError_
            if source61_.is_AwsCryptographicMaterialProvidersException:
                d_1889___mcc_h12_ = source61_.message
                d_1890_message_ = d_1889___mcc_h12_
                return d_1890_message_
            elif source61_.is_EntryAlreadyExists:
                d_1891___mcc_h14_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_EntryDoesNotExist:
                d_1892___mcc_h16_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_InvalidAlgorithmSuiteInfo:
                d_1893___mcc_h18_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_InvalidAlgorithmSuiteInfoOnDecrypt:
                d_1894___mcc_h20_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_InvalidAlgorithmSuiteInfoOnEncrypt:
                d_1895___mcc_h22_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_InvalidDecryptionMaterials:
                d_1896___mcc_h24_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_InvalidDecryptionMaterialsTransition:
                d_1897___mcc_h26_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_InvalidEncryptionMaterials:
                d_1898___mcc_h28_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_InvalidEncryptionMaterialsTransition:
                d_1899___mcc_h30_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_AwsCryptographyKeyStore:
                d_1900___mcc_h32_ = source61_.AwsCryptographyKeyStore
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_AwsCryptographyPrimitives:
                d_1901___mcc_h34_ = source61_.AwsCryptographyPrimitives
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_ComAmazonawsDynamodb:
                d_1902___mcc_h36_ = source61_.ComAmazonawsDynamodb
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_ComAmazonawsKms:
                d_1903___mcc_h38_ = source61_.ComAmazonawsKms
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif source61_.is_CollectionOfErrors:
                d_1904___mcc_h40_ = source61_.list
                d_1905___mcc_h41_ = source61_.message
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
            elif True:
                d_1906___mcc_h44_ = source61_.obj
                return _dafny.Seq("Umapped AwsCryptographyMaterialProviders")
        elif source60_.is_ComAmazonawsKms:
            d_1907___mcc_h4_ = source60_.ComAmazonawsKms
            return _dafny.Seq("Umapped KeyVectorException")
        elif source60_.is_CollectionOfErrors:
            d_1908___mcc_h6_ = source60_.list
            d_1909___mcc_h7_ = source60_.message
            return _dafny.Seq("Umapped KeyVectorException")
        elif True:
            d_1910___mcc_h10_ = source60_.obj
            return _dafny.Seq("Umapped KeyVectorException")

