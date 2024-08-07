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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.TestManifests as TestManifests

# Module: WrappedMaterialProvidersMain

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Main(args):
        d_991_vectorOptions_: GetOpt.Options
        d_991_vectorOptions_ = GetOpt.Options_Options(_dafny.Seq("test-vectors"), _dafny.Seq("?"), _dafny.Seq([GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("decrypt"), _dafny.Seq("decrypt command for test-vectors"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("manifest-path"), _dafny.Seq("relative path to the location of the manifest"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_Required(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("test-name"), _dafny.Seq("id of the test to run"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No())]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("encrypt"), _dafny.Seq("encrypt command for test-vectors"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("manifest-path"), _dafny.Seq("relative path to the location of the manifest"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_Required(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("decrypt-manifest-path"), _dafny.Seq("relative path to the location where the decrypted manifest will be written to."), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_Required(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No()), GetOpt.Param_Opt(_dafny.Seq("test-name"), _dafny.Seq("id of the test to run"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_UnusedOk(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No())]))), GetOpt.Param_Command(GetOpt.Options_Options(_dafny.Seq("encrypt-manifest"), _dafny.Seq("encryp manifest command for test-vectors"), _dafny.Seq([GetOpt.Param_Opt(_dafny.Seq("encrypt-manifest-output"), _dafny.Seq("relative path of where to store the encrypt-manifest produced"), _dafny.Seq("arg"), GetOpt.default__.NullChar, GetOpt.Unused_Required(), False, GetOpt.Visibility_Normal(), _dafny.Seq([]), _dafny.Seq([]), GetOpt.Tri_No())])))]))
        if not((0) < (len(args))):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_992_parsedOptions_q_: Wrappers.Result
        d_992_parsedOptions_q_ = GetOpt.default__.GetOptions(d_991_vectorOptions_, args)
        if (d_992_parsedOptions_q_).is_Success:
            d_993_op_q_: Wrappers.Result
            d_993_op_q_ = default__.ParseCommandLineOptions((d_992_parsedOptions_q_).value)
            if (d_993_op_q_).is_Success:
                d_994_op_: MplManifestOptions.ManifestOptions
                d_994_op_ = (d_993_op_q_).value
                if (d_994_op_).is_Decrypt:
                    d_995_result_: Wrappers.Result
                    out70_: Wrappers.Result
                    out70_ = TestManifests.default__.StartDecrypt(d_994_op_)
                    d_995_result_ = out70_
                    if (d_995_result_).is_Failure:
                        _dafny.print(_dafny.string_of((d_995_result_).error))
                    if not((d_995_result_).is_Success):
                        raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(52,10): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                elif (d_994_op_).is_Encrypt:
                    d_996_result_: Wrappers.Result
                    out71_: Wrappers.Result
                    out71_ = TestManifests.default__.StartEncrypt(d_994_op_)
                    d_996_result_ = out71_
                    if (d_996_result_).is_Failure:
                        _dafny.print(_dafny.string_of((d_996_result_).error))
                    if not((d_996_result_).is_Success):
                        raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(58,10): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                elif (d_994_op_).is_EncryptManifest:
                    d_997_result_: Wrappers.Result
                    out72_: Wrappers.Result
                    out72_ = CompleteVectors.default__.WriteStuff(d_994_op_)
                    d_997_result_ = out72_
                    if (d_997_result_).is_Failure:
                        _dafny.print(_dafny.string_of((d_997_result_).error))
                    if not((d_997_result_).is_Success):
                        raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(64,10): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                elif True:
                    raise Exception("unreachable alternative")
            elif True:
                _dafny.print(_dafny.string_of(((d_993_op_q_).error) + (_dafny.Seq("\n"))))
                _dafny.print(_dafny.string_of(_dafny.Seq("help\n")))
        elif True:
            _dafny.print(_dafny.string_of(((d_992_parsedOptions_q_).error) + (_dafny.Seq("\n"))))

    @staticmethod
    def ParseCommandLineOptions(parsedOptions):
        pat_let_tv89_ = parsedOptions
        pat_let_tv90_ = parsedOptions
        pat_let_tv91_ = parsedOptions
        d_998_valueOrError0_ = Wrappers.default__.Need(((parsedOptions).subcommand).is_Some, _dafny.Seq("Must supply subcommand\n"))
        if (d_998_valueOrError0_).IsFailure():
            return (d_998_valueOrError0_).PropagateFailure()
        elif True:
            source34_ = (((parsedOptions).subcommand).value).command
            unmatched34 = True
            if unmatched34:
                if (source34_) == (_dafny.Seq("decrypt")):
                    unmatched34 = False
                    return default__.ParseDecryptCmd((((pat_let_tv89_).subcommand).value).params)
            if unmatched34:
                if (source34_) == (_dafny.Seq("encrypt")):
                    unmatched34 = False
                    return default__.ParseEncryptCmd((((pat_let_tv90_).subcommand).value).params)
            if unmatched34:
                if (source34_) == (_dafny.Seq("encrypt-manifest")):
                    unmatched34 = False
                    return default__.ParseEncryptManifestCmd((((pat_let_tv91_).subcommand).value).params)
            if unmatched34:
                unmatched34 = False
                return Wrappers.Result_Failure(_dafny.Seq("Received unknown subcommand"))
            raise Exception("unexpected control point")

    @staticmethod
    def ParseDecryptCmd(params):
        d_999_manifestPath_q_ = GetOpt.default__.OptValue(params, _dafny.Seq("manifest-path"))
        d_1000_testName_q_ = GetOpt.default__.OptValue(params, _dafny.Seq("test-name"))
        d_1001_manifestPath_ = ((d_999_manifestPath_q_).value if (d_999_manifestPath_q_).is_Some else _dafny.Seq("."))
        d_1002_valueOrError0_ = Wrappers.default__.Need((0) < (len(d_1001_manifestPath_)), _dafny.Seq("Invalid manifest path length\n"))
        if (d_1002_valueOrError0_).IsFailure():
            return (d_1002_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(MplManifestOptions.ManifestOptions_Decrypt((d_1001_manifestPath_ if (Seq.default__.Last(d_1001_manifestPath_)) == ('/') else (d_1001_manifestPath_) + (_dafny.Seq("/"))), (d_1000_testName_q_ if (d_1000_testName_q_).is_Some else Wrappers.Option_None())))

    @staticmethod
    def ParseEncryptCmd(params):
        d_1003_manifestPath_q_ = GetOpt.default__.OptValue(params, _dafny.Seq("manifest-path"))
        d_1004_decryptManifestPath_q_ = GetOpt.default__.OptValue(params, _dafny.Seq("decrypt-manifest-path"))
        d_1005_testName_q_ = GetOpt.default__.OptValue(params, _dafny.Seq("test-name"))
        d_1006_manifestPath_ = ((d_1003_manifestPath_q_).value if (d_1003_manifestPath_q_).is_Some else _dafny.Seq("."))
        d_1007_decryptManifestPath_ = ((d_1004_decryptManifestPath_q_).value if (d_1004_decryptManifestPath_q_).is_Some else _dafny.Seq("."))
        d_1008_valueOrError0_ = Wrappers.default__.Need(((0) < (len(d_1006_manifestPath_))) and ((0) < (len(d_1007_decryptManifestPath_))), _dafny.Seq("Invalid manifest or decrypt manifest path length\n"))
        if (d_1008_valueOrError0_).IsFailure():
            return (d_1008_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(MplManifestOptions.ManifestOptions_Encrypt((d_1006_manifestPath_ if (Seq.default__.Last(d_1006_manifestPath_)) == ('/') else (d_1006_manifestPath_) + (_dafny.Seq("/"))), (d_1007_decryptManifestPath_ if (Seq.default__.Last(d_1007_decryptManifestPath_)) == ('/') else (d_1007_decryptManifestPath_) + (_dafny.Seq("/"))), (d_1005_testName_q_ if (d_1005_testName_q_).is_Some else Wrappers.Option_None())))

    @staticmethod
    def ParseEncryptManifestCmd(params):
        d_1009_encryptManifestOutput_q_ = GetOpt.default__.OptValue(params, _dafny.Seq("encrypt-manifest-output"))
        d_1010_encryptManifestOutput_ = ((d_1009_encryptManifestOutput_q_).value if (d_1009_encryptManifestOutput_q_).is_Some else _dafny.Seq("."))
        d_1011_valueOrError0_ = Wrappers.default__.Need((0) < (len(d_1010_encryptManifestOutput_)), _dafny.Seq("Invalid encrypt manifest output length"))
        if (d_1011_valueOrError0_).IsFailure():
            return (d_1011_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(MplManifestOptions.ManifestOptions_EncryptManifest((d_1010_encryptManifestOutput_ if (Seq.default__.Last(d_1010_encryptManifestOutput_)) == ('/') else (d_1010_encryptManifestOutput_) + (_dafny.Seq("/")))))

    @staticmethod
    def DecryptSingleOptions_q(op):
        return ((((3) == (len(op))) and ((_dafny.Seq("-keys-path")) in (op))) and ((_dafny.Seq("-key-description")) in (op))) and ((_dafny.Seq("-base64-bytes")) in (op))

