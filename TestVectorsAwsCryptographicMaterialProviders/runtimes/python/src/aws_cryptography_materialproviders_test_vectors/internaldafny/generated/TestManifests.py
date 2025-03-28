import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.CacheConstants as CacheConstants
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Values as JSON_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_API as JSON_API
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeysVectorOperations as KeysVectorOperations
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyVectors as KeyVectors
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.TestVectors as TestVectors
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllHierarchy as AllHierarchy
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.EncryptionContextUtils as EncryptionContextUtils
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKms as AllKms
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsMrkAware as AllKmsMrkAware
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsMrkAwareDiscovery as AllKmsMrkAwareDiscovery
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsRsa as AllKmsRsa
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsEcdh as AllKmsEcdh
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRawRSA as AllRawRSA
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRawECDH as AllRawECDH
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllDefaultCmm as AllDefaultCmm
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRequiredEncryptionContextCmm as AllRequiredEncryptionContextCmm
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllMulti as AllMulti
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.WriteJsonManifests as WriteJsonManifests
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CompleteVectors as CompleteVectors
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.ParseJsonManifests as ParseJsonManifests

# Module: TestManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StartEncrypt(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_0_time_: Time.AbsoluteTime
        out0_: Time.AbsoluteTime
        out0_ = Time.default__.GetAbsoluteTime()
        d_0_time_ = out0_
        d_1_valueOrError0_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = default__.GetManifest((op).manifestPath, _dafny.Seq("manifest.json"))
        d_1_valueOrError0_ = out1_
        if (d_1_valueOrError0_).IsFailure():
            output = (d_1_valueOrError0_).PropagateFailure()
            return output
        d_2_encryptManifest_: ManifestData
        d_2_encryptManifest_ = (d_1_valueOrError0_).Extract()
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need((d_2_encryptManifest_).is_EncryptManifest, _dafny.Seq("Not a encrypt manifest"))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_4_valueOrError2_ = ParseJsonManifests.default__.BuildEncryptTestVector((d_2_encryptManifest_).keys, (d_2_encryptManifest_).jsonTests)
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5_encryptVectors_: _dafny.Seq
        d_5_encryptVectors_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = default__.ToEncryptTests((d_2_encryptManifest_).keys, d_5_encryptVectors_)
        d_6_valueOrError3_ = out2_
        if (d_6_valueOrError3_).IsFailure():
            output = (d_6_valueOrError3_).PropagateFailure()
            return output
        d_7_encryptTests_: _dafny.Seq
        d_7_encryptTests_ = (d_6_valueOrError3_).Extract()
        d_8_decryptVectors_: _dafny.Seq
        out3_: _dafny.Seq
        out3_ = default__.TestEncrypts(d_7_encryptTests_, (d_2_encryptManifest_).keys)
        d_8_decryptVectors_ = out3_
        d_9_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out4_: Wrappers.Result
        out4_ = CompleteVectors.default__.WriteDecryptManifest(op, (d_2_encryptManifest_).keys, d_8_decryptVectors_)
        d_9_valueOrError4_ = out4_
        if (d_9_valueOrError4_).IsFailure():
            output = (d_9_valueOrError4_).PropagateFailure()
            return output
        d_10___v0_: tuple
        d_10___v0_ = (d_9_valueOrError4_).Extract()
        Time.default__.PrintTimeSince(d_0_time_)
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def TestEncrypts(tests, keys):
        output: _dafny.Seq = _dafny.Seq({})
        d_0_hasFailure_: bool
        d_0_hasFailure_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Encrypt Tests =================== \n\n")))
        d_1_decryptableTests_: _dafny.Seq
        d_1_decryptableTests_ = _dafny.Seq([])
        hi0_ = len(tests)
        for d_2_i_ in range(0, hi0_):
            d_3_test_: TestVectors.EncryptTest
            d_3_test_ = (tests)[d_2_i_]
            d_4_pass_: bool
            d_5_maybeEncryptionMaterials_: Wrappers.Option
            out0_: bool
            out1_: Wrappers.Option
            out0_, out1_ = TestVectors.default__.TestGetEncryptionMaterials(d_3_test_)
            d_4_pass_ = out0_
            d_5_maybeEncryptionMaterials_ = out1_
            if (d_4_pass_) and (not(((d_3_test_).vector).is_NegativeEncryptKeyringVector)):
                d_1_decryptableTests_ = (d_1_decryptableTests_) + (_dafny.Seq([(d_3_test_, (d_5_maybeEncryptionMaterials_).value)]))
            elif not(d_4_pass_):
                d_0_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Encrypt Tests =================== \n\n")))
        if not(not(d_0_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(78,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_6_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = default__.ToDecryptTestVectors(keys, d_1_decryptableTests_)
        d_6_valueOrError0_ = out2_
        if not(not((d_6_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(79,14): " + _dafny.string_of(d_6_valueOrError0_))
        output = (d_6_valueOrError0_).Extract()
        return output

    @staticmethod
    def StartDecrypt(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_0_time_: Time.AbsoluteTime
        out0_: Time.AbsoluteTime
        out0_ = Time.default__.GetAbsoluteTime()
        d_0_time_ = out0_
        d_1_valueOrError0_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = default__.GetManifest((op).manifestPath, _dafny.Seq("manifest.json"))
        d_1_valueOrError0_ = out1_
        if (d_1_valueOrError0_).IsFailure():
            output = (d_1_valueOrError0_).PropagateFailure()
            return output
        d_2_decryptManifest_: ManifestData
        d_2_decryptManifest_ = (d_1_valueOrError0_).Extract()
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need((d_2_decryptManifest_).is_DecryptManifest, _dafny.Seq("Not a encrypt manifest"))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_4_valueOrError2_ = ParseJsonManifests.default__.BuildDecryptTestVector((d_2_decryptManifest_).keys, (d_2_decryptManifest_).jsonTests)
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5_decryptVectors_: _dafny.Seq
        d_5_decryptVectors_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = default__.ToDecryptTests((d_2_decryptManifest_).keys, d_5_decryptVectors_)
        d_6_valueOrError3_ = out2_
        if (d_6_valueOrError3_).IsFailure():
            output = (d_6_valueOrError3_).PropagateFailure()
            return output
        d_7_decryptTests_: _dafny.Seq
        d_7_decryptTests_ = (d_6_valueOrError3_).Extract()
        default__.TestDecrypts(d_7_decryptTests_)
        Time.default__.PrintTimeSince(d_0_time_)
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def TestDecrypts(tests):
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Decrypt Tests =================== \n\n")))
        d_0_hasFailure_: bool
        d_0_hasFailure_ = False
        hi0_ = len(tests)
        for d_1_i_ in range(0, hi0_):
            d_2_pass_: bool
            out0_: bool
            out0_ = TestVectors.default__.TestDecryptMaterials((tests)[d_1_i_])
            d_2_pass_ = out0_
            if not(d_2_pass_):
                d_0_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Decrypt Tests =================== \n\n")))
        if not(not(d_0_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(119,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def ToEncryptTests(keys, encryptVectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_encryptTests_: _dafny.Seq
        d_0_encryptTests_ = _dafny.Seq([])
        hi0_ = len(encryptVectors)
        for d_1_i_ in range(0, hi0_):
            d_2_valueOrError0_: Wrappers.Result = None
            out0_: Wrappers.Result
            out0_ = TestVectors.default__.ToEncryptTest(keys, (encryptVectors)[d_1_i_])
            d_2_valueOrError0_ = out0_
            if (d_2_valueOrError0_).IsFailure():
                output = (d_2_valueOrError0_).PropagateFailure()
                return output
            d_3_test_: TestVectors.EncryptTest
            d_3_test_ = (d_2_valueOrError0_).Extract()
            d_0_encryptTests_ = (d_0_encryptTests_) + (_dafny.Seq([d_3_test_]))
        output = Wrappers.Result_Success(d_0_encryptTests_)
        return output
        return output

    @staticmethod
    def ToDecryptTestVectors(keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_successfulEncrypt_: _dafny.Seq
        def lambda0_(d_1_r_):
            return ((((d_1_r_)[0]).vector).is_PositiveEncryptKeyringVector) or ((((d_1_r_)[0]).vector).is_PositiveEncryptNegativeDecryptKeyringVector)

        d_0_successfulEncrypt_ = Seq.default__.Filter(lambda0_, tests)
        d_2_decryptTestVectors_: _dafny.Seq
        d_2_decryptTestVectors_ = _dafny.Seq([])
        hi0_ = len(d_0_successfulEncrypt_)
        for d_3_i_ in range(0, hi0_):
            d_4_vector_: TestVectors.DecryptTestVector
            d_4_vector_ = TestVectors.default__.EncryptTestToDecryptVector(((d_0_successfulEncrypt_)[d_3_i_])[0], ((d_0_successfulEncrypt_)[d_3_i_])[1])
            d_2_decryptTestVectors_ = (d_2_decryptTestVectors_) + (_dafny.Seq([d_4_vector_]))
        output = Wrappers.Result_Success(d_2_decryptTestVectors_)
        return output

    @staticmethod
    def ToDecryptTests(keys, vectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_decryptTests_: _dafny.Seq
        d_0_decryptTests_ = _dafny.Seq([])
        hi0_ = len(vectors)
        for d_1_i_ in range(0, hi0_):
            d_2_valueOrError0_: Wrappers.Result = None
            out0_: Wrappers.Result
            out0_ = TestVectors.default__.DecryptVectorToDecryptTest(keys, (vectors)[d_1_i_])
            d_2_valueOrError0_ = out0_
            if (d_2_valueOrError0_).IsFailure():
                output = (d_2_valueOrError0_).PropagateFailure()
                return output
            d_3_test_: TestVectors.DecryptTest
            d_3_test_ = (d_2_valueOrError0_).Extract()
            d_0_decryptTests_ = (d_0_decryptTests_) + (_dafny.Seq([d_3_test_]))
        output = Wrappers.Result_Success(d_0_decryptTests_)
        return output
        return output

    @staticmethod
    def GetManifest(manifestPath, manifestFileName):
        manifestData: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = FileIO.default__.ReadBytesFromFile((manifestPath) + (manifestFileName))
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            manifestData = (d_0_valueOrError0_).PropagateFailure()
            return manifestData
        d_1_decryptManifestBytes_: _dafny.Seq
        d_1_decryptManifestBytes_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
        def lambda0_(d_3_e_):
            return (d_3_e_).ToString()

        d_2_valueOrError1_ = (JSON_API.default__.Deserialize(d_1_decryptManifestBytes_)).MapFailure(lambda0_)
        if (d_2_valueOrError1_).IsFailure():
            manifestData = (d_2_valueOrError1_).PropagateFailure()
            return manifestData
        d_4_manifestJson_: JSON_Values.JSON
        d_4_manifestJson_ = (d_2_valueOrError1_).Extract()
        d_5_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError2_ = Wrappers.default__.Need((d_4_manifestJson_).is_Object, _dafny.Seq("Not a JSON object"))
        if (d_5_valueOrError2_).IsFailure():
            manifestData = (d_5_valueOrError2_).PropagateFailure()
            return manifestData
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_6_valueOrError3_ = JSONHelpers.default__.GetObject(_dafny.Seq("manifest"), (d_4_manifestJson_).obj)
        if (d_6_valueOrError3_).IsFailure():
            manifestData = (d_6_valueOrError3_).PropagateFailure()
            return manifestData
        d_7_manifest_: _dafny.Seq
        d_7_manifest_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = Wrappers.Result.default(System_.nat.default)()
        d_8_valueOrError4_ = JSONHelpers.default__.GetNat(_dafny.Seq("version"), d_7_manifest_)
        if (d_8_valueOrError4_).IsFailure():
            manifestData = (d_8_valueOrError4_).PropagateFailure()
            return manifestData
        d_9_version_: int
        d_9_version_ = (d_8_valueOrError4_).Extract()
        d_10_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_10_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("type"), d_7_manifest_)
        if (d_10_valueOrError5_).IsFailure():
            manifestData = (d_10_valueOrError5_).PropagateFailure()
            return manifestData
        d_11_typ_: _dafny.Seq
        d_11_typ_ = (d_10_valueOrError5_).Extract()
        d_12_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_12_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("keys"), (d_4_manifestJson_).obj)
        if (d_12_valueOrError6_).IsFailure():
            manifestData = (d_12_valueOrError6_).PropagateFailure()
            return manifestData
        d_13_keyManifestUri_: _dafny.Seq
        d_13_keyManifestUri_ = (d_12_valueOrError6_).Extract()
        d_14_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_14_valueOrError7_ = Wrappers.default__.Need((_dafny.Seq("file://")) < (d_13_keyManifestUri_), _dafny.Seq("Unexpected URI prefix"))
        if (d_14_valueOrError7_).IsFailure():
            manifestData = (d_14_valueOrError7_).PropagateFailure()
            return manifestData
        d_15_keyManifestPath_: _dafny.Seq
        d_15_keyManifestPath_ = (manifestPath) + (_dafny.Seq((d_13_keyManifestUri_)[7::]))
        d_16_valueOrError8_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = KeyVectors.default__.KeyVectors(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig_KeyVectorsConfig(d_15_keyManifestPath_))
        d_16_valueOrError8_ = out1_
        if not(not((d_16_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(227,16): " + _dafny.string_of(d_16_valueOrError8_))
        d_17_keys_: KeyVectors.KeyVectorsClient
        d_17_keys_ = (d_16_valueOrError8_).Extract()
        d_18_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_18_valueOrError9_ = JSONHelpers.default__.GetObject(_dafny.Seq("tests"), (d_4_manifestJson_).obj)
        if (d_18_valueOrError9_).IsFailure():
            manifestData = (d_18_valueOrError9_).PropagateFailure()
            return manifestData
        d_19_jsonTests_: _dafny.Seq
        d_19_jsonTests_ = (d_18_valueOrError9_).Extract()
        source0_ = d_11_typ_
        with _dafny.label("match0"):
            if True:
                if (source0_) == (_dafny.Seq("awses-mpl-decrypt")):
                    d_20_valueOrError10_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
                    d_20_valueOrError10_ = JSONHelpers.default__.Get(_dafny.Seq("client"), (d_4_manifestJson_).obj)
                    if (d_20_valueOrError10_).IsFailure():
                        manifestData = (d_20_valueOrError10_).PropagateFailure()
                        return manifestData
                    d_21_client_: JSON_Values.JSON
                    d_21_client_ = (d_20_valueOrError10_).Extract()
                    manifestData = Wrappers.Result_Success(ManifestData_DecryptManifest(d_9_version_, d_17_keys_, d_21_client_, d_19_jsonTests_))
                    raise _dafny.Break("match0")
            if True:
                if (source0_) == (_dafny.Seq("awses-mpl-encrypt")):
                    manifestData = Wrappers.Result_Success(ManifestData_EncryptManifest(d_9_version_, d_17_keys_, d_19_jsonTests_))
                    raise _dafny.Break("match0")
            if True:
                manifestData = Wrappers.Result_Failure((_dafny.Seq("Unsupported manifest type:")) + (d_11_typ_))
            pass
        return manifestData


class ManifestData:
    @classmethod
    def default(cls, ):
        return lambda: ManifestData_DecryptManifest(int(0), None, JSON_Values.JSON.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptManifest(self) -> bool:
        return isinstance(self, ManifestData_DecryptManifest)
    @property
    def is_EncryptManifest(self) -> bool:
        return isinstance(self, ManifestData_EncryptManifest)

class ManifestData_DecryptManifest(ManifestData, NamedTuple('DecryptManifest', [('version', Any), ('keys', Any), ('client', Any), ('jsonTests', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestManifests.ManifestData.DecryptManifest({_dafny.string_of(self.version)}, {_dafny.string_of(self.keys)}, {_dafny.string_of(self.client)}, {_dafny.string_of(self.jsonTests)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ManifestData_DecryptManifest) and self.version == __o.version and self.keys == __o.keys and self.client == __o.client and self.jsonTests == __o.jsonTests
    def __hash__(self) -> int:
        return super().__hash__()

class ManifestData_EncryptManifest(ManifestData, NamedTuple('EncryptManifest', [('version', Any), ('keys', Any), ('jsonTests', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestManifests.ManifestData.EncryptManifest({_dafny.string_of(self.version)}, {_dafny.string_of(self.keys)}, {_dafny.string_of(self.jsonTests)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ManifestData_EncryptManifest) and self.version == __o.version and self.keys == __o.keys and self.jsonTests == __o.jsonTests
    def __hash__(self) -> int:
        return super().__hash__()

