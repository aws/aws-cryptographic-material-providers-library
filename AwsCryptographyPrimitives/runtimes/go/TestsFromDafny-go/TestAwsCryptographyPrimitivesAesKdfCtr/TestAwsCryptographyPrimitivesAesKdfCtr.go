// Package TestAwsCryptographyPrimitivesAesKdfCtr
// Dafny module TestAwsCryptographyPrimitivesAesKdfCtr compiled into Go

package TestAwsCryptographyPrimitivesAesKdfCtr

import (
	os "os"

	m_AESEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/AESEncryption"
	m_AesKdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/AesKdfCtr"
	m_AtomicPrimitives "github.com/aws/aws-cryptographic-material-providers-library/primitives/AtomicPrimitives"
	m_AwsCryptographyPrimitivesOperations "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesOperations"
	m_AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	m_Digest "github.com/aws/aws-cryptographic-material-providers-library/primitives/Digest"
	m_ECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/ECDH"
	m_HKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/HKDF"
	m_HMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/HMAC"
	m_KdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/KdfCtr"
	m_RSAEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/RSAEncryption"
	m_Random "github.com/aws/aws-cryptographic-material-providers-library/primitives/Random"
	m_Signature "github.com/aws/aws-cryptographic-material-providers-library/primitives/Signature"
	m_WrappedHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHKDF"
	m_WrappedHMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHMAC"
	m_ConstantTime "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/ConstantTime"
	m_ConstantTimeTest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/ConstantTimeTest"
	m_TestAwsCryptographyPrimitivesDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesDigest"
	m_TestAwsCryptographyPrimitivesGenerateRandomBytes "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesGenerateRandomBytes"
	m_TestAwsCryptographyPrimitivesHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHKDF"
	m_TestAwsCryptographyPrimitivesHMacDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMacDigest"
	m_TestECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestECDH"
	m_TestKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDF"
	m_TestKDFK__TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDFK__TestVectors"
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
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
var _ m_Random.Dummy__
var _ m_AESEncryption.Dummy__
var _ m_Digest.Dummy__
var _ m_HMAC.Dummy__
var _ m_WrappedHMAC.Dummy__
var _ m_HKDF.Dummy__
var _ m_WrappedHKDF.Dummy__
var _ m_Signature.Dummy__
var _ m_KdfCtr.Dummy__
var _ m_RSAEncryption.Dummy__
var _ m_ECDH.Dummy__
var _ m_AwsCryptographyPrimitivesOperations.Dummy__
var _ m_AtomicPrimitives.Dummy__
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
var _ m_TestKDF.Dummy__
var _ m_TestKDFK__TestVectors.Dummy__
var _ m_TestAwsCryptographyPrimitivesHMacDigest.Dummy__
var _ m_TestECDH.Dummy__
var _ m_TestAwsCryptographyPrimitivesHKDF.Dummy__
var _ m_TestAwsCryptographyPrimitivesGenerateRandomBytes.Dummy__
var _ m_TestAwsCryptographyPrimitivesDigest.Dummy__
var _ m_ConstantTime.Dummy__
var _ m_ConstantTimeTest.Dummy__

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
	return "TestAwsCryptographyPrimitivesAesKdfCtr.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) AesKdfCtrTests() {
	var _0_key _dafny.Sequence
	_ = _0_key
	_0_key = _dafny.SeqOf(uint8(138), uint8(39), uint8(30), uint8(72), uint8(206), uint8(182), uint8(214), uint8(144), uint8(245), uint8(34), uint8(28), uint8(219), uint8(204), uint8(175), uint8(198), uint8(23), uint8(132), uint8(234), uint8(125), uint8(246), uint8(130), uint8(54), uint8(251), uint8(60), uint8(137), uint8(120), uint8(166), uint8(245), uint8(0), uint8(150), uint8(79), uint8(107))
	var _1_nonce _dafny.Sequence
	_ = _1_nonce
	_1_nonce = _dafny.SeqOf(uint8(66), uint8(32), uint8(73), uint8(11), uint8(207), uint8(79), uint8(97), uint8(80), uint8(11), uint8(22), uint8(236), uint8(247), uint8(42), uint8(6), uint8(222), uint8(165))
	var _2_goal _dafny.Sequence
	_ = _2_goal
	_2_goal = _dafny.SeqOf(uint8(143), uint8(128), uint8(174), uint8(191), uint8(9), uint8(171), uint8(140), uint8(22), uint8(40), uint8(143), uint8(11), uint8(239), uint8(249), uint8(101), uint8(61), uint8(120), uint8(176), uint8(23), uint8(233), uint8(210), uint8(125), uint8(72), uint8(114), uint8(70), uint8(209), uint8(170), uint8(206), uint8(96), uint8(24), uint8(112), uint8(215), uint8(169), uint8(100), uint8(136), uint8(162), uint8(231), uint8(208), uint8(24), uint8(135), uint8(121), uint8(223), uint8(13), uint8(239), uint8(180))
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _3_valueOrError0
	_3_valueOrError0 = m_AesKdfCtr.AesKdfCtrStream(_1_nonce, _0_key, uint32(44))
	if !(!((_3_valueOrError0).IsFailure())) {
		panic("test/TestAesKdfCtr.dfy(18,18): " + (_3_valueOrError0).String())
	}
	var _4_result _dafny.Sequence
	_ = _4_result
	_4_result = (_3_valueOrError0).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_4_result).Cardinality())).Cmp(_dafny.IntOfInt64(44)) == 0) {
		panic("test/TestAesKdfCtr.dfy(19,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_goal, _4_result)) {
		panic("test/TestAesKdfCtr.dfy(20,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_key = _dafny.SeqOf(uint8(212), uint8(191), uint8(10), uint8(32), uint8(13), uint8(55), uint8(22), uint8(101), uint8(189), uint8(182), uint8(186), uint8(119), uint8(202), uint8(16), uint8(175), uint8(49), uint8(103), uint8(82), uint8(87), uint8(190), uint8(13), uint8(142), uint8(103), uint8(201), uint8(98), uint8(84), uint8(228), uint8(47), uint8(142), uint8(96), uint8(61), uint8(167))
	_1_nonce = _dafny.SeqOf(uint8(135), uint8(1), uint8(132), uint8(66), uint8(198), uint8(216), uint8(26), uint8(105), uint8(47), uint8(97), uint8(246), uint8(192), uint8(186), uint8(187), uint8(54), uint8(129))
	_2_goal = _dafny.SeqOf(uint8(11), uint8(154), uint8(37), uint8(42), uint8(116), uint8(143), uint8(238), uint8(68), uint8(62), uint8(135), uint8(225), uint8(71), uint8(98), uint8(224), uint8(135), uint8(18))
	var _5_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _5_valueOrError1
	_5_valueOrError1 = m_AesKdfCtr.AesKdfCtrStream(_1_nonce, _0_key, uint32(16))
	if !(!((_5_valueOrError1).IsFailure())) {
		panic("test/TestAesKdfCtr.dfy(25,14): " + (_5_valueOrError1).String())
	}
	_4_result = (_5_valueOrError1).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_4_result).Cardinality())).Cmp(_dafny.IntOfInt64(16)) == 0) {
		panic("test/TestAesKdfCtr.dfy(26,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_goal, _4_result)) {
		panic("test/TestAesKdfCtr.dfy(27,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_key = _dafny.SeqOf(uint8(106), uint8(72), uint8(42), uint8(47), uint8(58), uint8(213), uint8(111), uint8(196), uint8(126), uint8(37), uint8(46), uint8(203), uint8(150), uint8(153), uint8(188), uint8(53), uint8(32), uint8(194), uint8(159), uint8(196), uint8(221), uint8(90), uint8(124), uint8(70), uint8(45), uint8(252), uint8(99), uint8(98), uint8(42), uint8(68), uint8(94), uint8(19))
	_1_nonce = _dafny.SeqOf(uint8(13), uint8(247), uint8(32), uint8(159), uint8(220), uint8(254), uint8(69), uint8(218), uint8(42), uint8(110), uint8(159), uint8(42), uint8(209), uint8(244), uint8(79), uint8(232))
	_2_goal = _dafny.SeqOf(uint8(150), uint8(218), uint8(139), uint8(126), uint8(166), uint8(233), uint8(178), uint8(123), uint8(229), uint8(210), uint8(40), uint8(218), uint8(141), uint8(26), uint8(127), uint8(208), uint8(124), uint8(197), uint8(212), uint8(69), uint8(251), uint8(71), uint8(73), uint8(90), uint8(47), uint8(134), uint8(46), uint8(7), uint8(215), uint8(208), uint8(194), uint8(180), uint8(174), uint8(110), uint8(1), uint8(57), uint8(16), uint8(37), uint8(16), uint8(235), uint8(93), uint8(138), uint8(25), uint8(180), uint8(85), uint8(16), uint8(229), uint8(165), uint8(238), uint8(36), uint8(56), uint8(131), uint8(247), uint8(31), uint8(64), uint8(23), uint8(249), uint8(67), uint8(153), uint8(94), uint8(23), uint8(243), uint8(69), uint8(11))
	var _6_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _6_valueOrError2
	_6_valueOrError2 = m_AesKdfCtr.AesKdfCtrStream(_1_nonce, _0_key, uint32(64))
	if !(!((_6_valueOrError2).IsFailure())) {
		panic("test/TestAesKdfCtr.dfy(32,14): " + (_6_valueOrError2).String())
	}
	_4_result = (_6_valueOrError2).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_4_result).Cardinality())).Cmp(_dafny.IntOfInt64(64)) == 0) {
		panic("test/TestAesKdfCtr.dfy(33,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_goal, _4_result)) {
		panic("test/TestAesKdfCtr.dfy(34,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
