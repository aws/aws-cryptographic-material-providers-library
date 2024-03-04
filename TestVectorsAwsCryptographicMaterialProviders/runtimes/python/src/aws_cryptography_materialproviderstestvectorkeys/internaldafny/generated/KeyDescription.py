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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
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
import AesKdfCtr
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
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import MplManifestOptions
import AllAlgorithmSuites
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
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
    def ToKeyDescription(json):
        if (json).is_Array:
            d_72_valueOrError0_ = Wrappers.default__.Need((1) <= (len((json).arr)), _dafny.Seq("Need at least one element in a JSON Array."))
            if (d_72_valueOrError0_).IsFailure():
                return (d_72_valueOrError0_).PropagateFailure()
            elif True:
                def lambda7_(forall_var_7_):
                    d_74_c_: JSON_Values.JSON = forall_var_7_
                    return not ((d_74_c_) in ((json).arr)) or ((d_74_c_).is_Object)

                d_73_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((json).arr).UniqueElements, True, lambda7_), _dafny.Seq("No nested arrays."))
                if (d_73_valueOrError1_).IsFailure():
                    return (d_73_valueOrError1_).PropagateFailure()
                elif True:
                    return default__.ToMultiKeyring(json, Wrappers.Option_Some(((json).arr)[0]), _dafny.Seq(((json).arr)[1::]))
        elif True:
            d_75_valueOrError2_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("KeyDescription not an object"))
            if (d_75_valueOrError2_).IsFailure():
                return (d_75_valueOrError2_).PropagateFailure()
            elif True:
                d_76_obj_ = (json).obj
                d_77_typString_ = _dafny.Seq("type")
                d_78_valueOrError3_ = JSONHelpers.default__.GetString(d_77_typString_, d_76_obj_)
                if (d_78_valueOrError3_).IsFailure():
                    return (d_78_valueOrError3_).PropagateFailure()
                elif True:
                    d_79_typ_ = (d_78_valueOrError3_).Extract()
                    d_80_valueOrError4_ = Wrappers.default__.Need(default__.KeyDescriptionString_q(d_79_typ_), (_dafny.Seq("Unsupported KeyDescription type:")) + (d_79_typ_))
                    if (d_80_valueOrError4_).IsFailure():
                        return (d_80_valueOrError4_).PropagateFailure()
                    elif True:
                        if (d_79_typ_) == (_dafny.Seq("aws-kms-mrk-aware-discovery")):
                            return default__.ToAwsKmsMrkAwareDiscovery(d_76_obj_)
                        elif (d_79_typ_) == (_dafny.Seq("multi-keyring")):
                            d_81_generatorJson_ = (JSONHelpers.default__.Get(_dafny.Seq("generator"), d_76_obj_)).ToOption()
                            d_82_valueOrError5_ = JSONHelpers.default__.GetArray(_dafny.Seq("childKeyrings"), d_76_obj_)
                            if (d_82_valueOrError5_).IsFailure():
                                return (d_82_valueOrError5_).PropagateFailure()
                            elif True:
                                d_83_childKeyringsJson_ = (d_82_valueOrError5_).Extract()
                                return default__.ToMultiKeyring(json, d_81_generatorJson_, d_83_childKeyringsJson_)
                        elif (d_79_typ_) == (_dafny.Seq("required-encryption-context-cmm")):
                            d_84_valueOrError6_ = JSONHelpers.default__.Get(_dafny.Seq("underlying"), d_76_obj_)
                            if (d_84_valueOrError6_).IsFailure():
                                return (d_84_valueOrError6_).PropagateFailure()
                            elif True:
                                d_85_u_ = (d_84_valueOrError6_).Extract()
                                d_86_valueOrError7_ = default__.ToKeyDescription(d_85_u_)
                                if (d_86_valueOrError7_).IsFailure():
                                    return (d_86_valueOrError7_).PropagateFailure()
                                elif True:
                                    d_87_underlying_ = (d_86_valueOrError7_).Extract()
                                    d_88_requiredEncryptionContextStrings_ = ((JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_76_obj_)).ToOption()).UnwrapOr(_dafny.Seq([]))
                                    d_89_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_88_requiredEncryptionContextStrings_)
                                    if (d_89_valueOrError8_).IsFailure():
                                        return (d_89_valueOrError8_).PropagateFailure()
                                    elif True:
                                        d_90_requiredEncryptionContextKeys_ = (d_89_valueOrError8_).Extract()
                                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RequiredEncryptionContext(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(d_87_underlying_, d_90_requiredEncryptionContextKeys_)))
                        elif True:
                            d_91_valueOrError9_ = JSONHelpers.default__.GetString(_dafny.Seq("key"), d_76_obj_)
                            if (d_91_valueOrError9_).IsFailure():
                                return (d_91_valueOrError9_).PropagateFailure()
                            elif True:
                                d_92_key_ = (d_91_valueOrError9_).Extract()
                                if (d_79_typ_) == (_dafny.Seq("static-material-keyring")):
                                    return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Static(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.StaticKeyring_StaticKeyring(d_92_key_)))
                                elif (d_79_typ_) == (_dafny.Seq("aws-kms")):
                                    return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KMSInfo_KMSInfo(d_92_key_)))
                                elif (d_79_typ_) == (_dafny.Seq("aws-kms-mrk-aware")):
                                    return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrk(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAware_KmsMrkAware(d_92_key_)))
                                elif (d_79_typ_) == (_dafny.Seq("aws-kms-rsa")):
                                    return default__.ToAwsKmsRsa(d_92_key_, d_76_obj_)
                                elif (d_79_typ_) == (_dafny.Seq("aws-kms-hierarchy")):
                                    return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Hierarchy(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.HierarchyKeyring_HierarchyKeyring(d_92_key_)))
                                elif True:
                                    d_93_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_76_obj_)
                                    if (d_93_valueOrError10_).IsFailure():
                                        return (d_93_valueOrError10_).PropagateFailure()
                                    elif True:
                                        d_94_algorithm_ = (d_93_valueOrError10_).Extract()
                                        d_95_valueOrError11_ = Wrappers.default__.Need(default__.RawAlgorithmString_q(d_94_algorithm_), (_dafny.Seq("Unsupported algorithm:")) + (d_94_algorithm_))
                                        if (d_95_valueOrError11_).IsFailure():
                                            return (d_95_valueOrError11_).PropagateFailure()
                                        elif True:
                                            if (d_94_algorithm_) == (_dafny.Seq("aes")):
                                                return default__.ToRawAes(d_92_key_, d_76_obj_)
                                            elif True:
                                                return default__.ToRawRsa(d_92_key_, d_76_obj_)

    @staticmethod
    def ToDiscoveryFilter(obj):
        d_96_valueOrError0_ = (JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)).ToOption()
        if (d_96_valueOrError0_).IsFailure():
            return (d_96_valueOrError0_).PropagateFailure()
        elif True:
            d_97_filter_ = (d_96_valueOrError0_).Extract()
            d_98_valueOrError1_ = (JSONHelpers.default__.GetString(_dafny.Seq("partition"), d_97_filter_)).ToOption()
            if (d_98_valueOrError1_).IsFailure():
                return (d_98_valueOrError1_).PropagateFailure()
            elif True:
                d_99_partition_ = (d_98_valueOrError1_).Extract()
                d_100_valueOrError2_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("account-ids"), d_97_filter_)).ToOption()
                if (d_100_valueOrError2_).IsFailure():
                    return (d_100_valueOrError2_).PropagateFailure()
                elif True:
                    d_101_accountIds_ = (d_100_valueOrError2_).Extract()
                    return Wrappers.Option_Some(software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter(d_101_accountIds_, d_99_partition_))

    @staticmethod
    def ToAwsKmsMrkAwareDiscovery(obj):
        d_102_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("default-mrk-region"), obj)
        if (d_102_valueOrError0_).IsFailure():
            return (d_102_valueOrError0_).PropagateFailure()
        elif True:
            d_103_defaultMrkRegion_ = (d_102_valueOrError0_).Extract()
            d_104_filter_ = JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)
            d_105_awsKmsDiscoveryFilter_ = default__.ToDiscoveryFilter(obj)
            return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsMrkDiscovery(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq("aws-kms-mrk-aware-discovery"), d_103_defaultMrkRegion_, d_105_awsKmsDiscoveryFilter_)))

    @staticmethod
    def ToAwsKmsRsa(key, obj):
        d_106_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), obj)
        if (d_106_valueOrError0_).IsFailure():
            return (d_106_valueOrError0_).PropagateFailure()
        elif True:
            d_107_encryptionAlgorithmString_ = (d_106_valueOrError0_).Extract()
            d_108_valueOrError1_ = Wrappers.default__.Need((d_107_encryptionAlgorithmString_) in (default__.String2EncryptionAlgorithmSpec), (_dafny.Seq("Unsupported EncryptionAlgorithmSpec:")) + (d_107_encryptionAlgorithmString_))
            if (d_108_valueOrError1_).IsFailure():
                return (d_108_valueOrError1_).PropagateFailure()
            elif True:
                d_109_encryptionAlgorithm_ = (default__.String2EncryptionAlgorithmSpec)[d_107_encryptionAlgorithmString_]
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsRsa(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsRsaKeyring_KmsRsaKeyring(key, d_109_encryptionAlgorithm_)))

    @staticmethod
    def ToRawAes(key, obj):
        d_110_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_110_valueOrError0_).IsFailure():
            return (d_110_valueOrError0_).PropagateFailure()
        elif True:
            d_111_providerId_ = (d_110_valueOrError0_).Extract()
            return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES(key, d_111_providerId_)))

    @staticmethod
    def ToRawRsa(key, obj):
        d_112_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_112_valueOrError0_).IsFailure():
            return (d_112_valueOrError0_).PropagateFailure()
        elif True:
            d_113_providerId_ = (d_112_valueOrError0_).Extract()
            d_114_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-algorithm"), obj)
            if (d_114_valueOrError1_).IsFailure():
                return (d_114_valueOrError1_).PropagateFailure()
            elif True:
                d_115_paddingAlgorithm_ = (d_114_valueOrError1_).Extract()
                d_116_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("padding-hash"), obj)
                if (d_116_valueOrError2_).IsFailure():
                    return (d_116_valueOrError2_).PropagateFailure()
                elif True:
                    d_117_maybePaddingHash_ = (d_116_valueOrError2_).Extract()
                    d_118_valueOrError3_ = Wrappers.default__.Need(not ((d_117_maybePaddingHash_).is_None) or ((d_115_paddingAlgorithm_) == (_dafny.Seq("pkcs1"))), _dafny.Seq("oaep-mgf1 MUST define padding-hash"))
                    if (d_118_valueOrError3_).IsFailure():
                        return (d_118_valueOrError3_).PropagateFailure()
                    elif True:
                        d_119_paddingHash_ = (d_117_maybePaddingHash_).UnwrapOr(_dafny.Seq("sha1"))
                        d_120_valueOrError4_ = Wrappers.default__.Need(((d_115_paddingAlgorithm_, d_119_paddingHash_)) in (default__.String2PaddingAlgorithm), (((_dafny.Seq("Unsupported padding:")) + (d_115_paddingAlgorithm_)) + (_dafny.Seq(" hash:"))) + (d_119_paddingHash_))
                        if (d_120_valueOrError4_).IsFailure():
                            return (d_120_valueOrError4_).PropagateFailure()
                        elif True:
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(key, d_113_providerId_, (default__.String2PaddingAlgorithm)[(d_115_paddingAlgorithm_, d_119_paddingHash_)])))

    @staticmethod
    def ToMultiKeyring(json, generatorJson, childKeyringsJson):
        d_121_valueOrError0_ = Wrappers.default__.Need(not ((generatorJson).is_Some) or (((generatorJson).value).is_Object), _dafny.Seq("Not an object"))
        if (d_121_valueOrError0_).IsFailure():
            return (d_121_valueOrError0_).PropagateFailure()
        elif True:
            def iife5_(_pat_let0_0):
                def iife6_(d_123_valueOrError2_):
                    def iife7_(_pat_let1_0):
                        def iife8_(d_124_g_):
                            return Wrappers.Result_Success(Wrappers.Option_Some(d_124_g_))
                        return iife8_(_pat_let1_0)
                    return ((d_123_valueOrError2_).PropagateFailure() if (d_123_valueOrError2_).IsFailure() else iife7_((d_123_valueOrError2_).Extract()))
                return iife6_(_pat_let0_0)
            d_122_valueOrError1_ = (iife5_(default__.ToKeyDescription((generatorJson).value)) if (generatorJson).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
            if (d_122_valueOrError1_).IsFailure():
                return (d_122_valueOrError1_).PropagateFailure()
            elif True:
                d_125_generator_ = (d_122_valueOrError1_).Extract()
                def lambda8_(d_127_childKeyringsJson_):
                    def lambda9_(d_128_c_):
                        return default__.ToKeyDescription(d_128_c_)

                    return lambda9_

                d_126_valueOrError3_ = Seq.default__.MapWithResult(lambda8_(childKeyringsJson), childKeyringsJson)
                if (d_126_valueOrError3_).IsFailure():
                    return (d_126_valueOrError3_).PropagateFailure()
                elif True:
                    d_129_childKeyrings_ = (d_126_valueOrError3_).Extract()
                    return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Multi(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.MultiKeyring_MultiKeyring(d_125_generator_, d_129_childKeyrings_)))

    @staticmethod
    def KeyDescriptionString_q(s):
        return (((((((((s) == (_dafny.Seq("static-material-keyring"))) or ((s) == (_dafny.Seq("aws-kms")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware-discovery")))) or ((s) == (_dafny.Seq("raw")))) or ((s) == (_dafny.Seq("aws-kms-hierarchy")))) or ((s) == (_dafny.Seq("aws-kms-rsa")))) or ((s) == (_dafny.Seq("required-encryption-context-cmm")))) or ((s) == (_dafny.Seq("multi-keyring")))

    @staticmethod
    def RawAlgorithmString_q(s):
        return ((s) == (_dafny.Seq("aes"))) or ((s) == (_dafny.Seq("rsa")))

    @staticmethod
    def KeyDescriptionVersion_q(v):
        return (((v) == (1)) or ((v) == (2))) or ((v) == (3))

    @staticmethod
    def ToJson(keyDescription, outputVersion):
        source1_ = keyDescription
        if source1_.is_Kms:
            d_130___mcc_h0_ = source1_.Kms
            d_131_Kms_ = d_130___mcc_h0_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_131_Kms_).keyId))])))
        elif source1_.is_KmsMrk:
            d_132___mcc_h1_ = source1_.KmsMrk
            d_133_KmsMrk_ = d_132___mcc_h1_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_133_KmsMrk_).keyId))])))
        elif source1_.is_KmsMrkDiscovery:
            d_134___mcc_h2_ = source1_.KmsMrkDiscovery
            d_135_KmsMrkDiscovery_ = d_134___mcc_h2_
            def lambda10_(d_137_s_):
                return JSON_Values.JSON_String(d_137_s_)

            d_136_filter_ = (_dafny.Seq([(_dafny.Seq("aws-kms-discovery-filter"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("partition"), JSON_Values.JSON_String((((d_135_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).partition)), (_dafny.Seq("account-ids"), JSON_Values.JSON_Array(Seq.default__.Map(lambda10_, (((d_135_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).accountIds)))])))]) if ((d_135_KmsMrkDiscovery_).awsKmsDiscoveryFilter).is_Some else _dafny.Seq([]))
            return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_Values.JSON_String((d_135_KmsMrkDiscovery_).defaultMrkRegion))])) + (d_136_filter_)))
        elif source1_.is_RSA:
            d_138___mcc_h3_ = source1_.RSA
            d_139_RSA_ = d_138___mcc_h3_
            d_140_padding_ = (default__.PaddingAlgorithmString2String)[(d_139_RSA_).padding]
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_139_RSA_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_139_RSA_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("rsa"))), (_dafny.Seq("padding-algorithm"), JSON_Values.JSON_String((d_140_padding_)[0])), (_dafny.Seq("padding-hash"), JSON_Values.JSON_String((d_140_padding_)[1]))])))
        elif source1_.is_AES:
            d_141___mcc_h4_ = source1_.AES
            d_142_AES_ = d_141___mcc_h4_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_142_AES_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_142_AES_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("aes")))])))
        elif source1_.is_Static:
            d_143___mcc_h5_ = source1_.Static
            d_144_Static_ = d_143___mcc_h5_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("static-material-keyring"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_144_Static_).keyId))])))
        elif source1_.is_KmsRsa:
            d_145___mcc_h6_ = source1_.KmsRsa
            d_146_KmsRsa_ = d_145___mcc_h6_
            d_147_valueOrError0_ = Wrappers.default__.Need(((d_146_KmsRsa_).encryptionAlgorithm) in (default__.EncryptionAlgorithmSpec2String), _dafny.Seq("Unsupported encryptionAlgorithm"))
            if (d_147_valueOrError0_).IsFailure():
                return (d_147_valueOrError0_).PropagateFailure()
            elif True:
                d_148_encryptionAlgorithm_ = (default__.EncryptionAlgorithmSpec2String)[(d_146_KmsRsa_).encryptionAlgorithm]
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_146_KmsRsa_).keyId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(d_148_encryptionAlgorithm_))])))
        elif source1_.is_Hierarchy:
            d_149___mcc_h7_ = source1_.Hierarchy
            d_150_Hierarchy_ = d_149___mcc_h7_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_150_Hierarchy_).keyId))])))
        elif source1_.is_Multi:
            d_151___mcc_h8_ = source1_.Multi
            d_152_MultiKeyring_ = d_151___mcc_h8_
            def lambda11_(forall_var_8_):
                d_154_c_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription = forall_var_8_
                return not ((d_154_c_) in ((d_152_MultiKeyring_).childKeyrings)) or (default__.Keyring_q(d_154_c_))

            d_153_valueOrError1_ = Wrappers.default__.Need((not (((d_152_MultiKeyring_).generator).is_Some) or (default__.Keyring_q(((d_152_MultiKeyring_).generator).value))) and (_dafny.quantifier(((d_152_MultiKeyring_).childKeyrings).UniqueElements, True, lambda11_)), _dafny.Seq("CMMs not supported by Multi Keyrings"))
            if (d_153_valueOrError1_).IsFailure():
                return (d_153_valueOrError1_).PropagateFailure()
            elif True:
                if (outputVersion) == (3):
                    def iife9_(_pat_let2_0):
                        def iife10_(d_156_valueOrError3_):
                            def iife11_(_pat_let3_0):
                                def iife12_(d_157_g_):
                                    return Wrappers.Result_Success(Wrappers.Option_Some(d_157_g_))
                                return iife12_(_pat_let3_0)
                            return ((d_156_valueOrError3_).PropagateFailure() if (d_156_valueOrError3_).IsFailure() else iife11_((d_156_valueOrError3_).Extract()))
                        return iife10_(_pat_let2_0)
                    d_155_valueOrError2_ = (iife9_(default__.ToJson(((d_152_MultiKeyring_).generator).value, outputVersion)) if ((d_152_MultiKeyring_).generator).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                    if (d_155_valueOrError2_).IsFailure():
                        return (d_155_valueOrError2_).PropagateFailure()
                    elif True:
                        d_158_generator_ = (d_155_valueOrError2_).Extract()
                        d_159_valueOrError4_ = default__.KeyDescriptionListToJson((d_152_MultiKeyring_).childKeyrings, outputVersion)
                        if (d_159_valueOrError4_).IsFailure():
                            return (d_159_valueOrError4_).PropagateFailure()
                        elif True:
                            d_160_childKeyrings_ = (d_159_valueOrError4_).Extract()
                            return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("multi-keyring"))), (_dafny.Seq("childKeyrings"), JSON_Values.JSON_Array(d_160_childKeyrings_))])) + ((_dafny.Seq([(_dafny.Seq("generator"), (d_158_generator_).value)]) if (d_158_generator_).is_Some else _dafny.Seq([])))))
                elif True:
                    d_161_valueOrError5_ = Wrappers.default__.Need(((d_152_MultiKeyring_).generator).is_Some, _dafny.Seq("Generator required for v1 or v2"))
                    if (d_161_valueOrError5_).IsFailure():
                        return (d_161_valueOrError5_).PropagateFailure()
                    elif True:
                        d_162_keyrings_ = (_dafny.Seq([((d_152_MultiKeyring_).generator).value])) + ((d_152_MultiKeyring_).childKeyrings)
                        def lambda12_(forall_var_9_):
                            d_164_c_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription = forall_var_9_
                            return not ((d_164_c_) in (d_162_keyrings_)) or (not((d_164_c_).is_Multi))

                        d_163_valueOrError6_ = Wrappers.default__.Need(_dafny.quantifier((d_162_keyrings_).UniqueElements, True, lambda12_), _dafny.Seq("Recursive structures not supported"))
                        if (d_163_valueOrError6_).IsFailure():
                            return (d_163_valueOrError6_).PropagateFailure()
                        elif True:
                            d_165_valueOrError7_ = default__.KeyDescriptionListToJson((d_152_MultiKeyring_).childKeyrings, outputVersion)
                            if (d_165_valueOrError7_).IsFailure():
                                return (d_165_valueOrError7_).PropagateFailure()
                            elif True:
                                d_166_keyrings_ = (d_165_valueOrError7_).Extract()
                                return Wrappers.Result_Success(JSON_Values.JSON_Array(d_166_keyrings_))
        elif True:
            d_167___mcc_h9_ = source1_.RequiredEncryptionContext
            d_168_RequiredEncryptionContext_ = d_167___mcc_h9_
            d_169_valueOrError8_ = default__.ToJson((d_168_RequiredEncryptionContext_).underlying, outputVersion)
            if (d_169_valueOrError8_).IsFailure():
                return (d_169_valueOrError8_).PropagateFailure()
            elif True:
                d_170_underlying_ = (d_169_valueOrError8_).Extract()
                def lambda13_(d_172_key_):
                    def iife13_(_pat_let4_0):
                        def iife14_(d_173_valueOrError10_):
                            def iife15_(_pat_let5_0):
                                def iife16_(d_174_s_):
                                    return Wrappers.Result_Success(JSON_Values.JSON_String(d_174_s_))
                                return iife16_(_pat_let5_0)
                            return ((d_173_valueOrError10_).PropagateFailure() if (d_173_valueOrError10_).IsFailure() else iife15_((d_173_valueOrError10_).Extract()))
                        return iife14_(_pat_let4_0)
                    return iife13_(UTF8.default__.Decode(d_172_key_))

                d_171_valueOrError9_ = Seq.default__.MapWithResult(lambda13_, (d_168_RequiredEncryptionContext_).requiredEncryptionContextKeys)
                if (d_171_valueOrError9_).IsFailure():
                    return (d_171_valueOrError9_).PropagateFailure()
                elif True:
                    d_175_requiredEncryptionContextKeys_ = (d_171_valueOrError9_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("required-encryption-context-cmm"))), (_dafny.Seq("underlying"), d_170_underlying_), (_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(d_175_requiredEncryptionContextKeys_))])))

    @staticmethod
    def Keyring_q(description):
        return (((((((((description).is_Kms) or ((description).is_KmsMrk)) or ((description).is_KmsMrkDiscovery)) or ((description).is_RSA)) or ((description).is_AES)) or ((description).is_Static)) or ((description).is_KmsRsa)) or ((description).is_Hierarchy)) or ((description).is_Multi)

    @staticmethod
    def KeyDescriptionListToJson(childKeyrings, outputVersion):
        if (0) == (len(childKeyrings)):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_176_valueOrError0_ = default__.ToJson((childKeyrings)[0], outputVersion)
            if (d_176_valueOrError0_).IsFailure():
                return (d_176_valueOrError0_).PropagateFailure()
            elif True:
                d_177_json_ = (d_176_valueOrError0_).Extract()
                d_178_valueOrError1_ = default__.KeyDescriptionListToJson(_dafny.Seq((childKeyrings)[1::]), outputVersion)
                if (d_178_valueOrError1_).IsFailure():
                    return (d_178_valueOrError1_).PropagateFailure()
                elif True:
                    d_179_rest_ = (d_178_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_177_json_])) + (d_179_rest_))

    @staticmethod
    def Invert(m):
        def iife17_():
            coll5_ = _dafny.Map()
            compr_5_: TypeVar('X__')
            for compr_5_ in (m).keys.Elements:
                d_180_k_: TypeVar('X__') = compr_5_
                if (d_180_k_) in (m):
                    coll5_[(m)[d_180_k_]] = d_180_k_
            return _dafny.Map(coll5_)
        return iife17_()
        

    @_dafny.classproperty
    def EncryptionAlgorithmSpec2String(instance):
        return _dafny.Map({software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(): _dafny.Seq("RSAES_OAEP_SHA_1"), software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256(): _dafny.Seq("RSAES_OAEP_SHA_256")})
    @_dafny.classproperty
    def String2EncryptionAlgorithmSpec(instance):
        return default__.Invert(default__.EncryptionAlgorithmSpec2String)
    @_dafny.classproperty
    def PaddingAlgorithmString2String(instance):
        return _dafny.Map({software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_PKCS1(): (_dafny.Seq("pkcs1"), _dafny.Seq("sha1")), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha1")), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA256__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha256")), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA384__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha384")), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA512__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha512"))})
    @_dafny.classproperty
    def String2PaddingAlgorithm(instance):
        return default__.Invert(default__.PaddingAlgorithmString2String)

class KeyDescriptionVersion:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return 1
