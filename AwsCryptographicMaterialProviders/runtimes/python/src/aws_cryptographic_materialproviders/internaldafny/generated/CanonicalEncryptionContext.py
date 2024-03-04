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

# Module: CanonicalEncryptionContext

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextToAAD(encryptionContext):
        d_392_valueOrError0_ = Wrappers.default__.Need((len(encryptionContext)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context is too large")))
        if (d_392_valueOrError0_).IsFailure():
            return (d_392_valueOrError0_).PropagateFailure()
        elif True:
            d_393_keys_ = StandardLibrary.default__.SetToOrderedSequence((encryptionContext).keys, StandardLibrary_UInt.default__.UInt8Less)
            if (len(d_393_keys_)) == (0):
                return Wrappers.Result_Success(_dafny.Seq([]))
            elif True:
                def lambda42_(d_395_encryptionContext_):
                    def lambda43_(d_396_k_):
                        def iife16_(_pat_let3_0):
                            def iife17_(d_397_v_):
                                def iife18_(_pat_let4_0):
                                    def iife19_(d_398_valueOrError1_):
                                        return ((d_398_valueOrError1_).PropagateFailure() if (d_398_valueOrError1_).IsFailure() else Wrappers.Result_Success((((StandardLibrary_UInt.default__.UInt16ToSeq(len(d_396_k_))) + (d_396_k_)) + (StandardLibrary_UInt.default__.UInt16ToSeq(len(d_397_v_)))) + (d_397_v_)))
                                    return iife19_(_pat_let4_0)
                                return iife18_(Wrappers.default__.Need((StandardLibrary_UInt.default__.HasUint16Len(d_396_k_)) and (StandardLibrary_UInt.default__.HasUint16Len(d_397_v_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to serialize encryption context"))))
                            return iife17_(_pat_let3_0)
                        return iife16_((d_395_encryptionContext_)[d_396_k_])

                    return lambda43_

                d_394_KeyIntoPairBytes_ = lambda42_(encryptionContext)
                d_399_valueOrError2_ = Seq.default__.MapWithResult(d_394_KeyIntoPairBytes_, d_393_keys_)
                if (d_399_valueOrError2_).IsFailure():
                    return (d_399_valueOrError2_).PropagateFailure()
                elif True:
                    d_400_pairsBytes_ = (d_399_valueOrError2_).Extract()
                    d_401_allBytes_ = (StandardLibrary_UInt.default__.UInt16ToSeq(len(d_393_keys_))) + (Seq.default__.Flatten(d_400_pairsBytes_))
                    return Wrappers.Result_Success(d_401_allBytes_)

