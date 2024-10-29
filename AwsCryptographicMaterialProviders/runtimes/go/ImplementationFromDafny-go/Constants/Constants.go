// Package Constants
// Dafny module Constants compiled into Go

package Constants

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/ComAmazonawsDynamodbTypes"
	m_Com_Amazonaws_Dynamodb "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/Com_Amazonaws_Dynamodb"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/kms/ComAmazonawsKmsTypes"
	m_Com_Amazonaws_Kms "github.com/aws/aws-cryptographic-material-providers-library/kms/Com_Amazonaws_Kms"
	m_AlgorithmSuites "github.com/aws/aws-cryptographic-material-providers-library/mpl/AlgorithmSuites"
	m_AwsArnParsing "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsArnParsing"
	m_AwsCryptographyKeyStoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyKeyStoreOperations"
	m_AwsCryptographyKeyStoreTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyKeyStoreTypes"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsMrkAreUnique "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkAreUnique"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsUtils"
	m_CreateKeyStoreTable "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeyStoreTable"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/DDBKeystoreOperations"
	m_GetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/GetKeys"
	m_KMSKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/KMSKeystoreOperations"
	m_KeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStore"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStoreErrorMessages"
	m_Keyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/Keyring"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/mpl/KmsArn"
	m_Materials "github.com/aws/aws-cryptographic-material-providers-library/mpl/Materials"
	m_MultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MultiKeyring"
	m_Structure "github.com/aws/aws-cryptographic-material-providers-library/mpl/Structure"
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
	m_UTF8 "github.com/dafny-lang/DafnyStandardLibGo/UTF8"
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
var _ m_ComAmazonawsDynamodbTypes.Dummy__
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
var _ m_AwsCryptographyKeyStoreTypes.Dummy__
var _ m_AwsCryptographyMaterialProvidersTypes.Dummy__
var _ m_AwsArnParsing.Dummy__
var _ m_AwsKmsMrkMatchForDecrypt.Dummy__
var _ m_AwsKmsUtils.Dummy__
var _ m_KeyStoreErrorMessages.Dummy__
var _ m_KmsArn.Dummy__
var _ m_Structure.Dummy__
var _ m_KMSKeystoreOperations.Dummy__
var _ m_DDBKeystoreOperations.Dummy__
var _ m_CreateKeys.Dummy__
var _ m_CreateKeyStoreTable.Dummy__
var _ m_GetKeys.Dummy__
var _ m_AwsCryptographyKeyStoreOperations.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__
var _ m_KeyStore.Dummy__
var _ m_AlgorithmSuites.Dummy__
var _ m_Materials.Dummy__
var _ m_Keyring.Dummy__
var _ m_MultiKeyring.Dummy__
var _ m_AwsKmsMrkAreUnique.Dummy__

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
	return "Constants.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) ECDH__PROVIDER__INFO__RPL__INDEX() uint32 {
	return uint32(1)
}
func (_static *CompanionStruct_Default___) ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN() _dafny.Int {
	return _dafny.IntOfInt64(4)
}
func (_static *CompanionStruct_Default___) ECDH__PROVIDER__INFO__RPK__INDEX() uint32 {
	return (Companion_Default___.ECDH__PROVIDER__INFO__RPL__INDEX()) + ((Companion_Default___.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN()).Uint32())
}
func (_static *CompanionStruct_Default___) ECDH__AES__256__ENC__KEY__LENGTH() int32 {
	return int32(32)
}
func (_static *CompanionStruct_Default___) ECDH__AES__256__ENC__TAG__LENGTH() int32 {
	return int32(16)
}
func (_static *CompanionStruct_Default___) ECDH__AES__256__ENC__IV__LENGTH() int32 {
	return int32(12)
}
func (_static *CompanionStruct_Default___) ECDH__AES__256__ENC__ALG() m_AwsCryptographyPrimitivesTypes.AES__GCM {
	return m_AwsCryptographyPrimitivesTypes.Companion_AES__GCM_.Create_AES__GCM_(Companion_Default___.ECDH__AES__256__ENC__KEY__LENGTH(), Companion_Default___.ECDH__AES__256__ENC__TAG__LENGTH(), Companion_Default___.ECDH__AES__256__ENC__IV__LENGTH())
}
func (_static *CompanionStruct_Default___) PROVIDER__ID() _dafny.Sequence {
	var _0_s _dafny.Sequence = _dafny.SeqOf(uint8(97), uint8(119), uint8(115), uint8(45), uint8(107), uint8(109), uint8(115))
	_ = _0_s
	return _0_s
}
func (_static *CompanionStruct_Default___) UINT32__TO__SEQ__LEN() _dafny.Int {
	return _dafny.IntOfInt64(4)
}
func (_static *CompanionStruct_Default___) KDF__SALT__LEN() int32 {
	return int32(32)
}
func (_static *CompanionStruct_Default___) KDF__EXPECTED__LEN() int32 {
	return int32(64)
}
func (_static *CompanionStruct_Default___) ECDH__COMMITMENT__KEY__LENGTH() _dafny.Int {
	return _dafny.IntOfInt64(32)
}
func (_static *CompanionStruct_Default___) ECDH__COMMITMENT__KEY__INDEX() _dafny.Int {
	return _dafny.IntOfInt64(32)
}
func (_static *CompanionStruct_Default___) ECDH__WRAPPED__KEY__MATERIAL__INDEX() _dafny.Int {
	return _dafny.IntOfInt64(64)
}
func (_static *CompanionStruct_Default___) ECDH__KDF__STRING() _dafny.Sequence {
	return _dafny.SeqOfString("ecdh-key-derivation")
}
func (_static *CompanionStruct_Default___) ECDH__KDF__PRF__STRING() _dafny.Sequence {
	return _dafny.SeqOfString("HMAC_SHA384")
}
func (_static *CompanionStruct_Default___) ECDH__KDF__DELIMETER() _dafny.Sequence {
	return _dafny.SeqOf(uint8(0))
}
func (_static *CompanionStruct_Default___) ECDH__PROVIDER__INFO__256__LEN() uint32 {
	return uint32(75)
}
func (_static *CompanionStruct_Default___) ECDH__PROVIDER__INFO__384__LEN() uint32 {
	return uint32(107)
}
func (_static *CompanionStruct_Default___) ECDH__PROVIDER__INFO__521__LEN() uint32 {
	return uint32(143)
}
func (_static *CompanionStruct_Default___) ECDH__PUBLIC__KEY__LEN__ECC__NIST__256() _dafny.Int {
	return _dafny.IntOfInt64(91)
}
func (_static *CompanionStruct_Default___) ECDH__PUBLIC__KEY__LEN__ECC__NIST__384() _dafny.Int {
	return _dafny.IntOfInt64(120)
}
func (_static *CompanionStruct_Default___) ECDH__PUBLIC__KEY__LEN__ECC__NIST__521() _dafny.Int {
	return _dafny.IntOfInt64(158)
}
func (_static *CompanionStruct_Default___) ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__256() _dafny.Int {
	return _dafny.IntOfInt64(33)
}
func (_static *CompanionStruct_Default___) ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__384() _dafny.Int {
	return _dafny.IntOfInt64(49)
}
func (_static *CompanionStruct_Default___) ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__521() _dafny.Int {
	return _dafny.IntOfInt64(67)
}
func (_static *CompanionStruct_Default___) CIPHERTEXT__WRAPPED__MATERIAL__INDEX() _dafny.Int {
	return _dafny.IntOfInt64(68)
}
func (_static *CompanionStruct_Default___) PROVIDER__ID__HIERARCHY() _dafny.Sequence {
	var _0_s _dafny.Sequence = _dafny.SeqOf(uint8(97), uint8(119), uint8(115), uint8(45), uint8(107), uint8(109), uint8(115), uint8(45), uint8(104), uint8(105), uint8(101), uint8(114), uint8(97), uint8(114), uint8(99), uint8(104), uint8(121))
	_ = _0_s
	return _0_s
}
func (_static *CompanionStruct_Default___) RSA__PROVIDER__ID() _dafny.Sequence {
	var _0_s _dafny.Sequence = _dafny.SeqOf(uint8(97), uint8(119), uint8(115), uint8(45), uint8(107), uint8(109), uint8(115), uint8(45), uint8(114), uint8(115), uint8(97))
	_ = _0_s
	return _0_s
}
func (_static *CompanionStruct_Default___) KMS__ECDH__PROVIDER__ID() _dafny.Sequence {
	return m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("aws-kms-ecdh"))
}
func (_static *CompanionStruct_Default___) RAW__ECDH__PROVIDER__ID() _dafny.Sequence {
	return m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("raw-ecdh"))
}
func (_static *CompanionStruct_Default___) ECDH__KDF__PRF__NAME() _dafny.Sequence {
	return m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("HMAC_SHA384"))
}
func (_static *CompanionStruct_Default___) ECDH__KDF__UTF8() _dafny.Sequence {
	return m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("ecdh-key-derivation"))
}

// End of class Default__

// Definition of class AwsKmsEncryptedDataKey
type AwsKmsEncryptedDataKey struct {
}

func New_AwsKmsEncryptedDataKey_() *AwsKmsEncryptedDataKey {
	_this := AwsKmsEncryptedDataKey{}

	return &_this
}

type CompanionStruct_AwsKmsEncryptedDataKey_ struct {
}

var Companion_AwsKmsEncryptedDataKey_ = CompanionStruct_AwsKmsEncryptedDataKey_{}

func (*AwsKmsEncryptedDataKey) String() string {
	return "Constants.AwsKmsEncryptedDataKey"
}

// End of class AwsKmsEncryptedDataKey

func Type_AwsKmsEncryptedDataKey_() _dafny.TypeDescriptor {
	return type_AwsKmsEncryptedDataKey_{}
}

type type_AwsKmsEncryptedDataKey_ struct {
}

func (_this type_AwsKmsEncryptedDataKey_) Default() interface{} {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptedDataKey_.Default()
}

func (_this type_AwsKmsEncryptedDataKey_) String() string {
	return "Constants.AwsKmsEncryptedDataKey"
}
func (_this *CompanionStruct_AwsKmsEncryptedDataKey_) Is_(__source m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey) bool {
	var _0_edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey = (__source)
	_ = _0_edk
	return (_dafny.Companion_Sequence_.Equal((_0_edk).Dtor_keyProviderId(), Companion_Default___.PROVIDER__ID())) && (m_UTF8.Companion_Default___.ValidUTF8Seq((_0_edk).Dtor_keyProviderInfo()))
}

// Definition of datatype AwsKmsEdkHelper
type AwsKmsEdkHelper struct {
	Data_AwsKmsEdkHelper_
}

func (_this AwsKmsEdkHelper) Get_() Data_AwsKmsEdkHelper_ {
	return _this.Data_AwsKmsEdkHelper_
}

type Data_AwsKmsEdkHelper_ interface {
	isAwsKmsEdkHelper()
}

type CompanionStruct_AwsKmsEdkHelper_ struct {
}

var Companion_AwsKmsEdkHelper_ = CompanionStruct_AwsKmsEdkHelper_{}

type AwsKmsEdkHelper_AwsKmsEdkHelper struct {
	Edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
	Arn m_AwsArnParsing.AwsArn
}

func (AwsKmsEdkHelper_AwsKmsEdkHelper) isAwsKmsEdkHelper() {}

func (CompanionStruct_AwsKmsEdkHelper_) Create_AwsKmsEdkHelper_(Edk m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey, Arn m_AwsArnParsing.AwsArn) AwsKmsEdkHelper {
	return AwsKmsEdkHelper{AwsKmsEdkHelper_AwsKmsEdkHelper{Edk, Arn}}
}

func (_this AwsKmsEdkHelper) Is_AwsKmsEdkHelper() bool {
	_, ok := _this.Get_().(AwsKmsEdkHelper_AwsKmsEdkHelper)
	return ok
}

func (CompanionStruct_AwsKmsEdkHelper_) Default() AwsKmsEdkHelper {
	return Companion_AwsKmsEdkHelper_.Create_AwsKmsEdkHelper_(m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptedDataKey_.Default(), m_AwsArnParsing.Companion_AwsArn_.Default())
}

func (_this AwsKmsEdkHelper) Dtor_edk() m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey {
	return _this.Get_().(AwsKmsEdkHelper_AwsKmsEdkHelper).Edk
}

func (_this AwsKmsEdkHelper) Dtor_arn() m_AwsArnParsing.AwsArn {
	return _this.Get_().(AwsKmsEdkHelper_AwsKmsEdkHelper).Arn
}

func (_this AwsKmsEdkHelper) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case AwsKmsEdkHelper_AwsKmsEdkHelper:
		{
			return "Constants.AwsKmsEdkHelper.AwsKmsEdkHelper" + "(" + _dafny.String(data.Edk) + ", " + _dafny.String(data.Arn) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this AwsKmsEdkHelper) Equals(other AwsKmsEdkHelper) bool {
	switch data1 := _this.Get_().(type) {
	case AwsKmsEdkHelper_AwsKmsEdkHelper:
		{
			data2, ok := other.Get_().(AwsKmsEdkHelper_AwsKmsEdkHelper)
			return ok && data1.Edk.Equals(data2.Edk) && data1.Arn.Equals(data2.Arn)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this AwsKmsEdkHelper) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(AwsKmsEdkHelper)
	return ok && _this.Equals(typed)
}

func Type_AwsKmsEdkHelper_() _dafny.TypeDescriptor {
	return type_AwsKmsEdkHelper_{}
}

type type_AwsKmsEdkHelper_ struct {
}

func (_this type_AwsKmsEdkHelper_) Default() interface{} {
	return Companion_AwsKmsEdkHelper_.Default()
}

func (_this type_AwsKmsEdkHelper_) String() string {
	return "Constants.AwsKmsEdkHelper"
}
func (_this AwsKmsEdkHelper) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = AwsKmsEdkHelper{}

// End of datatype AwsKmsEdkHelper
