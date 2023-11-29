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
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny

# assert "TestComAmazonawsKms" == __name__
TestComAmazonawsKms = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def workAround(literal):
        return literal

    @staticmethod
    def BasicDecryptTests():
        d_1_CiphertextBlob_: _dafny.Seq
        d_1_CiphertextBlob_ = _dafny.Seq([1, 1, 1, 0, 120, 64, 243, 140, 39, 94, 49, 9, 116, 22, 193, 7, 41, 81, 80, 87, 25, 100, 173, 163, 239, 28, 33, 233, 76, 139, 160, 189, 188, 157, 15, 180, 20, 0, 0, 0, 98, 48, 96, 6, 9, 42, 134, 72, 134, 247, 13, 1, 7, 6, 160, 83, 48, 81, 2, 1, 0, 48, 76, 6, 9, 42, 134, 72, 134, 247, 13, 1, 7, 1, 48, 30, 6, 9, 96, 134, 72, 1, 101, 3, 4, 1, 46, 48, 17, 4, 12, 196, 249, 60, 7, 21, 231, 87, 70, 216, 12, 31, 13, 2, 1, 16, 128, 31, 222, 119, 162, 112, 88, 153, 39, 197, 21, 182, 116, 176, 120, 174, 107, 82, 182, 223, 160, 201, 15, 29, 3, 254, 3, 208, 72, 171, 64, 207, 175])
        TestComAmazonawsKms.default__.BasicDecryptTest(software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest(TestComAmazonawsKms.default__.workAround(d_1_CiphertextBlob_), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some((TestComAmazonawsKms.default__).keyId), Wrappers.Option_None()), _dafny.Seq([165, 191, 67, 62]), (TestComAmazonawsKms.default__).keyId)

    @staticmethod
    def BasicGenerateTests():
        TestComAmazonawsKms.default__.BasicGenerateTest(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest_GenerateDataKeyRequest((TestComAmazonawsKms.default__).keyId, Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def BasicEncryptTests():
        TestComAmazonawsKms.default__.BasicEncryptTest(software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest_EncryptRequest((TestComAmazonawsKms.default__).keyId, _dafny.Seq([97, 115, 100, 102]), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def BasicDecryptTest(input, expectedPlaintext, expectedKeyId):
        d_2_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_3_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        print(software_amazon_cryptography_services_kms_internaldafny.default__)
        print(software_amazon_cryptography_services_kms_internaldafny.default__.__dict__)
        out0_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_3_valueOrError0_ = out0_
        if not(not((d_3_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(88,15): " + _dafny.string_of(d_3_valueOrError0_))
        d_2_client_ = (d_3_valueOrError0_).Extract()
        d_4_ret_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_2_client_).Decrypt(input)
        d_4_ret_ = out1_
        _dafny.print(_dafny.string_of(d_4_ret_))
        if not((d_4_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(94,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs0_ = (d_4_ret_).value
        d_5_KeyId_ = let_tmp_rhs0_.KeyId
        d_6_Plaintext_ = let_tmp_rhs0_.Plaintext
        d_7_EncryptionAlgorithm_ = let_tmp_rhs0_.EncryptionAlgorithm
        if not((d_6_Plaintext_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(98,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_5_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_6_Plaintext_).value) == (expectedPlaintext)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(100,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_5_KeyId_).value) == (expectedKeyId)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicGenerateTest(input):
        d_8_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_9_valueOrError0_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_9_valueOrError0_ = out2_
        if not(not((d_9_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(109,15): " + _dafny.string_of(d_9_valueOrError0_))
        d_8_client_ = (d_9_valueOrError0_).Extract()
        d_10_ret_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_8_client_).GenerateDataKey(input)
        d_10_ret_ = out3_
        if not((d_10_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs1_ = (d_10_ret_).value
        d_11_CiphertextBlob_ = let_tmp_rhs1_.CiphertextBlob
        d_12_Plaintext_ = let_tmp_rhs1_.Plaintext
        d_13_KeyId_ = let_tmp_rhs1_.KeyId
        if not((d_11_CiphertextBlob_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(117,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_12_Plaintext_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_13_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(119,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_12_Plaintext_).value)) == (((input).NumberOfBytes).value)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(120,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_14_decryptInput_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_14_decryptInput_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((d_11_CiphertextBlob_).value, (input).EncryptionContext, (input).GrantTokens, Wrappers.Option_Some((d_13_KeyId_).value), Wrappers.Option_None())
        TestComAmazonawsKms.default__.BasicDecryptTest(d_14_decryptInput_, (d_12_Plaintext_).value, (input).KeyId)

    @staticmethod
    def BasicEncryptTest(input):
        d_15_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_16_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_16_valueOrError0_ = out4_
        if not(not((d_16_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(141,15): " + _dafny.string_of(d_16_valueOrError0_))
        d_15_client_ = (d_16_valueOrError0_).Extract()
        d_17_ret_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_15_client_).Encrypt(input)
        d_17_ret_ = out5_
        if not((d_17_ret_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(145,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs2_ = (d_17_ret_).value
        d_18_CiphertextBlob_ = let_tmp_rhs2_.CiphertextBlob
        d_19_KeyId_ = let_tmp_rhs2_.KeyId
        d_20_EncryptionAlgorithm_ = let_tmp_rhs2_.EncryptionAlgorithm
        if not((d_18_CiphertextBlob_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_19_KeyId_).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_21_decryptInput_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_21_decryptInput_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((d_18_CiphertextBlob_).value, (input).EncryptionContext, (input).GrantTokens, Wrappers.Option_Some((d_19_KeyId_).value), (input).EncryptionAlgorithm)
        TestComAmazonawsKms.default__.BasicDecryptTest(d_21_decryptInput_, (input).Plaintext, (input).KeyId)

    @staticmethod
    def RegionMatchTest():
        d_22_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_23_valueOrError0_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_23_valueOrError0_ = out6_
        if not(not((d_23_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(170,15): " + _dafny.string_of(d_23_valueOrError0_))
        d_22_client_ = (d_23_valueOrError0_).Extract()
        d_24_region_: Wrappers.Option
        d_24_region_ = software_amazon_cryptography_services_kms_internaldafny.default__.RegionMatch(d_22_client_, (TestComAmazonawsKms.default__).TEST__REGION)
        if not(((d_24_region_).is_None) or ((d_24_region_).value)):
            raise _dafny.HaltException("test/TestComAmazonawsKms.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def keyId(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
    @_dafny.classproperty
    def TEST__REGION(instance):
        return _dafny.Seq("us-west-2")
