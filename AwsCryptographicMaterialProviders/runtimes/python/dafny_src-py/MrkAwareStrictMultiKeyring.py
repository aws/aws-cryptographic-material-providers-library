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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny
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
        d_833_allStrings_: _dafny.Seq
        def lambda65_(source30_):
            if source30_.is_None:
                return (awsKmsKeys).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_834___mcc_h0_ = source30_.value
                def iife46_(_pat_let18_0):
                    def iife47_(d_835_g_):
                        return (_dafny.Seq([d_835_g_])) + ((pat_let_tv35_).UnwrapOr(_dafny.Seq([])))
                    return iife47_(_pat_let18_0)
                return iife46_(d_834___mcc_h0_)

        d_833_allStrings_ = lambda65_(generator)
        d_836_allIdentifiers_: _dafny.Seq
        d_837_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_837_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_833_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_837_valueOrError0_).IsFailure():
            output = (d_837_valueOrError0_).PropagateFailure()
            return output
        d_836_allIdentifiers_ = (d_837_valueOrError0_).Extract()
        d_838_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_838_valueOrError1_ = AwsKmsMrkAreUnique.default__.AwsKmsMrkAreUnique(d_836_allIdentifiers_)
        if (d_838_valueOrError1_).IsFailure():
            output = (d_838_valueOrError1_).PropagateFailure()
            return output
        d_839_generatorKeyring_: Wrappers.Option = Wrappers.Option_None.default()()
        source31_ = generator
        if source31_.is_None:
            d_839_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_840___mcc_h1_ = source31_.value
            d_841_generatorIdentifier_ = d_840___mcc_h1_
            d_842_arn_: AwsArnParsing.AwsKmsIdentifier
            d_843_valueOrError2_: Wrappers.Result = None
            d_843_valueOrError2_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_841_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_843_valueOrError2_).IsFailure():
                output = (d_843_valueOrError2_).PropagateFailure()
                return output
            d_842_arn_ = (d_843_valueOrError2_).Extract()
            d_844_region_: Wrappers.Option
            d_844_region_ = AwsArnParsing.default__.GetRegion(d_842_arn_)
            d_845_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_846_valueOrError3_: Wrappers.Result = None
            out162_: Wrappers.Result
            out162_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_844_region_).UnwrapOr(_dafny.Seq(""))))
            d_846_valueOrError3_ = out162_
            if (d_846_valueOrError3_).IsFailure():
                output = (d_846_valueOrError3_).PropagateFailure()
                return output
            d_845_client_ = (d_846_valueOrError3_).Extract()
            d_847_g_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
            nw26_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
            nw26_.ctor__(d_845_client_, d_841_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_847_g_ = nw26_
            d_839_generatorKeyring_ = Wrappers.Option_Some(d_847_g_)
        d_848_children_: _dafny.Seq
        d_848_children_ = _dafny.Seq([])
        source32_ = awsKmsKeys
        if source32_.is_None:
            d_848_children_ = _dafny.Seq([])
        elif True:
            d_849___mcc_h2_ = source32_.value
            d_850_childIdentifiers_ = d_849___mcc_h2_
            hi6_: int = len(d_850_childIdentifiers_)
            for d_851_index_ in range(0, hi6_):
                d_852_childIdentifier_: _dafny.Seq
                d_852_childIdentifier_ = (d_850_childIdentifiers_)[d_851_index_]
                d_853_info_: AwsArnParsing.AwsKmsIdentifier
                d_854_valueOrError4_: Wrappers.Result = None
                d_854_valueOrError4_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_852_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_854_valueOrError4_).IsFailure():
                    output = (d_854_valueOrError4_).PropagateFailure()
                    return output
                d_853_info_ = (d_854_valueOrError4_).Extract()
                d_855_region_: Wrappers.Option
                d_855_region_ = AwsArnParsing.default__.GetRegion(d_853_info_)
                d_856_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_857_valueOrError5_: Wrappers.Result = None
                out163_: Wrappers.Result
                out163_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_855_region_).UnwrapOr(_dafny.Seq(""))))
                d_857_valueOrError5_ = out163_
                if (d_857_valueOrError5_).IsFailure():
                    output = (d_857_valueOrError5_).PropagateFailure()
                    return output
                d_856_client_ = (d_857_valueOrError5_).Extract()
                d_858_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                nw27_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                nw27_.ctor__(d_856_client_, d_852_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_858_keyring_ = nw27_
                d_848_children_ = (d_848_children_) + (_dafny.Seq([d_858_keyring_]))
        d_859_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_859_valueOrError6_ = Wrappers.default__.Need(((d_839_generatorKeyring_).is_Some) or ((len(d_848_children_)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keyrings needed to create a multi keyring")))
        if (d_859_valueOrError6_).IsFailure():
            output = (d_859_valueOrError6_).PropagateFailure()
            return output
        d_860_keyring_: MultiKeyring.MultiKeyring
        nw28_ = MultiKeyring.MultiKeyring()
        nw28_.ctor__(d_839_generatorKeyring_, d_848_children_)
        d_860_keyring_ = nw28_
        output = Wrappers.Result_Success(d_860_keyring_)
        return output
        return output

