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
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
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
import UUID
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

# Module: DiscoveryMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMultiKeyring(regions, discoveryFilter, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        d_641_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_641_valueOrError0_ = Wrappers.default__.Need((len(regions)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No regions passed.")))
        if (d_641_valueOrError0_).IsFailure():
            output = (d_641_valueOrError0_).PropagateFailure()
            return output
        d_642_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_642_valueOrError1_ = Wrappers.default__.Need((Seq.default__.IndexOfOption(regions, _dafny.Seq(""))).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Empty string is not a valid region.")))
        if (d_642_valueOrError1_).IsFailure():
            output = (d_642_valueOrError1_).PropagateFailure()
            return output
        d_643_children_: _dafny.Seq
        d_643_children_ = _dafny.Seq([])
        hi3_ = len(regions)
        for d_644_i_ in range(0, hi3_):
            d_645_region_: _dafny.Seq
            d_645_region_ = (regions)[d_644_i_]
            d_646_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_647_valueOrError2_: Wrappers.Result = None
            out98_: Wrappers.Result
            out98_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(d_645_region_))
            d_647_valueOrError2_ = out98_
            if (d_647_valueOrError2_).IsFailure():
                output = (d_647_valueOrError2_).PropagateFailure()
                return output
            d_646_client_ = (d_647_valueOrError2_).Extract()
            d_648_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
            nw13_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
            nw13_.ctor__(d_646_client_, discoveryFilter, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_648_keyring_ = nw13_
            d_643_children_ = (d_643_children_) + (_dafny.Seq([d_648_keyring_]))
        d_649_keyring_: MultiKeyring.MultiKeyring
        nw14_ = MultiKeyring.MultiKeyring()
        nw14_.ctor__(Wrappers.Option_None(), d_643_children_)
        d_649_keyring_ = nw14_
        output = Wrappers.Result_Success(d_649_keyring_)
        return output
        return output

