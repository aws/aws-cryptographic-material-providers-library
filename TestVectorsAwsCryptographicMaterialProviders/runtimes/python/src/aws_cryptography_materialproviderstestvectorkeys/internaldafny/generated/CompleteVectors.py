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

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CompleteVectors

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteStuff(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_879_tests_: _dafny.Seq
        d_879_tests_ = SortedSets.default__.SetToSequence(default__.AllPositiveKeyringTests)
        d_880_testsJSON_: _dafny.Seq
        d_880_testsJSON_ = _dafny.Seq([])
        hi1_ = len(d_879_tests_)
        for d_881_i_ in range(0, hi1_):
            d_882_name_: _dafny.Seq
            d_883_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out57_: Wrappers.Result
            out57_ = UUID.default__.GenerateUUID()
            d_883_valueOrError0_ = out57_
            if (d_883_valueOrError0_).IsFailure():
                output = (d_883_valueOrError0_).PropagateFailure()
                return output
            d_882_name_ = (d_883_valueOrError0_).Extract()
            d_884_test_: JSON_Values.JSON
            d_885_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
            d_885_valueOrError1_ = WriteJsonManifests.default__.EncryptTestVectorToJson((d_879_tests_)[d_881_i_])
            if (d_885_valueOrError1_).IsFailure():
                output = (d_885_valueOrError1_).PropagateFailure()
                return output
            d_884_test_ = (d_885_valueOrError1_).Extract()
            d_880_testsJSON_ = (d_880_testsJSON_) + (_dafny.Seq([(d_882_name_, d_884_test_)]))
        d_886_mplEncryptManifest_: JSON_Values.JSON
        d_886_mplEncryptManifest_ = JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("manifest"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("version"), JSON_Values.JSON_Number(JSON_Values.default__.Int(4))), (_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("awses-mpl-encrypt")))]))), (_dafny.Seq("keys"), JSON_Values.JSON_String(_dafny.Seq("file://keys.json"))), (_dafny.Seq("tests"), JSON_Values.JSON_Object(d_880_testsJSON_))]))
        d_887_mplEncryptManifestBytes_: _dafny.Seq
        d_888_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda100_(d_889_e_):
            return (d_889_e_).ToString()

        d_888_valueOrError2_ = (JSON_API.default__.Serialize(d_886_mplEncryptManifest_)).MapFailure(lambda100_)
        if (d_888_valueOrError2_).IsFailure():
            output = (d_888_valueOrError2_).PropagateFailure()
            return output
        d_887_mplEncryptManifestBytes_ = (d_888_valueOrError2_).Extract()
        d_890___v0_: tuple
        d_891_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out58_: Wrappers.Result
        out58_ = default__.WriteVectorsFile(((op).encryptManifestOutput) + (_dafny.Seq("manifest.json")), d_887_mplEncryptManifestBytes_)
        d_891_valueOrError3_ = out58_
        if (d_891_valueOrError3_).IsFailure():
            output = (d_891_valueOrError3_).PropagateFailure()
            return output
        d_890___v0_ = (d_891_valueOrError3_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def WriteDecryptManifest(op, keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_892_testsJSON_: _dafny.Seq
        d_892_testsJSON_ = _dafny.Seq([])
        hi2_ = len(tests)
        for d_893_i_ in range(0, hi2_):
            d_894_name_: _dafny.Seq
            d_895_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out59_: Wrappers.Result
            out59_ = UUID.default__.GenerateUUID()
            d_895_valueOrError0_ = out59_
            if (d_895_valueOrError0_).IsFailure():
                output = (d_895_valueOrError0_).PropagateFailure()
                return output
            d_894_name_ = (d_895_valueOrError0_).Extract()
            d_896_test_: JSON_Values.JSON
            d_897_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
            d_897_valueOrError1_ = WriteJsonManifests.default__.DecryptTestVectorToJson((tests)[d_893_i_])
            if (d_897_valueOrError1_).IsFailure():
                output = (d_897_valueOrError1_).PropagateFailure()
                return output
            d_896_test_ = (d_897_valueOrError1_).Extract()
            d_892_testsJSON_ = (d_892_testsJSON_) + (_dafny.Seq([(d_894_name_, d_896_test_)]))
        d_898_mplDecryptManifest_: JSON_Values.JSON
        d_898_mplDecryptManifest_ = JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("manifest"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("version"), JSON_Values.JSON_Number(JSON_Values.default__.Int(4))), (_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("awses-mpl-decrypt")))]))), (_dafny.Seq("client"), JSON_Values.JSON_String(_dafny.Seq("mpl-dafny"))), (_dafny.Seq("keys"), JSON_Values.JSON_String(_dafny.Seq("file://keys.json"))), (_dafny.Seq("tests"), JSON_Values.JSON_Object(d_892_testsJSON_))]))
        d_899_mplDecryptManifestBytes_: _dafny.Seq
        d_900_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda101_(d_901_e_):
            return (d_901_e_).ToString()

        d_900_valueOrError2_ = (JSON_API.default__.Serialize(d_898_mplDecryptManifest_)).MapFailure(lambda101_)
        if (d_900_valueOrError2_).IsFailure():
            output = (d_900_valueOrError2_).PropagateFailure()
            return output
        d_899_mplDecryptManifestBytes_ = (d_900_valueOrError2_).Extract()
        d_902___v1_: tuple
        d_903_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out60_: Wrappers.Result
        out60_ = default__.WriteVectorsFile(((op).decryptManifestOutput) + (_dafny.Seq("manifest.json")), d_899_mplDecryptManifestBytes_)
        d_903_valueOrError3_ = out60_
        if (d_903_valueOrError3_).IsFailure():
            output = (d_903_valueOrError3_).PropagateFailure()
            return output
        d_902___v1_ = (d_903_valueOrError3_).Extract()
        d_904_keysJsonFileName_: _dafny.Seq
        d_904_keysJsonFileName_ = _dafny.Seq("keys.json")
        d_905_keysJsonBytes_: _dafny.Seq
        d_906_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda102_(d_907_e_):
            return (d_907_e_).ToString()

        d_906_valueOrError4_ = (JSON_API.default__.Serialize(((keys).config).keysJson)).MapFailure(lambda102_)
        if (d_906_valueOrError4_).IsFailure():
            output = (d_906_valueOrError4_).PropagateFailure()
            return output
        d_905_keysJsonBytes_ = (d_906_valueOrError4_).Extract()
        d_908___v2_: tuple
        d_909_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out61_: Wrappers.Result
        out61_ = default__.WriteVectorsFile(((op).decryptManifestOutput) + (d_904_keysJsonFileName_), d_905_keysJsonBytes_)
        d_909_valueOrError5_ = out61_
        if (d_909_valueOrError5_).IsFailure():
            output = (d_909_valueOrError5_).PropagateFailure()
            return output
        d_908___v2_ = (d_909_valueOrError5_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def WriteVectorsFile(location, bytes):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_910_bv_: _dafny.Seq
        d_910_bv_ = JSONHelpers.default__.BytesBv(bytes)
        out62_: Wrappers.Result
        out62_ = FileIO.default__.WriteBytesToFile(location, d_910_bv_)
        output = out62_
        return output

    @_dafny.classproperty
    def AllPositiveKeyringTests(instance):
        return ((((((((((_dafny.Set({})) | (AllDefaultCmm.default__.Tests)) | (AllHierarchy.default__.Tests)) | (AllKms.default__.Tests)) | (AllKmsMrkAware.default__.Tests)) | (AllKmsMrkAwareDiscovery.default__.Tests)) | (AllKmsRsa.default__.Tests)) | (AllRawAES.default__.Tests)) | (AllRawRSA.default__.Tests)) | (AllMulti.default__.Tests)) | (AllRequiredEncryptionContextCmm.default__.Tests)
