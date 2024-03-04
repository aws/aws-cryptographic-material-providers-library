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
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.primitives.internaldafny.types
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
import software.amazon.cryptography.keystore.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
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
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
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
        pat_let_tv159_ = awsKmsKeys
        pat_let_tv160_ = awsKmsKeys
        d_729_allStrings_: _dafny.Seq
        def lambda65_(source26_):
            if source26_.is_None:
                return (pat_let_tv159_).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_730___mcc_h0_ = source26_.value
                d_731_g_ = d_730___mcc_h0_
                return (_dafny.Seq([d_731_g_])) + ((pat_let_tv160_).UnwrapOr(_dafny.Seq([])))

        d_729_allStrings_ = lambda65_(generator)
        d_732_allIdentifiers_: _dafny.Seq
        d_733_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_733_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_729_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_733_valueOrError0_).IsFailure():
            output = (d_733_valueOrError0_).PropagateFailure()
            return output
        d_732_allIdentifiers_ = (d_733_valueOrError0_).Extract()
        d_734_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_734_valueOrError1_ = AwsKmsMrkAreUnique.default__.AwsKmsMrkAreUnique(d_732_allIdentifiers_)
        if (d_734_valueOrError1_).IsFailure():
            output = (d_734_valueOrError1_).PropagateFailure()
            return output
        d_735_generatorKeyring_: Wrappers.Option = Wrappers.Option.default()()
        source27_ = generator
        if source27_.is_None:
            d_735_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_736___mcc_h1_ = source27_.value
            d_737_generatorIdentifier_ = d_736___mcc_h1_
            d_738_arn_: AwsArnParsing.AwsKmsIdentifier
            d_739_valueOrError2_: Wrappers.Result = None
            d_739_valueOrError2_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_737_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_739_valueOrError2_).IsFailure():
                output = (d_739_valueOrError2_).PropagateFailure()
                return output
            d_738_arn_ = (d_739_valueOrError2_).Extract()
            d_740_region_: Wrappers.Option
            d_740_region_ = AwsArnParsing.default__.GetRegion(d_738_arn_)
            d_741_client_: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient
            d_742_valueOrError3_: Wrappers.Result = None
            out111_: Wrappers.Result
            out111_ = (clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput_GetClientInput((d_740_region_).UnwrapOr(_dafny.Seq(""))))
            d_742_valueOrError3_ = out111_
            if (d_742_valueOrError3_).IsFailure():
                output = (d_742_valueOrError3_).PropagateFailure()
                return output
            d_741_client_ = (d_742_valueOrError3_).Extract()
            d_743_g_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
            nw25_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
            nw25_.ctor__(d_741_client_, d_737_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_743_g_ = nw25_
            d_735_generatorKeyring_ = Wrappers.Option_Some(d_743_g_)
        d_744_children_: _dafny.Seq
        d_744_children_ = _dafny.Seq([])
        source28_ = awsKmsKeys
        if source28_.is_None:
            d_744_children_ = _dafny.Seq([])
        elif True:
            d_745___mcc_h2_ = source28_.value
            d_746_childIdentifiers_ = d_745___mcc_h2_
            hi5_ = len(d_746_childIdentifiers_)
            for d_747_index_ in range(0, hi5_):
                d_748_childIdentifier_: _dafny.Seq
                d_748_childIdentifier_ = (d_746_childIdentifiers_)[d_747_index_]
                d_749_info_: AwsArnParsing.AwsKmsIdentifier
                d_750_valueOrError4_: Wrappers.Result = None
                d_750_valueOrError4_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_748_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_750_valueOrError4_).IsFailure():
                    output = (d_750_valueOrError4_).PropagateFailure()
                    return output
                d_749_info_ = (d_750_valueOrError4_).Extract()
                d_751_region_: Wrappers.Option
                d_751_region_ = AwsArnParsing.default__.GetRegion(d_749_info_)
                d_752_client_: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient
                d_753_valueOrError5_: Wrappers.Result = None
                out112_: Wrappers.Result
                out112_ = (clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput_GetClientInput((d_751_region_).UnwrapOr(_dafny.Seq(""))))
                d_753_valueOrError5_ = out112_
                if (d_753_valueOrError5_).IsFailure():
                    output = (d_753_valueOrError5_).PropagateFailure()
                    return output
                d_752_client_ = (d_753_valueOrError5_).Extract()
                d_754_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                nw26_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                nw26_.ctor__(d_752_client_, d_748_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_754_keyring_ = nw26_
                d_744_children_ = (d_744_children_) + (_dafny.Seq([d_754_keyring_]))
        d_755_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_755_valueOrError6_ = Wrappers.default__.Need(((d_735_generatorKeyring_).is_Some) or ((len(d_744_children_)) > (0)), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keyrings needed to create a multi keyring")))
        if (d_755_valueOrError6_).IsFailure():
            output = (d_755_valueOrError6_).PropagateFailure()
            return output
        d_756_keyring_: MultiKeyring.MultiKeyring
        nw27_ = MultiKeyring.MultiKeyring()
        nw27_.ctor__(d_735_generatorKeyring_, d_744_children_)
        d_756_keyring_ = nw27_
        output = Wrappers.Result_Success(d_756_keyring_)
        return output
        return output

