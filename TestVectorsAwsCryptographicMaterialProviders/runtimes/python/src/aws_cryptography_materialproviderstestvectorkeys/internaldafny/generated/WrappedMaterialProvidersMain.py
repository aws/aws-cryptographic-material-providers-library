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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CompleteVectors as CompleteVectors
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.ParseJsonManifests as ParseJsonManifests
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.TestManifests as TestManifests

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProvidersMain

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Main(args):
        if not((0) < (len(args))):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(19,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1120_op_q_: Wrappers.Result
        d_1120_op_q_ = default__.ParseCommandLineOptions(_dafny.Seq((args)[1::]))
        if (d_1120_op_q_).is_Success:
            d_1121_op_: MplManifestOptions.ManifestOptions
            d_1121_op_ = (d_1120_op_q_).value
            if (d_1121_op_).is_Decrypt:
                pass
            elif (d_1121_op_).is_Encrypt:
                d_1122_result_: Wrappers.Result
                out77_: Wrappers.Result
                out77_ = TestManifests.default__.StartEncrypt(d_1121_op_)
                d_1122_result_ = out77_
                if (d_1122_result_).is_Failure:
                    _dafny.print(_dafny.string_of((d_1122_result_).error))
                if not((d_1122_result_).is_Success):
                    raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(33,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            elif (d_1121_op_).is_EncryptManifest:
                d_1123_result_: Wrappers.Result
                out78_: Wrappers.Result
                out78_ = CompleteVectors.default__.WriteStuff(d_1121_op_)
                d_1123_result_ = out78_
                if (d_1123_result_).is_Failure:
                    _dafny.print(_dafny.string_of((d_1123_result_).error))
                if not((d_1123_result_).is_Success):
                    raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(39,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            elif True:
                raise Exception("unreachable alternative")
        elif True:
            _dafny.print(_dafny.string_of((d_1120_op_q_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("help")))

    @staticmethod
    def ParseCommandLineOptions(args):
        d_1124_valueOrError0_ = Wrappers.default__.Need((1) < (len(args)), _dafny.Seq("Not enough arguments."))
        if (d_1124_valueOrError0_).IsFailure():
            return (d_1124_valueOrError0_).PropagateFailure()
        elif True:
            d_1125_valueOrError1_ = Wrappers.default__.Need(default__.CommandOption_q((args)[0]), (_dafny.Seq("Unknown argument:")) + ((args)[0]))
            if (d_1125_valueOrError1_).IsFailure():
                return (d_1125_valueOrError1_).PropagateFailure()
            elif True:
                d_1126_op_ = (default__.Options2Map(_dafny.Seq((args)[1::])) if (_dafny.euclidian_modulus((len(args)) - (1), 2)) == (0) else default__.Options2Map(_dafny.Seq((args)[1:(len(args)) - (1):])))
                if ((args)[0]) == (_dafny.Seq("decrypt")):
                    return default__.ParseDecryptOptions(d_1126_op_)
                elif ((args)[0]) == (_dafny.Seq("encrypt")):
                    return default__.ParseEncryptOptions(d_1126_op_)
                elif True:
                    return default__.ParseEncryptManifestOptions(d_1126_op_)

    @staticmethod
    def ParseDecryptOptions(op):
        d_1127_valueOrError0_ = Wrappers.default__.Need(default__.DecryptOptions_q(op), _dafny.Seq("Incorrect arguments"))
        if (d_1127_valueOrError0_).IsFailure():
            return (d_1127_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(MplManifestOptions.ManifestOptions_Decrypt(((op)[_dafny.Seq("-manifest-path")] if (Seq.default__.Last((op)[_dafny.Seq("-manifest-path")])) == ('/') else ((op)[_dafny.Seq("-manifest-path")]) + (_dafny.Seq("/"))), (Wrappers.Option_Some((op)[_dafny.Seq("-test-name")]) if (_dafny.Seq("-test-name")) in (op) else Wrappers.Option_None())))

    @staticmethod
    def ParseEncryptOptions(op):
        d_1128_valueOrError0_ = Wrappers.default__.Need(default__.EncryptOptions_q(op), _dafny.Seq("Incorrect arguments"))
        if (d_1128_valueOrError0_).IsFailure():
            return (d_1128_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(MplManifestOptions.ManifestOptions_Encrypt(((op)[_dafny.Seq("-manifest-path")] if (Seq.default__.Last((op)[_dafny.Seq("-manifest-path")])) == ('/') else ((op)[_dafny.Seq("-manifest-path")]) + (_dafny.Seq("/"))), (op)[_dafny.Seq("-decrypt-manifest-output")], (Wrappers.Option_Some((op)[_dafny.Seq("-test-name")]) if (_dafny.Seq("-test-name")) in (op) else Wrappers.Option_None())))

    @staticmethod
    def ParseEncryptManifestOptions(op):
        d_1129_valueOrError0_ = Wrappers.default__.Need(default__.EncryptManifestOptions_q(op), _dafny.Seq("Incorrect arguments"))
        if (d_1129_valueOrError0_).IsFailure():
            return (d_1129_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(MplManifestOptions.ManifestOptions_EncryptManifest(((op)[_dafny.Seq("-encrypt-manifest-output")] if (Seq.default__.Last((op)[_dafny.Seq("-encrypt-manifest-output")])) == ('/') else ((op)[_dafny.Seq("-encrypt-manifest-output")]) + (_dafny.Seq("/")))))

    @staticmethod
    def CommandOption_q(s):
        return (((s) == (_dafny.Seq("decrypt"))) or ((s) == (_dafny.Seq("encrypt")))) or ((s) == (_dafny.Seq("encrypt-manifest")))

    @staticmethod
    def DecryptOptions_q(op):
        return (((((1) <= (len(op))) and ((len(op)) <= (2))) and ((_dafny.Seq("-manifest-path")) in (op))) and ((0) < (len((op)[_dafny.Seq("-manifest-path")])))) and (not ((len(op)) == (2)) or ((_dafny.Seq("-test-name")) in (op)))

    @staticmethod
    def EncryptOptions_q(op):
        return ((((((3) <= (len(op))) and ((len(op)) <= (4))) and ((_dafny.Seq("-manifest-path")) in (op))) and ((0) < (len((op)[_dafny.Seq("-manifest-path")])))) and ((_dafny.Seq("-decrypt-manifest-output")) in (op))) and (not ((len(op)) == (4)) or ((_dafny.Seq("-test-name")) in (op)))

    @staticmethod
    def EncryptManifestOptions_q(op):
        return ((((1) <= (len(op))) and ((len(op)) <= (2))) and ((_dafny.Seq("-encrypt-manifest-output")) in (op))) and ((0) < (len((op)[_dafny.Seq("-encrypt-manifest-output")])))

    @staticmethod
    def DecryptSingleOptions_q(op):
        return ((((3) == (len(op))) and ((_dafny.Seq("-keys-path")) in (op))) and ((_dafny.Seq("-key-description")) in (op))) and ((_dafny.Seq("-base64-bytes")) in (op))

    @staticmethod
    def DecryptRequiredOptions_q(s):
        return (False) or ((s) == (_dafny.Seq("manifest-path")))

    @staticmethod
    def Options2Map(args):
        if (len(args)) == (0):
            return _dafny.Map({})
        elif True:
            d_1130_key_ = (args)[0]
            d_1131_value_ = (args)[1]
            return (_dafny.Map({d_1130_key_: d_1131_value_})) | (default__.Options2Map(_dafny.Seq((args)[2::])))

