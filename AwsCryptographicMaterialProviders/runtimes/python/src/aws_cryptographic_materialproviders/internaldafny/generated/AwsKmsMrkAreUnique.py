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

# Module: AwsKmsMrkAreUnique

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AwsKmsMrkAreUnique(identifiers):
        d_373_mrks_ = Seq.default__.Filter(AwsArnParsing.default__.IsMultiRegionAwsKmsIdentifier, identifiers)
        if (len(d_373_mrks_)) == (0):
            return Wrappers.Outcome_Pass()
        elif True:
            d_374_mrkKeyIds_ = Seq.default__.Map(default__.GetKeyId, d_373_mrks_)
            d_375_setMrks_ = Seq.default__.ToSet(d_374_mrkKeyIds_)
            if (len(d_374_mrkKeyIds_)) == (len(d_375_setMrks_)):
                return Wrappers.Outcome_Pass()
            elif True:
                def iife15_():
                    coll9_ = _dafny.Set()
                    compr_9_: _dafny.Seq
                    for compr_9_ in (d_374_mrkKeyIds_).Elements:
                        d_377_x_: _dafny.Seq = compr_9_
                        if ((d_377_x_) in (d_374_mrkKeyIds_)) and (((_dafny.MultiSet(d_374_mrkKeyIds_))[d_377_x_]) >= (1)):
                            coll9_ = coll9_.union(_dafny.Set([d_377_x_]))
                    return _dafny.Set(coll9_)
                d_376_duplicateMrkIds_ = iife15_()

                def lambda39_(d_379_duplicateMrkIds_):
                    def lambda40_(d_380_identifier_):
                        return (default__.GetKeyId(d_380_identifier_)) in (d_379_duplicateMrkIds_)

                    return lambda40_

                d_378_isDuplicate_ = lambda39_(d_376_duplicateMrkIds_)
                def lambda41_(d_382_i_):
                    return (d_382_i_).ToString()

                d_381_identifierToString_ = lambda41_
                d_383_duplicateIdentifiers_ = Seq.default__.Filter(d_378_isDuplicate_, identifiers)
                d_384_duplicates_ = Seq.default__.Map(d_381_identifierToString_, d_383_duplicateIdentifiers_)
                if (len(d_384_duplicates_)) == (0):
                    return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Impossible")))
                elif True:
                    return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("Related multi-Region keys: ")) + (StandardLibrary.default__.Join(d_384_duplicates_, _dafny.Seq(",")))) + (_dafny.Seq("are not allowed."))))

    @staticmethod
    def GetKeyId(identifier):
        source18_ = identifier
        if source18_.is_AwsKmsArnIdentifier:
            d_385___mcc_h0_ = source18_.a
            d_386_a_ = d_385___mcc_h0_
            return ((d_386_a_).resource).value
        elif True:
            d_387___mcc_h1_ = source18_.r
            d_388_i_ = d_387___mcc_h1_
            return (d_388_i_).value

