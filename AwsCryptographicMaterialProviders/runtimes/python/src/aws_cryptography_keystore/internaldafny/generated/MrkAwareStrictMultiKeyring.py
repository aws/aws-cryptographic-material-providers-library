import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring

assert "MrkAwareStrictMultiKeyring" == __name__
MrkAwareStrictMultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MrkAwareStrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv35_ = awsKmsKeys
        d_1032_allStrings_: _dafny.Seq
        def lambda66_(source30_):
            if source30_.is_None:
                return (awsKmsKeys).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_1033___mcc_h0_ = source30_.value
                def iife50_(_pat_let19_0):
                    def iife51_(d_1034_g_):
                        return (_dafny.Seq([d_1034_g_])) + ((pat_let_tv35_).UnwrapOr(_dafny.Seq([])))
                    return iife51_(_pat_let19_0)
                return iife50_(d_1033___mcc_h0_)

        d_1032_allStrings_ = lambda66_(generator)
        d_1035_allIdentifiers_: _dafny.Seq
        d_1036_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1036_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_1032_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1036_valueOrError0_).IsFailure():
            output = (d_1036_valueOrError0_).PropagateFailure()
            return output
        d_1035_allIdentifiers_ = (d_1036_valueOrError0_).Extract()
        d_1037_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1037_valueOrError1_ = AwsKmsMrkAreUnique.default__.AwsKmsMrkAreUnique(d_1035_allIdentifiers_)
        if (d_1037_valueOrError1_).IsFailure():
            output = (d_1037_valueOrError1_).PropagateFailure()
            return output
        d_1038_generatorKeyring_: Wrappers.Option = Wrappers.Option_None.default()()
        source31_ = generator
        if source31_.is_None:
            d_1038_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_1039___mcc_h1_ = source31_.value
            d_1040_generatorIdentifier_ = d_1039___mcc_h1_
            d_1041_arn_: AwsArnParsing.AwsKmsIdentifier
            d_1042_valueOrError2_: Wrappers.Result = None
            d_1042_valueOrError2_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_1040_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_1042_valueOrError2_).IsFailure():
                output = (d_1042_valueOrError2_).PropagateFailure()
                return output
            d_1041_arn_ = (d_1042_valueOrError2_).Extract()
            d_1043_region_: Wrappers.Option
            d_1043_region_ = AwsArnParsing.default__.GetRegion(d_1041_arn_)
            d_1044_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_1045_valueOrError3_: Wrappers.Result = None
            out239_: Wrappers.Result
            out239_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_1043_region_).UnwrapOr(_dafny.Seq(""))))
            d_1045_valueOrError3_ = out239_
            if (d_1045_valueOrError3_).IsFailure():
                output = (d_1045_valueOrError3_).PropagateFailure()
                return output
            d_1044_client_ = (d_1045_valueOrError3_).Extract()
            d_1046_g_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
            nw26_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
            nw26_.ctor__(d_1044_client_, d_1040_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_1046_g_ = nw26_
            d_1038_generatorKeyring_ = Wrappers.Option_Some(d_1046_g_)
        d_1047_children_: _dafny.Seq
        d_1047_children_ = _dafny.Seq([])
        source32_ = awsKmsKeys
        if source32_.is_None:
            d_1047_children_ = _dafny.Seq([])
        elif True:
            d_1048___mcc_h2_ = source32_.value
            d_1049_childIdentifiers_ = d_1048___mcc_h2_
            hi6_: int = len(d_1049_childIdentifiers_)
            for d_1050_index_ in range(0, hi6_):
                d_1051_childIdentifier_: _dafny.Seq
                d_1051_childIdentifier_ = (d_1049_childIdentifiers_)[d_1050_index_]
                d_1052_info_: AwsArnParsing.AwsKmsIdentifier
                d_1053_valueOrError4_: Wrappers.Result = None
                d_1053_valueOrError4_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_1051_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_1053_valueOrError4_).IsFailure():
                    output = (d_1053_valueOrError4_).PropagateFailure()
                    return output
                d_1052_info_ = (d_1053_valueOrError4_).Extract()
                d_1054_region_: Wrappers.Option
                d_1054_region_ = AwsArnParsing.default__.GetRegion(d_1052_info_)
                d_1055_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_1056_valueOrError5_: Wrappers.Result = None
                out240_: Wrappers.Result
                out240_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_1054_region_).UnwrapOr(_dafny.Seq(""))))
                d_1056_valueOrError5_ = out240_
                if (d_1056_valueOrError5_).IsFailure():
                    output = (d_1056_valueOrError5_).PropagateFailure()
                    return output
                d_1055_client_ = (d_1056_valueOrError5_).Extract()
                d_1057_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                nw27_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                nw27_.ctor__(d_1055_client_, d_1051_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_1057_keyring_ = nw27_
                d_1047_children_ = (d_1047_children_) + (_dafny.Seq([d_1057_keyring_]))
        d_1058_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1058_valueOrError6_ = Wrappers.default__.Need(((d_1038_generatorKeyring_).is_Some) or ((len(d_1047_children_)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keyrings needed to create a multi keyring")))
        if (d_1058_valueOrError6_).IsFailure():
            output = (d_1058_valueOrError6_).PropagateFailure()
            return output
        d_1059_keyring_: MultiKeyring.MultiKeyring
        nw28_ = MultiKeyring.MultiKeyring()
        nw28_.ctor__(d_1038_generatorKeyring_, d_1047_children_)
        d_1059_keyring_ = nw28_
        output = Wrappers.Result_Success(d_1059_keyring_)
        return output
        return output

