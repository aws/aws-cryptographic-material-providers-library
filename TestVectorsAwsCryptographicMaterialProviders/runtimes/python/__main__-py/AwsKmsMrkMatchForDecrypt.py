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
import AwsKmsMrkAreUnique

# Module: AwsKmsMrkMatchForDecrypt

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AwsKmsMrkMatchForDecrypt(configuredAwsKmsIdentifier, messageAwsKmsIdentifer):
        if (configuredAwsKmsIdentifier) == (messageAwsKmsIdentifer):
            return True
        elif True:
            source14_ = (messageAwsKmsIdentifer, configuredAwsKmsIdentifier)
            d_159___mcc_h0_ = source14_[0]
            d_160___mcc_h1_ = source14_[1]
            source15_ = d_159___mcc_h0_
            if source15_.is_AwsKmsArnIdentifier:
                d_161___mcc_h2_ = source15_.a
                source16_ = d_160___mcc_h1_
                if source16_.is_AwsKmsArnIdentifier:
                    d_162___mcc_h4_ = source16_.a
                    d_163_messageAwsKmsArn_ = d_162___mcc_h4_
                    d_164_configuredAwsKmsArn_ = d_161___mcc_h2_
                    if (not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_164_configuredAwsKmsArn_))) or (not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_163_messageAwsKmsArn_))):
                        return False
                    elif True:
                        return (((((d_163_messageAwsKmsArn_).partition) == ((d_164_configuredAwsKmsArn_).partition)) and (((d_163_messageAwsKmsArn_).service) == ((d_164_configuredAwsKmsArn_).service))) and (((d_163_messageAwsKmsArn_).account) == ((d_164_configuredAwsKmsArn_).account))) and (((d_163_messageAwsKmsArn_).resource) == ((d_164_configuredAwsKmsArn_).resource))
                elif True:
                    d_165___mcc_h6_ = source16_.r
                    return False
            elif True:
                d_166___mcc_h8_ = source15_.r
                return False

