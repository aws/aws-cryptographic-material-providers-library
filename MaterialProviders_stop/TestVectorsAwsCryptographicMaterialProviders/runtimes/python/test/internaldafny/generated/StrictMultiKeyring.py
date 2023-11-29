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

assert "StrictMultiKeyring" == __name__
StrictMultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv30_ = awsKmsKeys
        d_492_allStrings_: _dafny.Seq
        def lambda35_(source21_):
            if source21_.is_None:
                return (awsKmsKeys).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_493___mcc_h0_ = source21_.value
                def iife23_(_pat_let10_0):
                    def iife24_(d_494_g_):
                        return (_dafny.Seq([d_494_g_])) + ((pat_let_tv30_).UnwrapOr(_dafny.Seq([])))
                    return iife24_(_pat_let10_0)
                return iife23_(d_493___mcc_h0_)

        d_492_allStrings_ = lambda35_(generator)
        d_495_allIdentifiers_: _dafny.Seq
        d_496_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_496_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_492_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_496_valueOrError0_).IsFailure():
            output = (d_496_valueOrError0_).PropagateFailure()
            return output
        d_495_allIdentifiers_ = (d_496_valueOrError0_).Extract()
        d_497_generatorKeyring_: Wrappers.Option = Wrappers.Option_None.default()()
        source22_ = generator
        if source22_.is_None:
            d_497_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_498___mcc_h1_ = source22_.value
            d_499_generatorIdentifier_ = d_498___mcc_h1_
            d_500_arn_: AwsArnParsing.AwsKmsIdentifier
            d_501_valueOrError1_: Wrappers.Result = None
            d_501_valueOrError1_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_499_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_501_valueOrError1_).IsFailure():
                output = (d_501_valueOrError1_).PropagateFailure()
                return output
            d_500_arn_ = (d_501_valueOrError1_).Extract()
            d_502_region_: Wrappers.Option
            d_502_region_ = AwsArnParsing.default__.GetRegion(d_500_arn_)
            d_503_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_504_valueOrError2_: Wrappers.Result = None
            out97_: Wrappers.Result
            out97_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_502_region_).UnwrapOr(_dafny.Seq(""))))
            d_504_valueOrError2_ = out97_
            if (d_504_valueOrError2_).IsFailure():
                output = (d_504_valueOrError2_).PropagateFailure()
                return output
            d_503_client_ = (d_504_valueOrError2_).Extract()
            d_505_g_: AwsKmsKeyring.AwsKmsKeyring
            nw6_ = AwsKmsKeyring.AwsKmsKeyring()
            nw6_.ctor__(d_503_client_, d_499_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_505_g_ = nw6_
            d_497_generatorKeyring_ = Wrappers.Option_Some(d_505_g_)
        d_506_children_: _dafny.Seq
        d_506_children_ = _dafny.Seq([])
        source23_ = awsKmsKeys
        if source23_.is_None:
            d_506_children_ = _dafny.Seq([])
        elif True:
            d_507___mcc_h2_ = source23_.value
            d_508_childIdentifiers_ = d_507___mcc_h2_
            hi3_: int = len(d_508_childIdentifiers_)
            for d_509_index_ in range(0, hi3_):
                d_510_childIdentifier_: _dafny.Seq
                d_510_childIdentifier_ = (d_508_childIdentifiers_)[d_509_index_]
                d_511_info_: AwsArnParsing.AwsKmsIdentifier
                d_512_valueOrError3_: Wrappers.Result = None
                d_512_valueOrError3_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_510_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_512_valueOrError3_).IsFailure():
                    output = (d_512_valueOrError3_).PropagateFailure()
                    return output
                d_511_info_ = (d_512_valueOrError3_).Extract()
                d_513_region_: Wrappers.Option
                d_513_region_ = AwsArnParsing.default__.GetRegion(d_511_info_)
                d_514_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_515_valueOrError4_: Wrappers.Result = None
                out98_: Wrappers.Result
                out98_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_513_region_).UnwrapOr(_dafny.Seq(""))))
                d_515_valueOrError4_ = out98_
                if (d_515_valueOrError4_).IsFailure():
                    output = (d_515_valueOrError4_).PropagateFailure()
                    return output
                d_514_client_ = (d_515_valueOrError4_).Extract()
                d_516_keyring_: AwsKmsKeyring.AwsKmsKeyring
                nw7_ = AwsKmsKeyring.AwsKmsKeyring()
                nw7_.ctor__(d_514_client_, d_510_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_516_keyring_ = nw7_
                d_506_children_ = (d_506_children_) + (_dafny.Seq([d_516_keyring_]))
        d_517_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_517_valueOrError5_ = Wrappers.default__.Need(((d_497_generatorKeyring_).is_Some) or ((len(d_506_children_)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keryings needed to create a multi keyring")))
        if (d_517_valueOrError5_).IsFailure():
            output = (d_517_valueOrError5_).PropagateFailure()
            return output
        d_518_keyring_: MultiKeyring.MultiKeyring
        nw8_ = MultiKeyring.MultiKeyring()
        nw8_.ctor__(d_497_generatorKeyring_, d_506_children_)
        d_518_keyring_ = nw8_
        output = Wrappers.Result_Success(d_518_keyring_)
        return output
        return output

