import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms

# Module: TestComAmazonawsKms

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def workAround(literal):
        return literal

    @staticmethod
    def BasicDecryptTests():
        d_0_CiphertextBlob_: _dafny.Seq
        d_0_CiphertextBlob_ = _dafny.Seq([1, 1, 1, 0, 120, 64, 243, 140, 39, 94, 49, 9, 116, 22, 193, 7, 41, 81, 80, 87, 25, 100, 173, 163, 239, 28, 33, 233, 76, 139, 160, 189, 188, 157, 15, 180, 20, 0, 0, 0, 98, 48, 96, 6, 9, 42, 134, 72, 134, 247, 13, 1, 7, 6, 160, 83, 48, 81, 2, 1, 0, 48, 76, 6, 9, 42, 134, 72, 134, 247, 13, 1, 7, 1, 48, 30, 6, 9, 96, 134, 72, 1, 101, 3, 4, 1, 46, 48, 17, 4, 12, 196, 249, 60, 7, 21, 231, 87, 70, 216, 12, 31, 13, 2, 1, 16, 128, 31, 222, 119, 162, 112, 88, 153, 39, 197, 21, 182, 116, 176, 120, 174, 107, 82, 182, 223, 160, 201, 15, 29, 3, 254, 3, 208, 72, 171, 64, 207, 175])
        default__.BasicDecryptTest(ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest(default__.workAround(d_0_CiphertextBlob_), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(default__.keyId), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()), _dafny.Seq([165, 191, 67, 62]), default__.keyId)

    @staticmethod
    def BasicGenerateTests():
        default__.BasicGenerateTest(ComAmazonawsKmsTypes.GenerateDataKeyRequest_GenerateDataKeyRequest(default__.keyId, Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def BasicGenerateWithoutPlaintextTests():
        default__.BasicGenerateWithoutPlaintextTest(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest(default__.keyIdGenerateWOPlain, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def BasicEncryptTests():
        default__.BasicEncryptTest(ComAmazonawsKmsTypes.EncryptRequest_EncryptRequest(default__.keyId, _dafny.Seq([97, 115, 100, 102]), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def BasicFailTests():
        d_1_client_: ComAmazonawsKmsTypes.IKMSClient
        d_2_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_2_valueOrError0_ = out0_
        if not(not((d_2_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(117,18): " + _dafny.string_of(d_2_valueOrError0_))
        d_1_client_ = (d_2_valueOrError0_).Extract()
        d_3_ret_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_1_client_).GenerateDataKeyWithoutPlaintext(default__.failingInput)
        d_3_ret_ = out1_
        if not((d_3_ret_).is_Failure):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(119,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_4_err_: ComAmazonawsKmsTypes.Error
        d_4_err_ = (d_3_ret_).error
        if not((d_4_err_).is_Opaque):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(121,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = d_4_err_
        unmatched0 = True
        if unmatched0:
            if source0_.is_Opaque:
                d_5_obj_ = source0_.obj
                unmatched0 = False
                if not(True):
                    raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(123,26): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched0:
            unmatched0 = False
            if not(False):
                raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(124,16): " + _dafny.string_of(_dafny.Seq("Failing KMS Key MUST cause an OpaqueError that can later be unwrapped to a proper but generic KMS Exception.")))

    @staticmethod
    def BasicDecryptTest(input, expectedPlaintext, expectedKeyId):
        d_6_client_: ComAmazonawsKmsTypes.IKMSClient
        d_7_valueOrError0_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_7_valueOrError0_ = out2_
        if not(not((d_7_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(134,18): " + _dafny.string_of(d_7_valueOrError0_))
        d_6_client_ = (d_7_valueOrError0_).Extract()
        d_8_ret_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_6_client_).Decrypt(input)
        d_8_ret_ = out3_
        if not((d_8_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(140,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs0_ = (d_8_ret_).value
        d_9_KeyId_ = let_tmp_rhs0_.KeyId
        d_10_Plaintext_ = let_tmp_rhs0_.Plaintext
        d_11_EncryptionAlgorithm_ = let_tmp_rhs0_.EncryptionAlgorithm
        d_12_CiphertextBlob_ = let_tmp_rhs0_.CiphertextForRecipient
        if not((d_10_Plaintext_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(144,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_9_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(145,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_10_Plaintext_).value) == (expectedPlaintext)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_9_KeyId_).value) == (expectedKeyId)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(147,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicGenerateTest(input):
        d_13_client_: ComAmazonawsKmsTypes.IKMSClient
        d_14_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_14_valueOrError0_ = out4_
        if not(not((d_14_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(155,18): " + _dafny.string_of(d_14_valueOrError0_))
        d_13_client_ = (d_14_valueOrError0_).Extract()
        d_15_ret_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_13_client_).GenerateDataKey(input)
        d_15_ret_ = out5_
        if not((d_15_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(159,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs1_ = (d_15_ret_).value
        d_16_CiphertextBlob_ = let_tmp_rhs1_.CiphertextBlob
        d_17_Plaintext_ = let_tmp_rhs1_.Plaintext
        d_18_KeyId_ = let_tmp_rhs1_.KeyId
        d_19_CiphertextForRecipient_ = let_tmp_rhs1_.CiphertextForRecipient
        if not((d_16_CiphertextBlob_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(163,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_17_Plaintext_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(164,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_18_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_17_Plaintext_).value)) == (((input).NumberOfBytes).value)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(166,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_20_decryptInput_: ComAmazonawsKmsTypes.DecryptRequest
        d_20_decryptInput_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((d_16_CiphertextBlob_).value, (input).EncryptionContext, (input).GrantTokens, Wrappers.Option_Some((d_18_KeyId_).value), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        default__.BasicDecryptTest(d_20_decryptInput_, (d_17_Plaintext_).value, (input).KeyId)

    @staticmethod
    def BasicGenerateWithoutPlaintextTest(input):
        d_21_client_: ComAmazonawsKmsTypes.IKMSClient
        d_22_valueOrError0_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_22_valueOrError0_ = out6_
        if not(not((d_22_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(188,18): " + _dafny.string_of(d_22_valueOrError0_))
        d_21_client_ = (d_22_valueOrError0_).Extract()
        d_23_retGenerate_: Wrappers.Result
        out7_: Wrappers.Result
        out7_ = (d_21_client_).GenerateDataKeyWithoutPlaintext(input)
        d_23_retGenerate_ = out7_
        if not((d_23_retGenerate_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(192,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs2_ = (d_23_retGenerate_).value
        d_24_CiphertextBlob_ = let_tmp_rhs2_.CiphertextBlob
        d_25_KeyId_ = let_tmp_rhs2_.KeyId
        if not((d_24_CiphertextBlob_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(196,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_25_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(197,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_26_decryptInput_: ComAmazonawsKmsTypes.DecryptRequest
        d_26_decryptInput_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((d_24_CiphertextBlob_).value, (input).EncryptionContext, (input).GrantTokens, Wrappers.Option_Some((d_25_KeyId_).value), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_27_ret_: Wrappers.Result
        out8_: Wrappers.Result
        out8_ = (d_21_client_).Decrypt(d_26_decryptInput_)
        d_27_ret_ = out8_
        if not((d_27_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(208,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs3_ = (d_27_ret_).value
        d_28_KeyIdTwo_ = let_tmp_rhs3_.KeyId
        d_29_Plaintext_ = let_tmp_rhs3_.Plaintext
        d_30_EncryptionAlgorithm_ = let_tmp_rhs3_.EncryptionAlgorithm
        d_31_CiphertextBlobTwo_ = let_tmp_rhs3_.CiphertextForRecipient
        if not((d_28_KeyIdTwo_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(211,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_28_KeyIdTwo_).value) == ((d_25_KeyId_).value)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(212,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicEncryptTest(input):
        d_32_client_: ComAmazonawsKmsTypes.IKMSClient
        d_33_valueOrError0_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_33_valueOrError0_ = out9_
        if not(not((d_33_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(219,18): " + _dafny.string_of(d_33_valueOrError0_))
        d_32_client_ = (d_33_valueOrError0_).Extract()
        d_34_ret_: Wrappers.Result
        out10_: Wrappers.Result
        out10_ = (d_32_client_).Encrypt(input)
        d_34_ret_ = out10_
        if not((d_34_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(223,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs4_ = (d_34_ret_).value
        d_35_CiphertextBlob_ = let_tmp_rhs4_.CiphertextBlob
        d_36_KeyId_ = let_tmp_rhs4_.KeyId
        d_37_EncryptionAlgorithm_ = let_tmp_rhs4_.EncryptionAlgorithm
        if not((d_35_CiphertextBlob_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(227,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_36_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(228,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_38_decryptInput_: ComAmazonawsKmsTypes.DecryptRequest
        d_38_decryptInput_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((d_35_CiphertextBlob_).value, (input).EncryptionContext, (input).GrantTokens, Wrappers.Option_Some((d_36_KeyId_).value), (input).EncryptionAlgorithm, Wrappers.Option_None(), Wrappers.Option_None())
        default__.BasicDecryptTest(d_38_decryptInput_, (input).Plaintext, (input).KeyId)

    @staticmethod
    def RegionMatchTest():
        d_39_client_: ComAmazonawsKmsTypes.IKMSClient
        d_40_valueOrError0_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_40_valueOrError0_ = out11_
        if not(not((d_40_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(248,18): " + _dafny.string_of(d_40_valueOrError0_))
        d_39_client_ = (d_40_valueOrError0_).Extract()
        d_41_region_: Wrappers.Option
        d_41_region_ = Com_Amazonaws_Kms.default__.RegionMatch(d_39_client_, default__.TEST__REGION)
        if not(((d_41_region_).is_None) or ((d_41_region_).value)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(250,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def EmptyStringIsDefaultRegion():
        d_42_client_: ComAmazonawsKmsTypes.IKMSClient
        d_43_valueOrError0_: Wrappers.Result = None
        out12_: Wrappers.Result
        out12_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(_dafny.Seq(""))
        d_43_valueOrError0_ = out12_
        if not(not((d_43_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(255,18): " + _dafny.string_of(d_43_valueOrError0_))
        d_42_client_ = (d_43_valueOrError0_).Extract()

    @staticmethod
    def BasicDeriveSharedSecretTests(input):
        d_44_client_: ComAmazonawsKmsTypes.IKMSClient
        d_45_valueOrError0_: Wrappers.Result = None
        out13_: Wrappers.Result
        out13_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_45_valueOrError0_ = out13_
        if not(not((d_45_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(262,18): " + _dafny.string_of(d_45_valueOrError0_))
        d_44_client_ = (d_45_valueOrError0_).Extract()
        d_46_ret_: Wrappers.Result
        out14_: Wrappers.Result
        out14_ = (d_44_client_).DeriveSharedSecret(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest((input).KeyId, (input).KeyAgreementAlgorithm, (input).PublicKey, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_46_ret_ = out14_
        if (d_46_ret_).is_Success:
            let_tmp_rhs5_ = (d_46_ret_).value
            d_47_KeyId_ = let_tmp_rhs5_.KeyId
            d_48_SharedSecret_ = let_tmp_rhs5_.SharedSecret
            d_49_CiphertextForRecipient_ = let_tmp_rhs5_.CiphertextForRecipient
            d_50_KeyAgreementAlgorithm_ = let_tmp_rhs5_.KeyAgreementAlgorithm
            d_51_KeyOrigin_ = let_tmp_rhs5_.KeyOrigin
            if not((d_48_SharedSecret_).is_Some):
                raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(275,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not((d_47_KeyId_).is_Some):
                raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(276,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_47_KeyId_).value) == ((input).KeyId)):
                raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(278,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        elif True:
            if not((d_46_ret_).is_Failure):
                raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(281,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GetPublicKeyHelper(input):
        publicKey: _dafny.Seq = None
        d_52_client_: ComAmazonawsKmsTypes.IKMSClient
        d_53_valueOrError0_: Wrappers.Result = None
        out15_: Wrappers.Result
        out15_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_53_valueOrError0_ = out15_
        if not(not((d_53_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(292,18): " + _dafny.string_of(d_53_valueOrError0_))
        d_52_client_ = (d_53_valueOrError0_).Extract()
        d_54_ret_: Wrappers.Result
        out16_: Wrappers.Result
        out16_ = (d_52_client_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((input).KeyId, (input).GrantTokens))
        d_54_ret_ = out16_
        if not((d_54_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(299,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs6_ = (d_54_ret_).value
        d_55___v1_ = let_tmp_rhs6_.KeyId
        d_56_PublicKey_ = let_tmp_rhs6_.PublicKey
        d_57___v2_ = let_tmp_rhs6_.CustomerMasterKeySpec
        d_58___v3_ = let_tmp_rhs6_.KeySpec
        d_59___v4_ = let_tmp_rhs6_.KeyUsage
        d_60___v5_ = let_tmp_rhs6_.EncryptionAlgorithms
        d_61___v6_ = let_tmp_rhs6_.SigningAlgorithms
        d_62___v7_ = let_tmp_rhs6_.KeyAgreementAlgorithms
        if not((d_56_PublicKey_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(302,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        publicKey = (d_56_PublicKey_).value
        return publicKey
        return publicKey

    @staticmethod
    def DeriveSharedSecretTestSuccess():
        d_63_recipientPublicKey_: _dafny.Seq
        out17_: _dafny.Seq
        out17_ = default__.GetPublicKeyHelper(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(default__.recipientKmsKey, Wrappers.Option_None()))
        d_63_recipientPublicKey_ = out17_
        default__.BasicDeriveSharedSecretTests(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(default__.senderKmsKey, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), d_63_recipientPublicKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def DeriveSharedSecretTestFailure():
        d_64_recipientPublicKeyOnWrongCurve_: _dafny.Seq
        out18_: _dafny.Seq
        out18_ = default__.GetPublicKeyHelper(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(default__.incorrectEccCurveKey, Wrappers.Option_None()))
        d_64_recipientPublicKeyOnWrongCurve_ = out18_
        default__.BasicDeriveSharedSecretTests(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(default__.senderKmsKey, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), d_64_recipientPublicKeyOnWrongCurve_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def CreateNoneForEncryptionContext():
        return Wrappers.Option_None()

    @staticmethod
    def CreateNoneForKeySpec():
        return Wrappers.Option_None()

    @staticmethod
    def CreateNoneForNumberOfBytes():
        return Wrappers.Option_None()

    @staticmethod
    def CreateNoneForGrantTokens():
        return Wrappers.Option_None()

    @staticmethod
    def CreateNoneForDryRun():
        return Wrappers.Option_None()

    @_dafny.classproperty
    def TEST__REGION(instance):
        return _dafny.Seq("us-west-2")
    @_dafny.classproperty
    def keyId(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
    @_dafny.classproperty
    def keyIdGenerateWOPlain(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126")
    @_dafny.classproperty
    def failingKeyId(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/e20ac7b8-3d95-46ee-b3d5-f5dca6393945")
    @_dafny.classproperty
    def failingInput(instance):
        return ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest(default__.failingKeyId, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_None(), Wrappers.Option_None())
    @_dafny.classproperty
    def recipientKmsKey(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5")
    @_dafny.classproperty
    def senderKmsKey(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9")
    @_dafny.classproperty
    def incorrectEccCurveKey(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/7f35a704-f4fb-469d-98b1-62a1fa2cc44e")
