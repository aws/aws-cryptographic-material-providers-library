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
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import CmmFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import AllHierarchy
import AllKms
import AllKmsMrkAware
import AllKmsMrkAwareDiscovery
import AllKmsRsa
import AllRawAES
import AllRawRSA
import AllDefaultCmm
import AllRequiredEncryptionContextCmm
import AllMulti

# Module: WriteJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextKeysToJson(keys):
        if (keys).is_Some:
            def lambda96_(d_780_bytes_):
                def iife83_(_pat_let16_0):
                    def iife84_(d_781_valueOrError1_):
                        def iife85_(_pat_let17_0):
                            def iife86_(d_782_key_):
                                return Wrappers.Result_Success(JSON_Values.JSON_String(d_782_key_))
                            return iife86_(_pat_let17_0)
                        return ((d_781_valueOrError1_).PropagateFailure() if (d_781_valueOrError1_).IsFailure() else iife85_((d_781_valueOrError1_).Extract()))
                    return iife84_(_pat_let16_0)
                return iife83_(UTF8.default__.Decode(d_780_bytes_))

            d_779_valueOrError0_ = Seq.default__.MapWithResult(lambda96_, (keys).value)
            if (d_779_valueOrError0_).IsFailure():
                return (d_779_valueOrError0_).PropagateFailure()
            elif True:
                d_783_tmp_ = (d_779_valueOrError0_).Extract()
                return Wrappers.Result_Success(_dafny.Seq([(_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(d_783_tmp_))]))
        elif True:
            return Wrappers.Result_Success(_dafny.Seq([]))

    @staticmethod
    def EncryptionContextToJson(key, m):
        d_784_keys_ = SortedSets.default__.SetToSequence((m).keys)
        def lambda97_(d_786_m_):
            def lambda98_(d_787_k_):
                def iife87_(_pat_let18_0):
                    def iife88_(d_788_valueOrError1_):
                        def iife89_(_pat_let19_0):
                            def iife90_(d_789_key_):
                                def iife91_(_pat_let20_0):
                                    def iife92_(d_790_valueOrError2_):
                                        def iife93_(_pat_let21_0):
                                            def iife94_(d_791_value_):
                                                return Wrappers.Result_Success((d_789_key_, JSON_Values.JSON_String(d_791_value_)))
                                            return iife94_(_pat_let21_0)
                                        return ((d_790_valueOrError2_).PropagateFailure() if (d_790_valueOrError2_).IsFailure() else iife93_((d_790_valueOrError2_).Extract()))
                                    return iife92_(_pat_let20_0)
                                return iife91_(UTF8.default__.Decode((d_786_m_)[d_787_k_]))
                            return iife90_(_pat_let19_0)
                        return ((d_788_valueOrError1_).PropagateFailure() if (d_788_valueOrError1_).IsFailure() else iife89_((d_788_valueOrError1_).Extract()))
                    return iife88_(_pat_let18_0)
                return iife87_(UTF8.default__.Decode(d_787_k_))

            return lambda98_

        d_785_valueOrError0_ = Seq.default__.MapWithResult(lambda97_(m), d_784_keys_)
        if (d_785_valueOrError0_).IsFailure():
            return (d_785_valueOrError0_).PropagateFailure()
        elif True:
            d_792_pairsBytes_ = (d_785_valueOrError0_).Extract()
            return Wrappers.Result_Success(_dafny.Seq([(key, JSON_Values.JSON_Object(d_792_pairsBytes_))]))

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
        d_793_id_ = AllAlgorithmSuites.default__.ToHex((test).algorithmSuite)
        d_794_description_ = (((test).name) + (_dafny.Seq(" "))) + (d_793_id_)
        d_795_valueOrError0_ = default__.EncryptionContextToJson(_dafny.Seq("encryptionContext"), (test).encryptionContext)
        if (d_795_valueOrError0_).IsFailure():
            return (d_795_valueOrError0_).PropagateFailure()
        elif True:
            d_796_encryptionContext_ = (d_795_valueOrError0_).Extract()
            d_797_maxPlaintextL_ = (_dafny.Seq([(_dafny.Seq("maxPlaintextLength"), JSON_Values.JSON_Number(JSON_Values.default__.Int(((test).maxPlaintextLength).value)))]) if ((test).maxPlaintextLength).is_Some else _dafny.Seq([]))
            d_798_valueOrError1_ = default__.EncryptionContextKeysToJson((test).requiredEncryptionContextKeys)
            if (d_798_valueOrError1_).IsFailure():
                return (d_798_valueOrError1_).PropagateFailure()
            elif True:
                d_799_requiredEncryptionContextKeys_ = (d_798_valueOrError1_).Extract()
                d_800_valueOrError2_ = (default__.EncryptionContextToJson(_dafny.Seq("reproducedEncryptionContext"), ((test).reproducedEncryptionContext).value) if (not((test).is_NegativeEncryptKeyringVector)) and (((test).reproducedEncryptionContext).is_Some) else Wrappers.Result_Success(_dafny.Seq([])))
                if (d_800_valueOrError2_).IsFailure():
                    return (d_800_valueOrError2_).PropagateFailure()
                elif True:
                    d_801_reproducedEc_ = (d_800_valueOrError2_).Extract()
                    d_802_optionalValues_ = (((d_801_reproducedEc_) + (d_797_maxPlaintextL_)) + (d_799_requiredEncryptionContextKeys_)) + (d_796_encryptionContext_)
                    source22_ = test
                    if source22_.is_PositiveEncryptKeyringVector:
                        d_803___mcc_h0_ = source22_.name
                        d_804___mcc_h1_ = source22_.description
                        d_805___mcc_h2_ = source22_.encryptionContext
                        d_806___mcc_h3_ = source22_.commitmentPolicy
                        d_807___mcc_h4_ = source22_.algorithmSuite
                        d_808___mcc_h5_ = source22_.maxPlaintextLength
                        d_809___mcc_h6_ = source22_.requiredEncryptionContextKeys
                        d_810___mcc_h7_ = source22_.encryptDescription
                        d_811___mcc_h8_ = source22_.decryptDescription
                        d_812___mcc_h9_ = source22_.reproducedEncryptionContext
                        d_813_valueOrError3_ = KeyDescription.default__.ToJson((test).encryptDescription, 3)
                        if (d_813_valueOrError3_).IsFailure():
                            return (d_813_valueOrError3_).PropagateFailure()
                        elif True:
                            d_814_encrypt_ = (d_813_valueOrError3_).Extract()
                            d_815_valueOrError4_ = KeyDescription.default__.ToJson((test).decryptDescription, 3)
                            if (d_815_valueOrError4_).IsFailure():
                                return (d_815_valueOrError4_).PropagateFailure()
                            elif True:
                                d_816_decrypt_ = (d_815_valueOrError4_).Extract()
                                return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_794_description_)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_793_id_)), (_dafny.Seq("encryptKeyDescription"), d_814_encrypt_), (_dafny.Seq("decryptKeyDescription"), d_816_decrypt_)])) + (d_802_optionalValues_)))
                    elif source22_.is_PositiveEncryptNegativeDecryptKeyringVector:
                        d_817___mcc_h10_ = source22_.name
                        d_818___mcc_h11_ = source22_.description
                        d_819___mcc_h12_ = source22_.encryptionContext
                        d_820___mcc_h13_ = source22_.commitmentPolicy
                        d_821___mcc_h14_ = source22_.algorithmSuite
                        d_822___mcc_h15_ = source22_.maxPlaintextLength
                        d_823___mcc_h16_ = source22_.requiredEncryptionContextKeys
                        d_824___mcc_h17_ = source22_.decryptErrorDescription
                        d_825___mcc_h18_ = source22_.encryptDescription
                        d_826___mcc_h19_ = source22_.decryptDescription
                        d_827___mcc_h20_ = source22_.reproducedEncryptionContext
                        d_828_valueOrError5_ = KeyDescription.default__.ToJson((test).encryptDescription, 3)
                        if (d_828_valueOrError5_).IsFailure():
                            return (d_828_valueOrError5_).PropagateFailure()
                        elif True:
                            d_829_encrypt_ = (d_828_valueOrError5_).Extract()
                            d_830_valueOrError6_ = KeyDescription.default__.ToJson((test).decryptDescription, 3)
                            if (d_830_valueOrError6_).IsFailure():
                                return (d_830_valueOrError6_).PropagateFailure()
                            elif True:
                                d_831_decrypt_ = (d_830_valueOrError6_).Extract()
                                return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-decrypt-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_794_description_)), (_dafny.Seq("decryptErrorDescription"), JSON_Values.JSON_String((test).decryptErrorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_793_id_)), (_dafny.Seq("encryptKeyDescription"), d_829_encrypt_), (_dafny.Seq("decryptKeyDescription"), d_831_decrypt_)])) + (d_802_optionalValues_)))
                    elif True:
                        d_832___mcc_h21_ = source22_.name
                        d_833___mcc_h22_ = source22_.description
                        d_834___mcc_h23_ = source22_.encryptionContext
                        d_835___mcc_h24_ = source22_.commitmentPolicy
                        d_836___mcc_h25_ = source22_.algorithmSuite
                        d_837___mcc_h26_ = source22_.maxPlaintextLength
                        d_838___mcc_h27_ = source22_.requiredEncryptionContextKeys
                        d_839___mcc_h28_ = source22_.errorDescription
                        d_840___mcc_h29_ = source22_.keyDescription
                        d_841_valueOrError7_ = KeyDescription.default__.ToJson((test).keyDescription, 3)
                        if (d_841_valueOrError7_).IsFailure():
                            return (d_841_valueOrError7_).PropagateFailure()
                        elif True:
                            d_842_keyDescription_ = (d_841_valueOrError7_).Extract()
                            return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-encrypt-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_794_description_)), (_dafny.Seq("errorDescription"), JSON_Values.JSON_String((test).errorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_793_id_)), (_dafny.Seq("keyDescription"), d_842_keyDescription_)])) + (d_802_optionalValues_)))

    @staticmethod
    def OptionalBytes(key, secret):
        if (secret).is_Some:
            d_843_base64_ = Base64.default__.Encode((secret).value)
            return _dafny.Seq([(key, JSON_Values.JSON_String(d_843_base64_))])
        elif True:
            return _dafny.Seq([])

    @staticmethod
    def EncryptedDataKey(encryptedDataKey):
        d_844_valueOrError0_ = UTF8.default__.Decode((encryptedDataKey).keyProviderId)
        if (d_844_valueOrError0_).IsFailure():
            return (d_844_valueOrError0_).PropagateFailure()
        elif True:
            d_845_keyProviderId_ = (d_844_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("keyProviderId"), JSON_Values.JSON_String(d_845_keyProviderId_)), (_dafny.Seq("keyProviderInfo"), JSON_Values.JSON_String(Base64.default__.Encode((encryptedDataKey).keyProviderInfo))), (_dafny.Seq("ciphertext"), JSON_Values.JSON_String(Base64.default__.Encode((encryptedDataKey).ciphertext)))])))

    @staticmethod
    def DecryptTestVectorToJson(test):
        d_846_id_ = AllAlgorithmSuites.default__.ToHex((test).algorithmSuite)
        d_847_description_ = (((test).name) + (_dafny.Seq(" "))) + (d_846_id_)
        d_848_valueOrError0_ = default__.EncryptionContextToJson(_dafny.Seq("encryptionContext"), (test).encryptionContext)
        if (d_848_valueOrError0_).IsFailure():
            return (d_848_valueOrError0_).PropagateFailure()
        elif True:
            d_849_encryptionContext_ = (d_848_valueOrError0_).Extract()
            d_850_valueOrError1_ = (default__.EncryptionContextToJson(_dafny.Seq("reproducedEncryptionContext"), ((test).reproducedEncryptionContext).value) if ((test).reproducedEncryptionContext).is_Some else Wrappers.Result_Success(_dafny.Seq([])))
            if (d_850_valueOrError1_).IsFailure():
                return (d_850_valueOrError1_).PropagateFailure()
            elif True:
                d_851_reproducedEc_ = (d_850_valueOrError1_).Extract()
                d_852_valueOrError2_ = KeyDescription.default__.ToJson((test).keyDescription, 3)
                if (d_852_valueOrError2_).IsFailure():
                    return (d_852_valueOrError2_).PropagateFailure()
                elif True:
                    d_853_keyDescription_ = (d_852_valueOrError2_).Extract()
                    def lambda99_(d_855_edk_):
                        return default__.EncryptedDataKey(d_855_edk_)

                    d_854_valueOrError3_ = Seq.default__.MapWithResult(lambda99_, (test).encryptedDataKeys)
                    if (d_854_valueOrError3_).IsFailure():
                        return (d_854_valueOrError3_).PropagateFailure()
                    elif True:
                        d_856_encryptedDataKeys_ = (d_854_valueOrError3_).Extract()
                        source23_ = test
                        if source23_.is_PositiveDecryptKeyringTest:
                            d_857___mcc_h0_ = source23_.name
                            d_858___mcc_h1_ = source23_.algorithmSuite
                            d_859___mcc_h2_ = source23_.commitmentPolicy
                            d_860___mcc_h3_ = source23_.encryptedDataKeys
                            d_861___mcc_h4_ = source23_.encryptionContext
                            d_862___mcc_h5_ = source23_.keyDescription
                            d_863___mcc_h6_ = source23_.expectedResult
                            d_864___mcc_h7_ = source23_.description
                            d_865___mcc_h8_ = source23_.reproducedEncryptionContext
                            d_866_plaintextDataKey_ = default__.OptionalBytes(_dafny.Seq("plaintextDataKey"), ((test).expectedResult).plaintextDataKey)
                            d_867_symmetricSigningKey_ = default__.OptionalBytes(_dafny.Seq("symmetricSigningKey"), ((test).expectedResult).symmetricSigningKey)
                            d_868_valueOrError4_ = default__.EncryptionContextKeysToJson(Wrappers.Option_Some(((test).expectedResult).requiredEncryptionContextKeys))
                            if (d_868_valueOrError4_).IsFailure():
                                return (d_868_valueOrError4_).PropagateFailure()
                            elif True:
                                d_869_requiredEncryptionContextKeys_ = (d_868_valueOrError4_).Extract()
                                return Wrappers.Result_Success(JSON_Values.JSON_Object(((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_847_description_)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_846_id_)), (_dafny.Seq("keyDescription"), d_853_keyDescription_), (_dafny.Seq("encryptedDataKeys"), JSON_Values.JSON_Array(d_856_encryptedDataKeys_)), (_dafny.Seq("result"), JSON_Values.JSON_Object(((d_866_plaintextDataKey_) + (d_867_symmetricSigningKey_)) + (d_869_requiredEncryptionContextKeys_)))])) + (d_851_reproducedEc_)) + (d_849_encryptionContext_)))
                        elif True:
                            d_870___mcc_h9_ = source23_.name
                            d_871___mcc_h10_ = source23_.algorithmSuite
                            d_872___mcc_h11_ = source23_.commitmentPolicy
                            d_873___mcc_h12_ = source23_.encryptedDataKeys
                            d_874___mcc_h13_ = source23_.encryptionContext
                            d_875___mcc_h14_ = source23_.errorDescription
                            d_876___mcc_h15_ = source23_.keyDescription
                            d_877___mcc_h16_ = source23_.reproducedEncryptionContext
                            d_878___mcc_h17_ = source23_.description
                            return Wrappers.Result_Success(JSON_Values.JSON_Object(((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("negative-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String(d_847_description_)), (_dafny.Seq("errorDescription"), JSON_Values.JSON_String((test).errorDescription)), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_846_id_)), (_dafny.Seq("keyDescription"), d_853_keyDescription_), (_dafny.Seq("encryptedDataKeys"), JSON_Values.JSON_Array(d_856_encryptedDataKeys_))])) + (d_851_reproducedEc_)) + (d_849_encryptionContext_)))

