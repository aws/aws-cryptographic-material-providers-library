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

assert "MultiKeyring" == __name__
MultiKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AttemptDecryptDataKey(keyring, input):
        res: Wrappers.Result = None
        d_655_output_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_656_valueOrError0_: Wrappers.Result = None
        out167_: Wrappers.Result
        out167_ = (keyring).OnDecrypt(input)
        d_656_valueOrError0_ = out167_
        if (d_656_valueOrError0_).IsFailure():
            res = (d_656_valueOrError0_).PropagateFailure()
            return res
        d_655_output_ = (d_656_valueOrError0_).Extract()
        d_657_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_657_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).materials, (d_655_output_).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring performed invalid material transition")))
        if (d_657_valueOrError1_).IsFailure():
            res = (d_657_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_655_output_)
        return res
        return res


class MultiKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._generatorKeyring: Wrappers.Option = Wrappers.Option_None.default()()
        self._childKeyrings: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "MultiKeyring.MultiKeyring"
    def OnEncrypt(self, input):
        out168_: Wrappers.Result
        out168_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out168_

    def OnDecrypt(self, input):
        out169_: Wrappers.Result
        out169_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out169_

    def ctor__(self, generatorKeyring, childKeyrings):
        (self)._generatorKeyring = generatorKeyring
        (self)._childKeyrings = childKeyrings

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if (((self).generatorKeyring).is_None) and ((((input).materials).plaintextDataKey).is_None):
            d_658_exception_: _dafny.Seq
            d_658_exception_ = _dafny.Seq("Need either a generator keyring or input encryption materials which contain a plaintext data key")
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_658_exception_))
            return res
        d_659_returnMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_659_returnMaterials_ = (input).materials
        if ((self).generatorKeyring).is_Some:
            d_660_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_660_valueOrError0_ = Wrappers.default__.Need((((input).materials).plaintextDataKey).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("This multi keyring has a generator but provided Encryption Materials already contain plaintext data key")))
            if (d_660_valueOrError0_).IsFailure():
                res = (d_660_valueOrError0_).PropagateFailure()
                return res
            d_661_onEncryptOutput_: Wrappers.Result
            out170_: Wrappers.Result
            out170_ = (((self).generatorKeyring).value).OnEncrypt(input)
            d_661_onEncryptOutput_ = out170_
            d_662_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_662_valueOrError1_ = Wrappers.default__.Need((d_661_onEncryptOutput_).is_Success, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Generator keyring failed to generate plaintext data key")))
            if (d_662_valueOrError1_).IsFailure():
                res = (d_662_valueOrError1_).PropagateFailure()
                return res
            d_663_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_663_valueOrError2_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, ((d_661_onEncryptOutput_).value).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Generator keyring returned invalid encryption materials")))
            if (d_663_valueOrError2_).IsFailure():
                res = (d_663_valueOrError2_).PropagateFailure()
                return res
            d_659_returnMaterials_ = ((d_661_onEncryptOutput_).value).materials
        hi1_: int = len((self).childKeyrings)
        for d_664_i_ in range(0, hi1_):
            d_665_onEncryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput
            d_665_onEncryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_659_returnMaterials_)
            d_666_onEncryptOutput_: Wrappers.Result
            out171_: Wrappers.Result
            out171_ = (((self).childKeyrings)[d_664_i_]).OnEncrypt(d_665_onEncryptInput_)
            d_666_onEncryptOutput_ = out171_
            d_667_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_667_valueOrError3_ = Wrappers.default__.Need((d_666_onEncryptOutput_).is_Success, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring failed to encrypt plaintext data key")))
            if (d_667_valueOrError3_).IsFailure():
                res = (d_667_valueOrError3_).PropagateFailure()
                return res
            d_668_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_668_valueOrError4_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_659_returnMaterials_, ((d_666_onEncryptOutput_).value).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring performed invalid transition on encryption materials")))
            if (d_668_valueOrError4_).IsFailure():
                res = (d_668_valueOrError4_).PropagateFailure()
                return res
            d_659_returnMaterials_ = ((d_666_onEncryptOutput_).value).materials
        d_669_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_669_valueOrError5_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, d_659_returnMaterials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A child or generator keyring modified the encryption materials in illegal ways.")))
        if (d_669_valueOrError5_).IsFailure():
            res = (d_669_valueOrError5_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_659_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_670_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_670_materials_ = (input).materials
        d_671_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_671_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey((input).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_671_valueOrError0_).IsFailure():
            res = (d_671_valueOrError0_).PropagateFailure()
            return res
        d_672_failures_: _dafny.Seq
        d_672_failures_ = _dafny.Seq([])
        if ((self).generatorKeyring).is_Some:
            d_673_result_: Wrappers.Result
            out172_: Wrappers.Result
            out172_ = MultiKeyring.default__.AttemptDecryptDataKey(((self).generatorKeyring).value, input)
            d_673_result_ = out172_
            if (d_673_result_).is_Success:
                if ((((d_673_result_).value).materials).plaintextDataKey).is_Some:
                    res = Wrappers.Result_Success((d_673_result_).value)
                    return res
            elif True:
                d_672_failures_ = (d_672_failures_) + (_dafny.Seq([(d_673_result_).error]))
        hi2_: int = len((self).childKeyrings)
        for d_674_j_ in range(0, hi2_):
            d_675_result_: Wrappers.Result
            out173_: Wrappers.Result
            out173_ = MultiKeyring.default__.AttemptDecryptDataKey(((self).childKeyrings)[d_674_j_], input)
            d_675_result_ = out173_
            if (d_675_result_).is_Success:
                res = Wrappers.Result_Success((d_675_result_).value)
                return res
            elif True:
                d_672_failures_ = (d_672_failures_) + (_dafny.Seq([(d_675_result_).error]))
        d_676_combinedResult_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_676_combinedResult_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_672_failures_, _dafny.Seq("No Configured Keyring was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))
        res = Wrappers.Result_Failure(d_676_combinedResult_)
        return res
        return res

    @property
    def generatorKeyring(self):
        return self._generatorKeyring
    @property
    def childKeyrings(self):
        return self._childKeyrings
