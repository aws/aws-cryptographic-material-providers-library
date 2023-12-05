import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing

# Module: AwsKmsMrkAreUnique

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AwsKmsMrkAreUnique(identifiers):
        d_143_mrks_ = Seq.default__.Filter(AwsArnParsing.default__.IsMultiRegionAwsKmsIdentifier, identifiers)
        if (len(d_143_mrks_)) == (0):
            return Wrappers.Outcome_Pass()
        elif True:
            d_144_mrkKeyIds_ = Seq.default__.Map(default__.GetKeyId, d_143_mrks_)
            d_145_setMrks_ = Seq.default__.ToSet(d_144_mrkKeyIds_)
            if (len(d_144_mrkKeyIds_)) == (len(d_145_setMrks_)):
                return Wrappers.Outcome_Pass()
            elif True:
                def iife4_():
                    coll0_ = _dafny.Set()
                    compr_0_: _dafny.Seq
                    for compr_0_ in (d_144_mrkKeyIds_).Elements:
                        d_147_x_: _dafny.Seq = compr_0_
                        if ((d_147_x_) in (d_144_mrkKeyIds_)) and (((_dafny.MultiSet(d_144_mrkKeyIds_))[d_147_x_]) >= (1)):
                            coll0_ = coll0_.union(_dafny.Set([d_147_x_]))
                    return _dafny.Set(coll0_)
                d_146_duplicateMrkIds_ = iife4_()

                def lambda10_(d_149_duplicateMrkIds_):
                    def lambda11_(d_150_identifier_):
                        return (default__.GetKeyId(d_150_identifier_)) in (d_149_duplicateMrkIds_)

                    return lambda11_

                d_148_isDuplicate_ = lambda10_(d_146_duplicateMrkIds_)
                def lambda12_(d_152_i_):
                    return (d_152_i_).ToString()

                d_151_identifierToString_ = lambda12_
                d_153_duplicateIdentifiers_ = Seq.default__.Filter(d_148_isDuplicate_, identifiers)
                d_154_duplicates_ = Seq.default__.Map(d_151_identifierToString_, d_153_duplicateIdentifiers_)
                if (len(d_154_duplicates_)) == (0):
                    return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Impossible")))
                elif True:
                    return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("Related multi-Region keys: ")) + (StandardLibrary.default__.Join(d_154_duplicates_, _dafny.Seq(",")))) + (_dafny.Seq("are not allowed."))))

    @staticmethod
    def GetKeyId(identifier):
        source13_ = identifier
        if source13_.is_AwsKmsArnIdentifier:
            d_155___mcc_h0_ = source13_.a
            d_156_a_ = d_155___mcc_h0_
            return ((d_156_a_).resource).value
        elif True:
            d_157___mcc_h1_ = source13_.r
            d_158_i_ = d_157___mcc_h1_
            return (d_158_i_).value

