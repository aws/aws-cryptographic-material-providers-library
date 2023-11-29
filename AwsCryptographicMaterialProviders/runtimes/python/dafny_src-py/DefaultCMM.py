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
        out261_: Wrappers.Result
        out261_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out261_

    def DecryptMaterials(self, input):
        out262_: Wrappers.Result
        out262_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out262_

    def OfKeyring(self, k, c):
        (self)._keyring = k
        (self)._cryptoPrimitives = c

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1251_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1251_valueOrError0_ = Wrappers.default__.Need(((Materials.default__).EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reserved Field found in EncryptionContext keys.")))
        if (d_1251_valueOrError0_).IsFailure():
            output = (d_1251_valueOrError0_).PropagateFailure()
            return output
        d_1252_algorithmId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_1252_algorithmId_ = (((input).algorithmSuiteId).value if ((input).algorithmSuiteId).is_Some else Defaults.default__.GetAlgorithmSuiteForCommitmentPolicy((input).commitmentPolicy))
        d_1253_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1253_valueOrError1_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt(d_1252_algorithmId_, (input).commitmentPolicy)
        if (d_1253_valueOrError1_).IsFailure():
            output = (d_1253_valueOrError1_).PropagateFailure()
            return output
        d_1254_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1254_suite_ = AlgorithmSuites.default__.GetSuite(d_1252_algorithmId_)
        d_1255_signingKey_: Wrappers.Option = Wrappers.Option_None.default()()
        d_1256_verificationKey_: Wrappers.Option = Wrappers.Option_None.default()()
        if ((d_1254_suite_).signature).is_ECDSA:
            d_1257_maybeECDSAPair_: Wrappers.Result
            out263_: Wrappers.Result
            out263_ = ((self).cryptoPrimitives).GenerateECDSASignatureKey(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput((((d_1254_suite_).signature).ECDSA).curve))
            d_1257_maybeECDSAPair_ = out263_
            d_1258_pair_: software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput
            d_1259_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
            def lambda94_(d_1260_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1260_e_)

            d_1259_valueOrError2_ = (d_1257_maybeECDSAPair_).MapFailure(lambda94_)
            if (d_1259_valueOrError2_).IsFailure():
                output = (d_1259_valueOrError2_).PropagateFailure()
                return output
            d_1258_pair_ = (d_1259_valueOrError2_).Extract()
            d_1255_signingKey_ = Wrappers.Option_Some((d_1258_pair_).signingKey)
            d_1256_verificationKey_ = Wrappers.Option_Some((d_1258_pair_).verificationKey)
        elif True:
            d_1255_signingKey_ = Wrappers.Option_None()
            d_1256_verificationKey_ = Wrappers.Option_None()
        d_1261_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1262_valueOrError3_: Wrappers.Result = None
        d_1262_valueOrError3_ = Materials.default__.InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1252_algorithmId_, (input).encryptionContext, ((input).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])), d_1255_signingKey_, d_1256_verificationKey_))
        if (d_1262_valueOrError3_).IsFailure():
            output = (d_1262_valueOrError3_).PropagateFailure()
            return output
        d_1261_materials_ = (d_1262_valueOrError3_).Extract()
        d_1263_result_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_1264_valueOrError4_: Wrappers.Result = None
        out264_: Wrappers.Result
        out264_ = ((self).keyring).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_1261_materials_))
        d_1264_valueOrError4_ = out264_
        if (d_1264_valueOrError4_).IsFailure():
            output = (d_1264_valueOrError4_).PropagateFailure()
            return output
        d_1263_result_ = (d_1264_valueOrError4_).Extract()
        d_1265_encryptionMaterialsOutput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput
        d_1265_encryptionMaterialsOutput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput((d_1263_result_).materials)
        d_1266_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1266_valueOrError5_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1265_encryptionMaterialsOutput_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1266_valueOrError5_).IsFailure():
            output = (d_1266_valueOrError5_).PropagateFailure()
            return output
        d_1267_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1267_valueOrError6_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_1261_materials_, (d_1265_encryptionMaterialsOutput_).encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1267_valueOrError6_).IsFailure():
            output = (d_1267_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1265_encryptionMaterialsOutput_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1268_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1268_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithmSuiteId, (input).commitmentPolicy)
        if (d_1268_valueOrError0_).IsFailure():
            output = (d_1268_valueOrError0_).PropagateFailure()
            return output
        d_1269_requiredEncryptionContextKeys_: _dafny.Seq
        d_1269_requiredEncryptionContextKeys_ = _dafny.Seq([])
        if ((input).reproducedEncryptionContext).is_Some:
            d_1270_keysSet_: _dafny.Set
            d_1270_keysSet_ = (((input).reproducedEncryptionContext).value).keys
            while (d_1270_keysSet_) != (_dafny.Set({})):
                d_1271_key_: _dafny.Seq
                with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                    assign_such_that_0_: _dafny.Seq
                    for assign_such_that_0_ in (d_1270_keysSet_).Elements:
                        d_1271_key_ = assign_such_that_0_
                        if (d_1271_key_) in (d_1270_keysSet_):
                            raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                    raise Exception("assign-such-that search produced no value (line 491)")
                    pass
                if (d_1271_key_) in ((input).encryptionContext):
                    d_1272_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
                    d_1272_valueOrError1_ = Wrappers.default__.Need(((((input).reproducedEncryptionContext).value)[d_1271_key_]) == (((input).encryptionContext)[d_1271_key_]), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
                    if (d_1272_valueOrError1_).IsFailure():
                        output = (d_1272_valueOrError1_).PropagateFailure()
                        return output
                elif True:
                    d_1269_requiredEncryptionContextKeys_ = (d_1269_requiredEncryptionContextKeys_) + (_dafny.Seq([d_1271_key_]))
                d_1270_keysSet_ = (d_1270_keysSet_) - (_dafny.Set({d_1271_key_}))
        d_1273_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1274_valueOrError2_: Wrappers.Result = None
        d_1274_valueOrError2_ = Materials.default__.InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput((input).algorithmSuiteId, ((input).encryptionContext) | (((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))), d_1269_requiredEncryptionContextKeys_))
        if (d_1274_valueOrError2_).IsFailure():
            output = (d_1274_valueOrError2_).PropagateFailure()
            return output
        d_1273_materials_ = (d_1274_valueOrError2_).Extract()
        d_1275_result_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_1276_valueOrError3_: Wrappers.Result = None
        out265_: Wrappers.Result
        out265_ = ((self).keyring).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_1273_materials_, (input).encryptedDataKeys))
        d_1276_valueOrError3_ = out265_
        if (d_1276_valueOrError3_).IsFailure():
            output = (d_1276_valueOrError3_).PropagateFailure()
            return output
        d_1275_result_ = (d_1276_valueOrError3_).Extract()
        d_1277_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1277_valueOrError4_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid(d_1273_materials_, (d_1275_result_).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1277_valueOrError4_).IsFailure():
            output = (d_1277_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsOutput_DecryptMaterialsOutput((d_1275_result_).materials))
        return output
        return output

    @property
    def keyring(self):
        return self._keyring
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
