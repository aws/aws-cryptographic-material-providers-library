// Package StormTracker
// Dafny module StormTracker compiled into Go

package StormTracker

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
	m_AwsKmsDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsDiscoveryKeyring"
	m_AwsKmsKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsKeyring"
	m_AwsKmsMrkAreUnique "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkAreUnique"
	m_AwsKmsMrkDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkDiscoveryKeyring"
	m_AwsKmsMrkKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkKeyring"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsKmsUtils"
	m_CanonicalEncryptionContext "github.com/aws/aws-cryptographic-material-providers-library/mpl/CanonicalEncryptionContext"
	m_Constants "github.com/aws/aws-cryptographic-material-providers-library/mpl/Constants"
	m_CreateKeyStoreTable "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeyStoreTable"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/mpl/DDBKeystoreOperations"
	m_DiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/DiscoveryMultiKeyring"
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
	m_StrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/StrictMultiKeyring"
	m_Structure "github.com/aws/aws-cryptographic-material-providers-library/mpl/Structure"
	m_SynchronizedLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/mpl/SynchronizedLocalCMC"
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
	m_DafnyLibraries "github.com/dafny-lang/DafnyStandardLibGo/DafnyLibraries"
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
	m_SortedSets "github.com/dafny-lang/DafnyStandardLibGo/SortedSets"
	m_Sorting "github.com/dafny-lang/DafnyStandardLibGo/Sorting"
	m_StandardLibrary "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary"
	m_StandardLibraryInterop "github.com/dafny-lang/DafnyStandardLibGo/StandardLibraryInterop"
	m_StandardLibrary_String "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_UInt"
	m_Streams "github.com/dafny-lang/DafnyStandardLibGo/Streams"
	m__Time "github.com/dafny-lang/DafnyStandardLibGo/Time_"
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
	return "StormTracker.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) DefaultStorm() m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_StormTrackingCache_.Create_StormTrackingCache_(int32(1000), m_Wrappers.Companion_Option_.Create_Some_(int32(1)), int32(10), int32(1), int32(20), int32(10), int32(20))
}
func (_static *CompanionStruct_Default___) ConsistentSettings(cache m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) bool {
	return ((((cache).Dtor_graceInterval()) <= ((cache).Dtor_gracePeriod())) && (((cache).Dtor_inFlightTTL()) <= ((cache).Dtor_gracePeriod()))) && (((cache).Dtor_graceInterval()) <= ((cache).Dtor_inFlightTTL()))
}
func (_static *CompanionStruct_Default___) N(n int32) _dafny.Sequence {
	return m_StandardLibrary_String.Companion_Default___.Base10Int2String(_dafny.IntOfInt32(n))
}
func (_static *CompanionStruct_Default___) BadCacheMsg(cache m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) _dafny.Sequence {
	var _0_msg _dafny.Sequence = _dafny.SeqOfString("For a StormCache : ")
	_ = _0_msg
	var _1_msg _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_0_msg, (func() _dafny.Sequence {
		if !(((cache).Dtor_graceInterval()) <= ((cache).Dtor_gracePeriod())) {
			return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("graceInterval must not exceed gracePeriod, yet configuration has graceInterval="), Companion_Default___.N((cache).Dtor_graceInterval())), _dafny.SeqOfString(" and gracePeriod=")), Companion_Default___.N((cache).Dtor_gracePeriod())), _dafny.SeqOfString(". "))
		}
		return _dafny.SeqOfString("")
	})())
	_ = _1_msg
	var _2_msg _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_1_msg, (func() _dafny.Sequence {
		if !(((cache).Dtor_inFlightTTL()) <= ((cache).Dtor_gracePeriod())) {
			return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("inFlightTTL must not exceed gracePeriod, yet configuration has inFlightTTL="), Companion_Default___.N((cache).Dtor_inFlightTTL())), _dafny.SeqOfString(" and gracePeriod=")), Companion_Default___.N((cache).Dtor_gracePeriod())), _dafny.SeqOfString(". "))
		}
		return _dafny.SeqOfString("")
	})())
	_ = _2_msg
	var _3_msg _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_2_msg, (func() _dafny.Sequence {
		if !(((cache).Dtor_graceInterval()) <= ((cache).Dtor_inFlightTTL())) {
			return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("graceInterval must not exceed inFlightTTL, yet configuration has graceInterval="), Companion_Default___.N((cache).Dtor_graceInterval())), _dafny.SeqOfString(" and inFlightTTL=")), Companion_Default___.N((cache).Dtor_inFlightTTL())), _dafny.SeqOfString(". "))
		}
		return _dafny.SeqOfString("")
	})())
	_ = _3_msg
	return _3_msg
}
func (_static *CompanionStruct_Default___) CheckSettings(cache m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) m_Wrappers.Outcome {
	if Companion_Default___.ConsistentSettings(cache) {
		return m_Wrappers.Companion_Outcome_.Create_Pass_()
	} else {
		return m_Wrappers.Companion_Outcome_.Create_Fail_(m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(Companion_Default___.BadCacheMsg(cache)))
	}
}

// End of class Default__

// Definition of datatype CacheState
type CacheState struct {
	Data_CacheState_
}

func (_this CacheState) Get_() Data_CacheState_ {
	return _this.Data_CacheState_
}

type Data_CacheState_ interface {
	isCacheState()
}

type CompanionStruct_CacheState_ struct {
}

var Companion_CacheState_ = CompanionStruct_CacheState_{}

type CacheState_EmptyWait struct {
}

func (CacheState_EmptyWait) isCacheState() {}

func (CompanionStruct_CacheState_) Create_EmptyWait_() CacheState {
	return CacheState{CacheState_EmptyWait{}}
}

func (_this CacheState) Is_EmptyWait() bool {
	_, ok := _this.Get_().(CacheState_EmptyWait)
	return ok
}

type CacheState_EmptyFetch struct {
}

func (CacheState_EmptyFetch) isCacheState() {}

func (CompanionStruct_CacheState_) Create_EmptyFetch_() CacheState {
	return CacheState{CacheState_EmptyFetch{}}
}

func (_this CacheState) Is_EmptyFetch() bool {
	_, ok := _this.Get_().(CacheState_EmptyFetch)
	return ok
}

type CacheState_Full struct {
	Data m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput
}

func (CacheState_Full) isCacheState() {}

func (CompanionStruct_CacheState_) Create_Full_(Data m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput) CacheState {
	return CacheState{CacheState_Full{Data}}
}

func (_this CacheState) Is_Full() bool {
	_, ok := _this.Get_().(CacheState_Full)
	return ok
}

func (CompanionStruct_CacheState_) Default() CacheState {
	return Companion_CacheState_.Create_EmptyWait_()
}

func (_this CacheState) Dtor_data() m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput {
	return _this.Get_().(CacheState_Full).Data
}

func (_this CacheState) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case CacheState_EmptyWait:
		{
			return "StormTracker.CacheState.EmptyWait"
		}
	case CacheState_EmptyFetch:
		{
			return "StormTracker.CacheState.EmptyFetch"
		}
	case CacheState_Full:
		{
			return "StormTracker.CacheState.Full" + "(" + _dafny.String(data.Data) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this CacheState) Equals(other CacheState) bool {
	switch data1 := _this.Get_().(type) {
	case CacheState_EmptyWait:
		{
			_, ok := other.Get_().(CacheState_EmptyWait)
			return ok
		}
	case CacheState_EmptyFetch:
		{
			_, ok := other.Get_().(CacheState_EmptyFetch)
			return ok
		}
	case CacheState_Full:
		{
			data2, ok := other.Get_().(CacheState_Full)
			return ok && data1.Data.Equals(data2.Data)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this CacheState) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(CacheState)
	return ok && _this.Equals(typed)
}

func Type_CacheState_() _dafny.TypeDescriptor {
	return type_CacheState_{}
}

type type_CacheState_ struct {
}

func (_this type_CacheState_) Default() interface{} {
	return Companion_CacheState_.Default()
}

func (_this type_CacheState_) String() string {
	return "StormTracker.CacheState"
}
func (_this CacheState) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = CacheState{}

// End of datatype CacheState

// Definition of class StormTracker
type StormTracker struct {
	Wrapped       *m_LocalCMC.LocalCMC
	InFlight      *m_DafnyLibraries.MutableMap
	GracePeriod   int64
	GraceInterval int64
	FanOut        int64
	InFlightTTL   int64
	LastPrune     int64
	SleepMilli    int64
}

func New_StormTracker_() *StormTracker {
	_this := StormTracker{}

	_this.Wrapped = (*m_LocalCMC.LocalCMC)(nil)
	_this.InFlight = (*m_DafnyLibraries.MutableMap)(nil)
	_this.GracePeriod = int64(0)
	_this.GraceInterval = int64(0)
	_this.FanOut = int64(0)
	_this.InFlightTTL = int64(0)
	_this.LastPrune = int64(0)
	_this.SleepMilli = int64(0)
	return &_this
}

type CompanionStruct_StormTracker_ struct {
}

var Companion_StormTracker_ = CompanionStruct_StormTracker_{}

func (_this *StormTracker) Equals(other *StormTracker) bool {
	return _this == other
}

func (_this *StormTracker) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*StormTracker)
	return ok && _this.Equals(other)
}

func (*StormTracker) String() string {
	return "StormTracker.StormTracker"
}

func Type_StormTracker_() _dafny.TypeDescriptor {
	return type_StormTracker_{}
}

type type_StormTracker_ struct {
}

func (_this type_StormTracker_) Default() interface{} {
	return (*StormTracker)(nil)
}

func (_this type_StormTracker_) String() string {
	return "StormTracker.StormTracker"
}
func (_this *StormTracker) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &StormTracker{}

func (_this *StormTracker) Ctor__(cache m_AwsCryptographyMaterialProvidersTypes.StormTrackingCache) {
	{
		var _nw0 *m_LocalCMC.LocalCMC = m_LocalCMC.New_LocalCMC_()
		_ = _nw0
		_nw0.Ctor__(_dafny.IntOfInt32((cache).Dtor_entryCapacity()), _dafny.IntOfInt32(((cache).Dtor_entryPruningTailSize()).UnwrapOr(int32(1)).(int32)))
		(_this).Wrapped = _nw0
		var _nw1 *m_DafnyLibraries.MutableMap = m_DafnyLibraries.New_MutableMap_()
		_ = _nw1
		(_this).InFlight = _nw1
		(_this).GracePeriod = int64((cache).Dtor_gracePeriod())
		(_this).GraceInterval = int64((cache).Dtor_graceInterval())
		(_this).FanOut = int64((cache).Dtor_fanOut())
		(_this).InFlightTTL = int64((cache).Dtor_inFlightTTL())
		(_this).SleepMilli = int64((cache).Dtor_sleepMilli())
		(_this).LastPrune = int64(0)
	}
}
func (_this *StormTracker) InFlightSize() int64 {
	{
		var _0_x _dafny.Int = (_this.InFlight).Size()
		_ = _0_x
		if (_0_x).Cmp(m_StandardLibrary_UInt.Companion_Default___.INT64__MAX__LIMIT()) <= 0 {
			return (_0_x).Int64()
		} else {
			return (m_StandardLibrary_UInt.Companion_Default___.INT64__MAX__LIMIT()).Int64()
		}
	}
}
func (_this *StormTracker) FanOutReached(now int64) bool {
	{
		var res bool = false
		_ = res
		(_this).PruneInFlight(now)
		res = (_this.FanOut) <= ((_this).InFlightSize())
		return res
		return res
	}
}
func (_this *StormTracker) AddLong(x int64, y int64) int64 {
	{
		if (x) < (((m_StandardLibrary_UInt.Companion_Default___.INT64__MAX__LIMIT()).Int64()) - (y)) {
			return (x) + (y)
		} else {
			return (m_StandardLibrary_UInt.Companion_Default___.INT64__MAX__LIMIT()).Int64()
		}
	}
}
func (_this *StormTracker) CheckInFlight(identifier _dafny.Sequence, result m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput, now int64) CacheState {
	{
		var output CacheState = Companion_CacheState_.Default()
		_ = output
		var _0_fanOutReached bool
		_ = _0_fanOutReached
		var _out0 bool
		_ = _out0
		_out0 = (_this).FanOutReached(now)
		_0_fanOutReached = _out0
		if _0_fanOutReached {
			output = Companion_CacheState_.Create_Full_(result)
			return output
		} else if ((result).Dtor_expiryTime()) <= (now) {
			var _out1 CacheState
			_ = _out1
			_out1 = (_this).CheckNewEntry(identifier, now)
			output = _out1
		} else if (now) < (((result).Dtor_expiryTime()) - (_this.GracePeriod)) {
			output = Companion_CacheState_.Create_Full_(result)
			return output
		} else {
			if (_this.InFlight).HasKey(identifier) {
				var _1_entry int64
				_ = _1_entry
				_1_entry = (_this.InFlight).Select(identifier).(int64)
				if ((_this).AddLong(_1_entry, _this.GraceInterval)) > (now) {
					output = Companion_CacheState_.Create_Full_(result)
					return output
				}
			}
			(_this.InFlight).Put(identifier, now)
			output = Companion_CacheState_.Create_EmptyFetch_()
			return output
		}
		return output
	}
}
func (_this *StormTracker) PruneInFlight(now int64) {
	{
		if (_this.FanOut) > ((_this).InFlightSize()) {
			return
		}
		if (_this.LastPrune) == (now) {
			return
		}
		(_this).LastPrune = now
		var _0_keySet _dafny.Set
		_ = _0_keySet
		_0_keySet = (_this.InFlight).Keys()
		var _1_keys _dafny.Sequence
		_ = _1_keys
		_1_keys = m_SortedSets.SetToSequence(_0_keySet)
		var _hi0 _dafny.Int = _dafny.IntOfUint32((_1_keys).Cardinality())
		_ = _hi0
		for _2_i := _dafny.Zero; _2_i.Cmp(_hi0) < 0; _2_i = _2_i.Plus(_dafny.One) {
			var _3_v int64
			_ = _3_v
			_3_v = (_this.InFlight).Select((_1_keys).Select((_2_i).Uint32()).(_dafny.Sequence)).(int64)
			if (now) >= ((_this).AddLong(_3_v, _this.InFlightTTL)) {
				(_this.InFlight).Remove((_1_keys).Select((_2_i).Uint32()).(_dafny.Sequence))
			}
		}
	}
}
func (_this *StormTracker) CheckNewEntry(identifier _dafny.Sequence, now int64) CacheState {
	{
		var output CacheState = Companion_CacheState_.Default()
		_ = output
		var _0_fanOutReached bool
		_ = _0_fanOutReached
		var _out0 bool
		_ = _out0
		_out0 = (_this).FanOutReached(now)
		_0_fanOutReached = _out0
		if _0_fanOutReached {
			output = Companion_CacheState_.Create_EmptyWait_()
			return output
		} else if (_this.InFlight).HasKey(identifier) {
			var _1_entry int64
			_ = _1_entry
			_1_entry = (_this.InFlight).Select(identifier).(int64)
			if ((_this).AddLong(_1_entry, _this.GraceInterval)) > (now) {
				output = Companion_CacheState_.Create_EmptyWait_()
				return output
			}
		}
		(_this.InFlight).Put(identifier, now)
		output = Companion_CacheState_.Create_EmptyFetch_()
		return output
		return output
	}
}
func (_this *StormTracker) GetFromCacheWithTime(input m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput, now int64) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(Companion_CacheState_.Default())
		_ = output
		var _0_result m_Wrappers.Result
		_ = _0_result
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = (_this.Wrapped).GetCacheEntryWithTime(input, now)
		_0_result = _out0
		if (_0_result).Is_Success() {
			var _1_newResult CacheState
			_ = _1_newResult
			var _out1 CacheState
			_ = _out1
			_out1 = (_this).CheckInFlight((input).Dtor_identifier(), (_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput), now)
			_1_newResult = _out1
			output = m_Wrappers.Companion_Result_.Create_Success_(_1_newResult)
			return output
		} else if ((_0_result).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error)).Is_EntryDoesNotExist() {
			var _2_newResult CacheState
			_ = _2_newResult
			var _out2 CacheState
			_ = _out2
			_out2 = (_this).CheckNewEntry((input).Dtor_identifier(), now)
			_2_newResult = _out2
			output = m_Wrappers.Companion_Result_.Create_Success_(_2_newResult)
			return output
		} else {
			output = m_Wrappers.Companion_Result_.Create_Failure_((_0_result).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error))
			return output
		}
		return output
	}
}
func (_this *StormTracker) GetFromCache(input m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(Companion_CacheState_.Default())
		_ = output
		var _0_now int64
		_ = _0_now
		var _out0 int64
		_ = _out0
		_out0 = m__Time.CurrentRelativeTime()
		_0_now = _out0
		var _out1 m_Wrappers.Result
		_ = _out1
		_out1 = (_this).GetFromCacheWithTime(input, _0_now)
		output = _out1
		return output
	}
}
func (_this *StormTracker) GetCacheEntry(input m_AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Result{}
		_ = output
		var _0_result m_Wrappers.Result
		_ = _0_result
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = (_this).GetFromCache(input)
		_0_result = _out0
		if (_0_result).Is_Failure() {
			output = m_Wrappers.Companion_Result_.Create_Failure_((_0_result).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error))
			return output
		} else if ((_0_result).Dtor_value().(CacheState)).Is_Full() {
			output = m_Wrappers.Companion_Result_.Create_Success_(((_0_result).Dtor_value().(CacheState)).Dtor_data())
			return output
		} else {
			output = m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_EntryDoesNotExist_(_dafny.SeqOfString("Entry does not exist")))
			return output
		}
		return output
	}
}
func (_this *StormTracker) PutCacheEntry(input m_AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = output
		(_this.InFlight).Remove((input).Dtor_identifier())
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = (_this.Wrapped).PutCacheEntry_k(input)
		output = _out0
		return output
	}
}
func (_this *StormTracker) DeleteCacheEntry(input m_AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = output
		(_this.InFlight).Remove((input).Dtor_identifier())
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = (_this.Wrapped).DeleteCacheEntry_k(input)
		output = _out0
		return output
	}
}
func (_this *StormTracker) UpdateUsageMetadata(input m_AwsCryptographyMaterialProvidersTypes.UpdateUsageMetadataInput) m_Wrappers.Result {
	{
		var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
		_ = output
		var _out0 m_Wrappers.Result
		_ = _out0
		_out0 = (_this.Wrapped).UpdateUsageMetadata_k(input)
		output = _out0
		return output
	}
}

// End of class StormTracker
