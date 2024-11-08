// Package TestComAmazonawsKms
// Dafny module TestComAmazonawsKms compiled into Go

package TestComAmazonawsKms

import (
	os "os"

	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/kms/ComAmazonawsKmsTypes"
	m_Com_Amazonaws_Kms "github.com/aws/aws-cryptographic-material-providers-library/kms/Com_Amazonaws_Kms"
	m__System "github.com/dafny-lang/DafnyRuntimeGo/v4/System_"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	m_Actions "github.com/dafny-lang/DafnyStandardLibGo/Actions"
	m_Base64 "github.com/dafny-lang/DafnyStandardLibGo/Base64"
	m_Base64Lemmas "github.com/dafny-lang/DafnyStandardLibGo/Base64Lemmas"
	m_BoundedInts "github.com/dafny-lang/DafnyStandardLibGo/BoundedInts"
	m_DivInternals "github.com/dafny-lang/DafnyStandardLibGo/DivInternals"
	m_DivInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/DivInternalsNonlinear"
	m_DivMod "github.com/dafny-lang/DafnyStandardLibGo/DivMod"
	m_FileIO "github.com/dafny-lang/DafnyStandardLibGo/FileIO"
	m_FloatCompare "github.com/dafny-lang/DafnyStandardLibGo/FloatCompare"
	m_Functions "github.com/dafny-lang/DafnyStandardLibGo/Functions"
	m_GeneralInternals "github.com/dafny-lang/DafnyStandardLibGo/GeneralInternals"
	m_GetOpt "github.com/dafny-lang/DafnyStandardLibGo/GetOpt"
	m_HexStrings "github.com/dafny-lang/DafnyStandardLibGo/HexStrings"
	m_Logarithm "github.com/dafny-lang/DafnyStandardLibGo/Logarithm"
	m__Math "github.com/dafny-lang/DafnyStandardLibGo/Math_"
	m_ModInternals "github.com/dafny-lang/DafnyStandardLibGo/ModInternals"
	m_ModInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/ModInternalsNonlinear"
	m_Mul "github.com/dafny-lang/DafnyStandardLibGo/Mul"
	m_MulInternals "github.com/dafny-lang/DafnyStandardLibGo/MulInternals"
	m_MulInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/MulInternalsNonlinear"
	m_Power "github.com/dafny-lang/DafnyStandardLibGo/Power"
	m_Relations "github.com/dafny-lang/DafnyStandardLibGo/Relations"
	m_Seq "github.com/dafny-lang/DafnyStandardLibGo/Seq"
	m_Seq_MergeSort "github.com/dafny-lang/DafnyStandardLibGo/Seq_MergeSort"
	m_Sorting "github.com/dafny-lang/DafnyStandardLibGo/Sorting"
	m_StandardLibrary "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary"
	m_StandardLibraryInterop "github.com/dafny-lang/DafnyStandardLibGo/StandardLibraryInterop"
	m_StandardLibrary_String "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_UInt"
	m_Streams "github.com/dafny-lang/DafnyStandardLibGo/Streams"
	m_UnicodeStrings "github.com/dafny-lang/DafnyStandardLibGo/UnicodeStrings"
	m__Unicode "github.com/dafny-lang/DafnyStandardLibGo/Unicode_"
	m_Utf16EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf8EncodingForm"
	m_Wrappers "github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

var _ = os.Args
var _ _dafny.Dummy__
var _ m__System.Dummy__
var _ m_Wrappers.Dummy__
var _ m_BoundedInts.Dummy__
var _ m_StandardLibrary_UInt.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_ComAmazonawsKmsTypes.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m__Unicode.Dummy__
var _ m_Functions.Dummy__
var _ m_Utf8EncodingForm.Dummy__
var _ m_Utf16EncodingForm.Dummy__
var _ m_UnicodeStrings.Dummy__
var _ m_FileIO.Dummy__
var _ m_GeneralInternals.Dummy__
var _ m_MulInternalsNonlinear.Dummy__
var _ m_MulInternals.Dummy__
var _ m_Mul.Dummy__
var _ m_ModInternalsNonlinear.Dummy__
var _ m_DivInternalsNonlinear.Dummy__
var _ m_ModInternals.Dummy__
var _ m_DivInternals.Dummy__
var _ m_DivMod.Dummy__
var _ m_Power.Dummy__
var _ m_Logarithm.Dummy__
var _ m_StandardLibraryInterop.Dummy__
var _ m_Streams.Dummy__
var _ m_Sorting.Dummy__
var _ m_HexStrings.Dummy__
var _ m_GetOpt.Dummy__
var _ m_FloatCompare.Dummy__
var _ m_Base64.Dummy__
var _ m_Base64Lemmas.Dummy__
var _ m_Actions.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__

type Dummy__ struct{}

// Definition of class Default__
type Default__ struct {
	dummy byte
}

func New_Default___() *Default__ {
	_this := Default__{}

	return &_this
}

type CompanionStruct_Default___ struct {
}

var Companion_Default___ = CompanionStruct_Default___{}

func (_this *Default__) Equals(other *Default__) bool {
	return _this == other
}

func (_this *Default__) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*Default__)
	return ok && _this.Equals(other)
}

func (*Default__) String() string {
	return "TestComAmazonawsKms.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) WorkAround(literal _dafny.Sequence) _dafny.Sequence {
	return literal
}
func (_static *CompanionStruct_Default___) BasicDecryptTests() {
	var _0_CiphertextBlob _dafny.Sequence
	_ = _0_CiphertextBlob
	_0_CiphertextBlob = _dafny.SeqOf(uint8(1), uint8(1), uint8(1), uint8(0), uint8(120), uint8(64), uint8(243), uint8(140), uint8(39), uint8(94), uint8(49), uint8(9), uint8(116), uint8(22), uint8(193), uint8(7), uint8(41), uint8(81), uint8(80), uint8(87), uint8(25), uint8(100), uint8(173), uint8(163), uint8(239), uint8(28), uint8(33), uint8(233), uint8(76), uint8(139), uint8(160), uint8(189), uint8(188), uint8(157), uint8(15), uint8(180), uint8(20), uint8(0), uint8(0), uint8(0), uint8(98), uint8(48), uint8(96), uint8(6), uint8(9), uint8(42), uint8(134), uint8(72), uint8(134), uint8(247), uint8(13), uint8(1), uint8(7), uint8(6), uint8(160), uint8(83), uint8(48), uint8(81), uint8(2), uint8(1), uint8(0), uint8(48), uint8(76), uint8(6), uint8(9), uint8(42), uint8(134), uint8(72), uint8(134), uint8(247), uint8(13), uint8(1), uint8(7), uint8(1), uint8(48), uint8(30), uint8(6), uint8(9), uint8(96), uint8(134), uint8(72), uint8(1), uint8(101), uint8(3), uint8(4), uint8(1), uint8(46), uint8(48), uint8(17), uint8(4), uint8(12), uint8(196), uint8(249), uint8(60), uint8(7), uint8(21), uint8(231), uint8(87), uint8(70), uint8(216), uint8(12), uint8(31), uint8(13), uint8(2), uint8(1), uint8(16), uint8(128), uint8(31), uint8(222), uint8(119), uint8(162), uint8(112), uint8(88), uint8(153), uint8(39), uint8(197), uint8(21), uint8(182), uint8(116), uint8(176), uint8(120), uint8(174), uint8(107), uint8(82), uint8(182), uint8(223), uint8(160), uint8(201), uint8(15), uint8(29), uint8(3), uint8(254), uint8(3), uint8(208), uint8(72), uint8(171), uint8(64), uint8(207), uint8(175))
	Companion_Default___.BasicDecryptTest(m_ComAmazonawsKmsTypes.Companion_DecryptRequest_.Create_DecryptRequest_(Companion_Default___.WorkAround(_0_CiphertextBlob), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(Companion_Default___.KeyId()), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()), _dafny.SeqOf(uint8(165), uint8(191), uint8(67), uint8(62)), Companion_Default___.KeyId())
}
func (_static *CompanionStruct_Default___) BasicGenerateTests() {
	Companion_Default___.BasicGenerateTest(m_ComAmazonawsKmsTypes.Companion_GenerateDataKeyRequest_.Create_GenerateDataKeyRequest_(Companion_Default___.KeyId(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(int32(32)), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
}
func (_static *CompanionStruct_Default___) BasicGenerateWithoutPlaintextTests() {
	Companion_Default___.BasicGenerateWithoutPlaintextTest(m_ComAmazonawsKmsTypes.Companion_GenerateDataKeyWithoutPlaintextRequest_.Create_GenerateDataKeyWithoutPlaintextRequest_(Companion_Default___.KeyIdGenerateWOPlain(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(int32(32)), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
}
func (_static *CompanionStruct_Default___) BasicEncryptTests() {
	Companion_Default___.BasicEncryptTest(m_ComAmazonawsKmsTypes.Companion_EncryptRequest_.Create_EncryptRequest_(Companion_Default___.KeyId(), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102)), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
}
func (_static *CompanionStruct_Default___) BasicFailTests() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(117,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_ret m_Wrappers.Result
	_ = _2_ret
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).GenerateDataKeyWithoutPlaintext(Companion_Default___.FailingInput())
	_2_ret = _out1
	if !((_2_ret).Is_Failure()) {
		panic("test/TestComAmazonawsKms.dfy(119,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_err m_ComAmazonawsKmsTypes.Error
	_ = _3_err
	_3_err = (_2_ret).Dtor_error().(m_ComAmazonawsKmsTypes.Error)
	if !((_3_err).Is_Opaque()) {
		panic("test/TestComAmazonawsKms.dfy(121,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _source0 m_ComAmazonawsKmsTypes.Error = _3_err
	_ = _source0
	{
		{
			if _source0.Is_Opaque() {
				var _4_obj interface{} = _source0.Get_().(m_ComAmazonawsKmsTypes.Error_Opaque).Obj
				_ = _4_obj
				if !(true) {
					panic("test/TestComAmazonawsKms.dfy(123,26): " + (_dafny.SeqOfString("expectation violation")).String())
				}
				goto Lmatch0
			}
		}
		{
			if !(false) {
				panic("test/TestComAmazonawsKms.dfy(124,16): " + (_dafny.SeqOfString("Failing KMS Key MUST cause an OpaqueError that can later be unwrapped to a proper but generic KMS Exception.")).String())
			}
		}
		goto Lmatch0
	}
Lmatch0:
}
func (_static *CompanionStruct_Default___) BasicDecryptTest(input m_ComAmazonawsKmsTypes.DecryptRequest, expectedPlaintext _dafny.Sequence, expectedKeyId _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(134,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_ret m_Wrappers.Result
	_ = _2_ret
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).Decrypt(input)
	_2_ret = _out1
	if !((_2_ret).Is_Success()) {
		panic("test/TestComAmazonawsKms.dfy(140,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.DecryptResponse = (_2_ret).Dtor_value().(m_ComAmazonawsKmsTypes.DecryptResponse)
	_ = _let_tmp_rhs0
	var _3_KeyId m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).KeyId
	_ = _3_KeyId
	var _4_Plaintext m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).Plaintext
	_ = _4_Plaintext
	var _5_EncryptionAlgorithm m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).EncryptionAlgorithm
	_ = _5_EncryptionAlgorithm
	var _6_CiphertextBlob m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).CiphertextForRecipient
	_ = _6_CiphertextBlob
	if !((_4_Plaintext).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(144,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_3_KeyId).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(145,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_4_Plaintext).Dtor_value().(_dafny.Sequence), expectedPlaintext)) {
		panic("test/TestComAmazonawsKms.dfy(146,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_KeyId).Dtor_value().(_dafny.Sequence), expectedKeyId)) {
		panic("test/TestComAmazonawsKms.dfy(147,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) BasicGenerateTest(input m_ComAmazonawsKmsTypes.GenerateDataKeyRequest) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(155,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_ret m_Wrappers.Result
	_ = _2_ret
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).GenerateDataKey(input)
	_2_ret = _out1
	if !((_2_ret).Is_Success()) {
		panic("test/TestComAmazonawsKms.dfy(159,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GenerateDataKeyResponse = (_2_ret).Dtor_value().(m_ComAmazonawsKmsTypes.GenerateDataKeyResponse)
	_ = _let_tmp_rhs0
	var _3_CiphertextBlob m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GenerateDataKeyResponse_GenerateDataKeyResponse).CiphertextBlob
	_ = _3_CiphertextBlob
	var _4_Plaintext m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GenerateDataKeyResponse_GenerateDataKeyResponse).Plaintext
	_ = _4_Plaintext
	var _5_KeyId m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GenerateDataKeyResponse_GenerateDataKeyResponse).KeyId
	_ = _5_KeyId
	var _6_CiphertextForRecipient m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GenerateDataKeyResponse_GenerateDataKeyResponse).CiphertextForRecipient
	_ = _6_CiphertextForRecipient
	if !((_3_CiphertextBlob).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(163,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_4_Plaintext).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(164,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_5_KeyId).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(165,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_dafny.IntOfUint32(((_4_Plaintext).Dtor_value().(_dafny.Sequence)).Cardinality())).Cmp(_dafny.IntOfInt32(((input).Dtor_NumberOfBytes()).Dtor_value().(int32))) == 0) {
		panic("test/TestComAmazonawsKms.dfy(166,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _7_decryptInput m_ComAmazonawsKmsTypes.DecryptRequest
	_ = _7_decryptInput
	_7_decryptInput = m_ComAmazonawsKmsTypes.Companion_DecryptRequest_.Create_DecryptRequest_((_3_CiphertextBlob).Dtor_value().(_dafny.Sequence), (input).Dtor_EncryptionContext(), (input).Dtor_GrantTokens(), m_Wrappers.Companion_Option_.Create_Some_((_5_KeyId).Dtor_value().(_dafny.Sequence)), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	Companion_Default___.BasicDecryptTest(_7_decryptInput, (_4_Plaintext).Dtor_value().(_dafny.Sequence), (input).Dtor_KeyId())
}
func (_static *CompanionStruct_Default___) BasicGenerateWithoutPlaintextTest(input m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(188,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_retGenerate m_Wrappers.Result
	_ = _2_retGenerate
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).GenerateDataKeyWithoutPlaintext(input)
	_2_retGenerate = _out1
	if !((_2_retGenerate).Is_Success()) {
		panic("test/TestComAmazonawsKms.dfy(192,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse = (_2_retGenerate).Dtor_value().(m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse)
	_ = _let_tmp_rhs0
	var _3_CiphertextBlob m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse).CiphertextBlob
	_ = _3_CiphertextBlob
	var _4_KeyId m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse).KeyId
	_ = _4_KeyId
	if !((_3_CiphertextBlob).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(196,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_4_KeyId).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(197,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_decryptInput m_ComAmazonawsKmsTypes.DecryptRequest
	_ = _5_decryptInput
	_5_decryptInput = m_ComAmazonawsKmsTypes.Companion_DecryptRequest_.Create_DecryptRequest_((_3_CiphertextBlob).Dtor_value().(_dafny.Sequence), (input).Dtor_EncryptionContext(), (input).Dtor_GrantTokens(), m_Wrappers.Companion_Option_.Create_Some_((_4_KeyId).Dtor_value().(_dafny.Sequence)), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _6_ret m_Wrappers.Result
	_ = _6_ret
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_1_client).Decrypt(_5_decryptInput)
	_6_ret = _out2
	if !((_6_ret).Is_Success()) {
		panic("test/TestComAmazonawsKms.dfy(208,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs1 m_ComAmazonawsKmsTypes.DecryptResponse = (_6_ret).Dtor_value().(m_ComAmazonawsKmsTypes.DecryptResponse)
	_ = _let_tmp_rhs1
	var _7_KeyIdTwo m_Wrappers.Option = _let_tmp_rhs1.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).KeyId
	_ = _7_KeyIdTwo
	var _8_Plaintext m_Wrappers.Option = _let_tmp_rhs1.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).Plaintext
	_ = _8_Plaintext
	var _9_EncryptionAlgorithm m_Wrappers.Option = _let_tmp_rhs1.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).EncryptionAlgorithm
	_ = _9_EncryptionAlgorithm
	var _10_CiphertextBlobTwo m_Wrappers.Option = _let_tmp_rhs1.Get_().(m_ComAmazonawsKmsTypes.DecryptResponse_DecryptResponse).CiphertextForRecipient
	_ = _10_CiphertextBlobTwo
	if !((_7_KeyIdTwo).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(211,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_7_KeyIdTwo).Dtor_value().(_dafny.Sequence), (_4_KeyId).Dtor_value().(_dafny.Sequence))) {
		panic("test/TestComAmazonawsKms.dfy(212,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) BasicEncryptTest(input m_ComAmazonawsKmsTypes.EncryptRequest) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(219,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_ret m_Wrappers.Result
	_ = _2_ret
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).Encrypt(input)
	_2_ret = _out1
	if !((_2_ret).Is_Success()) {
		panic("test/TestComAmazonawsKms.dfy(223,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.EncryptResponse = (_2_ret).Dtor_value().(m_ComAmazonawsKmsTypes.EncryptResponse)
	_ = _let_tmp_rhs0
	var _3_CiphertextBlob m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.EncryptResponse_EncryptResponse).CiphertextBlob
	_ = _3_CiphertextBlob
	var _4_KeyId m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.EncryptResponse_EncryptResponse).KeyId
	_ = _4_KeyId
	var _5_EncryptionAlgorithm m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.EncryptResponse_EncryptResponse).EncryptionAlgorithm
	_ = _5_EncryptionAlgorithm
	if !((_3_CiphertextBlob).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(227,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((_4_KeyId).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(228,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_decryptInput m_ComAmazonawsKmsTypes.DecryptRequest
	_ = _6_decryptInput
	_6_decryptInput = m_ComAmazonawsKmsTypes.Companion_DecryptRequest_.Create_DecryptRequest_((_3_CiphertextBlob).Dtor_value().(_dafny.Sequence), (input).Dtor_EncryptionContext(), (input).Dtor_GrantTokens(), m_Wrappers.Companion_Option_.Create_Some_((_4_KeyId).Dtor_value().(_dafny.Sequence)), (input).Dtor_EncryptionAlgorithm(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	Companion_Default___.BasicDecryptTest(_6_decryptInput, (input).Dtor_Plaintext(), (input).Dtor_KeyId())
}
func (_static *CompanionStruct_Default___) RegionMatchTest() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(248,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_region m_Wrappers.Option
	_ = _2_region
	_2_region = m_Com_Amazonaws_Kms.Companion_Default___.RegionMatch(_1_client, Companion_Default___.TEST__REGION())
	if !(((_2_region).Is_None()) || ((_2_region).Dtor_value().(bool))) {
		panic("test/TestComAmazonawsKms.dfy(250,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) EmptyStringIsDefaultRegion() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(_dafny.SeqOfString(""))
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(255,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
}
func (_static *CompanionStruct_Default___) BasicDeriveSharedSecretTests(input m_ComAmazonawsKmsTypes.DeriveSharedSecretRequest) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(262,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_ret m_Wrappers.Result
	_ = _2_ret
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).DeriveSharedSecret(m_ComAmazonawsKmsTypes.Companion_DeriveSharedSecretRequest_.Create_DeriveSharedSecretRequest_((input).Dtor_KeyId(), (input).Dtor_KeyAgreementAlgorithm(), (input).Dtor_PublicKey(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
	_2_ret = _out1
	if (_2_ret).Is_Success() {
		var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse = (_2_ret).Dtor_value().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse)
		_ = _let_tmp_rhs0
		var _3_KeyId m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse_DeriveSharedSecretResponse).KeyId
		_ = _3_KeyId
		var _4_SharedSecret m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse_DeriveSharedSecretResponse).SharedSecret
		_ = _4_SharedSecret
		var _5_CiphertextForRecipient m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse_DeriveSharedSecretResponse).CiphertextForRecipient
		_ = _5_CiphertextForRecipient
		var _6_KeyAgreementAlgorithm m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse_DeriveSharedSecretResponse).KeyAgreementAlgorithm
		_ = _6_KeyAgreementAlgorithm
		var _7_KeyOrigin m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.DeriveSharedSecretResponse_DeriveSharedSecretResponse).KeyOrigin
		_ = _7_KeyOrigin
		if !((_4_SharedSecret).Is_Some()) {
			panic("test/TestComAmazonawsKms.dfy(275,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !((_3_KeyId).Is_Some()) {
			panic("test/TestComAmazonawsKms.dfy(276,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
		if !(_dafny.Companion_Sequence_.Equal((_3_KeyId).Dtor_value().(_dafny.Sequence), (input).Dtor_KeyId())) {
			panic("test/TestComAmazonawsKms.dfy(278,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	} else {
		if !((_2_ret).Is_Failure()) {
			panic("test/TestComAmazonawsKms.dfy(281,6): " + (_dafny.SeqOfString("expectation violation")).String())
		}
	}
}
func (_static *CompanionStruct_Default___) GetPublicKeyHelper(input m_ComAmazonawsKmsTypes.GetPublicKeyRequest) _dafny.Sequence {
	var publicKey _dafny.Sequence = _dafny.EmptySeq
	_ = publicKey
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Kms.Companion_Default___.KMSClientForRegion(Companion_Default___.TEST__REGION())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsKms.dfy(292,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsKmsTypes.IKMSClient
	_ = _1_client
	_1_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_ret m_Wrappers.Result
	_ = _2_ret
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).GetPublicKey(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_((input).Dtor_KeyId(), (input).Dtor_GrantTokens()))
	_2_ret = _out1
	if !((_2_ret).Is_Success()) {
		panic("test/TestComAmazonawsKms.dfy(299,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _let_tmp_rhs0 m_ComAmazonawsKmsTypes.GetPublicKeyResponse = (_2_ret).Dtor_value().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse)
	_ = _let_tmp_rhs0
	var _3___v1 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyId
	_ = _3___v1
	var _4_PublicKey m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).PublicKey
	_ = _4_PublicKey
	var _5___v2 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).CustomerMasterKeySpec
	_ = _5___v2
	var _6___v3 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeySpec
	_ = _6___v3
	var _7___v4 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyUsage
	_ = _7___v4
	var _8___v5 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).EncryptionAlgorithms
	_ = _8___v5
	var _9___v6 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).SigningAlgorithms
	_ = _9___v6
	var _10___v7 m_Wrappers.Option = _let_tmp_rhs0.Get_().(m_ComAmazonawsKmsTypes.GetPublicKeyResponse_GetPublicKeyResponse).KeyAgreementAlgorithms
	_ = _10___v7
	if !((_4_PublicKey).Is_Some()) {
		panic("test/TestComAmazonawsKms.dfy(302,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	publicKey = (_4_PublicKey).Dtor_value().(_dafny.Sequence)
	return publicKey
	return publicKey
}
func (_static *CompanionStruct_Default___) DeriveSharedSecretTestSuccess() {
	var _0_recipientPublicKey _dafny.Sequence
	_ = _0_recipientPublicKey
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = Companion_Default___.GetPublicKeyHelper(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_(Companion_Default___.RecipientKmsKey(), m_Wrappers.Companion_Option_.Create_None_()))
	_0_recipientPublicKey = _out0
	Companion_Default___.BasicDeriveSharedSecretTests(m_ComAmazonawsKmsTypes.Companion_DeriveSharedSecretRequest_.Create_DeriveSharedSecretRequest_(Companion_Default___.SenderKmsKey(), m_ComAmazonawsKmsTypes.Companion_KeyAgreementAlgorithmSpec_.Create_ECDH_(), _0_recipientPublicKey, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
}
func (_static *CompanionStruct_Default___) DeriveSharedSecretTestFailure() {
	var _0_recipientPublicKeyOnWrongCurve _dafny.Sequence
	_ = _0_recipientPublicKeyOnWrongCurve
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = Companion_Default___.GetPublicKeyHelper(m_ComAmazonawsKmsTypes.Companion_GetPublicKeyRequest_.Create_GetPublicKeyRequest_(Companion_Default___.IncorrectEccCurveKey(), m_Wrappers.Companion_Option_.Create_None_()))
	_0_recipientPublicKeyOnWrongCurve = _out0
	Companion_Default___.BasicDeriveSharedSecretTests(m_ComAmazonawsKmsTypes.Companion_DeriveSharedSecretRequest_.Create_DeriveSharedSecretRequest_(Companion_Default___.SenderKmsKey(), m_ComAmazonawsKmsTypes.Companion_KeyAgreementAlgorithmSpec_.Create_ECDH_(), _0_recipientPublicKeyOnWrongCurve, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
}
func (_static *CompanionStruct_Default___) CreateNoneForEncryptionContext() m_Wrappers.Option {
	return m_Wrappers.Companion_Option_.Create_None_()
}
func (_static *CompanionStruct_Default___) CreateNoneForKeySpec() m_Wrappers.Option {
	return m_Wrappers.Companion_Option_.Create_None_()
}
func (_static *CompanionStruct_Default___) CreateNoneForNumberOfBytes() m_Wrappers.Option {
	return m_Wrappers.Companion_Option_.Create_None_()
}
func (_static *CompanionStruct_Default___) CreateNoneForGrantTokens() m_Wrappers.Option {
	return m_Wrappers.Companion_Option_.Create_None_()
}
func (_static *CompanionStruct_Default___) CreateNoneForDryRun() m_Wrappers.Option {
	return m_Wrappers.Companion_Option_.Create_None_()
}
func (_static *CompanionStruct_Default___) TEST__REGION() _dafny.Sequence {
	return _dafny.SeqOfString("us-west-2")
}
func (_static *CompanionStruct_Default___) KeyId() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
}
func (_static *CompanionStruct_Default___) KeyIdGenerateWOPlain() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126")
}
func (_static *CompanionStruct_Default___) FailingKeyId() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/e20ac7b8-3d95-46ee-b3d5-f5dca6393945")
}
func (_static *CompanionStruct_Default___) FailingInput() m_ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest {
	return m_ComAmazonawsKmsTypes.Companion_GenerateDataKeyWithoutPlaintextRequest_.Create_GenerateDataKeyWithoutPlaintextRequest_(Companion_Default___.FailingKeyId(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(int32(32)), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
}
func (_static *CompanionStruct_Default___) RecipientKmsKey() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5")
}
func (_static *CompanionStruct_Default___) SenderKmsKey() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9")
}
func (_static *CompanionStruct_Default___) IncorrectEccCurveKey() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/7f35a704-f4fb-469d-98b1-62a1fa2cc44e")
}

// End of class Default__
