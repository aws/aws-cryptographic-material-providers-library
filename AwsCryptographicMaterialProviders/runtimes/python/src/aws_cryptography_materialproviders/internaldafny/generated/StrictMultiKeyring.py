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

assert "StrictMultiKeyring" == __name__
StrictMultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv30_ = awsKmsKeys
        d_879_allStrings_: _dafny.Seq
        def lambda58_(source23_):
            if source23_.is_None:
                return (awsKmsKeys).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_880___mcc_h0_ = source23_.value
                def iife36_(_pat_let12_0):
                    def iife37_(d_881_g_):
                        return (_dafny.Seq([d_881_g_])) + ((pat_let_tv30_).UnwrapOr(_dafny.Seq([])))
                    return iife37_(_pat_let12_0)
                return iife36_(d_880___mcc_h0_)

        d_879_allStrings_ = lambda58_(generator)
        d_882_allIdentifiers_: _dafny.Seq
        d_883_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_883_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_879_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_883_valueOrError0_).IsFailure():
            output = (d_883_valueOrError0_).PropagateFailure()
            return output
        d_882_allIdentifiers_ = (d_883_valueOrError0_).Extract()
        d_884_generatorKeyring_: Wrappers.Option = Wrappers.Option_None.default()()
        source24_ = generator
        if source24_.is_None:
            d_884_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_885___mcc_h1_ = source24_.value
            d_886_generatorIdentifier_ = d_885___mcc_h1_
            d_887_arn_: AwsArnParsing.AwsKmsIdentifier
            d_888_valueOrError1_: Wrappers.Result = None
            d_888_valueOrError1_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_886_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_888_valueOrError1_).IsFailure():
                output = (d_888_valueOrError1_).PropagateFailure()
                return output
            d_887_arn_ = (d_888_valueOrError1_).Extract()
            d_889_region_: Wrappers.Option
            d_889_region_ = AwsArnParsing.default__.GetRegion(d_887_arn_)
            d_890_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_891_valueOrError2_: Wrappers.Result = None
            out218_: Wrappers.Result
            out218_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_889_region_).UnwrapOr(_dafny.Seq(""))))
            d_891_valueOrError2_ = out218_
            if (d_891_valueOrError2_).IsFailure():
                output = (d_891_valueOrError2_).PropagateFailure()
                return output
            d_890_client_ = (d_891_valueOrError2_).Extract()
            d_892_g_: AwsKmsKeyring.AwsKmsKeyring
            nw7_ = AwsKmsKeyring.AwsKmsKeyring()
            nw7_.ctor__(d_890_client_, d_886_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_892_g_ = nw7_
            d_884_generatorKeyring_ = Wrappers.Option_Some(d_892_g_)
        d_893_children_: _dafny.Seq
        d_893_children_ = _dafny.Seq([])
        source25_ = awsKmsKeys
        if source25_.is_None:
            d_893_children_ = _dafny.Seq([])
        elif True:
            d_894___mcc_h2_ = source25_.value
            d_895_childIdentifiers_ = d_894___mcc_h2_
            hi3_: int = len(d_895_childIdentifiers_)
            for d_896_index_ in range(0, hi3_):
                d_897_childIdentifier_: _dafny.Seq
                d_897_childIdentifier_ = (d_895_childIdentifiers_)[d_896_index_]
                d_898_info_: AwsArnParsing.AwsKmsIdentifier
                d_899_valueOrError3_: Wrappers.Result = None
                d_899_valueOrError3_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_897_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_899_valueOrError3_).IsFailure():
                    output = (d_899_valueOrError3_).PropagateFailure()
                    return output
                d_898_info_ = (d_899_valueOrError3_).Extract()
                d_900_region_: Wrappers.Option
                d_900_region_ = AwsArnParsing.default__.GetRegion(d_898_info_)
                d_901_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_902_valueOrError4_: Wrappers.Result = None
                out219_: Wrappers.Result
                out219_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_900_region_).UnwrapOr(_dafny.Seq(""))))
                d_902_valueOrError4_ = out219_
                if (d_902_valueOrError4_).IsFailure():
                    output = (d_902_valueOrError4_).PropagateFailure()
                    return output
                d_901_client_ = (d_902_valueOrError4_).Extract()
                d_903_keyring_: AwsKmsKeyring.AwsKmsKeyring
                nw8_ = AwsKmsKeyring.AwsKmsKeyring()
                nw8_.ctor__(d_901_client_, d_897_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_903_keyring_ = nw8_
                d_893_children_ = (d_893_children_) + (_dafny.Seq([d_903_keyring_]))
        d_904_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_904_valueOrError5_ = Wrappers.default__.Need(((d_884_generatorKeyring_).is_Some) or ((len(d_893_children_)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keryings needed to create a multi keyring")))
        if (d_904_valueOrError5_).IsFailure():
            output = (d_904_valueOrError5_).PropagateFailure()
            return output
        d_905_keyring_: MultiKeyring.MultiKeyring
        nw9_ = MultiKeyring.MultiKeyring()
        nw9_.ctor__(d_884_generatorKeyring_, d_893_children_)
        d_905_keyring_ = nw9_
        output = Wrappers.Result_Success(d_905_keyring_)
        return output
        return output

