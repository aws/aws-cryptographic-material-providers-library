// Package MaterialProviders
// Dafny module MaterialProviders compiled into Go

package MaterialProviders

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
	return "MaterialProviders.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) DefaultMaterialProvidersConfig() m_AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_MaterialProvidersConfig_.Create_MaterialProvidersConfig_()
}
func (_static *CompanionStruct_Default___) MaterialProviders(config m_AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig) m_Wrappers.Result {
	var res m_Wrappers.Result = m_Wrappers.Result{}
	_ = res
	var _0_maybeCrypto m_Wrappers.Result
	_ = _0_maybeCrypto
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_maybeCrypto = _out0
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _1_valueOrError0
	_1_valueOrError0 = (_0_maybeCrypto).MapFailure(func(coer138 func(m_AwsCryptographyPrimitivesTypes.Error) m_AwsCryptographyMaterialProvidersTypes.Error) func(interface{}) interface{} {
		return func(arg139 interface{}) interface{} {
			return coer138(arg139.(m_AwsCryptographyPrimitivesTypes.Error))
		}
	}(func(_2_e m_AwsCryptographyPrimitivesTypes.Error) m_AwsCryptographyMaterialProvidersTypes.Error {
		return m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographyPrimitives_(_2_e)
	}))
	if (_1_valueOrError0).IsFailure() {
		res = (_1_valueOrError0).PropagateFailure()
		return res
	}
	var _3_cryptoPrimitivesX m_AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
	_ = _3_cryptoPrimitivesX
	_3_cryptoPrimitivesX = (_1_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _4_cryptoPrimitives *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _4_cryptoPrimitives
	_4_cryptoPrimitives = _3_cryptoPrimitivesX.(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _5_client *MaterialProvidersClient
	_ = _5_client
	var _nw0 *MaterialProvidersClient = New_MaterialProvidersClient_()
	_ = _nw0
	_nw0.Ctor__(m_AwsCryptographyMaterialProvidersOperations.Companion_Config_.Create_Config_(_4_cryptoPrimitives))
	_5_client = _nw0
	res = m_Wrappers.Companion_Result_.Create_Success_(_5_client)
	return res
	return res
}
func (_static *CompanionStruct_Default___) CreateSuccessOfClient(client m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient) m_Wrappers.Result {
	return m_Wrappers.Companion_Result_.Create_Success_(client)
}
func (_static *CompanionStruct_Default___) CreateFailureOfError(error_ m_AwsCryptographyMaterialProvidersTypes.Error) m_Wrappers.Result {
	return m_Wrappers.Companion_Result_.Create_Failure_(error_)
}

// End of class Default__

// Definition of class MaterialProvidersClient
type MaterialProvidersClient struct {
	_config m_AwsCryptographyMaterialProvidersOperations.Config
}

func New_MaterialProvidersClient_() *MaterialProvidersClient {
	_this := MaterialProvidersClient{}

	_this._config = m_AwsCryptographyMaterialProvidersOperations.Config{}
	return &_this
}

type CompanionStruct_MaterialProvidersClient_ struct {
}

var Companion_MaterialProvidersClient_ = CompanionStruct_MaterialProvidersClient_{}

func (_this *MaterialProvidersClient) Equals(other *MaterialProvidersClient) bool {
	return _this == other
}

func (_this *MaterialProvidersClient) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*MaterialProvidersClient)
	return ok && _this.Equals(other)
}

func (*MaterialProvidersClient) String() string {
	return "MaterialProviders.MaterialProvidersClient"
}

func Type_MaterialProvidersClient_() _dafny.TypeDescriptor {
	return type_MaterialProvidersClient_{}
}

type type_MaterialProvidersClient_ struct {
}

func (_this type_MaterialProvidersClient_) Default() interface{} {
	return (*MaterialProvidersClient)(nil)
}

func (_this type_MaterialProvidersClient_) String() string {
	return "MaterialProviders.MaterialProvidersClient"
}
func (_this *MaterialProvidersClient) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){m_AwsCryptographyMaterialProvidersTypes.Companion_IAwsCryptographicMaterialProvidersClient_.TraitID_}
}

var _ m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient = &MaterialProvidersClient{}
var _ _dafny.TraitOffspring = &MaterialProvidersClient{}

func (_this *MaterialProvidersClient) Ctor__(config m_AwsCryptographyMaterialProvidersOperations.Config) {
	{
		(_this)._config = config
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsDiscoveryKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsDiscoveryKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsMultiKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMultiKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsMultiKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsDiscoveryMultiKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryMultiKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsDiscoveryMultiKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsMrkKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsMrkKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsMrkMultiKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkMultiKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsMrkMultiKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsMrkDiscoveryKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsMrkDiscoveryKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsMrkDiscoveryMultiKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsMrkDiscoveryMultiKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsHierarchicalKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsHierarchicalKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsRsaKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsRsaKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateAwsKmsEcdhKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateAwsKmsEcdhKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateMultiKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateMultiKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateRawAesKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateRawAesKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateRawRsaKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateRawRsaKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateRawEcdhKeyring(input m_AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateRawEcdhKeyring((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateDefaultCryptographicMaterialsManager(input m_AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateDefaultCryptographicMaterialsManager((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateRequiredEncryptionContextCMM(input m_AwsCryptographyMaterialProvidersTypes.CreateRequiredEncryptionContextCMMInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateRequiredEncryptionContextCMM((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateCryptographicMaterialsCache(input m_AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateCryptographicMaterialsCache((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) CreateDefaultClientSupplier(input m_AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.CreateDefaultClientSupplier((_this).Config(), input)
		output = _out0
		return output
	}
}
func (_this *MaterialProvidersClient) InitializeEncryptionMaterials(input m_AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.InitializeEncryptionMaterials((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) InitializeDecryptionMaterials(input m_AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.InitializeDecryptionMaterials((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) ValidEncryptionMaterialsTransition(input m_AwsCryptographyMaterialProvidersTypes.ValidEncryptionMaterialsTransitionInput) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.ValidEncryptionMaterialsTransition((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) ValidDecryptionMaterialsTransition(input m_AwsCryptographyMaterialProvidersTypes.ValidDecryptionMaterialsTransitionInput) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.ValidDecryptionMaterialsTransition((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) EncryptionMaterialsHasPlaintextDataKey(input m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.EncryptionMaterialsHasPlaintextDataKey((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) DecryptionMaterialsWithPlaintextDataKey(input m_AwsCryptographyMaterialProvidersTypes.DecryptionMaterials) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.DecryptionMaterialsWithPlaintextDataKey((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) GetAlgorithmSuiteInfo(input _dafny.Sequence) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.GetAlgorithmSuiteInfo((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) ValidAlgorithmSuiteInfo(input m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.ValidAlgorithmSuiteInfo((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) ValidateCommitmentPolicyOnEncrypt(input m_AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnEncryptInput) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.ValidateCommitmentPolicyOnEncrypt((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) ValidateCommitmentPolicyOnDecrypt(input m_AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnDecryptInput) m_Wrappers.Result {
	{
		return m_AwsCryptographyMaterialProvidersOperations.Companion_Default___.ValidateCommitmentPolicyOnDecrypt((_this).Config(), input)
	}
}
func (_this *MaterialProvidersClient) Config() m_AwsCryptographyMaterialProvidersOperations.Config {
	{
		return _this._config
	}
}

// End of class MaterialProvidersClient