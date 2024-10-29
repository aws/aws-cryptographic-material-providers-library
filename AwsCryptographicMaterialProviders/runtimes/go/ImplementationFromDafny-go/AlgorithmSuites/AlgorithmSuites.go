// Package AlgorithmSuites
// Dafny module AlgorithmSuites compiled into Go

package AlgorithmSuites

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/ComAmazonawsDynamodbTypes"
	m_Com_Amazonaws_Dynamodb "github.com/aws/aws-cryptographic-material-providers-library/dynamodb/Com_Amazonaws_Dynamodb"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/kms/ComAmazonawsKmsTypes"
	m_Com_Amazonaws_Kms "github.com/aws/aws-cryptographic-material-providers-library/kms/Com_Amazonaws_Kms"
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
var _ m_CreateKeyStoreTable.Dummy__
var _ m_GetKeys.Dummy__
var _ m_AwsCryptographyKeyStoreOperations.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__
var _ m_KeyStore.Dummy__

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
	return "AlgorithmSuites.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) SupportedESDKEncrypt_q(e m_AwsCryptographyMaterialProvidersTypes.Encrypt) bool {
	return (((true) && ((((((e).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32))) || ((((e).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(24)))) || ((((e).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(16))))) && ((((e).Dtor_AES__GCM()).Dtor_tagLength()) == (int32(16)))) && ((((e).Dtor_AES__GCM()).Dtor_ivLength()) == (int32(12)))
}
func (_static *CompanionStruct_Default___) SupportedDBEEncrypt_q(e m_AwsCryptographyMaterialProvidersTypes.Encrypt) bool {
	return (((true) && ((((e).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && ((((e).Dtor_AES__GCM()).Dtor_tagLength()) == (int32(16)))) && ((((e).Dtor_AES__GCM()).Dtor_ivLength()) == (int32(12)))
}
func (_static *CompanionStruct_Default___) SupportedDBEEDKWrapping_q(p m_AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm) bool {
	return (((((((p).Is_IntermediateKeyWrapping()) && (true)) && ((((((p).Dtor_IntermediateKeyWrapping()).Dtor_pdkEncryptAlgorithm()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && ((((((p).Dtor_IntermediateKeyWrapping()).Dtor_pdkEncryptAlgorithm()).Dtor_AES__GCM()).Dtor_tagLength()) == (int32(16)))) && ((((((p).Dtor_IntermediateKeyWrapping()).Dtor_pdkEncryptAlgorithm()).Dtor_AES__GCM()).Dtor_ivLength()) == (int32(12)))) && ((((p).Dtor_IntermediateKeyWrapping()).Dtor_macKeyKdf()).Is_HKDF())) && ((((p).Dtor_IntermediateKeyWrapping()).Dtor_keyEncryptionKeyKdf()).Is_HKDF())
}
func (_static *CompanionStruct_Default___) KeyDerivationAlgorithm_q(kdf m_AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm) bool {
	return (!((true) && ((kdf).Is_HKDF())) || (((((kdf).Dtor_HKDF()).Dtor_inputKeyLength()) == (((kdf).Dtor_HKDF()).Dtor_outputKeyLength())) && (!((((kdf).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_())) || ((((kdf).Dtor_HKDF()).Dtor_inputKeyLength()) == (int32(32)))))) && (!((kdf).Is_None()))
}
func (_static *CompanionStruct_Default___) CommitmentDerivationAlgorithm_q(kdf m_AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm) bool {
	return (!((true) && ((kdf).Is_HKDF())) || (((((((kdf).Dtor_HKDF()).Dtor_hmac()).Is_SHA__512()) && ((((kdf).Dtor_HKDF()).Dtor_saltLength()) == (int32(32)))) && ((((kdf).Dtor_HKDF()).Dtor_inputKeyLength()) == (int32(32)))) && ((((kdf).Dtor_HKDF()).Dtor_outputKeyLength()) == (int32(32))))) && (!((kdf).Is_IDENTITY()))
}
func (_static *CompanionStruct_Default___) EdkWrappingAlgorithm_q(alg m_AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm) bool {
	return ((((((alg).Is_IntermediateKeyWrapping()) && ((((alg).Dtor_IntermediateKeyWrapping()).Dtor_keyEncryptionKeyKdf()).Is_HKDF())) && ((((alg).Dtor_IntermediateKeyWrapping()).Dtor_macKeyKdf()).Is_HKDF())) && (true)) && ((((((alg).Dtor_IntermediateKeyWrapping()).Dtor_pdkEncryptAlgorithm()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) || ((alg).Is_DIRECT__KEY__WRAPPING())
}
func (_static *CompanionStruct_Default___) AlgorithmSuiteInfo_q(a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) bool {
	return ((((((((Companion_Default___.KeyDerivationAlgorithm_q((a).Dtor_kdf())) && (Companion_Default___.CommitmentDerivationAlgorithm_q((a).Dtor_commitment()))) && (Companion_Default___.EdkWrappingAlgorithm_q((a).Dtor_edkWrapping()))) && (!(((a).Dtor_kdf()).Is_HKDF()) || ((true) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_outputKeyLength()) == ((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()))))) && (!(((a).Dtor_signature()).Is_ECDSA()) || (((a).Dtor_kdf()).Is_HKDF()))) && (!(((a).Dtor_commitment()).Is_HKDF()) || ((((((a).Dtor_commitment()).Dtor_HKDF()).Dtor_saltLength()) == (int32(32))) && (((a).Dtor_commitment()).Equals((a).Dtor_kdf()))))) && (!(((a).Dtor_edkWrapping()).Is_IntermediateKeyWrapping()) || (((((a).Dtor_kdf()).Is_HKDF()) && (((((a).Dtor_edkWrapping()).Dtor_IntermediateKeyWrapping()).Dtor_keyEncryptionKeyKdf()).Equals((a).Dtor_kdf()))) && (((((a).Dtor_edkWrapping()).Dtor_IntermediateKeyWrapping()).Dtor_macKeyKdf()).Equals((a).Dtor_kdf()))))) && (!((((a).Dtor_kdf()).Is_HKDF()) && (((a).Dtor_commitment()).Is_None())) || (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_saltLength()) == (int32(0))))) && (!(!(((a).Dtor_symmetricSignature()).Is_None())) || ((true) && (((a).Dtor_edkWrapping()).Is_IntermediateKeyWrapping())))
}
func (_static *CompanionStruct_Default___) ESDKAlgorithmSuite_q(a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) bool {
	return ((Companion_Default___.AlgorithmSuiteInfo_q(a)) && (Companion_Default___.SupportedESDKEncrypt_q((a).Dtor_encrypt()))) && (func() bool {
		var _source0 m_AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId = ((a).Dtor_id()).Dtor_ESDK()
		_ = _source0
		{
			if _source0.Is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF() {
				return ((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(0), uint8(20)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(16)))) && (((a).Dtor_kdf()).Is_IDENTITY())) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF() {
				return ((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(0), uint8(70)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(24)))) && (((a).Dtor_kdf()).Is_IDENTITY())) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF() {
				return ((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(0), uint8(120)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && (((a).Dtor_kdf()).Is_IDENTITY())) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256() {
				return (((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(1), uint8(20)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(16)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_()))) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256() {
				return (((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(1), uint8(70)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(24)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_()))) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256() {
				return (((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(1), uint8(120)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_()))) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256() {
				return ((((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(2), uint8(20)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(16)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_()))) && (((a).Dtor_signature()).Is_ECDSA())) && (((((a).Dtor_signature()).Dtor_ECDSA()).Dtor_curve()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P256_()))) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() {
				return ((((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(3), uint8(70)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(24)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_()))) && (((a).Dtor_signature()).Is_ECDSA())) && (((((a).Dtor_signature()).Dtor_ECDSA()).Dtor_curve()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_()))) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() {
				return ((((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(3), uint8(120)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_()))) && (((a).Dtor_signature()).Is_ECDSA())) && (((((a).Dtor_signature()).Dtor_ECDSA()).Dtor_curve()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_()))) && (((a).Dtor_commitment()).Is_None())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			if _source0.Is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY() {
				return (((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(4), uint8(120)))) && (((a).Dtor_messageVersion()) == (int32(2)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_()))) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_HKDF())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
			}
		}
		{
			return ((((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(5), uint8(120)))) && (((a).Dtor_messageVersion()) == (int32(2)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_()))) && (((a).Dtor_signature()).Is_ECDSA())) && (((((a).Dtor_signature()).Dtor_ECDSA()).Dtor_curve()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_()))) && (((a).Dtor_commitment()).Is_HKDF())) && (((a).Dtor_symmetricSignature()).Is_None())) && (((a).Dtor_edkWrapping()).Is_DIRECT__KEY__WRAPPING())
		}
	}())
}
func (_static *CompanionStruct_Default___) DBEAlgorithmSuite_q(a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) bool {
	return (((Companion_Default___.AlgorithmSuiteInfo_q(a)) && (Companion_Default___.SupportedDBEEncrypt_q((a).Dtor_encrypt()))) && (Companion_Default___.SupportedDBEEDKWrapping_q((a).Dtor_edkWrapping()))) && (func() bool {
		var _source0 m_AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId = ((a).Dtor_id()).Dtor_DBE()
		_ = _source0
		{
			if _source0.Is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384() {
				return ((((((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(103), uint8(0)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_()))) && (((a).Dtor_signature()).Is_None())) && (((a).Dtor_commitment()).Is_HKDF())) && (((a).Dtor_symmetricSignature()).Is_HMAC())) && ((((a).Dtor_symmetricSignature()).Dtor_HMAC()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_()))) && (((a).Dtor_edkWrapping()).Is_IntermediateKeyWrapping())) && (true)) && (((((((a).Dtor_edkWrapping()).Dtor_IntermediateKeyWrapping()).Dtor_pdkEncryptAlgorithm()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))
			}
		}
		{
			return (((((((((((((_dafny.Companion_Sequence_.Equal((a).Dtor_binaryId(), _dafny.SeqOf(uint8(103), uint8(1)))) && (((a).Dtor_messageVersion()) == (int32(1)))) && (true)) && (((((a).Dtor_encrypt()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))) && (((a).Dtor_kdf()).Is_HKDF())) && (((((a).Dtor_kdf()).Dtor_HKDF()).Dtor_hmac()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_()))) && (((a).Dtor_signature()).Is_ECDSA())) && (((((a).Dtor_signature()).Dtor_ECDSA()).Dtor_curve()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_()))) && (((a).Dtor_commitment()).Is_HKDF())) && (((a).Dtor_symmetricSignature()).Is_HMAC())) && ((((a).Dtor_symmetricSignature()).Dtor_HMAC()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_()))) && (((a).Dtor_edkWrapping()).Is_IntermediateKeyWrapping())) && (true)) && (((((((a).Dtor_edkWrapping()).Dtor_IntermediateKeyWrapping()).Dtor_pdkEncryptAlgorithm()).Dtor_AES__GCM()).Dtor_keyLength()) == (int32(32)))
		}
	}())
}
func (_static *CompanionStruct_Default___) AlgorithmSuite_q(a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) bool {
	var _source0 m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId = (a).Dtor_id()
	_ = _source0
	{
		if _source0.Is_ESDK() {
			return Companion_Default___.ESDKAlgorithmSuite_q(a)
		}
	}
	{
		return Companion_Default___.DBEAlgorithmSuite_q(a)
	}
}
func (_static *CompanionStruct_Default___) HKDF__SHA__256(keyLength int32) m_AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_HKDF_(m_AwsCryptographyMaterialProvidersTypes.Companion_HKDF_.Create_HKDF_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_(), int32(0), keyLength, keyLength))
}
func (_static *CompanionStruct_Default___) HKDF__SHA__384(keyLength int32) m_AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_HKDF_(m_AwsCryptographyMaterialProvidersTypes.Companion_HKDF_.Create_HKDF_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_(), int32(0), keyLength, keyLength))
}
func (_static *CompanionStruct_Default___) HKDF__SHA__512(keyLength int32) m_AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_HKDF_(m_AwsCryptographyMaterialProvidersTypes.Companion_HKDF_.Create_HKDF_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_(), int32(32), keyLength, keyLength))
}
func (_static *CompanionStruct_Default___) GetSuite(id m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId) m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	var _source0 m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId = id
	_ = _source0
	{
		if _source0.Is_ESDK() {
			var _0_e m_AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId = _source0.Get_().(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK).ESDK
			_ = _0_e
			return Companion_Default___.GetESDKSuite(_0_e)
		}
	}
	{
		var _1_e m_AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId = _source0.Get_().(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE).DBE
		_ = _1_e
		return Companion_Default___.GetDBESuite(_1_e)
	}
}
func (_static *CompanionStruct_Default___) GetDBESuite(id m_AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId) m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return (Companion_Default___.SupportedDBEAlgorithmSuites()).Get(id).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
}
func (_static *CompanionStruct_Default___) GetESDKSuite(id m_AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId) m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return (Companion_Default___.SupportedESDKAlgorithmSuites()).Get(id).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
}
func (_static *CompanionStruct_Default___) GetEncryptKeyLength(a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) int32 {
	var _source0 m_AwsCryptographyMaterialProvidersTypes.Encrypt = (a).Dtor_encrypt()
	_ = _source0
	{
		var _0_e m_AwsCryptographyPrimitivesTypes.AES__GCM = _source0.Get_().(m_AwsCryptographyMaterialProvidersTypes.Encrypt_AES__GCM).AES__GCM
		_ = _0_e
		return (_0_e).Dtor_keyLength()
	}
}
func (_static *CompanionStruct_Default___) GetEncryptTagLength(a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) int32 {
	var _source0 m_AwsCryptographyMaterialProvidersTypes.Encrypt = (a).Dtor_encrypt()
	_ = _source0
	{
		var _0_e m_AwsCryptographyPrimitivesTypes.AES__GCM = _source0.Get_().(m_AwsCryptographyMaterialProvidersTypes.Encrypt_AES__GCM).AES__GCM
		_ = _0_e
		return (_0_e).Dtor_tagLength()
	}
}
func (_static *CompanionStruct_Default___) GetEncryptIvLength(a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) int32 {
	var _source0 m_AwsCryptographyMaterialProvidersTypes.Encrypt = (a).Dtor_encrypt()
	_ = _source0
	{
		var _0_e m_AwsCryptographyPrimitivesTypes.AES__GCM = _source0.Get_().(m_AwsCryptographyMaterialProvidersTypes.Encrypt_AES__GCM).AES__GCM
		_ = _0_e
		return (_0_e).Dtor_ivLength()
	}
}
func (_static *CompanionStruct_Default___) GetAlgorithmSuiteInfo(binaryId_q _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((Companion_Default___.AlgorithmSuiteInfoByBinaryId()).Contains(binaryId_q), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Invalid BinaryId")))
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		return m_Wrappers.Companion_Result_.Create_Success_((Companion_Default___.AlgorithmSuiteInfoByBinaryId()).Get(binaryId_q).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo))
	}
}
func (_static *CompanionStruct_Default___) Bits128() int32 {
	return int32(16)
}
func (_static *CompanionStruct_Default___) TagLen() int32 {
	return int32(16)
}
func (_static *CompanionStruct_Default___) IvLen() int32 {
	return int32(12)
}
func (_static *CompanionStruct_Default___) AES__128__GCM__IV12__TAG16() m_AwsCryptographyMaterialProvidersTypes.Encrypt {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_Encrypt_.Create_AES__GCM_(m_AwsCryptographyPrimitivesTypes.Companion_AES__GCM_.Create_AES__GCM_(Companion_Default___.Bits128(), Companion_Default___.TagLen(), Companion_Default___.IvLen()))
}
func (_static *CompanionStruct_Default___) Bits192() int32 {
	return int32(24)
}
func (_static *CompanionStruct_Default___) AES__192__GCM__IV12__TAG16() m_AwsCryptographyMaterialProvidersTypes.Encrypt {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_Encrypt_.Create_AES__GCM_(m_AwsCryptographyPrimitivesTypes.Companion_AES__GCM_.Create_AES__GCM_(Companion_Default___.Bits192(), Companion_Default___.TagLen(), Companion_Default___.IvLen()))
}
func (_static *CompanionStruct_Default___) Bits256() int32 {
	return int32(32)
}
func (_static *CompanionStruct_Default___) AES__256__GCM__IV12__TAG16() m_AwsCryptographyMaterialProvidersTypes.Encrypt {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_Encrypt_.Create_AES__GCM_(m_AwsCryptographyPrimitivesTypes.Companion_AES__GCM_.Create_AES__GCM_(Companion_Default___.Bits256(), Companion_Default___.TagLen(), Companion_Default___.IvLen()))
}
func (_static *CompanionStruct_Default___) EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512() m_AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_IntermediateKeyWrapping_(m_AwsCryptographyMaterialProvidersTypes.Companion_IntermediateKeyWrapping_.Create_IntermediateKeyWrapping_(Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), Companion_Default___.AES__256__GCM__IV12__TAG16()))
}
func (_static *CompanionStruct_Default___) DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_DBE_(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384_()), _dafny.SeqOf(uint8(103), uint8(0)), int32(1), Companion_Default___.AES__256__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_HMAC_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_()), Companion_Default___.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512())
}
func (_static *CompanionStruct_Default___) DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_DBE_(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384_()), _dafny.SeqOf(uint8(103), uint8(1)), int32(1), Companion_Default___.AES__256__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_ECDSA_(m_AwsCryptographyMaterialProvidersTypes.Companion_ECDSA_.Create_ECDSA_(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_())), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_HMAC_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_()), Companion_Default___.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512())
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF_()), _dafny.SeqOf(uint8(0), uint8(20)), int32(1), Companion_Default___.AES__128__GCM__IV12__TAG16(), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_IDENTITY_(m_AwsCryptographyMaterialProvidersTypes.Companion_IDENTITY_.Create_IDENTITY_()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__192__GCM__IV12__TAG16__NO__KDF_()), _dafny.SeqOf(uint8(0), uint8(70)), int32(1), Companion_Default___.AES__192__GCM__IV12__TAG16(), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_IDENTITY_(m_AwsCryptographyMaterialProvidersTypes.Companion_IDENTITY_.Create_IDENTITY_()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_()), _dafny.SeqOf(uint8(0), uint8(120)), int32(1), Companion_Default___.AES__256__GCM__IV12__TAG16(), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_IDENTITY_(m_AwsCryptographyMaterialProvidersTypes.Companion_IDENTITY_.Create_IDENTITY_()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256_()), _dafny.SeqOf(uint8(1), uint8(20)), int32(1), Companion_Default___.AES__128__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__256(Companion_Default___.Bits128()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256_()), _dafny.SeqOf(uint8(1), uint8(70)), int32(1), Companion_Default___.AES__192__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__256(Companion_Default___.Bits192()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256_()), _dafny.SeqOf(uint8(1), uint8(120)), int32(1), Companion_Default___.AES__256__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__256(Companion_Default___.Bits256()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256_()), _dafny.SeqOf(uint8(2), uint8(20)), int32(1), Companion_Default___.AES__128__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__256(Companion_Default___.Bits128()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_ECDSA_(m_AwsCryptographyMaterialProvidersTypes.Companion_ECDSA_.Create_ECDSA_(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P256_())), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384_()), _dafny.SeqOf(uint8(3), uint8(70)), int32(1), Companion_Default___.AES__192__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__384(Companion_Default___.Bits192()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_ECDSA_(m_AwsCryptographyMaterialProvidersTypes.Companion_ECDSA_.Create_ECDSA_(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_())), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384_()), _dafny.SeqOf(uint8(3), uint8(120)), int32(1), Companion_Default___.AES__256__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__384(Companion_Default___.Bits256()), m_AwsCryptographyMaterialProvidersTypes.Companion_DerivationAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_ECDSA_(m_AwsCryptographyMaterialProvidersTypes.Companion_ECDSA_.Create_ECDSA_(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_())), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY_()), _dafny.SeqOf(uint8(4), uint8(120)), int32(2), Companion_Default___.AES__256__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Create_AlgorithmSuiteInfo_(m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteId_.Create_ESDK_(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384_()), _dafny.SeqOf(uint8(5), uint8(120)), int32(2), Companion_Default___.AES__256__GCM__IV12__TAG16(), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), Companion_Default___.HKDF__SHA__512(Companion_Default___.Bits256()), m_AwsCryptographyMaterialProvidersTypes.Companion_SignatureAlgorithm_.Create_ECDSA_(m_AwsCryptographyMaterialProvidersTypes.Companion_ECDSA_.Create_ECDSA_(m_AwsCryptographyPrimitivesTypes.Companion_ECDSASignatureAlgorithm_.Create_ECDSA__P384_())), m_AwsCryptographyMaterialProvidersTypes.Companion_SymmetricSignatureAlgorithm_.Create_None_(m_AwsCryptographyMaterialProvidersTypes.Companion_None_.Create_None_()), m_AwsCryptographyMaterialProvidersTypes.Companion_EdkWrappingAlgorithm_.Create_DIRECT__KEY__WRAPPING_(m_AwsCryptographyMaterialProvidersTypes.Companion_DIRECT__KEY__WRAPPING_.Create_DIRECT__KEY__WRAPPING_()))
}
func (_static *CompanionStruct_Default___) SupportedESDKAlgorithmSuites() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF_(), Companion_Default___.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__192__GCM__IV12__TAG16__NO__KDF_(), Companion_Default___.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF_(), Companion_Default___.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256_(), Companion_Default___.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256_(), Companion_Default___.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256_(), Companion_Default___.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256_(), Companion_Default___.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384_(), Companion_Default___.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384_(), Companion_Default___.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY_(), Companion_Default___.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_ESDKAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384_(), Companion_Default___.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384())
}
func (_static *CompanionStruct_Default___) SupportedDBEAlgorithmSuites() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384_(), Companion_Default___.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()).UpdateUnsafe(m_AwsCryptographyMaterialProvidersTypes.Companion_DBEAlgorithmSuiteId_.Create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384_(), Companion_Default___.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384())
}
func (_static *CompanionStruct_Default___) AlgorithmSuiteInfoByBinaryId() _dafny.Map {
	return _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOf(uint8(0), uint8(20)), Companion_Default___.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF()).UpdateUnsafe(_dafny.SeqOf(uint8(0), uint8(70)), Companion_Default___.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF()).UpdateUnsafe(_dafny.SeqOf(uint8(0), uint8(120)), Companion_Default___.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF()).UpdateUnsafe(_dafny.SeqOf(uint8(1), uint8(20)), Companion_Default___.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()).UpdateUnsafe(_dafny.SeqOf(uint8(1), uint8(70)), Companion_Default___.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()).UpdateUnsafe(_dafny.SeqOf(uint8(1), uint8(120)), Companion_Default___.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()).UpdateUnsafe(_dafny.SeqOf(uint8(2), uint8(20)), Companion_Default___.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()).UpdateUnsafe(_dafny.SeqOf(uint8(3), uint8(70)), Companion_Default___.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()).UpdateUnsafe(_dafny.SeqOf(uint8(3), uint8(120)), Companion_Default___.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()).UpdateUnsafe(_dafny.SeqOf(uint8(4), uint8(120)), Companion_Default___.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()).UpdateUnsafe(_dafny.SeqOf(uint8(5), uint8(120)), Companion_Default___.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()).UpdateUnsafe(_dafny.SeqOf(uint8(103), uint8(0)), Companion_Default___.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()).UpdateUnsafe(_dafny.SeqOf(uint8(103), uint8(1)), Companion_Default___.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384())
}

// End of class Default__

// Definition of class AlgorithmSuite
type AlgorithmSuite struct {
}

func New_AlgorithmSuite_() *AlgorithmSuite {
	_this := AlgorithmSuite{}

	return &_this
}

type CompanionStruct_AlgorithmSuite_ struct {
}

var Companion_AlgorithmSuite_ = CompanionStruct_AlgorithmSuite_{}

func (*AlgorithmSuite) String() string {
	return "AlgorithmSuites.AlgorithmSuite"
}

// End of class AlgorithmSuite

func Type_AlgorithmSuite_() _dafny.TypeDescriptor {
	return type_AlgorithmSuite_{}
}

type type_AlgorithmSuite_ struct {
}

func (_this type_AlgorithmSuite_) Default() interface{} {
	return m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Default()
}

func (_this type_AlgorithmSuite_) String() string {
	return "AlgorithmSuites.AlgorithmSuite"
}
func (_this *CompanionStruct_AlgorithmSuite_) Is_(__source m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo) bool {
	var _0_a m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = (__source)
	_ = _0_a
	return Companion_Default___.AlgorithmSuite_q(_0_a)
}
