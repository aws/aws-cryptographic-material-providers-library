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
import software_amazon_cryptography_primitives_internaldafny_types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
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
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring

# Module: StrictMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv153_ = awsKmsKeys
        pat_let_tv154_ = awsKmsKeys
        d_596_allStrings_: _dafny.Seq
        def lambda57_(source19_):
            if source19_.is_None:
                return (pat_let_tv153_).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_597___mcc_h0_ = source19_.value
                d_598_g_ = d_597___mcc_h0_
                return (_dafny.Seq([d_598_g_])) + ((pat_let_tv154_).UnwrapOr(_dafny.Seq([])))

        d_596_allStrings_ = lambda57_(generator)
        d_599_allIdentifiers_: _dafny.Seq
        d_600_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_600_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_596_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_600_valueOrError0_).IsFailure():
            output = (d_600_valueOrError0_).PropagateFailure()
            return output
        d_599_allIdentifiers_ = (d_600_valueOrError0_).Extract()
        d_601_generatorKeyring_: Wrappers.Option = Wrappers.Option.default()()
        source20_ = generator
        if source20_.is_None:
            d_601_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_602___mcc_h1_ = source20_.value
            d_603_generatorIdentifier_ = d_602___mcc_h1_
            d_604_arn_: AwsArnParsing.AwsKmsIdentifier
            d_605_valueOrError1_: Wrappers.Result = None
            d_605_valueOrError1_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_603_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_605_valueOrError1_).IsFailure():
                output = (d_605_valueOrError1_).PropagateFailure()
                return output
            d_604_arn_ = (d_605_valueOrError1_).Extract()
            d_606_region_: Wrappers.Option
            d_606_region_ = AwsArnParsing.default__.GetRegion(d_604_arn_)
            d_607_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_608_valueOrError2_: Wrappers.Result = None
            out90_: Wrappers.Result
            out90_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_606_region_).UnwrapOr(_dafny.Seq(""))))
            d_608_valueOrError2_ = out90_
            if (d_608_valueOrError2_).IsFailure():
                output = (d_608_valueOrError2_).PropagateFailure()
                return output
            d_607_client_ = (d_608_valueOrError2_).Extract()
            d_609_g_: AwsKmsKeyring.AwsKmsKeyring
            nw6_ = AwsKmsKeyring.AwsKmsKeyring()
            nw6_.ctor__(d_607_client_, d_603_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_609_g_ = nw6_
            d_601_generatorKeyring_ = Wrappers.Option_Some(d_609_g_)
        d_610_children_: _dafny.Seq
        d_610_children_ = _dafny.Seq([])
        source21_ = awsKmsKeys
        if source21_.is_None:
            d_610_children_ = _dafny.Seq([])
        elif True:
            d_611___mcc_h2_ = source21_.value
            d_612_childIdentifiers_ = d_611___mcc_h2_
            hi2_ = len(d_612_childIdentifiers_)
            for d_613_index_ in range(0, hi2_):
                d_614_childIdentifier_: _dafny.Seq
                d_614_childIdentifier_ = (d_612_childIdentifiers_)[d_613_index_]
                d_615_info_: AwsArnParsing.AwsKmsIdentifier
                d_616_valueOrError3_: Wrappers.Result = None
                d_616_valueOrError3_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_614_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_616_valueOrError3_).IsFailure():
                    output = (d_616_valueOrError3_).PropagateFailure()
                    return output
                d_615_info_ = (d_616_valueOrError3_).Extract()
                d_617_region_: Wrappers.Option
                d_617_region_ = AwsArnParsing.default__.GetRegion(d_615_info_)
                d_618_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_619_valueOrError4_: Wrappers.Result = None
                out91_: Wrappers.Result
                out91_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_617_region_).UnwrapOr(_dafny.Seq(""))))
                d_619_valueOrError4_ = out91_
                if (d_619_valueOrError4_).IsFailure():
                    output = (d_619_valueOrError4_).PropagateFailure()
                    return output
                d_618_client_ = (d_619_valueOrError4_).Extract()
                d_620_keyring_: AwsKmsKeyring.AwsKmsKeyring
                nw7_ = AwsKmsKeyring.AwsKmsKeyring()
                nw7_.ctor__(d_618_client_, d_614_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_620_keyring_ = nw7_
                d_610_children_ = (d_610_children_) + (_dafny.Seq([d_620_keyring_]))
        d_621_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_621_valueOrError5_ = Wrappers.default__.Need(((d_601_generatorKeyring_).is_Some) or ((len(d_610_children_)) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keryings needed to create a multi keyring")))
        if (d_621_valueOrError5_).IsFailure():
            output = (d_621_valueOrError5_).PropagateFailure()
            return output
        d_622_keyring_: MultiKeyring.MultiKeyring
        nw8_ = MultiKeyring.MultiKeyring()
        nw8_.ctor__(d_601_generatorKeyring_, d_610_children_)
        d_622_keyring_ = nw8_
        output = Wrappers.Result_Success(d_622_keyring_)
        return output
        return output

