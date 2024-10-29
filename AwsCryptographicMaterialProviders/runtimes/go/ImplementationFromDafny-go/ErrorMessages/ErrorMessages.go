// Package ErrorMessages
// Dafny module ErrorMessages compiled into Go

package ErrorMessages

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
	m_EdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/EdkWrapping"
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
	m_UTF8 "github.com/dafny-lang/DafnyStandardLibGo/UTF8"
	m_UUID "github.com/dafny-lang/DafnyStandardLibGo/UUID"
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
	return "ErrorMessages.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) IncorrectRawDataKeys(datakey _dafny.Sequence, keyringName _dafny.Sequence, keyProviderId _dafny.Sequence) _dafny.Sequence {
	return _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("EncryptedDataKey "), datakey), _dafny.SeqOfString(" did not match ")), keyringName), _dafny.SeqOfString(". ")), _dafny.SeqOfString("Expected: keyProviderId: ")), keyProviderId), _dafny.SeqOfString(".\n"))
}
func (_static *CompanionStruct_Default___) IncorrectDataKeys(encryptedDataKeys _dafny.Sequence, material m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, errMsg _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.IncorrectDataKeysExpectedValues(encryptedDataKeys, material, errMsg)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_expectedValue _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_expectedValue
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n"), _1_expectedValue))
	}
}
func (_static *CompanionStruct_Default___) IncorrectDataKeysExpectedValues(encryptedDataKeys _dafny.Sequence, material m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, errMsg _dafny.Sequence) m_Wrappers.Result {
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (_dafny.IntOfUint32((encryptedDataKeys).Cardinality())).Sign() == 0 {
		return m_Wrappers.Companion_Result_.Create_Success_(errMsg)
	} else {
		var _0_encryptedDataKey m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey = (encryptedDataKeys).Select(0).(m_AwsCryptographyMaterialProvidersTypes.EncryptedDataKey)
		_ = _0_encryptedDataKey
		var _1_valueOrError0 m_Wrappers.Result = (m_UTF8.Decode((_0_encryptedDataKey).Dtor_keyProviderId())).MapFailure(func(coer49 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error) func(interface{}) interface{} {
			return func(arg50 interface{}) interface{} {
				return coer49(arg50.(_dafny.Sequence))
			}
		}(func(_2_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error {
			return m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_2_e)
		}))
		_ = _1_valueOrError0
		if (_1_valueOrError0).IsFailure() {
			return (_1_valueOrError0).PropagateFailure()
		} else {
			var _3_extractedKeyProviderId _dafny.Sequence = (_1_valueOrError0).Extract().(_dafny.Sequence)
			_ = _3_extractedKeyProviderId
			var _4_valueOrError1 m_Wrappers.Result = (m_UTF8.Decode((_0_encryptedDataKey).Dtor_keyProviderInfo())).MapFailure(func(coer50 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error) func(interface{}) interface{} {
				return func(arg51 interface{}) interface{} {
					return coer50(arg51.(_dafny.Sequence))
				}
			}(func(_5_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error {
				return m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_5_e)
			}))
			_ = _4_valueOrError1
			if (_4_valueOrError1).IsFailure() {
				return (_4_valueOrError1).PropagateFailure()
			} else {
				var _6_extractedKeyProviderInfo _dafny.Sequence = (_4_valueOrError1).Extract().(_dafny.Sequence)
				_ = _6_extractedKeyProviderInfo
				if !_dafny.Companion_Sequence_.Equal(_3_extractedKeyProviderId, _dafny.SeqOfString("aws-kms-hierarchy")) {
					var _in0 _dafny.Sequence = (encryptedDataKeys).Drop(1)
					_ = _in0
					var _in1 m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = material
					_ = _in1
					var _in2 _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(errMsg, _dafny.SeqOfString("KeyProviderId: ")), _3_extractedKeyProviderId), _dafny.SeqOfString(", KeyProviderInfo: ")), _6_extractedKeyProviderInfo), _dafny.SeqOfString("\n"))
					_ = _in2
					encryptedDataKeys = _in0
					material = _in1
					errMsg = _in2
					goto TAIL_CALL_START
				} else {
					var _7_valueOrError2 m_Wrappers.Result = m_EdkWrapping.Companion_Default___.GetProviderWrappedMaterial((_0_encryptedDataKey).Dtor_ciphertext(), material)
					_ = _7_valueOrError2
					if (_7_valueOrError2).IsFailure() {
						return (_7_valueOrError2).PropagateFailure()
					} else {
						var _8_providerWrappedMaterial _dafny.Sequence = (_7_valueOrError2).Extract().(_dafny.Sequence)
						_ = _8_providerWrappedMaterial
						var _9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX _dafny.Int = (Companion_Default___.SALT__LENGTH()).Plus(Companion_Default___.IV__LENGTH())
						_ = _9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX
						var _10_EDK__CIPHERTEXT__VERSION__INDEX _dafny.Int = (_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX).Plus(Companion_Default___.VERSION__LENGTH())
						_ = _10_EDK__CIPHERTEXT__VERSION__INDEX
						var _11_valueOrError3 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX).Cmp(_10_EDK__CIPHERTEXT__VERSION__INDEX) < 0, m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Wrong branch key version index.")))
						_ = _11_valueOrError3
						if (_11_valueOrError3).IsFailure() {
							return (_11_valueOrError3).PropagateFailure()
						} else {
							var _12_valueOrError4 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_dafny.IntOfUint32((_8_providerWrappedMaterial).Cardinality())).Cmp(_10_EDK__CIPHERTEXT__VERSION__INDEX) >= 0, m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("Incorrect ciphertext structure.")))
							_ = _12_valueOrError4
							if (_12_valueOrError4).IsFailure() {
								return (_12_valueOrError4).PropagateFailure()
							} else {
								var _13_branchKeyVersionUuid _dafny.Sequence = (_8_providerWrappedMaterial).Subsequence((_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX).Uint32(), (_10_EDK__CIPHERTEXT__VERSION__INDEX).Uint32())
								_ = _13_branchKeyVersionUuid
								var _14_valueOrError5 m_Wrappers.Result = (m_UUID.FromByteArray(_13_branchKeyVersionUuid)).MapFailure(func(coer51 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error) func(interface{}) interface{} {
									return func(arg52 interface{}) interface{} {
										return coer51(arg52.(_dafny.Sequence))
									}
								}(func(_15_e _dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error {
									return m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_15_e)
								}))
								_ = _14_valueOrError5
								if (_14_valueOrError5).IsFailure() {
									return (_14_valueOrError5).PropagateFailure()
								} else {
									var _16_branchVersion _dafny.Sequence = (_14_valueOrError5).Extract().(_dafny.Sequence)
									_ = _16_branchVersion
									var _in3 _dafny.Sequence = (encryptedDataKeys).Drop(1)
									_ = _in3
									var _in4 m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = material
									_ = _in4
									var _in5 _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(errMsg, _dafny.SeqOfString("KeyProviderId: ")), _3_extractedKeyProviderId), _dafny.SeqOfString(", KeyProviderInfo: ")), _6_extractedKeyProviderInfo), _dafny.SeqOfString(", BranchKeyVersion: ")), _16_branchVersion), _dafny.SeqOfString("\n"))
									_ = _in5
									encryptedDataKeys = _in3
									material = _in4
									errMsg = _in5
									goto TAIL_CALL_START
								}
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) SALT__LENGTH() _dafny.Int {
	return _dafny.IntOfInt64(16)
}
func (_static *CompanionStruct_Default___) IV__LENGTH() _dafny.Int {
	return _dafny.IntOfInt64(12)
}
func (_static *CompanionStruct_Default___) VERSION__LENGTH() _dafny.Int {
	return _dafny.IntOfInt64(16)
}
func (_static *CompanionStruct_Default___) KMS__ECDH__DISCOVERY__ENCRYPT__ERROR() _dafny.Sequence {
	return _dafny.SeqOfString("KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")
}
func (_static *CompanionStruct_Default___) RAW__ECDH__DISCOVERY__ENCRYPT__ERROR() _dafny.Sequence {
	return _dafny.SeqOfString("PublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")
}
func (_static *CompanionStruct_Default___) RAW__ECDH__EPHEMERAL__DECRYPT__ERROR() _dafny.Sequence {
	return _dafny.SeqOfString("EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt.")
}

// End of class Default__
