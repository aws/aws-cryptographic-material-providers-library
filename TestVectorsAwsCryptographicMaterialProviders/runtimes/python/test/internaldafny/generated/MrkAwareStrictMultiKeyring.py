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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
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
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring

# Module: MrkAwareStrictMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MrkAwareStrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv35_ = awsKmsKeys
        d_646_allStrings_: _dafny.Seq
        def lambda43_(source28_):
            if source28_.is_None:
                return (awsKmsKeys).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_647___mcc_h0_ = source28_.value
                def iife37_(_pat_let17_0):
                    def iife38_(d_648_g_):
                        return (_dafny.Seq([d_648_g_])) + ((pat_let_tv35_).UnwrapOr(_dafny.Seq([])))
                    return iife38_(_pat_let17_0)
                return iife37_(d_647___mcc_h0_)

        d_646_allStrings_ = lambda43_(generator)
        d_649_allIdentifiers_: _dafny.Seq
        d_650_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_650_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_646_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_650_valueOrError0_).IsFailure():
            output = (d_650_valueOrError0_).PropagateFailure()
            return output
        d_649_allIdentifiers_ = (d_650_valueOrError0_).Extract()
        d_651_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_651_valueOrError1_ = AwsKmsMrkAreUnique.default__.AwsKmsMrkAreUnique(d_649_allIdentifiers_)
        if (d_651_valueOrError1_).IsFailure():
            output = (d_651_valueOrError1_).PropagateFailure()
            return output
        d_652_generatorKeyring_: Wrappers.Option = Wrappers.Option.default()()
        source29_ = generator
        if source29_.is_None:
            d_652_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_653___mcc_h1_ = source29_.value
            d_654_generatorIdentifier_ = d_653___mcc_h1_
            d_655_arn_: AwsArnParsing.AwsKmsIdentifier
            d_656_valueOrError2_: Wrappers.Result = None
            d_656_valueOrError2_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_654_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_656_valueOrError2_).IsFailure():
                output = (d_656_valueOrError2_).PropagateFailure()
                return output
            d_655_arn_ = (d_656_valueOrError2_).Extract()
            d_657_region_: Wrappers.Option
            d_657_region_ = AwsArnParsing.default__.GetRegion(d_655_arn_)
            d_658_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_659_valueOrError3_: Wrappers.Result = None
            out118_: Wrappers.Result
            out118_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_657_region_).UnwrapOr(_dafny.Seq(""))))
            d_659_valueOrError3_ = out118_
            if (d_659_valueOrError3_).IsFailure():
                output = (d_659_valueOrError3_).PropagateFailure()
                return output
            d_658_client_ = (d_659_valueOrError3_).Extract()
            d_660_g_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
            nw25_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
            nw25_.ctor__(d_658_client_, d_654_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_660_g_ = nw25_
            d_652_generatorKeyring_ = Wrappers.Option_Some(d_660_g_)
        d_661_children_: _dafny.Seq
        d_661_children_ = _dafny.Seq([])
        source30_ = awsKmsKeys
        if source30_.is_None:
            d_661_children_ = _dafny.Seq([])
        elif True:
            d_662___mcc_h2_ = source30_.value
            d_663_childIdentifiers_ = d_662___mcc_h2_
            hi6_ = len(d_663_childIdentifiers_)
            for d_664_index_ in range(0, hi6_):
                d_665_childIdentifier_: _dafny.Seq
                d_665_childIdentifier_ = (d_663_childIdentifiers_)[d_664_index_]
                d_666_info_: AwsArnParsing.AwsKmsIdentifier
                d_667_valueOrError4_: Wrappers.Result = None
                d_667_valueOrError4_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_665_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_667_valueOrError4_).IsFailure():
                    output = (d_667_valueOrError4_).PropagateFailure()
                    return output
                d_666_info_ = (d_667_valueOrError4_).Extract()
                d_668_region_: Wrappers.Option
                d_668_region_ = AwsArnParsing.default__.GetRegion(d_666_info_)
                d_669_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_670_valueOrError5_: Wrappers.Result = None
                out119_: Wrappers.Result
                out119_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_668_region_).UnwrapOr(_dafny.Seq(""))))
                d_670_valueOrError5_ = out119_
                if (d_670_valueOrError5_).IsFailure():
                    output = (d_670_valueOrError5_).PropagateFailure()
                    return output
                d_669_client_ = (d_670_valueOrError5_).Extract()
                d_671_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                nw26_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                nw26_.ctor__(d_669_client_, d_665_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_671_keyring_ = nw26_
                d_661_children_ = (d_661_children_) + (_dafny.Seq([d_671_keyring_]))
        d_672_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_672_valueOrError6_ = Wrappers.default__.Need(((d_652_generatorKeyring_).is_Some) or ((len(d_661_children_)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keyrings needed to create a multi keyring")))
        if (d_672_valueOrError6_).IsFailure():
            output = (d_672_valueOrError6_).PropagateFailure()
            return output
        d_673_keyring_: MultiKeyring.MultiKeyring
        nw27_ = MultiKeyring.MultiKeyring()
        nw27_.ctor__(d_652_generatorKeyring_, d_661_children_)
        d_673_keyring_ = nw27_
        output = Wrappers.Result_Success(d_673_keyring_)
        return output
        return output

