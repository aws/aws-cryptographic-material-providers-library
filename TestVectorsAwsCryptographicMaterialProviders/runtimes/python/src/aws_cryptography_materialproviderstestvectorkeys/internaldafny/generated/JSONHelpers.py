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

# Module: JSONHelpers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BvToBytes(bits):
        return _dafny.Seq([(bits)[d_3_i_] for d_3_i_ in range(len(bits))])

    @staticmethod
    def BytesBv(bits):
        return _dafny.Seq([(bits)[d_4_i_] for d_4_i_ in range(len(bits))])

    @staticmethod
    def Get(key, obj):
        while True:
            with _dafny.label():
                if (len(obj)) == (0):
                    return Wrappers.Result_Failure(((_dafny.Seq("Key: ")) + (key)) + (_dafny.Seq(" does not exist")))
                elif (((obj)[0])[0]) == (key):
                    return Wrappers.Result_Success(((obj)[0])[1])
                elif True:
                    in0_ = key
                    in1_ = _dafny.Seq((obj)[1::])
                    key = in0_
                    obj = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetString(key, obj):
        d_5_valueOrError0_ = default__.Get(key, obj)
        if (d_5_valueOrError0_).IsFailure():
            return (d_5_valueOrError0_).PropagateFailure()
        elif True:
            d_6_obj_ = (d_5_valueOrError0_).Extract()
            d_7_valueOrError1_ = Wrappers.default__.Need((d_6_obj_).is_String, _dafny.Seq("Not a string"))
            if (d_7_valueOrError1_).IsFailure():
                return (d_7_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_6_obj_).str)

    @staticmethod
    def GetBool(key, obj):
        d_8_valueOrError0_ = default__.Get(key, obj)
        if (d_8_valueOrError0_).IsFailure():
            return (d_8_valueOrError0_).PropagateFailure()
        elif True:
            d_9_obj_ = (d_8_valueOrError0_).Extract()
            d_10_valueOrError1_ = Wrappers.default__.Need((d_9_obj_).is_Bool, _dafny.Seq("Not a bool"))
            if (d_10_valueOrError1_).IsFailure():
                return (d_10_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_9_obj_).b)

    @staticmethod
    def GetNat(key, obj):
        d_11_valueOrError0_ = default__.Get(key, obj)
        if (d_11_valueOrError0_).IsFailure():
            return (d_11_valueOrError0_).PropagateFailure()
        elif True:
            d_12_obj_ = (d_11_valueOrError0_).Extract()
            d_13_valueOrError1_ = Wrappers.default__.Need((d_12_obj_).is_Number, _dafny.Seq("Not a number"))
            if (d_13_valueOrError1_).IsFailure():
                return (d_13_valueOrError1_).PropagateFailure()
            elif True:
                d_14_valueOrError2_ = Wrappers.default__.Need((0) < (((d_12_obj_).num).n), _dafny.Seq("Not a nat"))
                if (d_14_valueOrError2_).IsFailure():
                    return (d_14_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(((d_12_obj_).num).n)

    @staticmethod
    def GetPositiveLong(key, obj):
        d_15_valueOrError0_ = default__.GetNat(key, obj)
        if (d_15_valueOrError0_).IsFailure():
            return (d_15_valueOrError0_).PropagateFailure()
        elif True:
            d_16_n_ = (d_15_valueOrError0_).Extract()
            d_17_valueOrError1_ = Wrappers.default__.Need((d_16_n_) <= (BoundedInts.default__.INT64__MAX), _dafny.Seq("Int64 Overflow"))
            if (d_17_valueOrError1_).IsFailure():
                return (d_17_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_16_n_)

    @staticmethod
    def GetPositiveInteger(key, obj):
        d_18_valueOrError0_ = default__.GetNat(key, obj)
        if (d_18_valueOrError0_).IsFailure():
            return (d_18_valueOrError0_).PropagateFailure()
        elif True:
            d_19_n_ = (d_18_valueOrError0_).Extract()
            d_20_valueOrError1_ = Wrappers.default__.Need((d_19_n_) <= (BoundedInts.default__.INT32__MAX), _dafny.Seq("Int32 Overflow"))
            if (d_20_valueOrError1_).IsFailure():
                return (d_20_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_19_n_)

    @staticmethod
    def GetOptionalString(key, obj):
        d_21_obj_ = (default__.Get(key, obj)).ToOption()
        if (d_21_obj_).is_Some:
            d_22_valueOrError0_ = Wrappers.default__.Need(((d_21_obj_).value).is_String, _dafny.Seq("Not a string"))
            if (d_22_valueOrError0_).IsFailure():
                return (d_22_valueOrError0_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(Wrappers.Option_Some(((d_21_obj_).value).str))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def GetOptionalPositiveLong(key, obj):
        d_23_obj_ = (default__.Get(key, obj)).ToOption()
        if (d_23_obj_).is_Some:
            d_24_valueOrError0_ = Wrappers.default__.Need(((d_23_obj_).value).is_Number, _dafny.Seq("Not a number"))
            if (d_24_valueOrError0_).IsFailure():
                return (d_24_valueOrError0_).PropagateFailure()
            elif True:
                d_25_valueOrError1_ = Wrappers.default__.Need(((0) <= ((((d_23_obj_).value).num).n)) and (((((d_23_obj_).value).num).n) <= (BoundedInts.default__.INT64__MAX)), _dafny.Seq("Int64 Overflow"))
                if (d_25_valueOrError1_).IsFailure():
                    return (d_25_valueOrError1_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(Wrappers.Option_Some((((d_23_obj_).value).num).n))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def GetObject(key, obj):
        d_26_valueOrError0_ = default__.Get(key, obj)
        if (d_26_valueOrError0_).IsFailure():
            return (d_26_valueOrError0_).PropagateFailure()
        elif True:
            d_27_obj_ = (d_26_valueOrError0_).Extract()
            d_28_valueOrError1_ = Wrappers.default__.Need((d_27_obj_).is_Object, _dafny.Seq("Not an object"))
            if (d_28_valueOrError1_).IsFailure():
                return (d_28_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_27_obj_).obj)

    @staticmethod
    def GetArray(key, obj):
        d_29_valueOrError0_ = default__.Get(key, obj)
        if (d_29_valueOrError0_).IsFailure():
            return (d_29_valueOrError0_).PropagateFailure()
        elif True:
            d_30_obj_ = (d_29_valueOrError0_).Extract()
            d_31_valueOrError1_ = Wrappers.default__.Need((d_30_obj_).is_Array, _dafny.Seq("Not an array"))
            if (d_31_valueOrError1_).IsFailure():
                return (d_31_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_30_obj_).arr)

    @staticmethod
    def GetArrayString(key, obj):
        d_32_valueOrError0_ = default__.Get(key, obj)
        if (d_32_valueOrError0_).IsFailure():
            return (d_32_valueOrError0_).PropagateFailure()
        elif True:
            d_33_obj_ = (d_32_valueOrError0_).Extract()
            def lambda0_(forall_var_0_):
                d_35_s_: JSON_Values.JSON = forall_var_0_
                return not ((d_35_s_) in ((d_33_obj_).arr)) or ((d_35_s_).is_String)

            d_34_valueOrError1_ = Wrappers.default__.Need(((d_33_obj_).is_Array) and (_dafny.quantifier(((d_33_obj_).arr).UniqueElements, True, lambda0_)), _dafny.Seq("Not an array of strings"))
            if (d_34_valueOrError1_).IsFailure():
                return (d_34_valueOrError1_).PropagateFailure()
            elif True:
                d_36_arr_ = (d_33_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_36_arr_)[d_37_n_]).str for d_37_n_ in range(len(d_36_arr_))]))

    @staticmethod
    def GetArrayObject(key, obj):
        d_38_valueOrError0_ = default__.Get(key, obj)
        if (d_38_valueOrError0_).IsFailure():
            return (d_38_valueOrError0_).PropagateFailure()
        elif True:
            d_39_obj_ = (d_38_valueOrError0_).Extract()
            def lambda1_(forall_var_1_):
                d_41_s_: JSON_Values.JSON = forall_var_1_
                return not ((d_41_s_) in ((d_39_obj_).arr)) or ((d_41_s_).is_Object)

            d_40_valueOrError1_ = Wrappers.default__.Need(((d_39_obj_).is_Array) and (_dafny.quantifier(((d_39_obj_).arr).UniqueElements, True, lambda1_)), _dafny.Seq("Not an array of objects"))
            if (d_40_valueOrError1_).IsFailure():
                return (d_40_valueOrError1_).PropagateFailure()
            elif True:
                d_42_arr_ = (d_39_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_42_arr_)[d_43_n_]).obj for d_43_n_ in range(len(d_42_arr_))]))

    @staticmethod
    def SmallObjectToStringStringMap(key, obj):
        d_44_valueOrError0_ = default__.Get(key, obj)
        if (d_44_valueOrError0_).IsFailure():
            return (d_44_valueOrError0_).PropagateFailure()
        elif True:
            d_45_item_ = (d_44_valueOrError0_).Extract()
            return default__.JsonObjectToStringStringMap(d_45_item_)

    @staticmethod
    def GetOptionalSmallObjectToStringStringMap(key, obj):
        d_46_item_ = (default__.Get(key, obj)).ToOption()
        if (d_46_item_).is_Some:
            d_47_valueOrError0_ = default__.JsonObjectToStringStringMap((d_46_item_).value)
            if (d_47_valueOrError0_).IsFailure():
                return (d_47_valueOrError0_).PropagateFailure()
            elif True:
                d_48_m_ = (d_47_valueOrError0_).Extract()
                return Wrappers.Result_Success(Wrappers.Option_Some(d_48_m_))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def printJson(j):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(j))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def JsonObjectToStringStringMap(item):
        d_49_valueOrError0_ = Wrappers.default__.Need((item).is_Object, _dafny.Seq("Not an object"))
        if (d_49_valueOrError0_).IsFailure():
            return (d_49_valueOrError0_).PropagateFailure()
        elif True:
            d_50_obj_ = (item).obj
            def lambda2_(forall_var_2_):
                d_52_t_: tuple = forall_var_2_
                return not ((d_52_t_) in (d_50_obj_)) or (((d_52_t_)[1]).is_String)

            d_51_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier((d_50_obj_).UniqueElements, True, lambda2_), _dafny.Seq("Not a string string object"))
            if (d_51_valueOrError1_).IsFailure():
                return (d_51_valueOrError1_).PropagateFailure()
            elif True:
                def lambda3_(forall_var_3_):
                    def lambda4_(forall_var_4_):
                        d_55_j_: int = forall_var_4_
                        return not ((((0) <= (d_54_i_)) and ((d_54_i_) < (d_55_j_))) and ((d_55_j_) < (len(d_50_obj_)))) or ((((d_50_obj_)[d_54_i_])[0]) != (((d_50_obj_)[d_55_j_])[0]))

                    d_54_i_: int = forall_var_3_
                    return _dafny.quantifier(_dafny.IntegerRange((d_54_i_) + (1), len(d_50_obj_)), True, lambda4_)

                d_53_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(_dafny.IntegerRange(0, len(d_50_obj_)), True, lambda3_), _dafny.Seq("JSON serialization Error"))
                if (d_53_valueOrError2_).IsFailure():
                    return (d_53_valueOrError2_).PropagateFailure()
                elif True:
                    def iife2_():
                        coll2_ = _dafny.Map()
                        compr_2_: tuple
                        for compr_2_ in (d_50_obj_).Elements:
                            d_56_t_: tuple = compr_2_
                            if (d_56_t_) in (d_50_obj_):
                                coll2_[(d_56_t_)[0]] = ((d_56_t_)[1]).str
                        return _dafny.Map(coll2_)
                    return Wrappers.Result_Success(iife2_()
)

    @staticmethod
    def utf8EncodePair(key, value):
        d_57_valueOrError0_ = UTF8.default__.Encode(key)
        if (d_57_valueOrError0_).IsFailure():
            return (d_57_valueOrError0_).PropagateFailure()
        elif True:
            d_58_utf8Key_ = (d_57_valueOrError0_).Extract()
            d_59_valueOrError1_ = UTF8.default__.Encode(value)
            if (d_59_valueOrError1_).IsFailure():
                return (d_59_valueOrError1_).PropagateFailure()
            elif True:
                d_60_utf8Value_ = (d_59_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_58_utf8Key_, d_60_utf8Value_))

    @staticmethod
    def utf8EncodeMap(mapStringString):
        if (len(mapStringString)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife3_():
                coll3_ = _dafny.Map()
                compr_3_: _dafny.Seq
                for compr_3_ in (mapStringString).keys.Elements:
                    d_62_key_: _dafny.Seq = compr_3_
                    if (d_62_key_) in (mapStringString):
                        coll3_[d_62_key_] = default__.utf8EncodePair(d_62_key_, (mapStringString)[d_62_key_])
                return _dafny.Map(coll3_)
            d_61_encodedResults_ = iife3_()

            def lambda5_(forall_var_5_):
                d_64_r_: Wrappers.Result = forall_var_5_
                return not ((d_64_r_) in ((d_61_encodedResults_).values)) or ((d_64_r_).is_Success)

            d_63_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((d_61_encodedResults_).values).Elements, True, lambda5_), _dafny.Seq("String can not be UTF8 Encoded?"))
            if (d_63_valueOrError0_).IsFailure():
                return (d_63_valueOrError0_).PropagateFailure()
            elif True:
                def iife4_():
                    coll4_ = _dafny.Map()
                    compr_4_: Wrappers.Result
                    for compr_4_ in ((d_61_encodedResults_).values).Elements:
                        d_65_r_: Wrappers.Result = compr_4_
                        if (d_65_r_) in ((d_61_encodedResults_).values):
                            coll4_[((d_65_r_).value)[0]] = ((d_65_r_).value)[1]
                    return _dafny.Map(coll4_)
                return Wrappers.Result_Success(iife4_()
)

    @staticmethod
    def utf8EncodeSeq(seqOfStrings):
        d_66_encodedResults_ = _dafny.Seq([UTF8.default__.Encode((seqOfStrings)[d_67_i_]) for d_67_i_ in range(len(seqOfStrings))])
        def lambda6_(forall_var_6_):
            d_69_r_: Wrappers.Result = forall_var_6_
            return not ((d_69_r_) in (d_66_encodedResults_)) or ((d_69_r_).is_Success)

        d_68_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_66_encodedResults_).UniqueElements, True, lambda6_), _dafny.Seq("String can not be UTF8 Encoded?"))
        if (d_68_valueOrError0_).IsFailure():
            return (d_68_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(_dafny.Seq([((d_66_encodedResults_)[d_70_i_]).value for d_70_i_ in range(len(d_66_encodedResults_))]))

