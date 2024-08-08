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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.ParseJsonManifests as ParseJsonManifests

# Module: TestManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StartEncrypt(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_928_encryptManifest_: ManifestData
        d_929_valueOrError0_: Wrappers.Result = None
        out56_: Wrappers.Result
        out56_ = default__.GetManifest((op).manifestPath, _dafny.Seq("manifest.json"))
        d_929_valueOrError0_ = out56_
        if (d_929_valueOrError0_).IsFailure():
            output = (d_929_valueOrError0_).PropagateFailure()
            return output
        d_928_encryptManifest_ = (d_929_valueOrError0_).Extract()
        d_930_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_930_valueOrError1_ = Wrappers.default__.Need((d_928_encryptManifest_).is_EncryptManifest, _dafny.Seq("Not a encrypt manifest"))
        if (d_930_valueOrError1_).IsFailure():
            output = (d_930_valueOrError1_).PropagateFailure()
            return output
        d_931_encryptVectors_: _dafny.Seq
        d_932_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_932_valueOrError2_ = ParseJsonManifests.default__.BuildEncryptTestVector((d_928_encryptManifest_).keys, (d_928_encryptManifest_).jsonTests)
        if (d_932_valueOrError2_).IsFailure():
            output = (d_932_valueOrError2_).PropagateFailure()
            return output
        d_931_encryptVectors_ = (d_932_valueOrError2_).Extract()
        d_933_encryptTests_: _dafny.Seq
        d_934_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out57_: Wrappers.Result
        out57_ = default__.ToEncryptTests((d_928_encryptManifest_).keys, d_931_encryptVectors_)
        d_934_valueOrError3_ = out57_
        if (d_934_valueOrError3_).IsFailure():
            output = (d_934_valueOrError3_).PropagateFailure()
            return output
        d_933_encryptTests_ = (d_934_valueOrError3_).Extract()
        d_935_decryptVectors_: _dafny.Seq
        out58_: _dafny.Seq
        out58_ = default__.TestEncrypts(d_933_encryptTests_, (d_928_encryptManifest_).keys)
        d_935_decryptVectors_ = out58_
        d_936___v0_: tuple
        d_937_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out59_: Wrappers.Result
        out59_ = CompleteVectors.default__.WriteDecryptManifest(op, (d_928_encryptManifest_).keys, d_935_decryptVectors_)
        d_937_valueOrError4_ = out59_
        if (d_937_valueOrError4_).IsFailure():
            output = (d_937_valueOrError4_).PropagateFailure()
            return output
        d_936___v0_ = (d_937_valueOrError4_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def TestEncrypts(tests, keys):
        output: _dafny.Seq = _dafny.Seq({})
        d_938_hasFailure_: bool
        d_938_hasFailure_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Encrypt Tests =================== \n\n")))
        d_939_decryptableTests_: _dafny.Seq
        d_939_decryptableTests_ = _dafny.Seq([])
        hi3_ = len(tests)
        for d_940_i_ in range(0, hi3_):
            d_941_test_: TestVectors.EncryptTest
            d_941_test_ = (tests)[d_940_i_]
            d_942_pass_: bool
            d_943_maybeEncryptionMaterials_: Wrappers.Option
            out60_: bool
            out61_: Wrappers.Option
            out60_, out61_ = TestVectors.default__.TestGetEncryptionMaterials(d_941_test_)
            d_942_pass_ = out60_
            d_943_maybeEncryptionMaterials_ = out61_
            if (d_942_pass_) and (not(((d_941_test_).vector).is_NegativeEncryptKeyringVector)):
                d_939_decryptableTests_ = (d_939_decryptableTests_) + (_dafny.Seq([(d_941_test_, (d_943_maybeEncryptionMaterials_).value)]))
            elif not(d_942_pass_):
                d_938_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Encrypt Tests =================== \n\n")))
        if not(not(d_938_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_944_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out62_: Wrappers.Result
        out62_ = default__.ToDecryptTestVectors(keys, d_939_decryptableTests_)
        d_944_valueOrError0_ = out62_
        if not(not((d_944_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(75,14): " + _dafny.string_of(d_944_valueOrError0_))
        output = (d_944_valueOrError0_).Extract()
        return output

    @staticmethod
    def StartDecrypt(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_945_decryptManifest_: ManifestData
        d_946_valueOrError0_: Wrappers.Result = None
        out63_: Wrappers.Result
        out63_ = default__.GetManifest((op).manifestPath, _dafny.Seq("manifest.json"))
        d_946_valueOrError0_ = out63_
        if (d_946_valueOrError0_).IsFailure():
            output = (d_946_valueOrError0_).PropagateFailure()
            return output
        d_945_decryptManifest_ = (d_946_valueOrError0_).Extract()
        d_947_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_947_valueOrError1_ = Wrappers.default__.Need((d_945_decryptManifest_).is_DecryptManifest, _dafny.Seq("Not a encrypt manifest"))
        if (d_947_valueOrError1_).IsFailure():
            output = (d_947_valueOrError1_).PropagateFailure()
            return output
        d_948_decryptVectors_: _dafny.Seq
        d_949_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_949_valueOrError2_ = ParseJsonManifests.default__.BuildDecryptTestVector((d_945_decryptManifest_).keys, (d_945_decryptManifest_).jsonTests)
        if (d_949_valueOrError2_).IsFailure():
            output = (d_949_valueOrError2_).PropagateFailure()
            return output
        d_948_decryptVectors_ = (d_949_valueOrError2_).Extract()
        d_950_decryptTests_: _dafny.Seq
        d_951_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out64_: Wrappers.Result
        out64_ = default__.ToDecryptTests((d_945_decryptManifest_).keys, d_948_decryptVectors_)
        d_951_valueOrError3_ = out64_
        if (d_951_valueOrError3_).IsFailure():
            output = (d_951_valueOrError3_).PropagateFailure()
            return output
        d_950_decryptTests_ = (d_951_valueOrError3_).Extract()
        default__.TestDecrypts(d_950_decryptTests_)
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def TestDecrypts(tests):
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Decrypt Tests =================== \n\n")))
        d_952_hasFailure_: bool
        d_952_hasFailure_ = False
        hi4_ = len(tests)
        for d_953_i_ in range(0, hi4_):
            d_954_pass_: bool
            out65_: bool
            out65_ = TestVectors.default__.TestDecryptMaterials((tests)[d_953_i_])
            d_954_pass_ = out65_
            if not(d_954_pass_):
                d_952_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed ")))
        _dafny.print(_dafny.string_of(len(tests)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Decrypt Tests =================== \n\n")))
        if not(not(d_952_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def ToEncryptTests(keys, encryptVectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_955_encryptTests_: _dafny.Seq
        d_955_encryptTests_ = _dafny.Seq([])
        hi5_ = len(encryptVectors)
        for d_956_i_ in range(0, hi5_):
            d_957_test_: TestVectors.EncryptTest
            d_958_valueOrError0_: Wrappers.Result = None
            out66_: Wrappers.Result
            out66_ = TestVectors.default__.ToEncryptTest(keys, (encryptVectors)[d_956_i_])
            d_958_valueOrError0_ = out66_
            if (d_958_valueOrError0_).IsFailure():
                output = (d_958_valueOrError0_).PropagateFailure()
                return output
            d_957_test_ = (d_958_valueOrError0_).Extract()
            d_955_encryptTests_ = (d_955_encryptTests_) + (_dafny.Seq([d_957_test_]))
        output = Wrappers.Result_Success(d_955_encryptTests_)
        return output
        return output

    @staticmethod
    def ToDecryptTestVectors(keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_959_successfulEncrypt_: _dafny.Seq
        def lambda114_(d_960_r_):
            return ((((d_960_r_)[0]).vector).is_PositiveEncryptKeyringVector) or ((((d_960_r_)[0]).vector).is_PositiveEncryptNegativeDecryptKeyringVector)

        d_959_successfulEncrypt_ = Seq.default__.Filter(lambda114_, tests)
        d_961_decryptTestVectors_: _dafny.Seq
        d_961_decryptTestVectors_ = _dafny.Seq([])
        hi6_ = len(d_959_successfulEncrypt_)
        for d_962_i_ in range(0, hi6_):
            d_963_vector_: TestVectors.DecryptTestVector
            d_963_vector_ = TestVectors.default__.EncryptTestToDecryptVector(((d_959_successfulEncrypt_)[d_962_i_])[0], ((d_959_successfulEncrypt_)[d_962_i_])[1])
            d_961_decryptTestVectors_ = (d_961_decryptTestVectors_) + (_dafny.Seq([d_963_vector_]))
        output = Wrappers.Result_Success(d_961_decryptTestVectors_)
        return output

    @staticmethod
    def ToDecryptTests(keys, vectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_964_decryptTests_: _dafny.Seq
        d_964_decryptTests_ = _dafny.Seq([])
        hi7_ = len(vectors)
        for d_965_i_ in range(0, hi7_):
            d_966_test_: TestVectors.DecryptTest
            d_967_valueOrError0_: Wrappers.Result = None
            out67_: Wrappers.Result
            out67_ = TestVectors.default__.DecryptVectorToDecryptTest(keys, (vectors)[d_965_i_])
            d_967_valueOrError0_ = out67_
            if (d_967_valueOrError0_).IsFailure():
                output = (d_967_valueOrError0_).PropagateFailure()
                return output
            d_966_test_ = (d_967_valueOrError0_).Extract()
            d_964_decryptTests_ = (d_964_decryptTests_) + (_dafny.Seq([d_966_test_]))
        output = Wrappers.Result_Success(d_964_decryptTests_)
        return output
        return output

    @staticmethod
    def GetManifest(manifestPath, manifestFileName):
        manifestData: Wrappers.Result = None
        d_968_decryptManifestBv_: _dafny.Seq
        d_969_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out68_: Wrappers.Result
        out68_ = FileIO.default__.ReadBytesFromFile((manifestPath) + (manifestFileName))
        d_969_valueOrError0_ = out68_
        if (d_969_valueOrError0_).IsFailure():
            manifestData = (d_969_valueOrError0_).PropagateFailure()
            return manifestData
        d_968_decryptManifestBv_ = (d_969_valueOrError0_).Extract()
        d_970_decryptManifestBytes_: _dafny.Seq
        d_970_decryptManifestBytes_ = JSONHelpers.default__.BvToBytes(d_968_decryptManifestBv_)
        d_971_manifestJson_: JSON_Values.JSON
        d_972_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
        def lambda115_(d_973_e_):
            return (d_973_e_).ToString()

        d_972_valueOrError1_ = (JSON_API.default__.Deserialize(d_970_decryptManifestBytes_)).MapFailure(lambda115_)
        if (d_972_valueOrError1_).IsFailure():
            manifestData = (d_972_valueOrError1_).PropagateFailure()
            return manifestData
        d_971_manifestJson_ = (d_972_valueOrError1_).Extract()
        d_974_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_974_valueOrError2_ = Wrappers.default__.Need((d_971_manifestJson_).is_Object, _dafny.Seq("Not a JSON object"))
        if (d_974_valueOrError2_).IsFailure():
            manifestData = (d_974_valueOrError2_).PropagateFailure()
            return manifestData
        d_975_manifest_: _dafny.Seq
        d_976_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_976_valueOrError3_ = JSONHelpers.default__.GetObject(_dafny.Seq("manifest"), (d_971_manifestJson_).obj)
        if (d_976_valueOrError3_).IsFailure():
            manifestData = (d_976_valueOrError3_).PropagateFailure()
            return manifestData
        d_975_manifest_ = (d_976_valueOrError3_).Extract()
        d_977_version_: int
        d_978_valueOrError4_: Wrappers.Result = Wrappers.Result.default(System_.nat.default)()
        d_978_valueOrError4_ = JSONHelpers.default__.GetNat(_dafny.Seq("version"), d_975_manifest_)
        if (d_978_valueOrError4_).IsFailure():
            manifestData = (d_978_valueOrError4_).PropagateFailure()
            return manifestData
        d_977_version_ = (d_978_valueOrError4_).Extract()
        d_979_typ_: _dafny.Seq
        d_980_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_980_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("type"), d_975_manifest_)
        if (d_980_valueOrError5_).IsFailure():
            manifestData = (d_980_valueOrError5_).PropagateFailure()
            return manifestData
        d_979_typ_ = (d_980_valueOrError5_).Extract()
        d_981_keyManifestUri_: _dafny.Seq
        d_982_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_982_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("keys"), (d_971_manifestJson_).obj)
        if (d_982_valueOrError6_).IsFailure():
            manifestData = (d_982_valueOrError6_).PropagateFailure()
            return manifestData
        d_981_keyManifestUri_ = (d_982_valueOrError6_).Extract()
        d_983_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_983_valueOrError7_ = Wrappers.default__.Need((_dafny.Seq("file://")) < (d_981_keyManifestUri_), _dafny.Seq("Unexpected URI prefix"))
        if (d_983_valueOrError7_).IsFailure():
            manifestData = (d_983_valueOrError7_).PropagateFailure()
            return manifestData
        d_984_keyManifestPath_: _dafny.Seq
        d_984_keyManifestPath_ = (manifestPath) + (_dafny.Seq((d_981_keyManifestUri_)[7::]))
        d_985_keys_: KeyVectors.KeyVectorsClient
        d_986_valueOrError8_: Wrappers.Result = None
        out69_: Wrappers.Result
        out69_ = KeyVectors.default__.KeyVectors(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig_KeyVectorsConfig(d_984_keyManifestPath_))
        d_986_valueOrError8_ = out69_
        if not(not((d_986_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(222,16): " + _dafny.string_of(d_986_valueOrError8_))
        d_985_keys_ = (d_986_valueOrError8_).Extract()
        d_987_jsonTests_: _dafny.Seq
        d_988_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_988_valueOrError9_ = JSONHelpers.default__.GetObject(_dafny.Seq("tests"), (d_971_manifestJson_).obj)
        if (d_988_valueOrError9_).IsFailure():
            manifestData = (d_988_valueOrError9_).PropagateFailure()
            return manifestData
        d_987_jsonTests_ = (d_988_valueOrError9_).Extract()
        source33_ = d_979_typ_
        unmatched33 = True
        if unmatched33:
            if (source33_) == (_dafny.Seq("awses-mpl-decrypt")):
                unmatched33 = False
                d_989_client_: JSON_Values.JSON
                d_990_valueOrError10_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
                d_990_valueOrError10_ = JSONHelpers.default__.Get(_dafny.Seq("client"), (d_971_manifestJson_).obj)
                if (d_990_valueOrError10_).IsFailure():
                    manifestData = (d_990_valueOrError10_).PropagateFailure()
                    return manifestData
                d_989_client_ = (d_990_valueOrError10_).Extract()
                manifestData = Wrappers.Result_Success(ManifestData_DecryptManifest(d_977_version_, d_985_keys_, d_989_client_, d_987_jsonTests_))
        if unmatched33:
            if (source33_) == (_dafny.Seq("awses-mpl-encrypt")):
                unmatched33 = False
                manifestData = Wrappers.Result_Success(ManifestData_EncryptManifest(d_977_version_, d_985_keys_, d_987_jsonTests_))
        if unmatched33:
            unmatched33 = False
            manifestData = Wrappers.Result_Failure((_dafny.Seq("Unsupported manifest type:")) + (d_979_typ_))
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

