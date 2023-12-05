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
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
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
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
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
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
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
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers

# Module: KeyDescription

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
        d_180_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("KeyDescription not an object"))
        if (d_180_valueOrError0_).IsFailure():
            return (d_180_valueOrError0_).PropagateFailure()
        elif True:
            d_181_obj_ = (obj).obj
            d_182_typString_ = _dafny.Seq("type")
            d_183_valueOrError1_ = JSONHelpers.default__.GetString(d_182_typString_, d_181_obj_)
            if (d_183_valueOrError1_).IsFailure():
                return (d_183_valueOrError1_).PropagateFailure()
            elif True:
                d_184_typ_ = (d_183_valueOrError1_).Extract()
                d_185_valueOrError2_ = Wrappers.default__.Need(default__.KeyDescriptionString_q(d_184_typ_), (_dafny.Seq("Unsupported KeyDescription type:")) + (d_184_typ_))
                if (d_185_valueOrError2_).IsFailure():
                    return (d_185_valueOrError2_).PropagateFailure()
                elif True:
                    if (d_184_typ_) == (_dafny.Seq("aws-kms-mrk-aware-discovery")):
                        d_186_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("default-mrk-region"), d_181_obj_)
                        if (d_186_valueOrError3_).IsFailure():
                            return (d_186_valueOrError3_).PropagateFailure()
                        elif True:
                            d_187_defaultMrkRegion_ = (d_186_valueOrError3_).Extract()
                            d_188_filter_ = JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), d_181_obj_)
                            d_189_awsKmsDiscoveryFilter_ = default__.ToDiscoveryFilter(d_181_obj_)
                            return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrkDiscovery(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq("aws-kms-mrk-aware-discovery"), d_187_defaultMrkRegion_, d_189_awsKmsDiscoveryFilter_)))
                    elif True:
                        d_190_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("key"), d_181_obj_)
                        if (d_190_valueOrError4_).IsFailure():
                            return (d_190_valueOrError4_).PropagateFailure()
                        elif True:
                            d_191_key_ = (d_190_valueOrError4_).Extract()
                            if (d_184_typ_) == (_dafny.Seq("static-material-keyring")):
                                return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Static(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring_StaticKeyring(d_191_key_)))
                            elif (d_184_typ_) == (_dafny.Seq("aws-kms")):
                                return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Kms(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo_KMSInfo(d_191_key_)))
                            elif (d_184_typ_) == (_dafny.Seq("aws-kms-mrk-aware")):
                                return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrk(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware_KmsMrkAware(d_191_key_)))
                            elif (d_184_typ_) == (_dafny.Seq("aws-kms-rsa")):
                                d_192_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_181_obj_)
                                if (d_192_valueOrError5_).IsFailure():
                                    return (d_192_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_193_encryptionAlgorithmString_ = (d_192_valueOrError5_).Extract()
                                    d_194_valueOrError6_ = Wrappers.default__.Need(default__.EncryptionAlgorithmSpec_q(d_193_encryptionAlgorithmString_), (_dafny.Seq("Unsupported EncryptionAlgorithmSpec:")) + (d_193_encryptionAlgorithmString_))
                                    if (d_194_valueOrError6_).IsFailure():
                                        return (d_194_valueOrError6_).PropagateFailure()
                                    elif True:
                                        d_195_encryptionAlgorithm_ = (software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1() if (d_193_encryptionAlgorithmString_) == (_dafny.Seq("RSAES_OAEP_SHA_1")) else software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256())
                                        return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsRsa(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring_KmsRsaKeyring(d_191_key_, d_195_encryptionAlgorithm_)))
                            elif (d_184_typ_) == (_dafny.Seq("aws-kms-hierarchy")):
                                return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Hierarchy(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring_HierarchyKeyring(d_191_key_)))
                            elif True:
                                d_196_valueOrError7_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_181_obj_)
                                if (d_196_valueOrError7_).IsFailure():
                                    return (d_196_valueOrError7_).PropagateFailure()
                                elif True:
                                    d_197_algorithm_ = (d_196_valueOrError7_).Extract()
                                    d_198_valueOrError8_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), d_181_obj_)
                                    if (d_198_valueOrError8_).IsFailure():
                                        return (d_198_valueOrError8_).PropagateFailure()
                                    elif True:
                                        d_199_providerId_ = (d_198_valueOrError8_).Extract()
                                        d_200_valueOrError9_ = Wrappers.default__.Need(default__.RawAlgorithmString_q(d_197_algorithm_), (_dafny.Seq("Unsupported algorithm:")) + (d_197_algorithm_))
                                        if (d_200_valueOrError9_).IsFailure():
                                            return (d_200_valueOrError9_).PropagateFailure()
                                        elif True:
                                            if (d_197_algorithm_) == (_dafny.Seq("aes")):
                                                return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES_RawAES(d_191_key_, d_199_providerId_)))
                                            elif True:
                                                d_201_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-algorithm"), d_181_obj_)
                                                if (d_201_valueOrError10_).IsFailure():
                                                    return (d_201_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_202_paddingAlgorithm_ = (d_201_valueOrError10_).Extract()
                                                    d_203_valueOrError11_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-hash"), d_181_obj_)
                                                    if (d_203_valueOrError11_).IsFailure():
                                                        return (d_203_valueOrError11_).PropagateFailure()
                                                    elif True:
                                                        d_204_paddingHash_ = (d_203_valueOrError11_).Extract()
                                                        d_205_valueOrError12_ = Wrappers.default__.Need(default__.PaddingAlgorithmString_q(d_202_paddingAlgorithm_), (_dafny.Seq("Unsupported paddingAlgorithm:")) + (d_202_paddingAlgorithm_))
                                                        if (d_205_valueOrError12_).IsFailure():
                                                            return (d_205_valueOrError12_).PropagateFailure()
                                                        elif True:
                                                            d_206_valueOrError13_ = Wrappers.default__.Need(default__.PaddingHashString_q(d_204_paddingHash_), (_dafny.Seq("Unsupported paddingHash:")) + (d_204_paddingHash_))
                                                            if (d_206_valueOrError13_).IsFailure():
                                                                return (d_206_valueOrError13_).PropagateFailure()
                                                            elif True:
                                                                if (d_202_paddingAlgorithm_) == (_dafny.Seq("pkcs1")):
                                                                    d_207_valueOrError14_ = Wrappers.default__.Need((d_204_paddingHash_) == (_dafny.Seq("sha1")), (_dafny.Seq("Unsupported padding with pkcs1:")) + (d_204_paddingHash_))
                                                                    if (d_207_valueOrError14_).IsFailure():
                                                                        return (d_207_valueOrError14_).PropagateFailure()
                                                                    elif True:
                                                                        return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA_RawRSA(d_191_key_, d_199_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_PKCS1())))
                                                                elif True:
                                                                    if (d_204_paddingHash_) == (_dafny.Seq("sha1")):
                                                                        return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA_RawRSA(d_191_key_, d_199_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1())))
                                                                    elif (d_204_paddingHash_) == (_dafny.Seq("sha256")):
                                                                        return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA_RawRSA(d_191_key_, d_199_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA256__MGF1())))
                                                                    elif (d_204_paddingHash_) == (_dafny.Seq("sha384")):
                                                                        return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA_RawRSA(d_191_key_, d_199_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA384__MGF1())))
                                                                    elif True:
                                                                        return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA_RawRSA(d_191_key_, d_199_providerId_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA512__MGF1())))

    @staticmethod
    def ToDiscoveryFilter(obj):
        d_208_valueOrError0_ = (JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)).ToOption()
        if (d_208_valueOrError0_).IsFailure():
            return (d_208_valueOrError0_).PropagateFailure()
        elif True:
            d_209_filter_ = (d_208_valueOrError0_).Extract()
            d_210_valueOrError1_ = (JSONHelpers.default__.GetString(_dafny.Seq("partition"), d_209_filter_)).ToOption()
            if (d_210_valueOrError1_).IsFailure():
                return (d_210_valueOrError1_).PropagateFailure()
            elif True:
                d_211_partition_ = (d_210_valueOrError1_).Extract()
                d_212_valueOrError2_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("account-ids"), d_209_filter_)).ToOption()
                if (d_212_valueOrError2_).IsFailure():
                    return (d_212_valueOrError2_).PropagateFailure()
                elif True:
                    d_213_accountIds_ = (d_212_valueOrError2_).Extract()
                    return Wrappers.Option_Some(software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter(d_213_accountIds_, d_211_partition_))

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

