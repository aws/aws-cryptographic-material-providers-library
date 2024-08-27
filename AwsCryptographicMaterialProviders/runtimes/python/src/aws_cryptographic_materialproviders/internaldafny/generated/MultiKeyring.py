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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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

# Module: MultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AttemptDecryptDataKey(keyring, input):
        res: Wrappers.Result = None
        d_391_output_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_392_valueOrError0_: Wrappers.Result = None
        out59_: Wrappers.Result
        out59_ = (keyring).OnDecrypt(input)
        d_392_valueOrError0_ = out59_
        if (d_392_valueOrError0_).IsFailure():
            res = (d_392_valueOrError0_).PropagateFailure()
            return res
        d_391_output_ = (d_392_valueOrError0_).Extract()
        d_393_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_393_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).materials, (d_391_output_).materials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring performed invalid material transition")))
        if (d_393_valueOrError1_).IsFailure():
            res = (d_393_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_391_output_)
        return res
        return res


class MultiKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._generatorKeyring: Wrappers.Option = Wrappers.Option.default()()
        self._childKeyrings: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "MultiKeyring.MultiKeyring"
    def OnDecrypt(self, input):
        out60_: Wrappers.Result
        out60_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out60_

    def OnEncrypt(self, input):
        out61_: Wrappers.Result
        out61_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out61_

    def ctor__(self, generatorKeyring, childKeyrings):
        (self)._generatorKeyring = generatorKeyring
        (self)._childKeyrings = childKeyrings

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if (((self).generatorKeyring).is_None) and ((((input).materials).plaintextDataKey).is_None):
            d_394_exception_: _dafny.Seq
            d_394_exception_ = _dafny.Seq("Need either a generator keyring or input encryption materials which contain a plaintext data key")
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_394_exception_))
            return res
        d_395_returnMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_395_returnMaterials_ = (input).materials
        if ((self).generatorKeyring).is_Some:
            d_396_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_396_valueOrError0_ = Wrappers.default__.Need((((input).materials).plaintextDataKey).is_None, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("This multi keyring has a generator but provided Encryption Materials already contain plaintext data key")))
            if (d_396_valueOrError0_).IsFailure():
                res = (d_396_valueOrError0_).PropagateFailure()
                return res
            d_397_onEncryptOutput_: Wrappers.Result
            out62_: Wrappers.Result
            out62_ = (((self).generatorKeyring).value).OnEncrypt(input)
            d_397_onEncryptOutput_ = out62_
            d_398_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_398_valueOrError1_ = Wrappers.default__.Need((d_397_onEncryptOutput_).is_Success, ((d_397_onEncryptOutput_).error if (d_397_onEncryptOutput_).is_Failure else AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected failure. Input to Need is !Success."))))
            if (d_398_valueOrError1_).IsFailure():
                res = (d_398_valueOrError1_).PropagateFailure()
                return res
            d_399_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_399_valueOrError2_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, ((d_397_onEncryptOutput_).value).materials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Generator keyring returned invalid encryption materials")))
            if (d_399_valueOrError2_).IsFailure():
                res = (d_399_valueOrError2_).PropagateFailure()
                return res
            d_395_returnMaterials_ = ((d_397_onEncryptOutput_).value).materials
        hi0_ = len((self).childKeyrings)
        for d_400_i_ in range(0, hi0_):
            d_401_onEncryptInput_: AwsCryptographyMaterialProvidersTypes.OnEncryptInput
            d_401_onEncryptInput_ = AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_395_returnMaterials_)
            d_402_onEncryptOutput_: Wrappers.Result
            out63_: Wrappers.Result
            out63_ = (((self).childKeyrings)[d_400_i_]).OnEncrypt(d_401_onEncryptInput_)
            d_402_onEncryptOutput_ = out63_
            d_403_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_403_valueOrError3_ = Wrappers.default__.Need((d_402_onEncryptOutput_).is_Success, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring failed to encrypt plaintext data key")))
            if (d_403_valueOrError3_).IsFailure():
                res = (d_403_valueOrError3_).PropagateFailure()
                return res
            d_404_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_404_valueOrError4_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_395_returnMaterials_, ((d_402_onEncryptOutput_).value).materials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring performed invalid transition on encryption materials")))
            if (d_404_valueOrError4_).IsFailure():
                res = (d_404_valueOrError4_).PropagateFailure()
                return res
            d_395_returnMaterials_ = ((d_402_onEncryptOutput_).value).materials
        d_405_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_405_valueOrError5_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, d_395_returnMaterials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A child or generator keyring modified the encryption materials in illegal ways.")))
        if (d_405_valueOrError5_).IsFailure():
            res = (d_405_valueOrError5_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_395_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_406_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_406_materials_ = (input).materials
        d_407_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_407_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey((input).materials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_407_valueOrError0_).IsFailure():
            res = (d_407_valueOrError0_).PropagateFailure()
            return res
        d_408_failures_: _dafny.Seq
        d_408_failures_ = _dafny.Seq([])
        if ((self).generatorKeyring).is_Some:
            d_409_result_: Wrappers.Result
            out64_: Wrappers.Result
            out64_ = default__.AttemptDecryptDataKey(((self).generatorKeyring).value, input)
            d_409_result_ = out64_
            if (d_409_result_).is_Success:
                if ((((d_409_result_).value).materials).plaintextDataKey).is_Some:
                    res = Wrappers.Result_Success((d_409_result_).value)
                    return res
            elif True:
                d_408_failures_ = (d_408_failures_) + (_dafny.Seq([(d_409_result_).error]))
        hi1_ = len((self).childKeyrings)
        for d_410_j_ in range(0, hi1_):
            d_411_result_: Wrappers.Result
            out65_: Wrappers.Result
            out65_ = default__.AttemptDecryptDataKey(((self).childKeyrings)[d_410_j_], input)
            d_411_result_ = out65_
            if (d_411_result_).is_Success:
                res = Wrappers.Result_Success((d_411_result_).value)
                return res
            elif True:
                d_408_failures_ = (d_408_failures_) + (_dafny.Seq([(d_411_result_).error]))
        d_412_combinedResult_: AwsCryptographyMaterialProvidersTypes.Error
        d_412_combinedResult_ = AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_408_failures_, _dafny.Seq("No Configured Keyring was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))
        res = Wrappers.Result_Failure(d_412_combinedResult_)
        return res
        return res

    @property
    def generatorKeyring(self):
        return self._generatorKeyring
    @property
    def childKeyrings(self):
        return self._childKeyrings