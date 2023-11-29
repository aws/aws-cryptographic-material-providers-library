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

# Module: KeyringExpectations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExpectAlgorithmSuiteKeyringSuccess(mpl, keyring):
        d_1266_encryptionContext_: _dafny.Map
        out258_: _dafny.Map
        out258_ = TestVectorsUtils.default__.SmallEncryptionContext(TestVectorsUtils.SmallEncryptionContextVariation_A())
        d_1266_encryptionContext_ = out258_
        hi11_ = len(TestVectorConstants.default__.AllAlgorithmSuiteIds)
        for d_1267_i_ in range(0, hi11_):
            d_1268_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
            d_1268_algorithmSuiteId_ = (TestVectorConstants.default__.AllAlgorithmSuiteIds)[d_1267_i_]
            d_1269_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            out259_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            out259_ = TestVectorsUtils.default__.GetEncryptionMaterials(mpl, d_1268_algorithmSuiteId_, d_1266_encryptionContext_)
            d_1269_encryptionMaterials_ = out259_
            d_1270___v0_: Materials
            out260_: Materials
            out260_ = default__.ExpectKeyringSuccess(mpl, keyring, d_1269_encryptionMaterials_)
            d_1270___v0_ = out260_

    @staticmethod
    def ExpectKeyringSuccess(mpl, keyring, encryptionMaterialsIn):
        results: Materials = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n ExpectKeyringSuccess:\n")))
        _dafny.print(_dafny.string_of(((encryptionMaterialsIn).algorithmSuite).id))
        d_1271_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out261_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out261_ = default__.ExpectOnEncryptSuccess(mpl, keyring, encryptionMaterialsIn)
        d_1271_encryptionMaterials_ = out261_
        d_1272_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1273_valueOrError0_: Wrappers.Result = None
        d_1273_valueOrError0_ = (mpl).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(((d_1271_encryptionMaterials_).algorithmSuite).id, (d_1271_encryptionMaterials_).encryptionContext, _dafny.Seq([])))
        if not(not((d_1273_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(68,30): " + _dafny.string_of(d_1273_valueOrError0_))
        d_1272_decryptionMaterialsIn_ = (d_1273_valueOrError0_).Extract()
        d_1274_decryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out262_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out262_ = default__.ExpectOnDecryptSuccess(mpl, keyring, d_1272_decryptionMaterialsIn_, (d_1271_encryptionMaterials_).encryptedDataKeys)
        d_1274_decryptionMaterials_ = out262_
        if not(((d_1271_encryptionMaterials_).plaintextDataKey) == ((d_1274_decryptionMaterials_).plaintextDataKey)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        results = Materials_Materials(d_1271_encryptionMaterials_, d_1274_decryptionMaterials_)
        return results

    @staticmethod
    def ExpectOnEncryptSuccess(mpl, keyring, encryptionMaterialsIn):
        encryptionMaterials: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        d_1275_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1276_valueOrError0_: Wrappers.Result = None
        out263_: Wrappers.Result
        out263_ = (keyring).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(encryptionMaterialsIn))
        d_1276_valueOrError0_ = out263_
        if not(not((d_1276_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(110,31): " + _dafny.string_of(d_1276_valueOrError0_))
        d_1275_encryptionMaterialsOut_ = (d_1276_valueOrError0_).Extract()
        encryptionMaterials = (d_1275_encryptionMaterialsOut_).materials
        d_1277___v1_: tuple
        d_1278_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1278_valueOrError1_ = (mpl).ValidEncryptionMaterialsTransition(software_amazon_cryptography_materialproviders_internaldafny_types.ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput(encryptionMaterialsIn, encryptionMaterials))
        if not(not((d_1278_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(117,10): " + _dafny.string_of(d_1278_valueOrError1_))
        d_1277___v1_ = (d_1278_valueOrError1_).Extract()
        d_1279___v2_: tuple
        d_1280_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1280_valueOrError2_ = (mpl).EncryptionMaterialsHasPlaintextDataKey(encryptionMaterials)
        if not(not((d_1280_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(125,10): " + _dafny.string_of(d_1280_valueOrError2_))
        d_1279___v2_ = (d_1280_valueOrError2_).Extract()
        if not((1) <= (len(((d_1275_encryptionMaterialsOut_).materials).encryptedDataKeys))):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        return encryptionMaterials

    @staticmethod
    def ExpectOnDecryptSuccess(mpl, keyring, decryptionMaterialsIn, encryptedDataKeys):
        decryptionMaterials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        d_1281_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1282_valueOrError0_: Wrappers.Result = None
        out264_: Wrappers.Result
        out264_ = (keyring).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(decryptionMaterialsIn, encryptedDataKeys))
        d_1282_valueOrError0_ = out264_
        if not(not((d_1282_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(152,31): " + _dafny.string_of(d_1282_valueOrError0_))
        d_1281_decryptionMaterialsOut_ = (d_1282_valueOrError0_).Extract()
        decryptionMaterials = (d_1281_decryptionMaterialsOut_).materials
        d_1283___v3_: tuple
        d_1284_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1284_valueOrError1_ = (mpl).ValidDecryptionMaterialsTransition(software_amazon_cryptography_materialproviders_internaldafny_types.ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput(decryptionMaterialsIn, decryptionMaterials))
        if not(not((d_1284_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(162,10): " + _dafny.string_of(d_1284_valueOrError1_))
        d_1283___v3_ = (d_1284_valueOrError1_).Extract()
        d_1285___v4_: tuple
        d_1286_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1286_valueOrError2_ = (mpl).DecryptionMaterialsWithPlaintextDataKey(decryptionMaterials)
        if not(not((d_1286_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/KeyringExpectations.dfy(170,10): " + _dafny.string_of(d_1286_valueOrError2_))
        d_1285___v4_ = (d_1286_valueOrError2_).Extract()
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

