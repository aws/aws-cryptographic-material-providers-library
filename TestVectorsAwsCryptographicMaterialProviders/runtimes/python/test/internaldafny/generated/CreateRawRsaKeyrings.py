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
import Aws_mCryptography
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
import CreateRawAesKeyrings

assert "CreateRawRsaKeyrings" == __name__
CreateRawRsaKeyrings = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllRawRsaKeyring(input):
        allRSA: _dafny.Seq = _dafny.Seq({})
        allRSA = _dafny.Seq([])
        d_1335_AllPaddingSchemes_: _dafny.Set
        def iife53_():
            coll5_ = _dafny.Set()
            compr_5_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
            for compr_5_ in software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme.AllSingletonConstructors:
                d_1336_w_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme = compr_5_
                if True:
                    coll5_ = coll5_.union(_dafny.Set([d_1336_w_]))
            return _dafny.Set(coll5_)
        d_1335_AllPaddingSchemes_ = iife53_()
        
        while (d_1335_AllPaddingSchemes_) != (_dafny.Set({})):
            d_1337_paddingScheme_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
            with _dafny.label("_ASSIGN_SUCH_THAT_d_3"):
                assign_such_that_3_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
                for assign_such_that_3_ in (d_1335_AllPaddingSchemes_).Elements:
                    d_1337_paddingScheme_ = assign_such_that_3_
                    if (d_1337_paddingScheme_) in (d_1335_AllPaddingSchemes_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_3")
                raise Exception("assign-such-that search produced no value (line 40)")
                pass
            d_1338_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out288_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out288_ = CreateRawRsaKeyrings.default__.CreateRawRsaKeyring(d_1337_paddingScheme_)
            d_1338_keyring_ = out288_
            allRSA = (allRSA) + (_dafny.Seq([d_1338_keyring_]))
            d_1335_AllPaddingSchemes_ = (d_1335_AllPaddingSchemes_) - (_dafny.Set({d_1337_paddingScheme_}))
        return allRSA

    @staticmethod
    def CreateRawRsaKeyring(paddingScheme):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        d_1339_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1340_valueOrError0_: Wrappers.Result = None
        out289_: Wrappers.Result
        out289_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1340_valueOrError0_ = out289_
        if not(not((d_1340_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(56,12): " + _dafny.string_of(d_1340_valueOrError0_))
        d_1339_mpl_ = (d_1340_valueOrError0_).Extract()
        d_1341_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1342_valueOrError1_: Wrappers.Result = None
        out290_: Wrappers.Result
        out290_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1342_valueOrError1_ = out290_
        if not(not((d_1342_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(57,15): " + _dafny.string_of(d_1342_valueOrError1_))
        d_1341_crypto_ = (d_1342_valueOrError1_).Extract()
        d_1343_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        d_1344_valueOrError2_: Wrappers.Result = None
        out291_: Wrappers.Result
        out291_ = (d_1341_crypto_).GenerateRSAKeyPair(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(2048))
        d_1344_valueOrError2_ = out291_
        if not(not((d_1344_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(59,13): " + _dafny.string_of(d_1344_valueOrError2_))
        d_1343_keys_ = (d_1344_valueOrError2_).Extract()
        d_1345_namespace_: _dafny.Seq
        d_1346_name_: _dafny.Seq
        out292_: _dafny.Seq
        out293_: _dafny.Seq
        out292_, out293_ = TestVectorsUtils.default__.NamespaceAndName(0)
        d_1345_namespace_ = out292_
        d_1346_name_ = out293_
        d_1347_valueOrError3_: Wrappers.Result = None
        out294_: Wrappers.Result
        out294_ = (d_1339_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_1345_namespace_, d_1346_name_, paddingScheme, Wrappers.Option_Some(((d_1343_keys_).publicKey).pem), Wrappers.Option_Some(((d_1343_keys_).privateKey).pem)))
        d_1347_valueOrError3_ = out294_
        if not(not((d_1347_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateRawRsaKeyrings.dfy(66,12): " + _dafny.string_of(d_1347_valueOrError3_))
        keyring = (d_1347_valueOrError3_).Extract()
        return keyring

