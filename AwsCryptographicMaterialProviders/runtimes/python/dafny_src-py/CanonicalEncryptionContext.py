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

assert "CanonicalEncryptionContext" == __name__
CanonicalEncryptionContext = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextToAAD(encryptionContext):
        d_498_valueOrError0_ = Wrappers.default__.Need((len(encryptionContext)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context is too large")))
        if (d_498_valueOrError0_).IsFailure():
            return (d_498_valueOrError0_).PropagateFailure()
        elif True:
            d_499_keys_ = StandardLibrary.default__.SetToOrderedSequence((encryptionContext).keys, StandardLibrary_mUInt.default__.UInt8Less)
            if (len(d_499_keys_)) == (0):
                return Wrappers.Result_Success(_dafny.Seq([]))
            elif True:
                def lambda42_(d_501_encryptionContext_):
                    def lambda43_(d_502_k_):
                        def iife24_(_pat_let7_0):
                            def iife25_(d_503_v_):
                                def iife26_(_pat_let8_0):
                                    def iife27_(d_504_valueOrError1_):
                                        return ((d_504_valueOrError1_).PropagateFailure() if (d_504_valueOrError1_).IsFailure() else Wrappers.Result_Success((((StandardLibrary_mUInt.default__.UInt16ToSeq(len(d_502_k_))) + (d_502_k_)) + (StandardLibrary_mUInt.default__.UInt16ToSeq(len(d_503_v_)))) + (d_503_v_)))
                                    return iife27_(_pat_let8_0)
                                return iife26_(Wrappers.default__.Need((StandardLibrary_mUInt.default__.HasUint16Len(d_502_k_)) and (StandardLibrary_mUInt.default__.HasUint16Len(d_503_v_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to serialize encryption context"))))
                            return iife25_(_pat_let7_0)
                        return iife24_((d_501_encryptionContext_)[d_502_k_])

                    return lambda43_

                d_500_KeyIntoPairBytes_ = lambda42_(encryptionContext)
                d_505_valueOrError2_ = Seq.default__.MapWithResult(d_500_KeyIntoPairBytes_, d_499_keys_)
                if (d_505_valueOrError2_).IsFailure():
                    return (d_505_valueOrError2_).PropagateFailure()
                elif True:
                    d_506_pairsBytes_ = (d_505_valueOrError2_).Extract()
                    d_507_allBytes_ = (StandardLibrary_mUInt.default__.UInt16ToSeq(len(d_499_keys_))) + (Seq.default__.Flatten(d_506_pairsBytes_))
                    return Wrappers.Result_Success(d_507_allBytes_)

