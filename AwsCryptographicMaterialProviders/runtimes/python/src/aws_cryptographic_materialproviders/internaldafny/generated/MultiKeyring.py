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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
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
import software_amazon_cryptography_keystore_internaldafny_types
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
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring

# Module: MultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AttemptDecryptDataKey(keyring, input):
        res: Wrappers.Result = None
        d_370_output_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_371_valueOrError0_: Wrappers.Result = None
        out54_: Wrappers.Result
        out54_ = (keyring).OnDecrypt(input)
        d_371_valueOrError0_ = out54_
        if (d_371_valueOrError0_).IsFailure():
            res = (d_371_valueOrError0_).PropagateFailure()
            return res
        d_370_output_ = (d_371_valueOrError0_).Extract()
        d_372_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_372_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).materials, (d_370_output_).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring performed invalid material transition")))
        if (d_372_valueOrError1_).IsFailure():
            res = (d_372_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_370_output_)
        return res
        return res


class MultiKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._generatorKeyring: Wrappers.Option = Wrappers.Option.default()()
        self._childKeyrings: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "MultiKeyring.MultiKeyring"
    def OnEncrypt(self, input):
        out55_: Wrappers.Result
        out55_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out55_

    def OnDecrypt(self, input):
        out56_: Wrappers.Result
        out56_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out56_

    def ctor__(self, generatorKeyring, childKeyrings):
        (self)._generatorKeyring = generatorKeyring
        (self)._childKeyrings = childKeyrings

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if (((self).generatorKeyring).is_None) and ((((input).materials).plaintextDataKey).is_None):
            d_373_exception_: _dafny.Seq
            d_373_exception_ = _dafny.Seq("Need either a generator keyring or input encryption materials which contain a plaintext data key")
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_373_exception_))
            return res
        d_374_returnMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_374_returnMaterials_ = (input).materials
        if ((self).generatorKeyring).is_Some:
            d_375_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_375_valueOrError0_ = Wrappers.default__.Need((((input).materials).plaintextDataKey).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("This multi keyring has a generator but provided Encryption Materials already contain plaintext data key")))
            if (d_375_valueOrError0_).IsFailure():
                res = (d_375_valueOrError0_).PropagateFailure()
                return res
            d_376_onEncryptOutput_: Wrappers.Result
            out57_: Wrappers.Result
            out57_ = (((self).generatorKeyring).value).OnEncrypt(input)
            d_376_onEncryptOutput_ = out57_
            d_377_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_377_valueOrError1_ = Wrappers.default__.Need((d_376_onEncryptOutput_).is_Success, ((d_376_onEncryptOutput_).error if (d_376_onEncryptOutput_).is_Failure else software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected failure. Input to Need is !Success."))))
            if (d_377_valueOrError1_).IsFailure():
                res = (d_377_valueOrError1_).PropagateFailure()
                return res
            d_378_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_378_valueOrError2_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, ((d_376_onEncryptOutput_).value).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Generator keyring returned invalid encryption materials")))
            if (d_378_valueOrError2_).IsFailure():
                res = (d_378_valueOrError2_).PropagateFailure()
                return res
            d_374_returnMaterials_ = ((d_376_onEncryptOutput_).value).materials
        hi0_ = len((self).childKeyrings)
        for d_379_i_ in range(0, hi0_):
            d_380_onEncryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput
            d_380_onEncryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_374_returnMaterials_)
            d_381_onEncryptOutput_: Wrappers.Result
            out58_: Wrappers.Result
            out58_ = (((self).childKeyrings)[d_379_i_]).OnEncrypt(d_380_onEncryptInput_)
            d_381_onEncryptOutput_ = out58_
            d_382_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_382_valueOrError3_ = Wrappers.default__.Need((d_381_onEncryptOutput_).is_Success, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring failed to encrypt plaintext data key")))
            if (d_382_valueOrError3_).IsFailure():
                res = (d_382_valueOrError3_).PropagateFailure()
                return res
            d_383_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_383_valueOrError4_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_374_returnMaterials_, ((d_381_onEncryptOutput_).value).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring performed invalid transition on encryption materials")))
            if (d_383_valueOrError4_).IsFailure():
                res = (d_383_valueOrError4_).PropagateFailure()
                return res
            d_374_returnMaterials_ = ((d_381_onEncryptOutput_).value).materials
        d_384_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_384_valueOrError5_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, d_374_returnMaterials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A child or generator keyring modified the encryption materials in illegal ways.")))
        if (d_384_valueOrError5_).IsFailure():
            res = (d_384_valueOrError5_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_374_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_385_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_385_materials_ = (input).materials
        d_386_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_386_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey((input).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_386_valueOrError0_).IsFailure():
            res = (d_386_valueOrError0_).PropagateFailure()
            return res
        d_387_failures_: _dafny.Seq
        d_387_failures_ = _dafny.Seq([])
        if ((self).generatorKeyring).is_Some:
            d_388_result_: Wrappers.Result
            out59_: Wrappers.Result
            out59_ = default__.AttemptDecryptDataKey(((self).generatorKeyring).value, input)
            d_388_result_ = out59_
            if (d_388_result_).is_Success:
                if ((((d_388_result_).value).materials).plaintextDataKey).is_Some:
                    res = Wrappers.Result_Success((d_388_result_).value)
                    return res
            elif True:
                d_387_failures_ = (d_387_failures_) + (_dafny.Seq([(d_388_result_).error]))
        hi1_ = len((self).childKeyrings)
        for d_389_j_ in range(0, hi1_):
            d_390_result_: Wrappers.Result
            out60_: Wrappers.Result
            out60_ = default__.AttemptDecryptDataKey(((self).childKeyrings)[d_389_j_], input)
            d_390_result_ = out60_
            if (d_390_result_).is_Success:
                res = Wrappers.Result_Success((d_390_result_).value)
                return res
            elif True:
                d_387_failures_ = (d_387_failures_) + (_dafny.Seq([(d_390_result_).error]))
        d_391_combinedResult_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_391_combinedResult_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_387_failures_, _dafny.Seq("No Configured Keyring was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))
        res = Wrappers.Result_Failure(d_391_combinedResult_)
        return res
        return res

    @property
    def generatorKeyring(self):
        return self._generatorKeyring
    @property
    def childKeyrings(self):
        return self._childKeyrings
