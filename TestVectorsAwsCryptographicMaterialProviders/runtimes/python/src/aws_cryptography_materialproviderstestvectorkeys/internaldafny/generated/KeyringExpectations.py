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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
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

# Module: KeyringExpectations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExpectAlgorithmSuiteKeyringSuccess(mpl, keyring):
        d_32_encryptionContext_: _dafny.Map
        out2_: _dafny.Map
        out2_ = TestVectorsUtils.default__.SmallEncryptionContext(TestVectorsUtils.SmallEncryptionContextVariation_A())
        d_32_encryptionContext_ = out2_
        hi0_ = len(TestVectorConstants.default__.AllAlgorithmSuiteIds)
        for d_33_i_ in range(0, hi0_):
            d_34_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
            d_34_algorithmSuiteId_ = (TestVectorConstants.default__.AllAlgorithmSuiteIds)[d_33_i_]
            d_35_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            out3_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            out3_ = TestVectorsUtils.default__.GetEncryptionMaterials(mpl, d_34_algorithmSuiteId_, d_32_encryptionContext_)
            d_35_encryptionMaterials_ = out3_
            d_36___v0_: Materials
            out4_: Materials
            out4_ = default__.ExpectKeyringSuccess(mpl, keyring, d_35_encryptionMaterials_)
            d_36___v0_ = out4_

    @staticmethod
    def ExpectKeyringSuccess(mpl, keyring, encryptionMaterialsIn):
        results: Materials = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n ExpectKeyringSuccess:\n")))
        _dafny.print(_dafny.string_of(((encryptionMaterialsIn).algorithmSuite).id))
        d_37_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out5_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out5_ = default__.ExpectOnEncryptSuccess(mpl, keyring, encryptionMaterialsIn)
        d_37_encryptionMaterials_ = out5_
        d_38_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_39_valueOrError0_: Wrappers.Result = None
        d_39_valueOrError0_ = (mpl).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(((d_37_encryptionMaterials_).algorithmSuite).id, (d_37_encryptionMaterials_).encryptionContext, _dafny.Seq([])))
        if not(not((d_39_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(68,30): " + _dafny.string_of(d_39_valueOrError0_))
        d_38_decryptionMaterialsIn_ = (d_39_valueOrError0_).Extract()
        d_40_decryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out6_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out6_ = default__.ExpectOnDecryptSuccess(mpl, keyring, d_38_decryptionMaterialsIn_, (d_37_encryptionMaterials_).encryptedDataKeys)
        d_40_decryptionMaterials_ = out6_
        if not(((d_37_encryptionMaterials_).plaintextDataKey) == ((d_40_decryptionMaterials_).plaintextDataKey)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        results = Materials_Materials(d_37_encryptionMaterials_, d_40_decryptionMaterials_)
        return results

    @staticmethod
    def ExpectOnEncryptSuccess(mpl, keyring, encryptionMaterialsIn):
        encryptionMaterials: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        d_41_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_42_valueOrError0_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (keyring).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(encryptionMaterialsIn))
        d_42_valueOrError0_ = out7_
        if not(not((d_42_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(110,31): " + _dafny.string_of(d_42_valueOrError0_))
        d_41_encryptionMaterialsOut_ = (d_42_valueOrError0_).Extract()
        encryptionMaterials = (d_41_encryptionMaterialsOut_).materials
        d_43___v1_: tuple
        d_44_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_44_valueOrError1_ = (mpl).ValidEncryptionMaterialsTransition(software_amazon_cryptography_materialproviders_internaldafny_types.ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput(encryptionMaterialsIn, encryptionMaterials))
        if not(not((d_44_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(117,10): " + _dafny.string_of(d_44_valueOrError1_))
        d_43___v1_ = (d_44_valueOrError1_).Extract()
        d_45___v2_: tuple
        d_46_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_46_valueOrError2_ = (mpl).EncryptionMaterialsHasPlaintextDataKey(encryptionMaterials)
        if not(not((d_46_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(125,10): " + _dafny.string_of(d_46_valueOrError2_))
        d_45___v2_ = (d_46_valueOrError2_).Extract()
        if not((1) <= (len(((d_41_encryptionMaterialsOut_).materials).encryptedDataKeys))):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        return encryptionMaterials

    @staticmethod
    def ExpectOnDecryptSuccess(mpl, keyring, decryptionMaterialsIn, encryptedDataKeys):
        decryptionMaterials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        d_47_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_48_valueOrError0_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = (keyring).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(decryptionMaterialsIn, encryptedDataKeys))
        d_48_valueOrError0_ = out8_
        if not(not((d_48_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(152,31): " + _dafny.string_of(d_48_valueOrError0_))
        d_47_decryptionMaterialsOut_ = (d_48_valueOrError0_).Extract()
        decryptionMaterials = (d_47_decryptionMaterialsOut_).materials
        d_49___v3_: tuple
        d_50_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_50_valueOrError1_ = (mpl).ValidDecryptionMaterialsTransition(software_amazon_cryptography_materialproviders_internaldafny_types.ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput(decryptionMaterialsIn, decryptionMaterials))
        if not(not((d_50_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(162,10): " + _dafny.string_of(d_50_valueOrError1_))
        d_49___v3_ = (d_50_valueOrError1_).Extract()
        d_51___v4_: tuple
        d_52_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_52_valueOrError2_ = (mpl).DecryptionMaterialsWithPlaintextDataKey(decryptionMaterials)
        if not(not((d_52_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(170,10): " + _dafny.string_of(d_52_valueOrError2_))
        d_51___v4_ = (d_52_valueOrError2_).Extract()
        return decryptionMaterials


class Materials:
    @classmethod
    def default(cls, ):
        return lambda: Materials_Materials(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Materials(self) -> bool:
        return isinstance(self, Materials_Materials)

class Materials_Materials(Materials, NamedTuple('Materials', [('encryptionMaterials', Any), ('decryptionMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyringExpectations.Materials.Materials({_dafny.string_of(self.encryptionMaterials)}, {_dafny.string_of(self.decryptionMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Materials_Materials) and self.encryptionMaterials == __o.encryptionMaterials and self.decryptionMaterials == __o.decryptionMaterials
    def __hash__(self) -> int:
        return super().__hash__()

