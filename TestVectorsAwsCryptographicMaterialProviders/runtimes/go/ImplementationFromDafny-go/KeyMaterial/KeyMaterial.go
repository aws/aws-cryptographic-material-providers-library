// Package KeyMaterial
// Dafny module KeyMaterial compiled into Go

package KeyMaterial

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
	m_AwsCryptographyMaterialProvidersTestVectorKeysTypes "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AwsCryptographyMaterialProvidersTestVectorKeysTypes"
	m_JSONHelpers "github.com/aws/aws-cryptographic-material-providers-library/testvectors/JSONHelpers"
	m_KeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyDescription"
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
	m_JSON_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_API"
	m_JSON_ConcreteSyntax_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_Spec"
	m_JSON_ConcreteSyntax_SpecProperties "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_SpecProperties"
	m_JSON_Deserializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer"
	m_JSON_Deserializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_ByteStrConversion"
	m_JSON_Deserializer_Uint16StrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_Uint16StrConversion"
	m_JSON_Errors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Errors"
	m_JSON_Grammar "github.com/dafny-lang/DafnyStandardLibGo/JSON_Grammar"
	m_JSON_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer"
	m_JSON_Serializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer_ByteStrConversion"
	m_JSON_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_Spec"
	m_JSON_Utils_Cursors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Cursors"
	m_JSON_Utils_Lexers_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Core"
	m_JSON_Utils_Lexers_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Strings"
	m_JSON_Utils_Parsers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Parsers"
	m_JSON_Utils_Seq "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Seq"
	m_JSON_Utils_Str "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str"
	m_JSON_Utils_Str_CharStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrConversion"
	m_JSON_Utils_Str_CharStrEscaping "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrEscaping"
	m_JSON_Utils_Vectors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Vectors"
	m_JSON_Utils_Views_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Core"
	m_JSON_Utils_Views_Writers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Writers"
	m_JSON_Values "github.com/dafny-lang/DafnyStandardLibGo/JSON_Values"
	m_JSON_ZeroCopy_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_API"
	m_JSON_ZeroCopy_Deserializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer"
	m_JSON_ZeroCopy_Deserializer_API "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_API"
	m_JSON_ZeroCopy_Deserializer_ArrayParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ArrayParams"
	m_JSON_ZeroCopy_Deserializer_Arrays "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Arrays"
	m_JSON_ZeroCopy_Deserializer_Constants "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Constants"
	m_JSON_ZeroCopy_Deserializer_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Core"
	m_JSON_ZeroCopy_Deserializer_Numbers "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Numbers"
	m_JSON_ZeroCopy_Deserializer_ObjectParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ObjectParams"
	m_JSON_ZeroCopy_Deserializer_Objects "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Objects"
	m_JSON_ZeroCopy_Deserializer_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Strings"
	m_JSON_ZeroCopy_Deserializer_Values "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Values"
	m_JSON_ZeroCopy_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Serializer"
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
var _ m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Dummy__
var _ m_JSON_Utils_Views_Core.Dummy__
var _ m_JSON_Utils_Views_Writers.Dummy__
var _ m_JSON_Utils_Lexers_Core.Dummy__
var _ m_JSON_Utils_Lexers_Strings.Dummy__
var _ m_JSON_Utils_Cursors.Dummy__
var _ m_JSON_Utils_Parsers.Dummy__
var _ m_JSON_Utils_Str_CharStrConversion.Dummy__
var _ m_JSON_Utils_Str_CharStrEscaping.Dummy__
var _ m_JSON_Utils_Str.Dummy__
var _ m_JSON_Utils_Seq.Dummy__
var _ m_JSON_Utils_Vectors.Dummy__
var _ m_JSON_Errors.Dummy__
var _ m_JSON_Values.Dummy__
var _ m_JSON_Spec.Dummy__
var _ m_JSON_Grammar.Dummy__
var _ m_JSON_Serializer_ByteStrConversion.Dummy__
var _ m_JSON_Serializer.Dummy__
var _ m_JSON_Deserializer_Uint16StrConversion.Dummy__
var _ m_JSON_Deserializer_ByteStrConversion.Dummy__
var _ m_JSON_Deserializer.Dummy__
var _ m_JSON_ConcreteSyntax_Spec.Dummy__
var _ m_JSON_ConcreteSyntax_SpecProperties.Dummy__
var _ m_JSON_ZeroCopy_Serializer.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Core.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Strings.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Numbers.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ObjectParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Objects.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ArrayParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Arrays.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Constants.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Values.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_API.Dummy__
var _ m_JSON_ZeroCopy_Deserializer.Dummy__
var _ m_JSON_ZeroCopy_API.Dummy__
var _ m_JSON_API.Dummy__
var _ m_JSONHelpers.Dummy__
var _ m_KeyDescription.Dummy__

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
	return "KeyMaterial.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) BuildKeyMaterials(mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient, obj _dafny.Sequence) m_Wrappers.Result {
	if (_dafny.IntOfUint32((obj).Cardinality())).Sign() == 0 {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.NewMapBuilder().ToMap())
	} else {
		var _0_name _dafny.Sequence = (*((obj).Select(0).(_dafny.Tuple)).IndexInt(0)).(_dafny.Sequence)
		_ = _0_name
		var _1_valueOrError0 m_Wrappers.Result = Companion_Default___.ToKeyMaterial(mpl, _0_name, (*((obj).Select(0).(_dafny.Tuple)).IndexInt(1)).(m_JSON_Values.JSON))
		_ = _1_valueOrError0
		if (_1_valueOrError0).IsFailure() {
			return (_1_valueOrError0).PropagateFailure()
		} else {
			var _2_keyMaterial KeyMaterial = (_1_valueOrError0).Extract().(KeyMaterial)
			_ = _2_keyMaterial
			var _3_valueOrError1 m_Wrappers.Result = Companion_Default___.BuildKeyMaterials(mpl, (obj).Drop(1))
			_ = _3_valueOrError1
			if (_3_valueOrError1).IsFailure() {
				return (_3_valueOrError1).PropagateFailure()
			} else {
				var _4_tail _dafny.Map = (_3_valueOrError1).Extract().(_dafny.Map)
				_ = _4_tail
				return m_Wrappers.Companion_Result_.Create_Success_((_dafny.NewMapBuilder().ToMap().UpdateUnsafe(_0_name, _2_keyMaterial)).Merge(_4_tail))
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToKeyMaterial(mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient, name _dafny.Sequence, obj m_JSON_Values.JSON) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((obj).Is_Object(), _dafny.SeqOfString("KeyDescription not an object"))
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj _dafny.Sequence = (obj).Dtor_obj()
		_ = _1_obj
		var _2_typString _dafny.Sequence = _dafny.SeqOfString("type")
		_ = _2_typString
		var _3_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_2_typString, _1_obj)
		_ = _3_valueOrError1
		if (_3_valueOrError1).IsFailure() {
			return (_3_valueOrError1).PropagateFailure()
		} else {
			var _4_typ _dafny.Sequence = (_3_valueOrError1).Extract().(_dafny.Sequence)
			_ = _4_typ
			var _5_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(Companion_Default___.KeyMaterialString_q(_4_typ), _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported KeyMaterial type:"), _4_typ))
			_ = _5_valueOrError2
			if (_5_valueOrError2).IsFailure() {
				return (_5_valueOrError2).PropagateFailure()
			} else {
				var _source0 _dafny.Sequence = _4_typ
				_ = _source0
				{
					if (_source0).Equals(_dafny.SeqOfString("static-material")) {
						return Companion_Default___.ToStaticMaterial(mpl, name, _1_obj)
					}
				}
				{
					if (_source0).Equals(_dafny.SeqOfString("static-branch-key")) {
						return Companion_Default___.ToStaticBranchKey(mpl, name, _1_obj)
					}
				}
				{
					var _6_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetBool(_dafny.SeqOfString("encrypt"), _1_obj)
					_ = _6_valueOrError3
					if (_6_valueOrError3).IsFailure() {
						return (_6_valueOrError3).PropagateFailure()
					} else {
						var _7_encrypt bool = (_6_valueOrError3).Extract().(bool)
						_ = _7_encrypt
						var _8_valueOrError4 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetBool(_dafny.SeqOfString("decrypt"), _1_obj)
						_ = _8_valueOrError4
						if (_8_valueOrError4).IsFailure() {
							return (_8_valueOrError4).PropagateFailure()
						} else {
							var _9_decrypt bool = (_8_valueOrError4).Extract().(bool)
							_ = _9_decrypt
							var _10_valueOrError5 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("key-id"), _1_obj)
							_ = _10_valueOrError5
							if (_10_valueOrError5).IsFailure() {
								return (_10_valueOrError5).PropagateFailure()
							} else {
								var _11_keyIdentifierOption m_Wrappers.Option = (_10_valueOrError5).Extract().(m_Wrappers.Option)
								_ = _11_keyIdentifierOption
								var _12_keyIdentifier _dafny.Sequence = (_11_keyIdentifierOption).UnwrapOr(name).(_dafny.Sequence)
								_ = _12_keyIdentifier
								var _source1 _dafny.Sequence = _4_typ
								_ = _source1
								{
									if (_source1).Equals(_dafny.SeqOfString("aws-kms")) {
										return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_KMS_(name, _7_encrypt, _9_decrypt, _12_keyIdentifier))
									}
								}
								{
									if (_source1).Equals(_dafny.SeqOfString("aws-kms-ecdh")) {
										var _13_valueOrError6 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("algorithm"), _1_obj)
										_ = _13_valueOrError6
										if (_13_valueOrError6).IsFailure() {
											return (_13_valueOrError6).PropagateFailure()
										} else {
											var _14_algorithm _dafny.Sequence = (_13_valueOrError6).Extract().(_dafny.Sequence)
											_ = _14_algorithm
											var _15_valueOrError7 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender-material"), _1_obj)
											_ = _15_valueOrError7
											if (_15_valueOrError7).IsFailure() {
												return (_15_valueOrError7).PropagateFailure()
											} else {
												var _16_senderMaterial _dafny.Sequence = (_15_valueOrError7).Extract().(_dafny.Sequence)
												_ = _16_senderMaterial
												var _17_valueOrError8 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient-material"), _1_obj)
												_ = _17_valueOrError8
												if (_17_valueOrError8).IsFailure() {
													return (_17_valueOrError8).PropagateFailure()
												} else {
													var _18_recipientMaterial _dafny.Sequence = (_17_valueOrError8).Extract().(_dafny.Sequence)
													_ = _18_recipientMaterial
													var _19_valueOrError9 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("encoding"), _1_obj)
													_ = _19_valueOrError9
													if (_19_valueOrError9).IsFailure() {
														return (_19_valueOrError9).PropagateFailure()
													} else {
														var _20_encoding _dafny.Sequence = (_19_valueOrError9).Extract().(_dafny.Sequence)
														_ = _20_encoding
														var _21_valueOrError10 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender-material-public-key"), _1_obj)
														_ = _21_valueOrError10
														if (_21_valueOrError10).IsFailure() {
															return (_21_valueOrError10).PropagateFailure()
														} else {
															var _22_senderPublicKey _dafny.Sequence = (_21_valueOrError10).Extract().(_dafny.Sequence)
															_ = _22_senderPublicKey
															var _23_valueOrError11 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient-material-public-key"), _1_obj)
															_ = _23_valueOrError11
															if (_23_valueOrError11).IsFailure() {
																return (_23_valueOrError11).PropagateFailure()
															} else {
																var _24_recipientPublicKey _dafny.Sequence = (_23_valueOrError11).Extract().(_dafny.Sequence)
																_ = _24_recipientPublicKey
																return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_KMSEcdh_(name, _7_encrypt, _9_decrypt, _12_keyIdentifier, _14_algorithm, _16_senderMaterial, _18_recipientMaterial, _22_senderPublicKey, _24_recipientPublicKey))
															}
														}
													}
												}
											}
										}
									}
								}
								{
									if (_source1).Equals(_dafny.SeqOfString("ecc-private")) {
										var _25_valueOrError12 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("algorithm"), _1_obj)
										_ = _25_valueOrError12
										if (_25_valueOrError12).IsFailure() {
											return (_25_valueOrError12).PropagateFailure()
										} else {
											var _26_algorithm _dafny.Sequence = (_25_valueOrError12).Extract().(_dafny.Sequence)
											_ = _26_algorithm
											var _27_valueOrError13 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetNat(_dafny.SeqOfString("bits"), _1_obj)
											_ = _27_valueOrError13
											if (_27_valueOrError13).IsFailure() {
												return (_27_valueOrError13).PropagateFailure()
											} else {
												var _28_bits _dafny.Int = (_27_valueOrError13).Extract().(_dafny.Int)
												_ = _28_bits
												var _29_valueOrError14 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("encoding"), _1_obj)
												_ = _29_valueOrError14
												if (_29_valueOrError14).IsFailure() {
													return (_29_valueOrError14).PropagateFailure()
												} else {
													var _30_encoding _dafny.Sequence = (_29_valueOrError14).Extract().(_dafny.Sequence)
													_ = _30_encoding
													var _31_valueOrError15 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender-material"), _1_obj)
													_ = _31_valueOrError15
													if (_31_valueOrError15).IsFailure() {
														return (_31_valueOrError15).PropagateFailure()
													} else {
														var _32_senderMaterial _dafny.Sequence = (_31_valueOrError15).Extract().(_dafny.Sequence)
														_ = _32_senderMaterial
														var _33_valueOrError16 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient-material"), _1_obj)
														_ = _33_valueOrError16
														if (_33_valueOrError16).IsFailure() {
															return (_33_valueOrError16).PropagateFailure()
														} else {
															var _34_recipientMaterial _dafny.Sequence = (_33_valueOrError16).Extract().(_dafny.Sequence)
															_ = _34_recipientMaterial
															var _35_valueOrError17 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("sender-material-public-key"), _1_obj)
															_ = _35_valueOrError17
															if (_35_valueOrError17).IsFailure() {
																return (_35_valueOrError17).PropagateFailure()
															} else {
																var _36_senderPublicKey _dafny.Sequence = (_35_valueOrError17).Extract().(_dafny.Sequence)
																_ = _36_senderPublicKey
																var _37_valueOrError18 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("recipient-material-public-key"), _1_obj)
																_ = _37_valueOrError18
																if (_37_valueOrError18).IsFailure() {
																	return (_37_valueOrError18).PropagateFailure()
																} else {
																	var _38_recipientPublicKey _dafny.Sequence = (_37_valueOrError18).Extract().(_dafny.Sequence)
																	_ = _38_recipientPublicKey
																	return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_PrivateECDH_(name, _7_encrypt, _9_decrypt, _26_algorithm, _28_bits, _30_encoding, _32_senderMaterial, _34_recipientMaterial, _36_senderPublicKey, _38_recipientPublicKey, _12_keyIdentifier))
																}
															}
														}
													}
												}
											}
										}
									}
								}
								{
									var _39_valueOrError19 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("algorithm"), _1_obj)
									_ = _39_valueOrError19
									if (_39_valueOrError19).IsFailure() {
										return (_39_valueOrError19).PropagateFailure()
									} else {
										var _40_algorithm _dafny.Sequence = (_39_valueOrError19).Extract().(_dafny.Sequence)
										_ = _40_algorithm
										var _41_valueOrError20 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetNat(_dafny.SeqOfString("bits"), _1_obj)
										_ = _41_valueOrError20
										if (_41_valueOrError20).IsFailure() {
											return (_41_valueOrError20).PropagateFailure()
										} else {
											var _42_bits _dafny.Int = (_41_valueOrError20).Extract().(_dafny.Int)
											_ = _42_bits
											var _43_valueOrError21 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("encoding"), _1_obj)
											_ = _43_valueOrError21
											if (_43_valueOrError21).IsFailure() {
												return (_43_valueOrError21).PropagateFailure()
											} else {
												var _44_encoding _dafny.Sequence = (_43_valueOrError21).Extract().(_dafny.Sequence)
												_ = _44_encoding
												var _45_valueOrError22 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Get(_dafny.SeqOfString("material"), _1_obj)
												_ = _45_valueOrError22
												if (_45_valueOrError22).IsFailure() {
													return (_45_valueOrError22).PropagateFailure()
												} else {
													var _46_material_q m_JSON_Values.JSON = (_45_valueOrError22).Extract().(m_JSON_Values.JSON)
													_ = _46_material_q
													var _47_valueOrError23 m_Wrappers.Result = func() m_Wrappers.Result {
														var _source2 m_JSON_Values.JSON = _46_material_q
														_ = _source2
														{
															if _source2.Is_String() {
																var _48_str _dafny.Sequence = _source2.Get_().(m_JSON_Values.JSON_String).Str
																_ = _48_str
																return m_Wrappers.Companion_Result_.Create_Success_(_48_str)
															}
														}
														{
															if _source2.Is_Array() {
																var _49_arr _dafny.Sequence = _source2.Get_().(m_JSON_Values.JSON_Array).Arr
																_ = _49_arr
																var _50_valueOrError24 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(((_dafny.IntOfUint32((_49_arr).Cardinality())).Sign() == 1) && (_dafny.Quantifier((_49_arr).UniqueElements(), true, func(_forall_var_0 m_JSON_Values.JSON) bool {
																	var _51_s m_JSON_Values.JSON
																	_51_s = interface{}(_forall_var_0).(m_JSON_Values.JSON)
																	return !(_dafny.Companion_Sequence_.Contains(_49_arr, _51_s)) || ((_51_s).Is_String())
																})), _dafny.SeqOfString("Unsupported material shape."))
																_ = _50_valueOrError24
																if (_50_valueOrError24).IsFailure() {
																	return (_50_valueOrError24).PropagateFailure()
																} else {
																	var _52_strings _dafny.Sequence = m_Seq.Companion_Default___.Map(func(coer9 func(m_JSON_Values.JSON) _dafny.Sequence) func(interface{}) interface{} {
																		return func(arg9 interface{}) interface{} {
																			return coer9(arg9.(m_JSON_Values.JSON))
																		}
																	}(func(_53_s m_JSON_Values.JSON) _dafny.Sequence {
																		return (_53_s).Dtor_str()
																	}), _49_arr)
																	_ = _52_strings
																	var _54_material _dafny.Sequence = m_StandardLibrary.Companion_Default___.Join(_52_strings, _dafny.SeqOfString("\n"))
																	_ = _54_material
																	return m_Wrappers.Companion_Result_.Create_Success_(_54_material)
																}
															}
														}
														{
															return m_Wrappers.Companion_Result_.Create_Failure_(_dafny.SeqOfString("Unsupported material shape."))
														}
													}()
													_ = _47_valueOrError23
													if (_47_valueOrError23).IsFailure() {
														return (_47_valueOrError23).PropagateFailure()
													} else {
														var _55_material _dafny.Sequence = (_47_valueOrError23).Extract().(_dafny.Sequence)
														_ = _55_material
														var _source3 _dafny.Sequence = _4_typ
														_ = _source3
														{
															if (_source3).Equals(_dafny.SeqOfString("symmetric")) {
																var _56_valueOrError25 m_Wrappers.Result = m_Base64.Companion_Default___.Decode(_55_material)
																_ = _56_valueOrError25
																if (_56_valueOrError25).IsFailure() {
																	return (_56_valueOrError25).PropagateFailure()
																} else {
																	var _57_materialBytes _dafny.Sequence = (_56_valueOrError25).Extract().(_dafny.Sequence)
																	_ = _57_materialBytes
																	return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_Symetric_(name, _7_encrypt, _9_decrypt, _40_algorithm, _42_bits, _44_encoding, _57_materialBytes, _12_keyIdentifier))
																}
															}
														}
														{
															if (_source3).Equals(_dafny.SeqOfString("private")) {
																return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_PrivateRSA_(name, _7_encrypt, _9_decrypt, _40_algorithm, _42_bits, _44_encoding, _55_material, _12_keyIdentifier))
															}
														}
														{
															if (_source3).Equals(_dafny.SeqOfString("public")) {
																return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_PublicRSA_(name, _7_encrypt, _9_decrypt, _42_bits, _40_algorithm, _44_encoding, _55_material, _12_keyIdentifier))
															}
														}
														{
															var _58_valueOrError26 m_Wrappers.Result = m_UTF8.Encode(_55_material)
															_ = _58_valueOrError26
															if (_58_valueOrError26).IsFailure() {
																return (_58_valueOrError26).PropagateFailure()
															} else {
																var _59_publicKey _dafny.Sequence = (_58_valueOrError26).Extract().(_dafny.Sequence)
																_ = _59_publicKey
																return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_KMSAsymetric_(name, _7_encrypt, _9_decrypt, _12_keyIdentifier, _42_bits, _40_algorithm, _44_encoding, _59_publicKey))
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToStaticMaterial(mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient, name _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.GetAlgorithmSuiteInfo(mpl, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = (_0_valueOrError0).Extract().(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
		_ = _1_algorithmSuite
		var _2_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.SmallObjectToStringStringMap(_dafny.SeqOfString("encryptionContext"), obj)
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_encryptionContextStrings _dafny.Map = (_2_valueOrError1).Extract().(_dafny.Map)
			_ = _3_encryptionContextStrings
			var _4_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeMap(_3_encryptionContextStrings)
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				var _5_encryptionContext _dafny.Map = (_4_valueOrError2).Extract().(_dafny.Map)
				_ = _5_encryptionContext
				var _6_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetArrayString(_dafny.SeqOfString("requiredEncryptionContextKeys"), obj)
				_ = _6_valueOrError3
				if (_6_valueOrError3).IsFailure() {
					return (_6_valueOrError3).PropagateFailure()
				} else {
					var _7_keysAsStrings _dafny.Sequence = (_6_valueOrError3).Extract().(_dafny.Sequence)
					_ = _7_keysAsStrings
					var _8_valueOrError4 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeSeq(_7_keysAsStrings)
					_ = _8_valueOrError4
					if (_8_valueOrError4).IsFailure() {
						return (_8_valueOrError4).PropagateFailure()
					} else {
						var _9_requiredEncryptionContextKeys _dafny.Sequence = (_8_valueOrError4).Extract().(_dafny.Sequence)
						_ = _9_requiredEncryptionContextKeys
						var _10_valueOrError5 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetArrayObject(_dafny.SeqOfString("encryptedDataKeys"), obj)
						_ = _10_valueOrError5
						if (_10_valueOrError5).IsFailure() {
							return (_10_valueOrError5).PropagateFailure()
						} else {
							var _11_encryptedDataKeysJSON _dafny.Sequence = (_10_valueOrError5).Extract().(_dafny.Sequence)
							_ = _11_encryptedDataKeysJSON
							var _12_valueOrError6 m_Wrappers.Result = m_Seq.Companion_Default___.MapWithResult(func(coer10 func(_dafny.Sequence) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
								return func(arg10 interface{}) m_Wrappers.Result {
									return coer10(arg10.(_dafny.Sequence))
								}
							}(Companion_Default___.ToEncryptedDataKey), _11_encryptedDataKeysJSON)
							_ = _12_valueOrError6
							if (_12_valueOrError6).IsFailure() {
								return (_12_valueOrError6).PropagateFailure()
							} else {
								var _13_encryptedDataKeys _dafny.Sequence = (_12_valueOrError6).Extract().(_dafny.Sequence)
								_ = _13_encryptedDataKeys
								var _14_valueOrError7 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("plaintextDataKey"), obj)
								_ = _14_valueOrError7
								if (_14_valueOrError7).IsFailure() {
									return (_14_valueOrError7).PropagateFailure()
								} else {
									var _15_plaintextDataKeyEncoded m_Wrappers.Option = (_14_valueOrError7).Extract().(m_Wrappers.Option)
									_ = _15_plaintextDataKeyEncoded
									var _16_valueOrError8 m_Wrappers.Result = (func() m_Wrappers.Result {
										if (_15_plaintextDataKeyEncoded).Is_Some() {
											return func(_pat_let6_0 m_Wrappers.Result) m_Wrappers.Result {
												return func(_17_result m_Wrappers.Result) m_Wrappers.Result {
													return (func() m_Wrappers.Result {
														if (_17_result).Is_Success() {
															return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_((_17_result).Dtor_value().(_dafny.Sequence)))
														}
														return m_Wrappers.Companion_Result_.Create_Failure_((_17_result).Dtor_error().(_dafny.Sequence))
													})()
												}(_pat_let6_0)
											}(m_Base64.Companion_Default___.Decode((_15_plaintextDataKeyEncoded).Dtor_value().(_dafny.Sequence)))
										}
										return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
									})()
									_ = _16_valueOrError8
									if (_16_valueOrError8).IsFailure() {
										return (_16_valueOrError8).PropagateFailure()
									} else {
										var _18_plaintextDataKey m_Wrappers.Option = (_16_valueOrError8).Extract().(m_Wrappers.Option)
										_ = _18_plaintextDataKey
										var _19_valueOrError9 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("signingKey"), obj)
										_ = _19_valueOrError9
										if (_19_valueOrError9).IsFailure() {
											return (_19_valueOrError9).PropagateFailure()
										} else {
											var _20_signingKey m_Wrappers.Option = (_19_valueOrError9).Extract().(m_Wrappers.Option)
											_ = _20_signingKey
											var _21_valueOrError10 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("verificationKey"), obj)
											_ = _21_valueOrError10
											if (_21_valueOrError10).IsFailure() {
												return (_21_valueOrError10).PropagateFailure()
											} else {
												var _22_verificationKey m_Wrappers.Option = (_21_valueOrError10).Extract().(m_Wrappers.Option)
												_ = _22_verificationKey
												var _23_symmetricSigningKeys m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.GetArrayString(_dafny.SeqOfString("symmetricSigningKeys"), obj)).ToOption()
												_ = _23_symmetricSigningKeys
												return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_StaticMaterial_(name, _1_algorithmSuite, _5_encryptionContext, _13_encryptedDataKeys, _9_requiredEncryptionContextKeys, _18_plaintextDataKey, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_()))
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToStaticBranchKey(mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient, name _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("key-id"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_keyIdentifier _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_keyIdentifier
		var _2_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("branchKeyVersion"), obj)
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_branchKeyVersionEncoded _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
			_ = _3_branchKeyVersionEncoded
			var _4_valueOrError2 m_Wrappers.Result = m_UTF8.Encode(_3_branchKeyVersionEncoded)
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				var _5_branchKeyVersion _dafny.Sequence = (_4_valueOrError2).Extract().(_dafny.Sequence)
				_ = _5_branchKeyVersion
				var _6_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("branchKey"), obj)
				_ = _6_valueOrError3
				if (_6_valueOrError3).IsFailure() {
					return (_6_valueOrError3).PropagateFailure()
				} else {
					var _7_branchKeyEncoded _dafny.Sequence = (_6_valueOrError3).Extract().(_dafny.Sequence)
					_ = _7_branchKeyEncoded
					var _8_valueOrError4 m_Wrappers.Result = m_Base64.Companion_Default___.Decode(_7_branchKeyEncoded)
					_ = _8_valueOrError4
					if (_8_valueOrError4).IsFailure() {
						return (_8_valueOrError4).PropagateFailure()
					} else {
						var _9_branchKey _dafny.Sequence = (_8_valueOrError4).Extract().(_dafny.Sequence)
						_ = _9_branchKey
						var _10_valueOrError5 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("beaconKey"), obj)
						_ = _10_valueOrError5
						if (_10_valueOrError5).IsFailure() {
							return (_10_valueOrError5).PropagateFailure()
						} else {
							var _11_beaconKeyEncoded _dafny.Sequence = (_10_valueOrError5).Extract().(_dafny.Sequence)
							_ = _11_beaconKeyEncoded
							var _12_valueOrError6 m_Wrappers.Result = m_Base64.Companion_Default___.Decode(_11_beaconKeyEncoded)
							_ = _12_valueOrError6
							if (_12_valueOrError6).IsFailure() {
								return (_12_valueOrError6).PropagateFailure()
							} else {
								var _13_beaconKey _dafny.Sequence = (_12_valueOrError6).Extract().(_dafny.Sequence)
								_ = _13_beaconKey
								return m_Wrappers.Companion_Result_.Create_Success_(Companion_KeyMaterial_.Create_StaticKeyStoreInformation_(_1_keyIdentifier, _5_branchKeyVersion, _9_branchKey, _13_beaconKey))
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToEncryptedDataKey(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("keyProviderId"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_keyProviderIdJSON _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_keyProviderIdJSON
		var _2_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("keyProviderInfo"), obj)
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_keyProviderInfoJSON _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
			_ = _3_keyProviderInfoJSON
			var _4_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("ciphertext"), obj)
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				var _5_ciphertextJSON _dafny.Sequence = (_4_valueOrError2).Extract().(_dafny.Sequence)
				_ = _5_ciphertextJSON
				var _6_valueOrError3 m_Wrappers.Result = m_UTF8.Encode(_1_keyProviderIdJSON)
				_ = _6_valueOrError3
				if (_6_valueOrError3).IsFailure() {
					return (_6_valueOrError3).PropagateFailure()
				} else {
					var _7_keyProviderId _dafny.Sequence = (_6_valueOrError3).Extract().(_dafny.Sequence)
					_ = _7_keyProviderId
					var _8_valueOrError4 m_Wrappers.Result = m_Base64.Companion_Default___.Decode(_3_keyProviderInfoJSON)
					_ = _8_valueOrError4
					if (_8_valueOrError4).IsFailure() {
						return (_8_valueOrError4).PropagateFailure()
					} else {
						var _9_keyProviderInfo _dafny.Sequence = (_8_valueOrError4).Extract().(_dafny.Sequence)
						_ = _9_keyProviderInfo
						var _10_valueOrError5 m_Wrappers.Result = m_Base64.Companion_Default___.Decode(_5_ciphertextJSON)
						_ = _10_valueOrError5
						if (_10_valueOrError5).IsFailure() {
							return (_10_valueOrError5).PropagateFailure()
						} else {
							var _11_ciphertext _dafny.Sequence = (_10_valueOrError5).Extract().(_dafny.Sequence)
							_ = _11_ciphertext
							return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptedDataKey_.Create_EncryptedDataKey_(_7_keyProviderId, _9_keyProviderInfo, _11_ciphertext))
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) GetAlgorithmSuiteInfo(mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("algorithmSuiteId"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_algorithmSuiteHex _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_algorithmSuiteHex
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(m_HexStrings.Companion_Default___.IsLooseHexString(_1_algorithmSuiteHex), _dafny.SeqOfString("Not hex encoded binary"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_binaryId _dafny.Sequence = m_HexStrings.Companion_Default___.FromHexString(_1_algorithmSuiteHex)
			_ = _3_binaryId
			return ((mpl).GetAlgorithmSuiteInfo(_3_binaryId)).MapFailure(func(coer11 func(m_AwsCryptographyMaterialProvidersTypes.Error) _dafny.Sequence) func(interface{}) interface{} {
				return func(arg11 interface{}) interface{} {
					return coer11(arg11.(m_AwsCryptographyMaterialProvidersTypes.Error))
				}
			}((func(_4_algorithmSuiteHex _dafny.Sequence) func(m_AwsCryptographyMaterialProvidersTypes.Error) _dafny.Sequence {
				return func(_5_e m_AwsCryptographyMaterialProvidersTypes.Error) _dafny.Sequence {
					return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Invalid Suite:"), _4_algorithmSuiteHex)
				}
			})(_1_algorithmSuiteHex)))
		}
	}
}
func (_static *CompanionStruct_Default___) KeyMaterialString_q(s _dafny.Sequence) bool {
	return ((((((((_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("static-material"))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("symmetric")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("private")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("public")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("static-branch-key")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms-rsa")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("ecc-private")))) || (_dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfString("aws-kms-ecdh")))
}

// End of class Default__

// Definition of datatype KeyMaterial
type KeyMaterial struct {
	Data_KeyMaterial_
}

func (_this KeyMaterial) Get_() Data_KeyMaterial_ {
	return _this.Data_KeyMaterial_
}

type Data_KeyMaterial_ interface {
	isKeyMaterial()
}

type CompanionStruct_KeyMaterial_ struct {
}

var Companion_KeyMaterial_ = CompanionStruct_KeyMaterial_{}

type KeyMaterial_Symetric struct {
	Name          _dafny.Sequence
	Encrypt       bool
	Decrypt       bool
	Algorithm     _dafny.Sequence
	Bits          _dafny.Int
	Encoding      _dafny.Sequence
	WrappingKey   _dafny.Sequence
	KeyIdentifier _dafny.Sequence
}

func (KeyMaterial_Symetric) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_Symetric_(Name _dafny.Sequence, Encrypt bool, Decrypt bool, Algorithm _dafny.Sequence, Bits _dafny.Int, Encoding _dafny.Sequence, WrappingKey _dafny.Sequence, KeyIdentifier _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_Symetric{Name, Encrypt, Decrypt, Algorithm, Bits, Encoding, WrappingKey, KeyIdentifier}}
}

func (_this KeyMaterial) Is_Symetric() bool {
	_, ok := _this.Get_().(KeyMaterial_Symetric)
	return ok
}

type KeyMaterial_PrivateRSA struct {
	Name          _dafny.Sequence
	Encrypt       bool
	Decrypt       bool
	Algorithm     _dafny.Sequence
	Bits          _dafny.Int
	Encoding      _dafny.Sequence
	Material      _dafny.Sequence
	KeyIdentifier _dafny.Sequence
}

func (KeyMaterial_PrivateRSA) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_PrivateRSA_(Name _dafny.Sequence, Encrypt bool, Decrypt bool, Algorithm _dafny.Sequence, Bits _dafny.Int, Encoding _dafny.Sequence, Material _dafny.Sequence, KeyIdentifier _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_PrivateRSA{Name, Encrypt, Decrypt, Algorithm, Bits, Encoding, Material, KeyIdentifier}}
}

func (_this KeyMaterial) Is_PrivateRSA() bool {
	_, ok := _this.Get_().(KeyMaterial_PrivateRSA)
	return ok
}

type KeyMaterial_PublicRSA struct {
	Name          _dafny.Sequence
	Encrypt       bool
	Decrypt       bool
	Bits          _dafny.Int
	Algorithm     _dafny.Sequence
	Encoding      _dafny.Sequence
	Material      _dafny.Sequence
	KeyIdentifier _dafny.Sequence
}

func (KeyMaterial_PublicRSA) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_PublicRSA_(Name _dafny.Sequence, Encrypt bool, Decrypt bool, Bits _dafny.Int, Algorithm _dafny.Sequence, Encoding _dafny.Sequence, Material _dafny.Sequence, KeyIdentifier _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_PublicRSA{Name, Encrypt, Decrypt, Bits, Algorithm, Encoding, Material, KeyIdentifier}}
}

func (_this KeyMaterial) Is_PublicRSA() bool {
	_, ok := _this.Get_().(KeyMaterial_PublicRSA)
	return ok
}

type KeyMaterial_PrivateECDH struct {
	Name               _dafny.Sequence
	Encrypt            bool
	Decrypt            bool
	Algorithm          _dafny.Sequence
	Bits               _dafny.Int
	Encoding           _dafny.Sequence
	SenderMaterial     _dafny.Sequence
	RecipientMaterial  _dafny.Sequence
	SenderPublicKey    _dafny.Sequence
	RecipientPublicKey _dafny.Sequence
	KeyIdentifier      _dafny.Sequence
}

func (KeyMaterial_PrivateECDH) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_PrivateECDH_(Name _dafny.Sequence, Encrypt bool, Decrypt bool, Algorithm _dafny.Sequence, Bits _dafny.Int, Encoding _dafny.Sequence, SenderMaterial _dafny.Sequence, RecipientMaterial _dafny.Sequence, SenderPublicKey _dafny.Sequence, RecipientPublicKey _dafny.Sequence, KeyIdentifier _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_PrivateECDH{Name, Encrypt, Decrypt, Algorithm, Bits, Encoding, SenderMaterial, RecipientMaterial, SenderPublicKey, RecipientPublicKey, KeyIdentifier}}
}

func (_this KeyMaterial) Is_PrivateECDH() bool {
	_, ok := _this.Get_().(KeyMaterial_PrivateECDH)
	return ok
}

type KeyMaterial_KMS struct {
	Name          _dafny.Sequence
	Encrypt       bool
	Decrypt       bool
	KeyIdentifier _dafny.Sequence
}

func (KeyMaterial_KMS) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_KMS_(Name _dafny.Sequence, Encrypt bool, Decrypt bool, KeyIdentifier _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_KMS{Name, Encrypt, Decrypt, KeyIdentifier}}
}

func (_this KeyMaterial) Is_KMS() bool {
	_, ok := _this.Get_().(KeyMaterial_KMS)
	return ok
}

type KeyMaterial_KMSAsymetric struct {
	Name          _dafny.Sequence
	Encrypt       bool
	Decrypt       bool
	KeyIdentifier _dafny.Sequence
	Bits          _dafny.Int
	Algorithm     _dafny.Sequence
	Encoding      _dafny.Sequence
	PublicKey     _dafny.Sequence
}

func (KeyMaterial_KMSAsymetric) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_KMSAsymetric_(Name _dafny.Sequence, Encrypt bool, Decrypt bool, KeyIdentifier _dafny.Sequence, Bits _dafny.Int, Algorithm _dafny.Sequence, Encoding _dafny.Sequence, PublicKey _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_KMSAsymetric{Name, Encrypt, Decrypt, KeyIdentifier, Bits, Algorithm, Encoding, PublicKey}}
}

func (_this KeyMaterial) Is_KMSAsymetric() bool {
	_, ok := _this.Get_().(KeyMaterial_KMSAsymetric)
	return ok
}

type KeyMaterial_KMSEcdh struct {
	Name               _dafny.Sequence
	Encrypt            bool
	Decrypt            bool
	KeyIdentifier      _dafny.Sequence
	Algorithm          _dafny.Sequence
	SenderMaterial     _dafny.Sequence
	RecipientMaterial  _dafny.Sequence
	SenderPublicKey    _dafny.Sequence
	RecipientPublicKey _dafny.Sequence
}

func (KeyMaterial_KMSEcdh) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_KMSEcdh_(Name _dafny.Sequence, Encrypt bool, Decrypt bool, KeyIdentifier _dafny.Sequence, Algorithm _dafny.Sequence, SenderMaterial _dafny.Sequence, RecipientMaterial _dafny.Sequence, SenderPublicKey _dafny.Sequence, RecipientPublicKey _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_KMSEcdh{Name, Encrypt, Decrypt, KeyIdentifier, Algorithm, SenderMaterial, RecipientMaterial, SenderPublicKey, RecipientPublicKey}}
}

func (_this KeyMaterial) Is_KMSEcdh() bool {
	_, ok := _this.Get_().(KeyMaterial_KMSEcdh)
	return ok
}

type KeyMaterial_StaticMaterial struct {
	Name                          _dafny.Sequence
	AlgorithmSuite                m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	EncryptionContext             _dafny.Map
	EncryptedDataKeys             _dafny.Sequence
	RequiredEncryptionContextKeys _dafny.Sequence
	PlaintextDataKey              m_Wrappers.Option
	SigningKey                    m_Wrappers.Option
	VerificationKey               m_Wrappers.Option
	SymmetricSigningKeys          m_Wrappers.Option
}

func (KeyMaterial_StaticMaterial) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_StaticMaterial_(Name _dafny.Sequence, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, EncryptionContext _dafny.Map, EncryptedDataKeys _dafny.Sequence, RequiredEncryptionContextKeys _dafny.Sequence, PlaintextDataKey m_Wrappers.Option, SigningKey m_Wrappers.Option, VerificationKey m_Wrappers.Option, SymmetricSigningKeys m_Wrappers.Option) KeyMaterial {
	return KeyMaterial{KeyMaterial_StaticMaterial{Name, AlgorithmSuite, EncryptionContext, EncryptedDataKeys, RequiredEncryptionContextKeys, PlaintextDataKey, SigningKey, VerificationKey, SymmetricSigningKeys}}
}

func (_this KeyMaterial) Is_StaticMaterial() bool {
	_, ok := _this.Get_().(KeyMaterial_StaticMaterial)
	return ok
}

type KeyMaterial_StaticKeyStoreInformation struct {
	KeyIdentifier    _dafny.Sequence
	BranchKeyVersion _dafny.Sequence
	BranchKey        _dafny.Sequence
	BeaconKey        _dafny.Sequence
}

func (KeyMaterial_StaticKeyStoreInformation) isKeyMaterial() {}

func (CompanionStruct_KeyMaterial_) Create_StaticKeyStoreInformation_(KeyIdentifier _dafny.Sequence, BranchKeyVersion _dafny.Sequence, BranchKey _dafny.Sequence, BeaconKey _dafny.Sequence) KeyMaterial {
	return KeyMaterial{KeyMaterial_StaticKeyStoreInformation{KeyIdentifier, BranchKeyVersion, BranchKey, BeaconKey}}
}

func (_this KeyMaterial) Is_StaticKeyStoreInformation() bool {
	_, ok := _this.Get_().(KeyMaterial_StaticKeyStoreInformation)
	return ok
}

func (CompanionStruct_KeyMaterial_) Default() KeyMaterial {
	return Companion_KeyMaterial_.Create_Symetric_(_dafny.EmptySeq.SetString(), false, false, _dafny.EmptySeq.SetString(), _dafny.Zero, _dafny.EmptySeq.SetString(), _dafny.EmptySeq, _dafny.EmptySeq.SetString())
}

func (_this KeyMaterial) Dtor_name() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		return data.Name
	case KeyMaterial_PrivateRSA:
		return data.Name
	case KeyMaterial_PublicRSA:
		return data.Name
	case KeyMaterial_PrivateECDH:
		return data.Name
	case KeyMaterial_KMS:
		return data.Name
	case KeyMaterial_KMSAsymetric:
		return data.Name
	case KeyMaterial_KMSEcdh:
		return data.Name
	default:
		return data.(KeyMaterial_StaticMaterial).Name
	}
}

func (_this KeyMaterial) Dtor_encrypt() bool {
	switch data := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		return data.Encrypt
	case KeyMaterial_PrivateRSA:
		return data.Encrypt
	case KeyMaterial_PublicRSA:
		return data.Encrypt
	case KeyMaterial_PrivateECDH:
		return data.Encrypt
	case KeyMaterial_KMS:
		return data.Encrypt
	case KeyMaterial_KMSAsymetric:
		return data.Encrypt
	default:
		return data.(KeyMaterial_KMSEcdh).Encrypt
	}
}

func (_this KeyMaterial) Dtor_decrypt() bool {
	switch data := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		return data.Decrypt
	case KeyMaterial_PrivateRSA:
		return data.Decrypt
	case KeyMaterial_PublicRSA:
		return data.Decrypt
	case KeyMaterial_PrivateECDH:
		return data.Decrypt
	case KeyMaterial_KMS:
		return data.Decrypt
	case KeyMaterial_KMSAsymetric:
		return data.Decrypt
	default:
		return data.(KeyMaterial_KMSEcdh).Decrypt
	}
}

func (_this KeyMaterial) Dtor_algorithm() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		return data.Algorithm
	case KeyMaterial_PrivateRSA:
		return data.Algorithm
	case KeyMaterial_PublicRSA:
		return data.Algorithm
	case KeyMaterial_PrivateECDH:
		return data.Algorithm
	case KeyMaterial_KMSAsymetric:
		return data.Algorithm
	default:
		return data.(KeyMaterial_KMSEcdh).Algorithm
	}
}

func (_this KeyMaterial) Dtor_bits() _dafny.Int {
	switch data := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		return data.Bits
	case KeyMaterial_PrivateRSA:
		return data.Bits
	case KeyMaterial_PublicRSA:
		return data.Bits
	case KeyMaterial_PrivateECDH:
		return data.Bits
	default:
		return data.(KeyMaterial_KMSAsymetric).Bits
	}
}

func (_this KeyMaterial) Dtor_encoding() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		return data.Encoding
	case KeyMaterial_PrivateRSA:
		return data.Encoding
	case KeyMaterial_PublicRSA:
		return data.Encoding
	case KeyMaterial_PrivateECDH:
		return data.Encoding
	default:
		return data.(KeyMaterial_KMSAsymetric).Encoding
	}
}

func (_this KeyMaterial) Dtor_wrappingKey() _dafny.Sequence {
	return _this.Get_().(KeyMaterial_Symetric).WrappingKey
}

func (_this KeyMaterial) Dtor_keyIdentifier() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		return data.KeyIdentifier
	case KeyMaterial_PrivateRSA:
		return data.KeyIdentifier
	case KeyMaterial_PublicRSA:
		return data.KeyIdentifier
	case KeyMaterial_PrivateECDH:
		return data.KeyIdentifier
	case KeyMaterial_KMS:
		return data.KeyIdentifier
	case KeyMaterial_KMSAsymetric:
		return data.KeyIdentifier
	case KeyMaterial_KMSEcdh:
		return data.KeyIdentifier
	default:
		return data.(KeyMaterial_StaticKeyStoreInformation).KeyIdentifier
	}
}

func (_this KeyMaterial) Dtor_material() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_PrivateRSA:
		return data.Material
	default:
		return data.(KeyMaterial_PublicRSA).Material
	}
}

func (_this KeyMaterial) Dtor_senderMaterial() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_PrivateECDH:
		return data.SenderMaterial
	default:
		return data.(KeyMaterial_KMSEcdh).SenderMaterial
	}
}

func (_this KeyMaterial) Dtor_recipientMaterial() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_PrivateECDH:
		return data.RecipientMaterial
	default:
		return data.(KeyMaterial_KMSEcdh).RecipientMaterial
	}
}

func (_this KeyMaterial) Dtor_senderPublicKey() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_PrivateECDH:
		return data.SenderPublicKey
	default:
		return data.(KeyMaterial_KMSEcdh).SenderPublicKey
	}
}

func (_this KeyMaterial) Dtor_recipientPublicKey() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case KeyMaterial_PrivateECDH:
		return data.RecipientPublicKey
	default:
		return data.(KeyMaterial_KMSEcdh).RecipientPublicKey
	}
}

func (_this KeyMaterial) Dtor_publicKey() _dafny.Sequence {
	return _this.Get_().(KeyMaterial_KMSAsymetric).PublicKey
}

func (_this KeyMaterial) Dtor_algorithmSuite() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	return _this.Get_().(KeyMaterial_StaticMaterial).AlgorithmSuite
}

func (_this KeyMaterial) Dtor_encryptionContext() _dafny.Map {
	return _this.Get_().(KeyMaterial_StaticMaterial).EncryptionContext
}

func (_this KeyMaterial) Dtor_encryptedDataKeys() _dafny.Sequence {
	return _this.Get_().(KeyMaterial_StaticMaterial).EncryptedDataKeys
}

func (_this KeyMaterial) Dtor_requiredEncryptionContextKeys() _dafny.Sequence {
	return _this.Get_().(KeyMaterial_StaticMaterial).RequiredEncryptionContextKeys
}

func (_this KeyMaterial) Dtor_plaintextDataKey() m_Wrappers.Option {
	return _this.Get_().(KeyMaterial_StaticMaterial).PlaintextDataKey
}

func (_this KeyMaterial) Dtor_signingKey() m_Wrappers.Option {
	return _this.Get_().(KeyMaterial_StaticMaterial).SigningKey
}

func (_this KeyMaterial) Dtor_verificationKey() m_Wrappers.Option {
	return _this.Get_().(KeyMaterial_StaticMaterial).VerificationKey
}

func (_this KeyMaterial) Dtor_symmetricSigningKeys() m_Wrappers.Option {
	return _this.Get_().(KeyMaterial_StaticMaterial).SymmetricSigningKeys
}

func (_this KeyMaterial) Dtor_branchKeyVersion() _dafny.Sequence {
	return _this.Get_().(KeyMaterial_StaticKeyStoreInformation).BranchKeyVersion
}

func (_this KeyMaterial) Dtor_branchKey() _dafny.Sequence {
	return _this.Get_().(KeyMaterial_StaticKeyStoreInformation).BranchKey
}

func (_this KeyMaterial) Dtor_beaconKey() _dafny.Sequence {
	return _this.Get_().(KeyMaterial_StaticKeyStoreInformation).BeaconKey
}

func (_this KeyMaterial) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case KeyMaterial_Symetric:
		{
			return "KeyMaterial.KeyMaterial.Symetric" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Encrypt) + ", " + _dafny.String(data.Decrypt) + ", " + _dafny.String(data.Algorithm) + ", " + _dafny.String(data.Bits) + ", " + _dafny.String(data.Encoding) + ", " + _dafny.String(data.WrappingKey) + ", " + _dafny.String(data.KeyIdentifier) + ")"
		}
	case KeyMaterial_PrivateRSA:
		{
			return "KeyMaterial.KeyMaterial.PrivateRSA" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Encrypt) + ", " + _dafny.String(data.Decrypt) + ", " + _dafny.String(data.Algorithm) + ", " + _dafny.String(data.Bits) + ", " + _dafny.String(data.Encoding) + ", " + _dafny.String(data.Material) + ", " + _dafny.String(data.KeyIdentifier) + ")"
		}
	case KeyMaterial_PublicRSA:
		{
			return "KeyMaterial.KeyMaterial.PublicRSA" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Encrypt) + ", " + _dafny.String(data.Decrypt) + ", " + _dafny.String(data.Bits) + ", " + _dafny.String(data.Algorithm) + ", " + _dafny.String(data.Encoding) + ", " + _dafny.String(data.Material) + ", " + _dafny.String(data.KeyIdentifier) + ")"
		}
	case KeyMaterial_PrivateECDH:
		{
			return "KeyMaterial.KeyMaterial.PrivateECDH" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Encrypt) + ", " + _dafny.String(data.Decrypt) + ", " + _dafny.String(data.Algorithm) + ", " + _dafny.String(data.Bits) + ", " + _dafny.String(data.Encoding) + ", " + _dafny.String(data.SenderMaterial) + ", " + _dafny.String(data.RecipientMaterial) + ", " + _dafny.String(data.SenderPublicKey) + ", " + _dafny.String(data.RecipientPublicKey) + ", " + _dafny.String(data.KeyIdentifier) + ")"
		}
	case KeyMaterial_KMS:
		{
			return "KeyMaterial.KeyMaterial.KMS" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Encrypt) + ", " + _dafny.String(data.Decrypt) + ", " + _dafny.String(data.KeyIdentifier) + ")"
		}
	case KeyMaterial_KMSAsymetric:
		{
			return "KeyMaterial.KeyMaterial.KMSAsymetric" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Encrypt) + ", " + _dafny.String(data.Decrypt) + ", " + _dafny.String(data.KeyIdentifier) + ", " + _dafny.String(data.Bits) + ", " + _dafny.String(data.Algorithm) + ", " + _dafny.String(data.Encoding) + ", " + _dafny.String(data.PublicKey) + ")"
		}
	case KeyMaterial_KMSEcdh:
		{
			return "KeyMaterial.KeyMaterial.KMSEcdh" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Encrypt) + ", " + _dafny.String(data.Decrypt) + ", " + _dafny.String(data.KeyIdentifier) + ", " + _dafny.String(data.Algorithm) + ", " + _dafny.String(data.SenderMaterial) + ", " + _dafny.String(data.RecipientMaterial) + ", " + _dafny.String(data.SenderPublicKey) + ", " + _dafny.String(data.RecipientPublicKey) + ")"
		}
	case KeyMaterial_StaticMaterial:
		{
			return "KeyMaterial.KeyMaterial.StaticMaterial" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.EncryptionContext) + ", " + _dafny.String(data.EncryptedDataKeys) + ", " + _dafny.String(data.RequiredEncryptionContextKeys) + ", " + _dafny.String(data.PlaintextDataKey) + ", " + _dafny.String(data.SigningKey) + ", " + _dafny.String(data.VerificationKey) + ", " + _dafny.String(data.SymmetricSigningKeys) + ")"
		}
	case KeyMaterial_StaticKeyStoreInformation:
		{
			return "KeyMaterial.KeyMaterial.StaticKeyStoreInformation" + "(" + _dafny.String(data.KeyIdentifier) + ", " + _dafny.String(data.BranchKeyVersion) + ", " + _dafny.String(data.BranchKey) + ", " + _dafny.String(data.BeaconKey) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this KeyMaterial) Equals(other KeyMaterial) bool {
	switch data1 := _this.Get_().(type) {
	case KeyMaterial_Symetric:
		{
			data2, ok := other.Get_().(KeyMaterial_Symetric)
			return ok && data1.Name.Equals(data2.Name) && data1.Encrypt == data2.Encrypt && data1.Decrypt == data2.Decrypt && data1.Algorithm.Equals(data2.Algorithm) && data1.Bits.Cmp(data2.Bits) == 0 && data1.Encoding.Equals(data2.Encoding) && data1.WrappingKey.Equals(data2.WrappingKey) && data1.KeyIdentifier.Equals(data2.KeyIdentifier)
		}
	case KeyMaterial_PrivateRSA:
		{
			data2, ok := other.Get_().(KeyMaterial_PrivateRSA)
			return ok && data1.Name.Equals(data2.Name) && data1.Encrypt == data2.Encrypt && data1.Decrypt == data2.Decrypt && data1.Algorithm.Equals(data2.Algorithm) && data1.Bits.Cmp(data2.Bits) == 0 && data1.Encoding.Equals(data2.Encoding) && data1.Material.Equals(data2.Material) && data1.KeyIdentifier.Equals(data2.KeyIdentifier)
		}
	case KeyMaterial_PublicRSA:
		{
			data2, ok := other.Get_().(KeyMaterial_PublicRSA)
			return ok && data1.Name.Equals(data2.Name) && data1.Encrypt == data2.Encrypt && data1.Decrypt == data2.Decrypt && data1.Bits.Cmp(data2.Bits) == 0 && data1.Algorithm.Equals(data2.Algorithm) && data1.Encoding.Equals(data2.Encoding) && data1.Material.Equals(data2.Material) && data1.KeyIdentifier.Equals(data2.KeyIdentifier)
		}
	case KeyMaterial_PrivateECDH:
		{
			data2, ok := other.Get_().(KeyMaterial_PrivateECDH)
			return ok && data1.Name.Equals(data2.Name) && data1.Encrypt == data2.Encrypt && data1.Decrypt == data2.Decrypt && data1.Algorithm.Equals(data2.Algorithm) && data1.Bits.Cmp(data2.Bits) == 0 && data1.Encoding.Equals(data2.Encoding) && data1.SenderMaterial.Equals(data2.SenderMaterial) && data1.RecipientMaterial.Equals(data2.RecipientMaterial) && data1.SenderPublicKey.Equals(data2.SenderPublicKey) && data1.RecipientPublicKey.Equals(data2.RecipientPublicKey) && data1.KeyIdentifier.Equals(data2.KeyIdentifier)
		}
	case KeyMaterial_KMS:
		{
			data2, ok := other.Get_().(KeyMaterial_KMS)
			return ok && data1.Name.Equals(data2.Name) && data1.Encrypt == data2.Encrypt && data1.Decrypt == data2.Decrypt && data1.KeyIdentifier.Equals(data2.KeyIdentifier)
		}
	case KeyMaterial_KMSAsymetric:
		{
			data2, ok := other.Get_().(KeyMaterial_KMSAsymetric)
			return ok && data1.Name.Equals(data2.Name) && data1.Encrypt == data2.Encrypt && data1.Decrypt == data2.Decrypt && data1.KeyIdentifier.Equals(data2.KeyIdentifier) && data1.Bits.Cmp(data2.Bits) == 0 && data1.Algorithm.Equals(data2.Algorithm) && data1.Encoding.Equals(data2.Encoding) && data1.PublicKey.Equals(data2.PublicKey)
		}
	case KeyMaterial_KMSEcdh:
		{
			data2, ok := other.Get_().(KeyMaterial_KMSEcdh)
			return ok && data1.Name.Equals(data2.Name) && data1.Encrypt == data2.Encrypt && data1.Decrypt == data2.Decrypt && data1.KeyIdentifier.Equals(data2.KeyIdentifier) && data1.Algorithm.Equals(data2.Algorithm) && data1.SenderMaterial.Equals(data2.SenderMaterial) && data1.RecipientMaterial.Equals(data2.RecipientMaterial) && data1.SenderPublicKey.Equals(data2.SenderPublicKey) && data1.RecipientPublicKey.Equals(data2.RecipientPublicKey)
		}
	case KeyMaterial_StaticMaterial:
		{
			data2, ok := other.Get_().(KeyMaterial_StaticMaterial)
			return ok && data1.Name.Equals(data2.Name) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.EncryptionContext.Equals(data2.EncryptionContext) && data1.EncryptedDataKeys.Equals(data2.EncryptedDataKeys) && data1.RequiredEncryptionContextKeys.Equals(data2.RequiredEncryptionContextKeys) && data1.PlaintextDataKey.Equals(data2.PlaintextDataKey) && data1.SigningKey.Equals(data2.SigningKey) && data1.VerificationKey.Equals(data2.VerificationKey) && data1.SymmetricSigningKeys.Equals(data2.SymmetricSigningKeys)
		}
	case KeyMaterial_StaticKeyStoreInformation:
		{
			data2, ok := other.Get_().(KeyMaterial_StaticKeyStoreInformation)
			return ok && data1.KeyIdentifier.Equals(data2.KeyIdentifier) && data1.BranchKeyVersion.Equals(data2.BranchKeyVersion) && data1.BranchKey.Equals(data2.BranchKey) && data1.BeaconKey.Equals(data2.BeaconKey)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this KeyMaterial) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(KeyMaterial)
	return ok && _this.Equals(typed)
}

func Type_KeyMaterial_() _dafny.TypeDescriptor {
	return type_KeyMaterial_{}
}

type type_KeyMaterial_ struct {
}

func (_this type_KeyMaterial_) Default() interface{} {
	return Companion_KeyMaterial_.Default()
}

func (_this type_KeyMaterial_) String() string {
	return "KeyMaterial.KeyMaterial"
}
func (_this KeyMaterial) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = KeyMaterial{}

// End of datatype KeyMaterial
