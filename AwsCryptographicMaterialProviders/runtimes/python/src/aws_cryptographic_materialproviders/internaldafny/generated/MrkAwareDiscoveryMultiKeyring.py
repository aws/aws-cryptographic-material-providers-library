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
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring

# Module: MrkAwareDiscoveryMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MrkAwareDiscoveryMultiKeyring(regions, discoveryFilter, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        d_703_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_703_valueOrError0_ = Wrappers.default__.Need((len(regions)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No regions passed.")))
        if (d_703_valueOrError0_).IsFailure():
            output = (d_703_valueOrError0_).PropagateFailure()
            return output
        d_704_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_704_valueOrError1_ = Wrappers.default__.Need((Seq.default__.IndexOfOption(regions, _dafny.Seq(""))).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Empty string is not a valid region.")))
        if (d_704_valueOrError1_).IsFailure():
            output = (d_704_valueOrError1_).PropagateFailure()
            return output
        d_705_children_: _dafny.Seq
        d_705_children_ = _dafny.Seq([])
        hi4_ = len(regions)
        for d_706_i_ in range(0, hi4_):
            d_707_region_: _dafny.Seq
            d_707_region_ = (regions)[d_706_i_]
            d_708_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_709_valueOrError2_: Wrappers.Result = None
            out104_: Wrappers.Result
            out104_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(d_707_region_))
            d_709_valueOrError2_ = out104_
            if (d_709_valueOrError2_).IsFailure():
                output = (d_709_valueOrError2_).PropagateFailure()
                return output
            d_708_client_ = (d_709_valueOrError2_).Extract()
            d_710_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
            nw18_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
            nw18_.ctor__(d_708_client_, d_707_region_, discoveryFilter, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_710_keyring_ = nw18_
            d_705_children_ = (d_705_children_) + (_dafny.Seq([d_710_keyring_]))
        d_711_keyring_: MultiKeyring.MultiKeyring
        nw19_ = MultiKeyring.MultiKeyring()
        nw19_.ctor__(Wrappers.Option_None(), d_705_children_)
        d_711_keyring_ = nw19_
        output = Wrappers.Result_Success(d_711_keyring_)
        return output
        return output

