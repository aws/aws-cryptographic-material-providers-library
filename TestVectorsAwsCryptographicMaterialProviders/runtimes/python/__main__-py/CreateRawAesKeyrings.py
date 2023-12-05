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
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
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
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings

# Module: CreateRawAesKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllRawAesKeyring(input):
        allAES: _dafny.Seq = _dafny.Seq({})
        allAES = _dafny.Seq([])
        d_1323_AllAesWrappingAlgs_: _dafny.Set
        def iife32_():
            coll4_ = _dafny.Set()
            compr_4_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
            for compr_4_ in software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg.AllSingletonConstructors:
                d_1324_w_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg = compr_4_
                if True:
                    coll4_ = coll4_.union(_dafny.Set([d_1324_w_]))
            return _dafny.Set(coll4_)
        d_1323_AllAesWrappingAlgs_ = iife32_()
        
        while (d_1323_AllAesWrappingAlgs_) != (_dafny.Set({})):
            d_1325_wrappingAlg_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
            with _dafny.label("_ASSIGN_SUCH_THAT_d_2"):
                assign_such_that_2_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
                for assign_such_that_2_ in (d_1323_AllAesWrappingAlgs_).Elements:
                    d_1325_wrappingAlg_ = assign_such_that_2_
                    if (d_1325_wrappingAlg_) in (d_1323_AllAesWrappingAlgs_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_2")
                raise Exception("assign-such-that search produced no value (line 40)")
                pass
            d_1326_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out281_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out281_ = default__.CreateRawAesKeyring(d_1325_wrappingAlg_)
            d_1326_keyring_ = out281_
            allAES = (allAES) + (_dafny.Seq([d_1326_keyring_]))
            d_1323_AllAesWrappingAlgs_ = (d_1323_AllAesWrappingAlgs_) - (_dafny.Set({d_1325_wrappingAlg_}))
        return allAES

    @staticmethod
    def CreateRawAesKeyring(wrappingAlg):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateRawAesKeyring: ")))
        _dafny.print(_dafny.string_of(wrappingAlg))
        d_1327_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1328_valueOrError0_: Wrappers.Result = None
        out282_: Wrappers.Result
        out282_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1328_valueOrError0_ = out282_
        if not(not((d_1328_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(59,12): " + _dafny.string_of(d_1328_valueOrError0_))
        d_1327_mpl_ = (d_1328_valueOrError0_).Extract()
        d_1329_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1330_valueOrError1_: Wrappers.Result = None
        out283_: Wrappers.Result
        out283_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1330_valueOrError1_ = out283_
        if not(not((d_1330_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(60,15): " + _dafny.string_of(d_1330_valueOrError1_))
        d_1329_crypto_ = (d_1330_valueOrError1_).Extract()
        d_1331_length_: int
        def lambda82_(source38_):
            if source38_.is_ALG__AES128__GCM__IV12__TAG16:
                return 16
            elif source38_.is_ALG__AES192__GCM__IV12__TAG16:
                return 24
            elif True:
                return 32

        d_1331_length_ = lambda82_(wrappingAlg)
        d_1332_wrappingKey_: _dafny.Seq
        d_1333_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out284_: Wrappers.Result
        out284_ = (d_1329_crypto_).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(d_1331_length_))
        d_1333_valueOrError2_ = out284_
        if not(not((d_1333_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(67,20): " + _dafny.string_of(d_1333_valueOrError2_))
        d_1332_wrappingKey_ = (d_1333_valueOrError2_).Extract()
        d_1334_namespace_: _dafny.Seq
        d_1335_name_: _dafny.Seq
        out285_: _dafny.Seq
        out286_: _dafny.Seq
        out285_, out286_ = TestVectorsUtils.default__.NamespaceAndName(0)
        d_1334_namespace_ = out285_
        d_1335_name_ = out286_
        d_1336_valueOrError3_: Wrappers.Result = None
        out287_: Wrappers.Result
        out287_ = (d_1327_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_1334_namespace_, d_1335_name_, d_1332_wrappingKey_, wrappingAlg))
        d_1336_valueOrError3_ = out287_
        if not(not((d_1336_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(74,12): " + _dafny.string_of(d_1336_valueOrError3_))
        keyring = (d_1336_valueOrError3_).Extract()
        return keyring

