// Package CreateKeyStoreTable
// Dafny module CreateKeyStoreTable compiled into Go

package CreateKeyStoreTable

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/ComAmazonawsDynamodbTypes"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/kms/ComAmazonawsKmsTypes"
	m_AwsArnParsing "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsArnParsing"
	m_AwsCryptographyKeyStoreTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyKeyStoreTypes"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsUtils"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/DDBKeystoreOperations"
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
var _ m_DDBKeystoreOperations.Dummy__
var _ m_CreateKeys.Dummy__

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
	return "CreateKeyStoreTable.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) KeyStoreHasExpectedConstruction_q(t m_ComAmazonawsDynamodbTypes.TableDescription) bool {
	return (((((((t).Dtor_AttributeDefinitions()).Is_Some()) && (((t).Dtor_KeySchema()).Is_Some())) && (((t).Dtor_TableName()).Is_Some())) && (((t).Dtor_TableArn()).Is_Some())) && ((m_Seq.Companion_Default___.ToSet(Companion_Default___.ATTRIBUTE__DEFINITIONS())).IsSubsetOf(m_Seq.Companion_Default___.ToSet(((t).Dtor_AttributeDefinitions()).Dtor_value().(_dafny.Sequence))))) && ((m_Seq.Companion_Default___.ToSet(Companion_Default___.KEY__SCHEMA())).IsSubsetOf(m_Seq.Companion_Default___.ToSet(((t).Dtor_KeySchema()).Dtor_value().(_dafny.Sequence))))
}
func (_static *CompanionStruct_Default___) CreateKeyStoreTable(tableName _dafny.Sequence, ddbClient m_ComAmazonawsDynamodbTypes.IDynamoDBClient) m_Wrappers.Result {
	var res m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = res
	var _0_maybeDescribeTableResponse m_Wrappers.Result
	_ = _0_maybeDescribeTableResponse
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = (ddbClient).DescribeTable(m_ComAmazonawsDynamodbTypes.Companion_DescribeTableInput_.Create_DescribeTableInput_(tableName))
	_0_maybeDescribeTableResponse = _out0
	if (_0_maybeDescribeTableResponse).Is_Failure() {
		var _1_error m_ComAmazonawsDynamodbTypes.Error
		_ = _1_error
		_1_error = (_0_maybeDescribeTableResponse).Dtor_error().(m_ComAmazonawsDynamodbTypes.Error)
		if (_1_error).Is_ResourceNotFoundException() {
			var _2_maybeCreateTableResponse m_Wrappers.Result
			_ = _2_maybeCreateTableResponse
			var _out1 m_Wrappers.Result
			_ = _out1
			_out1 = (ddbClient).CreateTable(m_ComAmazonawsDynamodbTypes.Companion_CreateTableInput_.Create_CreateTableInput_(Companion_Default___.ATTRIBUTE__DEFINITIONS(), tableName, Companion_Default___.KEY__SCHEMA(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(m_ComAmazonawsDynamodbTypes.Companion_BillingMode_.Create_PAY__PER__REQUEST_()), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
			_2_maybeCreateTableResponse = _out1
			if (_2_maybeCreateTableResponse).Is_Failure() {
				res = m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsDynamodb_((_2_maybeCreateTableResponse).Dtor_error().(m_ComAmazonawsDynamodbTypes.Error)))
			} else {
				var _3_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
				_ = _3_valueOrError0
				_3_valueOrError0 = m_Wrappers.Companion_Default___.Need(((((_2_maybeCreateTableResponse).Dtor_value().(m_ComAmazonawsDynamodbTypes.CreateTableOutput)).Dtor_TableDescription()).Is_Some()) && (Companion_Default___.KeyStoreHasExpectedConstruction_q((((_2_maybeCreateTableResponse).Dtor_value().(m_ComAmazonawsDynamodbTypes.CreateTableOutput)).Dtor_TableDescription()).Dtor_value().(m_ComAmazonawsDynamodbTypes.TableDescription))), Companion_Default___.E(_dafny.SeqOfString("Configured table name does not conform to expected Key Store construction.")))
				if (_3_valueOrError0).IsFailure() {
					res = (_3_valueOrError0).PropagateFailure()
					return res
				}
				res = m_Wrappers.Companion_Result_.Create_Success_((((((_2_maybeCreateTableResponse).Dtor_value().(m_ComAmazonawsDynamodbTypes.CreateTableOutput)).Dtor_TableDescription()).Dtor_value().(m_ComAmazonawsDynamodbTypes.TableDescription)).Dtor_TableArn()).Dtor_value().(_dafny.Sequence))
			}
		} else {
			res = m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_ComAmazonawsDynamodb_(_1_error))
		}
	} else {
		var _4_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
		_ = _4_valueOrError1
		_4_valueOrError1 = m_Wrappers.Companion_Default___.Need(((((_0_maybeDescribeTableResponse).Dtor_value().(m_ComAmazonawsDynamodbTypes.DescribeTableOutput)).Dtor_Table()).Is_Some()) && (Companion_Default___.KeyStoreHasExpectedConstruction_q((((_0_maybeDescribeTableResponse).Dtor_value().(m_ComAmazonawsDynamodbTypes.DescribeTableOutput)).Dtor_Table()).Dtor_value().(m_ComAmazonawsDynamodbTypes.TableDescription))), Companion_Default___.E(_dafny.SeqOfString("Configured table name does not conform to expected Key Store construction.")))
		if (_4_valueOrError1).IsFailure() {
			res = (_4_valueOrError1).PropagateFailure()
			return res
		}
		res = m_Wrappers.Companion_Result_.Create_Success_((((((_0_maybeDescribeTableResponse).Dtor_value().(m_ComAmazonawsDynamodbTypes.DescribeTableOutput)).Dtor_Table()).Dtor_value().(m_ComAmazonawsDynamodbTypes.TableDescription)).Dtor_TableArn()).Dtor_value().(_dafny.Sequence))
	}
	return res
}
func (_static *CompanionStruct_Default___) E(s _dafny.Sequence) m_AwsCryptographyKeyStoreTypes.Error {
	return m_AwsCryptographyKeyStoreTypes.Companion_Error_.Create_KeyStoreException_(s)
}
func (_static *CompanionStruct_Default___) ATTRIBUTE__DEFINITIONS() _dafny.Sequence {
	return _dafny.SeqOf(m_ComAmazonawsDynamodbTypes.Companion_AttributeDefinition_.Create_AttributeDefinition_(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_ScalarAttributeType_.Create_S_()), m_ComAmazonawsDynamodbTypes.Companion_AttributeDefinition_.Create_AttributeDefinition_(m_Structure.Companion_Default___.TYPE__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_ScalarAttributeType_.Create_S_()))
}
func (_static *CompanionStruct_Default___) KEY__SCHEMA() _dafny.Sequence {
	return _dafny.SeqOf(m_ComAmazonawsDynamodbTypes.Companion_KeySchemaElement_.Create_KeySchemaElement_(m_Structure.Companion_Default___.BRANCH__KEY__IDENTIFIER__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_KeyType_.Create_HASH_()), m_ComAmazonawsDynamodbTypes.Companion_KeySchemaElement_.Create_KeySchemaElement_(m_Structure.Companion_Default___.TYPE__FIELD(), m_ComAmazonawsDynamodbTypes.Companion_KeyType_.Create_RANGE_()))
}

// End of class Default__

// Definition of class KeyStoreDescription
type KeyStoreDescription struct {
}

func New_KeyStoreDescription_() *KeyStoreDescription {
	_this := KeyStoreDescription{}

	return &_this
}

type CompanionStruct_KeyStoreDescription_ struct {
}

var Companion_KeyStoreDescription_ = CompanionStruct_KeyStoreDescription_{}

func (*KeyStoreDescription) String() string {
	return "CreateKeyStoreTable.KeyStoreDescription"
}

// End of class KeyStoreDescription

func Type_KeyStoreDescription_() _dafny.TypeDescriptor {
	return type_KeyStoreDescription_{}
}

type type_KeyStoreDescription_ struct {
}

func (_this type_KeyStoreDescription_) Default() interface{} {
	return m_ComAmazonawsDynamodbTypes.Companion_TableDescription_.Default()
}

func (_this type_KeyStoreDescription_) String() string {
	return "CreateKeyStoreTable.KeyStoreDescription"
}
func (_this *CompanionStruct_KeyStoreDescription_) Is_(__source m_ComAmazonawsDynamodbTypes.TableDescription) bool {
	var _0_t m_ComAmazonawsDynamodbTypes.TableDescription = (__source)
	_ = _0_t
	return Companion_Default___.KeyStoreHasExpectedConstruction_q(_0_t)
}
