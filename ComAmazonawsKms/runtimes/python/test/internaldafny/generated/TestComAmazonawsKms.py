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
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_kms.internaldafny.generated.Com as Com

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
        default__.BasicDecryptTest(ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest(default__.workAround(d_0_CiphertextBlob_), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(default__.keyId), Wrappers.Option_None()), _dafny.Seq([165, 191, 67, 62]), default__.keyId)

    @staticmethod
    def BasicGenerateTests():
        default__.BasicGenerateTest(ComAmazonawsKmsTypes.GenerateDataKeyRequest_GenerateDataKeyRequest(default__.keyId, Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def BasicEncryptTests():
        default__.BasicEncryptTest(ComAmazonawsKmsTypes.EncryptRequest_EncryptRequest(default__.keyId, _dafny.Seq([97, 115, 100, 102]), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def BasicDecryptTest(input, expectedPlaintext, expectedKeyId):
        d_1_client_: ComAmazonawsKmsTypes.IKMSClient
        d_2_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_2_valueOrError0_ = out0_
        if not(not((d_2_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(88,18): " + _dafny.string_of(d_2_valueOrError0_))
        d_1_client_ = (d_2_valueOrError0_).Extract()
        d_3_ret_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_1_client_).Decrypt(input)
        d_3_ret_ = out1_
        _dafny.print(_dafny.string_of(d_3_ret_))
        if not((d_3_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(94,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs0_ = (d_3_ret_).value
        d_4_KeyId_ = let_tmp_rhs0_.KeyId
        d_5_Plaintext_ = let_tmp_rhs0_.Plaintext
        d_6_EncryptionAlgorithm_ = let_tmp_rhs0_.EncryptionAlgorithm
        if not((d_5_Plaintext_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(98,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_4_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_5_Plaintext_).value) == (expectedPlaintext)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(100,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_4_KeyId_).value) == (expectedKeyId)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicGenerateTest(input):
        d_7_client_: ComAmazonawsKmsTypes.IKMSClient
        d_8_valueOrError0_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_8_valueOrError0_ = out2_
        if not(not((d_8_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(109,18): " + _dafny.string_of(d_8_valueOrError0_))
        d_7_client_ = (d_8_valueOrError0_).Extract()
        d_9_ret_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_client_).GenerateDataKey(input)
        d_9_ret_ = out3_
        if not((d_9_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs1_ = (d_9_ret_).value
        d_10_CiphertextBlob_ = let_tmp_rhs1_.CiphertextBlob
        d_11_Plaintext_ = let_tmp_rhs1_.Plaintext
        d_12_KeyId_ = let_tmp_rhs1_.KeyId
        if not((d_10_CiphertextBlob_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(117,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_11_Plaintext_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_12_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(119,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_11_Plaintext_).value)) == (((input).NumberOfBytes).value)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(120,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_13_decryptInput_: ComAmazonawsKmsTypes.DecryptRequest
        d_13_decryptInput_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((d_10_CiphertextBlob_).value, (input).EncryptionContext, (input).GrantTokens, Wrappers.Option_Some((d_12_KeyId_).value), Wrappers.Option_None())
        default__.BasicDecryptTest(d_13_decryptInput_, (d_11_Plaintext_).value, (input).KeyId)

    @staticmethod
    def BasicEncryptTest(input):
        d_14_client_: ComAmazonawsKmsTypes.IKMSClient
        d_15_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_15_valueOrError0_ = out4_
        if not(not((d_15_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(141,18): " + _dafny.string_of(d_15_valueOrError0_))
        d_14_client_ = (d_15_valueOrError0_).Extract()
        d_16_ret_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_14_client_).Encrypt(input)
        d_16_ret_ = out5_
        if not((d_16_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(145,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs2_ = (d_16_ret_).value
        d_17_CiphertextBlob_ = let_tmp_rhs2_.CiphertextBlob
        d_18_KeyId_ = let_tmp_rhs2_.KeyId
        d_19_EncryptionAlgorithm_ = let_tmp_rhs2_.EncryptionAlgorithm
        if not((d_17_CiphertextBlob_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_18_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_20_decryptInput_: ComAmazonawsKmsTypes.DecryptRequest
        d_20_decryptInput_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((d_17_CiphertextBlob_).value, (input).EncryptionContext, (input).GrantTokens, Wrappers.Option_Some((d_18_KeyId_).value), (input).EncryptionAlgorithm)
        default__.BasicDecryptTest(d_20_decryptInput_, (input).Plaintext, (input).KeyId)

    @staticmethod
    def RegionMatchTest():
        d_21_client_: ComAmazonawsKmsTypes.IKMSClient
        d_22_valueOrError0_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(default__.TEST__REGION)
        d_22_valueOrError0_ = out6_
        if not(not((d_22_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(170,18): " + _dafny.string_of(d_22_valueOrError0_))
        d_21_client_ = (d_22_valueOrError0_).Extract()
        d_23_region_: Wrappers.Option
        d_23_region_ = Com_Amazonaws_Kms.default__.RegionMatch(d_21_client_, default__.TEST__REGION)
        if not(((d_23_region_).is_None) or ((d_23_region_).value)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def EmptyStringIsDefaultRegion():
        d_24_client_: ComAmazonawsKmsTypes.IKMSClient
        d_25_valueOrError0_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = Com_Amazonaws_Kms.default__.KMSClientForRegion(_dafny.Seq(""))
        d_25_valueOrError0_ = out7_
        if not(not((d_25_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(177,18): " + _dafny.string_of(d_25_valueOrError0_))
        d_24_client_ = (d_25_valueOrError0_).Extract()

    @_dafny.classproperty
    def TEST__REGION(instance):
        return _dafny.Seq("us-west-2")
    @_dafny.classproperty
    def keyId(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
