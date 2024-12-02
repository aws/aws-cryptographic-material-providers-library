// Package EdkWrapping
// Dafny module EdkWrapping compiled into Go

package EdkWrapping

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
	m_CanonicalEncryptionContext "github.com/aws/aws-cryptographic-material-providers-library/mpl/CanonicalEncryptionContext"
	m_Constants "github.com/aws/aws-cryptographic-material-providers-library/mpl/Constants"
	m_CreateKeyStoreTable "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeyStoreTable"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/DDBKeystoreOperations"
	m_GetKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/GetKeys"
	m_IntermediateKeyWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/IntermediateKeyWrapping"
	m_KMSKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/KMSKeystoreOperations"
	m_KeyStore "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStore"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/mpl/KeyStoreErrorMessages"
	m_Keyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/Keyring"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/mpl/KmsArn"
	m_MaterialWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/MaterialWrapping"
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
var _ m_MaterialWrapping.Dummy__
var _ m_CanonicalEncryptionContext.Dummy__
var _ m_IntermediateKeyWrapping.Dummy__

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
	return "EdkWrapping.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) WrapEdkMaterial(encryptionMaterials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials, wrap m_MaterialWrapping.WrapMaterial, generateAndWrap m_MaterialWrapping.GenerateAndWrapMaterial) m_Wrappers.Result {
	var ret m_Wrappers.Result = m_Wrappers.Result{}
	_ = ret
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _0_valueOrError0
	_0_valueOrError0 = m_Wrappers.Companion_Default___.Need(m_Materials.Companion_Default___.ValidEncryptionMaterials(encryptionMaterials), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Invalid materials for encryption.")))
	if (_0_valueOrError0).IsFailure() {
		ret = (_0_valueOrError0).PropagateFailure()
		return ret
	}
	if (((encryptionMaterials).Dtor_plaintextDataKey()).Is_Some()) && ((((encryptionMaterials).Dtor_algorithmSuite()).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING()) {
		var _1_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _1_valueOrError1
		var _out0 interface{}
		_ = _out0
		_out0 = (wrap).Invoke(m_MaterialWrapping.Companion_WrapInput_.Create_WrapInput_(((encryptionMaterials).Dtor_plaintextDataKey()).Dtor_value().(_dafny.Sequence), (encryptionMaterials).Dtor_algorithmSuite(), (encryptionMaterials).Dtor_encryptionContext()))
		_1_valueOrError1 = _out0.(m_Wrappers.Result)
		if (_1_valueOrError1).IsFailure() {
			ret = (_1_valueOrError1).PropagateFailure()
			return ret
		}
		var _2_directOutput m_MaterialWrapping.WrapOutput
		_ = _2_directOutput
		_2_directOutput = (_1_valueOrError1).Extract().(m_MaterialWrapping.WrapOutput)
		ret = m_Wrappers.Companion_Result_.Create_Success_(Companion_WrapEdkMaterialOutput_.Create_WrapOnlyEdkMaterialOutput_((_2_directOutput).Dtor_wrappedMaterial(), m_Wrappers.Companion_Option_.Create_None_(), (_2_directOutput).Dtor_wrapInfo()))
		return ret
	} else if (((encryptionMaterials).Dtor_plaintextDataKey()).Is_Some()) && ((((encryptionMaterials).Dtor_algorithmSuite()).Dtor_edkWrapping()).Is_IntermediateKeyWrapping()) {
		var _3_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _3_valueOrError2
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_IntermediateKeyWrapping.Companion_Default___.IntermediateWrap(generateAndWrap, ((encryptionMaterials).Dtor_plaintextDataKey()).Dtor_value().(_dafny.Sequence), (encryptionMaterials).Dtor_algorithmSuite(), (encryptionMaterials).Dtor_encryptionContext())
		_3_valueOrError2 = _out1
		if (_3_valueOrError2).IsFailure() {
			ret = (_3_valueOrError2).PropagateFailure()
			return ret
		}
		var _4_intermediateOutput m_IntermediateKeyWrapping.IntermediateWrapOutput
		_ = _4_intermediateOutput
		_4_intermediateOutput = (_3_valueOrError2).Extract().(m_IntermediateKeyWrapping.IntermediateWrapOutput)
		ret = m_Wrappers.Companion_Result_.Create_Success_(Companion_WrapEdkMaterialOutput_.Create_WrapOnlyEdkMaterialOutput_((_4_intermediateOutput).Dtor_wrappedMaterial(), m_Wrappers.Companion_Option_.Create_Some_((_4_intermediateOutput).Dtor_symmetricSigningKey()), (_4_intermediateOutput).Dtor_wrapInfo()))
		return ret
	} else if (((encryptionMaterials).Dtor_plaintextDataKey()).Is_None()) && ((((encryptionMaterials).Dtor_algorithmSuite()).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING()) {
		var _5_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _5_valueOrError3
		var _out2 interface{}
		_ = _out2
		_out2 = (generateAndWrap).Invoke(m_MaterialWrapping.Companion_GenerateAndWrapInput_.Create_GenerateAndWrapInput_((encryptionMaterials).Dtor_algorithmSuite(), (encryptionMaterials).Dtor_encryptionContext()))
		_5_valueOrError3 = _out2.(m_Wrappers.Result)
		if (_5_valueOrError3).IsFailure() {
			ret = (_5_valueOrError3).PropagateFailure()
			return ret
		}
		var _6_directOutput m_MaterialWrapping.GenerateAndWrapOutput
		_ = _6_directOutput
		_6_directOutput = (_5_valueOrError3).Extract().(m_MaterialWrapping.GenerateAndWrapOutput)
		ret = m_Wrappers.Companion_Result_.Create_Success_(Companion_WrapEdkMaterialOutput_.Create_GenerateAndWrapEdkMaterialOutput_((_6_directOutput).Dtor_plaintextMaterial(), (_6_directOutput).Dtor_wrappedMaterial(), m_Wrappers.Companion_Option_.Create_None_(), (_6_directOutput).Dtor_wrapInfo()))
		return ret
	} else if (((encryptionMaterials).Dtor_plaintextDataKey()).Is_None()) && ((((encryptionMaterials).Dtor_algorithmSuite()).Dtor_edkWrapping()).Is_IntermediateKeyWrapping()) {
		var _7_valueOrError4 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
		_ = _7_valueOrError4
		_7_valueOrError4 = m_Wrappers.Companion_Default___.Need((((encryptionMaterials).Dtor_algorithmSuite()).Dtor_commitment()).Is_HKDF(), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Invalid algorithm suite: suites with intermediate key wrapping must use key commitment.")))
		if (_7_valueOrError4).IsFailure() {
			ret = (_7_valueOrError4).PropagateFailure()
			return ret
		}
		var _8_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _8_valueOrError5
		var _out3 m_Wrappers.Result
		_ = _out3
		_out3 = m_IntermediateKeyWrapping.Companion_Default___.IntermediateGenerateAndWrap(generateAndWrap, (encryptionMaterials).Dtor_algorithmSuite(), (encryptionMaterials).Dtor_encryptionContext())
		_8_valueOrError5 = _out3
		if (_8_valueOrError5).IsFailure() {
			ret = (_8_valueOrError5).PropagateFailure()
			return ret
		}
		var _9_intermediateOutput m_IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput
		_ = _9_intermediateOutput
		_9_intermediateOutput = (_8_valueOrError5).Extract().(m_IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput)
		ret = m_Wrappers.Companion_Result_.Create_Success_(Companion_WrapEdkMaterialOutput_.Create_GenerateAndWrapEdkMaterialOutput_((_9_intermediateOutput).Dtor_plaintextDataKey(), (_9_intermediateOutput).Dtor_wrappedMaterial(), m_Wrappers.Companion_Option_.Create_Some_((_9_intermediateOutput).Dtor_symmetricSigningKey()), (_9_intermediateOutput).Dtor_wrapInfo()))
		return ret
	} else {
	}
	return ret
}
func (_static *CompanionStruct_Default___) UnwrapEdkMaterial(wrappedMaterial _dafny.Sequence, decryptionMaterials m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials, unwrap m_MaterialWrapping.UnwrapMaterial) m_Wrappers.Result {
	var ret m_Wrappers.Result = m_Wrappers.Result{}
	_ = ret
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _0_valueOrError0
	_0_valueOrError0 = m_Wrappers.Companion_Default___.Need(m_Materials.Companion_Default___.ValidDecryptionMaterials(decryptionMaterials), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Invalid materials for decryption.")))
	if (_0_valueOrError0).IsFailure() {
		ret = (_0_valueOrError0).PropagateFailure()
		return ret
	}
	if (((decryptionMaterials).Dtor_algorithmSuite()).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING() {
		var _1_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _1_valueOrError1
		var _out0 interface{}
		_ = _out0
		_out0 = (unwrap).Invoke(m_MaterialWrapping.Companion_UnwrapInput_.Create_UnwrapInput_(wrappedMaterial, (decryptionMaterials).Dtor_algorithmSuite(), (decryptionMaterials).Dtor_encryptionContext()))
		_1_valueOrError1 = _out0.(m_Wrappers.Result)
		if (_1_valueOrError1).IsFailure() {
			ret = (_1_valueOrError1).PropagateFailure()
			return ret
		}
		var _2_directOutput m_MaterialWrapping.UnwrapOutput
		_ = _2_directOutput
		_2_directOutput = (_1_valueOrError1).Extract().(m_MaterialWrapping.UnwrapOutput)
		ret = m_Wrappers.Companion_Result_.Create_Success_(Companion_UnwrapEdkMaterialOutput_.Create_UnwrapEdkMaterialOutput_((_2_directOutput).Dtor_unwrappedMaterial(), m_Wrappers.Companion_Option_.Create_None_(), (_2_directOutput).Dtor_unwrapInfo()))
		return ret
	} else if (((decryptionMaterials).Dtor_algorithmSuite()).Dtor_edkWrapping()).Is_IntermediateKeyWrapping() {
		var _3_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
		_ = _3_valueOrError2
		_3_valueOrError2 = m_Wrappers.Companion_Default___.Need((_dafny.IntOfUint32((wrappedMaterial).Cardinality())).Cmp(_dafny.IntOfInt32((((((decryptionMaterials).Dtor_algorithmSuite()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength())+(((((decryptionMaterials).Dtor_algorithmSuite()).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_tagLength()))) >= 0, m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Invalid material for Intermediate Unwrapping")))
		if (_3_valueOrError2).IsFailure() {
			ret = (_3_valueOrError2).PropagateFailure()
			return ret
		}
		var _4_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
		_ = _4_valueOrError3
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = m_IntermediateKeyWrapping.Companion_Default___.IntermediateUnwrap(unwrap, wrappedMaterial, (decryptionMaterials).Dtor_algorithmSuite(), (decryptionMaterials).Dtor_encryptionContext())
		_4_valueOrError3 = _out1
		if (_4_valueOrError3).IsFailure() {
			ret = (_4_valueOrError3).PropagateFailure()
			return ret
		}
		var _5_intermediateOutput m_IntermediateKeyWrapping.IntermediateUnwrapOutput
		_ = _5_intermediateOutput
		_5_intermediateOutput = (_4_valueOrError3).Extract().(m_IntermediateKeyWrapping.IntermediateUnwrapOutput)
		ret = m_Wrappers.Companion_Result_.Create_Success_(Companion_UnwrapEdkMaterialOutput_.Create_UnwrapEdkMaterialOutput_((_5_intermediateOutput).Dtor_plaintextDataKey(), m_Wrappers.Companion_Option_.Create_Some_((_5_intermediateOutput).Dtor_symmetricSigningKey()), (_5_intermediateOutput).Dtor_unwrapInfo()))
		return ret
	} else {
	}
	return ret
}
func (_static *CompanionStruct_Default___) GetProviderWrappedMaterial(material _dafny.Sequence, algSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) m_Wrappers.Result {
	if ((algSuite).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING() {
		return m_Wrappers.Companion_Result_.Create_Success_(material)
	} else {
		var _0_deserializedWrappedRes m_Wrappers.Result = m_IntermediateKeyWrapping.Companion_Default___.DeserializeIntermediateWrappedMaterial(material, algSuite)
		_ = _0_deserializedWrappedRes
		if (_0_deserializedWrappedRes).Is_Failure() {
			return m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Unable to deserialize Intermediate Key Wrapped material.")))
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_(((_0_deserializedWrappedRes).Dtor_value().(m_IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial)).Dtor_providerWrappedIkm())
		}
	}
}

// End of class Default__

// Definition of datatype WrapEdkMaterialOutput
type WrapEdkMaterialOutput struct {
	Data_WrapEdkMaterialOutput_
}

func (_this WrapEdkMaterialOutput) Get_() Data_WrapEdkMaterialOutput_ {
	return _this.Data_WrapEdkMaterialOutput_
}

type Data_WrapEdkMaterialOutput_ interface {
	isWrapEdkMaterialOutput()
}

type CompanionStruct_WrapEdkMaterialOutput_ struct {
}

var Companion_WrapEdkMaterialOutput_ = CompanionStruct_WrapEdkMaterialOutput_{}

type WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput struct {
	WrappedMaterial     _dafny.Sequence
	SymmetricSigningKey m_Wrappers.Option
	WrapInfo            interface{}
}

func (WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput) isWrapEdkMaterialOutput() {}

func (CompanionStruct_WrapEdkMaterialOutput_) Create_WrapOnlyEdkMaterialOutput_(WrappedMaterial _dafny.Sequence, SymmetricSigningKey m_Wrappers.Option, WrapInfo interface{}) WrapEdkMaterialOutput {
	return WrapEdkMaterialOutput{WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput{WrappedMaterial, SymmetricSigningKey, WrapInfo}}
}

func (_this WrapEdkMaterialOutput) Is_WrapOnlyEdkMaterialOutput() bool {
	_, ok := _this.Get_().(WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput)
	return ok
}

type WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput struct {
	PlaintextDataKey    _dafny.Sequence
	WrappedMaterial     _dafny.Sequence
	SymmetricSigningKey m_Wrappers.Option
	WrapInfo            interface{}
}

func (WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput) isWrapEdkMaterialOutput() {}

func (CompanionStruct_WrapEdkMaterialOutput_) Create_GenerateAndWrapEdkMaterialOutput_(PlaintextDataKey _dafny.Sequence, WrappedMaterial _dafny.Sequence, SymmetricSigningKey m_Wrappers.Option, WrapInfo interface{}) WrapEdkMaterialOutput {
	return WrapEdkMaterialOutput{WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput{PlaintextDataKey, WrappedMaterial, SymmetricSigningKey, WrapInfo}}
}

func (_this WrapEdkMaterialOutput) Is_GenerateAndWrapEdkMaterialOutput() bool {
	_, ok := _this.Get_().(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput)
	return ok
}

func (CompanionStruct_WrapEdkMaterialOutput_) Default(_default_T interface{}) WrapEdkMaterialOutput {
	return Companion_WrapEdkMaterialOutput_.Create_WrapOnlyEdkMaterialOutput_(_dafny.EmptySeq, m_Wrappers.Companion_Option_.Default(), _default_T)
}

func (_this WrapEdkMaterialOutput) Dtor_wrappedMaterial() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput:
		return data.WrappedMaterial
	default:
		return data.(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput).WrappedMaterial
	}
}

func (_this WrapEdkMaterialOutput) Dtor_symmetricSigningKey() m_Wrappers.Option {
	switch data := _this.Get_().(type) {
	case WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput:
		return data.SymmetricSigningKey
	default:
		return data.(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput).SymmetricSigningKey
	}
}

func (_this WrapEdkMaterialOutput) Dtor_wrapInfo() interface{} {
	switch data := _this.Get_().(type) {
	case WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput:
		return data.WrapInfo
	default:
		return data.(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput).WrapInfo
	}
}

func (_this WrapEdkMaterialOutput) Dtor_plaintextDataKey() _dafny.Sequence {
	return _this.Get_().(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput).PlaintextDataKey
}

func (_this WrapEdkMaterialOutput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput:
		{
			return "EdkWrapping.WrapEdkMaterialOutput.WrapOnlyEdkMaterialOutput" + "(" + _dafny.String(data.WrappedMaterial) + ", " + _dafny.String(data.SymmetricSigningKey) + ", " + _dafny.String(data.WrapInfo) + ")"
		}
	case WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput:
		{
			return "EdkWrapping.WrapEdkMaterialOutput.GenerateAndWrapEdkMaterialOutput" + "(" + _dafny.String(data.PlaintextDataKey) + ", " + _dafny.String(data.WrappedMaterial) + ", " + _dafny.String(data.SymmetricSigningKey) + ", " + _dafny.String(data.WrapInfo) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this WrapEdkMaterialOutput) Equals(other WrapEdkMaterialOutput) bool {
	switch data1 := _this.Get_().(type) {
	case WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput:
		{
			data2, ok := other.Get_().(WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput)
			return ok && data1.WrappedMaterial.Equals(data2.WrappedMaterial) && data1.SymmetricSigningKey.Equals(data2.SymmetricSigningKey) && _dafny.AreEqual(data1.WrapInfo, data2.WrapInfo)
		}
	case WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput:
		{
			data2, ok := other.Get_().(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput)
			return ok && data1.PlaintextDataKey.Equals(data2.PlaintextDataKey) && data1.WrappedMaterial.Equals(data2.WrappedMaterial) && data1.SymmetricSigningKey.Equals(data2.SymmetricSigningKey) && _dafny.AreEqual(data1.WrapInfo, data2.WrapInfo)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this WrapEdkMaterialOutput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(WrapEdkMaterialOutput)
	return ok && _this.Equals(typed)
}

func Type_WrapEdkMaterialOutput_(Type_T_ _dafny.TypeDescriptor) _dafny.TypeDescriptor {
	return type_WrapEdkMaterialOutput_{Type_T_}
}

type type_WrapEdkMaterialOutput_ struct {
	Type_T_ _dafny.TypeDescriptor
}

func (_this type_WrapEdkMaterialOutput_) Default() interface{} {
	Type_T_ := _this.Type_T_
	_ = Type_T_
	return Companion_WrapEdkMaterialOutput_.Default(Type_T_.Default())
}

func (_this type_WrapEdkMaterialOutput_) String() string {
	return "EdkWrapping.WrapEdkMaterialOutput"
}
func (_this WrapEdkMaterialOutput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = WrapEdkMaterialOutput{}

// End of datatype WrapEdkMaterialOutput

// Definition of datatype UnwrapEdkMaterialOutput
type UnwrapEdkMaterialOutput struct {
	Data_UnwrapEdkMaterialOutput_
}

func (_this UnwrapEdkMaterialOutput) Get_() Data_UnwrapEdkMaterialOutput_ {
	return _this.Data_UnwrapEdkMaterialOutput_
}

type Data_UnwrapEdkMaterialOutput_ interface {
	isUnwrapEdkMaterialOutput()
}

type CompanionStruct_UnwrapEdkMaterialOutput_ struct {
}

var Companion_UnwrapEdkMaterialOutput_ = CompanionStruct_UnwrapEdkMaterialOutput_{}

type UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput struct {
	PlaintextDataKey    _dafny.Sequence
	SymmetricSigningKey m_Wrappers.Option
	UnwrapInfo          interface{}
}

func (UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput) isUnwrapEdkMaterialOutput() {}

func (CompanionStruct_UnwrapEdkMaterialOutput_) Create_UnwrapEdkMaterialOutput_(PlaintextDataKey _dafny.Sequence, SymmetricSigningKey m_Wrappers.Option, UnwrapInfo interface{}) UnwrapEdkMaterialOutput {
	return UnwrapEdkMaterialOutput{UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput{PlaintextDataKey, SymmetricSigningKey, UnwrapInfo}}
}

func (_this UnwrapEdkMaterialOutput) Is_UnwrapEdkMaterialOutput() bool {
	_, ok := _this.Get_().(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput)
	return ok
}

func (CompanionStruct_UnwrapEdkMaterialOutput_) Default(_default_T interface{}) UnwrapEdkMaterialOutput {
	return Companion_UnwrapEdkMaterialOutput_.Create_UnwrapEdkMaterialOutput_(_dafny.EmptySeq, m_Wrappers.Companion_Option_.Default(), _default_T)
}

func (_this UnwrapEdkMaterialOutput) Dtor_plaintextDataKey() _dafny.Sequence {
	return _this.Get_().(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput).PlaintextDataKey
}

func (_this UnwrapEdkMaterialOutput) Dtor_symmetricSigningKey() m_Wrappers.Option {
	return _this.Get_().(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput).SymmetricSigningKey
}

func (_this UnwrapEdkMaterialOutput) Dtor_unwrapInfo() interface{} {
	return _this.Get_().(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput).UnwrapInfo
}

func (_this UnwrapEdkMaterialOutput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput:
		{
			return "EdkWrapping.UnwrapEdkMaterialOutput.UnwrapEdkMaterialOutput" + "(" + _dafny.String(data.PlaintextDataKey) + ", " + _dafny.String(data.SymmetricSigningKey) + ", " + _dafny.String(data.UnwrapInfo) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this UnwrapEdkMaterialOutput) Equals(other UnwrapEdkMaterialOutput) bool {
	switch data1 := _this.Get_().(type) {
	case UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput:
		{
			data2, ok := other.Get_().(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput)
			return ok && data1.PlaintextDataKey.Equals(data2.PlaintextDataKey) && data1.SymmetricSigningKey.Equals(data2.SymmetricSigningKey) && _dafny.AreEqual(data1.UnwrapInfo, data2.UnwrapInfo)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this UnwrapEdkMaterialOutput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(UnwrapEdkMaterialOutput)
	return ok && _this.Equals(typed)
}

func Type_UnwrapEdkMaterialOutput_(Type_T_ _dafny.TypeDescriptor) _dafny.TypeDescriptor {
	return type_UnwrapEdkMaterialOutput_{Type_T_}
}

type type_UnwrapEdkMaterialOutput_ struct {
	Type_T_ _dafny.TypeDescriptor
}

func (_this type_UnwrapEdkMaterialOutput_) Default() interface{} {
	Type_T_ := _this.Type_T_
	_ = Type_T_
	return Companion_UnwrapEdkMaterialOutput_.Default(Type_T_.Default())
}

func (_this type_UnwrapEdkMaterialOutput_) String() string {
	return "EdkWrapping.UnwrapEdkMaterialOutput"
}
func (_this UnwrapEdkMaterialOutput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = UnwrapEdkMaterialOutput{}

// End of datatype UnwrapEdkMaterialOutput
