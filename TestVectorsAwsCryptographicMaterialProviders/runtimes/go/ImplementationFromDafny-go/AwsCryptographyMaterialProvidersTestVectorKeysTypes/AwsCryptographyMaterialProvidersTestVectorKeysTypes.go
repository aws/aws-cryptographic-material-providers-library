// Package AwsCryptographyMaterialProvidersTestVectorKeysTypes
// Dafny module AwsCryptographyMaterialProvidersTestVectorKeysTypes compiled into Go

package AwsCryptographyMaterialProvidersTestVectorKeysTypes

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
	m_AllAlgorithmSuites "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllAlgorithmSuites"
	m_MplManifestOptions "github.com/aws/aws-cryptographic-material-providers-library/testvectors/MplManifestOptions"
	m_WrappedMaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/testvectors/WrappedMaterialProviders"
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
var _ m_AwsCryptographyKeyStoreTypes.Dummy__
var _ m_AwsCryptographyMaterialProvidersTypes.Dummy__
var _ m_Base64.Dummy__
var _ m_AlgorithmSuites.Dummy__
var _ m_Materials.Dummy__
var _ m_Keyring.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m_MultiKeyring.Dummy__
var _ m_AwsArnParsing.Dummy__
var _ m_AwsKmsMrkAreUnique.Dummy__
var _ m_Actions.Dummy__
var _ m_AwsKmsMrkMatchForDecrypt.Dummy__
var _ m_AwsKmsUtils.Dummy__
var _ m_Constants.Dummy__
var _ m_MaterialWrapping.Dummy__
var _ m_CanonicalEncryptionContext.Dummy__
var _ m_IntermediateKeyWrapping.Dummy__
var _ m_EdkWrapping.Dummy__
var _ m_ErrorMessages.Dummy__
var _ m_AwsKmsKeyring.Dummy__
var _ m_StrictMultiKeyring.Dummy__
var _ m_AwsKmsDiscoveryKeyring.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__
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
var _ m_KeyStoreErrorMessages.Dummy__
var _ m_KmsArn.Dummy__
var _ m_Structure.Dummy__
var _ m_KMSKeystoreOperations.Dummy__
var _ m_DDBKeystoreOperations.Dummy__
var _ m_CreateKeys.Dummy__
var _ m_CreateKeyStoreTable.Dummy__
var _ m_GetKeys.Dummy__
var _ m_AwsCryptographyKeyStoreOperations.Dummy__
var _ m_KeyStore.Dummy__
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
var _ m_MplManifestOptions.Dummy__
var _ m_AllAlgorithmSuites.Dummy__
var _ m_WrappedMaterialProviders.Dummy__

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
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) IsDummySubsetType(x _dafny.Int) bool {
	return (x).Sign() == 1
}

// End of class Default__

// Definition of datatype DafnyCallEvent
type DafnyCallEvent struct {
	Data_DafnyCallEvent_
}

func (_this DafnyCallEvent) Get_() Data_DafnyCallEvent_ {
	return _this.Data_DafnyCallEvent_
}

type Data_DafnyCallEvent_ interface {
	isDafnyCallEvent()
}

type CompanionStruct_DafnyCallEvent_ struct {
}

var Companion_DafnyCallEvent_ = CompanionStruct_DafnyCallEvent_{}

type DafnyCallEvent_DafnyCallEvent struct {
	Input  interface{}
	Output interface{}
}

func (DafnyCallEvent_DafnyCallEvent) isDafnyCallEvent() {}

func (CompanionStruct_DafnyCallEvent_) Create_DafnyCallEvent_(Input interface{}, Output interface{}) DafnyCallEvent {
	return DafnyCallEvent{DafnyCallEvent_DafnyCallEvent{Input, Output}}
}

func (_this DafnyCallEvent) Is_DafnyCallEvent() bool {
	_, ok := _this.Get_().(DafnyCallEvent_DafnyCallEvent)
	return ok
}

func (CompanionStruct_DafnyCallEvent_) Default(_default_I interface{}, _default_O interface{}) DafnyCallEvent {
	return Companion_DafnyCallEvent_.Create_DafnyCallEvent_(_default_I, _default_O)
}

func (_this DafnyCallEvent) Dtor_input() interface{} {
	return _this.Get_().(DafnyCallEvent_DafnyCallEvent).Input
}

func (_this DafnyCallEvent) Dtor_output() interface{} {
	return _this.Get_().(DafnyCallEvent_DafnyCallEvent).Output
}

func (_this DafnyCallEvent) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case DafnyCallEvent_DafnyCallEvent:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.DafnyCallEvent.DafnyCallEvent" + "(" + _dafny.String(data.Input) + ", " + _dafny.String(data.Output) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this DafnyCallEvent) Equals(other DafnyCallEvent) bool {
	switch data1 := _this.Get_().(type) {
	case DafnyCallEvent_DafnyCallEvent:
		{
			data2, ok := other.Get_().(DafnyCallEvent_DafnyCallEvent)
			return ok && _dafny.AreEqual(data1.Input, data2.Input) && _dafny.AreEqual(data1.Output, data2.Output)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this DafnyCallEvent) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(DafnyCallEvent)
	return ok && _this.Equals(typed)
}

func Type_DafnyCallEvent_(Type_I_ _dafny.TypeDescriptor, Type_O_ _dafny.TypeDescriptor) _dafny.TypeDescriptor {
	return type_DafnyCallEvent_{Type_I_, Type_O_}
}

type type_DafnyCallEvent_ struct {
	Type_I_ _dafny.TypeDescriptor
	Type_O_ _dafny.TypeDescriptor
}

func (_this type_DafnyCallEvent_) Default() interface{} {
	Type_I_ := _this.Type_I_
	_ = Type_I_
	Type_O_ := _this.Type_O_
	_ = Type_O_
	return Companion_DafnyCallEvent_.Default(Type_I_.Default(), Type_O_.Default())
}

func (_this type_DafnyCallEvent_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.DafnyCallEvent"
}
func (_this DafnyCallEvent) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = DafnyCallEvent{}

// End of datatype DafnyCallEvent

// Definition of datatype CmmOperation
type CmmOperation struct {
	Data_CmmOperation_
}

func (_this CmmOperation) Get_() Data_CmmOperation_ {
	return _this.Data_CmmOperation_
}

type Data_CmmOperation_ interface {
	isCmmOperation()
}

type CompanionStruct_CmmOperation_ struct {
}

var Companion_CmmOperation_ = CompanionStruct_CmmOperation_{}

type CmmOperation_ENCRYPT struct {
}

func (CmmOperation_ENCRYPT) isCmmOperation() {}

func (CompanionStruct_CmmOperation_) Create_ENCRYPT_() CmmOperation {
	return CmmOperation{CmmOperation_ENCRYPT{}}
}

func (_this CmmOperation) Is_ENCRYPT() bool {
	_, ok := _this.Get_().(CmmOperation_ENCRYPT)
	return ok
}

type CmmOperation_DECRYPT struct {
}

func (CmmOperation_DECRYPT) isCmmOperation() {}

func (CompanionStruct_CmmOperation_) Create_DECRYPT_() CmmOperation {
	return CmmOperation{CmmOperation_DECRYPT{}}
}

func (_this CmmOperation) Is_DECRYPT() bool {
	_, ok := _this.Get_().(CmmOperation_DECRYPT)
	return ok
}

func (CompanionStruct_CmmOperation_) Default() CmmOperation {
	return Companion_CmmOperation_.Create_ENCRYPT_()
}

func (_ CompanionStruct_CmmOperation_) AllSingletonConstructors() _dafny.Iterator {
	i := -1
	return func() (interface{}, bool) {
		i++
		switch i {
		case 0:
			return Companion_CmmOperation_.Create_ENCRYPT_(), true
		case 1:
			return Companion_CmmOperation_.Create_DECRYPT_(), true
		default:
			return CmmOperation{}, false
		}
	}
}

func (_this CmmOperation) String() string {
	switch _this.Get_().(type) {
	case nil:
		return "null"
	case CmmOperation_ENCRYPT:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.ENCRYPT"
		}
	case CmmOperation_DECRYPT:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.DECRYPT"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this CmmOperation) Equals(other CmmOperation) bool {
	switch _this.Get_().(type) {
	case CmmOperation_ENCRYPT:
		{
			_, ok := other.Get_().(CmmOperation_ENCRYPT)
			return ok
		}
	case CmmOperation_DECRYPT:
		{
			_, ok := other.Get_().(CmmOperation_DECRYPT)
			return ok
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this CmmOperation) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(CmmOperation)
	return ok && _this.Equals(typed)
}

func Type_CmmOperation_() _dafny.TypeDescriptor {
	return type_CmmOperation_{}
}

type type_CmmOperation_ struct {
}

func (_this type_CmmOperation_) Default() interface{} {
	return Companion_CmmOperation_.Default()
}

func (_this type_CmmOperation_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation"
}
func (_this CmmOperation) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = CmmOperation{}

// End of datatype CmmOperation

// Definition of datatype GetKeyDescriptionInput
type GetKeyDescriptionInput struct {
	Data_GetKeyDescriptionInput_
}

func (_this GetKeyDescriptionInput) Get_() Data_GetKeyDescriptionInput_ {
	return _this.Data_GetKeyDescriptionInput_
}

type Data_GetKeyDescriptionInput_ interface {
	isGetKeyDescriptionInput()
}

type CompanionStruct_GetKeyDescriptionInput_ struct {
}

var Companion_GetKeyDescriptionInput_ = CompanionStruct_GetKeyDescriptionInput_{}

type GetKeyDescriptionInput_GetKeyDescriptionInput struct {
	Json _dafny.Sequence
}

func (GetKeyDescriptionInput_GetKeyDescriptionInput) isGetKeyDescriptionInput() {}

func (CompanionStruct_GetKeyDescriptionInput_) Create_GetKeyDescriptionInput_(Json _dafny.Sequence) GetKeyDescriptionInput {
	return GetKeyDescriptionInput{GetKeyDescriptionInput_GetKeyDescriptionInput{Json}}
}

func (_this GetKeyDescriptionInput) Is_GetKeyDescriptionInput() bool {
	_, ok := _this.Get_().(GetKeyDescriptionInput_GetKeyDescriptionInput)
	return ok
}

func (CompanionStruct_GetKeyDescriptionInput_) Default() GetKeyDescriptionInput {
	return Companion_GetKeyDescriptionInput_.Create_GetKeyDescriptionInput_(_dafny.EmptySeq)
}

func (_this GetKeyDescriptionInput) Dtor_json() _dafny.Sequence {
	return _this.Get_().(GetKeyDescriptionInput_GetKeyDescriptionInput).Json
}

func (_this GetKeyDescriptionInput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case GetKeyDescriptionInput_GetKeyDescriptionInput:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput.GetKeyDescriptionInput" + "(" + _dafny.String(data.Json) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this GetKeyDescriptionInput) Equals(other GetKeyDescriptionInput) bool {
	switch data1 := _this.Get_().(type) {
	case GetKeyDescriptionInput_GetKeyDescriptionInput:
		{
			data2, ok := other.Get_().(GetKeyDescriptionInput_GetKeyDescriptionInput)
			return ok && data1.Json.Equals(data2.Json)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this GetKeyDescriptionInput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(GetKeyDescriptionInput)
	return ok && _this.Equals(typed)
}

func Type_GetKeyDescriptionInput_() _dafny.TypeDescriptor {
	return type_GetKeyDescriptionInput_{}
}

type type_GetKeyDescriptionInput_ struct {
}

func (_this type_GetKeyDescriptionInput_) Default() interface{} {
	return Companion_GetKeyDescriptionInput_.Default()
}

func (_this type_GetKeyDescriptionInput_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput"
}
func (_this GetKeyDescriptionInput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = GetKeyDescriptionInput{}

// End of datatype GetKeyDescriptionInput

// Definition of datatype GetKeyDescriptionOutput
type GetKeyDescriptionOutput struct {
	Data_GetKeyDescriptionOutput_
}

func (_this GetKeyDescriptionOutput) Get_() Data_GetKeyDescriptionOutput_ {
	return _this.Data_GetKeyDescriptionOutput_
}

type Data_GetKeyDescriptionOutput_ interface {
	isGetKeyDescriptionOutput()
}

type CompanionStruct_GetKeyDescriptionOutput_ struct {
}

var Companion_GetKeyDescriptionOutput_ = CompanionStruct_GetKeyDescriptionOutput_{}

type GetKeyDescriptionOutput_GetKeyDescriptionOutput struct {
	KeyDescription KeyDescription
}

func (GetKeyDescriptionOutput_GetKeyDescriptionOutput) isGetKeyDescriptionOutput() {}

func (CompanionStruct_GetKeyDescriptionOutput_) Create_GetKeyDescriptionOutput_(KeyDescription KeyDescription) GetKeyDescriptionOutput {
	return GetKeyDescriptionOutput{GetKeyDescriptionOutput_GetKeyDescriptionOutput{KeyDescription}}
}

func (_this GetKeyDescriptionOutput) Is_GetKeyDescriptionOutput() bool {
	_, ok := _this.Get_().(GetKeyDescriptionOutput_GetKeyDescriptionOutput)
	return ok
}

func (CompanionStruct_GetKeyDescriptionOutput_) Default() GetKeyDescriptionOutput {
	return Companion_GetKeyDescriptionOutput_.Create_GetKeyDescriptionOutput_(Companion_KeyDescription_.Default())
}

func (_this GetKeyDescriptionOutput) Dtor_keyDescription() KeyDescription {
	return _this.Get_().(GetKeyDescriptionOutput_GetKeyDescriptionOutput).KeyDescription
}

func (_this GetKeyDescriptionOutput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case GetKeyDescriptionOutput_GetKeyDescriptionOutput:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput.GetKeyDescriptionOutput" + "(" + _dafny.String(data.KeyDescription) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this GetKeyDescriptionOutput) Equals(other GetKeyDescriptionOutput) bool {
	switch data1 := _this.Get_().(type) {
	case GetKeyDescriptionOutput_GetKeyDescriptionOutput:
		{
			data2, ok := other.Get_().(GetKeyDescriptionOutput_GetKeyDescriptionOutput)
			return ok && data1.KeyDescription.Equals(data2.KeyDescription)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this GetKeyDescriptionOutput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(GetKeyDescriptionOutput)
	return ok && _this.Equals(typed)
}

func Type_GetKeyDescriptionOutput_() _dafny.TypeDescriptor {
	return type_GetKeyDescriptionOutput_{}
}

type type_GetKeyDescriptionOutput_ struct {
}

func (_this type_GetKeyDescriptionOutput_) Default() interface{} {
	return Companion_GetKeyDescriptionOutput_.Default()
}

func (_this type_GetKeyDescriptionOutput_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput"
}
func (_this GetKeyDescriptionOutput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = GetKeyDescriptionOutput{}

// End of datatype GetKeyDescriptionOutput

// Definition of datatype HierarchyKeyring
type HierarchyKeyring struct {
	Data_HierarchyKeyring_
}

func (_this HierarchyKeyring) Get_() Data_HierarchyKeyring_ {
	return _this.Data_HierarchyKeyring_
}

type Data_HierarchyKeyring_ interface {
	isHierarchyKeyring()
}

type CompanionStruct_HierarchyKeyring_ struct {
}

var Companion_HierarchyKeyring_ = CompanionStruct_HierarchyKeyring_{}

type HierarchyKeyring_HierarchyKeyring struct {
	KeyId _dafny.Sequence
}

func (HierarchyKeyring_HierarchyKeyring) isHierarchyKeyring() {}

func (CompanionStruct_HierarchyKeyring_) Create_HierarchyKeyring_(KeyId _dafny.Sequence) HierarchyKeyring {
	return HierarchyKeyring{HierarchyKeyring_HierarchyKeyring{KeyId}}
}

func (_this HierarchyKeyring) Is_HierarchyKeyring() bool {
	_, ok := _this.Get_().(HierarchyKeyring_HierarchyKeyring)
	return ok
}

func (CompanionStruct_HierarchyKeyring_) Default() HierarchyKeyring {
	return Companion_HierarchyKeyring_.Create_HierarchyKeyring_(_dafny.EmptySeq.SetString())
}

func (_this HierarchyKeyring) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(HierarchyKeyring_HierarchyKeyring).KeyId
}

func (_this HierarchyKeyring) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case HierarchyKeyring_HierarchyKeyring:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring.HierarchyKeyring" + "(" + _dafny.String(data.KeyId) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this HierarchyKeyring) Equals(other HierarchyKeyring) bool {
	switch data1 := _this.Get_().(type) {
	case HierarchyKeyring_HierarchyKeyring:
		{
			data2, ok := other.Get_().(HierarchyKeyring_HierarchyKeyring)
			return ok && data1.KeyId.Equals(data2.KeyId)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this HierarchyKeyring) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(HierarchyKeyring)
	return ok && _this.Equals(typed)
}

func Type_HierarchyKeyring_() _dafny.TypeDescriptor {
	return type_HierarchyKeyring_{}
}

type type_HierarchyKeyring_ struct {
}

func (_this type_HierarchyKeyring_) Default() interface{} {
	return Companion_HierarchyKeyring_.Default()
}

func (_this type_HierarchyKeyring_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring"
}
func (_this HierarchyKeyring) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = HierarchyKeyring{}

// End of datatype HierarchyKeyring

// Definition of datatype KeyDescription
type KeyDescription struct {
	Data_KeyDescription_
}

func (_this KeyDescription) Get_() Data_KeyDescription_ {
	return _this.Data_KeyDescription_
}

type Data_KeyDescription_ interface {
	isKeyDescription()
}

type CompanionStruct_KeyDescription_ struct {
}

var Companion_KeyDescription_ = CompanionStruct_KeyDescription_{}

type KeyDescription_Kms struct {
	Kms KMSInfo
}

func (KeyDescription_Kms) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_Kms_(Kms KMSInfo) KeyDescription {
	return KeyDescription{KeyDescription_Kms{Kms}}
}

func (_this KeyDescription) Is_Kms() bool {
	_, ok := _this.Get_().(KeyDescription_Kms)
	return ok
}

type KeyDescription_KmsMrk struct {
	KmsMrk KmsMrkAware
}

func (KeyDescription_KmsMrk) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_KmsMrk_(KmsMrk KmsMrkAware) KeyDescription {
	return KeyDescription{KeyDescription_KmsMrk{KmsMrk}}
}

func (_this KeyDescription) Is_KmsMrk() bool {
	_, ok := _this.Get_().(KeyDescription_KmsMrk)
	return ok
}

type KeyDescription_KmsMrkDiscovery struct {
	KmsMrkDiscovery KmsMrkAwareDiscovery
}

func (KeyDescription_KmsMrkDiscovery) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_KmsMrkDiscovery_(KmsMrkDiscovery KmsMrkAwareDiscovery) KeyDescription {
	return KeyDescription{KeyDescription_KmsMrkDiscovery{KmsMrkDiscovery}}
}

func (_this KeyDescription) Is_KmsMrkDiscovery() bool {
	_, ok := _this.Get_().(KeyDescription_KmsMrkDiscovery)
	return ok
}

type KeyDescription_RSA struct {
	RSA RawRSA
}

func (KeyDescription_RSA) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_RSA_(RSA RawRSA) KeyDescription {
	return KeyDescription{KeyDescription_RSA{RSA}}
}

func (_this KeyDescription) Is_RSA() bool {
	_, ok := _this.Get_().(KeyDescription_RSA)
	return ok
}

type KeyDescription_AES struct {
	AES RawAES
}

func (KeyDescription_AES) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_AES_(AES RawAES) KeyDescription {
	return KeyDescription{KeyDescription_AES{AES}}
}

func (_this KeyDescription) Is_AES() bool {
	_, ok := _this.Get_().(KeyDescription_AES)
	return ok
}

type KeyDescription_ECDH struct {
	ECDH RawEcdh
}

func (KeyDescription_ECDH) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_ECDH_(ECDH RawEcdh) KeyDescription {
	return KeyDescription{KeyDescription_ECDH{ECDH}}
}

func (_this KeyDescription) Is_ECDH() bool {
	_, ok := _this.Get_().(KeyDescription_ECDH)
	return ok
}

type KeyDescription_Static struct {
	Static StaticKeyring
}

func (KeyDescription_Static) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_Static_(Static StaticKeyring) KeyDescription {
	return KeyDescription{KeyDescription_Static{Static}}
}

func (_this KeyDescription) Is_Static() bool {
	_, ok := _this.Get_().(KeyDescription_Static)
	return ok
}

type KeyDescription_KmsRsa struct {
	KmsRsa KmsRsaKeyring
}

func (KeyDescription_KmsRsa) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_KmsRsa_(KmsRsa KmsRsaKeyring) KeyDescription {
	return KeyDescription{KeyDescription_KmsRsa{KmsRsa}}
}

func (_this KeyDescription) Is_KmsRsa() bool {
	_, ok := _this.Get_().(KeyDescription_KmsRsa)
	return ok
}

type KeyDescription_KmsECDH struct {
	KmsECDH KmsEcdhKeyring
}

func (KeyDescription_KmsECDH) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_KmsECDH_(KmsECDH KmsEcdhKeyring) KeyDescription {
	return KeyDescription{KeyDescription_KmsECDH{KmsECDH}}
}

func (_this KeyDescription) Is_KmsECDH() bool {
	_, ok := _this.Get_().(KeyDescription_KmsECDH)
	return ok
}

type KeyDescription_Hierarchy struct {
	Hierarchy HierarchyKeyring
}

func (KeyDescription_Hierarchy) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_Hierarchy_(Hierarchy HierarchyKeyring) KeyDescription {
	return KeyDescription{KeyDescription_Hierarchy{Hierarchy}}
}

func (_this KeyDescription) Is_Hierarchy() bool {
	_, ok := _this.Get_().(KeyDescription_Hierarchy)
	return ok
}

type KeyDescription_Multi struct {
	Multi MultiKeyring
}

func (KeyDescription_Multi) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_Multi_(Multi MultiKeyring) KeyDescription {
	return KeyDescription{KeyDescription_Multi{Multi}}
}

func (_this KeyDescription) Is_Multi() bool {
	_, ok := _this.Get_().(KeyDescription_Multi)
	return ok
}

type KeyDescription_RequiredEncryptionContext struct {
	RequiredEncryptionContext RequiredEncryptionContextCMM
}

func (KeyDescription_RequiredEncryptionContext) isKeyDescription() {}

func (CompanionStruct_KeyDescription_) Create_RequiredEncryptionContext_(RequiredEncryptionContext RequiredEncryptionContextCMM) KeyDescription {
	return KeyDescription{KeyDescription_RequiredEncryptionContext{RequiredEncryptionContext}}
}

func (_this KeyDescription) Is_RequiredEncryptionContext() bool {
	_, ok := _this.Get_().(KeyDescription_RequiredEncryptionContext)
	return ok
}

func (CompanionStruct_KeyDescription_) Default() KeyDescription {
	return Companion_KeyDescription_.Create_Kms_(Companion_KMSInfo_.Default())
}

func (_this KeyDescription) Dtor_Kms() KMSInfo {
	return _this.Get_().(KeyDescription_Kms).Kms
}

func (_this KeyDescription) Dtor_KmsMrk() KmsMrkAware {
	return _this.Get_().(KeyDescription_KmsMrk).KmsMrk
}

func (_this KeyDescription) Dtor_KmsMrkDiscovery() KmsMrkAwareDiscovery {
	return _this.Get_().(KeyDescription_KmsMrkDiscovery).KmsMrkDiscovery
}

func (_this KeyDescription) Dtor_RSA() RawRSA {
	return _this.Get_().(KeyDescription_RSA).RSA
}

func (_this KeyDescription) Dtor_AES() RawAES {
	return _this.Get_().(KeyDescription_AES).AES
}

func (_this KeyDescription) Dtor_ECDH() RawEcdh {
	return _this.Get_().(KeyDescription_ECDH).ECDH
}

func (_this KeyDescription) Dtor_Static() StaticKeyring {
	return _this.Get_().(KeyDescription_Static).Static
}

func (_this KeyDescription) Dtor_KmsRsa() KmsRsaKeyring {
	return _this.Get_().(KeyDescription_KmsRsa).KmsRsa
}

func (_this KeyDescription) Dtor_KmsECDH() KmsEcdhKeyring {
	return _this.Get_().(KeyDescription_KmsECDH).KmsECDH
}

func (_this KeyDescription) Dtor_Hierarchy() HierarchyKeyring {
	return _this.Get_().(KeyDescription_Hierarchy).Hierarchy
}

func (_this KeyDescription) Dtor_Multi() MultiKeyring {
	return _this.Get_().(KeyDescription_Multi).Multi
}

func (_this KeyDescription) Dtor_RequiredEncryptionContext() RequiredEncryptionContextCMM {
	return _this.Get_().(KeyDescription_RequiredEncryptionContext).RequiredEncryptionContext
}

func (_this KeyDescription) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KeyDescription_Kms:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Kms" + "(" + _dafny.String(data.Kms) + ")"
		}
	case KeyDescription_KmsMrk:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrk" + "(" + _dafny.String(data.KmsMrk) + ")"
		}
	case KeyDescription_KmsMrkDiscovery:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrkDiscovery" + "(" + _dafny.String(data.KmsMrkDiscovery) + ")"
		}
	case KeyDescription_RSA:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RSA" + "(" + _dafny.String(data.RSA) + ")"
		}
	case KeyDescription_AES:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.AES" + "(" + _dafny.String(data.AES) + ")"
		}
	case KeyDescription_ECDH:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.ECDH" + "(" + _dafny.String(data.ECDH) + ")"
		}
	case KeyDescription_Static:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Static" + "(" + _dafny.String(data.Static) + ")"
		}
	case KeyDescription_KmsRsa:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsRsa" + "(" + _dafny.String(data.KmsRsa) + ")"
		}
	case KeyDescription_KmsECDH:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsECDH" + "(" + _dafny.String(data.KmsECDH) + ")"
		}
	case KeyDescription_Hierarchy:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Hierarchy" + "(" + _dafny.String(data.Hierarchy) + ")"
		}
	case KeyDescription_Multi:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Multi" + "(" + _dafny.String(data.Multi) + ")"
		}
	case KeyDescription_RequiredEncryptionContext:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RequiredEncryptionContext" + "(" + _dafny.String(data.RequiredEncryptionContext) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KeyDescription) Equals(other KeyDescription) bool {
	switch data1 := _this.Get_().(type) {
	case KeyDescription_Kms:
		{
			data2, ok := other.Get_().(KeyDescription_Kms)
			return ok && data1.Kms.Equals(data2.Kms)
		}
	case KeyDescription_KmsMrk:
		{
			data2, ok := other.Get_().(KeyDescription_KmsMrk)
			return ok && data1.KmsMrk.Equals(data2.KmsMrk)
		}
	case KeyDescription_KmsMrkDiscovery:
		{
			data2, ok := other.Get_().(KeyDescription_KmsMrkDiscovery)
			return ok && data1.KmsMrkDiscovery.Equals(data2.KmsMrkDiscovery)
		}
	case KeyDescription_RSA:
		{
			data2, ok := other.Get_().(KeyDescription_RSA)
			return ok && data1.RSA.Equals(data2.RSA)
		}
	case KeyDescription_AES:
		{
			data2, ok := other.Get_().(KeyDescription_AES)
			return ok && data1.AES.Equals(data2.AES)
		}
	case KeyDescription_ECDH:
		{
			data2, ok := other.Get_().(KeyDescription_ECDH)
			return ok && data1.ECDH.Equals(data2.ECDH)
		}
	case KeyDescription_Static:
		{
			data2, ok := other.Get_().(KeyDescription_Static)
			return ok && data1.Static.Equals(data2.Static)
		}
	case KeyDescription_KmsRsa:
		{
			data2, ok := other.Get_().(KeyDescription_KmsRsa)
			return ok && data1.KmsRsa.Equals(data2.KmsRsa)
		}
	case KeyDescription_KmsECDH:
		{
			data2, ok := other.Get_().(KeyDescription_KmsECDH)
			return ok && data1.KmsECDH.Equals(data2.KmsECDH)
		}
	case KeyDescription_Hierarchy:
		{
			data2, ok := other.Get_().(KeyDescription_Hierarchy)
			return ok && data1.Hierarchy.Equals(data2.Hierarchy)
		}
	case KeyDescription_Multi:
		{
			data2, ok := other.Get_().(KeyDescription_Multi)
			return ok && data1.Multi.Equals(data2.Multi)
		}
	case KeyDescription_RequiredEncryptionContext:
		{
			data2, ok := other.Get_().(KeyDescription_RequiredEncryptionContext)
			return ok && data1.RequiredEncryptionContext.Equals(data2.RequiredEncryptionContext)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KeyDescription) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KeyDescription)
	return ok && _this.Equals(typed)
}

func Type_KeyDescription_() _dafny.TypeDescriptor {
	return type_KeyDescription_{}
}

type type_KeyDescription_ struct {
}

func (_this type_KeyDescription_) Default() interface{} {
	return Companion_KeyDescription_.Default()
}

func (_this type_KeyDescription_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription"
}
func (_this KeyDescription) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KeyDescription{}

// End of datatype KeyDescription

// Definition of class IKeyVectorsClientCallHistory
type IKeyVectorsClientCallHistory struct {
	dummy byte
}

func New_IKeyVectorsClientCallHistory_() *IKeyVectorsClientCallHistory {
	_this := IKeyVectorsClientCallHistory{}

	return &_this
}

type CompanionStruct_IKeyVectorsClientCallHistory_ struct {
}

var Companion_IKeyVectorsClientCallHistory_ = CompanionStruct_IKeyVectorsClientCallHistory_{}

func (_this *IKeyVectorsClientCallHistory) Equals(other *IKeyVectorsClientCallHistory) bool {
	return _this == other
}

func (_this *IKeyVectorsClientCallHistory) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*IKeyVectorsClientCallHistory)
	return ok && _this.Equals(other)
}

func (*IKeyVectorsClientCallHistory) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.IKeyVectorsClientCallHistory"
}

func Type_IKeyVectorsClientCallHistory_() _dafny.TypeDescriptor {
	return type_IKeyVectorsClientCallHistory_{}
}

type type_IKeyVectorsClientCallHistory_ struct {
}

func (_this type_IKeyVectorsClientCallHistory_) Default() interface{} {
	return (*IKeyVectorsClientCallHistory)(nil)
}

func (_this type_IKeyVectorsClientCallHistory_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.IKeyVectorsClientCallHistory"
}
func (_this *IKeyVectorsClientCallHistory) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &IKeyVectorsClientCallHistory{}

// End of class IKeyVectorsClientCallHistory

// Definition of trait IKeyVectorsClient
type IKeyVectorsClient interface {
	String() string
	CreateTestVectorKeyring(input TestVectorKeyringInput) m_Wrappers.Result
	CreateWrappedTestVectorKeyring(input TestVectorKeyringInput) m_Wrappers.Result
	CreateWrappedTestVectorCmm(input TestVectorCmmInput) m_Wrappers.Result
	GetKeyDescription(input GetKeyDescriptionInput) m_Wrappers.Result
	SerializeKeyDescription(input SerializeKeyDescriptionInput) m_Wrappers.Result
}
type CompanionStruct_IKeyVectorsClient_ struct {
	TraitID_ *_dafny.TraitID
}

var Companion_IKeyVectorsClient_ = CompanionStruct_IKeyVectorsClient_{
	TraitID_: &_dafny.TraitID{},
}

func (CompanionStruct_IKeyVectorsClient_) CastTo_(x interface{}) IKeyVectorsClient {
	var t IKeyVectorsClient
	t, _ = x.(IKeyVectorsClient)
	return t
}

// End of trait IKeyVectorsClient

// Definition of datatype KeyVectorsConfig
type KeyVectorsConfig struct {
	Data_KeyVectorsConfig_
}

func (_this KeyVectorsConfig) Get_() Data_KeyVectorsConfig_ {
	return _this.Data_KeyVectorsConfig_
}

type Data_KeyVectorsConfig_ interface {
	isKeyVectorsConfig()
}

type CompanionStruct_KeyVectorsConfig_ struct {
}

var Companion_KeyVectorsConfig_ = CompanionStruct_KeyVectorsConfig_{}

type KeyVectorsConfig_KeyVectorsConfig struct {
	KeyManifestPath _dafny.Sequence
}

func (KeyVectorsConfig_KeyVectorsConfig) isKeyVectorsConfig() {}

func (CompanionStruct_KeyVectorsConfig_) Create_KeyVectorsConfig_(KeyManifestPath _dafny.Sequence) KeyVectorsConfig {
	return KeyVectorsConfig{KeyVectorsConfig_KeyVectorsConfig{KeyManifestPath}}
}

func (_this KeyVectorsConfig) Is_KeyVectorsConfig() bool {
	_, ok := _this.Get_().(KeyVectorsConfig_KeyVectorsConfig)
	return ok
}

func (CompanionStruct_KeyVectorsConfig_) Default() KeyVectorsConfig {
	return Companion_KeyVectorsConfig_.Create_KeyVectorsConfig_(_dafny.EmptySeq.SetString())
}

func (_this KeyVectorsConfig) Dtor_keyManifestPath() _dafny.Sequence {
	return _this.Get_().(KeyVectorsConfig_KeyVectorsConfig).KeyManifestPath
}

func (_this KeyVectorsConfig) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KeyVectorsConfig_KeyVectorsConfig:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig.KeyVectorsConfig" + "(" + _dafny.String(data.KeyManifestPath) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KeyVectorsConfig) Equals(other KeyVectorsConfig) bool {
	switch data1 := _this.Get_().(type) {
	case KeyVectorsConfig_KeyVectorsConfig:
		{
			data2, ok := other.Get_().(KeyVectorsConfig_KeyVectorsConfig)
			return ok && data1.KeyManifestPath.Equals(data2.KeyManifestPath)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KeyVectorsConfig) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KeyVectorsConfig)
	return ok && _this.Equals(typed)
}

func Type_KeyVectorsConfig_() _dafny.TypeDescriptor {
	return type_KeyVectorsConfig_{}
}

type type_KeyVectorsConfig_ struct {
}

func (_this type_KeyVectorsConfig_) Default() interface{} {
	return Companion_KeyVectorsConfig_.Default()
}

func (_this type_KeyVectorsConfig_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig"
}
func (_this KeyVectorsConfig) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KeyVectorsConfig{}

// End of datatype KeyVectorsConfig

// Definition of datatype KmsEcdhKeyring
type KmsEcdhKeyring struct {
	Data_KmsEcdhKeyring_
}

func (_this KmsEcdhKeyring) Get_() Data_KmsEcdhKeyring_ {
	return _this.Data_KmsEcdhKeyring_
}

type Data_KmsEcdhKeyring_ interface {
	isKmsEcdhKeyring()
}

type CompanionStruct_KmsEcdhKeyring_ struct {
}

var Companion_KmsEcdhKeyring_ = CompanionStruct_KmsEcdhKeyring_{}

type KmsEcdhKeyring_KmsEcdhKeyring struct {
	SenderKeyId        _dafny.Sequence
	RecipientKeyId     _dafny.Sequence
	SenderPublicKey    _dafny.Sequence
	RecipientPublicKey _dafny.Sequence
	CurveSpec          _dafny.Sequence
	KeyAgreementScheme _dafny.Sequence
}

func (KmsEcdhKeyring_KmsEcdhKeyring) isKmsEcdhKeyring() {}

func (CompanionStruct_KmsEcdhKeyring_) Create_KmsEcdhKeyring_(SenderKeyId _dafny.Sequence, RecipientKeyId _dafny.Sequence, SenderPublicKey _dafny.Sequence, RecipientPublicKey _dafny.Sequence, CurveSpec _dafny.Sequence, KeyAgreementScheme _dafny.Sequence) KmsEcdhKeyring {
	return KmsEcdhKeyring{KmsEcdhKeyring_KmsEcdhKeyring{SenderKeyId, RecipientKeyId, SenderPublicKey, RecipientPublicKey, CurveSpec, KeyAgreementScheme}}
}

func (_this KmsEcdhKeyring) Is_KmsEcdhKeyring() bool {
	_, ok := _this.Get_().(KmsEcdhKeyring_KmsEcdhKeyring)
	return ok
}

func (CompanionStruct_KmsEcdhKeyring_) Default() KmsEcdhKeyring {
	return Companion_KmsEcdhKeyring_.Create_KmsEcdhKeyring_(_dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString())
}

func (_this KmsEcdhKeyring) Dtor_senderKeyId() _dafny.Sequence {
	return _this.Get_().(KmsEcdhKeyring_KmsEcdhKeyring).SenderKeyId
}

func (_this KmsEcdhKeyring) Dtor_recipientKeyId() _dafny.Sequence {
	return _this.Get_().(KmsEcdhKeyring_KmsEcdhKeyring).RecipientKeyId
}

func (_this KmsEcdhKeyring) Dtor_senderPublicKey() _dafny.Sequence {
	return _this.Get_().(KmsEcdhKeyring_KmsEcdhKeyring).SenderPublicKey
}

func (_this KmsEcdhKeyring) Dtor_recipientPublicKey() _dafny.Sequence {
	return _this.Get_().(KmsEcdhKeyring_KmsEcdhKeyring).RecipientPublicKey
}

func (_this KmsEcdhKeyring) Dtor_curveSpec() _dafny.Sequence {
	return _this.Get_().(KmsEcdhKeyring_KmsEcdhKeyring).CurveSpec
}

func (_this KmsEcdhKeyring) Dtor_keyAgreementScheme() _dafny.Sequence {
	return _this.Get_().(KmsEcdhKeyring_KmsEcdhKeyring).KeyAgreementScheme
}

func (_this KmsEcdhKeyring) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KmsEcdhKeyring_KmsEcdhKeyring:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring.KmsEcdhKeyring" + "(" + _dafny.String(data.SenderKeyId) + ", " + _dafny.String(data.RecipientKeyId) + ", " + _dafny.String(data.SenderPublicKey) + ", " + _dafny.String(data.RecipientPublicKey) + ", " + _dafny.String(data.CurveSpec) + ", " + _dafny.String(data.KeyAgreementScheme) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KmsEcdhKeyring) Equals(other KmsEcdhKeyring) bool {
	switch data1 := _this.Get_().(type) {
	case KmsEcdhKeyring_KmsEcdhKeyring:
		{
			data2, ok := other.Get_().(KmsEcdhKeyring_KmsEcdhKeyring)
			return ok && data1.SenderKeyId.Equals(data2.SenderKeyId) && data1.RecipientKeyId.Equals(data2.RecipientKeyId) && data1.SenderPublicKey.Equals(data2.SenderPublicKey) && data1.RecipientPublicKey.Equals(data2.RecipientPublicKey) && data1.CurveSpec.Equals(data2.CurveSpec) && data1.KeyAgreementScheme.Equals(data2.KeyAgreementScheme)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KmsEcdhKeyring) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KmsEcdhKeyring)
	return ok && _this.Equals(typed)
}

func Type_KmsEcdhKeyring_() _dafny.TypeDescriptor {
	return type_KmsEcdhKeyring_{}
}

type type_KmsEcdhKeyring_ struct {
}

func (_this type_KmsEcdhKeyring_) Default() interface{} {
	return Companion_KmsEcdhKeyring_.Default()
}

func (_this type_KmsEcdhKeyring_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring"
}
func (_this KmsEcdhKeyring) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KmsEcdhKeyring{}

// End of datatype KmsEcdhKeyring

// Definition of datatype KMSInfo
type KMSInfo struct {
	Data_KMSInfo_
}

func (_this KMSInfo) Get_() Data_KMSInfo_ {
	return _this.Data_KMSInfo_
}

type Data_KMSInfo_ interface {
	isKMSInfo()
}

type CompanionStruct_KMSInfo_ struct {
}

var Companion_KMSInfo_ = CompanionStruct_KMSInfo_{}

type KMSInfo_KMSInfo struct {
	KeyId _dafny.Sequence
}

func (KMSInfo_KMSInfo) isKMSInfo() {}

func (CompanionStruct_KMSInfo_) Create_KMSInfo_(KeyId _dafny.Sequence) KMSInfo {
	return KMSInfo{KMSInfo_KMSInfo{KeyId}}
}

func (_this KMSInfo) Is_KMSInfo() bool {
	_, ok := _this.Get_().(KMSInfo_KMSInfo)
	return ok
}

func (CompanionStruct_KMSInfo_) Default() KMSInfo {
	return Companion_KMSInfo_.Create_KMSInfo_(_dafny.EmptySeq.SetString())
}

func (_this KMSInfo) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(KMSInfo_KMSInfo).KeyId
}

func (_this KMSInfo) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KMSInfo_KMSInfo:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo.KMSInfo" + "(" + _dafny.String(data.KeyId) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KMSInfo) Equals(other KMSInfo) bool {
	switch data1 := _this.Get_().(type) {
	case KMSInfo_KMSInfo:
		{
			data2, ok := other.Get_().(KMSInfo_KMSInfo)
			return ok && data1.KeyId.Equals(data2.KeyId)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KMSInfo) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KMSInfo)
	return ok && _this.Equals(typed)
}

func Type_KMSInfo_() _dafny.TypeDescriptor {
	return type_KMSInfo_{}
}

type type_KMSInfo_ struct {
}

func (_this type_KMSInfo_) Default() interface{} {
	return Companion_KMSInfo_.Default()
}

func (_this type_KMSInfo_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo"
}
func (_this KMSInfo) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KMSInfo{}

// End of datatype KMSInfo

// Definition of datatype KmsMrkAware
type KmsMrkAware struct {
	Data_KmsMrkAware_
}

func (_this KmsMrkAware) Get_() Data_KmsMrkAware_ {
	return _this.Data_KmsMrkAware_
}

type Data_KmsMrkAware_ interface {
	isKmsMrkAware()
}

type CompanionStruct_KmsMrkAware_ struct {
}

var Companion_KmsMrkAware_ = CompanionStruct_KmsMrkAware_{}

type KmsMrkAware_KmsMrkAware struct {
	KeyId _dafny.Sequence
}

func (KmsMrkAware_KmsMrkAware) isKmsMrkAware() {}

func (CompanionStruct_KmsMrkAware_) Create_KmsMrkAware_(KeyId _dafny.Sequence) KmsMrkAware {
	return KmsMrkAware{KmsMrkAware_KmsMrkAware{KeyId}}
}

func (_this KmsMrkAware) Is_KmsMrkAware() bool {
	_, ok := _this.Get_().(KmsMrkAware_KmsMrkAware)
	return ok
}

func (CompanionStruct_KmsMrkAware_) Default() KmsMrkAware {
	return Companion_KmsMrkAware_.Create_KmsMrkAware_(_dafny.EmptySeq.SetString())
}

func (_this KmsMrkAware) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(KmsMrkAware_KmsMrkAware).KeyId
}

func (_this KmsMrkAware) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KmsMrkAware_KmsMrkAware:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware.KmsMrkAware" + "(" + _dafny.String(data.KeyId) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KmsMrkAware) Equals(other KmsMrkAware) bool {
	switch data1 := _this.Get_().(type) {
	case KmsMrkAware_KmsMrkAware:
		{
			data2, ok := other.Get_().(KmsMrkAware_KmsMrkAware)
			return ok && data1.KeyId.Equals(data2.KeyId)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KmsMrkAware) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KmsMrkAware)
	return ok && _this.Equals(typed)
}

func Type_KmsMrkAware_() _dafny.TypeDescriptor {
	return type_KmsMrkAware_{}
}

type type_KmsMrkAware_ struct {
}

func (_this type_KmsMrkAware_) Default() interface{} {
	return Companion_KmsMrkAware_.Default()
}

func (_this type_KmsMrkAware_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware"
}
func (_this KmsMrkAware) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KmsMrkAware{}

// End of datatype KmsMrkAware

// Definition of datatype KmsMrkAwareDiscovery
type KmsMrkAwareDiscovery struct {
	Data_KmsMrkAwareDiscovery_
}

func (_this KmsMrkAwareDiscovery) Get_() Data_KmsMrkAwareDiscovery_ {
	return _this.Data_KmsMrkAwareDiscovery_
}

type Data_KmsMrkAwareDiscovery_ interface {
	isKmsMrkAwareDiscovery()
}

type CompanionStruct_KmsMrkAwareDiscovery_ struct {
}

var Companion_KmsMrkAwareDiscovery_ = CompanionStruct_KmsMrkAwareDiscovery_{}

type KmsMrkAwareDiscovery_KmsMrkAwareDiscovery struct {
	KeyId                 _dafny.Sequence
	DefaultMrkRegion      _dafny.Sequence
	AwsKmsDiscoveryFilter m_Wrappers.Option
}

func (KmsMrkAwareDiscovery_KmsMrkAwareDiscovery) isKmsMrkAwareDiscovery() {}

func (CompanionStruct_KmsMrkAwareDiscovery_) Create_KmsMrkAwareDiscovery_(KeyId _dafny.Sequence, DefaultMrkRegion _dafny.Sequence, AwsKmsDiscoveryFilter m_Wrappers.Option) KmsMrkAwareDiscovery {
	return KmsMrkAwareDiscovery{KmsMrkAwareDiscovery_KmsMrkAwareDiscovery{KeyId, DefaultMrkRegion, AwsKmsDiscoveryFilter}}
}

func (_this KmsMrkAwareDiscovery) Is_KmsMrkAwareDiscovery() bool {
	_, ok := _this.Get_().(KmsMrkAwareDiscovery_KmsMrkAwareDiscovery)
	return ok
}

func (CompanionStruct_KmsMrkAwareDiscovery_) Default() KmsMrkAwareDiscovery {
	return Companion_KmsMrkAwareDiscovery_.Create_KmsMrkAwareDiscovery_(_dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), m_Wrappers.Companion_Option_.Default())
}

func (_this KmsMrkAwareDiscovery) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(KmsMrkAwareDiscovery_KmsMrkAwareDiscovery).KeyId
}

func (_this KmsMrkAwareDiscovery) Dtor_defaultMrkRegion() _dafny.Sequence {
	return _this.Get_().(KmsMrkAwareDiscovery_KmsMrkAwareDiscovery).DefaultMrkRegion
}

func (_this KmsMrkAwareDiscovery) Dtor_awsKmsDiscoveryFilter() m_Wrappers.Option {
	return _this.Get_().(KmsMrkAwareDiscovery_KmsMrkAwareDiscovery).AwsKmsDiscoveryFilter
}

func (_this KmsMrkAwareDiscovery) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KmsMrkAwareDiscovery_KmsMrkAwareDiscovery:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery.KmsMrkAwareDiscovery" + "(" + _dafny.String(data.KeyId) + ", " + _dafny.String(data.DefaultMrkRegion) + ", " + _dafny.String(data.AwsKmsDiscoveryFilter) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KmsMrkAwareDiscovery) Equals(other KmsMrkAwareDiscovery) bool {
	switch data1 := _this.Get_().(type) {
	case KmsMrkAwareDiscovery_KmsMrkAwareDiscovery:
		{
			data2, ok := other.Get_().(KmsMrkAwareDiscovery_KmsMrkAwareDiscovery)
			return ok && data1.KeyId.Equals(data2.KeyId) && data1.DefaultMrkRegion.Equals(data2.DefaultMrkRegion) && data1.AwsKmsDiscoveryFilter.Equals(data2.AwsKmsDiscoveryFilter)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KmsMrkAwareDiscovery) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KmsMrkAwareDiscovery)
	return ok && _this.Equals(typed)
}

func Type_KmsMrkAwareDiscovery_() _dafny.TypeDescriptor {
	return type_KmsMrkAwareDiscovery_{}
}

type type_KmsMrkAwareDiscovery_ struct {
}

func (_this type_KmsMrkAwareDiscovery_) Default() interface{} {
	return Companion_KmsMrkAwareDiscovery_.Default()
}

func (_this type_KmsMrkAwareDiscovery_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery"
}
func (_this KmsMrkAwareDiscovery) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KmsMrkAwareDiscovery{}

// End of datatype KmsMrkAwareDiscovery

// Definition of datatype KmsRsaKeyring
type KmsRsaKeyring struct {
	Data_KmsRsaKeyring_
}

func (_this KmsRsaKeyring) Get_() Data_KmsRsaKeyring_ {
	return _this.Data_KmsRsaKeyring_
}

type Data_KmsRsaKeyring_ interface {
	isKmsRsaKeyring()
}

type CompanionStruct_KmsRsaKeyring_ struct {
}

var Companion_KmsRsaKeyring_ = CompanionStruct_KmsRsaKeyring_{}

type KmsRsaKeyring_KmsRsaKeyring struct {
	KeyId               _dafny.Sequence
	EncryptionAlgorithm m_ComAmazonawsKmsTypes.EncryptionAlgorithmSpec
}

func (KmsRsaKeyring_KmsRsaKeyring) isKmsRsaKeyring() {}

func (CompanionStruct_KmsRsaKeyring_) Create_KmsRsaKeyring_(KeyId _dafny.Sequence, EncryptionAlgorithm m_ComAmazonawsKmsTypes.EncryptionAlgorithmSpec) KmsRsaKeyring {
	return KmsRsaKeyring{KmsRsaKeyring_KmsRsaKeyring{KeyId, EncryptionAlgorithm}}
}

func (_this KmsRsaKeyring) Is_KmsRsaKeyring() bool {
	_, ok := _this.Get_().(KmsRsaKeyring_KmsRsaKeyring)
	return ok
}

func (CompanionStruct_KmsRsaKeyring_) Default() KmsRsaKeyring {
	return Companion_KmsRsaKeyring_.Create_KmsRsaKeyring_(_dafny.EmptySeq.SetString(), m_ComAmazonawsKmsTypes.Companion_EncryptionAlgorithmSpec_.Default())
}

func (_this KmsRsaKeyring) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(KmsRsaKeyring_KmsRsaKeyring).KeyId
}

func (_this KmsRsaKeyring) Dtor_encryptionAlgorithm() m_ComAmazonawsKmsTypes.EncryptionAlgorithmSpec {
	return _this.Get_().(KmsRsaKeyring_KmsRsaKeyring).EncryptionAlgorithm
}

func (_this KmsRsaKeyring) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KmsRsaKeyring_KmsRsaKeyring:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring.KmsRsaKeyring" + "(" + _dafny.String(data.KeyId) + ", " + _dafny.String(data.EncryptionAlgorithm) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KmsRsaKeyring) Equals(other KmsRsaKeyring) bool {
	switch data1 := _this.Get_().(type) {
	case KmsRsaKeyring_KmsRsaKeyring:
		{
			data2, ok := other.Get_().(KmsRsaKeyring_KmsRsaKeyring)
			return ok && data1.KeyId.Equals(data2.KeyId) && data1.EncryptionAlgorithm.Equals(data2.EncryptionAlgorithm)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KmsRsaKeyring) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KmsRsaKeyring)
	return ok && _this.Equals(typed)
}

func Type_KmsRsaKeyring_() _dafny.TypeDescriptor {
	return type_KmsRsaKeyring_{}
}

type type_KmsRsaKeyring_ struct {
}

func (_this type_KmsRsaKeyring_) Default() interface{} {
	return Companion_KmsRsaKeyring_.Default()
}

func (_this type_KmsRsaKeyring_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring"
}
func (_this KmsRsaKeyring) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KmsRsaKeyring{}

// End of datatype KmsRsaKeyring

// Definition of datatype MultiKeyring
type MultiKeyring struct {
	Data_MultiKeyring_
}

func (_this MultiKeyring) Get_() Data_MultiKeyring_ {
	return _this.Data_MultiKeyring_
}

type Data_MultiKeyring_ interface {
	isMultiKeyring()
}

type CompanionStruct_MultiKeyring_ struct {
}

var Companion_MultiKeyring_ = CompanionStruct_MultiKeyring_{}

type MultiKeyring_MultiKeyring struct {
	Generator     m_Wrappers.Option
	ChildKeyrings _dafny.Sequence
}

func (MultiKeyring_MultiKeyring) isMultiKeyring() {}

func (CompanionStruct_MultiKeyring_) Create_MultiKeyring_(Generator m_Wrappers.Option, ChildKeyrings _dafny.Sequence) MultiKeyring {
	return MultiKeyring{MultiKeyring_MultiKeyring{Generator, ChildKeyrings}}
}

func (_this MultiKeyring) Is_MultiKeyring() bool {
	_, ok := _this.Get_().(MultiKeyring_MultiKeyring)
	return ok
}

func (CompanionStruct_MultiKeyring_) Default() MultiKeyring {
	return Companion_MultiKeyring_.Create_MultiKeyring_(m_Wrappers.Companion_Option_.Default(), _dafny.EmptySeq)
}

func (_this MultiKeyring) Dtor_generator() m_Wrappers.Option {
	return _this.Get_().(MultiKeyring_MultiKeyring).Generator
}

func (_this MultiKeyring) Dtor_childKeyrings() _dafny.Sequence {
	return _this.Get_().(MultiKeyring_MultiKeyring).ChildKeyrings
}

func (_this MultiKeyring) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case MultiKeyring_MultiKeyring:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring.MultiKeyring" + "(" + _dafny.String(data.Generator) + ", " + _dafny.String(data.ChildKeyrings) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this MultiKeyring) Equals(other MultiKeyring) bool {
	switch data1 := _this.Get_().(type) {
	case MultiKeyring_MultiKeyring:
		{
			data2, ok := other.Get_().(MultiKeyring_MultiKeyring)
			return ok && data1.Generator.Equals(data2.Generator) && data1.ChildKeyrings.Equals(data2.ChildKeyrings)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this MultiKeyring) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(MultiKeyring)
	return ok && _this.Equals(typed)
}

func Type_MultiKeyring_() _dafny.TypeDescriptor {
	return type_MultiKeyring_{}
}

type type_MultiKeyring_ struct {
}

func (_this type_MultiKeyring_) Default() interface{} {
	return Companion_MultiKeyring_.Default()
}

func (_this type_MultiKeyring_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring"
}
func (_this MultiKeyring) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = MultiKeyring{}

// End of datatype MultiKeyring

// Definition of datatype RawAES
type RawAES struct {
	Data_RawAES_
}

func (_this RawAES) Get_() Data_RawAES_ {
	return _this.Data_RawAES_
}

type Data_RawAES_ interface {
	isRawAES()
}

type CompanionStruct_RawAES_ struct {
}

var Companion_RawAES_ = CompanionStruct_RawAES_{}

type RawAES_RawAES struct {
	KeyId      _dafny.Sequence
	ProviderId _dafny.Sequence
}

func (RawAES_RawAES) isRawAES() {}

func (CompanionStruct_RawAES_) Create_RawAES_(KeyId _dafny.Sequence, ProviderId _dafny.Sequence) RawAES {
	return RawAES{RawAES_RawAES{KeyId, ProviderId}}
}

func (_this RawAES) Is_RawAES() bool {
	_, ok := _this.Get_().(RawAES_RawAES)
	return ok
}

func (CompanionStruct_RawAES_) Default() RawAES {
	return Companion_RawAES_.Create_RawAES_(_dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString())
}

func (_this RawAES) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(RawAES_RawAES).KeyId
}

func (_this RawAES) Dtor_providerId() _dafny.Sequence {
	return _this.Get_().(RawAES_RawAES).ProviderId
}

func (_this RawAES) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case RawAES_RawAES:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES.RawAES" + "(" + _dafny.String(data.KeyId) + ", " + _dafny.String(data.ProviderId) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this RawAES) Equals(other RawAES) bool {
	switch data1 := _this.Get_().(type) {
	case RawAES_RawAES:
		{
			data2, ok := other.Get_().(RawAES_RawAES)
			return ok && data1.KeyId.Equals(data2.KeyId) && data1.ProviderId.Equals(data2.ProviderId)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this RawAES) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(RawAES)
	return ok && _this.Equals(typed)
}

func Type_RawAES_() _dafny.TypeDescriptor {
	return type_RawAES_{}
}

type type_RawAES_ struct {
}

func (_this type_RawAES_) Default() interface{} {
	return Companion_RawAES_.Default()
}

func (_this type_RawAES_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES"
}
func (_this RawAES) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = RawAES{}

// End of datatype RawAES

// Definition of datatype RawEcdh
type RawEcdh struct {
	Data_RawEcdh_
}

func (_this RawEcdh) Get_() Data_RawEcdh_ {
	return _this.Data_RawEcdh_
}

type Data_RawEcdh_ interface {
	isRawEcdh()
}

type CompanionStruct_RawEcdh_ struct {
}

var Companion_RawEcdh_ = CompanionStruct_RawEcdh_{}

type RawEcdh_RawEcdh struct {
	SenderKeyId        _dafny.Sequence
	RecipientKeyId     _dafny.Sequence
	SenderPublicKey    _dafny.Sequence
	RecipientPublicKey _dafny.Sequence
	ProviderId         _dafny.Sequence
	CurveSpec          _dafny.Sequence
	KeyAgreementScheme _dafny.Sequence
}

func (RawEcdh_RawEcdh) isRawEcdh() {}

func (CompanionStruct_RawEcdh_) Create_RawEcdh_(SenderKeyId _dafny.Sequence, RecipientKeyId _dafny.Sequence, SenderPublicKey _dafny.Sequence, RecipientPublicKey _dafny.Sequence, ProviderId _dafny.Sequence, CurveSpec _dafny.Sequence, KeyAgreementScheme _dafny.Sequence) RawEcdh {
	return RawEcdh{RawEcdh_RawEcdh{SenderKeyId, RecipientKeyId, SenderPublicKey, RecipientPublicKey, ProviderId, CurveSpec, KeyAgreementScheme}}
}

func (_this RawEcdh) Is_RawEcdh() bool {
	_, ok := _this.Get_().(RawEcdh_RawEcdh)
	return ok
}

func (CompanionStruct_RawEcdh_) Default() RawEcdh {
	return Companion_RawEcdh_.Create_RawEcdh_(_dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString())
}

func (_this RawEcdh) Dtor_senderKeyId() _dafny.Sequence {
	return _this.Get_().(RawEcdh_RawEcdh).SenderKeyId
}

func (_this RawEcdh) Dtor_recipientKeyId() _dafny.Sequence {
	return _this.Get_().(RawEcdh_RawEcdh).RecipientKeyId
}

func (_this RawEcdh) Dtor_senderPublicKey() _dafny.Sequence {
	return _this.Get_().(RawEcdh_RawEcdh).SenderPublicKey
}

func (_this RawEcdh) Dtor_recipientPublicKey() _dafny.Sequence {
	return _this.Get_().(RawEcdh_RawEcdh).RecipientPublicKey
}

func (_this RawEcdh) Dtor_providerId() _dafny.Sequence {
	return _this.Get_().(RawEcdh_RawEcdh).ProviderId
}

func (_this RawEcdh) Dtor_curveSpec() _dafny.Sequence {
	return _this.Get_().(RawEcdh_RawEcdh).CurveSpec
}

func (_this RawEcdh) Dtor_keyAgreementScheme() _dafny.Sequence {
	return _this.Get_().(RawEcdh_RawEcdh).KeyAgreementScheme
}

func (_this RawEcdh) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case RawEcdh_RawEcdh:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh.RawEcdh" + "(" + _dafny.String(data.SenderKeyId) + ", " + _dafny.String(data.RecipientKeyId) + ", " + _dafny.String(data.SenderPublicKey) + ", " + _dafny.String(data.RecipientPublicKey) + ", " + _dafny.String(data.ProviderId) + ", " + _dafny.String(data.CurveSpec) + ", " + _dafny.String(data.KeyAgreementScheme) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this RawEcdh) Equals(other RawEcdh) bool {
	switch data1 := _this.Get_().(type) {
	case RawEcdh_RawEcdh:
		{
			data2, ok := other.Get_().(RawEcdh_RawEcdh)
			return ok && data1.SenderKeyId.Equals(data2.SenderKeyId) && data1.RecipientKeyId.Equals(data2.RecipientKeyId) && data1.SenderPublicKey.Equals(data2.SenderPublicKey) && data1.RecipientPublicKey.Equals(data2.RecipientPublicKey) && data1.ProviderId.Equals(data2.ProviderId) && data1.CurveSpec.Equals(data2.CurveSpec) && data1.KeyAgreementScheme.Equals(data2.KeyAgreementScheme)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this RawEcdh) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(RawEcdh)
	return ok && _this.Equals(typed)
}

func Type_RawEcdh_() _dafny.TypeDescriptor {
	return type_RawEcdh_{}
}

type type_RawEcdh_ struct {
}

func (_this type_RawEcdh_) Default() interface{} {
	return Companion_RawEcdh_.Default()
}

func (_this type_RawEcdh_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh"
}
func (_this RawEcdh) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = RawEcdh{}

// End of datatype RawEcdh

// Definition of datatype RawRSA
type RawRSA struct {
	Data_RawRSA_
}

func (_this RawRSA) Get_() Data_RawRSA_ {
	return _this.Data_RawRSA_
}

type Data_RawRSA_ interface {
	isRawRSA()
}

type CompanionStruct_RawRSA_ struct {
}

var Companion_RawRSA_ = CompanionStruct_RawRSA_{}

type RawRSA_RawRSA struct {
	KeyId      _dafny.Sequence
	ProviderId _dafny.Sequence
	Padding    m_AwsCryptographyMaterialProvidersTypes.PaddingScheme
}

func (RawRSA_RawRSA) isRawRSA() {}

func (CompanionStruct_RawRSA_) Create_RawRSA_(KeyId _dafny.Sequence, ProviderId _dafny.Sequence, Padding m_AwsCryptographyMaterialProvidersTypes.PaddingScheme) RawRSA {
	return RawRSA{RawRSA_RawRSA{KeyId, ProviderId, Padding}}
}

func (_this RawRSA) Is_RawRSA() bool {
	_, ok := _this.Get_().(RawRSA_RawRSA)
	return ok
}

func (CompanionStruct_RawRSA_) Default() RawRSA {
	return Companion_RawRSA_.Create_RawRSA_(_dafny.EmptySeq.SetString(), _dafny.EmptySeq.SetString(), m_AwsCryptographyMaterialProvidersTypes.Companion_PaddingScheme_.Default())
}

func (_this RawRSA) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(RawRSA_RawRSA).KeyId
}

func (_this RawRSA) Dtor_providerId() _dafny.Sequence {
	return _this.Get_().(RawRSA_RawRSA).ProviderId
}

func (_this RawRSA) Dtor_padding() m_AwsCryptographyMaterialProvidersTypes.PaddingScheme {
	return _this.Get_().(RawRSA_RawRSA).Padding
}

func (_this RawRSA) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case RawRSA_RawRSA:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA.RawRSA" + "(" + _dafny.String(data.KeyId) + ", " + _dafny.String(data.ProviderId) + ", " + _dafny.String(data.Padding) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this RawRSA) Equals(other RawRSA) bool {
	switch data1 := _this.Get_().(type) {
	case RawRSA_RawRSA:
		{
			data2, ok := other.Get_().(RawRSA_RawRSA)
			return ok && data1.KeyId.Equals(data2.KeyId) && data1.ProviderId.Equals(data2.ProviderId) && data1.Padding.Equals(data2.Padding)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this RawRSA) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(RawRSA)
	return ok && _this.Equals(typed)
}

func Type_RawRSA_() _dafny.TypeDescriptor {
	return type_RawRSA_{}
}

type type_RawRSA_ struct {
}

func (_this type_RawRSA_) Default() interface{} {
	return Companion_RawRSA_.Default()
}

func (_this type_RawRSA_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA"
}
func (_this RawRSA) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = RawRSA{}

// End of datatype RawRSA

// Definition of datatype RequiredEncryptionContextCMM
type RequiredEncryptionContextCMM struct {
	Data_RequiredEncryptionContextCMM_
}

func (_this RequiredEncryptionContextCMM) Get_() Data_RequiredEncryptionContextCMM_ {
	return _this.Data_RequiredEncryptionContextCMM_
}

type Data_RequiredEncryptionContextCMM_ interface {
	isRequiredEncryptionContextCMM()
}

type CompanionStruct_RequiredEncryptionContextCMM_ struct {
}

var Companion_RequiredEncryptionContextCMM_ = CompanionStruct_RequiredEncryptionContextCMM_{}

type RequiredEncryptionContextCMM_RequiredEncryptionContextCMM struct {
	Underlying                    KeyDescription
	RequiredEncryptionContextKeys _dafny.Sequence
}

func (RequiredEncryptionContextCMM_RequiredEncryptionContextCMM) isRequiredEncryptionContextCMM() {}

func (CompanionStruct_RequiredEncryptionContextCMM_) Create_RequiredEncryptionContextCMM_(Underlying KeyDescription, RequiredEncryptionContextKeys _dafny.Sequence) RequiredEncryptionContextCMM {
	return RequiredEncryptionContextCMM{RequiredEncryptionContextCMM_RequiredEncryptionContextCMM{Underlying, RequiredEncryptionContextKeys}}
}

func (_this RequiredEncryptionContextCMM) Is_RequiredEncryptionContextCMM() bool {
	_, ok := _this.Get_().(RequiredEncryptionContextCMM_RequiredEncryptionContextCMM)
	return ok
}

func (CompanionStruct_RequiredEncryptionContextCMM_) Default() RequiredEncryptionContextCMM {
	return Companion_RequiredEncryptionContextCMM_.Create_RequiredEncryptionContextCMM_(Companion_KeyDescription_.Default(), _dafny.EmptySeq)
}

func (_this RequiredEncryptionContextCMM) Dtor_underlying() KeyDescription {
	return _this.Get_().(RequiredEncryptionContextCMM_RequiredEncryptionContextCMM).Underlying
}

func (_this RequiredEncryptionContextCMM) Dtor_requiredEncryptionContextKeys() _dafny.Sequence {
	return _this.Get_().(RequiredEncryptionContextCMM_RequiredEncryptionContextCMM).RequiredEncryptionContextKeys
}

func (_this RequiredEncryptionContextCMM) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case RequiredEncryptionContextCMM_RequiredEncryptionContextCMM:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM.RequiredEncryptionContextCMM" + "(" + _dafny.String(data.Underlying) + ", " + _dafny.String(data.RequiredEncryptionContextKeys) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this RequiredEncryptionContextCMM) Equals(other RequiredEncryptionContextCMM) bool {
	switch data1 := _this.Get_().(type) {
	case RequiredEncryptionContextCMM_RequiredEncryptionContextCMM:
		{
			data2, ok := other.Get_().(RequiredEncryptionContextCMM_RequiredEncryptionContextCMM)
			return ok && data1.Underlying.Equals(data2.Underlying) && data1.RequiredEncryptionContextKeys.Equals(data2.RequiredEncryptionContextKeys)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this RequiredEncryptionContextCMM) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(RequiredEncryptionContextCMM)
	return ok && _this.Equals(typed)
}

func Type_RequiredEncryptionContextCMM_() _dafny.TypeDescriptor {
	return type_RequiredEncryptionContextCMM_{}
}

type type_RequiredEncryptionContextCMM_ struct {
}

func (_this type_RequiredEncryptionContextCMM_) Default() interface{} {
	return Companion_RequiredEncryptionContextCMM_.Default()
}

func (_this type_RequiredEncryptionContextCMM_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM"
}
func (_this RequiredEncryptionContextCMM) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = RequiredEncryptionContextCMM{}

// End of datatype RequiredEncryptionContextCMM

// Definition of datatype SerializeKeyDescriptionInput
type SerializeKeyDescriptionInput struct {
	Data_SerializeKeyDescriptionInput_
}

func (_this SerializeKeyDescriptionInput) Get_() Data_SerializeKeyDescriptionInput_ {
	return _this.Data_SerializeKeyDescriptionInput_
}

type Data_SerializeKeyDescriptionInput_ interface {
	isSerializeKeyDescriptionInput()
}

type CompanionStruct_SerializeKeyDescriptionInput_ struct {
}

var Companion_SerializeKeyDescriptionInput_ = CompanionStruct_SerializeKeyDescriptionInput_{}

type SerializeKeyDescriptionInput_SerializeKeyDescriptionInput struct {
	KeyDescription KeyDescription
}

func (SerializeKeyDescriptionInput_SerializeKeyDescriptionInput) isSerializeKeyDescriptionInput() {}

func (CompanionStruct_SerializeKeyDescriptionInput_) Create_SerializeKeyDescriptionInput_(KeyDescription KeyDescription) SerializeKeyDescriptionInput {
	return SerializeKeyDescriptionInput{SerializeKeyDescriptionInput_SerializeKeyDescriptionInput{KeyDescription}}
}

func (_this SerializeKeyDescriptionInput) Is_SerializeKeyDescriptionInput() bool {
	_, ok := _this.Get_().(SerializeKeyDescriptionInput_SerializeKeyDescriptionInput)
	return ok
}

func (CompanionStruct_SerializeKeyDescriptionInput_) Default() SerializeKeyDescriptionInput {
	return Companion_SerializeKeyDescriptionInput_.Create_SerializeKeyDescriptionInput_(Companion_KeyDescription_.Default())
}

func (_this SerializeKeyDescriptionInput) Dtor_keyDescription() KeyDescription {
	return _this.Get_().(SerializeKeyDescriptionInput_SerializeKeyDescriptionInput).KeyDescription
}

func (_this SerializeKeyDescriptionInput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case SerializeKeyDescriptionInput_SerializeKeyDescriptionInput:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionInput.SerializeKeyDescriptionInput" + "(" + _dafny.String(data.KeyDescription) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this SerializeKeyDescriptionInput) Equals(other SerializeKeyDescriptionInput) bool {
	switch data1 := _this.Get_().(type) {
	case SerializeKeyDescriptionInput_SerializeKeyDescriptionInput:
		{
			data2, ok := other.Get_().(SerializeKeyDescriptionInput_SerializeKeyDescriptionInput)
			return ok && data1.KeyDescription.Equals(data2.KeyDescription)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this SerializeKeyDescriptionInput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(SerializeKeyDescriptionInput)
	return ok && _this.Equals(typed)
}

func Type_SerializeKeyDescriptionInput_() _dafny.TypeDescriptor {
	return type_SerializeKeyDescriptionInput_{}
}

type type_SerializeKeyDescriptionInput_ struct {
}

func (_this type_SerializeKeyDescriptionInput_) Default() interface{} {
	return Companion_SerializeKeyDescriptionInput_.Default()
}

func (_this type_SerializeKeyDescriptionInput_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionInput"
}
func (_this SerializeKeyDescriptionInput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = SerializeKeyDescriptionInput{}

// End of datatype SerializeKeyDescriptionInput

// Definition of datatype SerializeKeyDescriptionOutput
type SerializeKeyDescriptionOutput struct {
	Data_SerializeKeyDescriptionOutput_
}

func (_this SerializeKeyDescriptionOutput) Get_() Data_SerializeKeyDescriptionOutput_ {
	return _this.Data_SerializeKeyDescriptionOutput_
}

type Data_SerializeKeyDescriptionOutput_ interface {
	isSerializeKeyDescriptionOutput()
}

type CompanionStruct_SerializeKeyDescriptionOutput_ struct {
}

var Companion_SerializeKeyDescriptionOutput_ = CompanionStruct_SerializeKeyDescriptionOutput_{}

type SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput struct {
	Json _dafny.Sequence
}

func (SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput) isSerializeKeyDescriptionOutput() {
}

func (CompanionStruct_SerializeKeyDescriptionOutput_) Create_SerializeKeyDescriptionOutput_(Json _dafny.Sequence) SerializeKeyDescriptionOutput {
	return SerializeKeyDescriptionOutput{SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput{Json}}
}

func (_this SerializeKeyDescriptionOutput) Is_SerializeKeyDescriptionOutput() bool {
	_, ok := _this.Get_().(SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput)
	return ok
}

func (CompanionStruct_SerializeKeyDescriptionOutput_) Default() SerializeKeyDescriptionOutput {
	return Companion_SerializeKeyDescriptionOutput_.Create_SerializeKeyDescriptionOutput_(_dafny.EmptySeq)
}

func (_this SerializeKeyDescriptionOutput) Dtor_json() _dafny.Sequence {
	return _this.Get_().(SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput).Json
}

func (_this SerializeKeyDescriptionOutput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput.SerializeKeyDescriptionOutput" + "(" + _dafny.String(data.Json) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this SerializeKeyDescriptionOutput) Equals(other SerializeKeyDescriptionOutput) bool {
	switch data1 := _this.Get_().(type) {
	case SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput:
		{
			data2, ok := other.Get_().(SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput)
			return ok && data1.Json.Equals(data2.Json)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this SerializeKeyDescriptionOutput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(SerializeKeyDescriptionOutput)
	return ok && _this.Equals(typed)
}

func Type_SerializeKeyDescriptionOutput_() _dafny.TypeDescriptor {
	return type_SerializeKeyDescriptionOutput_{}
}

type type_SerializeKeyDescriptionOutput_ struct {
}

func (_this type_SerializeKeyDescriptionOutput_) Default() interface{} {
	return Companion_SerializeKeyDescriptionOutput_.Default()
}

func (_this type_SerializeKeyDescriptionOutput_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput"
}
func (_this SerializeKeyDescriptionOutput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = SerializeKeyDescriptionOutput{}

// End of datatype SerializeKeyDescriptionOutput

// Definition of datatype StaticKeyring
type StaticKeyring struct {
	Data_StaticKeyring_
}

func (_this StaticKeyring) Get_() Data_StaticKeyring_ {
	return _this.Data_StaticKeyring_
}

type Data_StaticKeyring_ interface {
	isStaticKeyring()
}

type CompanionStruct_StaticKeyring_ struct {
}

var Companion_StaticKeyring_ = CompanionStruct_StaticKeyring_{}

type StaticKeyring_StaticKeyring struct {
	KeyId _dafny.Sequence
}

func (StaticKeyring_StaticKeyring) isStaticKeyring() {}

func (CompanionStruct_StaticKeyring_) Create_StaticKeyring_(KeyId _dafny.Sequence) StaticKeyring {
	return StaticKeyring{StaticKeyring_StaticKeyring{KeyId}}
}

func (_this StaticKeyring) Is_StaticKeyring() bool {
	_, ok := _this.Get_().(StaticKeyring_StaticKeyring)
	return ok
}

func (CompanionStruct_StaticKeyring_) Default() StaticKeyring {
	return Companion_StaticKeyring_.Create_StaticKeyring_(_dafny.EmptySeq.SetString())
}

func (_this StaticKeyring) Dtor_keyId() _dafny.Sequence {
	return _this.Get_().(StaticKeyring_StaticKeyring).KeyId
}

func (_this StaticKeyring) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case StaticKeyring_StaticKeyring:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring.StaticKeyring" + "(" + _dafny.String(data.KeyId) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this StaticKeyring) Equals(other StaticKeyring) bool {
	switch data1 := _this.Get_().(type) {
	case StaticKeyring_StaticKeyring:
		{
			data2, ok := other.Get_().(StaticKeyring_StaticKeyring)
			return ok && data1.KeyId.Equals(data2.KeyId)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this StaticKeyring) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(StaticKeyring)
	return ok && _this.Equals(typed)
}

func Type_StaticKeyring_() _dafny.TypeDescriptor {
	return type_StaticKeyring_{}
}

type type_StaticKeyring_ struct {
}

func (_this type_StaticKeyring_) Default() interface{} {
	return Companion_StaticKeyring_.Default()
}

func (_this type_StaticKeyring_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring"
}
func (_this StaticKeyring) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = StaticKeyring{}

// End of datatype StaticKeyring

// Definition of datatype TestVectorCmmInput
type TestVectorCmmInput struct {
	Data_TestVectorCmmInput_
}

func (_this TestVectorCmmInput) Get_() Data_TestVectorCmmInput_ {
	return _this.Data_TestVectorCmmInput_
}

type Data_TestVectorCmmInput_ interface {
	isTestVectorCmmInput()
}

type CompanionStruct_TestVectorCmmInput_ struct {
}

var Companion_TestVectorCmmInput_ = CompanionStruct_TestVectorCmmInput_{}

type TestVectorCmmInput_TestVectorCmmInput struct {
	KeyDescription KeyDescription
	ForOperation   CmmOperation
}

func (TestVectorCmmInput_TestVectorCmmInput) isTestVectorCmmInput() {}

func (CompanionStruct_TestVectorCmmInput_) Create_TestVectorCmmInput_(KeyDescription KeyDescription, ForOperation CmmOperation) TestVectorCmmInput {
	return TestVectorCmmInput{TestVectorCmmInput_TestVectorCmmInput{KeyDescription, ForOperation}}
}

func (_this TestVectorCmmInput) Is_TestVectorCmmInput() bool {
	_, ok := _this.Get_().(TestVectorCmmInput_TestVectorCmmInput)
	return ok
}

func (CompanionStruct_TestVectorCmmInput_) Default() TestVectorCmmInput {
	return Companion_TestVectorCmmInput_.Create_TestVectorCmmInput_(Companion_KeyDescription_.Default(), Companion_CmmOperation_.Default())
}

func (_this TestVectorCmmInput) Dtor_keyDescription() KeyDescription {
	return _this.Get_().(TestVectorCmmInput_TestVectorCmmInput).KeyDescription
}

func (_this TestVectorCmmInput) Dtor_forOperation() CmmOperation {
	return _this.Get_().(TestVectorCmmInput_TestVectorCmmInput).ForOperation
}

func (_this TestVectorCmmInput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case TestVectorCmmInput_TestVectorCmmInput:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput.TestVectorCmmInput" + "(" + _dafny.String(data.KeyDescription) + ", " + _dafny.String(data.ForOperation) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this TestVectorCmmInput) Equals(other TestVectorCmmInput) bool {
	switch data1 := _this.Get_().(type) {
	case TestVectorCmmInput_TestVectorCmmInput:
		{
			data2, ok := other.Get_().(TestVectorCmmInput_TestVectorCmmInput)
			return ok && data1.KeyDescription.Equals(data2.KeyDescription) && data1.ForOperation.Equals(data2.ForOperation)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this TestVectorCmmInput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(TestVectorCmmInput)
	return ok && _this.Equals(typed)
}

func Type_TestVectorCmmInput_() _dafny.TypeDescriptor {
	return type_TestVectorCmmInput_{}
}

type type_TestVectorCmmInput_ struct {
}

func (_this type_TestVectorCmmInput_) Default() interface{} {
	return Companion_TestVectorCmmInput_.Default()
}

func (_this type_TestVectorCmmInput_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput"
}
func (_this TestVectorCmmInput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = TestVectorCmmInput{}

// End of datatype TestVectorCmmInput

// Definition of datatype TestVectorKeyringInput
type TestVectorKeyringInput struct {
	Data_TestVectorKeyringInput_
}

func (_this TestVectorKeyringInput) Get_() Data_TestVectorKeyringInput_ {
	return _this.Data_TestVectorKeyringInput_
}

type Data_TestVectorKeyringInput_ interface {
	isTestVectorKeyringInput()
}

type CompanionStruct_TestVectorKeyringInput_ struct {
}

var Companion_TestVectorKeyringInput_ = CompanionStruct_TestVectorKeyringInput_{}

type TestVectorKeyringInput_TestVectorKeyringInput struct {
	KeyDescription KeyDescription
}

func (TestVectorKeyringInput_TestVectorKeyringInput) isTestVectorKeyringInput() {}

func (CompanionStruct_TestVectorKeyringInput_) Create_TestVectorKeyringInput_(KeyDescription KeyDescription) TestVectorKeyringInput {
	return TestVectorKeyringInput{TestVectorKeyringInput_TestVectorKeyringInput{KeyDescription}}
}

func (_this TestVectorKeyringInput) Is_TestVectorKeyringInput() bool {
	_, ok := _this.Get_().(TestVectorKeyringInput_TestVectorKeyringInput)
	return ok
}

func (CompanionStruct_TestVectorKeyringInput_) Default() TestVectorKeyringInput {
	return Companion_TestVectorKeyringInput_.Create_TestVectorKeyringInput_(Companion_KeyDescription_.Default())
}

func (_this TestVectorKeyringInput) Dtor_keyDescription() KeyDescription {
	return _this.Get_().(TestVectorKeyringInput_TestVectorKeyringInput).KeyDescription
}

func (_this TestVectorKeyringInput) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case TestVectorKeyringInput_TestVectorKeyringInput:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorKeyringInput.TestVectorKeyringInput" + "(" + _dafny.String(data.KeyDescription) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this TestVectorKeyringInput) Equals(other TestVectorKeyringInput) bool {
	switch data1 := _this.Get_().(type) {
	case TestVectorKeyringInput_TestVectorKeyringInput:
		{
			data2, ok := other.Get_().(TestVectorKeyringInput_TestVectorKeyringInput)
			return ok && data1.KeyDescription.Equals(data2.KeyDescription)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this TestVectorKeyringInput) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(TestVectorKeyringInput)
	return ok && _this.Equals(typed)
}

func Type_TestVectorKeyringInput_() _dafny.TypeDescriptor {
	return type_TestVectorKeyringInput_{}
}

type type_TestVectorKeyringInput_ struct {
}

func (_this type_TestVectorKeyringInput_) Default() interface{} {
	return Companion_TestVectorKeyringInput_.Default()
}

func (_this type_TestVectorKeyringInput_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorKeyringInput"
}
func (_this TestVectorKeyringInput) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = TestVectorKeyringInput{}

// End of datatype TestVectorKeyringInput

// Definition of datatype Error
type Error struct {
	Data_Error_
}

func (_this Error) Get_() Data_Error_ {
	return _this.Data_Error_
}

type Data_Error_ interface {
	isError()
}

type CompanionStruct_Error_ struct {
}

var Companion_Error_ = CompanionStruct_Error_{}

type Error_KeyVectorException struct {
	Message _dafny.Sequence
}

func (Error_KeyVectorException) isError() {}

func (CompanionStruct_Error_) Create_KeyVectorException_(Message _dafny.Sequence) Error {
	return Error{Error_KeyVectorException{Message}}
}

func (_this Error) Is_KeyVectorException() bool {
	_, ok := _this.Get_().(Error_KeyVectorException)
	return ok
}

type Error_AwsCryptographyMaterialProviders struct {
	AwsCryptographyMaterialProviders m_AwsCryptographyMaterialProvidersTypes.Error
}

func (Error_AwsCryptographyMaterialProviders) isError() {}

func (CompanionStruct_Error_) Create_AwsCryptographyMaterialProviders_(AwsCryptographyMaterialProviders m_AwsCryptographyMaterialProvidersTypes.Error) Error {
	return Error{Error_AwsCryptographyMaterialProviders{AwsCryptographyMaterialProviders}}
}

func (_this Error) Is_AwsCryptographyMaterialProviders() bool {
	_, ok := _this.Get_().(Error_AwsCryptographyMaterialProviders)
	return ok
}

type Error_ComAmazonawsKms struct {
	ComAmazonawsKms m_ComAmazonawsKmsTypes.Error
}

func (Error_ComAmazonawsKms) isError() {}

func (CompanionStruct_Error_) Create_ComAmazonawsKms_(ComAmazonawsKms m_ComAmazonawsKmsTypes.Error) Error {
	return Error{Error_ComAmazonawsKms{ComAmazonawsKms}}
}

func (_this Error) Is_ComAmazonawsKms() bool {
	_, ok := _this.Get_().(Error_ComAmazonawsKms)
	return ok
}

type Error_CollectionOfErrors struct {
	List    _dafny.Sequence
	Message _dafny.Sequence
}

func (Error_CollectionOfErrors) isError() {}

func (CompanionStruct_Error_) Create_CollectionOfErrors_(List _dafny.Sequence, Message _dafny.Sequence) Error {
	return Error{Error_CollectionOfErrors{List, Message}}
}

func (_this Error) Is_CollectionOfErrors() bool {
	_, ok := _this.Get_().(Error_CollectionOfErrors)
	return ok
}

type Error_Opaque struct {
	Obj interface{}
}

func (Error_Opaque) isError() {}

func (CompanionStruct_Error_) Create_Opaque_(Obj interface{}) Error {
	return Error{Error_Opaque{Obj}}
}

func (_this Error) Is_Opaque() bool {
	_, ok := _this.Get_().(Error_Opaque)
	return ok
}

func (CompanionStruct_Error_) Default() Error {
	return Companion_Error_.Create_KeyVectorException_(_dafny.EmptySeq.SetString())
}

func (_this Error) Dtor_message() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case Error_KeyVectorException:
		return data.Message
	default:
		return data.(Error_CollectionOfErrors).Message
	}
}

func (_this Error) Dtor_AwsCryptographyMaterialProviders() m_AwsCryptographyMaterialProvidersTypes.Error {
	return _this.Get_().(Error_AwsCryptographyMaterialProviders).AwsCryptographyMaterialProviders
}

func (_this Error) Dtor_ComAmazonawsKms() m_ComAmazonawsKmsTypes.Error {
	return _this.Get_().(Error_ComAmazonawsKms).ComAmazonawsKms
}

func (_this Error) Dtor_list() _dafny.Sequence {
	return _this.Get_().(Error_CollectionOfErrors).List
}

func (_this Error) Dtor_obj() interface{} {
	return _this.Get_().(Error_Opaque).Obj
}

func (_this Error) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case Error_KeyVectorException:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.KeyVectorException" + "(" + _dafny.String(data.Message) + ")"
		}
	case Error_AwsCryptographyMaterialProviders:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.AwsCryptographyMaterialProviders" + "(" + _dafny.String(data.AwsCryptographyMaterialProviders) + ")"
		}
	case Error_ComAmazonawsKms:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.ComAmazonawsKms" + "(" + _dafny.String(data.ComAmazonawsKms) + ")"
		}
	case Error_CollectionOfErrors:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.CollectionOfErrors" + "(" + _dafny.String(data.List) + ", " + _dafny.String(data.Message) + ")"
		}
	case Error_Opaque:
		{
			return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.Opaque" + "(" + _dafny.String(data.Obj) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this Error) Equals(other Error) bool {
	switch data1 := _this.Get_().(type) {
	case Error_KeyVectorException:
		{
			data2, ok := other.Get_().(Error_KeyVectorException)
			return ok && data1.Message.Equals(data2.Message)
		}
	case Error_AwsCryptographyMaterialProviders:
		{
			data2, ok := other.Get_().(Error_AwsCryptographyMaterialProviders)
			return ok && data1.AwsCryptographyMaterialProviders.Equals(data2.AwsCryptographyMaterialProviders)
		}
	case Error_ComAmazonawsKms:
		{
			data2, ok := other.Get_().(Error_ComAmazonawsKms)
			return ok && data1.ComAmazonawsKms.Equals(data2.ComAmazonawsKms)
		}
	case Error_CollectionOfErrors:
		{
			data2, ok := other.Get_().(Error_CollectionOfErrors)
			return ok && data1.List.Equals(data2.List) && data1.Message.Equals(data2.Message)
		}
	case Error_Opaque:
		{
			data2, ok := other.Get_().(Error_Opaque)
			return ok && _dafny.AreEqual(data1.Obj, data2.Obj)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this Error) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(Error)
	return ok && _this.Equals(typed)
}

func Type_Error_() _dafny.TypeDescriptor {
	return type_Error_{}
}

type type_Error_ struct {
}

func (_this type_Error_) Default() interface{} {
	return Companion_Error_.Default()
}

func (_this type_Error_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error"
}
func (_this Error) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = Error{}

// End of datatype Error

// Definition of class OpaqueError
type OpaqueError struct {
}

func New_OpaqueError_() *OpaqueError {
	_this := OpaqueError{}

	return &_this
}

type CompanionStruct_OpaqueError_ struct {
}

var Companion_OpaqueError_ = CompanionStruct_OpaqueError_{}

func (*OpaqueError) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.OpaqueError"
}

// End of class OpaqueError

func Type_OpaqueError_() _dafny.TypeDescriptor {
	return type_OpaqueError_{}
}

type type_OpaqueError_ struct {
}

func (_this type_OpaqueError_) Default() interface{} {
	return Companion_Error_.Default()
}

func (_this type_OpaqueError_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.OpaqueError"
}
func (_this *CompanionStruct_OpaqueError_) Is_(__source Error) bool {
	var _0_e Error = (__source)
	_ = _0_e
	return (_0_e).Is_Opaque()
}

// Definition of class DummySubsetType
type DummySubsetType struct {
}

func New_DummySubsetType_() *DummySubsetType {
	_this := DummySubsetType{}

	return &_this
}

type CompanionStruct_DummySubsetType_ struct {
}

var Companion_DummySubsetType_ = CompanionStruct_DummySubsetType_{}

func (*DummySubsetType) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.DummySubsetType"
}
func (_this *CompanionStruct_DummySubsetType_) Witness() _dafny.Int {
	return _dafny.One
}

// End of class DummySubsetType

func Type_DummySubsetType_() _dafny.TypeDescriptor {
	return type_DummySubsetType_{}
}

type type_DummySubsetType_ struct {
}

func (_this type_DummySubsetType_) Default() interface{} {
	return Companion_DummySubsetType_.Witness()
}

func (_this type_DummySubsetType_) String() string {
	return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.DummySubsetType"
}
func (_this *CompanionStruct_DummySubsetType_) Is_(__source _dafny.Int) bool {
	var _1_x _dafny.Int = (__source)
	_ = _1_x
	return Companion_Default___.IsDummySubsetType(_1_x)
}
