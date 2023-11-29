import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
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
import Seq_mMergeSort
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
import Aws_mCryptography
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
import CreateRawAesKeyrings

# Module: CreateRawRsaKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllRawRsaKeyring(input):
        allRSA: _dafny.Seq = _dafny.Seq({})
        allRSA = _dafny.Seq([])
        d_103_AllPaddingSchemes_: _dafny.Set
        def iife1_():
            coll1_ = _dafny.Set()
            compr_1_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
            for compr_1_ in software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme.AllSingletonConstructors:
                d_104_w_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme = compr_1_
                if True:
                    coll1_ = coll1_.union(_dafny.Set([d_104_w_]))
            return _dafny.Set(coll1_)
        d_103_AllPaddingSchemes_ = iife1_()
        
        while (d_103_AllPaddingSchemes_) != (_dafny.Set({})):
            d_105_paddingScheme_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
            with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                assign_such_that_1_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
                for assign_such_that_1_ in (d_103_AllPaddingSchemes_).Elements:
                    d_105_paddingScheme_ = assign_such_that_1_
                    if (d_105_paddingScheme_) in (d_103_AllPaddingSchemes_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                raise Exception("assign-such-that search produced no value (line 40)")
                pass
            d_106_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out32_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out32_ = default__.CreateRawRsaKeyring(d_105_paddingScheme_)
            d_106_keyring_ = out32_
            allRSA = (allRSA) + (_dafny.Seq([d_106_keyring_]))
            d_103_AllPaddingSchemes_ = (d_103_AllPaddingSchemes_) - (_dafny.Set({d_105_paddingScheme_}))
        return allRSA

    @staticmethod
    def CreateRawRsaKeyring(paddingScheme):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        d_107_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_108_valueOrError0_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_108_valueOrError0_ = out33_
        if not(not((d_108_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(56,12): " + _dafny.string_of(d_108_valueOrError0_))
        d_107_mpl_ = (d_108_valueOrError0_).Extract()
        d_109_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_110_valueOrError1_: Wrappers.Result = None
        out34_: Wrappers.Result
        out34_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_110_valueOrError1_ = out34_
        if not(not((d_110_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(57,15): " + _dafny.string_of(d_110_valueOrError1_))
        d_109_crypto_ = (d_110_valueOrError1_).Extract()
        d_111_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        d_112_valueOrError2_: Wrappers.Result = None
        out35_: Wrappers.Result
        out35_ = (d_109_crypto_).GenerateRSAKeyPair(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(2048))
        d_112_valueOrError2_ = out35_
        if not(not((d_112_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(59,13): " + _dafny.string_of(d_112_valueOrError2_))
        d_111_keys_ = (d_112_valueOrError2_).Extract()
        d_113_namespace_: _dafny.Seq
        d_114_name_: _dafny.Seq
        out36_: _dafny.Seq
        out37_: _dafny.Seq
        out36_, out37_ = TestVectorsUtils.default__.NamespaceAndName(0)
        d_113_namespace_ = out36_
        d_114_name_ = out37_
        d_115_valueOrError3_: Wrappers.Result = None
        out38_: Wrappers.Result
        out38_ = (d_107_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_113_namespace_, d_114_name_, paddingScheme, Wrappers.Option_Some(((d_111_keys_).publicKey).pem), Wrappers.Option_Some(((d_111_keys_).privateKey).pem)))
        d_115_valueOrError3_ = out38_
        if not(not((d_115_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(66,12): " + _dafny.string_of(d_115_valueOrError3_))
        keyring = (d_115_valueOrError3_).Extract()
        return keyring

