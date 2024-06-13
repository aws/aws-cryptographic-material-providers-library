import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment

# Module: DefaultCMM


class DefaultCMM(CMM.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager):
    def  __init__(self):
        self._i_keyring: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "DefaultCMM.DefaultCMM"
    def DecryptMaterials(self, input):
        out212_: Wrappers.Result
        out212_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out212_

    def GetEncryptionMaterials(self, input):
        out213_: Wrappers.Result
        out213_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out213_

    def OfKeyring(self, k, c):
        (self)._i_keyring = k
        (self)._i_cryptoPrimitives = c

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1203_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1203_valueOrError0_ = Wrappers.default__.Need((Materials.default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reserved Field found in EncryptionContext keys.")))
        if (d_1203_valueOrError0_).IsFailure():
            output = (d_1203_valueOrError0_).PropagateFailure()
            return output
        d_1204_algorithmId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_1204_algorithmId_ = (((input).algorithmSuiteId).value if ((input).algorithmSuiteId).is_Some else Defaults.default__.GetAlgorithmSuiteForCommitmentPolicy((input).commitmentPolicy))
        d_1205_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1205_valueOrError1_ = Commitment.default__.ValidateCommitmentPolicyOnEncrypt(d_1204_algorithmId_, (input).commitmentPolicy)
        if (d_1205_valueOrError1_).IsFailure():
            output = (d_1205_valueOrError1_).PropagateFailure()
            return output
        d_1206_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1206_suite_ = AlgorithmSuites.default__.GetSuite(d_1204_algorithmId_)
        d_1207_signingKey_: Wrappers.Option = Wrappers.Option.default()()
        d_1208_verificationKey_: Wrappers.Option = Wrappers.Option.default()()
        if ((d_1206_suite_).signature).is_ECDSA:
            d_1209_maybeECDSAPair_: Wrappers.Result
            out214_: Wrappers.Result
            out214_ = ((self).cryptoPrimitives).GenerateECDSASignatureKey(AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput((((d_1206_suite_).signature).ECDSA).curve))
            d_1209_maybeECDSAPair_ = out214_
            d_1210_pair_: AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput
            d_1211_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput.default())()
            def lambda102_(d_1212_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1212_e_)

            d_1211_valueOrError2_ = (d_1209_maybeECDSAPair_).MapFailure(lambda102_)
            if (d_1211_valueOrError2_).IsFailure():
                output = (d_1211_valueOrError2_).PropagateFailure()
                return output
            d_1210_pair_ = (d_1211_valueOrError2_).Extract()
            d_1207_signingKey_ = Wrappers.Option_Some((d_1210_pair_).signingKey)
            d_1208_verificationKey_ = Wrappers.Option_Some((d_1210_pair_).verificationKey)
        elif True:
            d_1207_signingKey_ = Wrappers.Option_None()
            d_1208_verificationKey_ = Wrappers.Option_None()
        d_1213_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1214_valueOrError3_: Wrappers.Result = None
        d_1214_valueOrError3_ = Materials.default__.InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1204_algorithmId_, (input).encryptionContext, ((input).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])), d_1207_signingKey_, d_1208_verificationKey_))
        if (d_1214_valueOrError3_).IsFailure():
            output = (d_1214_valueOrError3_).PropagateFailure()
            return output
        d_1213_materials_ = (d_1214_valueOrError3_).Extract()
        d_1215_result_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_1216_valueOrError4_: Wrappers.Result = None
        out215_: Wrappers.Result
        out215_ = ((self).keyring).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1213_materials_))
        d_1216_valueOrError4_ = out215_
        if (d_1216_valueOrError4_).IsFailure():
            output = (d_1216_valueOrError4_).PropagateFailure()
            return output
        d_1215_result_ = (d_1216_valueOrError4_).Extract()
        d_1217_encryptionMaterialsOutput_: AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsOutput
        d_1217_encryptionMaterialsOutput_ = AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput((d_1215_result_).materials)
        d_1218_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1218_valueOrError5_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1217_encryptionMaterialsOutput_).encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1218_valueOrError5_).IsFailure():
            output = (d_1218_valueOrError5_).PropagateFailure()
            return output
        d_1219_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1219_valueOrError6_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_1213_materials_, (d_1217_encryptionMaterialsOutput_).encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1219_valueOrError6_).IsFailure():
            output = (d_1219_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1217_encryptionMaterialsOutput_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1220_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1220_valueOrError0_ = Commitment.default__.ValidateCommitmentPolicyOnDecrypt((input).algorithmSuiteId, (input).commitmentPolicy)
        if (d_1220_valueOrError0_).IsFailure():
            output = (d_1220_valueOrError0_).PropagateFailure()
            return output
        d_1221_requiredEncryptionContextKeys_: _dafny.Seq
        d_1221_requiredEncryptionContextKeys_ = _dafny.Seq([])
        if ((input).reproducedEncryptionContext).is_Some:
            d_1222_keysSet_: _dafny.Set
            d_1222_keysSet_ = (((input).reproducedEncryptionContext).value).keys
            while (d_1222_keysSet_) != (_dafny.Set({})):
                d_1223_key_: _dafny.Seq
                with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                    assign_such_that_0_: _dafny.Seq
                    for assign_such_that_0_ in (d_1222_keysSet_).Elements:
                        d_1223_key_ = assign_such_that_0_
                        if UTF8.ValidUTF8Bytes._Is(d_1223_key_):
                            if (d_1223_key_) in (d_1222_keysSet_):
                                raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                    raise Exception("assign-such-that search produced no value (line 491)")
                    pass
                if (d_1223_key_) in ((input).encryptionContext):
                    d_1224_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_1224_valueOrError1_ = Wrappers.default__.Need(((((input).reproducedEncryptionContext).value)[d_1223_key_]) == (((input).encryptionContext)[d_1223_key_]), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
                    if (d_1224_valueOrError1_).IsFailure():
                        output = (d_1224_valueOrError1_).PropagateFailure()
                        return output
                elif True:
                    d_1221_requiredEncryptionContextKeys_ = (d_1221_requiredEncryptionContextKeys_) + (_dafny.Seq([d_1223_key_]))
                d_1222_keysSet_ = (d_1222_keysSet_) - (_dafny.Set({d_1223_key_}))
        d_1225_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1226_valueOrError2_: Wrappers.Result = None
        d_1226_valueOrError2_ = Materials.default__.InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput((input).algorithmSuiteId, ((input).encryptionContext) | (((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))), d_1221_requiredEncryptionContextKeys_))
        if (d_1226_valueOrError2_).IsFailure():
            output = (d_1226_valueOrError2_).PropagateFailure()
            return output
        d_1225_materials_ = (d_1226_valueOrError2_).Extract()
        d_1227_result_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_1228_valueOrError3_: Wrappers.Result = None
        out216_: Wrappers.Result
        out216_ = ((self).keyring).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1225_materials_, (input).encryptedDataKeys))
        d_1228_valueOrError3_ = out216_
        if (d_1228_valueOrError3_).IsFailure():
            output = (d_1228_valueOrError3_).PropagateFailure()
            return output
        d_1227_result_ = (d_1228_valueOrError3_).Extract()
        d_1229_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1229_valueOrError4_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid(d_1225_materials_, (d_1227_result_).materials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1229_valueOrError4_).IsFailure():
            output = (d_1229_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput_DecryptMaterialsOutput((d_1227_result_).materials))
        return output
        return output

    @property
    def keyring(self):
        return self._i_keyring
    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives
