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

# Module: WriteJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextKeysToJson(keys):
        if (keys).is_Some:
            def lambda104_(d_724_bytes_):
                def iife94_(_pat_let16_0):
                    def iife95_(d_725_valueOrError1_):
                        def iife96_(_pat_let17_0):
                            def iife97_(d_726_key_):
                                return Wrappers.Result_Success(JSON_Values.JSON_String(d_726_key_))
                            return iife97_(_pat_let17_0)
                        return ((d_725_valueOrError1_).PropagateFailure() if (d_725_valueOrError1_).IsFailure() else iife96_((d_725_valueOrError1_).Extract()))
                    return iife95_(_pat_let16_0)
                return iife94_(UTF8.default__.Decode(d_724_bytes_))

            d_723_valueOrError0_ = Seq.default__.MapWithResult(lambda104_, (keys).value)
            if (d_723_valueOrError0_).IsFailure():
                return (d_723_valueOrError0_).PropagateFailure()
            elif True:
                d_727_tmp_ = (d_723_valueOrError0_).Extract()
                return Wrappers.Result_Success(_dafny.Seq([(_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(d_727_tmp_))]))
        elif True:
            return Wrappers.Result_Success(_dafny.Seq([]))

    @staticmethod
    def EncryptionContextToJson(key, m):
        d_728_keys_ = SortedSets.default__.SetToSequence((m).keys)
        def lambda105_(d_730_m_):
            def lambda106_(d_731_k_):
                def iife98_(_pat_let18_0):
                    def iife99_(d_732_valueOrError1_):
                        def iife100_(_pat_let19_0):
                            def iife101_(d_733_key_):
                                def iife102_(_pat_let20_0):
                                    def iife103_(d_734_valueOrError2_):
                                        def iife104_(_pat_let21_0):
                                            def iife105_(d_735_value_):
                                                return Wrappers.Result_Success((d_733_key_, JSON_Values.JSON_String(d_735_value_)))
                                            return iife105_(_pat_let21_0)
                                        return ((d_734_valueOrError2_).PropagateFailure() if (d_734_valueOrError2_).IsFailure() else iife104_((d_734_valueOrError2_).Extract()))
                                    return iife103_(_pat_let20_0)
                                return iife102_(UTF8.default__.Decode((d_730_m_)[d_731_k_]))
                            return iife101_(_pat_let19_0)
                        return ((d_732_valueOrError1_).PropagateFailure() if (d_732_valueOrError1_).IsFailure() else iife100_((d_732_valueOrError1_).Extract()))
                    return iife99_(_pat_let18_0)
                return iife98_(UTF8.default__.Decode(d_731_k_))

            return lambda106_

        d_729_valueOrError0_ = Seq.default__.MapWithResult(lambda105_(m), d_728_keys_)
        if (d_729_valueOrError0_).IsFailure():
            return (d_729_valueOrError0_).PropagateFailure()
        elif True:
            d_736_pairsBytes_ = (d_729_valueOrError0_).Extract()
            return Wrappers.Result_Success(_dafny.Seq([(key, JSON_Values.JSON_Object(d_736_pairsBytes_))]))

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
        pat_let_tv68_ = test
        pat_let_tv69_ = test
        pat_let_tv70_ = test
        pat_let_tv71_ = test
        pat_let_tv72_ = test
        pat_let_tv73_ = test
        pat_let_tv74_ = test
        d_737_id_ = AllAlgorithmSuites.default__.ToHex((test).algorithmSuite)
        d_738_description_ = (((test).name) + (_dafny.Seq(" "))) + (d_737_id_)
        d_739_valueOrError0_ = default__.EncryptionContextToJson(_dafny.Seq("encryptionContext"), (test).encryptionContext)
        if (d_739_valueOrError0_).IsFailure():
            return (d_739_valueOrError0_).PropagateFailure()
        elif True:
            d_740_encryptionContext_ = (d_739_valueOrError0_).Extract()
            d_741_maxPlaintextL_ = (_dafny.Seq([(_dafny.Seq("maxPlaintextLength"), JSON_Values.JSON_Number(JSON_Values.default__.Int(((test).maxPlaintextLength).value)))]) if ((test).maxPlaintextLength).is_Some else _dafny.Seq([]))
            d_742_valueOrError1_ = default__.EncryptionContextKeysToJson((test).requiredEncryptionContextKeys)
            if (d_742_valueOrError1_).IsFailure():
                return (d_742_valueOrError1_).PropagateFailure()
            elif True:
                d_743_requiredEncryptionContextKeys_ = (d_742_valueOrError1_).Extract()
                d_744_valueOrError2_ = (default__.EncryptionContextToJson(_dafny.Seq("reproducedEncryptionContext"), ((test).reproducedEncryptionContext).value) if (not((test).is_NegativeEncryptKeyringVector)) and (((test).reproducedEncryptionContext).is_Some) else Wrappers.Result_Success(_dafny.Seq([])))
                if (d_744_valueOrError2_).IsFailure():
                    return (d_744_valueOrError2_).PropagateFailure()
                elif True:
                    d_745_reproducedEc_ = (d_744_valueOrError2_).Extract()
                    d_746_optionalValues_ = (((d_745_reproducedEc_) + (d_741_maxPlaintextL_)) + (d_743_requiredEncryptionContextKeys_)) + (d_740_encryptionContext_)
                    source25_ = test
                    unmatched25 = True
                    if unmatched25:
                        if source25_.is_PositiveEncryptKeyringVector:
                            unmatched25 = False
                            d_747_valueOrError3_ = KeyDescription.default__.ToJson((pat_let_tv68_).encryptDescription, 3)
                            if (d_747_valueOrError3_).IsFailure():
                                return (d_747_valueOrError3_).PropagateFailure()
                            elif True:
                                d_748_encrypt_ = (d_747_valueOrError3_).Extract()
                                d_749_valueOrError4_ = KeyDescription.default__.ToJson((pat_let_tv69_).decryptDescription, 3)
                                if (d_749_valueOrError4_).IsFailure():
                                    return (d_749_valueOrError4_).PropagateFailure()
                                elif True:
                                    d_750_decrypt_ = (d_749_valueOrError4_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_738_description_)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_737_id_)), (_dafny.Seq("encryptKeyDescription"), d_748_encrypt_), (_dafny.Seq("decryptKeyDescription"), d_750_decrypt_)])) + (d_746_optionalValues_)))
                    if unmatched25:
                        if source25_.is_PositiveEncryptNegativeDecryptKeyringVector:
                            unmatched25 = False
                            d_751_valueOrError5_ = KeyDescription.default__.ToJson((pat_let_tv70_).encryptDescription, 3)
                            if (d_751_valueOrError5_).IsFailure():
                                return (d_751_valueOrError5_).PropagateFailure()
                            elif True:
                                d_752_encrypt_ = (d_751_valueOrError5_).Extract()
                                d_753_valueOrError6_ = KeyDescription.default__.ToJson((pat_let_tv71_).decryptDescription, 3)
                                if (d_753_valueOrError6_).IsFailure():
                                    return (d_753_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_754_decrypt_ = (d_753_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-decrypt-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_738_description_)), (_dafny.Seq("decryptErrorDescription"), JSON_Values.JSON_String((pat_let_tv72_).decryptErrorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_737_id_)), (_dafny.Seq("encryptKeyDescription"), d_752_encrypt_), (_dafny.Seq("decryptKeyDescription"), d_754_decrypt_)])) + (d_746_optionalValues_)))
                    if unmatched25:
                        unmatched25 = False
                        d_755_valueOrError7_ = KeyDescription.default__.ToJson((pat_let_tv73_).keyDescription, 3)
                        if (d_755_valueOrError7_).IsFailure():
                            return (d_755_valueOrError7_).PropagateFailure()
                        elif True:
                            d_756_keyDescription_ = (d_755_valueOrError7_).Extract()
                            return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-encrypt-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_738_description_)), (_dafny.Seq("errorDescription"), JSON_Values.JSON_String((pat_let_tv74_).errorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_737_id_)), (_dafny.Seq("keyDescription"), d_756_keyDescription_)])) + (d_746_optionalValues_)))
                    raise Exception("unexpected control point")

    @staticmethod
    def OptionalBytes(key, secret):
        if (secret).is_Some:
            d_757_base64_ = Base64.default__.Encode((secret).value)
            return _dafny.Seq([(key, JSON_Values.JSON_String(d_757_base64_))])
        elif True:
            return _dafny.Seq([])

    @staticmethod
    def EncryptedDataKey(encryptedDataKey):
        d_758_valueOrError0_ = UTF8.default__.Decode((encryptedDataKey).keyProviderId)
        if (d_758_valueOrError0_).IsFailure():
            return (d_758_valueOrError0_).PropagateFailure()
        elif True:
            d_759_keyProviderId_ = (d_758_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("keyProviderId"), JSON_Values.JSON_String(d_759_keyProviderId_)), (_dafny.Seq("keyProviderInfo"), JSON_Values.JSON_String(Base64.default__.Encode((encryptedDataKey).keyProviderInfo))), (_dafny.Seq("ciphertext"), JSON_Values.JSON_String(Base64.default__.Encode((encryptedDataKey).ciphertext)))])))

    @staticmethod
    def DecryptTestVectorToJson(test):
        pat_let_tv75_ = test
        pat_let_tv76_ = test
        pat_let_tv77_ = test
        pat_let_tv78_ = test
        d_760_id_ = AllAlgorithmSuites.default__.ToHex((test).algorithmSuite)
        d_761_description_ = (((test).name) + (_dafny.Seq(" "))) + (d_760_id_)
        d_762_valueOrError0_ = default__.EncryptionContextToJson(_dafny.Seq("encryptionContext"), (test).encryptionContext)
        if (d_762_valueOrError0_).IsFailure():
            return (d_762_valueOrError0_).PropagateFailure()
        elif True:
            d_763_encryptionContext_ = (d_762_valueOrError0_).Extract()
            d_764_valueOrError1_ = (default__.EncryptionContextToJson(_dafny.Seq("reproducedEncryptionContext"), ((test).reproducedEncryptionContext).value) if ((test).reproducedEncryptionContext).is_Some else Wrappers.Result_Success(_dafny.Seq([])))
            if (d_764_valueOrError1_).IsFailure():
                return (d_764_valueOrError1_).PropagateFailure()
            elif True:
                d_765_reproducedEc_ = (d_764_valueOrError1_).Extract()
                d_766_valueOrError2_ = KeyDescription.default__.ToJson((test).keyDescription, 3)
                if (d_766_valueOrError2_).IsFailure():
                    return (d_766_valueOrError2_).PropagateFailure()
                elif True:
                    d_767_keyDescription_ = (d_766_valueOrError2_).Extract()
                    def lambda107_(d_769_edk_):
                        return default__.EncryptedDataKey(d_769_edk_)

                    d_768_valueOrError3_ = Seq.default__.MapWithResult(lambda107_, (test).encryptedDataKeys)
                    if (d_768_valueOrError3_).IsFailure():
                        return (d_768_valueOrError3_).PropagateFailure()
                    elif True:
                        d_770_encryptedDataKeys_ = (d_768_valueOrError3_).Extract()
                        source26_ = test
                        unmatched26 = True
                        if unmatched26:
                            if source26_.is_PositiveDecryptKeyringTest:
                                unmatched26 = False
                                d_771_plaintextDataKey_ = default__.OptionalBytes(_dafny.Seq("plaintextDataKey"), ((pat_let_tv75_).expectedResult).plaintextDataKey)
                                d_772_symmetricSigningKey_ = default__.OptionalBytes(_dafny.Seq("symmetricSigningKey"), ((pat_let_tv76_).expectedResult).symmetricSigningKey)
                                d_773_valueOrError4_ = default__.EncryptionContextKeysToJson(Wrappers.Option_Some(((pat_let_tv77_).expectedResult).requiredEncryptionContextKeys))
                                if (d_773_valueOrError4_).IsFailure():
                                    return (d_773_valueOrError4_).PropagateFailure()
                                elif True:
                                    d_774_requiredEncryptionContextKeys_ = (d_773_valueOrError4_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object(((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_761_description_)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_760_id_)), (_dafny.Seq("keyDescription"), d_767_keyDescription_), (_dafny.Seq("encryptedDataKeys"), JSON_Values.JSON_Array(d_770_encryptedDataKeys_)), (_dafny.Seq("result"), JSON_Values.JSON_Object(((d_771_plaintextDataKey_) + (d_772_symmetricSigningKey_)) + (d_774_requiredEncryptionContextKeys_)))])) + (d_765_reproducedEc_)) + (d_763_encryptionContext_)))
                        if unmatched26:
                            unmatched26 = False
                            return Wrappers.Result_Success(JSON_Values.JSON_Object(((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_761_description_)), (_dafny.Seq("errorDescription"), JSON_Values.JSON_String((pat_let_tv78_).errorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_760_id_)), (_dafny.Seq("keyDescription"), d_767_keyDescription_), (_dafny.Seq("encryptedDataKeys"), JSON_Values.JSON_Array(d_770_encryptedDataKeys_))])) + (d_765_reproducedEc_)) + (d_763_encryptionContext_)))
                        raise Exception("unexpected control point")

