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
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
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
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
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
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
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
        d_89_AllAesWrappingAlgs_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
            for compr_0_ in software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg.AllSingletonConstructors:
                d_90_w_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg = compr_0_
                if True:
                    coll0_ = coll0_.union(_dafny.Set([d_90_w_]))
            return _dafny.Set(coll0_)
        d_89_AllAesWrappingAlgs_ = iife0_()
        
        while (d_89_AllAesWrappingAlgs_) != (_dafny.Set({})):
            d_91_wrappingAlg_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
            with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                assign_such_that_0_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
                for assign_such_that_0_ in (d_89_AllAesWrappingAlgs_).Elements:
                    d_91_wrappingAlg_ = assign_such_that_0_
                    if (d_91_wrappingAlg_) in (d_89_AllAesWrappingAlgs_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                raise Exception("assign-such-that search produced no value (line 40)")
                pass
            d_92_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out25_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out25_ = default__.CreateRawAesKeyring(d_91_wrappingAlg_)
            d_92_keyring_ = out25_
            allAES = (allAES) + (_dafny.Seq([d_92_keyring_]))
            d_89_AllAesWrappingAlgs_ = (d_89_AllAesWrappingAlgs_) - (_dafny.Set({d_91_wrappingAlg_}))
        return allAES

    @staticmethod
    def CreateRawAesKeyring(wrappingAlg):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateRawAesKeyring: ")))
        _dafny.print(_dafny.string_of(wrappingAlg))
        d_93_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_94_valueOrError0_: Wrappers.Result = None
        out26_: Wrappers.Result
        out26_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_94_valueOrError0_ = out26_
        if not(not((d_94_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(59,12): " + _dafny.string_of(d_94_valueOrError0_))
        d_93_mpl_ = (d_94_valueOrError0_).Extract()
        d_95_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_96_valueOrError1_: Wrappers.Result = None
        out27_: Wrappers.Result
        out27_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_96_valueOrError1_ = out27_
        if not(not((d_96_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(60,15): " + _dafny.string_of(d_96_valueOrError1_))
        d_95_crypto_ = (d_96_valueOrError1_).Extract()
        d_97_length_: int
        def lambda0_(source1_):
            if source1_.is_ALG__AES128__GCM__IV12__TAG16:
                return 16
            elif source1_.is_ALG__AES192__GCM__IV12__TAG16:
                return 24
            elif True:
                return 32

        d_97_length_ = lambda0_(wrappingAlg)
        d_98_wrappingKey_: _dafny.Seq
        d_99_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out28_: Wrappers.Result
        out28_ = (d_95_crypto_).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(d_97_length_))
        d_99_valueOrError2_ = out28_
        if not(not((d_99_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(67,20): " + _dafny.string_of(d_99_valueOrError2_))
        d_98_wrappingKey_ = (d_99_valueOrError2_).Extract()
        d_100_namespace_: _dafny.Seq
        d_101_name_: _dafny.Seq
        out29_: _dafny.Seq
        out30_: _dafny.Seq
        out29_, out30_ = TestVectorsUtils.default__.NamespaceAndName(0)
        d_100_namespace_ = out29_
        d_101_name_ = out30_
        d_102_valueOrError3_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = (d_93_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_100_namespace_, d_101_name_, d_98_wrappingKey_, wrappingAlg))
        d_102_valueOrError3_ = out31_
        if not(not((d_102_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawAesKeyrings.dfy(74,12): " + _dafny.string_of(d_102_valueOrError3_))
        keyring = (d_102_valueOrError3_).Extract()
        return keyring

