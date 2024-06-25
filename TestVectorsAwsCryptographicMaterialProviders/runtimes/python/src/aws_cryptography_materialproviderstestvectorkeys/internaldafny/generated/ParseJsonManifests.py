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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeysVectorOperations as KeysVectorOperations
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyVectors as KeyVectors
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.TestVectors as TestVectors
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllHierarchy as AllHierarchy
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKms as AllKms
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsMrkAware as AllKmsMrkAware
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsMrkAwareDiscovery as AllKmsMrkAwareDiscovery
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsRsa as AllKmsRsa
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawRSA as AllRawRSA
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllDefaultCmm as AllDefaultCmm
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRequiredEncryptionContextCmm as AllRequiredEncryptionContextCmm
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllMulti as AllMulti
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WriteJsonManifests as WriteJsonManifests
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CompleteVectors as CompleteVectors

# Module: ParseJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildEncryptTestVector(keys, obj):
        hresult_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_802_i_: int
        d_802_i_ = len(obj)
        d_803_vectors_: _dafny.Seq
        d_803_vectors_ = _dafny.Seq([])
        while (d_802_i_) != (0):
            d_802_i_ = (d_802_i_) - (1)
            d_804_test_: Wrappers.Result
            d_804_test_ = default__.ToEncryptTestVector(keys, ((obj)[d_802_i_])[0], ((obj)[d_802_i_])[1])
            if (d_804_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_804_test_).error)
                return hresult_
            d_803_vectors_ = (_dafny.Seq([(d_804_test_).value])) + (d_803_vectors_)
        hresult_ = Wrappers.Result_Success(d_803_vectors_)
        return hresult_
        return hresult_

    @staticmethod
    def ToEncryptTestVector(keys, name, obj):
        pat_let_tv77_ = keys
        pat_let_tv78_ = keys
        pat_let_tv79_ = name
        pat_let_tv80_ = keys
        pat_let_tv81_ = name
        pat_let_tv82_ = keys
        pat_let_tv83_ = keys
        pat_let_tv84_ = name
        d_805_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("EncryptTestVector not an object"))
        if (d_805_valueOrError0_).IsFailure():
            return (d_805_valueOrError0_).PropagateFailure()
        elif True:
            d_806_obj_ = (obj).obj
            d_807_typString_ = _dafny.Seq("type")
            d_808_valueOrError1_ = JSONHelpers.default__.GetString(d_807_typString_, d_806_obj_)
            if (d_808_valueOrError1_).IsFailure():
                return (d_808_valueOrError1_).PropagateFailure()
            elif True:
                d_809_typ_ = (d_808_valueOrError1_).Extract()
                d_810_description_ = (JSONHelpers.default__.GetString(_dafny.Seq("description"), d_806_obj_)).ToOption()
                d_811_valueOrError2_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_806_obj_)
                if (d_811_valueOrError2_).IsFailure():
                    return (d_811_valueOrError2_).PropagateFailure()
                elif True:
                    d_812_encryptionContextStrings_ = (d_811_valueOrError2_).Extract()
                    d_813_valueOrError3_ = JSONHelpers.default__.utf8EncodeMap(d_812_encryptionContextStrings_)
                    if (d_813_valueOrError3_).IsFailure():
                        return (d_813_valueOrError3_).PropagateFailure()
                    elif True:
                        d_814_encryptionContext_ = (d_813_valueOrError3_).Extract()
                        d_815_valueOrError4_ = default__.GetAlgorithmSuiteInfo(d_806_obj_)
                        if (d_815_valueOrError4_).IsFailure():
                            return (d_815_valueOrError4_).PropagateFailure()
                        elif True:
                            d_816_algorithmSuite_ = (d_815_valueOrError4_).Extract()
                            d_817_valueOrError5_ = default__.GetRequiredEncryptionContextKeys(d_806_obj_)
                            if (d_817_valueOrError5_).IsFailure():
                                return (d_817_valueOrError5_).PropagateFailure()
                            elif True:
                                d_818_requiredEncryptionContextKeys_ = (d_817_valueOrError5_).Extract()
                                d_819_valueOrError6_ = default__.GetReproducedEncryptionContext(d_806_obj_)
                                if (d_819_valueOrError6_).IsFailure():
                                    return (d_819_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_820_reproducedEncryptionContext_ = (d_819_valueOrError6_).Extract()
                                    d_821_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_816_algorithmSuite_)
                                    d_822_maxPlaintextLength_ = (JSONHelpers.default__.GetPositiveLong(_dafny.Seq("maxPlaintextLength"), d_806_obj_)).ToOption()
                                    source23_ = d_809_typ_
                                    unmatched23 = True
                                    if unmatched23:
                                        if (source23_) == (_dafny.Seq("positive-keyring")):
                                            unmatched23 = False
                                            d_823_valueOrError7_ = default__.GetKeyDescription(pat_let_tv77_, _dafny.Seq("encryptKeyDescription"), d_806_obj_)
                                            if (d_823_valueOrError7_).IsFailure():
                                                return (d_823_valueOrError7_).PropagateFailure()
                                            elif True:
                                                d_824_encryptKeyDescription_ = (d_823_valueOrError7_).Extract()
                                                d_825_valueOrError8_ = default__.GetKeyDescription(pat_let_tv78_, _dafny.Seq("decryptKeyDescription"), d_806_obj_)
                                                if (d_825_valueOrError8_).IsFailure():
                                                    return (d_825_valueOrError8_).PropagateFailure()
                                                elif True:
                                                    d_826_decryptKeyDescription_ = (d_825_valueOrError8_).Extract()
                                                    return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(pat_let_tv79_, d_810_description_, d_814_encryptionContext_, d_821_commitmentPolicy_, d_816_algorithmSuite_, d_822_maxPlaintextLength_, d_818_requiredEncryptionContextKeys_, d_824_encryptKeyDescription_, d_826_decryptKeyDescription_, d_820_reproducedEncryptionContext_))
                                    if unmatched23:
                                        if (source23_) == (_dafny.Seq("negative-encrypt-keyring")):
                                            unmatched23 = False
                                            d_827_valueOrError9_ = default__.GetKeyDescription(pat_let_tv80_, _dafny.Seq("keyDescription"), d_806_obj_)
                                            if (d_827_valueOrError9_).IsFailure():
                                                return (d_827_valueOrError9_).PropagateFailure()
                                            elif True:
                                                d_828_keyDescription_ = (d_827_valueOrError9_).Extract()
                                                d_829_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_806_obj_)
                                                if (d_829_valueOrError10_).IsFailure():
                                                    return (d_829_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_830_errorDescription_ = (d_829_valueOrError10_).Extract()
                                                    d_831_valueOrError11_ = Wrappers.default__.Need((d_820_reproducedEncryptionContext_).is_None, _dafny.Seq("reproducedEncryptionContext not supported"))
                                                    if (d_831_valueOrError11_).IsFailure():
                                                        return (d_831_valueOrError11_).PropagateFailure()
                                                    elif True:
                                                        return Wrappers.Result_Success(TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(pat_let_tv81_, d_810_description_, d_814_encryptionContext_, d_821_commitmentPolicy_, d_816_algorithmSuite_, d_822_maxPlaintextLength_, d_818_requiredEncryptionContextKeys_, d_830_errorDescription_, d_828_keyDescription_))
                                    if unmatched23:
                                        if (source23_) == (_dafny.Seq("negative-decrypt-keyring")):
                                            unmatched23 = False
                                            d_832_valueOrError12_ = default__.GetKeyDescription(pat_let_tv82_, _dafny.Seq("encryptKeyDescription"), d_806_obj_)
                                            if (d_832_valueOrError12_).IsFailure():
                                                return (d_832_valueOrError12_).PropagateFailure()
                                            elif True:
                                                d_833_encryptKeyDescription_ = (d_832_valueOrError12_).Extract()
                                                d_834_valueOrError13_ = default__.GetKeyDescription(pat_let_tv83_, _dafny.Seq("decryptKeyDescription"), d_806_obj_)
                                                if (d_834_valueOrError13_).IsFailure():
                                                    return (d_834_valueOrError13_).PropagateFailure()
                                                elif True:
                                                    d_835_decryptKeyDescription_ = (d_834_valueOrError13_).Extract()
                                                    d_836_valueOrError14_ = JSONHelpers.default__.GetString(_dafny.Seq("decryptErrorDescription"), d_806_obj_)
                                                    if (d_836_valueOrError14_).IsFailure():
                                                        return (d_836_valueOrError14_).PropagateFailure()
                                                    elif True:
                                                        d_837_decryptErrorDescription_ = (d_836_valueOrError14_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(pat_let_tv84_, d_810_description_, d_814_encryptionContext_, d_821_commitmentPolicy_, d_816_algorithmSuite_, d_822_maxPlaintextLength_, d_818_requiredEncryptionContextKeys_, d_837_decryptErrorDescription_, d_833_encryptKeyDescription_, d_835_decryptKeyDescription_, d_820_reproducedEncryptionContext_))
                                    if unmatched23:
                                        d_838___v0_ = source23_
                                        unmatched23 = False
                                        return Wrappers.Result_Failure((_dafny.Seq("Unsupported EncryptTestVector type:")) + (d_809_typ_))
                                    raise Exception("unexpected control point")

    @staticmethod
    def GetKeyDescription(keyVectorClient, key, obj):
        d_839_valueOrError0_ = JSONHelpers.default__.Get(key, obj)
        if (d_839_valueOrError0_).IsFailure():
            return (d_839_valueOrError0_).PropagateFailure()
        elif True:
            d_840_keyDescriptionObject_ = (d_839_valueOrError0_).Extract()
            def lambda96_(d_842_e_):
                return (d_842_e_).ToString()

            d_841_valueOrError1_ = (JSON_API.default__.Serialize(d_840_keyDescriptionObject_)).MapFailure(lambda96_)
            if (d_841_valueOrError1_).IsFailure():
                return (d_841_valueOrError1_).PropagateFailure()
            elif True:
                d_843_descriptionStr_ = (d_841_valueOrError1_).Extract()
                d_844_valueOrError2_ = ((keyVectorClient).GetKeyDescription(AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput_GetKeyDescriptionInput(d_843_descriptionStr_))).MapFailure(default__.ErrorToString)
                if (d_844_valueOrError2_).IsFailure():
                    return (d_844_valueOrError2_).PropagateFailure()
                elif True:
                    d_845_keyDescriptionOutput_ = (d_844_valueOrError2_).Extract()
                    return Wrappers.Result_Success((d_845_keyDescriptionOutput_).keyDescription)

    @staticmethod
    def GetAlgorithmSuiteInfo(obj):
        d_846_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), obj)
        if (d_846_valueOrError0_).IsFailure():
            return (d_846_valueOrError0_).PropagateFailure()
        elif True:
            d_847_algorithmSuiteHex_ = (d_846_valueOrError0_).Extract()
            d_848_valueOrError1_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_847_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binary"))
            if (d_848_valueOrError1_).IsFailure():
                return (d_848_valueOrError1_).PropagateFailure()
            elif True:
                d_849_binaryId_ = HexStrings.default__.FromHexString(d_847_algorithmSuiteHex_)
                def lambda97_(d_850_algorithmSuiteHex_):
                    def lambda98_(d_851_e_):
                        return (_dafny.Seq("Invalid Suite:")) + (d_850_algorithmSuiteHex_)

                    return lambda98_

                return (AlgorithmSuites.default__.GetAlgorithmSuiteInfo(d_849_binaryId_)).MapFailure(lambda97_(d_847_algorithmSuiteHex_))

    @staticmethod
    def GetRequiredEncryptionContextKeys(obj):
        d_852_keysAsStrings_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), obj)).ToOption()
        source24_ = d_852_keysAsStrings_
        unmatched24 = True
        if unmatched24:
            if source24_.is_Some:
                d_853_s_ = source24_.value
                unmatched24 = False
                d_854_valueOrError0_ = JSONHelpers.default__.utf8EncodeSeq((d_852_keysAsStrings_).value)
                if (d_854_valueOrError0_).IsFailure():
                    return (d_854_valueOrError0_).PropagateFailure()
                elif True:
                    d_855_k_ = (d_854_valueOrError0_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_855_k_))
        if unmatched24:
            unmatched24 = False
            return Wrappers.Result_Success(Wrappers.Option_None())
        raise Exception("unexpected control point")

    @staticmethod
    def GetReproducedEncryptionContext(obj):
        d_856_valueOrError0_ = JSONHelpers.default__.GetOptionalSmallObjectToStringStringMap(_dafny.Seq("reproducedEncryptionContext"), obj)
        if (d_856_valueOrError0_).IsFailure():
            return (d_856_valueOrError0_).PropagateFailure()
        elif True:
            d_857_reproducedEncryptionContextStrings_ = (d_856_valueOrError0_).Extract()
            source25_ = d_857_reproducedEncryptionContextStrings_
            unmatched25 = True
            if unmatched25:
                if source25_.is_Some:
                    d_858_r_ = source25_.value
                    unmatched25 = False
                    d_859_valueOrError1_ = JSONHelpers.default__.utf8EncodeMap(d_858_r_)
                    if (d_859_valueOrError1_).IsFailure():
                        return (d_859_valueOrError1_).PropagateFailure()
                    elif True:
                        d_860_e_ = (d_859_valueOrError1_).Extract()
                        return Wrappers.Result_Success(Wrappers.Option_Some(d_860_e_))
            if unmatched25:
                unmatched25 = False
                return Wrappers.Result_Success(Wrappers.Option_None())
            raise Exception("unexpected control point")

    @staticmethod
    def ErrorToString(e):
        source26_ = e
        unmatched26 = True
        if unmatched26:
            if source26_.is_KeyVectorException:
                d_861_message_ = source26_.message
                unmatched26 = False
                return d_861_message_
        if unmatched26:
            if source26_.is_AwsCryptographyMaterialProviders:
                d_862_mplError_ = source26_.AwsCryptographyMaterialProviders
                unmatched26 = False
                source27_ = d_862_mplError_
                unmatched27 = True
                if unmatched27:
                    if source27_.is_AwsCryptographicMaterialProvidersException:
                        d_863_message_ = source27_.message
                        unmatched27 = False
                        return d_863_message_
                if unmatched27:
                    d_864___v1_ = source27_
                    unmatched27 = False
                    return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
                raise Exception("unexpected control point")
        if unmatched26:
            d_865___v2_ = source26_
            unmatched26 = False
            return _dafny.Seq("Unmapped KeyVectorException")
        raise Exception("unexpected control point")

    @staticmethod
    def BuildDecryptTestVector(keys, obj):
        hresult_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_866_i_: int
        d_866_i_ = len(obj)
        d_867_vectors_: _dafny.Seq
        d_867_vectors_ = _dafny.Seq([])
        while (d_866_i_) != (0):
            d_866_i_ = (d_866_i_) - (1)
            d_868_test_: Wrappers.Result
            d_868_test_ = default__.ToDecryptTestVector(keys, ((obj)[d_866_i_])[0], ((obj)[d_866_i_])[1])
            if (d_868_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_868_test_).error)
                return hresult_
            d_867_vectors_ = (_dafny.Seq([(d_868_test_).value])) + (d_867_vectors_)
        hresult_ = Wrappers.Result_Success(d_867_vectors_)
        return hresult_
        return hresult_

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
    def GetEncryptedDataKeys(obj):
        d_869_valueOrError0_ = JSONHelpers.default__.GetArray(_dafny.Seq("encryptedDataKeys"), obj)
        if (d_869_valueOrError0_).IsFailure():
            return (d_869_valueOrError0_).PropagateFailure()
        elif True:
            d_870_encryptedDataKeysJson_ = (d_869_valueOrError0_).Extract()
            return Seq.default__.MapWithResult(default__.GetEncryptedDataKey, d_870_encryptedDataKeysJson_)

    @staticmethod
    def GetEncryptedDataKey(json):
        d_871_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("Encrypted data key is not an object"))
        if (d_871_valueOrError0_).IsFailure():
            return (d_871_valueOrError0_).PropagateFailure()
        elif True:
            d_872_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), (json).obj)
            if (d_872_valueOrError1_).IsFailure():
                return (d_872_valueOrError1_).PropagateFailure()
            elif True:
                d_873_keyProviderId_ = (d_872_valueOrError1_).Extract()
                d_874_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), (json).obj)
                if (d_874_valueOrError2_).IsFailure():
                    return (d_874_valueOrError2_).PropagateFailure()
                elif True:
                    d_875_keyProviderInfo_ = (d_874_valueOrError2_).Extract()
                    d_876_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), (json).obj)
                    if (d_876_valueOrError3_).IsFailure():
                        return (d_876_valueOrError3_).PropagateFailure()
                    elif True:
                        d_877_ciphertext_ = (d_876_valueOrError3_).Extract()
                        d_878_valueOrError4_ = UTF8.default__.Encode(d_873_keyProviderId_)
                        if (d_878_valueOrError4_).IsFailure():
                            return (d_878_valueOrError4_).PropagateFailure()
                        elif True:
                            d_879_keyProviderId_ = (d_878_valueOrError4_).Extract()
                            d_880_valueOrError5_ = Base64.default__.Decode(d_875_keyProviderInfo_)
                            if (d_880_valueOrError5_).IsFailure():
                                return (d_880_valueOrError5_).PropagateFailure()
                            elif True:
                                d_881_keyProviderInfo_ = (d_880_valueOrError5_).Extract()
                                d_882_valueOrError6_ = Base64.default__.Decode(d_877_ciphertext_)
                                if (d_882_valueOrError6_).IsFailure():
                                    return (d_882_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_883_ciphertext_ = (d_882_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(d_879_keyProviderId_, d_881_keyProviderInfo_, d_883_ciphertext_))

    @staticmethod
    def GetExpectedResult(obj):
        d_884_valueOrError0_ = JSONHelpers.default__.GetObject(_dafny.Seq("result"), obj)
        if (d_884_valueOrError0_).IsFailure():
            return (d_884_valueOrError0_).PropagateFailure()
        elif True:
            d_885_result_ = (d_884_valueOrError0_).Extract()
            d_886_valueOrError1_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), d_885_result_)
            if (d_886_valueOrError1_).IsFailure():
                return (d_886_valueOrError1_).PropagateFailure()
            elif True:
                d_887_plaintextDataKey_ = (d_886_valueOrError1_).Extract()
                d_888_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("symmetricSigningKey"), d_885_result_)
                if (d_888_valueOrError2_).IsFailure():
                    return (d_888_valueOrError2_).PropagateFailure()
                elif True:
                    d_889_symmetricSigningKey_ = (d_888_valueOrError2_).Extract()
                    d_890_valueOrError3_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_885_result_)
                    if (d_890_valueOrError3_).IsFailure():
                        return (d_890_valueOrError3_).PropagateFailure()
                    elif True:
                        d_891_requiredEncryptionContextKeys_ = (d_890_valueOrError3_).Extract()
                        def iife95_(_pat_let22_0):
                            def iife96_(d_893_valueOrError5_):
                                def iife97_(_pat_let23_0):
                                    def iife98_(d_894_p_):
                                        return Wrappers.Result_Success(Wrappers.Option_Some(d_894_p_))
                                    return iife98_(_pat_let23_0)
                                return ((d_893_valueOrError5_).PropagateFailure() if (d_893_valueOrError5_).IsFailure() else iife97_((d_893_valueOrError5_).Extract()))
                            return iife96_(_pat_let22_0)
                        d_892_valueOrError4_ = (iife95_(Base64.default__.Decode((d_887_plaintextDataKey_).value)) if (d_887_plaintextDataKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                        if (d_892_valueOrError4_).IsFailure():
                            return (d_892_valueOrError4_).PropagateFailure()
                        elif True:
                            d_895_plaintextDataKey_ = (d_892_valueOrError4_).Extract()
                            def iife99_(_pat_let24_0):
                                def iife100_(d_897_valueOrError7_):
                                    def iife101_(_pat_let25_0):
                                        def iife102_(d_898_p_):
                                            return Wrappers.Result_Success(Wrappers.Option_Some(d_898_p_))
                                        return iife102_(_pat_let25_0)
                                    return ((d_897_valueOrError7_).PropagateFailure() if (d_897_valueOrError7_).IsFailure() else iife101_((d_897_valueOrError7_).Extract()))
                                return iife100_(_pat_let24_0)
                            d_896_valueOrError6_ = (iife99_(Base64.default__.Decode((d_889_symmetricSigningKey_).value)) if (d_889_symmetricSigningKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                            if (d_896_valueOrError6_).IsFailure():
                                return (d_896_valueOrError6_).PropagateFailure()
                            elif True:
                                d_899_symmetricSigningKey_ = (d_896_valueOrError6_).Extract()
                                d_900_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_891_requiredEncryptionContextKeys_)
                                if (d_900_valueOrError8_).IsFailure():
                                    return (d_900_valueOrError8_).PropagateFailure()
                                elif True:
                                    d_901_requiredEncryptionContextKeys_ = (d_900_valueOrError8_).Extract()
                                    return Wrappers.Result_Success(TestVectors.DecryptResult_DecryptResult(d_895_plaintextDataKey_, d_899_symmetricSigningKey_, d_901_requiredEncryptionContextKeys_))

    @staticmethod
    def ToDecryptTestVector(keys, name, json):
        pat_let_tv85_ = name
        pat_let_tv86_ = name
        d_902_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("DecryptTestVector not an object"))
        if (d_902_valueOrError0_).IsFailure():
            return (d_902_valueOrError0_).PropagateFailure()
        elif True:
            d_903_obj_ = (json).obj
            d_904_typString_ = _dafny.Seq("type")
            d_905_valueOrError1_ = JSONHelpers.default__.GetString(d_904_typString_, d_903_obj_)
            if (d_905_valueOrError1_).IsFailure():
                return (d_905_valueOrError1_).PropagateFailure()
            elif True:
                d_906_typ_ = (d_905_valueOrError1_).Extract()
                d_907_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("description"), d_903_obj_)
                if (d_907_valueOrError2_).IsFailure():
                    return (d_907_valueOrError2_).PropagateFailure()
                elif True:
                    d_908_description_ = (d_907_valueOrError2_).Extract()
                    d_909_valueOrError3_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_903_obj_)
                    if (d_909_valueOrError3_).IsFailure():
                        return (d_909_valueOrError3_).PropagateFailure()
                    elif True:
                        d_910_encryptionContextStrings_ = (d_909_valueOrError3_).Extract()
                        d_911_valueOrError4_ = JSONHelpers.default__.utf8EncodeMap(d_910_encryptionContextStrings_)
                        if (d_911_valueOrError4_).IsFailure():
                            return (d_911_valueOrError4_).PropagateFailure()
                        elif True:
                            d_912_encryptionContext_ = (d_911_valueOrError4_).Extract()
                            d_913_valueOrError5_ = default__.GetAlgorithmSuiteInfo(d_903_obj_)
                            if (d_913_valueOrError5_).IsFailure():
                                return (d_913_valueOrError5_).PropagateFailure()
                            elif True:
                                d_914_algorithmSuite_ = (d_913_valueOrError5_).Extract()
                                d_915_valueOrError6_ = default__.GetReproducedEncryptionContext(d_903_obj_)
                                if (d_915_valueOrError6_).IsFailure():
                                    return (d_915_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_916_reproducedEncryptionContext_ = (d_915_valueOrError6_).Extract()
                                    d_917_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_914_algorithmSuite_)
                                    d_918_valueOrError7_ = default__.GetKeyDescription(keys, _dafny.Seq("keyDescription"), d_903_obj_)
                                    if (d_918_valueOrError7_).IsFailure():
                                        return (d_918_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_919_keyDescription_ = (d_918_valueOrError7_).Extract()
                                        d_920_valueOrError8_ = default__.GetEncryptedDataKeys(d_903_obj_)
                                        if (d_920_valueOrError8_).IsFailure():
                                            return (d_920_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_921_encryptedDataKeys_ = (d_920_valueOrError8_).Extract()
                                            source28_ = d_906_typ_
                                            unmatched28 = True
                                            if unmatched28:
                                                if (source28_) == (_dafny.Seq("positive-keyring")):
                                                    unmatched28 = False
                                                    d_922_valueOrError9_ = default__.GetExpectedResult(d_903_obj_)
                                                    if (d_922_valueOrError9_).IsFailure():
                                                        return (d_922_valueOrError9_).PropagateFailure()
                                                    elif True:
                                                        d_923_expectedResult_ = (d_922_valueOrError9_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.DecryptTestVector_PositiveDecryptKeyringTest(pat_let_tv85_, d_914_algorithmSuite_, d_917_commitmentPolicy_, d_921_encryptedDataKeys_, d_912_encryptionContext_, d_919_keyDescription_, d_923_expectedResult_, d_908_description_, d_916_reproducedEncryptionContext_))
                                            if unmatched28:
                                                if (source28_) == (_dafny.Seq("negative-keyring")):
                                                    unmatched28 = False
                                                    d_924_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_903_obj_)
                                                    if (d_924_valueOrError10_).IsFailure():
                                                        return (d_924_valueOrError10_).PropagateFailure()
                                                    elif True:
                                                        d_925_errorDescription_ = (d_924_valueOrError10_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.DecryptTestVector_NegativeDecryptKeyringTest(pat_let_tv86_, d_914_algorithmSuite_, d_917_commitmentPolicy_, d_921_encryptedDataKeys_, d_912_encryptionContext_, d_925_errorDescription_, d_919_keyDescription_, d_916_reproducedEncryptionContext_, d_908_description_))
                                            if unmatched28:
                                                d_926___v3_ = source28_
                                                unmatched28 = False
                                                return Wrappers.Result_Failure((_dafny.Seq("Unsupported DecryptTestVector type:")) + (d_906_typ_))
                                            raise Exception("unexpected control point")

