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
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier

# Module: RequiredEncryptionContextCMM


class RequiredEncryptionContextCMM(CMM.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager):
    def  __init__(self):
        self._i_underlyingCMM: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager = None
        self._i_requiredEncryptionContextKeys: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "RequiredEncryptionContextCMM.RequiredEncryptionContextCMM"
    def DecryptMaterials(self, input):
        out219_: Wrappers.Result
        out219_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager.DecryptMaterials(self, input)
        return out219_

    def GetEncryptionMaterials(self, input):
        out220_: Wrappers.Result
        out220_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager.GetEncryptionMaterials(self, input)
        return out220_

    def ctor__(self, inputCMM, inputKeys):
        d_1232_keySet_: _dafny.Set
        d_1232_keySet_ = inputKeys
        d_1233_keySeq_: _dafny.Seq
        d_1233_keySeq_ = _dafny.Seq([])
        while (d_1232_keySet_) != (_dafny.Set({})):
            d_1234_key_: _dafny.Seq
            with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                assign_such_that_1_: _dafny.Seq
                for assign_such_that_1_ in (d_1232_keySet_).Elements:
                    d_1234_key_ = assign_such_that_1_
                    if UTF8.ValidUTF8Bytes._Is(d_1234_key_):
                        if (d_1234_key_) in (d_1232_keySet_):
                            raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                raise Exception("assign-such-that search produced no value (line 61)")
                pass
            d_1233_keySeq_ = (d_1233_keySeq_) + (_dafny.Seq([d_1234_key_]))
            d_1232_keySet_ = (d_1232_keySet_) - (_dafny.Set({d_1234_key_}))
        (self)._i_underlyingCMM = inputCMM
        (self)._i_requiredEncryptionContextKeys = d_1233_keySeq_

    def GetEncryptionMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1235_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda104_(forall_var_15_):
            d_1236_k_: _dafny.Seq = forall_var_15_
            if UTF8.ValidUTF8Bytes._Is(d_1236_k_):
                return not ((d_1236_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1236_k_) in ((input).encryptionContext))
            elif True:
                return True

        d_1235_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda104_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not contain required keys.")))
        if (d_1235_valueOrError0_).IsFailure():
            output = (d_1235_valueOrError0_).PropagateFailure()
            return output
        d_1237_result_: AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsOutput
        d_1238_valueOrError1_: Wrappers.Result = None
        pat_let_tv171_ = input
        out221_: Wrappers.Result
        def iife30_(_pat_let10_0):
            def iife31_(d_1239_dt__update__tmp_h0_):
                def iife32_(_pat_let11_0):
                    def iife33_(d_1240_dt__update_hrequiredEncryptionContextKeys_h0_):
                        return AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((d_1239_dt__update__tmp_h0_).encryptionContext, (d_1239_dt__update__tmp_h0_).commitmentPolicy, (d_1239_dt__update__tmp_h0_).algorithmSuiteId, (d_1239_dt__update__tmp_h0_).maxPlaintextLength, d_1240_dt__update_hrequiredEncryptionContextKeys_h0_)
                    return iife33_(_pat_let11_0)
                return iife32_(Wrappers.Option_Some((((pat_let_tv171_).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))) + ((self).requiredEncryptionContextKeys)))
            return iife31_(_pat_let10_0)
        out221_ = ((self).underlyingCMM).GetEncryptionMaterials(iife30_(input))
        d_1238_valueOrError1_ = out221_
        if (d_1238_valueOrError1_).IsFailure():
            output = (d_1238_valueOrError1_).PropagateFailure()
            return output
        d_1237_result_ = (d_1238_valueOrError1_).Extract()
        d_1241_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda105_(forall_var_16_):
            d_1242_k_: _dafny.Seq = forall_var_16_
            if UTF8.ValidUTF8Bytes._Is(d_1242_k_):
                return not ((d_1242_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1242_k_) in (((d_1237_result_).encryptionMaterials).requiredEncryptionContextKeys))
            elif True:
                return True

        d_1241_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda105_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Expected encryption context keys do not exist in keys to only authenticate.")))
        if (d_1241_valueOrError2_).IsFailure():
            output = (d_1241_valueOrError2_).PropagateFailure()
            return output
        d_1243_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1243_valueOrError3_ = Wrappers.default__.Need(Materials.default__.EncryptionMaterialsHasPlaintextDataKey((d_1237_result_).encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Could not retrieve materials required for encryption")))
        if (d_1243_valueOrError3_).IsFailure():
            output = (d_1243_valueOrError3_).PropagateFailure()
            return output
        d_1244_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1244_valueOrError4_ = Wrappers.default__.Need(CMM.default__.RequiredEncryptionContextKeys_q((input).requiredEncryptionContextKeys, (d_1237_result_).encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring returned an invalid response")))
        if (d_1244_valueOrError4_).IsFailure():
            output = (d_1244_valueOrError4_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1237_result_)
        return output

    def DecryptMaterials_k(self, input):
        output: Wrappers.Result = None
        d_1245_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1245_valueOrError0_ = Wrappers.default__.Need(((input).reproducedEncryptionContext).is_Some, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No reproduced encryption context on decrypt.")))
        if (d_1245_valueOrError0_).IsFailure():
            output = (d_1245_valueOrError0_).PropagateFailure()
            return output
        d_1246_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1246_valueOrError1_ = Wrappers.default__.Need(CMM.default__.ReproducedEncryptionContext_q(input), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context does not match reproduced encryption context.")))
        if (d_1246_valueOrError1_).IsFailure():
            output = (d_1246_valueOrError1_).PropagateFailure()
            return output
        d_1247_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda106_(forall_var_17_):
            d_1248_k_: _dafny.Seq = forall_var_17_
            if UTF8.ValidUTF8Bytes._Is(d_1248_k_):
                return not ((d_1248_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1248_k_) in (((input).reproducedEncryptionContext).value))
            elif True:
                return True

        d_1247_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda106_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing required keys.")))
        if (d_1247_valueOrError2_).IsFailure():
            output = (d_1247_valueOrError2_).PropagateFailure()
            return output
        d_1249_result_: AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput
        d_1250_valueOrError3_: Wrappers.Result = None
        out222_: Wrappers.Result
        out222_ = ((self).underlyingCMM).DecryptMaterials(input)
        d_1250_valueOrError3_ = out222_
        if (d_1250_valueOrError3_).IsFailure():
            output = (d_1250_valueOrError3_).PropagateFailure()
            return output
        d_1249_result_ = (d_1250_valueOrError3_).Extract()
        d_1251_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda107_(forall_var_18_):
            d_1252_k_: _dafny.Seq = forall_var_18_
            if UTF8.ValidUTF8Bytes._Is(d_1252_k_):
                return not ((d_1252_k_) in ((self).requiredEncryptionContextKeys)) or ((d_1252_k_) in (((d_1249_result_).decryptionMaterials).encryptionContext))
            elif True:
                return True

        d_1251_valueOrError4_ = Wrappers.default__.Need(_dafny.quantifier(((self).requiredEncryptionContextKeys).UniqueElements, True, lambda107_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Final encryption context missing required keys.")))
        if (d_1251_valueOrError4_).IsFailure():
            output = (d_1251_valueOrError4_).PropagateFailure()
            return output
        d_1253_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1253_valueOrError5_ = Wrappers.default__.Need(CMM.default__.EncryptionContextComplete(input, (d_1249_result_).decryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reproduced encryption context missing from encryption context.")))
        if (d_1253_valueOrError5_).IsFailure():
            output = (d_1253_valueOrError5_).PropagateFailure()
            return output
        d_1254_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1254_valueOrError6_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithPlaintextDataKey((d_1249_result_).decryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring.OnDecrypt failed to decrypt the plaintext data key.")))
        if (d_1254_valueOrError6_).IsFailure():
            output = (d_1254_valueOrError6_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1249_result_)
        return output
        return output

    @property
    def underlyingCMM(self):
        return self._i_underlyingCMM
    @property
    def requiredEncryptionContextKeys(self):
        return self._i_requiredEncryptionContextKeys
