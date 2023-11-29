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

assert "StrictMultiKeyring" == __name__
StrictMultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv30_ = awsKmsKeys
        d_680_allStrings_: _dafny.Seq
        def lambda57_(source23_):
            if source23_.is_None:
                return (awsKmsKeys).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_681___mcc_h0_ = source23_.value
                def iife32_(_pat_let11_0):
                    def iife33_(d_682_g_):
                        return (_dafny.Seq([d_682_g_])) + ((pat_let_tv30_).UnwrapOr(_dafny.Seq([])))
                    return iife33_(_pat_let11_0)
                return iife32_(d_681___mcc_h0_)

        d_680_allStrings_ = lambda57_(generator)
        d_683_allIdentifiers_: _dafny.Seq
        d_684_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_684_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_680_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_684_valueOrError0_).IsFailure():
            output = (d_684_valueOrError0_).PropagateFailure()
            return output
        d_683_allIdentifiers_ = (d_684_valueOrError0_).Extract()
        d_685_generatorKeyring_: Wrappers.Option = Wrappers.Option_None.default()()
        source24_ = generator
        if source24_.is_None:
            d_685_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_686___mcc_h1_ = source24_.value
            d_687_generatorIdentifier_ = d_686___mcc_h1_
            d_688_arn_: AwsArnParsing.AwsKmsIdentifier
            d_689_valueOrError1_: Wrappers.Result = None
            d_689_valueOrError1_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_687_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_689_valueOrError1_).IsFailure():
                output = (d_689_valueOrError1_).PropagateFailure()
                return output
            d_688_arn_ = (d_689_valueOrError1_).Extract()
            d_690_region_: Wrappers.Option
            d_690_region_ = AwsArnParsing.default__.GetRegion(d_688_arn_)
            d_691_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_692_valueOrError2_: Wrappers.Result = None
            out141_: Wrappers.Result
            out141_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_690_region_).UnwrapOr(_dafny.Seq(""))))
            d_692_valueOrError2_ = out141_
            if (d_692_valueOrError2_).IsFailure():
                output = (d_692_valueOrError2_).PropagateFailure()
                return output
            d_691_client_ = (d_692_valueOrError2_).Extract()
            d_693_g_: AwsKmsKeyring.AwsKmsKeyring
            nw7_ = AwsKmsKeyring.AwsKmsKeyring()
            nw7_.ctor__(d_691_client_, d_687_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_693_g_ = nw7_
            d_685_generatorKeyring_ = Wrappers.Option_Some(d_693_g_)
        d_694_children_: _dafny.Seq
        d_694_children_ = _dafny.Seq([])
        source25_ = awsKmsKeys
        if source25_.is_None:
            d_694_children_ = _dafny.Seq([])
        elif True:
            d_695___mcc_h2_ = source25_.value
            d_696_childIdentifiers_ = d_695___mcc_h2_
            hi3_: int = len(d_696_childIdentifiers_)
            for d_697_index_ in range(0, hi3_):
                d_698_childIdentifier_: _dafny.Seq
                d_698_childIdentifier_ = (d_696_childIdentifiers_)[d_697_index_]
                d_699_info_: AwsArnParsing.AwsKmsIdentifier
                d_700_valueOrError3_: Wrappers.Result = None
                d_700_valueOrError3_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_698_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_700_valueOrError3_).IsFailure():
                    output = (d_700_valueOrError3_).PropagateFailure()
                    return output
                d_699_info_ = (d_700_valueOrError3_).Extract()
                d_701_region_: Wrappers.Option
                d_701_region_ = AwsArnParsing.default__.GetRegion(d_699_info_)
                d_702_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_703_valueOrError4_: Wrappers.Result = None
                out142_: Wrappers.Result
                out142_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_701_region_).UnwrapOr(_dafny.Seq(""))))
                d_703_valueOrError4_ = out142_
                if (d_703_valueOrError4_).IsFailure():
                    output = (d_703_valueOrError4_).PropagateFailure()
                    return output
                d_702_client_ = (d_703_valueOrError4_).Extract()
                d_704_keyring_: AwsKmsKeyring.AwsKmsKeyring
                nw8_ = AwsKmsKeyring.AwsKmsKeyring()
                nw8_.ctor__(d_702_client_, d_698_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_704_keyring_ = nw8_
                d_694_children_ = (d_694_children_) + (_dafny.Seq([d_704_keyring_]))
        d_705_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_705_valueOrError5_ = Wrappers.default__.Need(((d_685_generatorKeyring_).is_Some) or ((len(d_694_children_)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keryings needed to create a multi keyring")))
        if (d_705_valueOrError5_).IsFailure():
            output = (d_705_valueOrError5_).PropagateFailure()
            return output
        d_706_keyring_: MultiKeyring.MultiKeyring
        nw9_ = MultiKeyring.MultiKeyring()
        nw9_.ctor__(d_685_generatorKeyring_, d_694_children_)
        d_706_keyring_ = nw9_
        output = Wrappers.Result_Success(d_706_keyring_)
        return output
        return output

