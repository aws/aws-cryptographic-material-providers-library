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
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
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

# assert "RequiredEncryptionContextCMM" == __name__
RequiredEncryptionContextCMM = sys.modules[__name__]


class RequiredEncryptionContextCMM(CMM.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager):
    def  __init__(self):
        self._underlyingCMM: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager = None
        self._requiredEncryptionContextKeys: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "RequiredEncryptionContextCMM.RequiredEncryptionContextCMM"
    def GetEncryptionMaterials(self, input):
        out345_: Wrappers.Result
        out345_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out345_

    def DecryptMaterials(self, input):
        out346_: Wrappers.Result
        out346_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out346_

    def ctor__(self, inputCMM, inputKeys):
        d_1479_keySet_: _dafny.Set
        d_1479_keySet_ = inputKeys
        d_1480_keySeq_: _dafny.Seq
        d_1480_keySeq_ = _dafny.Seq([])
        while (d_1479_keySet_) != (_dafny.Set({})):
            d_1481_key_: _dafny.Seq
            with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                assign_such_that_1_: _dafny.Seq
                for assign_such_that_1_ in (d_1479_keySet_).Elements:
                    d_1481_key_ = assign_such_that_1_
                    if (d_1481_key_) in (d_1479_keySet_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                raise Exception("assign-such-that search produced no value (line 61)")
                pass
            d_1480_keySeq_ = (d_1480_keySeq_) + (_dafny.Seq([d_1481_key_]))
            d_1479_keySet_ = (d_1479_keySet_) - (_dafny.Set({d_1481_key_}))
        (self)._underlyingCMM = inputCMM
        (self)._requiredEncryptionContextKeys = d_1480_keySeq_

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1482_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda97_(forall_var_16_):
            d_1483_k_: _dafny.Seq = forall_var_16_
            return not ((d_1483_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1483_k_) in ((input).encryptionContext))

        d_1482_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda97_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not contain required keys.")))
        if (d_1482_valueOrError0_).IsFailure():
            output = (d_1482_valueOrError0_).PropagateFailure()
            return output
        d_1484_result_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput
        d_1485_valueOrError1_: Wrappers.Result = None
        pat_let_tv36_ = input
        def iife56_(_pat_let22_0):
            def iife57_(d_1486_dt__update__tmp_h0_):
                def iife58_(_pat_let23_0):
                    def iife59_(d_1487_dt__update_hrequiredEncryptionContextKeys_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((d_1486_dt__update__tmp_h0_).encryptionContext, (d_1486_dt__update__tmp_h0_).commitmentPolicy, (d_1486_dt__update__tmp_h0_).algorithmSuiteId, (d_1486_dt__update__tmp_h0_).maxPlaintextLength, d_1487_dt__update_hrequiredEncryptionContextKeys_h0_)
                    return iife59_(_pat_let23_0)
                return iife58_(Wrappers.Option_Some((((pat_let_tv36_).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))) + ((self).requiredEncryptionContextKeys)))
            return iife57_(_pat_let22_0)
        out347_: Wrappers.Result
        out347_ = ((self).underlyingCMM).GetEncryptionMaterials(iife56_(input))
        d_1485_valueOrError1_ = out347_
        if (d_1485_valueOrError1_).IsFailure():
            output = (d_1485_valueOrError1_).PropagateFailure()
            return output
        d_1484_result_ = (d_1485_valueOrError1_).Extract()
        d_1488_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda98_(forall_var_17_):
            d_1489_k_: _dafny.Seq = forall_var_17_
            return not ((d_1489_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1489_k_) in (((d_1484_result_).encryptionMaterials).requiredEncryptionContextKeys))

        d_1488_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda98_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Expected encryption context keys do not exist in keys to only authenticate.")))
        if (d_1488_valueOrError2_).IsFailure():
            output = (d_1488_valueOrError2_).PropagateFailure()
            return output
        d_1490_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1490_valueOrError3_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1484_result_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1490_valueOrError3_).IsFailure():
            output = (d_1490_valueOrError3_).PropagateFailure()
            return output
        d_1491_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1491_valueOrError4_ = Wrappers.default__.Need(CMM.default__.RequiredEncryptionContextKeys_q((input).requiredEncryptionContextKeys, (d_1484_result_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1491_valueOrError4_).IsFailure():
            output = (d_1491_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1484_result_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1492_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1492_valueOrError0_ = Wrappers.default__.Need(((input).reproducedEncryptionContext).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No reproduced encryption context on decrypt.")))
        if (d_1492_valueOrError0_).IsFailure():
            output = (d_1492_valueOrError0_).PropagateFailure()
            return output
        d_1493_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1493_valueOrError1_ = Wrappers.default__.Need(CMM.default__.ReproducedEncryptionContext_q(input), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
        if (d_1493_valueOrError1_).IsFailure():
            output = (d_1493_valueOrError1_).PropagateFailure()
            return output
        d_1494_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda99_(forall_var_18_):
            d_1495_k_: _dafny.Seq = forall_var_18_
            return not ((d_1495_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1495_k_) in (((input).reproducedEncryptionContext).value))

        d_1494_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda99_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing required keys.")))
        if (d_1494_valueOrError2_).IsFailure():
            output = (d_1494_valueOrError2_).PropagateFailure()
            return output
        d_1496_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsOutput
        d_1497_valueOrError3_: Wrappers.Result = None
        out348_: Wrappers.Result
        out348_ = ((self).underlyingCMM).DecryptMaterials(input)
        d_1497_valueOrError3_ = out348_
        if (d_1497_valueOrError3_).IsFailure():
            output = (d_1497_valueOrError3_).PropagateFailure()
            return output
        d_1496_result_ = (d_1497_valueOrError3_).Extract()
        d_1498_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda100_(forall_var_19_):
            d_1499_k_: _dafny.Seq = forall_var_19_
            return not ((d_1499_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1499_k_) in (((d_1496_result_).decryptionMaterials).encryptionContext))

        d_1498_valueOrError4_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda100_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Final encryption context missing required keys.")))
        if (d_1498_valueOrError4_).IsFailure():
            output = (d_1498_valueOrError4_).PropagateFailure()
            return output
        d_1500_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1500_valueOrError5_ = Wrappers.default__.Need(CMM.default__.EncryptionContextComplete(input, (d_1496_result_).decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing from encryption context.")))
        if (d_1500_valueOrError5_).IsFailure():
            output = (d_1500_valueOrError5_).PropagateFailure()
            return output
        d_1501_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1501_valueOrError6_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey((d_1496_result_).decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1501_valueOrError6_).IsFailure():
            output = (d_1501_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1496_result_)
        return output
        return output

    @property
    def underlyingCMM(self):
        return self._underlyingCMM
    @property
    def requiredEncryptionContextKeys(self):
        return self._requiredEncryptionContextKeys
