// Package AwsKmsMrkAreUnique
// Dafny module AwsKmsMrkAreUnique compiled into Go

package AwsKmsMrkAreUnique

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
	return "AwsKmsMrkAreUnique.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) AwsKmsMrkAreUnique(identifiers _dafny.Sequence) m_Wrappers.Outcome {
	var _0_mrks _dafny.Sequence = m_Seq.Companion_Default___.Filter(func(coer32 func(m_AwsArnParsing.AwsKmsIdentifier) bool) func(interface{}) bool {
		return func(arg32 interface{}) bool {
			return coer32(arg32.(m_AwsArnParsing.AwsKmsIdentifier))
		}
	}(m_AwsArnParsing.Companion_Default___.IsMultiRegionAwsKmsIdentifier), identifiers)
	_ = _0_mrks
	if (_dafny.IntOfUint32((_0_mrks).Cardinality())).Sign() == 0 {
		return m_Wrappers.Companion_Outcome_.Create_Pass_()
	} else {
		var _1_mrkKeyIds _dafny.Sequence = m_Seq.Companion_Default___.Map(func(coer33 func(m_AwsArnParsing.AwsKmsIdentifier) _dafny.Sequence) func(interface{}) interface{} {
			return func(arg33 interface{}) interface{} {
				return coer33(arg33.(m_AwsArnParsing.AwsKmsIdentifier))
			}
		}(Companion_Default___.GetKeyId), _0_mrks)
		_ = _1_mrkKeyIds
		var _2_setMrks _dafny.Set = m_Seq.Companion_Default___.ToSet(_1_mrkKeyIds)
		_ = _2_setMrks
		if (_dafny.IntOfUint32((_1_mrkKeyIds).Cardinality())).Cmp((_2_setMrks).Cardinality()) == 0 {
			return m_Wrappers.Companion_Outcome_.Create_Pass_()
		} else {
			var _3_duplicateMrkIds _dafny.Set = func() _dafny.Set {
				var _coll0 = _dafny.NewBuilder()
				_ = _coll0
				for _iter9 := _dafny.Iterate((_1_mrkKeyIds).Elements()); ; {
					_compr_0, _ok9 := _iter9()
					if !_ok9 {
						break
					}
					var _4_x _dafny.Sequence
					_4_x = interface{}(_compr_0).(_dafny.Sequence)
					if (_dafny.Companion_Sequence_.Contains(_1_mrkKeyIds, _4_x)) && (((_dafny.MultiSetFromSeq(_1_mrkKeyIds)).Multiplicity(_4_x)).Cmp(_dafny.One) >= 0) {
						_coll0.Add(_4_x)
					}
				}
				return _coll0.ToSet()
			}()
			_ = _3_duplicateMrkIds
			var _5_isDuplicate func(m_AwsArnParsing.AwsKmsIdentifier) bool = (func(_6_duplicateMrkIds _dafny.Set) func(m_AwsArnParsing.AwsKmsIdentifier) bool {
				return func(_7_identifier m_AwsArnParsing.AwsKmsIdentifier) bool {
					return (_6_duplicateMrkIds).Contains(Companion_Default___.GetKeyId(_7_identifier))
				}
			})(_3_duplicateMrkIds)
			_ = _5_isDuplicate
			var _8_identifierToString func(m_AwsArnParsing.AwsKmsIdentifier) _dafny.Sequence = func(_9_i m_AwsArnParsing.AwsKmsIdentifier) _dafny.Sequence {
				return (_9_i).ToString()
			}
			_ = _8_identifierToString
			var _10_duplicateIdentifiers _dafny.Sequence = m_Seq.Companion_Default___.Filter(func(coer34 func(m_AwsArnParsing.AwsKmsIdentifier) bool) func(interface{}) bool {
				return func(arg34 interface{}) bool {
					return coer34(arg34.(m_AwsArnParsing.AwsKmsIdentifier))
				}
			}(_5_isDuplicate), identifiers)
			_ = _10_duplicateIdentifiers
			var _11_duplicates _dafny.Sequence = m_Seq.Companion_Default___.Map(func(coer35 func(m_AwsArnParsing.AwsKmsIdentifier) _dafny.Sequence) func(interface{}) interface{} {
				return func(arg35 interface{}) interface{} {
					return coer35(arg35.(m_AwsArnParsing.AwsKmsIdentifier))
				}
			}(_8_identifierToString), _10_duplicateIdentifiers)
			_ = _11_duplicates
			if (_dafny.IntOfUint32((_11_duplicates).Cardinality())).Sign() == 0 {
				return m_Wrappers.Companion_Outcome_.Create_Fail_(m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Impossible")))
			} else {
				return m_Wrappers.Companion_Outcome_.Create_Fail_(m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Related multi-Region keys: "), m_StandardLibrary.Companion_Default___.Join(_11_duplicates, _dafny.SeqOfString(","))), _dafny.SeqOfString("are not allowed."))))
			}
		}
	}
}
func (_static *CompanionStruct_Default___) GetKeyId(identifier m_AwsArnParsing.AwsKmsIdentifier) _dafny.Sequence {
	var _source0 m_AwsArnParsing.AwsKmsIdentifier = identifier
	_ = _source0
	{
		if _source0.Is_AwsKmsArnIdentifier() {
			var _0_a m_AwsArnParsing.AwsArn = _source0.Get_().(m_AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier).A
			_ = _0_a
			return ((_0_a).Dtor_resource()).Dtor_value()
		}
	}
	{
		var _1_i m_AwsArnParsing.AwsResource = _source0.Get_().(m_AwsArnParsing.AwsKmsIdentifier_AwsKmsRawResourceIdentifier).R
		_ = _1_i
		return (_1_i).Dtor_value()
	}
}

// End of class Default__