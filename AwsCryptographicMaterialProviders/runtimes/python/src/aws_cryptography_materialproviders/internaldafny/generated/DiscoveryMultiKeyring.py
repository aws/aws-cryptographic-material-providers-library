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

# assert "DiscoveryMultiKeyring" == __name__
DiscoveryMultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMultiKeyring(regions, discoveryFilter, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        d_946_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_946_valueOrError0_ = Wrappers.default__.Need((len(regions)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No regions passed.")))
        if (d_946_valueOrError0_).IsFailure():
            output = (d_946_valueOrError0_).PropagateFailure()
            return output
        d_947_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_947_valueOrError1_ = Wrappers.default__.Need((Seq.default__.IndexOfOption(regions, _dafny.Seq(""))).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Empty string is not a valid region.")))
        if (d_947_valueOrError1_).IsFailure():
            output = (d_947_valueOrError1_).PropagateFailure()
            return output
        d_948_children_: _dafny.Seq
        d_948_children_ = _dafny.Seq([])
        hi4_: int = len(regions)
        for d_949_i_ in range(0, hi4_):
            d_950_region_: _dafny.Seq
            d_950_region_ = (regions)[d_949_i_]
            d_951_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_952_valueOrError2_: Wrappers.Result = None
            out226_: Wrappers.Result
            out226_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(d_950_region_))
            d_952_valueOrError2_ = out226_
            if (d_952_valueOrError2_).IsFailure():
                output = (d_952_valueOrError2_).PropagateFailure()
                return output
            d_951_client_ = (d_952_valueOrError2_).Extract()
            d_953_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
            nw14_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
            nw14_.ctor__(d_951_client_, discoveryFilter, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_953_keyring_ = nw14_
            d_948_children_ = (d_948_children_) + (_dafny.Seq([d_953_keyring_]))
        d_954_keyring_: MultiKeyring.MultiKeyring
        nw15_ = MultiKeyring.MultiKeyring()
        nw15_.ctor__(Wrappers.Option_None(), d_948_children_)
        d_954_keyring_ = nw15_
        output = Wrappers.Result_Success(d_954_keyring_)
        return output
        return output

