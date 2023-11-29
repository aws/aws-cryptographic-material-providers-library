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

# assert "AwsKmsMrkMatchForDecrypt" == __name__
AwsKmsMrkMatchForDecrypt = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AwsKmsMrkMatchForDecrypt(configuredAwsKmsIdentifier, messageAwsKmsIdentifer):
        if (configuredAwsKmsIdentifier) == (messageAwsKmsIdentifer):
            return True
        elif True:
            source5_ = (messageAwsKmsIdentifer, configuredAwsKmsIdentifier)
            if True:
                d_57___mcc_h0_ = source5_[0]
                d_58___mcc_h1_ = source5_[1]
                source6_ = d_57___mcc_h0_
                if source6_.is_AwsKmsArnIdentifier:
                    d_59___mcc_h2_ = source6_.a
                    source7_ = d_58___mcc_h1_
                    if source7_.is_AwsKmsArnIdentifier:
                        d_60___mcc_h4_ = source7_.a
                        d_61_messageAwsKmsArn_ = d_60___mcc_h4_
                        d_62_configuredAwsKmsArn_ = d_59___mcc_h2_
                        if (not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_62_configuredAwsKmsArn_))) or (not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_61_messageAwsKmsArn_))):
                            return False
                        elif True:
                            return (((((d_61_messageAwsKmsArn_).partition) == ((d_62_configuredAwsKmsArn_).partition)) and (((d_61_messageAwsKmsArn_).service) == ((d_62_configuredAwsKmsArn_).service))) and (((d_61_messageAwsKmsArn_).account) == ((d_62_configuredAwsKmsArn_).account))) and (((d_61_messageAwsKmsArn_).resource) == ((d_62_configuredAwsKmsArn_).resource))
                    elif True:
                        d_63___mcc_h6_ = source7_.r
                        return False
                elif True:
                    d_64___mcc_h8_ = source6_.r
                    return False

