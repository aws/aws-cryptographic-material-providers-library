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

# Module: CompleteVectors

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteStuff(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_775_tests_: _dafny.Seq
        d_775_tests_ = SortedSets.default__.SetToSequence(default__.AllPositiveKeyringTests)
        d_776_testsJSON_: _dafny.Seq
        d_776_testsJSON_ = _dafny.Seq([])
        hi1_ = len(d_775_tests_)
        for d_777_i_ in range(0, hi1_):
            d_778_name_: _dafny.Seq
            d_779_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out50_: Wrappers.Result
            out50_ = UUID.default__.GenerateUUID()
            d_779_valueOrError0_ = out50_
            if (d_779_valueOrError0_).IsFailure():
                output = (d_779_valueOrError0_).PropagateFailure()
                return output
            d_778_name_ = (d_779_valueOrError0_).Extract()
            d_780_test_: JSON_Values.JSON
            d_781_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
            d_781_valueOrError1_ = WriteJsonManifests.default__.EncryptTestVectorToJson((d_775_tests_)[d_777_i_])
            if (d_781_valueOrError1_).IsFailure():
                output = (d_781_valueOrError1_).PropagateFailure()
                return output
            d_780_test_ = (d_781_valueOrError1_).Extract()
            d_776_testsJSON_ = (d_776_testsJSON_) + (_dafny.Seq([(d_778_name_, d_780_test_)]))
        d_782_mplEncryptManifest_: JSON_Values.JSON
        d_782_mplEncryptManifest_ = JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("manifest"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("version"), JSON_Values.JSON_Number(JSON_Values.default__.Int(4))), (_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("awses-mpl-encrypt")))]))), (_dafny.Seq("keys"), JSON_Values.JSON_String(_dafny.Seq("file://keys.json"))), (_dafny.Seq("tests"), JSON_Values.JSON_Object(d_776_testsJSON_))]))
        d_783_mplEncryptManifestBytes_: _dafny.Seq
        d_784_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda108_(d_785_e_):
            return (d_785_e_).ToString()

        d_784_valueOrError2_ = (JSON_API.default__.Serialize(d_782_mplEncryptManifest_)).MapFailure(lambda108_)
        if (d_784_valueOrError2_).IsFailure():
            output = (d_784_valueOrError2_).PropagateFailure()
            return output
        d_783_mplEncryptManifestBytes_ = (d_784_valueOrError2_).Extract()
        d_786___v0_: tuple
        d_787_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out51_: Wrappers.Result
        out51_ = default__.WriteVectorsFile(((op).encryptManifestOutput) + (_dafny.Seq("manifest.json")), d_783_mplEncryptManifestBytes_)
        d_787_valueOrError3_ = out51_
        if (d_787_valueOrError3_).IsFailure():
            output = (d_787_valueOrError3_).PropagateFailure()
            return output
        d_786___v0_ = (d_787_valueOrError3_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def WriteDecryptManifest(op, keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_788_testsJSON_: _dafny.Seq
        d_788_testsJSON_ = _dafny.Seq([])
        hi2_ = len(tests)
        for d_789_i_ in range(0, hi2_):
            d_790_name_: _dafny.Seq
            d_791_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out52_: Wrappers.Result
            out52_ = UUID.default__.GenerateUUID()
            d_791_valueOrError0_ = out52_
            if (d_791_valueOrError0_).IsFailure():
                output = (d_791_valueOrError0_).PropagateFailure()
                return output
            d_790_name_ = (d_791_valueOrError0_).Extract()
            d_792_test_: JSON_Values.JSON
            d_793_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
            d_793_valueOrError1_ = WriteJsonManifests.default__.DecryptTestVectorToJson((tests)[d_789_i_])
            if (d_793_valueOrError1_).IsFailure():
                output = (d_793_valueOrError1_).PropagateFailure()
                return output
            d_792_test_ = (d_793_valueOrError1_).Extract()
            d_788_testsJSON_ = (d_788_testsJSON_) + (_dafny.Seq([(d_790_name_, d_792_test_)]))
        d_794_mplDecryptManifest_: JSON_Values.JSON
        d_794_mplDecryptManifest_ = JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("manifest"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("version"), JSON_Values.JSON_Number(JSON_Values.default__.Int(4))), (_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("awses-mpl-decrypt")))]))), (_dafny.Seq("client"), JSON_Values.JSON_String(_dafny.Seq("mpl-dafny"))), (_dafny.Seq("keys"), JSON_Values.JSON_String(_dafny.Seq("file://keys.json"))), (_dafny.Seq("tests"), JSON_Values.JSON_Object(d_788_testsJSON_))]))
        d_795_mplDecryptManifestBytes_: _dafny.Seq
        d_796_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda109_(d_797_e_):
            return (d_797_e_).ToString()

        d_796_valueOrError2_ = (JSON_API.default__.Serialize(d_794_mplDecryptManifest_)).MapFailure(lambda109_)
        if (d_796_valueOrError2_).IsFailure():
            output = (d_796_valueOrError2_).PropagateFailure()
            return output
        d_795_mplDecryptManifestBytes_ = (d_796_valueOrError2_).Extract()
        d_798___v1_: tuple
        d_799_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out53_: Wrappers.Result
        out53_ = default__.WriteVectorsFile(((op).decryptManifestOutput) + (_dafny.Seq("manifest.json")), d_795_mplDecryptManifestBytes_)
        d_799_valueOrError3_ = out53_
        if (d_799_valueOrError3_).IsFailure():
            output = (d_799_valueOrError3_).PropagateFailure()
            return output
        d_798___v1_ = (d_799_valueOrError3_).Extract()
        d_800_keysJsonFileName_: _dafny.Seq
        d_800_keysJsonFileName_ = _dafny.Seq("keys.json")
        d_801_keysJsonBytes_: _dafny.Seq
        d_802_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda110_(d_803_e_):
            return (d_803_e_).ToString()

        d_802_valueOrError4_ = (JSON_API.default__.Serialize(((keys).config).keysJson)).MapFailure(lambda110_)
        if (d_802_valueOrError4_).IsFailure():
            output = (d_802_valueOrError4_).PropagateFailure()
            return output
        d_801_keysJsonBytes_ = (d_802_valueOrError4_).Extract()
        d_804___v2_: tuple
        d_805_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out54_: Wrappers.Result
        out54_ = default__.WriteVectorsFile(((op).decryptManifestOutput) + (d_800_keysJsonFileName_), d_801_keysJsonBytes_)
        d_805_valueOrError5_ = out54_
        if (d_805_valueOrError5_).IsFailure():
            output = (d_805_valueOrError5_).PropagateFailure()
            return output
        d_804___v2_ = (d_805_valueOrError5_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def WriteVectorsFile(location, bytes):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_806_bv_: _dafny.Seq
        d_806_bv_ = JSONHelpers.default__.BytesBv(bytes)
        out55_: Wrappers.Result
        out55_ = FileIO.default__.WriteBytesToFile(location, d_806_bv_)
        output = out55_
        return output

    @_dafny.classproperty
    def AllPositiveKeyringTests(instance):
        return ((((((((((((_dafny.Set({})) | (AllDefaultCmm.default__.Tests)) | (AllHierarchy.default__.Tests)) | (AllKms.default__.Tests)) | (AllKmsMrkAware.default__.Tests)) | (AllKmsMrkAwareDiscovery.default__.Tests)) | (AllKmsRsa.default__.Tests)) | (AllRawAES.default__.Tests)) | (AllRawRSA.default__.Tests)) | (AllMulti.default__.Tests)) | (AllRequiredEncryptionContextCmm.default__.Tests)) | (AllRawECDH.default__.Tests)) | (AllKmsEcdh.default__.Tests)
