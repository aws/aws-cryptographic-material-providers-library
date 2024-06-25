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

# Module: WriteJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextKeysToJson(keys):
        if (keys).is_Some:
            def lambda89_(d_671_bytes_):
                def iife83_(_pat_let16_0):
                    def iife84_(d_672_valueOrError1_):
                        def iife85_(_pat_let17_0):
                            def iife86_(d_673_key_):
                                return Wrappers.Result_Success(JSON_Values.JSON_String(d_673_key_))
                            return iife86_(_pat_let17_0)
                        return ((d_672_valueOrError1_).PropagateFailure() if (d_672_valueOrError1_).IsFailure() else iife85_((d_672_valueOrError1_).Extract()))
                    return iife84_(_pat_let16_0)
                return iife83_(UTF8.default__.Decode(d_671_bytes_))

            d_670_valueOrError0_ = Seq.default__.MapWithResult(lambda89_, (keys).value)
            if (d_670_valueOrError0_).IsFailure():
                return (d_670_valueOrError0_).PropagateFailure()
            elif True:
                d_674_tmp_ = (d_670_valueOrError0_).Extract()
                return Wrappers.Result_Success(_dafny.Seq([(_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(d_674_tmp_))]))
        elif True:
            return Wrappers.Result_Success(_dafny.Seq([]))

    @staticmethod
    def EncryptionContextToJson(key, m):
        d_675_keys_ = SortedSets.default__.SetToSequence((m).keys)
        def lambda90_(d_677_m_):
            def lambda91_(d_678_k_):
                def iife87_(_pat_let18_0):
                    def iife88_(d_679_valueOrError1_):
                        def iife89_(_pat_let19_0):
                            def iife90_(d_680_key_):
                                def iife91_(_pat_let20_0):
                                    def iife92_(d_681_valueOrError2_):
                                        def iife93_(_pat_let21_0):
                                            def iife94_(d_682_value_):
                                                return Wrappers.Result_Success((d_680_key_, JSON_Values.JSON_String(d_682_value_)))
                                            return iife94_(_pat_let21_0)
                                        return ((d_681_valueOrError2_).PropagateFailure() if (d_681_valueOrError2_).IsFailure() else iife93_((d_681_valueOrError2_).Extract()))
                                    return iife92_(_pat_let20_0)
                                return iife91_(UTF8.default__.Decode((d_677_m_)[d_678_k_]))
                            return iife90_(_pat_let19_0)
                        return ((d_679_valueOrError1_).PropagateFailure() if (d_679_valueOrError1_).IsFailure() else iife89_((d_679_valueOrError1_).Extract()))
                    return iife88_(_pat_let18_0)
                return iife87_(UTF8.default__.Decode(d_678_k_))

            return lambda91_

        d_676_valueOrError0_ = Seq.default__.MapWithResult(lambda90_(m), d_675_keys_)
        if (d_676_valueOrError0_).IsFailure():
            return (d_676_valueOrError0_).PropagateFailure()
        elif True:
            d_683_pairsBytes_ = (d_676_valueOrError0_).Extract()
            return Wrappers.Result_Success(_dafny.Seq([(key, JSON_Values.JSON_Object(d_683_pairsBytes_))]))

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
    def EncryptTestVectorToJson(test):
        pat_let_tv66_ = test
        pat_let_tv67_ = test
        pat_let_tv68_ = test
        pat_let_tv69_ = test
        pat_let_tv70_ = test
        pat_let_tv71_ = test
        pat_let_tv72_ = test
        d_684_id_ = AllAlgorithmSuites.default__.ToHex((test).algorithmSuite)
        d_685_description_ = (((test).name) + (_dafny.Seq(" "))) + (d_684_id_)
        d_686_valueOrError0_ = default__.EncryptionContextToJson(_dafny.Seq("encryptionContext"), (test).encryptionContext)
        if (d_686_valueOrError0_).IsFailure():
            return (d_686_valueOrError0_).PropagateFailure()
        elif True:
            d_687_encryptionContext_ = (d_686_valueOrError0_).Extract()
            d_688_maxPlaintextL_ = (_dafny.Seq([(_dafny.Seq("maxPlaintextLength"), JSON_Values.JSON_Number(JSON_Values.default__.Int(((test).maxPlaintextLength).value)))]) if ((test).maxPlaintextLength).is_Some else _dafny.Seq([]))
            d_689_valueOrError1_ = default__.EncryptionContextKeysToJson((test).requiredEncryptionContextKeys)
            if (d_689_valueOrError1_).IsFailure():
                return (d_689_valueOrError1_).PropagateFailure()
            elif True:
                d_690_requiredEncryptionContextKeys_ = (d_689_valueOrError1_).Extract()
                d_691_valueOrError2_ = (default__.EncryptionContextToJson(_dafny.Seq("reproducedEncryptionContext"), ((test).reproducedEncryptionContext).value) if (not((test).is_NegativeEncryptKeyringVector)) and (((test).reproducedEncryptionContext).is_Some) else Wrappers.Result_Success(_dafny.Seq([])))
                if (d_691_valueOrError2_).IsFailure():
                    return (d_691_valueOrError2_).PropagateFailure()
                elif True:
                    d_692_reproducedEc_ = (d_691_valueOrError2_).Extract()
                    d_693_optionalValues_ = (((d_692_reproducedEc_) + (d_688_maxPlaintextL_)) + (d_690_requiredEncryptionContextKeys_)) + (d_687_encryptionContext_)
                    source21_ = test
                    unmatched21 = True
                    if unmatched21:
                        if source21_.is_PositiveEncryptKeyringVector:
                            d_694___v0_ = source21_.name
                            d_695___v1_ = source21_.description
                            d_696___v2_ = source21_.encryptionContext
                            d_697___v3_ = source21_.commitmentPolicy
                            d_698___v4_ = source21_.algorithmSuite
                            d_699___v5_ = source21_.maxPlaintextLength
                            d_700___v6_ = source21_.requiredEncryptionContextKeys
                            d_701___v7_ = source21_.encryptDescription
                            d_702___v8_ = source21_.decryptDescription
                            d_703___v9_ = source21_.reproducedEncryptionContext
                            unmatched21 = False
                            d_704_valueOrError3_ = KeyDescription.default__.ToJson((pat_let_tv66_).encryptDescription, 3)
                            if (d_704_valueOrError3_).IsFailure():
                                return (d_704_valueOrError3_).PropagateFailure()
                            elif True:
                                d_705_encrypt_ = (d_704_valueOrError3_).Extract()
                                d_706_valueOrError4_ = KeyDescription.default__.ToJson((pat_let_tv67_).decryptDescription, 3)
                                if (d_706_valueOrError4_).IsFailure():
                                    return (d_706_valueOrError4_).PropagateFailure()
                                elif True:
                                    d_707_decrypt_ = (d_706_valueOrError4_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_685_description_)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_684_id_)), (_dafny.Seq("encryptKeyDescription"), d_705_encrypt_), (_dafny.Seq("decryptKeyDescription"), d_707_decrypt_)])) + (d_693_optionalValues_)))
                    if unmatched21:
                        if source21_.is_PositiveEncryptNegativeDecryptKeyringVector:
                            d_708___v10_ = source21_.name
                            d_709___v11_ = source21_.description
                            d_710___v12_ = source21_.encryptionContext
                            d_711___v13_ = source21_.commitmentPolicy
                            d_712___v14_ = source21_.algorithmSuite
                            d_713___v15_ = source21_.maxPlaintextLength
                            d_714___v16_ = source21_.requiredEncryptionContextKeys
                            d_715___v17_ = source21_.decryptErrorDescription
                            d_716___v18_ = source21_.encryptDescription
                            d_717___v19_ = source21_.decryptDescription
                            d_718___v20_ = source21_.reproducedEncryptionContext
                            unmatched21 = False
                            d_719_valueOrError5_ = KeyDescription.default__.ToJson((pat_let_tv68_).encryptDescription, 3)
                            if (d_719_valueOrError5_).IsFailure():
                                return (d_719_valueOrError5_).PropagateFailure()
                            elif True:
                                d_720_encrypt_ = (d_719_valueOrError5_).Extract()
                                d_721_valueOrError6_ = KeyDescription.default__.ToJson((pat_let_tv69_).decryptDescription, 3)
                                if (d_721_valueOrError6_).IsFailure():
                                    return (d_721_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_722_decrypt_ = (d_721_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-decrypt-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_685_description_)), (_dafny.Seq("decryptErrorDescription"), JSON_Values.JSON_String((pat_let_tv70_).decryptErrorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_684_id_)), (_dafny.Seq("encryptKeyDescription"), d_720_encrypt_), (_dafny.Seq("decryptKeyDescription"), d_722_decrypt_)])) + (d_693_optionalValues_)))
                    if unmatched21:
                        d_723___v21_ = source21_.name
                        d_724___v22_ = source21_.description
                        d_725___v23_ = source21_.encryptionContext
                        d_726___v24_ = source21_.commitmentPolicy
                        d_727___v25_ = source21_.algorithmSuite
                        d_728___v26_ = source21_.maxPlaintextLength
                        d_729___v27_ = source21_.requiredEncryptionContextKeys
                        d_730___v28_ = source21_.errorDescription
                        d_731___v29_ = source21_.keyDescription
                        unmatched21 = False
                        d_732_valueOrError7_ = KeyDescription.default__.ToJson((pat_let_tv71_).keyDescription, 3)
                        if (d_732_valueOrError7_).IsFailure():
                            return (d_732_valueOrError7_).PropagateFailure()
                        elif True:
                            d_733_keyDescription_ = (d_732_valueOrError7_).Extract()
                            return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-encrypt-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_685_description_)), (_dafny.Seq("errorDescription"), JSON_Values.JSON_String((pat_let_tv72_).errorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_684_id_)), (_dafny.Seq("keyDescription"), d_733_keyDescription_)])) + (d_693_optionalValues_)))
                    raise Exception("unexpected control point")

    @staticmethod
    def OptionalBytes(key, secret):
        if (secret).is_Some:
            d_734_base64_ = Base64.default__.Encode((secret).value)
            return _dafny.Seq([(key, JSON_Values.JSON_String(d_734_base64_))])
        elif True:
            return _dafny.Seq([])

    @staticmethod
    def EncryptedDataKey(encryptedDataKey):
        d_735_valueOrError0_ = UTF8.default__.Decode((encryptedDataKey).keyProviderId)
        if (d_735_valueOrError0_).IsFailure():
            return (d_735_valueOrError0_).PropagateFailure()
        elif True:
            d_736_keyProviderId_ = (d_735_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("keyProviderId"), JSON_Values.JSON_String(d_736_keyProviderId_)), (_dafny.Seq("keyProviderInfo"), JSON_Values.JSON_String(Base64.default__.Encode((encryptedDataKey).keyProviderInfo))), (_dafny.Seq("ciphertext"), JSON_Values.JSON_String(Base64.default__.Encode((encryptedDataKey).ciphertext)))])))

    @staticmethod
    def DecryptTestVectorToJson(test):
        pat_let_tv73_ = test
        pat_let_tv74_ = test
        pat_let_tv75_ = test
        pat_let_tv76_ = test
        d_737_id_ = AllAlgorithmSuites.default__.ToHex((test).algorithmSuite)
        d_738_description_ = (((test).name) + (_dafny.Seq(" "))) + (d_737_id_)
        d_739_valueOrError0_ = default__.EncryptionContextToJson(_dafny.Seq("encryptionContext"), (test).encryptionContext)
        if (d_739_valueOrError0_).IsFailure():
            return (d_739_valueOrError0_).PropagateFailure()
        elif True:
            d_740_encryptionContext_ = (d_739_valueOrError0_).Extract()
            d_741_valueOrError1_ = (default__.EncryptionContextToJson(_dafny.Seq("reproducedEncryptionContext"), ((test).reproducedEncryptionContext).value) if ((test).reproducedEncryptionContext).is_Some else Wrappers.Result_Success(_dafny.Seq([])))
            if (d_741_valueOrError1_).IsFailure():
                return (d_741_valueOrError1_).PropagateFailure()
            elif True:
                d_742_reproducedEc_ = (d_741_valueOrError1_).Extract()
                d_743_valueOrError2_ = KeyDescription.default__.ToJson((test).keyDescription, 3)
                if (d_743_valueOrError2_).IsFailure():
                    return (d_743_valueOrError2_).PropagateFailure()
                elif True:
                    d_744_keyDescription_ = (d_743_valueOrError2_).Extract()
                    def lambda92_(d_746_edk_):
                        return default__.EncryptedDataKey(d_746_edk_)

                    d_745_valueOrError3_ = Seq.default__.MapWithResult(lambda92_, (test).encryptedDataKeys)
                    if (d_745_valueOrError3_).IsFailure():
                        return (d_745_valueOrError3_).PropagateFailure()
                    elif True:
                        d_747_encryptedDataKeys_ = (d_745_valueOrError3_).Extract()
                        source22_ = test
                        unmatched22 = True
                        if unmatched22:
                            if source22_.is_PositiveDecryptKeyringTest:
                                d_748___v30_ = source22_.name
                                d_749___v31_ = source22_.algorithmSuite
                                d_750___v32_ = source22_.commitmentPolicy
                                d_751___v33_ = source22_.encryptedDataKeys
                                d_752___v34_ = source22_.encryptionContext
                                d_753___v35_ = source22_.keyDescription
                                d_754___v36_ = source22_.expectedResult
                                d_755___v37_ = source22_.description
                                d_756___v38_ = source22_.reproducedEncryptionContext
                                unmatched22 = False
                                d_757_plaintextDataKey_ = default__.OptionalBytes(_dafny.Seq("plaintextDataKey"), ((pat_let_tv73_).expectedResult).plaintextDataKey)
                                d_758_symmetricSigningKey_ = default__.OptionalBytes(_dafny.Seq("symmetricSigningKey"), ((pat_let_tv74_).expectedResult).symmetricSigningKey)
                                d_759_valueOrError4_ = default__.EncryptionContextKeysToJson(Wrappers.Option_Some(((pat_let_tv75_).expectedResult).requiredEncryptionContextKeys))
                                if (d_759_valueOrError4_).IsFailure():
                                    return (d_759_valueOrError4_).PropagateFailure()
                                elif True:
                                    d_760_requiredEncryptionContextKeys_ = (d_759_valueOrError4_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object(((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_738_description_)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_737_id_)), (_dafny.Seq("keyDescription"), d_744_keyDescription_), (_dafny.Seq("encryptedDataKeys"), JSON_Values.JSON_Array(d_747_encryptedDataKeys_)), (_dafny.Seq("result"), JSON_Values.JSON_Object(((d_757_plaintextDataKey_) + (d_758_symmetricSigningKey_)) + (d_760_requiredEncryptionContextKeys_)))])) + (d_742_reproducedEc_)) + (d_740_encryptionContext_)))
                        if unmatched22:
                            d_761___v39_ = source22_.name
                            d_762___v40_ = source22_.algorithmSuite
                            d_763___v41_ = source22_.commitmentPolicy
                            d_764___v42_ = source22_.encryptedDataKeys
                            d_765___v43_ = source22_.encryptionContext
                            d_766___v44_ = source22_.errorDescription
                            d_767___v45_ = source22_.keyDescription
                            d_768___v46_ = source22_.reproducedEncryptionContext
                            d_769___v47_ = source22_.description
                            unmatched22 = False
                            return Wrappers.Result_Success(JSON_Values.JSON_Object(((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_738_description_)), (_dafny.Seq("errorDescription"), JSON_Values.JSON_String((pat_let_tv76_).errorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_737_id_)), (_dafny.Seq("keyDescription"), d_744_keyDescription_), (_dafny.Seq("encryptedDataKeys"), JSON_Values.JSON_Array(d_747_encryptedDataKeys_))])) + (d_742_reproducedEc_)) + (d_740_encryptionContext_)))
                        raise Exception("unexpected control point")

