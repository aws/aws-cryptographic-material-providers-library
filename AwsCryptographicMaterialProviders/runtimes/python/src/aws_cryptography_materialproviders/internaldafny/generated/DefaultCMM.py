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

assert "DefaultCMM" == __name__
DefaultCMM = sys.modules[__name__]


class DefaultCMM(CMM.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager):
    def  __init__(self):
        self._keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "DefaultCMM.DefaultCMM"
    def GetEncryptionMaterials(self, input):
        out338_: Wrappers.Result
        out338_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out338_

    def DecryptMaterials(self, input):
        out339_: Wrappers.Result
        out339_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out339_

    def OfKeyring(self, k, c):
        (self)._keyring = k
        (self)._cryptoPrimitives = c

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1450_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1450_valueOrError0_ = Wrappers.default__.Need(((Materials.default__).EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reserved Field found in EncryptionContext keys.")))
        if (d_1450_valueOrError0_).IsFailure():
            output = (d_1450_valueOrError0_).PropagateFailure()
            return output
        d_1451_algorithmId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1451_algorithmId_ = (((input).algorithmSuiteId).value if ((input).algorithmSuiteId).is_Some else Defaults.default__.GetAlgorithmSuiteForCommitmentPolicy((input).commitmentPolicy))
        d_1452_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1452_valueOrError1_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt(d_1451_algorithmId_, (input).commitmentPolicy)
        if (d_1452_valueOrError1_).IsFailure():
            output = (d_1452_valueOrError1_).PropagateFailure()
            return output
        d_1453_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1453_suite_ = AlgorithmSuites.default__.GetSuite(d_1451_algorithmId_)
        d_1454_signingKey_: Wrappers.Option = Wrappers.Option_None.default()()
        d_1455_verificationKey_: Wrappers.Option = Wrappers.Option_None.default()()
        if ((d_1453_suite_).signature).is_ECDSA:
            d_1456_maybeECDSAPair_: Wrappers.Result
            out340_: Wrappers.Result
            out340_ = ((self).cryptoPrimitives).GenerateECDSASignatureKey(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput((((d_1453_suite_).signature).ECDSA).curve))
            d_1456_maybeECDSAPair_ = out340_
            d_1457_pair_: software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput
            d_1458_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
            def lambda95_(d_1459_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1459_e_)

            d_1458_valueOrError2_ = (d_1456_maybeECDSAPair_).MapFailure(lambda95_)
            if (d_1458_valueOrError2_).IsFailure():
                output = (d_1458_valueOrError2_).PropagateFailure()
                return output
            d_1457_pair_ = (d_1458_valueOrError2_).Extract()
            d_1454_signingKey_ = Wrappers.Option_Some((d_1457_pair_).signingKey)
            d_1455_verificationKey_ = Wrappers.Option_Some((d_1457_pair_).verificationKey)
        elif True:
            d_1454_signingKey_ = Wrappers.Option_None()
            d_1455_verificationKey_ = Wrappers.Option_None()
        d_1460_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1461_valueOrError3_: Wrappers.Result = None
        d_1461_valueOrError3_ = Materials.default__.InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1451_algorithmId_, (input).encryptionContext, ((input).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])), d_1454_signingKey_, d_1455_verificationKey_))
        if (d_1461_valueOrError3_).IsFailure():
            output = (d_1461_valueOrError3_).PropagateFailure()
            return output
        d_1460_materials_ = (d_1461_valueOrError3_).Extract()
        d_1462_result_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1463_valueOrError4_: Wrappers.Result = None
        out341_: Wrappers.Result
        out341_ = ((self).keyring).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1460_materials_))
        d_1463_valueOrError4_ = out341_
        if (d_1463_valueOrError4_).IsFailure():
            output = (d_1463_valueOrError4_).PropagateFailure()
            return output
        d_1462_result_ = (d_1463_valueOrError4_).Extract()
        d_1464_encryptionMaterialsOutput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput
        d_1464_encryptionMaterialsOutput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput((d_1462_result_).materials)
        d_1465_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1465_valueOrError5_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1464_encryptionMaterialsOutput_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1465_valueOrError5_).IsFailure():
            output = (d_1465_valueOrError5_).PropagateFailure()
            return output
        d_1466_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1466_valueOrError6_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_1460_materials_, (d_1464_encryptionMaterialsOutput_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1466_valueOrError6_).IsFailure():
            output = (d_1466_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1464_encryptionMaterialsOutput_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1467_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1467_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithmSuiteId, (input).commitmentPolicy)
        if (d_1467_valueOrError0_).IsFailure():
            output = (d_1467_valueOrError0_).PropagateFailure()
            return output
        d_1468_requiredEncryptionContextKeys_: _dafny.Seq
        d_1468_requiredEncryptionContextKeys_ = _dafny.Seq([])
        if ((input).reproducedEncryptionContext).is_Some:
            d_1469_keysSet_: _dafny.Set
            d_1469_keysSet_ = (((input).reproducedEncryptionContext).value).keys
            while (d_1469_keysSet_) != (_dafny.Set({})):
                d_1470_key_: _dafny.Seq
                with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                    assign_such_that_0_: _dafny.Seq
                    for assign_such_that_0_ in (d_1469_keysSet_).Elements:
                        d_1470_key_ = assign_such_that_0_
                        if (d_1470_key_) in (d_1469_keysSet_):
                            raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                    raise Exception("assign-such-that search produced no value (line 491)")
                    pass
                if (d_1470_key_) in ((input).encryptionContext):
                    d_1471_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
                    d_1471_valueOrError1_ = Wrappers.default__.Need(((((input).reproducedEncryptionContext).value)[d_1470_key_]) == (((input).encryptionContext)[d_1470_key_]), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
                    if (d_1471_valueOrError1_).IsFailure():
                        output = (d_1471_valueOrError1_).PropagateFailure()
                        return output
                elif True:
                    d_1468_requiredEncryptionContextKeys_ = (d_1468_requiredEncryptionContextKeys_) + (_dafny.Seq([d_1470_key_]))
                d_1469_keysSet_ = (d_1469_keysSet_) - (_dafny.Set({d_1470_key_}))
        d_1472_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1473_valueOrError2_: Wrappers.Result = None
        d_1473_valueOrError2_ = Materials.default__.InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput((input).algorithmSuiteId, ((input).encryptionContext) | (((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))), d_1468_requiredEncryptionContextKeys_))
        if (d_1473_valueOrError2_).IsFailure():
            output = (d_1473_valueOrError2_).PropagateFailure()
            return output
        d_1472_materials_ = (d_1473_valueOrError2_).Extract()
        d_1474_result_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1475_valueOrError3_: Wrappers.Result = None
        out342_: Wrappers.Result
        out342_ = ((self).keyring).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1472_materials_, (input).encryptedDataKeys))
        d_1475_valueOrError3_ = out342_
        if (d_1475_valueOrError3_).IsFailure():
            output = (d_1475_valueOrError3_).PropagateFailure()
            return output
        d_1474_result_ = (d_1475_valueOrError3_).Extract()
        d_1476_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1476_valueOrError4_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid(d_1472_materials_, (d_1474_result_).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1476_valueOrError4_).IsFailure():
            output = (d_1476_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsOutput_DecryptMaterialsOutput((d_1474_result_).materials))
        return output
        return output

    @property
    def keyring(self):
        return self._keyring
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
