import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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

# Module: MultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AttemptDecryptDataKey(keyring, input):
        res: Wrappers.Result = None
        d_65_output_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_66_valueOrError0_: Wrappers.Result = None
        out10_: Wrappers.Result
        out10_ = (keyring).OnDecrypt(input)
        d_66_valueOrError0_ = out10_
        if (d_66_valueOrError0_).IsFailure():
            res = (d_66_valueOrError0_).PropagateFailure()
            return res
        d_65_output_ = (d_66_valueOrError0_).Extract()
        d_67_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_67_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsTransitionIsValid((input).materials, (d_65_output_).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring performed invalid material transition")))
        if (d_67_valueOrError1_).IsFailure():
            res = (d_67_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_65_output_)
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
        out11_: Wrappers.Result
        out11_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out11_

    def OnDecrypt(self, input):
        out12_: Wrappers.Result
        out12_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out12_

    def ctor__(self, generatorKeyring, childKeyrings):
        (self)._generatorKeyring = generatorKeyring
        (self)._childKeyrings = childKeyrings

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if (((self).generatorKeyring).is_None) and ((((input).materials).plaintextDataKey).is_None):
            d_68_exception_: _dafny.Seq
            d_68_exception_ = _dafny.Seq("Need either a generator keyring or input encryption materials which contain a plaintext data key")
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_68_exception_))
            return res
        d_69_returnMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_69_returnMaterials_ = (input).materials
        if ((self).generatorKeyring).is_Some:
            d_70_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_70_valueOrError0_ = Wrappers.default__.Need((((input).materials).plaintextDataKey).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("This multi keyring has a generator but provided Encryption Materials already contain plaintext data key")))
            if (d_70_valueOrError0_).IsFailure():
                res = (d_70_valueOrError0_).PropagateFailure()
                return res
            d_71_onEncryptOutput_: Wrappers.Result
            out13_: Wrappers.Result
            out13_ = (((self).generatorKeyring).value).OnEncrypt(input)
            d_71_onEncryptOutput_ = out13_
            d_72_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_72_valueOrError1_ = Wrappers.default__.Need((d_71_onEncryptOutput_).is_Success, ((d_71_onEncryptOutput_).error if (d_71_onEncryptOutput_).is_Failure else software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected failure. Input to Need is !Success."))))
            if (d_72_valueOrError1_).IsFailure():
                res = (d_72_valueOrError1_).PropagateFailure()
                return res
            d_73_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_73_valueOrError2_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, ((d_71_onEncryptOutput_).value).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Generator keyring returned invalid encryption materials")))
            if (d_73_valueOrError2_).IsFailure():
                res = (d_73_valueOrError2_).PropagateFailure()
                return res
            d_69_returnMaterials_ = ((d_71_onEncryptOutput_).value).materials
        hi0_ = len((self).childKeyrings)
        for d_74_i_ in range(0, hi0_):
            d_75_onEncryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput
            d_75_onEncryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_69_returnMaterials_)
            d_76_onEncryptOutput_: Wrappers.Result
            out14_: Wrappers.Result
            out14_ = (((self).childKeyrings)[d_74_i_]).OnEncrypt(d_75_onEncryptInput_)
            d_76_onEncryptOutput_ = out14_
            d_77_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_77_valueOrError3_ = Wrappers.default__.Need((d_76_onEncryptOutput_).is_Success, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring failed to encrypt plaintext data key")))
            if (d_77_valueOrError3_).IsFailure():
                res = (d_77_valueOrError3_).PropagateFailure()
                return res
            d_78_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_78_valueOrError4_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition(d_69_returnMaterials_, ((d_76_onEncryptOutput_).value).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Child keyring performed invalid transition on encryption materials")))
            if (d_78_valueOrError4_).IsFailure():
                res = (d_78_valueOrError4_).PropagateFailure()
                return res
            d_69_returnMaterials_ = ((d_76_onEncryptOutput_).value).materials
        d_79_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_79_valueOrError5_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterialsTransition((input).materials, d_69_returnMaterials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A child or generator keyring modified the encryption materials in illegal ways.")))
        if (d_79_valueOrError5_).IsFailure():
            res = (d_79_valueOrError5_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_69_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_80_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_80_materials_ = (input).materials
        d_81_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_81_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey((input).materials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_81_valueOrError0_).IsFailure():
            res = (d_81_valueOrError0_).PropagateFailure()
            return res
        d_82_failures_: _dafny.Seq
        d_82_failures_ = _dafny.Seq([])
        if ((self).generatorKeyring).is_Some:
            d_83_result_: Wrappers.Result
            out15_: Wrappers.Result
            out15_ = default__.AttemptDecryptDataKey(((self).generatorKeyring).value, input)
            d_83_result_ = out15_
            if (d_83_result_).is_Success:
                if ((((d_83_result_).value).materials).plaintextDataKey).is_Some:
                    res = Wrappers.Result_Success((d_83_result_).value)
                    return res
            elif True:
                d_82_failures_ = (d_82_failures_) + (_dafny.Seq([(d_83_result_).error]))
        hi1_ = len((self).childKeyrings)
        for d_84_j_ in range(0, hi1_):
            d_85_result_: Wrappers.Result
            out16_: Wrappers.Result
            out16_ = default__.AttemptDecryptDataKey(((self).childKeyrings)[d_84_j_], input)
            d_85_result_ = out16_
            if (d_85_result_).is_Success:
                res = Wrappers.Result_Success((d_85_result_).value)
                return res
            elif True:
                d_82_failures_ = (d_82_failures_) + (_dafny.Seq([(d_85_result_).error]))
        d_86_combinedResult_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_86_combinedResult_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_82_failures_, _dafny.Seq("No Configured Keyring was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))
        res = Wrappers.Result_Failure(d_86_combinedResult_)
        return res
        return res

    @property
    def generatorKeyring(self):
        return self._generatorKeyring
    @property
    def childKeyrings(self):
        return self._childKeyrings
