// Package MaterialWrapping
// Dafny module MaterialWrapping compiled into Go

package MaterialWrapping

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
	m_Constants "github.com/aws/aws-cryptographic-material-providers-library/mpl/Constants"
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
var _ m_Constants.Dummy__

type Dummy__ struct{}

// Definition of datatype GenerateAndWrapInput
type GenerateAndWrapInput struct {
	Data_GenerateAndWrapInput_
}

func (_this GenerateAndWrapInput) Get_() Data_GenerateAndWrapInput_ {
	return _this.Data_GenerateAndWrapInput_
}

type Data_GenerateAndWrapInput_ interface {
	isGenerateAndWrapInput()
}

type CompanionStruct_GenerateAndWrapInput_ struct {
}

var Companion_GenerateAndWrapInput_ = CompanionStruct_GenerateAndWrapInput_{}

type GenerateAndWrapInput_GenerateAndWrapInput struct {
	AlgorithmSuite    m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	EncryptionContext _dafny.Map
}

func (GenerateAndWrapInput_GenerateAndWrapInput) isGenerateAndWrapInput() {}

func (CompanionStruct_GenerateAndWrapInput_) Create_GenerateAndWrapInput_(AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, EncryptionContext _dafny.Map) GenerateAndWrapInput {
	return GenerateAndWrapInput{GenerateAndWrapInput_GenerateAndWrapInput{AlgorithmSuite, EncryptionContext}}
}

func (_this GenerateAndWrapInput) Is_GenerateAndWrapInput() bool {
	_, ok := _this.Get_().(GenerateAndWrapInput_GenerateAndWrapInput)
	return ok
}

func (CompanionStruct_GenerateAndWrapInput_) Default() GenerateAndWrapInput {
	return Companion_GenerateAndWrapInput_.Create_GenerateAndWrapInput_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Default(), _dafny.EmptyMap)
}

func (_this GenerateAndWrapInput) Dtor_algorithmSuite() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return _this.Get_().(GenerateAndWrapInput_GenerateAndWrapInput).AlgorithmSuite
}

func (_this GenerateAndWrapInput) Dtor_encryptionContext() _dafny.Map {
	return _this.Get_().(GenerateAndWrapInput_GenerateAndWrapInput).EncryptionContext
}

func (_this GenerateAndWrapInput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case GenerateAndWrapInput_GenerateAndWrapInput:
		{
			return "MaterialWrapping.GenerateAndWrapInput.GenerateAndWrapInput" + "(" + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.EncryptionContext) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this GenerateAndWrapInput) Equals(other GenerateAndWrapInput) bool {
	switch data1 := _this.Get_().(type) {
	case GenerateAndWrapInput_GenerateAndWrapInput:
		{
			data2, ok := other.Get_().(GenerateAndWrapInput_GenerateAndWrapInput)
			return ok && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.EncryptionContext.Equals(data2.EncryptionContext)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this GenerateAndWrapInput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(GenerateAndWrapInput)
	return ok && _this.Equals(typed)
}

func Type_GenerateAndWrapInput_() _dafny.TypeDescriptor {
	return type_GenerateAndWrapInput_{}
}

type type_GenerateAndWrapInput_ struct {
}

func (_this type_GenerateAndWrapInput_) Default() interface{} {
	return Companion_GenerateAndWrapInput_.Default()
}

func (_this type_GenerateAndWrapInput_) String() string {
	return "MaterialWrapping.GenerateAndWrapInput"
}
func (_this GenerateAndWrapInput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = GenerateAndWrapInput{}

// End of datatype GenerateAndWrapInput

// Definition of datatype GenerateAndWrapOutput
type GenerateAndWrapOutput struct {
	Data_GenerateAndWrapOutput_
}

func (_this GenerateAndWrapOutput) Get_() Data_GenerateAndWrapOutput_ {
	return _this.Data_GenerateAndWrapOutput_
}

type Data_GenerateAndWrapOutput_ interface {
	isGenerateAndWrapOutput()
}

type CompanionStruct_GenerateAndWrapOutput_ struct {
}

var Companion_GenerateAndWrapOutput_ = CompanionStruct_GenerateAndWrapOutput_{}

type GenerateAndWrapOutput_GenerateAndWrapOutput struct {
	PlaintextMaterial _dafny.Sequence
	WrappedMaterial   _dafny.Sequence
	WrapInfo          interface{}
}

func (GenerateAndWrapOutput_GenerateAndWrapOutput) isGenerateAndWrapOutput() {}

func (CompanionStruct_GenerateAndWrapOutput_) Create_GenerateAndWrapOutput_(PlaintextMaterial _dafny.Sequence, WrappedMaterial _dafny.Sequence, WrapInfo interface{}) GenerateAndWrapOutput {
	return GenerateAndWrapOutput{GenerateAndWrapOutput_GenerateAndWrapOutput{PlaintextMaterial, WrappedMaterial, WrapInfo}}
}

func (_this GenerateAndWrapOutput) Is_GenerateAndWrapOutput() bool {
	_, ok := _this.Get_().(GenerateAndWrapOutput_GenerateAndWrapOutput)
	return ok
}

func (CompanionStruct_GenerateAndWrapOutput_) Default(_default_T interface{}) GenerateAndWrapOutput {
	return Companion_GenerateAndWrapOutput_.Create_GenerateAndWrapOutput_(_dafny.EmptySeq, _dafny.EmptySeq, _default_T)
}

func (_this GenerateAndWrapOutput) Dtor_plaintextMaterial() _dafny.Sequence {
	return _this.Get_().(GenerateAndWrapOutput_GenerateAndWrapOutput).PlaintextMaterial
}

func (_this GenerateAndWrapOutput) Dtor_wrappedMaterial() _dafny.Sequence {
	return _this.Get_().(GenerateAndWrapOutput_GenerateAndWrapOutput).WrappedMaterial
}

func (_this GenerateAndWrapOutput) Dtor_wrapInfo() interface{} {
	return _this.Get_().(GenerateAndWrapOutput_GenerateAndWrapOutput).WrapInfo
}

func (_this GenerateAndWrapOutput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case GenerateAndWrapOutput_GenerateAndWrapOutput:
		{
			return "MaterialWrapping.GenerateAndWrapOutput.GenerateAndWrapOutput" + "(" + _dafny.String(data.PlaintextMaterial) + ", " + _dafny.String(data.WrappedMaterial) + ", " + _dafny.String(data.WrapInfo) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this GenerateAndWrapOutput) Equals(other GenerateAndWrapOutput) bool {
	switch data1 := _this.Get_().(type) {
	case GenerateAndWrapOutput_GenerateAndWrapOutput:
		{
			data2, ok := other.Get_().(GenerateAndWrapOutput_GenerateAndWrapOutput)
			return ok && data1.PlaintextMaterial.Equals(data2.PlaintextMaterial) && data1.WrappedMaterial.Equals(data2.WrappedMaterial) && _dafny.AreEqual(data1.WrapInfo, data2.WrapInfo)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this GenerateAndWrapOutput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(GenerateAndWrapOutput)
	return ok && _this.Equals(typed)
}

func Type_GenerateAndWrapOutput_(Type_T_ _dafny.TypeDescriptor) _dafny.TypeDescriptor {
	return type_GenerateAndWrapOutput_{Type_T_}
}

type type_GenerateAndWrapOutput_ struct {
	Type_T_ _dafny.TypeDescriptor
}

func (_this type_GenerateAndWrapOutput_) Default() interface{} {
	Type_T_ := _this.Type_T_
	_ = Type_T_
	return Companion_GenerateAndWrapOutput_.Default(Type_T_.Default())
}

func (_this type_GenerateAndWrapOutput_) String() string {
	return "MaterialWrapping.GenerateAndWrapOutput"
}
func (_this GenerateAndWrapOutput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = GenerateAndWrapOutput{}

// End of datatype GenerateAndWrapOutput

// Definition of datatype WrapInput
type WrapInput struct {
	Data_WrapInput_
}

func (_this WrapInput) Get_() Data_WrapInput_ {
	return _this.Data_WrapInput_
}

type Data_WrapInput_ interface {
	isWrapInput()
}

type CompanionStruct_WrapInput_ struct {
}

var Companion_WrapInput_ = CompanionStruct_WrapInput_{}

type WrapInput_WrapInput struct {
	PlaintextMaterial _dafny.Sequence
	AlgorithmSuite    m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	EncryptionContext _dafny.Map
}

func (WrapInput_WrapInput) isWrapInput() {}

func (CompanionStruct_WrapInput_) Create_WrapInput_(PlaintextMaterial _dafny.Sequence, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, EncryptionContext _dafny.Map) WrapInput {
	return WrapInput{WrapInput_WrapInput{PlaintextMaterial, AlgorithmSuite, EncryptionContext}}
}

func (_this WrapInput) Is_WrapInput() bool {
	_, ok := _this.Get_().(WrapInput_WrapInput)
	return ok
}

func (CompanionStruct_WrapInput_) Default() WrapInput {
	return Companion_WrapInput_.Create_WrapInput_(_dafny.EmptySeq, m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Default(), _dafny.EmptyMap)
}

func (_this WrapInput) Dtor_plaintextMaterial() _dafny.Sequence {
	return _this.Get_().(WrapInput_WrapInput).PlaintextMaterial
}

func (_this WrapInput) Dtor_algorithmSuite() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return _this.Get_().(WrapInput_WrapInput).AlgorithmSuite
}

func (_this WrapInput) Dtor_encryptionContext() _dafny.Map {
	return _this.Get_().(WrapInput_WrapInput).EncryptionContext
}

func (_this WrapInput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case WrapInput_WrapInput:
		{
			return "MaterialWrapping.WrapInput.WrapInput" + "(" + _dafny.String(data.PlaintextMaterial) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.EncryptionContext) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this WrapInput) Equals(other WrapInput) bool {
	switch data1 := _this.Get_().(type) {
	case WrapInput_WrapInput:
		{
			data2, ok := other.Get_().(WrapInput_WrapInput)
			return ok && data1.PlaintextMaterial.Equals(data2.PlaintextMaterial) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.EncryptionContext.Equals(data2.EncryptionContext)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this WrapInput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(WrapInput)
	return ok && _this.Equals(typed)
}

func Type_WrapInput_() _dafny.TypeDescriptor {
	return type_WrapInput_{}
}

type type_WrapInput_ struct {
}

func (_this type_WrapInput_) Default() interface{} {
	return Companion_WrapInput_.Default()
}

func (_this type_WrapInput_) String() string {
	return "MaterialWrapping.WrapInput"
}
func (_this WrapInput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = WrapInput{}

// End of datatype WrapInput

// Definition of datatype WrapOutput
type WrapOutput struct {
	Data_WrapOutput_
}

func (_this WrapOutput) Get_() Data_WrapOutput_ {
	return _this.Data_WrapOutput_
}

type Data_WrapOutput_ interface {
	isWrapOutput()
}

type CompanionStruct_WrapOutput_ struct {
}

var Companion_WrapOutput_ = CompanionStruct_WrapOutput_{}

type WrapOutput_WrapOutput struct {
	WrappedMaterial _dafny.Sequence
	WrapInfo        interface{}
}

func (WrapOutput_WrapOutput) isWrapOutput() {}

func (CompanionStruct_WrapOutput_) Create_WrapOutput_(WrappedMaterial _dafny.Sequence, WrapInfo interface{}) WrapOutput {
	return WrapOutput{WrapOutput_WrapOutput{WrappedMaterial, WrapInfo}}
}

func (_this WrapOutput) Is_WrapOutput() bool {
	_, ok := _this.Get_().(WrapOutput_WrapOutput)
	return ok
}

func (CompanionStruct_WrapOutput_) Default(_default_T interface{}) WrapOutput {
	return Companion_WrapOutput_.Create_WrapOutput_(_dafny.EmptySeq, _default_T)
}

func (_this WrapOutput) Dtor_wrappedMaterial() _dafny.Sequence {
	return _this.Get_().(WrapOutput_WrapOutput).WrappedMaterial
}

func (_this WrapOutput) Dtor_wrapInfo() interface{} {
	return _this.Get_().(WrapOutput_WrapOutput).WrapInfo
}

func (_this WrapOutput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case WrapOutput_WrapOutput:
		{
			return "MaterialWrapping.WrapOutput.WrapOutput" + "(" + _dafny.String(data.WrappedMaterial) + ", " + _dafny.String(data.WrapInfo) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this WrapOutput) Equals(other WrapOutput) bool {
	switch data1 := _this.Get_().(type) {
	case WrapOutput_WrapOutput:
		{
			data2, ok := other.Get_().(WrapOutput_WrapOutput)
			return ok && data1.WrappedMaterial.Equals(data2.WrappedMaterial) && _dafny.AreEqual(data1.WrapInfo, data2.WrapInfo)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this WrapOutput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(WrapOutput)
	return ok && _this.Equals(typed)
}

func Type_WrapOutput_(Type_T_ _dafny.TypeDescriptor) _dafny.TypeDescriptor {
	return type_WrapOutput_{Type_T_}
}

type type_WrapOutput_ struct {
	Type_T_ _dafny.TypeDescriptor
}

func (_this type_WrapOutput_) Default() interface{} {
	Type_T_ := _this.Type_T_
	_ = Type_T_
	return Companion_WrapOutput_.Default(Type_T_.Default())
}

func (_this type_WrapOutput_) String() string {
	return "MaterialWrapping.WrapOutput"
}
func (_this WrapOutput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = WrapOutput{}

// End of datatype WrapOutput

// Definition of datatype UnwrapInput
type UnwrapInput struct {
	Data_UnwrapInput_
}

func (_this UnwrapInput) Get_() Data_UnwrapInput_ {
	return _this.Data_UnwrapInput_
}

type Data_UnwrapInput_ interface {
	isUnwrapInput()
}

type CompanionStruct_UnwrapInput_ struct {
}

var Companion_UnwrapInput_ = CompanionStruct_UnwrapInput_{}

type UnwrapInput_UnwrapInput struct {
	WrappedMaterial   _dafny.Sequence
	AlgorithmSuite    m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	EncryptionContext _dafny.Map
}

func (UnwrapInput_UnwrapInput) isUnwrapInput() {}

func (CompanionStruct_UnwrapInput_) Create_UnwrapInput_(WrappedMaterial _dafny.Sequence, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, EncryptionContext _dafny.Map) UnwrapInput {
	return UnwrapInput{UnwrapInput_UnwrapInput{WrappedMaterial, AlgorithmSuite, EncryptionContext}}
}

func (_this UnwrapInput) Is_UnwrapInput() bool {
	_, ok := _this.Get_().(UnwrapInput_UnwrapInput)
	return ok
}

func (CompanionStruct_UnwrapInput_) Default() UnwrapInput {
	return Companion_UnwrapInput_.Create_UnwrapInput_(_dafny.EmptySeq, m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Default(), _dafny.EmptyMap)
}

func (_this UnwrapInput) Dtor_wrappedMaterial() _dafny.Sequence {
	return _this.Get_().(UnwrapInput_UnwrapInput).WrappedMaterial
}

func (_this UnwrapInput) Dtor_algorithmSuite() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return _this.Get_().(UnwrapInput_UnwrapInput).AlgorithmSuite
}

func (_this UnwrapInput) Dtor_encryptionContext() _dafny.Map {
	return _this.Get_().(UnwrapInput_UnwrapInput).EncryptionContext
}

func (_this UnwrapInput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case UnwrapInput_UnwrapInput:
		{
			return "MaterialWrapping.UnwrapInput.UnwrapInput" + "(" + _dafny.String(data.WrappedMaterial) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.EncryptionContext) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this UnwrapInput) Equals(other UnwrapInput) bool {
	switch data1 := _this.Get_().(type) {
	case UnwrapInput_UnwrapInput:
		{
			data2, ok := other.Get_().(UnwrapInput_UnwrapInput)
			return ok && data1.WrappedMaterial.Equals(data2.WrappedMaterial) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.EncryptionContext.Equals(data2.EncryptionContext)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this UnwrapInput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(UnwrapInput)
	return ok && _this.Equals(typed)
}

func Type_UnwrapInput_() _dafny.TypeDescriptor {
	return type_UnwrapInput_{}
}

type type_UnwrapInput_ struct {
}

func (_this type_UnwrapInput_) Default() interface{} {
	return Companion_UnwrapInput_.Default()
}

func (_this type_UnwrapInput_) String() string {
	return "MaterialWrapping.UnwrapInput"
}
func (_this UnwrapInput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = UnwrapInput{}

// End of datatype UnwrapInput

// Definition of datatype UnwrapOutput
type UnwrapOutput struct {
	Data_UnwrapOutput_
}

func (_this UnwrapOutput) Get_() Data_UnwrapOutput_ {
	return _this.Data_UnwrapOutput_
}

type Data_UnwrapOutput_ interface {
	isUnwrapOutput()
}

type CompanionStruct_UnwrapOutput_ struct {
}

var Companion_UnwrapOutput_ = CompanionStruct_UnwrapOutput_{}

type UnwrapOutput_UnwrapOutput struct {
	UnwrappedMaterial _dafny.Sequence
	UnwrapInfo        interface{}
}

func (UnwrapOutput_UnwrapOutput) isUnwrapOutput() {}

func (CompanionStruct_UnwrapOutput_) Create_UnwrapOutput_(UnwrappedMaterial _dafny.Sequence, UnwrapInfo interface{}) UnwrapOutput {
	return UnwrapOutput{UnwrapOutput_UnwrapOutput{UnwrappedMaterial, UnwrapInfo}}
}

func (_this UnwrapOutput) Is_UnwrapOutput() bool {
	_, ok := _this.Get_().(UnwrapOutput_UnwrapOutput)
	return ok
}

func (CompanionStruct_UnwrapOutput_) Default(_default_T interface{}) UnwrapOutput {
	return Companion_UnwrapOutput_.Create_UnwrapOutput_(_dafny.EmptySeq, _default_T)
}

func (_this UnwrapOutput) Dtor_unwrappedMaterial() _dafny.Sequence {
	return _this.Get_().(UnwrapOutput_UnwrapOutput).UnwrappedMaterial
}

func (_this UnwrapOutput) Dtor_unwrapInfo() interface{} {
	return _this.Get_().(UnwrapOutput_UnwrapOutput).UnwrapInfo
}

func (_this UnwrapOutput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case UnwrapOutput_UnwrapOutput:
		{
			return "MaterialWrapping.UnwrapOutput.UnwrapOutput" + "(" + _dafny.String(data.UnwrappedMaterial) + ", " + _dafny.String(data.UnwrapInfo) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this UnwrapOutput) Equals(other UnwrapOutput) bool {
	switch data1 := _this.Get_().(type) {
	case UnwrapOutput_UnwrapOutput:
		{
			data2, ok := other.Get_().(UnwrapOutput_UnwrapOutput)
			return ok && data1.UnwrappedMaterial.Equals(data2.UnwrappedMaterial) && _dafny.AreEqual(data1.UnwrapInfo, data2.UnwrapInfo)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this UnwrapOutput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(UnwrapOutput)
	return ok && _this.Equals(typed)
}

func Type_UnwrapOutput_(Type_T_ _dafny.TypeDescriptor) _dafny.TypeDescriptor {
	return type_UnwrapOutput_{Type_T_}
}

type type_UnwrapOutput_ struct {
	Type_T_ _dafny.TypeDescriptor
}

func (_this type_UnwrapOutput_) Default() interface{} {
	Type_T_ := _this.Type_T_
	_ = Type_T_
	return Companion_UnwrapOutput_.Default(Type_T_.Default())
}

func (_this type_UnwrapOutput_) String() string {
	return "MaterialWrapping.UnwrapOutput"
}
func (_this UnwrapOutput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = UnwrapOutput{}

// End of datatype UnwrapOutput

// Definition of trait GenerateAndWrapMaterial
type GenerateAndWrapMaterial interface {
	String() string
	Invoke(a interface{}) interface{}
}
type CompanionStruct_GenerateAndWrapMaterial_ struct {
	TraitID_ *_dafny.TraitID
}

var Companion_GenerateAndWrapMaterial_ = CompanionStruct_GenerateAndWrapMaterial_{
	TraitID_: &_dafny.TraitID{},
}

func (CompanionStruct_GenerateAndWrapMaterial_) CastTo_(x interface{}) GenerateAndWrapMaterial {
	var t GenerateAndWrapMaterial
	t, _ = x.(GenerateAndWrapMaterial)
	return t
}

// End of trait GenerateAndWrapMaterial

// Definition of trait WrapMaterial
type WrapMaterial interface {
	String() string
	Invoke(a interface{}) interface{}
}
type CompanionStruct_WrapMaterial_ struct {
	TraitID_ *_dafny.TraitID
}

var Companion_WrapMaterial_ = CompanionStruct_WrapMaterial_{
	TraitID_: &_dafny.TraitID{},
}

func (CompanionStruct_WrapMaterial_) CastTo_(x interface{}) WrapMaterial {
	var t WrapMaterial
	t, _ = x.(WrapMaterial)
	return t
}

// End of trait WrapMaterial

// Definition of trait UnwrapMaterial
type UnwrapMaterial interface {
	String() string
	Invoke(a interface{}) interface{}
}
type CompanionStruct_UnwrapMaterial_ struct {
	TraitID_ *_dafny.TraitID
}

var Companion_UnwrapMaterial_ = CompanionStruct_UnwrapMaterial_{
	TraitID_: &_dafny.TraitID{},
}

func (CompanionStruct_UnwrapMaterial_) CastTo_(x interface{}) UnwrapMaterial {
	var t UnwrapMaterial
	t, _ = x.(UnwrapMaterial)
	return t
}

// End of trait UnwrapMaterial
