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

assert "KeyDescription" == __name__
KeyDescription = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def printErr(e):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(e))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def printJSON(e):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(e))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def ToKeyDescription(obj):
        d_1412_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("KeyDescription not an object"))
        if (d_1412_valueOrError0_).IsFailure():
            return (d_1412_valueOrError0_).PropagateFailure()
        elif True:
            d_1413_obj_ = (obj).obj
            d_1414_typString_ = _dafny.Seq("type")
            d_1415_valueOrError1_ = JSONHelpers.default__.GetString(d_1414_typString_, d_1413_obj_)
            if (d_1415_valueOrError1_).IsFailure():
                return (d_1415_valueOrError1_).PropagateFailure()
            elif True:
                d_1416_typ_ = (d_1415_valueOrError1_).Extract()
                d_1417_valueOrError2_ = Wrappers.default__.Need(KeyDescription.default__.KeyDescriptionString_q(d_1416_typ_), (_dafny.Seq("Unsupported KeyDescription type:")) + (d_1416_typ_))
                if (d_1417_valueOrError2_).IsFailure():
                    return (d_1417_valueOrError2_).PropagateFailure()
                elif True:
                    if (d_1416_typ_) == (_dafny.Seq("aws-kms-mrk-aware-discovery")):
                        d_1418_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("default-mrk-region"), d_1413_obj_)
                        if (d_1418_valueOrError3_).IsFailure():
                            return (d_1418_valueOrError3_).PropagateFailure()
                        elif True:
                            d_1419_defaultMrkRegion_ = (d_1418_valueOrError3_).Extract()
                            d_1420_filter_ = JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), d_1413_obj_)
                            d_1421_awsKmsDiscoveryFilter_ = KeyDescription.default__.ToDiscoveryFilter(d_1413_obj_)
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrkDiscovery(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq("aws-kms-mrk-aware-discovery"), d_1419_defaultMrkRegion_, d_1421_awsKmsDiscoveryFilter_)))
                    elif True:
                        d_1422_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("key"), d_1413_obj_)
                        if (d_1422_valueOrError4_).IsFailure():
                            return (d_1422_valueOrError4_).PropagateFailure()
                        elif True:
                            d_1423_key_ = (d_1422_valueOrError4_).Extract()
                            if (d_1416_typ_) == (_dafny.Seq("static-material-keyring")):
                                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Static(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.StaticKeyring_StaticKeyring(d_1423_key_)))
                            elif (d_1416_typ_) == (_dafny.Seq("aws-kms")):
                                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KMSInfo_KMSInfo(d_1423_key_)))
                            elif (d_1416_typ_) == (_dafny.Seq("aws-kms-mrk-aware")):
                                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrk(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAware_KmsMrkAware(d_1423_key_)))
                            elif (d_1416_typ_) == (_dafny.Seq("aws-kms-rsa")):
                                d_1424_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_1413_obj_)
                                if (d_1424_valueOrError5_).IsFailure():
                                    return (d_1424_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_1425_encryptionAlgorithmString_ = (d_1424_valueOrError5_).Extract()
                                    d_1426_valueOrError6_ = Wrappers.default__.Need(KeyDescription.default__.EncryptionAlgorithmSpec_q(d_1425_encryptionAlgorithmString_), (_dafny.Seq("Unsupported EncryptionAlgorithmSpec:")) + (d_1425_encryptionAlgorithmString_))
                                    if (d_1426_valueOrError6_).IsFailure():
                                        return (d_1426_valueOrError6_).PropagateFailure()
                                    elif True:
                                        d_1427_encryptionAlgorithm_ = (software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1() if (d_1425_encryptionAlgorithmString_) == (_dafny.Seq("RSAES_OAEP_SHA_1")) else software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256())
                                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsRsa(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsRsaKeyring_KmsRsaKeyring(d_1423_key_, d_1427_encryptionAlgorithm_)))
                            elif (d_1416_typ_) == (_dafny.Seq("aws-kms-hierarchy")):
                                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Hierarchy(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.HierarchyKeyring_HierarchyKeyring(d_1423_key_)))
                            elif True:
                                d_1428_valueOrError7_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_1413_obj_)
                                if (d_1428_valueOrError7_).IsFailure():
                                    return (d_1428_valueOrError7_).PropagateFailure()
                                elif True:
                                    d_1429_algorithm_ = (d_1428_valueOrError7_).Extract()
                                    d_1430_valueOrError8_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), d_1413_obj_)
                                    if (d_1430_valueOrError8_).IsFailure():
                                        return (d_1430_valueOrError8_).PropagateFailure()
                                    elif True:
                                        d_1431_providerId_ = (d_1430_valueOrError8_).Extract()
                                        d_1432_valueOrError9_ = Wrappers.default__.Need(KeyDescription.default__.RawAlgorithmString_q(d_1429_algorithm_), (_dafny.Seq("Unsupported algorithm:")) + (d_1429_algorithm_))
                                        if (d_1432_valueOrError9_).IsFailure():
                                            return (d_1432_valueOrError9_).PropagateFailure()
                                        elif True:
                                            if (d_1429_algorithm_) == (_dafny.Seq("aes")):
                                                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES(d_1423_key_, d_1431_providerId_)))
                                            elif True:
                                                d_1433_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-algorithm"), d_1413_obj_)
                                                if (d_1433_valueOrError10_).IsFailure():
                                                    return (d_1433_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_1434_paddingAlgorithm_ = (d_1433_valueOrError10_).Extract()
                                                    d_1435_valueOrError11_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-hash"), d_1413_obj_)
                                                    if (d_1435_valueOrError11_).IsFailure():
                                                        return (d_1435_valueOrError11_).PropagateFailure()
                                                    elif True:
                                                        d_1436_paddingHash_ = (d_1435_valueOrError11_).Extract()
                                                        d_1437_valueOrError12_ = Wrappers.default__.Need(KeyDescription.default__.PaddingAlgorithmString_q(d_1434_paddingAlgorithm_), (_dafny.Seq("Unsupported paddingAlgorithm:")) + (d_1434_paddingAlgorithm_))
                                                        if (d_1437_valueOrError12_).IsFailure():
                                                            return (d_1437_valueOrError12_).PropagateFailure()
                                                        elif True:
                                                            d_1438_valueOrError13_ = Wrappers.default__.Need(KeyDescription.default__.PaddingHashString_q(d_1436_paddingHash_), (_dafny.Seq("Unsupported paddingHash:")) + (d_1436_paddingHash_))
                                                            if (d_1438_valueOrError13_).IsFailure():
                                                                return (d_1438_valueOrError13_).PropagateFailure()
                                                            elif True:
                                                                if (d_1434_paddingAlgorithm_) == (_dafny.Seq("pkcs1")):
                                                                    d_1439_valueOrError14_ = Wrappers.default__.Need((d_1436_paddingHash_) == (_dafny.Seq("sha1")), (_dafny.Seq("Unsupported padding with pkcs1:")) + (d_1436_paddingHash_))
                                                                    if (d_1439_valueOrError14_).IsFailure():
                                                                        return (d_1439_valueOrError14_).PropagateFailure()
                                                                    elif True:
                                                                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_1423_key_, d_1431_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_PKCS1())))
                                                                elif True:
                                                                    if (d_1436_paddingHash_) == (_dafny.Seq("sha1")):
                                                                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_1423_key_, d_1431_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1())))
                                                                    elif (d_1436_paddingHash_) == (_dafny.Seq("sha256")):
                                                                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_1423_key_, d_1431_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA256__MGF1())))
                                                                    elif (d_1436_paddingHash_) == (_dafny.Seq("sha384")):
                                                                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_1423_key_, d_1431_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA384__MGF1())))
                                                                    elif True:
                                                                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_1423_key_, d_1431_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA512__MGF1())))

    @staticmethod
    def ToDiscoveryFilter(obj):
        d_1440_valueOrError0_ = (JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)).ToOption()
        if (d_1440_valueOrError0_).IsFailure():
            return (d_1440_valueOrError0_).PropagateFailure()
        elif True:
            d_1441_filter_ = (d_1440_valueOrError0_).Extract()
            d_1442_valueOrError1_ = (JSONHelpers.default__.GetString(_dafny.Seq("partition"), d_1441_filter_)).ToOption()
            if (d_1442_valueOrError1_).IsFailure():
                return (d_1442_valueOrError1_).PropagateFailure()
            elif True:
                d_1443_partition_ = (d_1442_valueOrError1_).Extract()
                d_1444_valueOrError2_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("account-ids"), d_1441_filter_)).ToOption()
                if (d_1444_valueOrError2_).IsFailure():
                    return (d_1444_valueOrError2_).PropagateFailure()
                elif True:
                    d_1445_accountIds_ = (d_1444_valueOrError2_).Extract()
                    return Wrappers.Option_Some(software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter(d_1445_accountIds_, d_1443_partition_))

    @staticmethod
    def KeyDescriptionString_q(s):
        return (((((((s) == (_dafny.Seq("static-material-keyring"))) or ((s) == (_dafny.Seq("aws-kms")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware-discovery")))) or ((s) == (_dafny.Seq("raw")))) or ((s) == (_dafny.Seq("aws-kms-hierarchy")))) or ((s) == (_dafny.Seq("aws-kms-rsa")))

    @staticmethod
    def RawAlgorithmString_q(s):
        return ((s) == (_dafny.Seq("aes"))) or ((s) == (_dafny.Seq("rsa")))

    @staticmethod
    def PaddingAlgorithmString_q(s):
        return ((s) == (_dafny.Seq("pkcs1"))) or ((s) == (_dafny.Seq("oaep-mgf1")))

    @staticmethod
    def PaddingHashString_q(s):
        return (((((s) == (_dafny.Seq("sha1"))) or ((s) == (_dafny.Seq("sha1")))) or ((s) == (_dafny.Seq("sha256")))) or ((s) == (_dafny.Seq("sha384")))) or ((s) == (_dafny.Seq("sha512")))

    @staticmethod
    def EncryptionAlgorithmSpec_q(s):
        return ((s) == (_dafny.Seq("RSAES_OAEP_SHA_1"))) or ((s) == (_dafny.Seq("RSAES_OAEP_SHA_256")))

