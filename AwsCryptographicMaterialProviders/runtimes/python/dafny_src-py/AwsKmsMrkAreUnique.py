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

assert "AwsKmsMrkAreUnique" == __name__
AwsKmsMrkAreUnique = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AwsKmsMrkAreUnique(identifiers):
        d_478_mrks_ = Seq.default__.Filter(AwsArnParsing.default__.IsMultiRegionAwsKmsIdentifier, identifiers)
        if (len(d_478_mrks_)) == (0):
            return Wrappers.Outcome_Pass()
        elif True:
            d_479_mrkKeyIds_ = Seq.default__.Map(AwsKmsMrkAreUnique.default__.GetKeyId, d_478_mrks_)
            d_480_setMrks_ = Seq.default__.ToSet(d_479_mrkKeyIds_)
            if (len(d_479_mrkKeyIds_)) == (len(d_480_setMrks_)):
                return Wrappers.Outcome_Pass()
            elif True:
                def iife23_():
                    coll9_ = _dafny.Set()
                    compr_9_: _dafny.Seq
                    for compr_9_ in (d_479_mrkKeyIds_).Elements:
                        d_482_x_: _dafny.Seq = compr_9_
                        if ((d_482_x_) in (d_479_mrkKeyIds_)) and (((_dafny.MultiSet(d_479_mrkKeyIds_))[d_482_x_]) >= (1)):
                            coll9_ = coll9_.union(_dafny.Set([d_482_x_]))
                    return _dafny.Set(coll9_)
                d_481_duplicateMrkIds_ = iife23_()

                def lambda39_(d_484_duplicateMrkIds_):
                    def lambda40_(d_485_identifier_):
                        return (AwsKmsMrkAreUnique.default__.GetKeyId(d_485_identifier_)) in (d_484_duplicateMrkIds_)

                    return lambda40_

                d_483_isDuplicate_ = lambda39_(d_481_duplicateMrkIds_)
                def lambda41_(d_487_i_):
                    return (d_487_i_).ToString()

                d_486_identifierToString_ = lambda41_
                d_488_duplicateIdentifiers_ = Seq.default__.Filter(d_483_isDuplicate_, identifiers)
                d_489_duplicates_ = Seq.default__.Map(d_486_identifierToString_, d_488_duplicateIdentifiers_)
                if (len(d_489_duplicates_)) == (0):
                    return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Impossible")))
                elif True:
                    return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("Related multi-Region keys: ")) + (StandardLibrary.default__.Join(d_489_duplicates_, _dafny.Seq(",")))) + (_dafny.Seq("are not allowed."))))

    @staticmethod
    def GetKeyId(identifier):
        source22_ = identifier
        if source22_.is_AwsKmsArnIdentifier:
            d_490___mcc_h0_ = source22_.a
            d_491_a_ = d_490___mcc_h0_
            return ((d_491_a_).resource).value
        elif True:
            d_492___mcc_h1_ = source22_.r
            d_493_i_ = d_492___mcc_h1_
            return (d_493_i_).value

