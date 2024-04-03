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
import WriteJsonManifests
import CompleteVectors
import ParseJsonManifests
import TestManifests

# Module: WrappedMaterialProvidersMain

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

