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
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring

# assert "MrkAwareDiscoveryMultiKeyring" == __name__
MrkAwareDiscoveryMultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MrkAwareDiscoveryMultiKeyring(regions, discoveryFilter, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        d_986_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_986_valueOrError0_ = Wrappers.default__.Need((len(regions)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No regions passed.")))
        if (d_986_valueOrError0_).IsFailure():
            output = (d_986_valueOrError0_).PropagateFailure()
            return output
        d_987_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_987_valueOrError1_ = Wrappers.default__.Need((Seq.default__.IndexOfOption(regions, _dafny.Seq(""))).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Empty string is not a valid region.")))
        if (d_987_valueOrError1_).IsFailure():
            output = (d_987_valueOrError1_).PropagateFailure()
            return output
        d_988_children_: _dafny.Seq
        d_988_children_ = _dafny.Seq([])
        hi5_: int = len(regions)
        for d_989_i_ in range(0, hi5_):
            d_990_region_: _dafny.Seq
            d_990_region_ = (regions)[d_989_i_]
            d_991_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_992_valueOrError2_: Wrappers.Result = None
            out232_: Wrappers.Result
            out232_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(d_990_region_))
            d_992_valueOrError2_ = out232_
            if (d_992_valueOrError2_).IsFailure():
                output = (d_992_valueOrError2_).PropagateFailure()
                return output
            d_991_client_ = (d_992_valueOrError2_).Extract()
            d_993_keyring_: AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
            nw19_ = AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring()
            nw19_.ctor__(d_991_client_, d_990_region_, discoveryFilter, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_993_keyring_ = nw19_
            d_988_children_ = (d_988_children_) + (_dafny.Seq([d_993_keyring_]))
        d_994_keyring_: MultiKeyring.MultiKeyring
        nw20_ = MultiKeyring.MultiKeyring()
        nw20_.ctor__(Wrappers.Option_None(), d_988_children_)
        d_994_keyring_ = nw20_
        output = Wrappers.Result_Success(d_994_keyring_)
        return output
        return output

