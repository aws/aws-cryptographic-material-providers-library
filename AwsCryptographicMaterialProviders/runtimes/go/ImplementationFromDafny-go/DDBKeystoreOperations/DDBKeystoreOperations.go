// Package DDBKeystoreOperations
// Dafny module DDBKeystoreOperations compiled into Go

package DDBKeystoreOperations

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/ComAmazonawsDynamodbTypes"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/kms/ComAmazonawsKmsTypes"
	m_AwsArnParsing "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsArnParsing"
	m_AwsCryptographyKeyStoreTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyKeyStoreTypes"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsUtils"
	m_KMSKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/KMSKeystoreOperations"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStoreErrorMessages"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/mpl/KmsArn"
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
	return "DDBKeystoreOperations.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) WriteNewKeyToStore(versionBranchKeyItem _dafny.Map, activeBranchKeyItem _dafny.Map, beaconKeyItem _dafny.Map, tableName _dafny.Sequence, ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsDynamodbTypes.Companion_TransactWriteItemsOutput_.Default())
	_ = output
	var _0_items _dafny.Sequence
	_ = _0_items
	_0_items = _dafny.SeqOf(Companion_Default___.CreateTransactWritePutItem(versionBranchKeyItem, tableName, Companion_ConditionExpression_.Create_BRANCH__KEY__NOT__EXIST_()), Companion_Default___.CreateTransactWritePutItem(activeBranchKeyItem, tableName, Companion_ConditionExpression_.Create_BRANCH__KEY__NOT__EXIST_()), Companion_Default___.CreateTransactWritePutItem(beaconKeyItem, tableName, Companion_ConditionExpression_.Create_BRANCH__KEY__NOT__EXIST_()))
	var _1_transactRequest m_ComAmazonawsDynamodbTypes.TransactWriteItemsInput
	_ = _1_transactRequest
	_1_transactRequest = m_ComAmazonawsDynamodbTypes.Companion_TransactWriteItemsInput_.Create_TransactWriteItemsInput_(_0_items, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _2_maybeTransactWriteResponse m_Wrappers.Result
	_ = _2_maybeTransactWriteResponse
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (ddbClient).TransactWriteItems(_1_transactRequest)
	_2_maybeTransactWriteResponse = _out0
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsDynamodbTypes.Companion_TransactWriteItemsOutput_.Default())
	_ = _3_valueOrError0
	_3_valueOrError0 = (_2_maybeTransactWriteResponse).MapFailure(func(coer14 func(m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg14 interface{}) interface{} {
			return coer14(arg14.(m_ComAmazonawsDynamodbTypes.Error))
		}
	}(func(_4_e m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsDynamodb_(_4_e)
	}))
	if (_3_valueOrError0).IsFailure() {
		output = (_3_valueOrError0).PropagateFailure()
		return output
	}
	var _5_transactWriteItemsResponse m_ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
	_ = _5_transactWriteItemsResponse
	_5_transactWriteItemsResponse = (_3_valueOrError0).Extract().(m_ComAmazonawsDynamodbTypes.TransactWriteItemsOutput)
	output = m_Wrappers.Companion_Result_.Create_Success_(_5_transactWriteItemsResponse)
	return output
}
func (_static *CompanionStruct_Default___) WriteNewBranchKeyVersionToKeystore(versionBranchKeyItem _dafny.Map, activeBranchKeyItem _dafny.Map, tableName _dafny.Sequence, ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsDynamodbTypes.Companion_TransactWriteItemsOutput_.Default())
	_ = output
	var _0_items _dafny.Sequence
	_ = _0_items
	_0_items = _dafny.SeqOf(Companion_Default___.CreateTransactWritePutItem(versionBranchKeyItem, tableName, Companion_ConditionExpression_.Create_BRANCH__KEY__NOT__EXIST_()), Companion_Default___.CreateTransactWritePutItem(activeBranchKeyItem, tableName, Companion_ConditionExpression_.Create_BRANCH__KEY__EXISTS_()))
	var _1_transactRequest m_ComAmazonawsDynamodbTypes.TransactWriteItemsInput
	_ = _1_transactRequest
	_1_transactRequest = m_ComAmazonawsDynamodbTypes.Companion_TransactWriteItemsInput_.Create_TransactWriteItemsInput_(_0_items, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _2_maybeTransactWriteResponse m_Wrappers.Result
	_ = _2_maybeTransactWriteResponse
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (ddbClient).TransactWriteItems(_1_transactRequest)
	_2_maybeTransactWriteResponse = _out0
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsDynamodbTypes.Companion_TransactWriteItemsOutput_.Default())
	_ = _3_valueOrError0
	_3_valueOrError0 = (_2_maybeTransactWriteResponse).MapFailure(func(coer15 func(m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg15 interface{}) interface{} {
			return coer15(arg15.(m_ComAmazonawsDynamodbTypes.Error))
		}
	}(func(_4_e m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsDynamodb_(_4_e)
	}))
	if (_3_valueOrError0).IsFailure() {
		output = (_3_valueOrError0).PropagateFailure()
		return output
	}
	var _5_transactWriteItemsResponse m_ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
	_ = _5_transactWriteItemsResponse
	_5_transactWriteItemsResponse = (_3_valueOrError0).Extract().(m_ComAmazonawsDynamodbTypes.TransactWriteItemsOutput)
	output = m_Wrappers.Companion_Result_.Create_Success_(_5_transactWriteItemsResponse)
	return output
}
func (_static *CompanionStruct_Default___) GetActiveBranchKeyItem(branchKeyIdentifier _dafny.Sequence, tableName _dafny.Sequence, ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_dynamoDbKey _dafny.Map
	_ = _0_dynamoDbKey
	_0_dynamoDbKey = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(branchKeyIdentifier)).UpdateUnsafe(m_Structure.Companion_Default___.TYPE__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(m_Structure.Companion_Default___.BRANCH__KEY__ACTIVE__TYPE()))
	var _1_ItemRequest m_ComAmazonawsDynamodbTypes.GetItemInput
	_ = _1_ItemRequest
	_1_ItemRequest = m_ComAmazonawsDynamodbTypes.Companion_GetItemInput_.Create_GetItemInput_(tableName, _0_dynamoDbKey, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _2_maybeGetItem m_Wrappers.Result
	_ = _2_maybeGetItem
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (ddbClient).GetItem(_1_ItemRequest)
	_2_maybeGetItem = _out0
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsDynamodbTypes.Companion_GetItemOutput_.Default())
	_ = _3_valueOrError0
	_3_valueOrError0 = (_2_maybeGetItem).MapFailure(func(coer16 func(m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg16 interface{}) interface{} {
			return coer16(arg16.(m_ComAmazonawsDynamodbTypes.Error))
		}
	}(func(_4_e m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsDynamodb_(_4_e)
	}))
	if (_3_valueOrError0).IsFailure() {
		output = (_3_valueOrError0).PropagateFailure()
		return output
	}
	var _5_getItemResponse m_ComAmazonawsDynamodbTypes.GetItemOutput
	_ = _5_getItemResponse
	_5_getItemResponse = (_3_valueOrError0).Extract().(m_ComAmazonawsDynamodbTypes.GetItemOutput)
	var _6_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _6_valueOrError1
	_6_valueOrError1 = m_Wrappers.Companion_Default___.Need((((_5_getItemResponse).Dtor_Item()).Is_Some()) && (((((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map)).Cardinality()).Cmp(_dafny.One) >= 0), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.NO__CORRESPONDING__BRANCH__KEY()))
	if (_6_valueOrError1).IsFailure() {
		output = (_6_valueOrError1).PropagateFailure()
		return output
	}
	var _7_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _7_valueOrError2
	_7_valueOrError2 = m_Wrappers.Companion_Default___.Need((m_Structure.Companion_Default___.ActiveBranchKeyItem_q(((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map))) && (_dafny.Companion_Sequence_.Equal(((((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map)).Get(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Dtor_S(), branchKeyIdentifier)), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Item found is not a valid active branch key.")))
	if (_7_valueOrError2).IsFailure() {
		output = (_7_valueOrError2).PropagateFailure()
		return output
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map))
	return output
}
func (_static *CompanionStruct_Default___) GetVersionBranchKeyItem(branchKeyIdentifier _dafny.Sequence, branchKeyVersion _dafny.Sequence, tableName _dafny.Sequence, ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_dynamoDbKey _dafny.Map
	_ = _0_dynamoDbKey
	_0_dynamoDbKey = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(branchKeyIdentifier)).UpdateUnsafe(m_Structure.Companion_Default___.TYPE__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.Companion_Sequence_.Concatenate(m_Structure.Companion_Default___.BRANCH__KEY__TYPE__PREFIX(), branchKeyVersion)))
	var _1_ItemRequest m_ComAmazonawsDynamodbTypes.GetItemInput
	_ = _1_ItemRequest
	_1_ItemRequest = m_ComAmazonawsDynamodbTypes.Companion_GetItemInput_.Create_GetItemInput_(tableName, _0_dynamoDbKey, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _2_maybeGetItem m_Wrappers.Result
	_ = _2_maybeGetItem
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (ddbClient).GetItem(_1_ItemRequest)
	_2_maybeGetItem = _out0
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsDynamodbTypes.Companion_GetItemOutput_.Default())
	_ = _3_valueOrError0
	_3_valueOrError0 = (_2_maybeGetItem).MapFailure(func(coer17 func(m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg17 interface{}) interface{} {
			return coer17(arg17.(m_ComAmazonawsDynamodbTypes.Error))
		}
	}(func(_4_e m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsDynamodb_(_4_e)
	}))
	if (_3_valueOrError0).IsFailure() {
		output = (_3_valueOrError0).PropagateFailure()
		return output
	}
	var _5_getItemResponse m_ComAmazonawsDynamodbTypes.GetItemOutput
	_ = _5_getItemResponse
	_5_getItemResponse = (_3_valueOrError0).Extract().(m_ComAmazonawsDynamodbTypes.GetItemOutput)
	var _6_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _6_valueOrError1
	_6_valueOrError1 = m_Wrappers.Companion_Default___.Need((((_5_getItemResponse).Dtor_Item()).Is_Some()) && (((((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map)).Cardinality()).Cmp(_dafny.One) >= 0), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.NO__CORRESPONDING__BRANCH__KEY()))
	if (_6_valueOrError1).IsFailure() {
		output = (_6_valueOrError1).PropagateFailure()
		return output
	}
	var _7_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _7_valueOrError2
	_7_valueOrError2 = m_Wrappers.Companion_Default___.Need(((m_Structure.Companion_Default___.VersionBranchKeyItem_q(((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map))) && (_dafny.Companion_Sequence_.Equal(((((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map)).Get(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Dtor_S(), branchKeyIdentifier))) && (_dafny.Companion_Sequence_.Equal(((((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map)).Get(m_Structure.Companion_Default___.TYPE__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Dtor_S(), _dafny.Companion_Sequence_.Concatenate(m_Structure.Companion_Default___.BRANCH__KEY__TYPE__PREFIX(), branchKeyVersion))), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Item found is not a valid branch key version.")))
	if (_7_valueOrError2).IsFailure() {
		output = (_7_valueOrError2).PropagateFailure()
		return output
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map))
	return output
}
func (_static *CompanionStruct_Default___) GetBeaconKeyItem(branchKeyIdentifier _dafny.Sequence, tableName _dafny.Sequence, ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_dynamoDbKey _dafny.Map
	_ = _0_dynamoDbKey
	_0_dynamoDbKey = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(branchKeyIdentifier)).UpdateUnsafe(m_Structure.Companion_Default___.TYPE__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(m_Structure.Companion_Default___.BEACON__KEY__TYPE__VALUE()))
	var _1_ItemRequest m_ComAmazonawsDynamodbTypes.GetItemInput
	_ = _1_ItemRequest
	_1_ItemRequest = m_ComAmazonawsDynamodbTypes.Companion_GetItemInput_.Create_GetItemInput_(tableName, _0_dynamoDbKey, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _2_maybeGetItem m_Wrappers.Result
	_ = _2_maybeGetItem
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (ddbClient).GetItem(_1_ItemRequest)
	_2_maybeGetItem = _out0
	var _3_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_ComAmazonawsDynamodbTypes.Companion_GetItemOutput_.Default())
	_ = _3_valueOrError0
	_3_valueOrError0 = (_2_maybeGetItem).MapFailure(func(coer18 func(m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error) func(interface{}) interface{} {
		return func(arg18 interface{}) interface{} {
			return coer18(arg18.(m_ComAmazonawsDynamodbTypes.Error))
		}
	}(func(_4_e m_ComAmazonawsDynamodbTypes.Error) m_AwsCryptographyKeyStoreTypes.Error {
		return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsDynamodb_(_4_e)
	}))
	if (_3_valueOrError0).IsFailure() {
		output = (_3_valueOrError0).PropagateFailure()
		return output
	}
	var _5_getItemResponse m_ComAmazonawsDynamodbTypes.GetItemOutput
	_ = _5_getItemResponse
	_5_getItemResponse = (_3_valueOrError0).Extract().(m_ComAmazonawsDynamodbTypes.GetItemOutput)
	var _6_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _6_valueOrError1
	_6_valueOrError1 = m_Wrappers.Companion_Default___.Need((((_5_getItemResponse).Dtor_Item()).Is_Some()) && (((((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map)).Cardinality()).Cmp(_dafny.One) >= 0), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(m_KeyStoreErrorMessages.Companion_Default___.NO__CORRESPONDING__BRANCH__KEY()))
	if (_6_valueOrError1).IsFailure() {
		output = (_6_valueOrError1).PropagateFailure()
		return output
	}
	var _7_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _7_valueOrError2
	_7_valueOrError2 = m_Wrappers.Companion_Default___.Need((m_Structure.Companion_Default___.BeaconKeyItem_q(((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map))) && (_dafny.Companion_Sequence_.Equal(((((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map)).Get(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD()).(m_ComAmazonawsDynamodbTypes.AttributeValue)).Dtor_S(), branchKeyIdentifier)), m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(_dafny.SeqOfString("Item found is not a valid beacon key.")))
	if (_7_valueOrError2).IsFailure() {
		output = (_7_valueOrError2).PropagateFailure()
		return output
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(((_5_getItemResponse).Dtor_Item()).Dtor_value().(_dafny.Map))
	return output
}
func (_static *CompanionStruct_Default___) CreateTransactWritePutItem(item _dafny.Map, tableName _dafny.Sequence, conditionExpression ConditionExpression) m_ComAmazonawsDynamodbTypes.TransactWriteItem {
	return m_ComAmazonawsDynamodbTypes.Companion_TransactWriteItem_.Create_TransactWriteItem_(m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_ComAmazonawsDynamodbTypes.Companion_Put_.Create_Put_(item, tableName, m_Wrappers.Companion_Option_.Create_Some_(func() _dafny.Sequence {
		var _source0 ConditionExpression = conditionExpression
		_ = _source0
		{
			if _source0.Is_BRANCH__KEY__NOT__EXIST() {
				return Companion_Default___.BRANCH__KEY__NOT__EXIST__CONDITION()
			}
		}
		{
			return Companion_Default___.BRANCH__KEY__EXISTS__CONDITION()
		}
	}()), m_Wrappers.Companion_Option_.Create_Some_(Companion_Default___.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES()), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
}
func (_static *CompanionStruct_Default___) BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME() _dafny.Sequence {
	return _dafny.SeqOfString("#BranchKeyIdentifierField")
}
func (_static *CompanionStruct_Default___) BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(Companion_Default___.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME(), m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD())
}
func (_static *CompanionStruct_Default___) BRANCH__KEY__NOT__EXIST__CONDITION() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("attribute_not_exists("), Companion_Default___.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME()), _dafny.SeqOfString(")"))
}
func (_static *CompanionStruct_Default___) BRANCH__KEY__EXISTS__CONDITION() _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("attribute_exists("), Companion_Default___.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME()), _dafny.SeqOfString(")"))
}

// End of class Default__

// Definition of datatype ConditionExpression
type ConditionExpression struct {
	Data_ConditionExpression_
}

func (_this ConditionExpression) Get_() Data_ConditionExpression_ {
	return _this.Data_ConditionExpression_
}

type Data_ConditionExpression_ interface {
	isConditionExpression()
}

type CompanionStruct_ConditionExpression_ struct {
}

var Companion_ConditionExpression_ = CompanionStruct_ConditionExpression_{}

type ConditionExpression_BRANCH__KEY__NOT__EXIST struct {
}

func (ConditionExpression_BRANCH__KEY__NOT__EXIST) isConditionExpression() {}

func (CompanionStruct_ConditionExpression_) Create_BRANCH__KEY__NOT__EXIST_() ConditionExpression {
	return ConditionExpression{ConditionExpression_BRANCH__KEY__NOT__EXIST{}}
}

func (_this ConditionExpression) Is_BRANCH__KEY__NOT__EXIST() bool {
	_, ok := _this.Get_().(ConditionExpression_BRANCH__KEY__NOT__EXIST)
	return ok
}

type ConditionExpression_BRANCH__KEY__EXISTS struct {
}

func (ConditionExpression_BRANCH__KEY__EXISTS) isConditionExpression() {}

func (CompanionStruct_ConditionExpression_) Create_BRANCH__KEY__EXISTS_() ConditionExpression {
	return ConditionExpression{ConditionExpression_BRANCH__KEY__EXISTS{}}
}

func (_this ConditionExpression) Is_BRANCH__KEY__EXISTS() bool {
	_, ok := _this.Get_().(ConditionExpression_BRANCH__KEY__EXISTS)
	return ok
}

func (CompanionStruct_ConditionExpression_) Default() ConditionExpression {
	return Companion_ConditionExpression_.Create_BRANCH__KEY__NOT__EXIST_()
}

func (_ CompanionStruct_ConditionExpression_) AllSingletonConstructors() _dafny.Iterator {
	i := -1
	return func() (interface{}, bool) {
		i++
		switch i {
		case 0:
			return Companion_ConditionExpression_.Create_BRANCH__KEY__NOT__EXIST_(), true
		case 1:
			return Companion_ConditionExpression_.Create_BRANCH__KEY__EXISTS_(), true
		default:
			return ConditionExpression{}, false
		}
	}
}

func (_this ConditionExpression) String() string {
	switch _this.Get_().(type) {
	case nil:
		return "null"
	case ConditionExpression_BRANCH__KEY__NOT__EXIST:
		{
			return "DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_NOT_EXIST"
		}
	case ConditionExpression_BRANCH__KEY__EXISTS:
		{
			return "DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_EXISTS"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this ConditionExpression) Equals(other ConditionExpression) bool {
	switch _this.Get_().(type) {
	case ConditionExpression_BRANCH__KEY__NOT__EXIST:
		{
			_, ok := other.Get_().(ConditionExpression_BRANCH__KEY__NOT__EXIST)
			return ok
		}
	case ConditionExpression_BRANCH__KEY__EXISTS:
		{
			_, ok := other.Get_().(ConditionExpression_BRANCH__KEY__EXISTS)
			return ok
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this ConditionExpression) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(ConditionExpression)
	return ok && _this.Equals(typed)
}

func Type_ConditionExpression_() _dafny.TypeDescriptor {
	return type_ConditionExpression_{}
}

type type_ConditionExpression_ struct {
}

func (_this type_ConditionExpression_) Default() interface{} {
	return Companion_ConditionExpression_.Default()
}

func (_this type_ConditionExpression_) String() string {
	return "DDBKeystoreOperations.ConditionExpression"
}
func (_this ConditionExpression) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = ConditionExpression{}

// End of datatype ConditionExpression
