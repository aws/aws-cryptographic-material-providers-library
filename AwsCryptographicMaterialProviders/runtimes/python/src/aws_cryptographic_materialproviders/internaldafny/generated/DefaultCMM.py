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
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.primitives.internaldafny.types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software.amazon.cryptography.keystore.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
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
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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

# Module: DefaultCMM


class DefaultCMM(CMM.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager):
    def  __init__(self):
        self._keyring: software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring = None
        self._cryptoPrimitives: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "DefaultCMM.DefaultCMM"
    def GetEncryptionMaterials(self, input):
        out210_: Wrappers.Result
        out210_ = software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out210_

    def DecryptMaterials(self, input):
        out211_: Wrappers.Result
        out211_ = software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out211_

    def OfKeyring(self, k, c):
        (self)._keyring = k
        (self)._cryptoPrimitives = c

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1148_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1148_valueOrError0_ = Wrappers.default__.Need((Materials.default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reserved Field found in EncryptionContext keys.")))
        if (d_1148_valueOrError0_).IsFailure():
            output = (d_1148_valueOrError0_).PropagateFailure()
            return output
        d_1149_algorithmId_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId
        d_1149_algorithmId_ = (((input).algorithmSuiteId).value if ((input).algorithmSuiteId).is_Some else Defaults.default__.GetAlgorithmSuiteForCommitmentPolicy((input).commitmentPolicy))
        d_1150_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1150_valueOrError1_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt(d_1149_algorithmId_, (input).commitmentPolicy)
        if (d_1150_valueOrError1_).IsFailure():
            output = (d_1150_valueOrError1_).PropagateFailure()
            return output
        d_1151_suite_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo
        d_1151_suite_ = AlgorithmSuites.default__.GetSuite(d_1149_algorithmId_)
        d_1152_signingKey_: Wrappers.Option = Wrappers.Option.default()()
        d_1153_verificationKey_: Wrappers.Option = Wrappers.Option.default()()
        if ((d_1151_suite_).signature).is_ECDSA:
            d_1154_maybeECDSAPair_: Wrappers.Result
            out212_: Wrappers.Result
            out212_ = ((self).cryptoPrimitives).GenerateECDSASignatureKey(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput((((d_1151_suite_).signature).ECDSA).curve))
            d_1154_maybeECDSAPair_ = out212_
            d_1155_pair_: software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput
            d_1156_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.default())()
            def lambda94_(d_1157_e_):
                return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_1157_e_)

            d_1156_valueOrError2_ = (d_1154_maybeECDSAPair_).MapFailure(lambda94_)
            if (d_1156_valueOrError2_).IsFailure():
                output = (d_1156_valueOrError2_).PropagateFailure()
                return output
            d_1155_pair_ = (d_1156_valueOrError2_).Extract()
            d_1152_signingKey_ = Wrappers.Option_Some((d_1155_pair_).signingKey)
            d_1153_verificationKey_ = Wrappers.Option_Some((d_1155_pair_).verificationKey)
        elif True:
            d_1152_signingKey_ = Wrappers.Option_None()
            d_1153_verificationKey_ = Wrappers.Option_None()
        d_1158_materials_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials
        d_1159_valueOrError3_: Wrappers.Result = None
        d_1159_valueOrError3_ = Materials.default__.InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1149_algorithmId_, (input).encryptionContext, ((input).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])), d_1152_signingKey_, d_1153_verificationKey_))
        if (d_1159_valueOrError3_).IsFailure():
            output = (d_1159_valueOrError3_).PropagateFailure()
            return output
        d_1158_materials_ = (d_1159_valueOrError3_).Extract()
        d_1160_result_: software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput
        d_1161_valueOrError4_: Wrappers.Result = None
        out213_: Wrappers.Result
        out213_ = ((self).keyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput_OnEncryptInput(d_1158_materials_))
        d_1161_valueOrError4_ = out213_
        if (d_1161_valueOrError4_).IsFailure():
            output = (d_1161_valueOrError4_).PropagateFailure()
            return output
        d_1160_result_ = (d_1161_valueOrError4_).Extract()
        d_1162_encryptionMaterialsOutput_: software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput
        d_1162_encryptionMaterialsOutput_ = software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput((d_1160_result_).materials)
        d_1163_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1163_valueOrError5_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1162_encryptionMaterialsOutput_).encryptionMaterials), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1163_valueOrError5_).IsFailure():
            output = (d_1163_valueOrError5_).PropagateFailure()
            return output
        d_1164_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1164_valueOrError6_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_1158_materials_, (d_1162_encryptionMaterialsOutput_).encryptionMaterials), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1164_valueOrError6_).IsFailure():
            output = (d_1164_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1162_encryptionMaterialsOutput_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1165_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1165_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithmSuiteId, (input).commitmentPolicy)
        if (d_1165_valueOrError0_).IsFailure():
            output = (d_1165_valueOrError0_).PropagateFailure()
            return output
        d_1166_requiredEncryptionContextKeys_: _dafny.Seq
        d_1166_requiredEncryptionContextKeys_ = _dafny.Seq([])
        if ((input).reproducedEncryptionContext).is_Some:
            d_1167_keysSet_: _dafny.Set
            d_1167_keysSet_ = (((input).reproducedEncryptionContext).value).keys
            while (d_1167_keysSet_) != (_dafny.Set({})):
                d_1168_key_: _dafny.Seq
                with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                    assign_such_that_0_: _dafny.Seq
                    for assign_such_that_0_ in (d_1167_keysSet_).Elements:
                        d_1168_key_ = assign_such_that_0_
                        if (d_1168_key_) in (d_1167_keysSet_):
                            raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                    raise Exception("assign-such-that search produced no value (line 491)")
                    pass
                if (d_1168_key_) in ((input).encryptionContext):
                    d_1169_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_1169_valueOrError1_ = Wrappers.default__.Need(((((input).reproducedEncryptionContext).value)[d_1168_key_]) == (((input).encryptionContext)[d_1168_key_]), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
                    if (d_1169_valueOrError1_).IsFailure():
                        output = (d_1169_valueOrError1_).PropagateFailure()
                        return output
                elif True:
                    d_1166_requiredEncryptionContextKeys_ = (d_1166_requiredEncryptionContextKeys_) + (_dafny.Seq([d_1168_key_]))
                d_1167_keysSet_ = (d_1167_keysSet_) - (_dafny.Set({d_1168_key_}))
        d_1170_materials_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
        d_1171_valueOrError2_: Wrappers.Result = None
        d_1171_valueOrError2_ = Materials.default__.InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput((input).algorithmSuiteId, ((input).encryptionContext) | (((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))), d_1166_requiredEncryptionContextKeys_))
        if (d_1171_valueOrError2_).IsFailure():
            output = (d_1171_valueOrError2_).PropagateFailure()
            return output
        d_1170_materials_ = (d_1171_valueOrError2_).Extract()
        d_1172_result_: software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput
        d_1173_valueOrError3_: Wrappers.Result = None
        out214_: Wrappers.Result
        out214_ = ((self).keyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput_OnDecryptInput(d_1170_materials_, (input).encryptedDataKeys))
        d_1173_valueOrError3_ = out214_
        if (d_1173_valueOrError3_).IsFailure():
            output = (d_1173_valueOrError3_).PropagateFailure()
            return output
        d_1172_result_ = (d_1173_valueOrError3_).Extract()
        d_1174_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1174_valueOrError4_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid(d_1170_materials_, (d_1172_result_).materials), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1174_valueOrError4_).IsFailure():
            output = (d_1174_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput_DecryptMaterialsOutput((d_1172_result_).materials))
        return output
        return output

    @property
    def keyring(self):
        return self._keyring
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
