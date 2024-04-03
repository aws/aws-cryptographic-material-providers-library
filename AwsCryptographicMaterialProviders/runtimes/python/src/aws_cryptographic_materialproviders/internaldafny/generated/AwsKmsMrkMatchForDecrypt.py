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

# Module: AwsKmsMrkMatchForDecrypt

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AwsKmsMrkMatchForDecrypt(configuredAwsKmsIdentifier, messageAwsKmsIdentifer):
        if (configuredAwsKmsIdentifier) == (messageAwsKmsIdentifer):
            return True
        elif True:
            source5_ = (messageAwsKmsIdentifer, configuredAwsKmsIdentifier)
            d_66___mcc_h0_ = source5_[0]
            d_67___mcc_h1_ = source5_[1]
            source6_ = d_66___mcc_h0_
            if source6_.is_AwsKmsArnIdentifier:
                d_68___mcc_h2_ = source6_.a
                source7_ = d_67___mcc_h1_
                if source7_.is_AwsKmsArnIdentifier:
                    d_69___mcc_h4_ = source7_.a
                    d_70_messageAwsKmsArn_ = d_69___mcc_h4_
                    d_71_configuredAwsKmsArn_ = d_68___mcc_h2_
                    if (not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_71_configuredAwsKmsArn_))) or (not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_70_messageAwsKmsArn_))):
                        return False
                    elif True:
                        return (((((d_70_messageAwsKmsArn_).partition) == ((d_71_configuredAwsKmsArn_).partition)) and (((d_70_messageAwsKmsArn_).service) == ((d_71_configuredAwsKmsArn_).service))) and (((d_70_messageAwsKmsArn_).account) == ((d_71_configuredAwsKmsArn_).account))) and (((d_70_messageAwsKmsArn_).resource) == ((d_71_configuredAwsKmsArn_).resource))
                elif True:
                    d_72___mcc_h6_ = source7_.r
                    return False
            elif True:
                d_73___mcc_h8_ = source6_.r
                return False

