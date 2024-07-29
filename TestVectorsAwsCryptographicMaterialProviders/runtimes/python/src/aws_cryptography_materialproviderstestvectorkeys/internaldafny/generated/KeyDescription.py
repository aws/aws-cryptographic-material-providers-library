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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
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
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
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
import standard_library.internaldafny.generated.JSON_API as JSON_API
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers

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
        pat_let_tv1_ = json
        if (json).is_Array:
            d_71_valueOrError0_ = Wrappers.default__.Need((1) <= (len((json).arr)), _dafny.Seq("Need at least one element in a JSON Array."))
            if (d_71_valueOrError0_).IsFailure():
                return (d_71_valueOrError0_).PropagateFailure()
            elif True:
                def lambda7_(forall_var_7_):
                    d_73_c_: JSON_Values.JSON = forall_var_7_
                    return not ((d_73_c_) in ((json).arr)) or ((d_73_c_).is_Object)

                d_72_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((json).arr).UniqueElements, True, lambda7_), _dafny.Seq("No nested arrays."))
                if (d_72_valueOrError1_).IsFailure():
                    return (d_72_valueOrError1_).PropagateFailure()
                elif True:
                    return default__.ToMultiKeyring(json, Wrappers.Option_Some(((json).arr)[0]), _dafny.Seq(((json).arr)[1::]))
        elif True:
            d_74_valueOrError2_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("KeyDescription not an object"))
            if (d_74_valueOrError2_).IsFailure():
                return (d_74_valueOrError2_).PropagateFailure()
            elif True:
                d_75_obj_ = (json).obj
                d_76_typString_ = _dafny.Seq("type")
                d_77_valueOrError3_ = JSONHelpers.default__.GetString(d_76_typString_, d_75_obj_)
                if (d_77_valueOrError3_).IsFailure():
                    return (d_77_valueOrError3_).PropagateFailure()
                elif True:
                    d_78_typ_ = (d_77_valueOrError3_).Extract()
                    d_79_valueOrError4_ = Wrappers.default__.Need(default__.KeyDescriptionString_q(d_78_typ_), (_dafny.Seq("Unsupported KeyDescription type:")) + (d_78_typ_))
                    if (d_79_valueOrError4_).IsFailure():
                        return (d_79_valueOrError4_).PropagateFailure()
                    elif True:
                        source1_ = d_78_typ_
                        unmatched1 = True
                        if unmatched1:
                            if (source1_) == (_dafny.Seq("aws-kms-mrk-aware-discovery")):
                                unmatched1 = False
                                return default__.ToAwsKmsMrkAwareDiscovery(d_75_obj_)
                        if unmatched1:
                            if (source1_) == (_dafny.Seq("multi-keyring")):
                                unmatched1 = False
                                d_80_generatorJson_ = (JSONHelpers.default__.Get(_dafny.Seq("generator"), d_75_obj_)).ToOption()
                                d_81_valueOrError5_ = JSONHelpers.default__.GetArray(_dafny.Seq("childKeyrings"), d_75_obj_)
                                if (d_81_valueOrError5_).IsFailure():
                                    return (d_81_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_82_childKeyringsJson_ = (d_81_valueOrError5_).Extract()
                                    return default__.ToMultiKeyring(pat_let_tv1_, d_80_generatorJson_, d_82_childKeyringsJson_)
                        if unmatched1:
                            if (source1_) == (_dafny.Seq("required-encryption-context-cmm")):
                                unmatched1 = False
                                d_83_valueOrError6_ = JSONHelpers.default__.Get(_dafny.Seq("underlying"), d_75_obj_)
                                if (d_83_valueOrError6_).IsFailure():
                                    return (d_83_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_84_u_ = (d_83_valueOrError6_).Extract()
                                    d_85_valueOrError7_ = default__.ToKeyDescription(d_84_u_)
                                    if (d_85_valueOrError7_).IsFailure():
                                        return (d_85_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_86_underlying_ = (d_85_valueOrError7_).Extract()
                                        d_87_requiredEncryptionContextStrings_ = ((JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_75_obj_)).ToOption()).UnwrapOr(_dafny.Seq([]))
                                        d_88_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_87_requiredEncryptionContextStrings_)
                                        if (d_88_valueOrError8_).IsFailure():
                                            return (d_88_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_89_requiredEncryptionContextKeys_ = (d_88_valueOrError8_).Extract()
                                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RequiredEncryptionContext(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(d_86_underlying_, d_89_requiredEncryptionContextKeys_)))
                        if unmatched1:
                            if (source1_) == (_dafny.Seq("raw-ecdh")):
                                unmatched1 = False
                                return default__.ToRawEcdh(d_75_obj_)
                        if unmatched1:
                            if (source1_) == (_dafny.Seq("aws-kms-ecdh")):
                                unmatched1 = False
                                return default__.ToAwsKmsEcdh(d_75_obj_)
                        if unmatched1:
                            unmatched1 = False
                            d_90_valueOrError9_ = JSONHelpers.default__.GetString(_dafny.Seq("key"), d_75_obj_)
                            if (d_90_valueOrError9_).IsFailure():
                                return (d_90_valueOrError9_).PropagateFailure()
                            elif True:
                                d_91_key_ = (d_90_valueOrError9_).Extract()
                                source2_ = d_78_typ_
                                unmatched2 = True
                                if unmatched2:
                                    if (source2_) == (_dafny.Seq("static-material-keyring")):
                                        unmatched2 = False
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(d_91_key_)))
                                if unmatched2:
                                    if (source2_) == (_dafny.Seq("aws-kms")):
                                        unmatched2 = False
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Kms(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo_KMSInfo(d_91_key_)))
                                if unmatched2:
                                    if (source2_) == (_dafny.Seq("aws-kms-mrk-aware")):
                                        unmatched2 = False
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrk(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware_KmsMrkAware(d_91_key_)))
                                if unmatched2:
                                    if (source2_) == (_dafny.Seq("aws-kms-rsa")):
                                        unmatched2 = False
                                        return default__.ToAwsKmsRsa(d_91_key_, d_75_obj_)
                                if unmatched2:
                                    if (source2_) == (_dafny.Seq("aws-kms-hierarchy")):
                                        unmatched2 = False
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Hierarchy(AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring_HierarchyKeyring(d_91_key_)))
                                if unmatched2:
                                    if (source2_) == (_dafny.Seq("raw")):
                                        unmatched2 = False
                                        d_92_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_75_obj_)
                                        if (d_92_valueOrError10_).IsFailure():
                                            return (d_92_valueOrError10_).PropagateFailure()
                                        elif True:
                                            d_93_algorithm_ = (d_92_valueOrError10_).Extract()
                                            d_94_valueOrError11_ = Wrappers.default__.Need(default__.RawAlgorithmString_q(d_93_algorithm_), (_dafny.Seq("Unsupported algorithm:")) + (d_93_algorithm_))
                                            if (d_94_valueOrError11_).IsFailure():
                                                return (d_94_valueOrError11_).PropagateFailure()
                                            elif True:
                                                source3_ = d_93_algorithm_
                                                unmatched3 = True
                                                if unmatched3:
                                                    if (source3_) == (_dafny.Seq("aes")):
                                                        unmatched3 = False
                                                        return default__.ToRawAes(d_91_key_, d_75_obj_)
                                                if unmatched3:
                                                    if (source3_) == (_dafny.Seq("rsa")):
                                                        unmatched3 = False
                                                        return default__.ToRawRsa(d_91_key_, d_75_obj_)
                                                raise Exception("unexpected control point")
                                raise Exception("unexpected control point")
                        raise Exception("unexpected control point")

    @staticmethod
    def ToDiscoveryFilter(obj):
        d_95_valueOrError0_ = (JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)).ToOption()
        if (d_95_valueOrError0_).IsFailure():
            return (d_95_valueOrError0_).PropagateFailure()
        elif True:
            d_96_filter_ = (d_95_valueOrError0_).Extract()
            d_97_valueOrError1_ = (JSONHelpers.default__.GetString(_dafny.Seq("partition"), d_96_filter_)).ToOption()
            if (d_97_valueOrError1_).IsFailure():
                return (d_97_valueOrError1_).PropagateFailure()
            elif True:
                d_98_partition_ = (d_97_valueOrError1_).Extract()
                d_99_valueOrError2_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("account-ids"), d_96_filter_)).ToOption()
                if (d_99_valueOrError2_).IsFailure():
                    return (d_99_valueOrError2_).PropagateFailure()
                elif True:
                    d_100_accountIds_ = (d_99_valueOrError2_).Extract()
                    return Wrappers.Option_Some(AwsCryptographyMaterialProvidersTypes.DiscoveryFilter_DiscoveryFilter(d_100_accountIds_, d_98_partition_))

    @staticmethod
    def ToAwsKmsMrkAwareDiscovery(obj):
        d_101_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("default-mrk-region"), obj)
        if (d_101_valueOrError0_).IsFailure():
            return (d_101_valueOrError0_).PropagateFailure()
        elif True:
            d_102_defaultMrkRegion_ = (d_101_valueOrError0_).Extract()
            d_103_filter_ = JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)
            d_104_awsKmsDiscoveryFilter_ = default__.ToDiscoveryFilter(obj)
            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrkDiscovery(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq("aws-kms-mrk-aware-discovery"), d_102_defaultMrkRegion_, d_104_awsKmsDiscoveryFilter_)))

    @staticmethod
    def ToAwsKmsRsa(key, obj):
        d_105_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), obj)
        if (d_105_valueOrError0_).IsFailure():
            return (d_105_valueOrError0_).PropagateFailure()
        elif True:
            d_106_encryptionAlgorithmString_ = (d_105_valueOrError0_).Extract()
            d_107_valueOrError1_ = Wrappers.default__.Need((d_106_encryptionAlgorithmString_) in (default__.String2EncryptionAlgorithmSpec), (_dafny.Seq("Unsupported EncryptionAlgorithmSpec:")) + (d_106_encryptionAlgorithmString_))
            if (d_107_valueOrError1_).IsFailure():
                return (d_107_valueOrError1_).PropagateFailure()
            elif True:
                d_108_encryptionAlgorithm_ = (default__.String2EncryptionAlgorithmSpec)[d_106_encryptionAlgorithmString_]
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsRsa(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring_KmsRsaKeyring(key, d_108_encryptionAlgorithm_)))

    @staticmethod
    def ToAwsKmsEcdh(obj):
        d_109_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("ecc-curve"), obj)
        if (d_109_valueOrError0_).IsFailure():
            return (d_109_valueOrError0_).PropagateFailure()
        elif True:
            d_110_eccCurve_ = (d_109_valueOrError0_).Extract()
            d_111_valueOrError1_ = Wrappers.default__.Need((d_110_eccCurve_) in (default__.KmsKey2EccAlgorithmSpec), (_dafny.Seq("Unsupported ECC Curve Spec:")) + (d_110_eccCurve_))
            if (d_111_valueOrError1_).IsFailure():
                return (d_111_valueOrError1_).PropagateFailure()
            elif True:
                d_112_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("schema"), obj)
                if (d_112_valueOrError2_).IsFailure():
                    return (d_112_valueOrError2_).PropagateFailure()
                elif True:
                    d_113_schema_ = (d_112_valueOrError2_).Extract()
                    d_114_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("sender"), obj)
                    if (d_114_valueOrError3_).IsFailure():
                        return (d_114_valueOrError3_).PropagateFailure()
                    elif True:
                        d_115_sender_ = (d_114_valueOrError3_).Extract()
                        d_116_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient"), obj)
                        if (d_116_valueOrError4_).IsFailure():
                            return (d_116_valueOrError4_).PropagateFailure()
                        elif True:
                            d_117_recipient_ = (d_116_valueOrError4_).Extract()
                            d_118_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-public-key"), obj)
                            if (d_118_valueOrError5_).IsFailure():
                                return (d_118_valueOrError5_).PropagateFailure()
                            elif True:
                                d_119_senderPublicKey_ = (d_118_valueOrError5_).Extract()
                                d_120_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-public-key"), obj)
                                if (d_120_valueOrError6_).IsFailure():
                                    return (d_120_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_121_recipientPublicKey_ = (d_120_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring(d_115_sender_, d_117_recipient_, d_119_senderPublicKey_, d_121_recipientPublicKey_, d_110_eccCurve_, d_113_schema_)))

    @staticmethod
    def ToRawAes(key, obj):
        d_122_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_122_valueOrError0_).IsFailure():
            return (d_122_valueOrError0_).PropagateFailure()
        elif True:
            d_123_providerId_ = (d_122_valueOrError0_).Extract()
            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_AES(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES_RawAES(key, d_123_providerId_)))

    @staticmethod
    def ToRawRsa(key, obj):
        d_124_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_124_valueOrError0_).IsFailure():
            return (d_124_valueOrError0_).PropagateFailure()
        elif True:
            d_125_providerId_ = (d_124_valueOrError0_).Extract()
            d_126_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-algorithm"), obj)
            if (d_126_valueOrError1_).IsFailure():
                return (d_126_valueOrError1_).PropagateFailure()
            elif True:
                d_127_paddingAlgorithm_ = (d_126_valueOrError1_).Extract()
                d_128_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("padding-hash"), obj)
                if (d_128_valueOrError2_).IsFailure():
                    return (d_128_valueOrError2_).PropagateFailure()
                elif True:
                    d_129_maybePaddingHash_ = (d_128_valueOrError2_).Extract()
                    d_130_valueOrError3_ = Wrappers.default__.Need(not ((d_129_maybePaddingHash_).is_None) or ((d_127_paddingAlgorithm_) == (_dafny.Seq("pkcs1"))), _dafny.Seq("oaep-mgf1 MUST define padding-hash"))
                    if (d_130_valueOrError3_).IsFailure():
                        return (d_130_valueOrError3_).PropagateFailure()
                    elif True:
                        d_131_paddingHash_ = (d_129_maybePaddingHash_).UnwrapOr(_dafny.Seq("sha1"))
                        d_132_valueOrError4_ = Wrappers.default__.Need(((d_127_paddingAlgorithm_, d_131_paddingHash_)) in (default__.String2PaddingAlgorithm), (((_dafny.Seq("Unsupported padding:")) + (d_127_paddingAlgorithm_)) + (_dafny.Seq(" hash:"))) + (d_131_paddingHash_))
                        if (d_132_valueOrError4_).IsFailure():
                            return (d_132_valueOrError4_).PropagateFailure()
                        elif True:
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RSA(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA_RawRSA(key, d_125_providerId_, (default__.String2PaddingAlgorithm)[(d_127_paddingAlgorithm_, d_131_paddingHash_)])))

    @staticmethod
    def ToRawEcdh(obj):
        d_133_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_133_valueOrError0_).IsFailure():
            return (d_133_valueOrError0_).PropagateFailure()
        elif True:
            d_134_providerId_ = (d_133_valueOrError0_).Extract()
            d_135_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("ecc-curve"), obj)
            if (d_135_valueOrError1_).IsFailure():
                return (d_135_valueOrError1_).PropagateFailure()
            elif True:
                d_136_ecc__curve_ = (d_135_valueOrError1_).Extract()
                d_137_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("sender"), obj)
                if (d_137_valueOrError2_).IsFailure():
                    return (d_137_valueOrError2_).PropagateFailure()
                elif True:
                    d_138_sender_ = (d_137_valueOrError2_).Extract()
                    d_139_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient"), obj)
                    if (d_139_valueOrError3_).IsFailure():
                        return (d_139_valueOrError3_).PropagateFailure()
                    elif True:
                        d_140_recipient_ = (d_139_valueOrError3_).Extract()
                        d_141_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("schema"), obj)
                        if (d_141_valueOrError4_).IsFailure():
                            return (d_141_valueOrError4_).PropagateFailure()
                        elif True:
                            d_142_schema_ = (d_141_valueOrError4_).Extract()
                            d_143_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-public-key"), obj)
                            if (d_143_valueOrError5_).IsFailure():
                                return (d_143_valueOrError5_).PropagateFailure()
                            elif True:
                                d_144_senderPublicKey_ = (d_143_valueOrError5_).Extract()
                                d_145_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-public-key"), obj)
                                if (d_145_valueOrError6_).IsFailure():
                                    return (d_145_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_146_recipientPublicKey_ = (d_145_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh(d_138_sender_, d_140_recipient_, d_144_senderPublicKey_, d_146_recipientPublicKey_, d_134_providerId_, d_136_ecc__curve_, d_142_schema_)))

    @staticmethod
    def ToMultiKeyring(json, generatorJson, childKeyringsJson):
        d_147_valueOrError0_ = Wrappers.default__.Need(not ((generatorJson).is_Some) or (((generatorJson).value).is_Object), _dafny.Seq("Not an object"))
        if (d_147_valueOrError0_).IsFailure():
            return (d_147_valueOrError0_).PropagateFailure()
        elif True:
            def iife5_(_pat_let0_0):
                def iife6_(d_149_valueOrError2_):
                    def iife7_(_pat_let1_0):
                        def iife8_(d_150_g_):
                            return Wrappers.Result_Success(Wrappers.Option_Some(d_150_g_))
                        return iife8_(_pat_let1_0)
                    return ((d_149_valueOrError2_).PropagateFailure() if (d_149_valueOrError2_).IsFailure() else iife7_((d_149_valueOrError2_).Extract()))
                return iife6_(_pat_let0_0)
            d_148_valueOrError1_ = (iife5_(default__.ToKeyDescription((generatorJson).value)) if (generatorJson).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
            if (d_148_valueOrError1_).IsFailure():
                return (d_148_valueOrError1_).PropagateFailure()
            elif True:
                d_151_generator_ = (d_148_valueOrError1_).Extract()
                def lambda8_(d_153_childKeyringsJson_):
                    def lambda9_(d_154_c_):
                        return default__.ToKeyDescription(d_154_c_)

                    return lambda9_

                d_152_valueOrError3_ = Seq.default__.MapWithResult(lambda8_(childKeyringsJson), childKeyringsJson)
                if (d_152_valueOrError3_).IsFailure():
                    return (d_152_valueOrError3_).PropagateFailure()
                elif True:
                    d_155_childKeyrings_ = (d_152_valueOrError3_).Extract()
                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Multi(AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring_MultiKeyring(d_151_generator_, d_155_childKeyrings_)))

    @staticmethod
    def KeyDescriptionString_q(s):
        return (((((((((((s) == (_dafny.Seq("static-material-keyring"))) or ((s) == (_dafny.Seq("aws-kms")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware-discovery")))) or ((s) == (_dafny.Seq("raw")))) or ((s) == (_dafny.Seq("raw-ecdh")))) or ((s) == (_dafny.Seq("aws-kms-hierarchy")))) or ((s) == (_dafny.Seq("aws-kms-rsa")))) or ((s) == (_dafny.Seq("aws-kms-ecdh")))) or ((s) == (_dafny.Seq("required-encryption-context-cmm")))) or ((s) == (_dafny.Seq("multi-keyring")))

    @staticmethod
    def RawAlgorithmString_q(s):
        return ((s) == (_dafny.Seq("aes"))) or ((s) == (_dafny.Seq("rsa")))

    @staticmethod
    def KeyDescriptionVersion_q(v):
        return (((v) == (1)) or ((v) == (2))) or ((v) == (3))

    @staticmethod
    def ToJson(keyDescription, outputVersion):
        pat_let_tv2_ = outputVersion
        pat_let_tv3_ = outputVersion
        pat_let_tv4_ = outputVersion
        pat_let_tv5_ = outputVersion
        source4_ = keyDescription
        unmatched4 = True
        if unmatched4:
            if source4_.is_Kms:
                d_156_Kms_ = source4_.Kms
                unmatched4 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_156_Kms_).keyId))])))
        if unmatched4:
            if source4_.is_KmsMrk:
                d_157_KmsMrk_ = source4_.KmsMrk
                unmatched4 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_157_KmsMrk_).keyId))])))
        if unmatched4:
            if source4_.is_KmsMrkDiscovery:
                d_158_KmsMrkDiscovery_ = source4_.KmsMrkDiscovery
                unmatched4 = False
                def lambda10_(d_160_s_):
                    return JSON_Values.JSON_String(d_160_s_)

                d_159_filter_ = (_dafny.Seq([(_dafny.Seq("aws-kms-discovery-filter"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("partition"), JSON_Values.JSON_String((((d_158_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).partition)), (_dafny.Seq("account-ids"), JSON_Values.JSON_Array(Seq.default__.Map(lambda10_, (((d_158_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).accountIds)))])))]) if ((d_158_KmsMrkDiscovery_).awsKmsDiscoveryFilter).is_Some else _dafny.Seq([]))
                return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_Values.JSON_String((d_158_KmsMrkDiscovery_).defaultMrkRegion))])) + (d_159_filter_)))
        if unmatched4:
            if source4_.is_RSA:
                d_161_RSA_ = source4_.RSA
                unmatched4 = False
                d_162_padding_ = (default__.PaddingAlgorithmString2String)[(d_161_RSA_).padding]
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_161_RSA_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_161_RSA_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("rsa"))), (_dafny.Seq("padding-algorithm"), JSON_Values.JSON_String((d_162_padding_)[0])), (_dafny.Seq("padding-hash"), JSON_Values.JSON_String((d_162_padding_)[1]))])))
        if unmatched4:
            if source4_.is_AES:
                d_163_AES_ = source4_.AES
                unmatched4 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_163_AES_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_163_AES_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("aes")))])))
        if unmatched4:
            if source4_.is_ECDH:
                d_164_ECDH_ = source4_.ECDH
                unmatched4 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw-ecdh"))), (_dafny.Seq("sender"), JSON_Values.JSON_String((d_164_ECDH_).senderKeyId)), (_dafny.Seq("recipient"), JSON_Values.JSON_String((d_164_ECDH_).recipientKeyId)), (_dafny.Seq("sender-public-key"), JSON_Values.JSON_String((d_164_ECDH_).senderPublicKey)), (_dafny.Seq("recipient-public-key"), JSON_Values.JSON_String((d_164_ECDH_).recipientPublicKey)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_164_ECDH_).providerId)), (_dafny.Seq("ecc-curve"), JSON_Values.JSON_String((d_164_ECDH_).curveSpec)), (_dafny.Seq("schema"), JSON_Values.JSON_String((d_164_ECDH_).keyAgreementScheme))])))
        if unmatched4:
            if source4_.is_Static:
                d_165_Static_ = source4_.Static
                unmatched4 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("static-material-keyring"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_165_Static_).keyId))])))
        if unmatched4:
            if source4_.is_KmsRsa:
                d_166_KmsRsa_ = source4_.KmsRsa
                unmatched4 = False
                d_167_valueOrError0_ = Wrappers.default__.Need(((d_166_KmsRsa_).encryptionAlgorithm) in (default__.EncryptionAlgorithmSpec2String), _dafny.Seq("Unsupported encryptionAlgorithm"))
                if (d_167_valueOrError0_).IsFailure():
                    return (d_167_valueOrError0_).PropagateFailure()
                elif True:
                    d_168_encryptionAlgorithm_ = (default__.EncryptionAlgorithmSpec2String)[(d_166_KmsRsa_).encryptionAlgorithm]
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_166_KmsRsa_).keyId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(d_168_encryptionAlgorithm_))])))
        if unmatched4:
            if source4_.is_KmsECDH:
                d_169_KmsECDH_ = source4_.KmsECDH
                unmatched4 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-ecdh"))), (_dafny.Seq("sender"), JSON_Values.JSON_String((d_169_KmsECDH_).senderKeyId)), (_dafny.Seq("recipient"), JSON_Values.JSON_String((d_169_KmsECDH_).recipientKeyId)), (_dafny.Seq("sender-public-key"), JSON_Values.JSON_String((d_169_KmsECDH_).senderPublicKey)), (_dafny.Seq("recipient-public-key"), JSON_Values.JSON_String((d_169_KmsECDH_).recipientPublicKey)), (_dafny.Seq("ecc-curve"), JSON_Values.JSON_String((d_169_KmsECDH_).curveSpec)), (_dafny.Seq("schema"), JSON_Values.JSON_String((d_169_KmsECDH_).keyAgreementScheme))])))
        if unmatched4:
            if source4_.is_Hierarchy:
                d_170_Hierarchy_ = source4_.Hierarchy
                unmatched4 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_170_Hierarchy_).keyId))])))
        if unmatched4:
            if source4_.is_Multi:
                d_171_MultiKeyring_ = source4_.Multi
                unmatched4 = False
                def lambda11_(forall_var_8_):
                    d_173_c_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = forall_var_8_
                    return not ((d_173_c_) in ((d_171_MultiKeyring_).childKeyrings)) or (default__.Keyring_q(d_173_c_))

                d_172_valueOrError1_ = Wrappers.default__.Need((not (((d_171_MultiKeyring_).generator).is_Some) or (default__.Keyring_q(((d_171_MultiKeyring_).generator).value))) and (_dafny.quantifier(((d_171_MultiKeyring_).childKeyrings).UniqueElements, True, lambda11_)), _dafny.Seq("CMMs not supported by Multi Keyrings"))
                if (d_172_valueOrError1_).IsFailure():
                    return (d_172_valueOrError1_).PropagateFailure()
                elif True:
                    source5_ = outputVersion
                    unmatched5 = True
                    if unmatched5:
                        if (source5_) == (3):
                            unmatched5 = False
                            def iife9_(_pat_let2_0):
                                def iife10_(d_175_valueOrError3_):
                                    def iife11_(_pat_let3_0):
                                        def iife12_(d_176_g_):
                                            return Wrappers.Result_Success(Wrappers.Option_Some(d_176_g_))
                                        return iife12_(_pat_let3_0)
                                    return ((d_175_valueOrError3_).PropagateFailure() if (d_175_valueOrError3_).IsFailure() else iife11_((d_175_valueOrError3_).Extract()))
                                return iife10_(_pat_let2_0)
                            d_174_valueOrError2_ = (iife9_(default__.ToJson(((d_171_MultiKeyring_).generator).value, pat_let_tv2_)) if ((d_171_MultiKeyring_).generator).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                            if (d_174_valueOrError2_).IsFailure():
                                return (d_174_valueOrError2_).PropagateFailure()
                            elif True:
                                d_177_generator_ = (d_174_valueOrError2_).Extract()
                                d_178_valueOrError4_ = default__.KeyDescriptionListToJson((d_171_MultiKeyring_).childKeyrings, pat_let_tv3_)
                                if (d_178_valueOrError4_).IsFailure():
                                    return (d_178_valueOrError4_).PropagateFailure()
                                elif True:
                                    d_179_childKeyrings_ = (d_178_valueOrError4_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("multi-keyring"))), (_dafny.Seq("childKeyrings"), JSON_Values.JSON_Array(d_179_childKeyrings_))])) + ((_dafny.Seq([(_dafny.Seq("generator"), (d_177_generator_).value)]) if (d_177_generator_).is_Some else _dafny.Seq([])))))
                    if unmatched5:
                        unmatched5 = False
                        d_180_valueOrError5_ = Wrappers.default__.Need(((d_171_MultiKeyring_).generator).is_Some, _dafny.Seq("Generator required for v1 or v2"))
                        if (d_180_valueOrError5_).IsFailure():
                            return (d_180_valueOrError5_).PropagateFailure()
                        elif True:
                            d_181_keyrings_ = (_dafny.Seq([((d_171_MultiKeyring_).generator).value])) + ((d_171_MultiKeyring_).childKeyrings)
                            def lambda12_(forall_var_9_):
                                d_183_c_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = forall_var_9_
                                return not ((d_183_c_) in (d_181_keyrings_)) or (not((d_183_c_).is_Multi))

                            d_182_valueOrError6_ = Wrappers.default__.Need(_dafny.quantifier((d_181_keyrings_).UniqueElements, True, lambda12_), _dafny.Seq("Recursive structures not supported"))
                            if (d_182_valueOrError6_).IsFailure():
                                return (d_182_valueOrError6_).PropagateFailure()
                            elif True:
                                d_184_valueOrError7_ = default__.KeyDescriptionListToJson((d_171_MultiKeyring_).childKeyrings, pat_let_tv4_)
                                if (d_184_valueOrError7_).IsFailure():
                                    return (d_184_valueOrError7_).PropagateFailure()
                                elif True:
                                    d_185_keyrings_ = (d_184_valueOrError7_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Array(d_185_keyrings_))
                    raise Exception("unexpected control point")
        if unmatched4:
            d_186_RequiredEncryptionContext_ = source4_.RequiredEncryptionContext
            unmatched4 = False
            d_187_valueOrError8_ = default__.ToJson((d_186_RequiredEncryptionContext_).underlying, pat_let_tv5_)
            if (d_187_valueOrError8_).IsFailure():
                return (d_187_valueOrError8_).PropagateFailure()
            elif True:
                d_188_underlying_ = (d_187_valueOrError8_).Extract()
                def lambda13_(d_190_key_):
                    def iife13_(_pat_let4_0):
                        def iife14_(d_191_valueOrError10_):
                            def iife15_(_pat_let5_0):
                                def iife16_(d_192_s_):
                                    return Wrappers.Result_Success(JSON_Values.JSON_String(d_192_s_))
                                return iife16_(_pat_let5_0)
                            return ((d_191_valueOrError10_).PropagateFailure() if (d_191_valueOrError10_).IsFailure() else iife15_((d_191_valueOrError10_).Extract()))
                        return iife14_(_pat_let4_0)
                    return iife13_(UTF8.default__.Decode(d_190_key_))

                d_189_valueOrError9_ = Seq.default__.MapWithResult(lambda13_, (d_186_RequiredEncryptionContext_).requiredEncryptionContextKeys)
                if (d_189_valueOrError9_).IsFailure():
                    return (d_189_valueOrError9_).PropagateFailure()
                elif True:
                    d_193_requiredEncryptionContextKeys_ = (d_189_valueOrError9_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("required-encryption-context-cmm"))), (_dafny.Seq("underlying"), d_188_underlying_), (_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(d_193_requiredEncryptionContextKeys_))])))
        raise Exception("unexpected control point")

    @staticmethod
    def Keyring_q(description):
        return (((((((((((description).is_Kms) or ((description).is_KmsMrk)) or ((description).is_KmsMrkDiscovery)) or ((description).is_RSA)) or ((description).is_AES)) or ((description).is_ECDH)) or ((description).is_Static)) or ((description).is_KmsRsa)) or ((description).is_KmsECDH)) or ((description).is_Hierarchy)) or ((description).is_Multi)

    @staticmethod
    def KeyDescriptionListToJson(childKeyrings, outputVersion):
        if (0) == (len(childKeyrings)):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_194_valueOrError0_ = default__.ToJson((childKeyrings)[0], outputVersion)
            if (d_194_valueOrError0_).IsFailure():
                return (d_194_valueOrError0_).PropagateFailure()
            elif True:
                d_195_json_ = (d_194_valueOrError0_).Extract()
                d_196_valueOrError1_ = default__.KeyDescriptionListToJson(_dafny.Seq((childKeyrings)[1::]), outputVersion)
                if (d_196_valueOrError1_).IsFailure():
                    return (d_196_valueOrError1_).PropagateFailure()
                elif True:
                    d_197_rest_ = (d_196_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_195_json_])) + (d_197_rest_))

    @staticmethod
    def Invert(m):
        def iife17_():
            coll5_ = _dafny.Map()
            compr_5_: TypeVar('X__')
            for compr_5_ in (m).keys.Elements:
                d_198_k_: TypeVar('X__') = compr_5_
                if (d_198_k_) in (m):
                    coll5_[(m)[d_198_k_]] = d_198_k_
            return _dafny.Map(coll5_)
        return iife17_()
        

    @_dafny.classproperty
    def KmsKey2EccAlgorithmSpec(instance):
        return _dafny.Map({_dafny.Seq("us-west-2-256-ecc"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), _dafny.Seq("us-west-2-384-ecc"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), _dafny.Seq("us-west-2-521-ecc"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()})
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
    @_dafny.classproperty
    def EccAlgorithmSpec2string(instance):
        return _dafny.Map({AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(): _dafny.Seq("secp256r1"), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(): _dafny.Seq("secp384r1"), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521(): _dafny.Seq("secp521r1")})
    @_dafny.classproperty
    def String2EccAlgorithmSpec(instance):
        return default__.Invert(default__.EccAlgorithmSpec2string)
    @_dafny.classproperty
    def Curve2EccAlgorithmSpec(instance):
        return _dafny.Map({_dafny.Seq("ecc-256"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), _dafny.Seq("ecc-384"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), _dafny.Seq("ecc-521"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()})
    @_dafny.classproperty
    def EccAlgorithmSpec2Spec(instance):
        return default__.Invert(default__.Curve2EccAlgorithmSpec)

class KeyDescriptionVersion:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return 1
    def _Is(source__):
        d_199_v_: int = source__
        return default__.KeyDescriptionVersion_q(d_199_v_)
