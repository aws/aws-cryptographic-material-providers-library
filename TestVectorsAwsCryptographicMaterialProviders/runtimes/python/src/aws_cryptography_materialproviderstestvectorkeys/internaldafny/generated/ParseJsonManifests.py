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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsEcdh as AllKmsEcdh
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawRSA as AllRawRSA
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawECDH as AllRawECDH
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
        d_807_i_: int
        d_807_i_ = len(obj)
        d_808_vectors_: _dafny.Seq
        d_808_vectors_ = _dafny.Seq([])
        while (d_807_i_) != (0):
            d_807_i_ = (d_807_i_) - (1)
            d_809_test_: Wrappers.Result
            d_809_test_ = default__.ToEncryptTestVector(keys, ((obj)[d_807_i_])[0], ((obj)[d_807_i_])[1])
            if (d_809_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_809_test_).error)
                return hresult_
            d_808_vectors_ = (_dafny.Seq([(d_809_test_).value])) + (d_808_vectors_)
        hresult_ = Wrappers.Result_Success(d_808_vectors_)
        return hresult_
        return hresult_

    @staticmethod
    def ToEncryptTestVector(keys, name, obj):
        pat_let_tv79_ = keys
        pat_let_tv80_ = keys
        pat_let_tv81_ = name
        pat_let_tv82_ = keys
        pat_let_tv83_ = name
        pat_let_tv84_ = keys
        pat_let_tv85_ = keys
        pat_let_tv86_ = name
        d_810_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("EncryptTestVector not an object"))
        if (d_810_valueOrError0_).IsFailure():
            return (d_810_valueOrError0_).PropagateFailure()
        elif True:
            d_811_obj_ = (obj).obj
            d_812_typString_ = _dafny.Seq("type")
            d_813_valueOrError1_ = JSONHelpers.default__.GetString(d_812_typString_, d_811_obj_)
            if (d_813_valueOrError1_).IsFailure():
                return (d_813_valueOrError1_).PropagateFailure()
            elif True:
                d_814_typ_ = (d_813_valueOrError1_).Extract()
                d_815_description_ = (JSONHelpers.default__.GetString(_dafny.Seq("description"), d_811_obj_)).ToOption()
                d_816_valueOrError2_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_811_obj_)
                if (d_816_valueOrError2_).IsFailure():
                    return (d_816_valueOrError2_).PropagateFailure()
                elif True:
                    d_817_encryptionContextStrings_ = (d_816_valueOrError2_).Extract()
                    d_818_valueOrError3_ = JSONHelpers.default__.utf8EncodeMap(d_817_encryptionContextStrings_)
                    if (d_818_valueOrError3_).IsFailure():
                        return (d_818_valueOrError3_).PropagateFailure()
                    elif True:
                        d_819_encryptionContext_ = (d_818_valueOrError3_).Extract()
                        d_820_valueOrError4_ = default__.GetAlgorithmSuiteInfo(d_811_obj_)
                        if (d_820_valueOrError4_).IsFailure():
                            return (d_820_valueOrError4_).PropagateFailure()
                        elif True:
                            d_821_algorithmSuite_ = (d_820_valueOrError4_).Extract()
                            d_822_valueOrError5_ = default__.GetRequiredEncryptionContextKeys(d_811_obj_)
                            if (d_822_valueOrError5_).IsFailure():
                                return (d_822_valueOrError5_).PropagateFailure()
                            elif True:
                                d_823_requiredEncryptionContextKeys_ = (d_822_valueOrError5_).Extract()
                                d_824_valueOrError6_ = default__.GetReproducedEncryptionContext(d_811_obj_)
                                if (d_824_valueOrError6_).IsFailure():
                                    return (d_824_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_825_reproducedEncryptionContext_ = (d_824_valueOrError6_).Extract()
                                    d_826_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_821_algorithmSuite_)
                                    d_827_maxPlaintextLength_ = (JSONHelpers.default__.GetPositiveLong(_dafny.Seq("maxPlaintextLength"), d_811_obj_)).ToOption()
                                    source27_ = d_814_typ_
                                    unmatched27 = True
                                    if unmatched27:
                                        if (source27_) == (_dafny.Seq("positive-keyring")):
                                            unmatched27 = False
                                            d_828_valueOrError7_ = default__.GetKeyDescription(pat_let_tv79_, _dafny.Seq("encryptKeyDescription"), d_811_obj_)
                                            if (d_828_valueOrError7_).IsFailure():
                                                return (d_828_valueOrError7_).PropagateFailure()
                                            elif True:
                                                d_829_encryptKeyDescription_ = (d_828_valueOrError7_).Extract()
                                                d_830_valueOrError8_ = default__.GetKeyDescription(pat_let_tv80_, _dafny.Seq("decryptKeyDescription"), d_811_obj_)
                                                if (d_830_valueOrError8_).IsFailure():
                                                    return (d_830_valueOrError8_).PropagateFailure()
                                                elif True:
                                                    d_831_decryptKeyDescription_ = (d_830_valueOrError8_).Extract()
                                                    return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(pat_let_tv81_, d_815_description_, d_819_encryptionContext_, d_826_commitmentPolicy_, d_821_algorithmSuite_, d_827_maxPlaintextLength_, d_823_requiredEncryptionContextKeys_, d_829_encryptKeyDescription_, d_831_decryptKeyDescription_, d_825_reproducedEncryptionContext_))
                                    if unmatched27:
                                        if (source27_) == (_dafny.Seq("negative-encrypt-keyring")):
                                            unmatched27 = False
                                            d_832_valueOrError9_ = default__.GetKeyDescription(pat_let_tv82_, _dafny.Seq("keyDescription"), d_811_obj_)
                                            if (d_832_valueOrError9_).IsFailure():
                                                return (d_832_valueOrError9_).PropagateFailure()
                                            elif True:
                                                d_833_keyDescription_ = (d_832_valueOrError9_).Extract()
                                                d_834_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_811_obj_)
                                                if (d_834_valueOrError10_).IsFailure():
                                                    return (d_834_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_835_errorDescription_ = (d_834_valueOrError10_).Extract()
                                                    d_836_valueOrError11_ = Wrappers.default__.Need((d_825_reproducedEncryptionContext_).is_None, _dafny.Seq("reproducedEncryptionContext not supported"))
                                                    if (d_836_valueOrError11_).IsFailure():
                                                        return (d_836_valueOrError11_).PropagateFailure()
                                                    elif True:
                                                        return Wrappers.Result_Success(TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(pat_let_tv83_, d_815_description_, d_819_encryptionContext_, d_826_commitmentPolicy_, d_821_algorithmSuite_, d_827_maxPlaintextLength_, d_823_requiredEncryptionContextKeys_, d_835_errorDescription_, d_833_keyDescription_))
                                    if unmatched27:
                                        if (source27_) == (_dafny.Seq("negative-decrypt-keyring")):
                                            unmatched27 = False
                                            d_837_valueOrError12_ = default__.GetKeyDescription(pat_let_tv84_, _dafny.Seq("encryptKeyDescription"), d_811_obj_)
                                            if (d_837_valueOrError12_).IsFailure():
                                                return (d_837_valueOrError12_).PropagateFailure()
                                            elif True:
                                                d_838_encryptKeyDescription_ = (d_837_valueOrError12_).Extract()
                                                d_839_valueOrError13_ = default__.GetKeyDescription(pat_let_tv85_, _dafny.Seq("decryptKeyDescription"), d_811_obj_)
                                                if (d_839_valueOrError13_).IsFailure():
                                                    return (d_839_valueOrError13_).PropagateFailure()
                                                elif True:
                                                    d_840_decryptKeyDescription_ = (d_839_valueOrError13_).Extract()
                                                    d_841_valueOrError14_ = JSONHelpers.default__.GetString(_dafny.Seq("decryptErrorDescription"), d_811_obj_)
                                                    if (d_841_valueOrError14_).IsFailure():
                                                        return (d_841_valueOrError14_).PropagateFailure()
                                                    elif True:
                                                        d_842_decryptErrorDescription_ = (d_841_valueOrError14_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(pat_let_tv86_, d_815_description_, d_819_encryptionContext_, d_826_commitmentPolicy_, d_821_algorithmSuite_, d_827_maxPlaintextLength_, d_823_requiredEncryptionContextKeys_, d_842_decryptErrorDescription_, d_838_encryptKeyDescription_, d_840_decryptKeyDescription_, d_825_reproducedEncryptionContext_))
                                    if unmatched27:
                                        unmatched27 = False
                                        return Wrappers.Result_Failure((_dafny.Seq("Unsupported EncryptTestVector type:")) + (d_814_typ_))
                                    raise Exception("unexpected control point")

    @staticmethod
    def GetKeyDescription(keyVectorClient, key, obj):
        d_843_valueOrError0_ = JSONHelpers.default__.Get(key, obj)
        if (d_843_valueOrError0_).IsFailure():
            return (d_843_valueOrError0_).PropagateFailure()
        elif True:
            d_844_keyDescriptionObject_ = (d_843_valueOrError0_).Extract()
            def lambda111_(d_846_e_):
                return (d_846_e_).ToString()

            d_845_valueOrError1_ = (JSON_API.default__.Serialize(d_844_keyDescriptionObject_)).MapFailure(lambda111_)
            if (d_845_valueOrError1_).IsFailure():
                return (d_845_valueOrError1_).PropagateFailure()
            elif True:
                d_847_descriptionStr_ = (d_845_valueOrError1_).Extract()
                d_848_valueOrError2_ = ((keyVectorClient).GetKeyDescription(AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput_GetKeyDescriptionInput(d_847_descriptionStr_))).MapFailure(default__.ErrorToString)
                if (d_848_valueOrError2_).IsFailure():
                    return (d_848_valueOrError2_).PropagateFailure()
                elif True:
                    d_849_keyDescriptionOutput_ = (d_848_valueOrError2_).Extract()
                    return Wrappers.Result_Success((d_849_keyDescriptionOutput_).keyDescription)

    @staticmethod
    def GetAlgorithmSuiteInfo(obj):
        d_850_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), obj)
        if (d_850_valueOrError0_).IsFailure():
            return (d_850_valueOrError0_).PropagateFailure()
        elif True:
            d_851_algorithmSuiteHex_ = (d_850_valueOrError0_).Extract()
            d_852_valueOrError1_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_851_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binary"))
            if (d_852_valueOrError1_).IsFailure():
                return (d_852_valueOrError1_).PropagateFailure()
            elif True:
                d_853_binaryId_ = HexStrings.default__.FromHexString(d_851_algorithmSuiteHex_)
                def lambda112_(d_854_algorithmSuiteHex_):
                    def lambda113_(d_855_e_):
                        return (_dafny.Seq("Invalid Suite:")) + (d_854_algorithmSuiteHex_)

                    return lambda113_

                return (AlgorithmSuites.default__.GetAlgorithmSuiteInfo(d_853_binaryId_)).MapFailure(lambda112_(d_851_algorithmSuiteHex_))

    @staticmethod
    def GetRequiredEncryptionContextKeys(obj):
        d_856_keysAsStrings_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), obj)).ToOption()
        source28_ = d_856_keysAsStrings_
        unmatched28 = True
        if unmatched28:
            if source28_.is_Some:
                d_857_s_ = source28_.value
                unmatched28 = False
                d_858_valueOrError0_ = JSONHelpers.default__.utf8EncodeSeq((d_856_keysAsStrings_).value)
                if (d_858_valueOrError0_).IsFailure():
                    return (d_858_valueOrError0_).PropagateFailure()
                elif True:
                    d_859_k_ = (d_858_valueOrError0_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_859_k_))
        if unmatched28:
            unmatched28 = False
            return Wrappers.Result_Success(Wrappers.Option_None())
        raise Exception("unexpected control point")

    @staticmethod
    def GetReproducedEncryptionContext(obj):
        d_860_valueOrError0_ = JSONHelpers.default__.GetOptionalSmallObjectToStringStringMap(_dafny.Seq("reproducedEncryptionContext"), obj)
        if (d_860_valueOrError0_).IsFailure():
            return (d_860_valueOrError0_).PropagateFailure()
        elif True:
            d_861_reproducedEncryptionContextStrings_ = (d_860_valueOrError0_).Extract()
            source29_ = d_861_reproducedEncryptionContextStrings_
            unmatched29 = True
            if unmatched29:
                if source29_.is_Some:
                    d_862_r_ = source29_.value
                    unmatched29 = False
                    d_863_valueOrError1_ = JSONHelpers.default__.utf8EncodeMap(d_862_r_)
                    if (d_863_valueOrError1_).IsFailure():
                        return (d_863_valueOrError1_).PropagateFailure()
                    elif True:
                        d_864_e_ = (d_863_valueOrError1_).Extract()
                        return Wrappers.Result_Success(Wrappers.Option_Some(d_864_e_))
            if unmatched29:
                unmatched29 = False
                return Wrappers.Result_Success(Wrappers.Option_None())
            raise Exception("unexpected control point")

    @staticmethod
    def ErrorToString(e):
        source30_ = e
        unmatched30 = True
        if unmatched30:
            if source30_.is_KeyVectorException:
                d_865_message_ = source30_.message
                unmatched30 = False
                return d_865_message_
        if unmatched30:
            if source30_.is_AwsCryptographyMaterialProviders:
                d_866_mplError_ = source30_.AwsCryptographyMaterialProviders
                unmatched30 = False
                source31_ = d_866_mplError_
                unmatched31 = True
                if unmatched31:
                    if source31_.is_AwsCryptographicMaterialProvidersException:
                        d_867_message_ = source31_.message
                        unmatched31 = False
                        return d_867_message_
                if unmatched31:
                    unmatched31 = False
                    return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
                raise Exception("unexpected control point")
        if unmatched30:
            unmatched30 = False
            return _dafny.Seq("Unmapped KeyVectorException")
        raise Exception("unexpected control point")

    @staticmethod
    def BuildDecryptTestVector(keys, obj):
        hresult_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_868_i_: int
        d_868_i_ = len(obj)
        d_869_vectors_: _dafny.Seq
        d_869_vectors_ = _dafny.Seq([])
        while (d_868_i_) != (0):
            d_868_i_ = (d_868_i_) - (1)
            d_870_test_: Wrappers.Result
            d_870_test_ = default__.ToDecryptTestVector(keys, ((obj)[d_868_i_])[0], ((obj)[d_868_i_])[1])
            if (d_870_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_870_test_).error)
                return hresult_
            d_869_vectors_ = (_dafny.Seq([(d_870_test_).value])) + (d_869_vectors_)
        hresult_ = Wrappers.Result_Success(d_869_vectors_)
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
        d_871_valueOrError0_ = JSONHelpers.default__.GetArray(_dafny.Seq("encryptedDataKeys"), obj)
        if (d_871_valueOrError0_).IsFailure():
            return (d_871_valueOrError0_).PropagateFailure()
        elif True:
            d_872_encryptedDataKeysJson_ = (d_871_valueOrError0_).Extract()
            return Seq.default__.MapWithResult(default__.GetEncryptedDataKey, d_872_encryptedDataKeysJson_)

    @staticmethod
    def GetEncryptedDataKey(json):
        d_873_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("Encrypted data key is not an object"))
        if (d_873_valueOrError0_).IsFailure():
            return (d_873_valueOrError0_).PropagateFailure()
        elif True:
            d_874_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), (json).obj)
            if (d_874_valueOrError1_).IsFailure():
                return (d_874_valueOrError1_).PropagateFailure()
            elif True:
                d_875_keyProviderId_ = (d_874_valueOrError1_).Extract()
                d_876_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), (json).obj)
                if (d_876_valueOrError2_).IsFailure():
                    return (d_876_valueOrError2_).PropagateFailure()
                elif True:
                    d_877_keyProviderInfo_ = (d_876_valueOrError2_).Extract()
                    d_878_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), (json).obj)
                    if (d_878_valueOrError3_).IsFailure():
                        return (d_878_valueOrError3_).PropagateFailure()
                    elif True:
                        d_879_ciphertext_ = (d_878_valueOrError3_).Extract()
                        d_880_valueOrError4_ = UTF8.default__.Encode(d_875_keyProviderId_)
                        if (d_880_valueOrError4_).IsFailure():
                            return (d_880_valueOrError4_).PropagateFailure()
                        elif True:
                            d_881_keyProviderId_ = (d_880_valueOrError4_).Extract()
                            d_882_valueOrError5_ = Base64.default__.Decode(d_877_keyProviderInfo_)
                            if (d_882_valueOrError5_).IsFailure():
                                return (d_882_valueOrError5_).PropagateFailure()
                            elif True:
                                d_883_keyProviderInfo_ = (d_882_valueOrError5_).Extract()
                                d_884_valueOrError6_ = Base64.default__.Decode(d_879_ciphertext_)
                                if (d_884_valueOrError6_).IsFailure():
                                    return (d_884_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_885_ciphertext_ = (d_884_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(d_881_keyProviderId_, d_883_keyProviderInfo_, d_885_ciphertext_))

    @staticmethod
    def GetExpectedResult(obj):
        d_886_valueOrError0_ = JSONHelpers.default__.GetObject(_dafny.Seq("result"), obj)
        if (d_886_valueOrError0_).IsFailure():
            return (d_886_valueOrError0_).PropagateFailure()
        elif True:
            d_887_result_ = (d_886_valueOrError0_).Extract()
            d_888_valueOrError1_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), d_887_result_)
            if (d_888_valueOrError1_).IsFailure():
                return (d_888_valueOrError1_).PropagateFailure()
            elif True:
                d_889_plaintextDataKey_ = (d_888_valueOrError1_).Extract()
                d_890_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("symmetricSigningKey"), d_887_result_)
                if (d_890_valueOrError2_).IsFailure():
                    return (d_890_valueOrError2_).PropagateFailure()
                elif True:
                    d_891_symmetricSigningKey_ = (d_890_valueOrError2_).Extract()
                    d_892_valueOrError3_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_887_result_)
                    if (d_892_valueOrError3_).IsFailure():
                        return (d_892_valueOrError3_).PropagateFailure()
                    elif True:
                        d_893_requiredEncryptionContextKeys_ = (d_892_valueOrError3_).Extract()
                        def iife106_(_pat_let22_0):
                            def iife107_(d_895_valueOrError5_):
                                def iife108_(_pat_let23_0):
                                    def iife109_(d_896_p_):
                                        return Wrappers.Result_Success(Wrappers.Option_Some(d_896_p_))
                                    return iife109_(_pat_let23_0)
                                return ((d_895_valueOrError5_).PropagateFailure() if (d_895_valueOrError5_).IsFailure() else iife108_((d_895_valueOrError5_).Extract()))
                            return iife107_(_pat_let22_0)
                        d_894_valueOrError4_ = (iife106_(Base64.default__.Decode((d_889_plaintextDataKey_).value)) if (d_889_plaintextDataKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                        if (d_894_valueOrError4_).IsFailure():
                            return (d_894_valueOrError4_).PropagateFailure()
                        elif True:
                            d_897_plaintextDataKey_ = (d_894_valueOrError4_).Extract()
                            def iife110_(_pat_let24_0):
                                def iife111_(d_899_valueOrError7_):
                                    def iife112_(_pat_let25_0):
                                        def iife113_(d_900_p_):
                                            return Wrappers.Result_Success(Wrappers.Option_Some(d_900_p_))
                                        return iife113_(_pat_let25_0)
                                    return ((d_899_valueOrError7_).PropagateFailure() if (d_899_valueOrError7_).IsFailure() else iife112_((d_899_valueOrError7_).Extract()))
                                return iife111_(_pat_let24_0)
                            d_898_valueOrError6_ = (iife110_(Base64.default__.Decode((d_891_symmetricSigningKey_).value)) if (d_891_symmetricSigningKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                            if (d_898_valueOrError6_).IsFailure():
                                return (d_898_valueOrError6_).PropagateFailure()
                            elif True:
                                d_901_symmetricSigningKey_ = (d_898_valueOrError6_).Extract()
                                d_902_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_893_requiredEncryptionContextKeys_)
                                if (d_902_valueOrError8_).IsFailure():
                                    return (d_902_valueOrError8_).PropagateFailure()
                                elif True:
                                    d_903_requiredEncryptionContextKeys_ = (d_902_valueOrError8_).Extract()
                                    return Wrappers.Result_Success(TestVectors.DecryptResult_DecryptResult(d_897_plaintextDataKey_, d_901_symmetricSigningKey_, d_903_requiredEncryptionContextKeys_))

    @staticmethod
    def ToDecryptTestVector(keys, name, json):
        pat_let_tv87_ = name
        pat_let_tv88_ = name
        d_904_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("DecryptTestVector not an object"))
        if (d_904_valueOrError0_).IsFailure():
            return (d_904_valueOrError0_).PropagateFailure()
        elif True:
            d_905_obj_ = (json).obj
            d_906_typString_ = _dafny.Seq("type")
            d_907_valueOrError1_ = JSONHelpers.default__.GetString(d_906_typString_, d_905_obj_)
            if (d_907_valueOrError1_).IsFailure():
                return (d_907_valueOrError1_).PropagateFailure()
            elif True:
                d_908_typ_ = (d_907_valueOrError1_).Extract()
                d_909_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("description"), d_905_obj_)
                if (d_909_valueOrError2_).IsFailure():
                    return (d_909_valueOrError2_).PropagateFailure()
                elif True:
                    d_910_description_ = (d_909_valueOrError2_).Extract()
                    d_911_valueOrError3_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_905_obj_)
                    if (d_911_valueOrError3_).IsFailure():
                        return (d_911_valueOrError3_).PropagateFailure()
                    elif True:
                        d_912_encryptionContextStrings_ = (d_911_valueOrError3_).Extract()
                        d_913_valueOrError4_ = JSONHelpers.default__.utf8EncodeMap(d_912_encryptionContextStrings_)
                        if (d_913_valueOrError4_).IsFailure():
                            return (d_913_valueOrError4_).PropagateFailure()
                        elif True:
                            d_914_encryptionContext_ = (d_913_valueOrError4_).Extract()
                            d_915_valueOrError5_ = default__.GetAlgorithmSuiteInfo(d_905_obj_)
                            if (d_915_valueOrError5_).IsFailure():
                                return (d_915_valueOrError5_).PropagateFailure()
                            elif True:
                                d_916_algorithmSuite_ = (d_915_valueOrError5_).Extract()
                                d_917_valueOrError6_ = default__.GetReproducedEncryptionContext(d_905_obj_)
                                if (d_917_valueOrError6_).IsFailure():
                                    return (d_917_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_918_reproducedEncryptionContext_ = (d_917_valueOrError6_).Extract()
                                    d_919_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_916_algorithmSuite_)
                                    d_920_valueOrError7_ = default__.GetKeyDescription(keys, _dafny.Seq("keyDescription"), d_905_obj_)
                                    if (d_920_valueOrError7_).IsFailure():
                                        return (d_920_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_921_keyDescription_ = (d_920_valueOrError7_).Extract()
                                        d_922_valueOrError8_ = default__.GetEncryptedDataKeys(d_905_obj_)
                                        if (d_922_valueOrError8_).IsFailure():
                                            return (d_922_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_923_encryptedDataKeys_ = (d_922_valueOrError8_).Extract()
                                            source32_ = d_908_typ_
                                            unmatched32 = True
                                            if unmatched32:
                                                if (source32_) == (_dafny.Seq("positive-keyring")):
                                                    unmatched32 = False
                                                    d_924_valueOrError9_ = default__.GetExpectedResult(d_905_obj_)
                                                    if (d_924_valueOrError9_).IsFailure():
                                                        return (d_924_valueOrError9_).PropagateFailure()
                                                    elif True:
                                                        d_925_expectedResult_ = (d_924_valueOrError9_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.DecryptTestVector_PositiveDecryptKeyringTest(pat_let_tv87_, d_916_algorithmSuite_, d_919_commitmentPolicy_, d_923_encryptedDataKeys_, d_914_encryptionContext_, d_921_keyDescription_, d_925_expectedResult_, d_910_description_, d_918_reproducedEncryptionContext_))
                                            if unmatched32:
                                                if (source32_) == (_dafny.Seq("negative-keyring")):
                                                    unmatched32 = False
                                                    d_926_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_905_obj_)
                                                    if (d_926_valueOrError10_).IsFailure():
                                                        return (d_926_valueOrError10_).PropagateFailure()
                                                    elif True:
                                                        d_927_errorDescription_ = (d_926_valueOrError10_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.DecryptTestVector_NegativeDecryptKeyringTest(pat_let_tv88_, d_916_algorithmSuite_, d_919_commitmentPolicy_, d_923_encryptedDataKeys_, d_914_encryptionContext_, d_927_errorDescription_, d_921_keyDescription_, d_918_reproducedEncryptionContext_, d_910_description_))
                                            if unmatched32:
                                                unmatched32 = False
                                                return Wrappers.Result_Failure((_dafny.Seq("Unsupported DecryptTestVector type:")) + (d_908_typ_))
                                            raise Exception("unexpected control point")

