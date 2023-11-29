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
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny
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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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

assert "RequiredEncryptionContextCMM" == __name__
RequiredEncryptionContextCMM = sys.modules[__name__]


class RequiredEncryptionContextCMM(CMM.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager):
    def  __init__(self):
        self._underlyingCMM: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager = None
        self._requiredEncryptionContextKeys: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "RequiredEncryptionContextCMM.RequiredEncryptionContextCMM"
    def GetEncryptionMaterials(self, input):
        out268_: Wrappers.Result
        out268_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out268_

    def DecryptMaterials(self, input):
        out269_: Wrappers.Result
        out269_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out269_

    def ctor__(self, inputCMM, inputKeys):
        d_1280_keySet_: _dafny.Set
        d_1280_keySet_ = inputKeys
        d_1281_keySeq_: _dafny.Seq
        d_1281_keySeq_ = _dafny.Seq([])
        while (d_1280_keySet_) != (_dafny.Set({})):
            d_1282_key_: _dafny.Seq
            with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                assign_such_that_1_: _dafny.Seq
                for assign_such_that_1_ in (d_1280_keySet_).Elements:
                    d_1282_key_ = assign_such_that_1_
                    if (d_1282_key_) in (d_1280_keySet_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                raise Exception("assign-such-that search produced no value (line 61)")
                pass
            d_1281_keySeq_ = (d_1281_keySeq_) + (_dafny.Seq([d_1282_key_]))
            d_1280_keySet_ = (d_1280_keySet_) - (_dafny.Set({d_1282_key_}))
        (self)._underlyingCMM = inputCMM
        (self)._requiredEncryptionContextKeys = d_1281_keySeq_

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1283_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda96_(forall_var_15_):
            d_1284_k_: _dafny.Seq = forall_var_15_
            return not ((d_1284_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1284_k_) in ((input).encryptionContext))

        d_1283_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda96_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not contain required keys.")))
        if (d_1283_valueOrError0_).IsFailure():
            output = (d_1283_valueOrError0_).PropagateFailure()
            return output
        d_1285_result_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput
        d_1286_valueOrError1_: Wrappers.Result = None
        pat_let_tv36_ = input
        def iife52_(_pat_let21_0):
            def iife53_(d_1287_dt__update__tmp_h0_):
                def iife54_(_pat_let22_0):
                    def iife55_(d_1288_dt__update_hrequiredEncryptionContextKeys_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((d_1287_dt__update__tmp_h0_).encryptionContext, (d_1287_dt__update__tmp_h0_).commitmentPolicy, (d_1287_dt__update__tmp_h0_).algorithmSuiteId, (d_1287_dt__update__tmp_h0_).maxPlaintextLength, d_1288_dt__update_hrequiredEncryptionContextKeys_h0_)
                    return iife55_(_pat_let22_0)
                return iife54_(Wrappers.Option_Some((((pat_let_tv36_).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))) + ((self).requiredEncryptionContextKeys)))
            return iife53_(_pat_let21_0)
        out270_: Wrappers.Result
        out270_ = ((self).underlyingCMM).GetEncryptionMaterials(iife52_(input))
        d_1286_valueOrError1_ = out270_
        if (d_1286_valueOrError1_).IsFailure():
            output = (d_1286_valueOrError1_).PropagateFailure()
            return output
        d_1285_result_ = (d_1286_valueOrError1_).Extract()
        d_1289_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda97_(forall_var_16_):
            d_1290_k_: _dafny.Seq = forall_var_16_
            return not ((d_1290_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1290_k_) in (((d_1285_result_).encryptionMaterials).requiredEncryptionContextKeys))

        d_1289_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda97_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Expected encryption context keys do not exist in keys to only authenticate.")))
        if (d_1289_valueOrError2_).IsFailure():
            output = (d_1289_valueOrError2_).PropagateFailure()
            return output
        d_1291_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1291_valueOrError3_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1285_result_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1291_valueOrError3_).IsFailure():
            output = (d_1291_valueOrError3_).PropagateFailure()
            return output
        d_1292_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1292_valueOrError4_ = Wrappers.default__.Need(CMM.default__.RequiredEncryptionContextKeys_q((input).requiredEncryptionContextKeys, (d_1285_result_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1292_valueOrError4_).IsFailure():
            output = (d_1292_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1285_result_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1293_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1293_valueOrError0_ = Wrappers.default__.Need(((input).reproducedEncryptionContext).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No reproduced encryption context on decrypt.")))
        if (d_1293_valueOrError0_).IsFailure():
            output = (d_1293_valueOrError0_).PropagateFailure()
            return output
        d_1294_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1294_valueOrError1_ = Wrappers.default__.Need(CMM.default__.ReproducedEncryptionContext_q(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
        if (d_1294_valueOrError1_).IsFailure():
            output = (d_1294_valueOrError1_).PropagateFailure()
            return output
        d_1295_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda98_(forall_var_17_):
            d_1296_k_: _dafny.Seq = forall_var_17_
            return not ((d_1296_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1296_k_) in (((input).reproducedEncryptionContext).value))

        d_1295_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda98_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing required keys.")))
        if (d_1295_valueOrError2_).IsFailure():
            output = (d_1295_valueOrError2_).PropagateFailure()
            return output
        d_1297_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsOutput
        d_1298_valueOrError3_: Wrappers.Result = None
        out271_: Wrappers.Result
        out271_ = ((self).underlyingCMM).DecryptMaterials(input)
        d_1298_valueOrError3_ = out271_
        if (d_1298_valueOrError3_).IsFailure():
            output = (d_1298_valueOrError3_).PropagateFailure()
            return output
        d_1297_result_ = (d_1298_valueOrError3_).Extract()
        d_1299_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda99_(forall_var_18_):
            d_1300_k_: _dafny.Seq = forall_var_18_
            return not ((d_1300_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1300_k_) in (((d_1297_result_).decryptionMaterials).encryptionContext))

        d_1299_valueOrError4_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda99_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Final encryption context missing required keys.")))
        if (d_1299_valueOrError4_).IsFailure():
            output = (d_1299_valueOrError4_).PropagateFailure()
            return output
        d_1301_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1301_valueOrError5_ = Wrappers.default__.Need(CMM.default__.EncryptionContextComplete(input, (d_1297_result_).decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing from encryption context.")))
        if (d_1301_valueOrError5_).IsFailure():
            output = (d_1301_valueOrError5_).PropagateFailure()
            return output
        d_1302_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1302_valueOrError6_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey((d_1297_result_).decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1302_valueOrError6_).IsFailure():
            output = (d_1302_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1297_result_)
        return output
        return output

    @property
    def underlyingCMM(self):
        return self._underlyingCMM
    @property
    def requiredEncryptionContextKeys(self):
        return self._requiredEncryptionContextKeys
