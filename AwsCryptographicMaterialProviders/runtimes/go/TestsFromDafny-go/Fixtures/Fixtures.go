// Package Fixtures
// Dafny module Fixtures compiled into Go

package Fixtures

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
	m_AwsCryptographyMaterialProvidersOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersOperations"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsDiscoveryKeyring"
	m_AwsKmsEcdhKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsEcdhKeyring"
	m_AwsKmsHierarchicalKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsHierarchicalKeyring"
	m_AwsKmsKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsKeyring"
	m_AwsKmsMrkAreUnique "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkAreUnique"
	m_AwsKmsMrkDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkDiscoveryKeyring"
	m_AwsKmsMrkKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkKeyring"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsRsaKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsRsaKeyring"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsUtils"
	m_CMM "github.com/aws/aws-cryptographic-material-providers-library/mpl/CMM"
	m_CacheConstants "github.com/aws/aws-cryptographic-material-providers-library/mpl/CacheConstants"
	m_CanonicalEncryptionContext "github.com/aws/aws-cryptographic-material-providers-library/mpl/CanonicalEncryptionContext"
	m_Commitment "github.com/aws/aws-cryptographic-material-providers-library/mpl/Commitment"
	m_Constants "github.com/aws/aws-cryptographic-material-providers-library/mpl/Constants"
	m_CreateKeyStoreTable "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeyStoreTable"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/DDBKeystoreOperations"
	m_DefaultCMM "github.com/aws/aws-cryptographic-material-providers-library/mpl/DefaultCMM"
	m_DefaultClientSupplier "github.com/aws/aws-cryptographic-material-providers-library/mpl/DefaultClientSupplier"
	m_Defaults "github.com/aws/aws-cryptographic-material-providers-library/mpl/Defaults"
	m_DiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/DiscoveryMultiKeyring"
	m_EcdhEdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/EcdhEdkWrapping"
	m_EdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/EdkWrapping"
	m_ErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/ErrorMessages"
	m_GetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/GetKeys"
	m_IntermediateKeyWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/IntermediateKeyWrapping"
	m_KMSKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/KMSKeystoreOperations"
	m_KeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStore"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStoreErrorMessages"
	m_Keyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/Keyring"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/mpl/KmsArn"
	m_LocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/LocalCMC"
	m_MaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/mpl/MaterialProviders"
	m_MaterialWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/MaterialWrapping"
	m_Materials "github.com/aws/aws-cryptographic-material-providers-library/mpl/Materials"
	m_MrkAwareDiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MrkAwareDiscoveryMultiKeyring"
	m_MrkAwareStrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MrkAwareStrictMultiKeyring"
	m_MultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MultiKeyring"
	m_RawAESKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/RawAESKeyring"
	m_RawECDHKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/RawECDHKeyring"
	m_RawRSAKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/RawRSAKeyring"
	m_RequiredEncryptionContextCMM "github.com/aws/aws-cryptographic-material-providers-library/mpl/RequiredEncryptionContextCMM"
	m_StormTracker "github.com/aws/aws-cryptographic-material-providers-library/mpl/StormTracker"
	m_StormTrackingCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/StormTrackingCMC"
	m_StrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/StrictMultiKeyring"
	m_Structure "github.com/aws/aws-cryptographic-material-providers-library/mpl/Structure"
	m_SynchronizedLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/SynchronizedLocalCMC"
	m_Utils "github.com/aws/aws-cryptographic-material-providers-library/mpl/Utils"
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
var _ m_ComAmazonawsDynamodbTypes.Dummy__
var _ m_ComAmazonawsKmsTypes.Dummy__
var _ m_AwsCryptographyKeyStoreTypes.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m_Actions.Dummy__
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
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
var _ m_Base64.Dummy__
var _ m_AlgorithmSuites.Dummy__
var _ m_Materials.Dummy__
var _ m_Keyring.Dummy__
var _ m_MultiKeyring.Dummy__
var _ m_AwsKmsMrkAreUnique.Dummy__
var _ m_Constants.Dummy__
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
var _ m_MaterialWrapping.Dummy__
var _ m_CanonicalEncryptionContext.Dummy__
var _ m_IntermediateKeyWrapping.Dummy__
var _ m_EdkWrapping.Dummy__
var _ m_ErrorMessages.Dummy__
var _ m_AwsKmsKeyring.Dummy__
var _ m_StrictMultiKeyring.Dummy__
var _ m_AwsKmsDiscoveryKeyring.Dummy__
var _ m_DiscoveryMultiKeyring.Dummy__
var _ m_AwsKmsMrkDiscoveryKeyring.Dummy__
var _ m_MrkAwareDiscoveryMultiKeyring.Dummy__
var _ m_AwsKmsMrkKeyring.Dummy__
var _ m_MrkAwareStrictMultiKeyring.Dummy__
var _ m_LocalCMC.Dummy__
var _ m_SynchronizedLocalCMC.Dummy__
var _ m_StormTracker.Dummy__
var _ m_StormTrackingCMC.Dummy__
var _ m_CacheConstants.Dummy__
var _ m_AwsKmsHierarchicalKeyring.Dummy__
var _ m_AwsKmsRsaKeyring.Dummy__
var _ m_EcdhEdkWrapping.Dummy__
var _ m_RawECDHKeyring.Dummy__
var _ m_AwsKmsEcdhKeyring.Dummy__
var _ m_RawAESKeyring.Dummy__
var _ m_RawRSAKeyring.Dummy__
var _ m_CMM.Dummy__
var _ m_Defaults.Dummy__
var _ m_Commitment.Dummy__
var _ m_DefaultCMM.Dummy__
var _ m_DefaultClientSupplier.Dummy__
var _ m_Utils.Dummy__
var _ m_RequiredEncryptionContextCMM.Dummy__
var _ m_AwsCryptographyMaterialProvidersOperations.Dummy__
var _ m_MaterialProviders.Dummy__
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
var _ m_Base64Lemmas.Dummy__

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
	return "Fixtures.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) EncodeEncryptionContext(input _dafny.Map) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptyMap)
	_ = output
	var _0_encodedEncryptionContext _dafny.Set
	_ = _0_encodedEncryptionContext
	_0_encodedEncryptionContext = func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter0 := _dafny.Iterate((input).Keys().Elements()); ; {
			_compr_0, _ok0 := _iter0()
			if !_ok0 {
				break
			}
			var _1_k _dafny.Sequence
			_1_k = interface{}(_compr_0).(_dafny.Sequence)
			if (input).Contains(_1_k) {
				_coll0.Add(_dafny.TupleOf(m_UTF8.Encode(_1_k), m_UTF8.Encode((input).Get(_1_k).(_dafny.Sequence)), _1_k))
			}
		}
		return _coll0.ToSet()
	}()
	var _2_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _2_valueOrError0
	_2_valueOrError0 = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier((_0_encodedEncryptionContext).Elements(), true, func(_forall_var_0 _dafny.Tuple) bool {
		var _3_i _dafny.Tuple
		_3_i = interface{}(_forall_var_0).(_dafny.Tuple)
		return !((_0_encodedEncryptionContext).Contains(_3_i)) || (((((*(_3_i).IndexInt(0)).(m_Wrappers.Result)).Is_Success()) && (((*(_3_i).IndexInt(1)).(m_Wrappers.Result)).Is_Success())) && (func(_pat_let0_0 m_Wrappers.Result) bool {
			return func(_4_encoded m_Wrappers.Result) bool {
				return ((_4_encoded).Is_Success()) && (_dafny.Companion_Sequence_.Equal((*(_3_i).IndexInt(2)).(_dafny.Sequence), (_4_encoded).Dtor_value().(_dafny.Sequence)))
			}(_pat_let0_0)
		}(m_UTF8.Decode(((*(_3_i).IndexInt(0)).(m_Wrappers.Result)).Dtor_value().(_dafny.Sequence)))))
	}), _dafny.SeqOfString("Unable to encode string"))
	if (_2_valueOrError0).IsFailure() {
		output = (_2_valueOrError0).PropagateFailure()
		return output
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(func() _dafny.Map {
		var _coll1 = _dafny.NewMapBuilder()
		_ = _coll1
		for _iter1 := _dafny.Iterate((_0_encodedEncryptionContext).Elements()); ; {
			_compr_1, _ok1 := _iter1()
			if !_ok1 {
				break
			}
			var _5_i _dafny.Tuple
			_5_i = interface{}(_compr_1).(_dafny.Tuple)
			if (_0_encodedEncryptionContext).Contains(_5_i) {
				_coll1.Add(((*(_5_i).IndexInt(0)).(m_Wrappers.Result)).Dtor_value().(_dafny.Sequence), ((*(_5_i).IndexInt(1)).(m_Wrappers.Result)).Dtor_value().(_dafny.Sequence))
			}
		}
		return _coll1.ToMap()
	}())
	return output
}
func (_static *CompanionStruct_Default___) DecodeEncryptionContext(input _dafny.Map) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptyMap)
	_ = output
	var _0_decodedEncryptionContext _dafny.Set
	_ = _0_decodedEncryptionContext
	_0_decodedEncryptionContext = func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter2 := _dafny.Iterate((input).Keys().Elements()); ; {
			_compr_0, _ok2 := _iter2()
			if !_ok2 {
				break
			}
			var _1_k _dafny.Sequence
			_1_k = interface{}(_compr_0).(_dafny.Sequence)
			if (input).Contains(_1_k) {
				_coll0.Add(_dafny.TupleOf(m_UTF8.Decode(_1_k), m_UTF8.Decode((input).Get(_1_k).(_dafny.Sequence)), _1_k))
			}
		}
		return _coll0.ToSet()
	}()
	var _2_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _2_valueOrError0
	_2_valueOrError0 = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier((_0_decodedEncryptionContext).Elements(), true, func(_forall_var_0 _dafny.Tuple) bool {
		var _3_i _dafny.Tuple
		_3_i = interface{}(_forall_var_0).(_dafny.Tuple)
		return !((_0_decodedEncryptionContext).Contains(_3_i)) || (((((*(_3_i).IndexInt(0)).(m_Wrappers.Result)).Is_Success()) && (((*(_3_i).IndexInt(1)).(m_Wrappers.Result)).Is_Success())) && (func(_pat_let1_0 m_Wrappers.Result) bool {
			return func(_4_decoded m_Wrappers.Result) bool {
				return ((_4_decoded).Is_Success()) && (_dafny.Companion_Sequence_.Equal((*(_3_i).IndexInt(2)).(_dafny.Sequence), (_4_decoded).Dtor_value().(_dafny.Sequence)))
			}(_pat_let1_0)
		}(m_UTF8.Encode(((*(_3_i).IndexInt(0)).(m_Wrappers.Result)).Dtor_value().(_dafny.Sequence)))))
	}), _dafny.SeqOfString("Unable to decode string"))
	if (_2_valueOrError0).IsFailure() {
		output = (_2_valueOrError0).PropagateFailure()
		return output
	}
	output = m_Wrappers.Companion_Result_.Create_Success_(func() _dafny.Map {
		var _coll1 = _dafny.NewMapBuilder()
		_ = _coll1
		for _iter3 := _dafny.Iterate((_0_decodedEncryptionContext).Elements()); ; {
			_compr_1, _ok3 := _iter3()
			if !_ok3 {
				break
			}
			var _5_i _dafny.Tuple
			_5_i = interface{}(_compr_1).(_dafny.Tuple)
			if (_0_decodedEncryptionContext).Contains(_5_i) {
				_coll1.Add(((*(_5_i).IndexInt(0)).(m_Wrappers.Result)).Dtor_value().(_dafny.Sequence), ((*(_5_i).IndexInt(1)).(m_Wrappers.Result)).Dtor_value().(_dafny.Sequence))
			}
		}
		return _coll1.ToMap()
	}())
	return output
}
func (_static *CompanionStruct_Default___) BranchKeyStoreName() _dafny.Sequence {
	return _dafny.SeqOfString("KeyStoreDdbTable")
}
func (_static *CompanionStruct_Default___) LogicalKeyStoreName() _dafny.Sequence {
	return Companion_Default___.BranchKeyStoreName()
}
func (_static *CompanionStruct_Default___) MrkArnEast() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-east-1:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7")
}
func (_static *CompanionStruct_Default___) KmsConfigEast() m_AwsCryptographyKeyStoreTypes.KMSConfiguration {
	return m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.MrkArnEast())
}
func (_static *CompanionStruct_Default___) MrkArnWest() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7")
}
func (_static *CompanionStruct_Default___) KmsConfigWest() m_AwsCryptographyKeyStoreTypes.KMSConfiguration {
	return m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.MrkArnWest())
}
func (_static *CompanionStruct_Default___) KmsMrkConfigEast() m_AwsCryptographyKeyStoreTypes.KMSConfiguration {
	return m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsMRKeyArn_(Companion_Default___.MrkArnEast())
}
func (_static *CompanionStruct_Default___) KmsMrkConfigWest() m_AwsCryptographyKeyStoreTypes.KMSConfiguration {
	return m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsMRKeyArn_(Companion_Default___.MrkArnWest())
}
func (_static *CompanionStruct_Default___) KmsSrkConfigEast() m_AwsCryptographyKeyStoreTypes.KMSConfiguration {
	return m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.MrkArnEast())
}
func (_static *CompanionStruct_Default___) KmsSrkConfigWest() m_AwsCryptographyKeyStoreTypes.KMSConfiguration {
	return m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsKeyArn_(Companion_Default___.MrkArnWest())
}
func (_static *CompanionStruct_Default___) MrkArnAP() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:ap-south-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7")
}
func (_static *CompanionStruct_Default___) KmsMrkConfigAP() m_AwsCryptographyKeyStoreTypes.KMSConfiguration {
	return m_AwsCryptographyKeyStoreTypes.Companion_KMSConfiguration_.Create_kmsMRKeyArn_(Companion_Default___.MrkArnAP())
}
func (_static *CompanionStruct_Default___) BranchKeyId() _dafny.Sequence {
	return _dafny.SeqOfString("75789115-1deb-4fe3-a2ec-be9e885d1945")
}
func (_static *CompanionStruct_Default___) BranchKeyIdActiveVersion() _dafny.Sequence {
	return _dafny.SeqOfString("fed7ad33-0774-4f97-aa5e-6c766fc8af9f")
}
func (_static *CompanionStruct_Default___) BranchKeyIdWithEC() _dafny.Sequence {
	return _dafny.SeqOfString("4bb57643-07c1-419e-92ad-0df0df149d7c")
}
func (_static *CompanionStruct_Default___) BranchKeyIdActiveVersionUtf8Bytes() _dafny.Sequence {
	return _dafny.SeqOf(uint8(102), uint8(101), uint8(100), uint8(55), uint8(97), uint8(100), uint8(51), uint8(51), uint8(45), uint8(48), uint8(55), uint8(55), uint8(52), uint8(45), uint8(52), uint8(102), uint8(57), uint8(55), uint8(45), uint8(97), uint8(97), uint8(53), uint8(101), uint8(45), uint8(54), uint8(99), uint8(55), uint8(54), uint8(54), uint8(102), uint8(99), uint8(56), uint8(97), uint8(102), uint8(57), uint8(102))
}
func (_static *CompanionStruct_Default___) KeyArn() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126")
}
func (_static *CompanionStruct_Default___) KeyId() _dafny.Sequence {
	return _dafny.SeqOfString("9d989aa2-2f9c-438c-a745-cc57d3ad0126")
}
func (_static *CompanionStruct_Default___) MrkRsaKeyArn() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297")
}
func (_static *CompanionStruct_Default___) KmsMrkEC() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("abc")), m_UTF8.Companion_Default___.EncodeAscii(_dafny.SeqOfString("123")))
}
func (_static *CompanionStruct_Default___) EastBranchKey() _dafny.Sequence {
	return _dafny.SeqOfString("MyEastBranch2")
}
func (_static *CompanionStruct_Default___) WestBranchKey() _dafny.Sequence {
	return _dafny.SeqOfString("MyWestBranch2")
}
func (_static *CompanionStruct_Default___) PublicKeyArn() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
}
func (_static *CompanionStruct_Default___) PostalHornKeyArn() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8")
}
func (_static *CompanionStruct_Default___) KmsKeyAlias() _dafny.Sequence {
	return _dafny.SeqOfString("arn:aws:kms:us-west-2:370957321024:alias/postalHorn")
}
func (_static *CompanionStruct_Default___) PostalHornBranchKeyId() _dafny.Sequence {
	return _dafny.SeqOfString("682dfba7-4c35-491d-8d6a-5a9c56194061")
}
func (_static *CompanionStruct_Default___) PostalHornBranchKeyActiveVersion() _dafny.Sequence {
	return _dafny.SeqOfString("6b7a8ef4-8c1c-4f63-b196-a6ef7e496e50")
}
func (_static *CompanionStruct_Default___) LyingBranchKeyId() _dafny.Sequence {
	return _dafny.SeqOfString("kms-arn-attribute-is-lying")
}
func (_static *CompanionStruct_Default___) LyingBranchKeyDecryptOnlyVersion() _dafny.Sequence {
	return _dafny.SeqOfString("129c5c87-308a-41c9-8b9d-a27f66e915f4")
}

// End of class Default__