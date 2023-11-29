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

# assert "CanonicalEncryptionContext" == __name__
CanonicalEncryptionContext = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextToAAD(encryptionContext):
        d_697_valueOrError0_ = Wrappers.default__.Need((len(encryptionContext)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context is too large")))
        if (d_697_valueOrError0_).IsFailure():
            return (d_697_valueOrError0_).PropagateFailure()
        elif True:
            d_698_keys_ = StandardLibrary.default__.SetToOrderedSequence((encryptionContext).keys, StandardLibrary_mUInt.default__.UInt8Less)
            if (len(d_698_keys_)) == (0):
                return Wrappers.Result_Success(_dafny.Seq([]))
            elif True:
                def lambda43_(d_700_encryptionContext_):
                    def lambda44_(d_701_k_):
                        def iife28_(_pat_let8_0):
                            def iife29_(d_702_v_):
                                def iife30_(_pat_let9_0):
                                    def iife31_(d_703_valueOrError1_):
                                        return ((d_703_valueOrError1_).PropagateFailure() if (d_703_valueOrError1_).IsFailure() else Wrappers.Result_Success((((StandardLibrary_mUInt.default__.UInt16ToSeq(len(d_701_k_))) + (d_701_k_)) + (StandardLibrary_mUInt.default__.UInt16ToSeq(len(d_702_v_)))) + (d_702_v_)))
                                    return iife31_(_pat_let9_0)
                                return iife30_(Wrappers.default__.Need((StandardLibrary_mUInt.default__.HasUint16Len(d_701_k_)) and (StandardLibrary_mUInt.default__.HasUint16Len(d_702_v_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to serialize encryption context"))))
                            return iife29_(_pat_let8_0)
                        return iife28_((d_700_encryptionContext_)[d_701_k_])

                    return lambda44_

                d_699_KeyIntoPairBytes_ = lambda43_(encryptionContext)
                d_704_valueOrError2_ = Seq.default__.MapWithResult(d_699_KeyIntoPairBytes_, d_698_keys_)
                if (d_704_valueOrError2_).IsFailure():
                    return (d_704_valueOrError2_).PropagateFailure()
                elif True:
                    d_705_pairsBytes_ = (d_704_valueOrError2_).Extract()
                    d_706_allBytes_ = (StandardLibrary_mUInt.default__.UInt16ToSeq(len(d_698_keys_))) + (Seq.default__.Flatten(d_705_pairsBytes_))
                    return Wrappers.Result_Success(d_706_allBytes_)

