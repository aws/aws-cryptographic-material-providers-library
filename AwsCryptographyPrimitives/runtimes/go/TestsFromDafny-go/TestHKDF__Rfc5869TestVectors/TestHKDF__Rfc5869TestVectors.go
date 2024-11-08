// Package TestHKDF__Rfc5869TestVectors
// Dafny module TestHKDF__Rfc5869TestVectors compiled into Go

package TestHKDF__Rfc5869TestVectors

import (
	os "os"

	m_AESEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/AESEncryption"
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
	m_TestAwsCryptographyPrimitivesAesKdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesAesKdfCtr"
	m_TestAwsCryptographyPrimitivesDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesDigest"
	m_TestAwsCryptographyPrimitivesGenerateRandomBytes "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesGenerateRandomBytes"
	m_TestAwsCryptographyPrimitivesHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHKDF"
	m_TestAwsCryptographyPrimitivesHMacDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMacDigest"
	m_TestECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestECDH"
	m_TestKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDF"
	m_TestKDFK__TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDFK__TestVectors"
	m_TestSignature "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestSignature"
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
var _ m_TestAwsCryptographyPrimitivesAesKdfCtr.Dummy__
var _ m_TestSignature.Dummy__

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
	return "TestHKDF__Rfc5869TestVectors.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) ExpectRFCTestVectors() {
	var _hi0 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.TestVectors()).Cardinality())
	_ = _hi0
	for _0_i := _dafny.Zero; _0_i.Cmp(_hi0) < 0; _0_i = _0_i.Plus(_dafny.One) {
		Companion_Default___.ExpectTestVector((Companion_Default___.TestVectors()).Select((_0_i).Uint32()).(RFCTestVector))
	}
}
func (_static *CompanionStruct_Default___) ExpectTestVector(vector RFCTestVector) {
	var _let_tmp_rhs0 RFCTestVector = vector
	_ = _let_tmp_rhs0
	var _0_name _dafny.Sequence = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).Name
	_ = _0_name
	var _1_hash m_AwsCryptographyPrimitivesTypes.DigestAlgorithm = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).Hash
	_ = _1_hash
	var _2_IKM _dafny.Sequence = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).IKM
	_ = _2_IKM
	var _3_salt _dafny.Sequence = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).Salt
	_ = _3_salt
	var _4_info _dafny.Sequence = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).Info
	_ = _4_info
	var _5_L int32 = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).L
	_ = _5_L
	var _6_PRK _dafny.Sequence = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).PRK
	_ = _6_PRK
	var _7_OKM _dafny.Sequence = _let_tmp_rhs0.Get_().(RFCTestVector_RFCTestVector).OKM
	_ = _7_OKM
	_dafny.Print((_dafny.Companion_Sequence_.Concatenate(_0_name, _dafny.SeqOfString("\n"))).SetString())
	m_TestAwsCryptographyPrimitivesHKDF.Companion_Default___.BasicExtractTest(m_AwsCryptographyPrimitivesTypes.Companion_HkdfExtractInput_.Create_HkdfExtractInput_(_1_hash, (func() m_Wrappers.Option {
		if (_dafny.IntOfUint32((_3_salt).Cardinality())).Sign() == 1 {
			return m_Wrappers.Companion_Option_.Create_Some_(_3_salt)
		}
		return m_Wrappers.Companion_Option_.Create_None_()
	})(), _2_IKM), _6_PRK)
	m_TestAwsCryptographyPrimitivesHKDF.Companion_Default___.BasicExpandTest(m_AwsCryptographyPrimitivesTypes.Companion_HkdfExpandInput_.Create_HkdfExpandInput_(_1_hash, _6_PRK, _4_info, _5_L), _7_OKM)
	m_TestAwsCryptographyPrimitivesHKDF.Companion_Default___.BasicHkdfTest(m_AwsCryptographyPrimitivesTypes.Companion_HkdfInput_.Create_HkdfInput_(_1_hash, (func() m_Wrappers.Option {
		if (_dafny.IntOfUint32((_3_salt).Cardinality())).Sign() == 1 {
			return m_Wrappers.Companion_Option_.Create_Some_(_3_salt)
		}
		return m_Wrappers.Companion_Option_.Create_None_()
	})(), _2_IKM, _4_info, _5_L), _7_OKM)
}
func (_static *CompanionStruct_Default___) A1() RFCTestVector {
	return Companion_RFCTestVector_.Create_RFCTestVector_(_dafny.SeqOfString("A.1.  Test Case 1"), m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_(), _dafny.SeqOf(uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11)), _dafny.SeqOf(uint8(0), uint8(1), uint8(2), uint8(3), uint8(4), uint8(5), uint8(6), uint8(7), uint8(8), uint8(9), uint8(10), uint8(11), uint8(12)), _dafny.SeqOf(uint8(240), uint8(241), uint8(242), uint8(243), uint8(244), uint8(245), uint8(246), uint8(247), uint8(248), uint8(249)), int32(42), _dafny.SeqOf(uint8(7), uint8(119), uint8(9), uint8(54), uint8(44), uint8(46), uint8(50), uint8(223), uint8(13), uint8(220), uint8(63), uint8(13), uint8(196), uint8(123), uint8(186), uint8(99), uint8(144), uint8(182), uint8(199), uint8(59), uint8(181), uint8(15), uint8(156), uint8(49), uint8(34), uint8(236), uint8(132), uint8(74), uint8(215), uint8(194), uint8(179), uint8(229)), _dafny.SeqOf(uint8(60), uint8(178), uint8(95), uint8(37), uint8(250), uint8(172), uint8(213), uint8(122), uint8(144), uint8(67), uint8(79), uint8(100), uint8(208), uint8(54), uint8(47), uint8(42), uint8(45), uint8(45), uint8(10), uint8(144), uint8(207), uint8(26), uint8(90), uint8(76), uint8(93), uint8(176), uint8(45), uint8(86), uint8(236), uint8(196), uint8(197), uint8(191), uint8(52), uint8(0), uint8(114), uint8(8), uint8(213), uint8(184), uint8(135), uint8(24), uint8(88), uint8(101)))
}
func (_static *CompanionStruct_Default___) A2() RFCTestVector {
	return Companion_RFCTestVector_.Create_RFCTestVector_(_dafny.SeqOfString("A.2.  Test Case 2"), m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_(), _dafny.SeqOf(uint8(0), uint8(1), uint8(2), uint8(3), uint8(4), uint8(5), uint8(6), uint8(7), uint8(8), uint8(9), uint8(10), uint8(11), uint8(12), uint8(13), uint8(14), uint8(15), uint8(16), uint8(17), uint8(18), uint8(19), uint8(20), uint8(21), uint8(22), uint8(23), uint8(24), uint8(25), uint8(26), uint8(27), uint8(28), uint8(29), uint8(30), uint8(31), uint8(32), uint8(33), uint8(34), uint8(35), uint8(36), uint8(37), uint8(38), uint8(39), uint8(40), uint8(41), uint8(42), uint8(43), uint8(44), uint8(45), uint8(46), uint8(47), uint8(48), uint8(49), uint8(50), uint8(51), uint8(52), uint8(53), uint8(54), uint8(55), uint8(56), uint8(57), uint8(58), uint8(59), uint8(60), uint8(61), uint8(62), uint8(63), uint8(64), uint8(65), uint8(66), uint8(67), uint8(68), uint8(69), uint8(70), uint8(71), uint8(72), uint8(73), uint8(74), uint8(75), uint8(76), uint8(77), uint8(78), uint8(79)), _dafny.SeqOf(uint8(96), uint8(97), uint8(98), uint8(99), uint8(100), uint8(101), uint8(102), uint8(103), uint8(104), uint8(105), uint8(106), uint8(107), uint8(108), uint8(109), uint8(110), uint8(111), uint8(112), uint8(113), uint8(114), uint8(115), uint8(116), uint8(117), uint8(118), uint8(119), uint8(120), uint8(121), uint8(122), uint8(123), uint8(124), uint8(125), uint8(126), uint8(127), uint8(128), uint8(129), uint8(130), uint8(131), uint8(132), uint8(133), uint8(134), uint8(135), uint8(136), uint8(137), uint8(138), uint8(139), uint8(140), uint8(141), uint8(142), uint8(143), uint8(144), uint8(145), uint8(146), uint8(147), uint8(148), uint8(149), uint8(150), uint8(151), uint8(152), uint8(153), uint8(154), uint8(155), uint8(156), uint8(157), uint8(158), uint8(159), uint8(160), uint8(161), uint8(162), uint8(163), uint8(164), uint8(165), uint8(166), uint8(167), uint8(168), uint8(169), uint8(170), uint8(171), uint8(172), uint8(173), uint8(174), uint8(175)), _dafny.SeqOf(uint8(176), uint8(177), uint8(178), uint8(179), uint8(180), uint8(181), uint8(182), uint8(183), uint8(184), uint8(185), uint8(186), uint8(187), uint8(188), uint8(189), uint8(190), uint8(191), uint8(192), uint8(193), uint8(194), uint8(195), uint8(196), uint8(197), uint8(198), uint8(199), uint8(200), uint8(201), uint8(202), uint8(203), uint8(204), uint8(205), uint8(206), uint8(207), uint8(208), uint8(209), uint8(210), uint8(211), uint8(212), uint8(213), uint8(214), uint8(215), uint8(216), uint8(217), uint8(218), uint8(219), uint8(220), uint8(221), uint8(222), uint8(223), uint8(224), uint8(225), uint8(226), uint8(227), uint8(228), uint8(229), uint8(230), uint8(231), uint8(232), uint8(233), uint8(234), uint8(235), uint8(236), uint8(237), uint8(238), uint8(239), uint8(240), uint8(241), uint8(242), uint8(243), uint8(244), uint8(245), uint8(246), uint8(247), uint8(248), uint8(249), uint8(250), uint8(251), uint8(252), uint8(253), uint8(254), uint8(255)), int32(82), _dafny.SeqOf(uint8(6), uint8(166), uint8(184), uint8(140), uint8(88), uint8(83), uint8(54), uint8(26), uint8(6), uint8(16), uint8(76), uint8(156), uint8(235), uint8(53), uint8(180), uint8(92), uint8(239), uint8(118), uint8(0), uint8(20), uint8(144), uint8(70), uint8(113), uint8(1), uint8(74), uint8(25), uint8(63), uint8(64), uint8(193), uint8(95), uint8(194), uint8(68)), _dafny.SeqOf(uint8(177), uint8(30), uint8(57), uint8(141), uint8(200), uint8(3), uint8(39), uint8(161), uint8(200), uint8(231), uint8(247), uint8(140), uint8(89), uint8(106), uint8(73), uint8(52), uint8(79), uint8(1), uint8(46), uint8(218), uint8(45), uint8(78), uint8(250), uint8(216), uint8(160), uint8(80), uint8(204), uint8(76), uint8(25), uint8(175), uint8(169), uint8(124), uint8(89), uint8(4), uint8(90), uint8(153), uint8(202), uint8(199), uint8(130), uint8(114), uint8(113), uint8(203), uint8(65), uint8(198), uint8(94), uint8(89), uint8(14), uint8(9), uint8(218), uint8(50), uint8(117), uint8(96), uint8(12), uint8(47), uint8(9), uint8(184), uint8(54), uint8(119), uint8(147), uint8(169), uint8(172), uint8(163), uint8(219), uint8(113), uint8(204), uint8(48), uint8(197), uint8(129), uint8(121), uint8(236), uint8(62), uint8(135), uint8(193), uint8(76), uint8(1), uint8(213), uint8(193), uint8(243), uint8(67), uint8(79), uint8(29), uint8(135)))
}
func (_static *CompanionStruct_Default___) A3() RFCTestVector {
	return Companion_RFCTestVector_.Create_RFCTestVector_(_dafny.SeqOfString("A.3.  Test Case 3"), m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_(), _dafny.SeqOf(uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11)), _dafny.SeqOf(), _dafny.SeqOf(), int32(42), _dafny.SeqOf(uint8(25), uint8(239), uint8(36), uint8(163), uint8(44), uint8(113), uint8(123), uint8(22), uint8(127), uint8(51), uint8(169), uint8(29), uint8(111), uint8(100), uint8(139), uint8(223), uint8(150), uint8(89), uint8(103), uint8(118), uint8(175), uint8(219), uint8(99), uint8(119), uint8(172), uint8(67), uint8(76), uint8(28), uint8(41), uint8(60), uint8(203), uint8(4)), _dafny.SeqOf(uint8(141), uint8(164), uint8(231), uint8(117), uint8(165), uint8(99), uint8(193), uint8(143), uint8(113), uint8(95), uint8(128), uint8(42), uint8(6), uint8(60), uint8(90), uint8(49), uint8(184), uint8(161), uint8(31), uint8(92), uint8(94), uint8(225), uint8(135), uint8(158), uint8(195), uint8(69), uint8(78), uint8(95), uint8(60), uint8(115), uint8(141), uint8(45), uint8(157), uint8(32), uint8(19), uint8(149), uint8(250), uint8(164), uint8(182), uint8(26), uint8(150), uint8(200)))
}
func (_static *CompanionStruct_Default___) TestVectors() _dafny.Sequence {
	return _dafny.SeqOf(Companion_Default___.A1(), Companion_Default___.A2(), Companion_Default___.A3())
}

// End of class Default__

// Definition of datatype RFCTestVector
type RFCTestVector struct {
	Data_RFCTestVector_
}

func (_this RFCTestVector) Get_() Data_RFCTestVector_ {
	return _this.Data_RFCTestVector_
}

type Data_RFCTestVector_ interface {
	isRFCTestVector()
}

type CompanionStruct_RFCTestVector_ struct {
}

var Companion_RFCTestVector_ = CompanionStruct_RFCTestVector_{}

type RFCTestVector_RFCTestVector struct {
	Name _dafny.Sequence
	Hash m_AwsCryptographyPrimitivesTypes.DigestAlgorithm
	IKM  _dafny.Sequence
	Salt _dafny.Sequence
	Info _dafny.Sequence
	L    int32
	PRK  _dafny.Sequence
	OKM  _dafny.Sequence
}

func (RFCTestVector_RFCTestVector) isRFCTestVector() {}

func (CompanionStruct_RFCTestVector_) Create_RFCTestVector_(Name _dafny.Sequence, Hash m_AwsCryptographyPrimitivesTypes.DigestAlgorithm, IKM _dafny.Sequence, Salt _dafny.Sequence, Info _dafny.Sequence, L int32, PRK _dafny.Sequence, OKM _dafny.Sequence) RFCTestVector {
	return RFCTestVector{RFCTestVector_RFCTestVector{Name, Hash, IKM, Salt, Info, L, PRK, OKM}}
}

func (_this RFCTestVector) Is_RFCTestVector() bool {
	_, ok := _this.Get_().(RFCTestVector_RFCTestVector)
	return ok
}

func (CompanionStruct_RFCTestVector_) Default() RFCTestVector {
	return Companion_RFCTestVector_.Create_RFCTestVector_(_dafny.EmptySeq.SetString(), m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Default(), _dafny.EmptySeq, _dafny.EmptySeq, _dafny.EmptySeq, int32(0), _dafny.EmptySeq, _dafny.EmptySeq)
}

func (_this RFCTestVector) Dtor_name() _dafny.Sequence {
	return _this.Get_().(RFCTestVector_RFCTestVector).Name
}

func (_this RFCTestVector) Dtor_hash() m_AwsCryptographyPrimitivesTypes.DigestAlgorithm {
	return _this.Get_().(RFCTestVector_RFCTestVector).Hash
}

func (_this RFCTestVector) Dtor_IKM() _dafny.Sequence {
	return _this.Get_().(RFCTestVector_RFCTestVector).IKM
}

func (_this RFCTestVector) Dtor_salt() _dafny.Sequence {
	return _this.Get_().(RFCTestVector_RFCTestVector).Salt
}

func (_this RFCTestVector) Dtor_info() _dafny.Sequence {
	return _this.Get_().(RFCTestVector_RFCTestVector).Info
}

func (_this RFCTestVector) Dtor_L() int32 {
	return _this.Get_().(RFCTestVector_RFCTestVector).L
}

func (_this RFCTestVector) Dtor_PRK() _dafny.Sequence {
	return _this.Get_().(RFCTestVector_RFCTestVector).PRK
}

func (_this RFCTestVector) Dtor_OKM() _dafny.Sequence {
	return _this.Get_().(RFCTestVector_RFCTestVector).OKM
}

func (_this RFCTestVector) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case RFCTestVector_RFCTestVector:
		{
			return "TestHKDF_Rfc5869TestVectors.RFCTestVector.RFCTestVector" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Hash) + ", " + _dafny.String(data.IKM) + ", " + _dafny.String(data.Salt) + ", " + _dafny.String(data.Info) + ", " + _dafny.String(data.L) + ", " + _dafny.String(data.PRK) + ", " + _dafny.String(data.OKM) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this RFCTestVector) Equals(other RFCTestVector) bool {
	switch data1 := _this.Get_().(type) {
	case RFCTestVector_RFCTestVector:
		{
			data2, ok := other.Get_().(RFCTestVector_RFCTestVector)
			return ok && data1.Name.Equals(data2.Name) && data1.Hash.Equals(data2.Hash) && data1.IKM.Equals(data2.IKM) && data1.Salt.Equals(data2.Salt) && data1.Info.Equals(data2.Info) && data1.L == data2.L && data1.PRK.Equals(data2.PRK) && data1.OKM.Equals(data2.OKM)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this RFCTestVector) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(RFCTestVector)
	return ok && _this.Equals(typed)
}

func Type_RFCTestVector_() _dafny.TypeDescriptor {
	return type_RFCTestVector_{}
}

type type_RFCTestVector_ struct {
}

func (_this type_RFCTestVector_) Default() interface{} {
	return Companion_RFCTestVector_.Default()
}

func (_this type_RFCTestVector_) String() string {
	return "TestHKDF__Rfc5869TestVectors.RFCTestVector"
}
func (_this RFCTestVector) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = RFCTestVector{}

// End of datatype RFCTestVector
