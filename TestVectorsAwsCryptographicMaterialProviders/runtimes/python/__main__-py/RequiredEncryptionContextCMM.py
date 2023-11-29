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

# Module: RequiredEncryptionContextCMM


class RequiredEncryptionContextCMM(CMM.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager):
    def  __init__(self):
        self._underlyingCMM: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager = None
        self._requiredEncryptionContextKeys: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "RequiredEncryptionContextCMM.RequiredEncryptionContextCMM"
    def GetEncryptionMaterials(self, input):
        out224_: Wrappers.Result
        out224_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out224_

    def DecryptMaterials(self, input):
        out225_: Wrappers.Result
        out225_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out225_

    def ctor__(self, inputCMM, inputKeys):
        d_1093_keySet_: _dafny.Set
        d_1093_keySet_ = inputKeys
        d_1094_keySeq_: _dafny.Seq
        d_1094_keySeq_ = _dafny.Seq([])
        while (d_1093_keySet_) != (_dafny.Set({})):
            d_1095_key_: _dafny.Seq
            with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                assign_such_that_1_: _dafny.Seq
                for assign_such_that_1_ in (d_1093_keySet_).Elements:
                    d_1095_key_ = assign_such_that_1_
                    if (d_1095_key_) in (d_1093_keySet_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                raise Exception("assign-such-that search produced no value (line 61)")
                pass
            d_1094_keySeq_ = (d_1094_keySeq_) + (_dafny.Seq([d_1095_key_]))
            d_1093_keySet_ = (d_1093_keySet_) - (_dafny.Set({d_1095_key_}))
        (self)._underlyingCMM = inputCMM
        (self)._requiredEncryptionContextKeys = d_1094_keySeq_

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1096_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda74_(forall_var_11_):
            d_1097_k_: _dafny.Seq = forall_var_11_
            return not ((d_1097_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1097_k_) in ((input).encryptionContext))

        d_1096_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda74_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not contain required keys.")))
        if (d_1096_valueOrError0_).IsFailure():
            output = (d_1096_valueOrError0_).PropagateFailure()
            return output
        d_1098_result_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput
        d_1099_valueOrError1_: Wrappers.Result = None
        pat_let_tv36_ = input
        out226_: Wrappers.Result
        def iife43_(_pat_let20_0):
            def iife44_(d_1100_dt__update__tmp_h0_):
                def iife45_(_pat_let21_0):
                    def iife46_(d_1101_dt__update_hrequiredEncryptionContextKeys_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((d_1100_dt__update__tmp_h0_).encryptionContext, (d_1100_dt__update__tmp_h0_).commitmentPolicy, (d_1100_dt__update__tmp_h0_).algorithmSuiteId, (d_1100_dt__update__tmp_h0_).maxPlaintextLength, d_1101_dt__update_hrequiredEncryptionContextKeys_h0_)
                    return iife46_(_pat_let21_0)
                return iife45_(Wrappers.Option_Some((((pat_let_tv36_).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))) + ((self).requiredEncryptionContextKeys)))
            return iife44_(_pat_let20_0)
        out226_ = ((self).underlyingCMM).GetEncryptionMaterials(iife43_(input))
        d_1099_valueOrError1_ = out226_
        if (d_1099_valueOrError1_).IsFailure():
            output = (d_1099_valueOrError1_).PropagateFailure()
            return output
        d_1098_result_ = (d_1099_valueOrError1_).Extract()
        d_1102_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda75_(forall_var_12_):
            d_1103_k_: _dafny.Seq = forall_var_12_
            return not ((d_1103_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1103_k_) in (((d_1098_result_).encryptionMaterials).requiredEncryptionContextKeys))

        d_1102_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda75_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Expected encryption context keys do not exist in keys to only authenticate.")))
        if (d_1102_valueOrError2_).IsFailure():
            output = (d_1102_valueOrError2_).PropagateFailure()
            return output
        d_1104_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1104_valueOrError3_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1098_result_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1104_valueOrError3_).IsFailure():
            output = (d_1104_valueOrError3_).PropagateFailure()
            return output
        d_1105_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1105_valueOrError4_ = Wrappers.default__.Need(CMM.default__.RequiredEncryptionContextKeys_q((input).requiredEncryptionContextKeys, (d_1098_result_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1105_valueOrError4_).IsFailure():
            output = (d_1105_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1098_result_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1106_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1106_valueOrError0_ = Wrappers.default__.Need(((input).reproducedEncryptionContext).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No reproduced encryption context on decrypt.")))
        if (d_1106_valueOrError0_).IsFailure():
            output = (d_1106_valueOrError0_).PropagateFailure()
            return output
        d_1107_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1107_valueOrError1_ = Wrappers.default__.Need(CMM.default__.ReproducedEncryptionContext_q(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
        if (d_1107_valueOrError1_).IsFailure():
            output = (d_1107_valueOrError1_).PropagateFailure()
            return output
        d_1108_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda76_(forall_var_13_):
            d_1109_k_: _dafny.Seq = forall_var_13_
            return not ((d_1109_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1109_k_) in (((input).reproducedEncryptionContext).value))

        d_1108_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda76_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing required keys.")))
        if (d_1108_valueOrError2_).IsFailure():
            output = (d_1108_valueOrError2_).PropagateFailure()
            return output
        d_1110_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsOutput
        d_1111_valueOrError3_: Wrappers.Result = None
        out227_: Wrappers.Result
        out227_ = ((self).underlyingCMM).DecryptMaterials(input)
        d_1111_valueOrError3_ = out227_
        if (d_1111_valueOrError3_).IsFailure():
            output = (d_1111_valueOrError3_).PropagateFailure()
            return output
        d_1110_result_ = (d_1111_valueOrError3_).Extract()
        d_1112_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda77_(forall_var_14_):
            d_1113_k_: _dafny.Seq = forall_var_14_
            return not ((d_1113_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1113_k_) in (((d_1110_result_).decryptionMaterials).encryptionContext))

        d_1112_valueOrError4_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda77_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Final encryption context missing required keys.")))
        if (d_1112_valueOrError4_).IsFailure():
            output = (d_1112_valueOrError4_).PropagateFailure()
            return output
        d_1114_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1114_valueOrError5_ = Wrappers.default__.Need(CMM.default__.EncryptionContextComplete(input, (d_1110_result_).decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing from encryption context.")))
        if (d_1114_valueOrError5_).IsFailure():
            output = (d_1114_valueOrError5_).PropagateFailure()
            return output
        d_1115_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1115_valueOrError6_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey((d_1110_result_).decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1115_valueOrError6_).IsFailure():
            output = (d_1115_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1110_result_)
        return output
        return output

    @property
    def underlyingCMM(self):
        return self._underlyingCMM
    @property
    def requiredEncryptionContextKeys(self):
        return self._requiredEncryptionContextKeys
