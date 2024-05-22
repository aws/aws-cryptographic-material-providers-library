import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import standard_library.internaldafny.generated.JSON_ZeroCopy as JSON_ZeroCopy
import standard_library.internaldafny.generated.JSON_API as JSON_API
import standard_library.internaldafny.generated.JSON as JSON
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription

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
            d_73_valueOrError0_ = Wrappers.default__.Need((1) <= (len((json).arr)), _dafny.Seq("Need at least one element in a JSON Array."))
            if (d_73_valueOrError0_).IsFailure():
                return (d_73_valueOrError0_).PropagateFailure()
            elif True:
                def lambda7_(forall_var_7_):
                    d_75_c_: JSON_Values.JSON = forall_var_7_
                    return not ((d_75_c_) in ((json).arr)) or ((d_75_c_).is_Object)

                d_74_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((json).arr).UniqueElements, True, lambda7_), _dafny.Seq("No nested arrays."))
                if (d_74_valueOrError1_).IsFailure():
                    return (d_74_valueOrError1_).PropagateFailure()
                elif True:
                    return default__.ToMultiKeyring(json, Wrappers.Option_Some(((json).arr)[0]), _dafny.Seq(((json).arr)[1::]))
        elif True:
            d_76_valueOrError2_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("KeyDescription not an object"))
            if (d_76_valueOrError2_).IsFailure():
                return (d_76_valueOrError2_).PropagateFailure()
            elif True:
                d_77_obj_ = (json).obj
                d_78_typString_ = _dafny.Seq("type")
                d_79_valueOrError3_ = JSONHelpers.default__.GetString(d_78_typString_, d_77_obj_)
                if (d_79_valueOrError3_).IsFailure():
                    return (d_79_valueOrError3_).PropagateFailure()
                elif True:
                    d_80_typ_ = (d_79_valueOrError3_).Extract()
                    d_81_valueOrError4_ = Wrappers.default__.Need(default__.KeyDescriptionString_q(d_80_typ_), (_dafny.Seq("Unsupported KeyDescription type:")) + (d_80_typ_))
                    if (d_81_valueOrError4_).IsFailure():
                        return (d_81_valueOrError4_).PropagateFailure()
                    elif True:
                        if (d_80_typ_) == (_dafny.Seq("aws-kms-mrk-aware-discovery")):
                            return default__.ToAwsKmsMrkAwareDiscovery(d_77_obj_)
                        elif (d_80_typ_) == (_dafny.Seq("multi-keyring")):
                            d_82_generatorJson_ = (JSONHelpers.default__.Get(_dafny.Seq("generator"), d_77_obj_)).ToOption()
                            d_83_valueOrError5_ = JSONHelpers.default__.GetArray(_dafny.Seq("childKeyrings"), d_77_obj_)
                            if (d_83_valueOrError5_).IsFailure():
                                return (d_83_valueOrError5_).PropagateFailure()
                            elif True:
                                d_84_childKeyringsJson_ = (d_83_valueOrError5_).Extract()
                                return default__.ToMultiKeyring(json, d_82_generatorJson_, d_84_childKeyringsJson_)
                        elif (d_80_typ_) == (_dafny.Seq("required-encryption-context-cmm")):
                            d_85_valueOrError6_ = JSONHelpers.default__.Get(_dafny.Seq("underlying"), d_77_obj_)
                            if (d_85_valueOrError6_).IsFailure():
                                return (d_85_valueOrError6_).PropagateFailure()
                            elif True:
                                d_86_u_ = (d_85_valueOrError6_).Extract()
                                d_87_valueOrError7_ = default__.ToKeyDescription(d_86_u_)
                                if (d_87_valueOrError7_).IsFailure():
                                    return (d_87_valueOrError7_).PropagateFailure()
                                elif True:
                                    d_88_underlying_ = (d_87_valueOrError7_).Extract()
                                    d_89_requiredEncryptionContextStrings_ = ((JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_77_obj_)).ToOption()).UnwrapOr(_dafny.Seq([]))
                                    d_90_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_89_requiredEncryptionContextStrings_)
                                    if (d_90_valueOrError8_).IsFailure():
                                        return (d_90_valueOrError8_).PropagateFailure()
                                    elif True:
                                        d_91_requiredEncryptionContextKeys_ = (d_90_valueOrError8_).Extract()
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RequiredEncryptionContext(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(d_88_underlying_, d_91_requiredEncryptionContextKeys_)))
                        elif True:
                            d_92_valueOrError9_ = JSONHelpers.default__.GetString(_dafny.Seq("key"), d_77_obj_)
                            if (d_92_valueOrError9_).IsFailure():
                                return (d_92_valueOrError9_).PropagateFailure()
                            elif True:
                                d_93_key_ = (d_92_valueOrError9_).Extract()
                                if (d_80_typ_) == (_dafny.Seq("static-material-keyring")):
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(d_93_key_)))
                                elif (d_80_typ_) == (_dafny.Seq("aws-kms")):
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Kms(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo_KMSInfo(d_93_key_)))
                                elif (d_80_typ_) == (_dafny.Seq("aws-kms-mrk-aware")):
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrk(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware_KmsMrkAware(d_93_key_)))
                                elif (d_80_typ_) == (_dafny.Seq("aws-kms-rsa")):
                                    return default__.ToAwsKmsRsa(d_93_key_, d_77_obj_)
                                elif (d_80_typ_) == (_dafny.Seq("aws-kms-hierarchy")):
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Hierarchy(AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring_HierarchyKeyring(d_93_key_)))
                                elif True:
                                    d_94_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_77_obj_)
                                    if (d_94_valueOrError10_).IsFailure():
                                        return (d_94_valueOrError10_).PropagateFailure()
                                    elif True:
                                        d_95_algorithm_ = (d_94_valueOrError10_).Extract()
                                        d_96_valueOrError11_ = Wrappers.default__.Need(default__.RawAlgorithmString_q(d_95_algorithm_), (_dafny.Seq("Unsupported algorithm:")) + (d_95_algorithm_))
                                        if (d_96_valueOrError11_).IsFailure():
                                            return (d_96_valueOrError11_).PropagateFailure()
                                        elif True:
                                            if (d_95_algorithm_) == (_dafny.Seq("aes")):
                                                return default__.ToRawAes(d_93_key_, d_77_obj_)
                                            elif True:
                                                return default__.ToRawRsa(d_93_key_, d_77_obj_)

    @staticmethod
    def ToDiscoveryFilter(obj):
        d_97_valueOrError0_ = (JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)).ToOption()
        if (d_97_valueOrError0_).IsFailure():
            return (d_97_valueOrError0_).PropagateFailure()
        elif True:
            d_98_filter_ = (d_97_valueOrError0_).Extract()
            d_99_valueOrError1_ = (JSONHelpers.default__.GetString(_dafny.Seq("partition"), d_98_filter_)).ToOption()
            if (d_99_valueOrError1_).IsFailure():
                return (d_99_valueOrError1_).PropagateFailure()
            elif True:
                d_100_partition_ = (d_99_valueOrError1_).Extract()
                d_101_valueOrError2_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("account-ids"), d_98_filter_)).ToOption()
                if (d_101_valueOrError2_).IsFailure():
                    return (d_101_valueOrError2_).PropagateFailure()
                elif True:
                    d_102_accountIds_ = (d_101_valueOrError2_).Extract()
                    return Wrappers.Option_Some(AwsCryptographyMaterialProvidersTypes.DiscoveryFilter_DiscoveryFilter(d_102_accountIds_, d_100_partition_))

    @staticmethod
    def ToAwsKmsMrkAwareDiscovery(obj):
        d_103_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("default-mrk-region"), obj)
        if (d_103_valueOrError0_).IsFailure():
            return (d_103_valueOrError0_).PropagateFailure()
        elif True:
            d_104_defaultMrkRegion_ = (d_103_valueOrError0_).Extract()
            d_105_filter_ = JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)
            d_106_awsKmsDiscoveryFilter_ = default__.ToDiscoveryFilter(obj)
            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrkDiscovery(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq("aws-kms-mrk-aware-discovery"), d_104_defaultMrkRegion_, d_106_awsKmsDiscoveryFilter_)))

    @staticmethod
    def ToAwsKmsRsa(key, obj):
        d_107_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), obj)
        if (d_107_valueOrError0_).IsFailure():
            return (d_107_valueOrError0_).PropagateFailure()
        elif True:
            d_108_encryptionAlgorithmString_ = (d_107_valueOrError0_).Extract()
            d_109_valueOrError1_ = Wrappers.default__.Need((d_108_encryptionAlgorithmString_) in (default__.String2EncryptionAlgorithmSpec), (_dafny.Seq("Unsupported EncryptionAlgorithmSpec:")) + (d_108_encryptionAlgorithmString_))
            if (d_109_valueOrError1_).IsFailure():
                return (d_109_valueOrError1_).PropagateFailure()
            elif True:
                d_110_encryptionAlgorithm_ = (default__.String2EncryptionAlgorithmSpec)[d_108_encryptionAlgorithmString_]
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsRsa(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring_KmsRsaKeyring(key, d_110_encryptionAlgorithm_)))

    @staticmethod
    def ToRawAes(key, obj):
        d_111_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_111_valueOrError0_).IsFailure():
            return (d_111_valueOrError0_).PropagateFailure()
        elif True:
            d_112_providerId_ = (d_111_valueOrError0_).Extract()
            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_AES(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES_RawAES(key, d_112_providerId_)))

    @staticmethod
    def ToRawRsa(key, obj):
        d_113_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_113_valueOrError0_).IsFailure():
            return (d_113_valueOrError0_).PropagateFailure()
        elif True:
            d_114_providerId_ = (d_113_valueOrError0_).Extract()
            d_115_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-algorithm"), obj)
            if (d_115_valueOrError1_).IsFailure():
                return (d_115_valueOrError1_).PropagateFailure()
            elif True:
                d_116_paddingAlgorithm_ = (d_115_valueOrError1_).Extract()
                d_117_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("padding-hash"), obj)
                if (d_117_valueOrError2_).IsFailure():
                    return (d_117_valueOrError2_).PropagateFailure()
                elif True:
                    d_118_maybePaddingHash_ = (d_117_valueOrError2_).Extract()
                    d_119_valueOrError3_ = Wrappers.default__.Need(not ((d_118_maybePaddingHash_).is_None) or ((d_116_paddingAlgorithm_) == (_dafny.Seq("pkcs1"))), _dafny.Seq("oaep-mgf1 MUST define padding-hash"))
                    if (d_119_valueOrError3_).IsFailure():
                        return (d_119_valueOrError3_).PropagateFailure()
                    elif True:
                        d_120_paddingHash_ = (d_118_maybePaddingHash_).UnwrapOr(_dafny.Seq("sha1"))
                        d_121_valueOrError4_ = Wrappers.default__.Need(((d_116_paddingAlgorithm_, d_120_paddingHash_)) in (default__.String2PaddingAlgorithm), (((_dafny.Seq("Unsupported padding:")) + (d_116_paddingAlgorithm_)) + (_dafny.Seq(" hash:"))) + (d_120_paddingHash_))
                        if (d_121_valueOrError4_).IsFailure():
                            return (d_121_valueOrError4_).PropagateFailure()
                        elif True:
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RSA(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA_RawRSA(key, d_114_providerId_, (default__.String2PaddingAlgorithm)[(d_116_paddingAlgorithm_, d_120_paddingHash_)])))

    @staticmethod
    def ToMultiKeyring(json, generatorJson, childKeyringsJson):
        d_122_valueOrError0_ = Wrappers.default__.Need(not ((generatorJson).is_Some) or (((generatorJson).value).is_Object), _dafny.Seq("Not an object"))
        if (d_122_valueOrError0_).IsFailure():
            return (d_122_valueOrError0_).PropagateFailure()
        elif True:
            def iife5_(_pat_let0_0):
                def iife6_(d_124_valueOrError2_):
                    def iife7_(_pat_let1_0):
                        def iife8_(d_125_g_):
                            return Wrappers.Result_Success(Wrappers.Option_Some(d_125_g_))
                        return iife8_(_pat_let1_0)
                    return ((d_124_valueOrError2_).PropagateFailure() if (d_124_valueOrError2_).IsFailure() else iife7_((d_124_valueOrError2_).Extract()))
                return iife6_(_pat_let0_0)
            d_123_valueOrError1_ = (iife5_(default__.ToKeyDescription((generatorJson).value)) if (generatorJson).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
            if (d_123_valueOrError1_).IsFailure():
                return (d_123_valueOrError1_).PropagateFailure()
            elif True:
                d_126_generator_ = (d_123_valueOrError1_).Extract()
                def lambda8_(d_128_childKeyringsJson_):
                    def lambda9_(d_129_c_):
                        return default__.ToKeyDescription(d_129_c_)

                    return lambda9_

                d_127_valueOrError3_ = Seq.default__.MapWithResult(lambda8_(childKeyringsJson), childKeyringsJson)
                if (d_127_valueOrError3_).IsFailure():
                    return (d_127_valueOrError3_).PropagateFailure()
                elif True:
                    d_130_childKeyrings_ = (d_127_valueOrError3_).Extract()
                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Multi(AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring_MultiKeyring(d_126_generator_, d_130_childKeyrings_)))

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
            d_131___mcc_h0_ = source1_.Kms
            d_132_Kms_ = d_131___mcc_h0_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_132_Kms_).keyId))])))
        elif source1_.is_KmsMrk:
            d_133___mcc_h1_ = source1_.KmsMrk
            d_134_KmsMrk_ = d_133___mcc_h1_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_134_KmsMrk_).keyId))])))
        elif source1_.is_KmsMrkDiscovery:
            d_135___mcc_h2_ = source1_.KmsMrkDiscovery
            d_136_KmsMrkDiscovery_ = d_135___mcc_h2_
            def lambda10_(d_138_s_):
                return JSON_Values.JSON_String(d_138_s_)

            d_137_filter_ = (_dafny.Seq([(_dafny.Seq("aws-kms-discovery-filter"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("partition"), JSON_Values.JSON_String((((d_136_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).partition)), (_dafny.Seq("account-ids"), JSON_Values.JSON_Array(Seq.default__.Map(lambda10_, (((d_136_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).accountIds)))])))]) if ((d_136_KmsMrkDiscovery_).awsKmsDiscoveryFilter).is_Some else _dafny.Seq([]))
            return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_Values.JSON_String((d_136_KmsMrkDiscovery_).defaultMrkRegion))])) + (d_137_filter_)))
        elif source1_.is_RSA:
            d_139___mcc_h3_ = source1_.RSA
            d_140_RSA_ = d_139___mcc_h3_
            d_141_padding_ = (default__.PaddingAlgorithmString2String)[(d_140_RSA_).padding]
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_140_RSA_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_140_RSA_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("rsa"))), (_dafny.Seq("padding-algorithm"), JSON_Values.JSON_String((d_141_padding_)[0])), (_dafny.Seq("padding-hash"), JSON_Values.JSON_String((d_141_padding_)[1]))])))
        elif source1_.is_AES:
            d_142___mcc_h4_ = source1_.AES
            d_143_AES_ = d_142___mcc_h4_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_143_AES_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_143_AES_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("aes")))])))
        elif source1_.is_Static:
            d_144___mcc_h5_ = source1_.Static
            d_145_Static_ = d_144___mcc_h5_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("static-material-keyring"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_145_Static_).keyId))])))
        elif source1_.is_KmsRsa:
            d_146___mcc_h6_ = source1_.KmsRsa
            d_147_KmsRsa_ = d_146___mcc_h6_
            d_148_valueOrError0_ = Wrappers.default__.Need(((d_147_KmsRsa_).encryptionAlgorithm) in (default__.EncryptionAlgorithmSpec2String), _dafny.Seq("Unsupported encryptionAlgorithm"))
            if (d_148_valueOrError0_).IsFailure():
                return (d_148_valueOrError0_).PropagateFailure()
            elif True:
                d_149_encryptionAlgorithm_ = (default__.EncryptionAlgorithmSpec2String)[(d_147_KmsRsa_).encryptionAlgorithm]
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_147_KmsRsa_).keyId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(d_149_encryptionAlgorithm_))])))
        elif source1_.is_Hierarchy:
            d_150___mcc_h7_ = source1_.Hierarchy
            d_151_Hierarchy_ = d_150___mcc_h7_
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_151_Hierarchy_).keyId))])))
        elif source1_.is_Multi:
            d_152___mcc_h8_ = source1_.Multi
            d_153_MultiKeyring_ = d_152___mcc_h8_
            def lambda11_(forall_var_8_):
                d_155_c_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = forall_var_8_
                return not ((d_155_c_) in ((d_153_MultiKeyring_).childKeyrings)) or (default__.Keyring_q(d_155_c_))

            d_154_valueOrError1_ = Wrappers.default__.Need((not (((d_153_MultiKeyring_).generator).is_Some) or (default__.Keyring_q(((d_153_MultiKeyring_).generator).value))) and (_dafny.quantifier(((d_153_MultiKeyring_).childKeyrings).UniqueElements, True, lambda11_)), _dafny.Seq("CMMs not supported by Multi Keyrings"))
            if (d_154_valueOrError1_).IsFailure():
                return (d_154_valueOrError1_).PropagateFailure()
            elif True:
                if (outputVersion) == (3):
                    def iife9_(_pat_let2_0):
                        def iife10_(d_157_valueOrError3_):
                            def iife11_(_pat_let3_0):
                                def iife12_(d_158_g_):
                                    return Wrappers.Result_Success(Wrappers.Option_Some(d_158_g_))
                                return iife12_(_pat_let3_0)
                            return ((d_157_valueOrError3_).PropagateFailure() if (d_157_valueOrError3_).IsFailure() else iife11_((d_157_valueOrError3_).Extract()))
                        return iife10_(_pat_let2_0)
                    d_156_valueOrError2_ = (iife9_(default__.ToJson(((d_153_MultiKeyring_).generator).value, outputVersion)) if ((d_153_MultiKeyring_).generator).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                    if (d_156_valueOrError2_).IsFailure():
                        return (d_156_valueOrError2_).PropagateFailure()
                    elif True:
                        d_159_generator_ = (d_156_valueOrError2_).Extract()
                        d_160_valueOrError4_ = default__.KeyDescriptionListToJson((d_153_MultiKeyring_).childKeyrings, outputVersion)
                        if (d_160_valueOrError4_).IsFailure():
                            return (d_160_valueOrError4_).PropagateFailure()
                        elif True:
                            d_161_childKeyrings_ = (d_160_valueOrError4_).Extract()
                            return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("multi-keyring"))), (_dafny.Seq("childKeyrings"), JSON_Values.JSON_Array(d_161_childKeyrings_))])) + ((_dafny.Seq([(_dafny.Seq("generator"), (d_159_generator_).value)]) if (d_159_generator_).is_Some else _dafny.Seq([])))))
                elif True:
                    d_162_valueOrError5_ = Wrappers.default__.Need(((d_153_MultiKeyring_).generator).is_Some, _dafny.Seq("Generator required for v1 or v2"))
                    if (d_162_valueOrError5_).IsFailure():
                        return (d_162_valueOrError5_).PropagateFailure()
                    elif True:
                        d_163_keyrings_ = (_dafny.Seq([((d_153_MultiKeyring_).generator).value])) + ((d_153_MultiKeyring_).childKeyrings)
                        def lambda12_(forall_var_9_):
                            d_165_c_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = forall_var_9_
                            return not ((d_165_c_) in (d_163_keyrings_)) or (not((d_165_c_).is_Multi))

                        d_164_valueOrError6_ = Wrappers.default__.Need(_dafny.quantifier((d_163_keyrings_).UniqueElements, True, lambda12_), _dafny.Seq("Recursive structures not supported"))
                        if (d_164_valueOrError6_).IsFailure():
                            return (d_164_valueOrError6_).PropagateFailure()
                        elif True:
                            d_166_valueOrError7_ = default__.KeyDescriptionListToJson((d_153_MultiKeyring_).childKeyrings, outputVersion)
                            if (d_166_valueOrError7_).IsFailure():
                                return (d_166_valueOrError7_).PropagateFailure()
                            elif True:
                                d_167_keyrings_ = (d_166_valueOrError7_).Extract()
                                return Wrappers.Result_Success(JSON_Values.JSON_Array(d_167_keyrings_))
        elif True:
            d_168___mcc_h9_ = source1_.RequiredEncryptionContext
            d_169_RequiredEncryptionContext_ = d_168___mcc_h9_
            d_170_valueOrError8_ = default__.ToJson((d_169_RequiredEncryptionContext_).underlying, outputVersion)
            if (d_170_valueOrError8_).IsFailure():
                return (d_170_valueOrError8_).PropagateFailure()
            elif True:
                d_171_underlying_ = (d_170_valueOrError8_).Extract()
                def lambda13_(d_173_key_):
                    def iife13_(_pat_let4_0):
                        def iife14_(d_174_valueOrError10_):
                            def iife15_(_pat_let5_0):
                                def iife16_(d_175_s_):
                                    return Wrappers.Result_Success(JSON_Values.JSON_String(d_175_s_))
                                return iife16_(_pat_let5_0)
                            return ((d_174_valueOrError10_).PropagateFailure() if (d_174_valueOrError10_).IsFailure() else iife15_((d_174_valueOrError10_).Extract()))
                        return iife14_(_pat_let4_0)
                    return iife13_(UTF8.default__.Decode(d_173_key_))

                d_172_valueOrError9_ = Seq.default__.MapWithResult(lambda13_, (d_169_RequiredEncryptionContext_).requiredEncryptionContextKeys)
                if (d_172_valueOrError9_).IsFailure():
                    return (d_172_valueOrError9_).PropagateFailure()
                elif True:
                    d_176_requiredEncryptionContextKeys_ = (d_172_valueOrError9_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("required-encryption-context-cmm"))), (_dafny.Seq("underlying"), d_171_underlying_), (_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(d_176_requiredEncryptionContextKeys_))])))

    @staticmethod
    def Keyring_q(description):
        return (((((((((description).is_Kms) or ((description).is_KmsMrk)) or ((description).is_KmsMrkDiscovery)) or ((description).is_RSA)) or ((description).is_AES)) or ((description).is_Static)) or ((description).is_KmsRsa)) or ((description).is_Hierarchy)) or ((description).is_Multi)

    @staticmethod
    def KeyDescriptionListToJson(childKeyrings, outputVersion):
        if (0) == (len(childKeyrings)):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_177_valueOrError0_ = default__.ToJson((childKeyrings)[0], outputVersion)
            if (d_177_valueOrError0_).IsFailure():
                return (d_177_valueOrError0_).PropagateFailure()
            elif True:
                d_178_json_ = (d_177_valueOrError0_).Extract()
                d_179_valueOrError1_ = default__.KeyDescriptionListToJson(_dafny.Seq((childKeyrings)[1::]), outputVersion)
                if (d_179_valueOrError1_).IsFailure():
                    return (d_179_valueOrError1_).PropagateFailure()
                elif True:
                    d_180_rest_ = (d_179_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_178_json_])) + (d_180_rest_))

    @staticmethod
    def Invert(m):
        def iife17_():
            coll5_ = _dafny.Map()
            compr_5_: TypeVar('X__')
            for compr_5_ in (m).keys.Elements:
                d_181_k_: TypeVar('X__') = compr_5_
                if (d_181_k_) in (m):
                    coll5_[(m)[d_181_k_]] = d_181_k_
            return _dafny.Map(coll5_)
        return iife17_()
        

    @_dafny.classproperty
    def EncryptionAlgorithmSpec2String(instance):
        return _dafny.Map({ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(): _dafny.Seq("RSAES_OAEP_SHA_1"), ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256(): _dafny.Seq("RSAES_OAEP_SHA_256")})
    @_dafny.classproperty
    def String2EncryptionAlgorithmSpec(instance):
        return default__.Invert(default__.EncryptionAlgorithmSpec2String)
    @_dafny.classproperty
    def PaddingAlgorithmString2String(instance):
        return _dafny.Map({AwsCryptographyMaterialProvidersTypes.PaddingScheme_PKCS1(): (_dafny.Seq("pkcs1"), _dafny.Seq("sha1")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha1")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA256__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha256")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA384__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha384")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA512__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha512"))})
    @_dafny.classproperty
    def String2PaddingAlgorithm(instance):
        return default__.Invert(default__.PaddingAlgorithmString2String)

class KeyDescriptionVersion:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return 1
    def _Is(source__):
        d_182_v_: int = source__
        return default__.KeyDescriptionVersion_q(d_182_v_)
