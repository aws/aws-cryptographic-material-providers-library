// Package JSONHelpers
// Dafny module JSONHelpers compiled into Go

package JSONHelpers

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
	return "JSONHelpers.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) BvToBytes(bits _dafny.Sequence) _dafny.Sequence {
	return _dafny.SeqCreate((_dafny.IntOfUint32((bits).Cardinality())).Uint32(), func(coer0 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg0 _dafny.Int) interface{} {
			return coer0(arg0)
		}
	}((func(_0_bits _dafny.Sequence) func(_dafny.Int) uint8 {
		return func(_1_i _dafny.Int) uint8 {
			return uint8((_0_bits).Select((_1_i).Uint32()).(uint8))
		}
	})(bits)))
}
func (_static *CompanionStruct_Default___) BytesBv(bits _dafny.Sequence) _dafny.Sequence {
	return _dafny.SeqCreate((_dafny.IntOfUint32((bits).Cardinality())).Uint32(), func(coer1 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg1 _dafny.Int) interface{} {
			return coer1(arg1)
		}
	}((func(_0_bits _dafny.Sequence) func(_dafny.Int) uint8 {
		return func(_1_i _dafny.Int) uint8 {
			return uint8((_0_bits).Select((_1_i).Uint32()).(uint8))
		}
	})(bits)))
}
func (_static *CompanionStruct_Default___) Get(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (_dafny.IntOfUint32((obj).Cardinality())).Sign() == 0 {
		return m_Wrappers.Companion_Result_.Create_Failure_(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Key: "), key), _dafny.SeqOfString(" does not exist")))
	} else if _dafny.Companion_Sequence_.Equal((*((obj).Select(0).(_dafny.Tuple)).IndexInt(0)).(_dafny.Sequence), key) {
		return m_Wrappers.Companion_Result_.Create_Success_((*((obj).Select(0).(_dafny.Tuple)).IndexInt(1)).(m_JSON_Values.JSON))
	} else {
		var _in0 _dafny.Sequence = key
		_ = _in0
		var _in1 _dafny.Sequence = (obj).Drop(1)
		_ = _in1
		key = _in0
		obj = _in1
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) GetString(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_1_obj).Is_String(), _dafny.SeqOfString("Not a string"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_((_1_obj).Dtor_str())
		}
	}
}
func (_static *CompanionStruct_Default___) GetBool(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_1_obj).Is_Bool(), _dafny.SeqOfString("Not a bool"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_((_1_obj).Dtor_b())
		}
	}
}
func (_static *CompanionStruct_Default___) GetNat(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_1_obj).Is_Number(), _dafny.SeqOfString("Not a number"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((((_1_obj).Dtor_num()).Dtor_n()).Sign() == 1, _dafny.SeqOfString("Not a nat"))
			_ = _3_valueOrError2
			if (_3_valueOrError2).IsFailure() {
				return (_3_valueOrError2).PropagateFailure()
			} else {
				return m_Wrappers.Companion_Result_.Create_Success_(((_1_obj).Dtor_num()).Dtor_n())
			}
		}
	}
}
func (_static *CompanionStruct_Default___) GetPositiveLong(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.GetNat(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_n _dafny.Int = (_0_valueOrError0).Extract().(_dafny.Int)
		_ = _1_n
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_1_n).Cmp(_dafny.IntOfInt64(m_BoundedInts.Companion_Default___.INT64__MAX())) <= 0, _dafny.SeqOfString("Int64 Overflow"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_((_1_n).Int64())
		}
	}
}
func (_static *CompanionStruct_Default___) GetPositiveInteger(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.GetNat(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_n _dafny.Int = (_0_valueOrError0).Extract().(_dafny.Int)
		_ = _1_n
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_1_n).Cmp(_dafny.IntOfInt32(m_BoundedInts.Companion_Default___.INT32__MAX())) <= 0, _dafny.SeqOfString("Int32 Overflow"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_((_1_n).Int32())
		}
	}
}
func (_static *CompanionStruct_Default___) GetOptionalString(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_obj m_Wrappers.Option = (Companion_Default___.Get(key, obj)).ToOption()
	_ = _0_obj
	if (_0_obj).Is_Some() {
		var _1_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(((_0_obj).Dtor_value().(m_JSON_Values.JSON)).Is_String(), _dafny.SeqOfString("Not a string"))
		_ = _1_valueOrError0
		if (_1_valueOrError0).IsFailure() {
			return (_1_valueOrError0).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(((_0_obj).Dtor_value().(m_JSON_Values.JSON)).Dtor_str()))
		}
	} else {
		return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
	}
}
func (_static *CompanionStruct_Default___) GetOptionalPositiveLong(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_obj m_Wrappers.Option = (Companion_Default___.Get(key, obj)).ToOption()
	_ = _0_obj
	if (_0_obj).Is_Some() {
		var _1_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(((_0_obj).Dtor_value().(m_JSON_Values.JSON)).Is_Number(), _dafny.SeqOfString("Not a number"))
		_ = _1_valueOrError0
		if (_1_valueOrError0).IsFailure() {
			return (_1_valueOrError0).PropagateFailure()
		} else {
			var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((((((_0_obj).Dtor_value().(m_JSON_Values.JSON)).Dtor_num()).Dtor_n()).Sign() != -1) && (((((_0_obj).Dtor_value().(m_JSON_Values.JSON)).Dtor_num()).Dtor_n()).Cmp(_dafny.IntOfInt64(m_BoundedInts.Companion_Default___.INT64__MAX())) <= 0), _dafny.SeqOfString("Int64 Overflow"))
			_ = _2_valueOrError1
			if (_2_valueOrError1).IsFailure() {
				return (_2_valueOrError1).PropagateFailure()
			} else {
				return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(((((_0_obj).Dtor_value().(m_JSON_Values.JSON)).Dtor_num()).Dtor_n()).Int64()))
			}
		}
	} else {
		return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
	}
}
func (_static *CompanionStruct_Default___) GetObject(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_1_obj).Is_Object(), _dafny.SeqOfString("Not an object"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_((_1_obj).Dtor_obj())
		}
	}
}
func (_static *CompanionStruct_Default___) GetArray(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_1_obj).Is_Array(), _dafny.SeqOfString("Not an array"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_((_1_obj).Dtor_arr())
		}
	}
}
func (_static *CompanionStruct_Default___) GetArrayString(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(((_1_obj).Is_Array()) && (_dafny.Quantifier(((_1_obj).Dtor_arr()).UniqueElements(), true, func(_forall_var_0 m_JSON_Values.JSON) bool {
			var _3_s m_JSON_Values.JSON
			_3_s = interface{}(_forall_var_0).(m_JSON_Values.JSON)
			return !(_dafny.Companion_Sequence_.Contains((_1_obj).Dtor_arr(), _3_s)) || ((_3_s).Is_String())
		})), _dafny.SeqOfString("Not an array of strings"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _4_arr _dafny.Sequence = (_1_obj).Dtor_arr()
			_ = _4_arr
			return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqCreate((_dafny.IntOfUint32((_4_arr).Cardinality())).Uint32(), func(coer2 func(_dafny.Int) _dafny.Sequence) func(_dafny.Int) interface{} {
				return func(arg2 _dafny.Int) interface{} {
					return coer2(arg2)
				}
			}((func(_5_arr _dafny.Sequence) func(_dafny.Int) _dafny.Sequence {
				return func(_6_n _dafny.Int) _dafny.Sequence {
					return ((_5_arr).Select((_6_n).Uint32()).(m_JSON_Values.JSON)).Dtor_str()
				}
			})(_4_arr))))
		}
	}
}
func (_static *CompanionStruct_Default___) GetArrayObject(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(((_1_obj).Is_Array()) && (_dafny.Quantifier(((_1_obj).Dtor_arr()).UniqueElements(), true, func(_forall_var_0 m_JSON_Values.JSON) bool {
			var _3_s m_JSON_Values.JSON
			_3_s = interface{}(_forall_var_0).(m_JSON_Values.JSON)
			return !(_dafny.Companion_Sequence_.Contains((_1_obj).Dtor_arr(), _3_s)) || ((_3_s).Is_Object())
		})), _dafny.SeqOfString("Not an array of objects"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _4_arr _dafny.Sequence = (_1_obj).Dtor_arr()
			_ = _4_arr
			return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqCreate((_dafny.IntOfUint32((_4_arr).Cardinality())).Uint32(), func(coer3 func(_dafny.Int) _dafny.Sequence) func(_dafny.Int) interface{} {
				return func(arg3 _dafny.Int) interface{} {
					return coer3(arg3)
				}
			}((func(_5_arr _dafny.Sequence) func(_dafny.Int) _dafny.Sequence {
				return func(_6_n _dafny.Int) _dafny.Sequence {
					return ((_5_arr).Select((_6_n).Uint32()).(m_JSON_Values.JSON)).Dtor_obj()
				}
			})(_4_arr))))
		}
	}
}
func (_static *CompanionStruct_Default___) SmallObjectToStringStringMap(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_item m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_item
		return Companion_Default___.JsonObjectToStringStringMap(_1_item)
	}
}
func (_static *CompanionStruct_Default___) GetOptionalSmallObjectToStringStringMap(key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_item m_Wrappers.Option = (Companion_Default___.Get(key, obj)).ToOption()
	_ = _0_item
	if (_0_item).Is_Some() {
		var _1_valueOrError0 m_Wrappers.Result = Companion_Default___.JsonObjectToStringStringMap((_0_item).Dtor_value().(m_JSON_Values.JSON))
		_ = _1_valueOrError0
		if (_1_valueOrError0).IsFailure() {
			return (_1_valueOrError0).PropagateFailure()
		} else {
			var _2_m _dafny.Map = (_1_valueOrError0).Extract().(_dafny.Map)
			_ = _2_m
			return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(_2_m))
		}
	} else {
		return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
	}
}
func (_static *CompanionStruct_Default___) PrintJson(j m_JSON_Values.JSON) _dafny.Tuple {
	var _hresult _dafny.Tuple = _dafny.TupleOf()
	_ = _hresult
	_dafny.Print(j)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_hresult = _dafny.TupleOf()
	return _hresult
	return _hresult
}
func (_static *CompanionStruct_Default___) JsonObjectToStringStringMap(item m_JSON_Values.JSON) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((item).Is_Object(), _dafny.SeqOfString("Not an object"))
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj _dafny.Sequence = (item).Dtor_obj()
		_ = _1_obj
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier((_1_obj).UniqueElements(), true, func(_forall_var_0 _dafny.Tuple) bool {
			var _3_t _dafny.Tuple
			_3_t = interface{}(_forall_var_0).(_dafny.Tuple)
			return !(_dafny.Companion_Sequence_.Contains(_1_obj, _3_t)) || (((*(_3_t).IndexInt(1)).(m_JSON_Values.JSON)).Is_String())
		}), _dafny.SeqOfString("Not a string string object"))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _4_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier(_dafny.IntegerRange(_dafny.Zero, _dafny.IntOfUint32((_1_obj).Cardinality())), true, func(_forall_var_1 _dafny.Int) bool {
				var _5_i _dafny.Int
				_5_i = interface{}(_forall_var_1).(_dafny.Int)
				return _dafny.Quantifier(_dafny.IntegerRange((_5_i).Plus(_dafny.One), _dafny.IntOfUint32((_1_obj).Cardinality())), true, func(_forall_var_2 _dafny.Int) bool {
					var _6_j _dafny.Int
					_6_j = interface{}(_forall_var_2).(_dafny.Int)
					return !((((_5_i).Sign() != -1) && ((_5_i).Cmp(_6_j) < 0)) && ((_6_j).Cmp(_dafny.IntOfUint32((_1_obj).Cardinality())) < 0)) || (!_dafny.Companion_Sequence_.Equal((*((_1_obj).Select((_5_i).Uint32()).(_dafny.Tuple)).IndexInt(0)).(_dafny.Sequence), (*((_1_obj).Select((_6_j).Uint32()).(_dafny.Tuple)).IndexInt(0)).(_dafny.Sequence)))
				})
			}), _dafny.SeqOfString("JSON serialization Error"))
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				return m_Wrappers.Companion_Result_.Create_Success_(func() _dafny.Map {
					var _coll0 = _dafny.NewMapBuilder()
					_ = _coll0
					for _iter2 := _dafny.Iterate((_1_obj).Elements()); ; {
						_compr_0, _ok2 := _iter2()
						if !_ok2 {
							break
						}
						var _7_t _dafny.Tuple
						_7_t = interface{}(_compr_0).(_dafny.Tuple)
						if _dafny.Companion_Sequence_.Contains(_1_obj, _7_t) {
							_coll0.Add((*(_7_t).IndexInt(0)).(_dafny.Sequence), ((*(_7_t).IndexInt(1)).(m_JSON_Values.JSON)).Dtor_str())
						}
					}
					return _coll0.ToMap()
				}())
			}
		}
	}
}
func (_static *CompanionStruct_Default___) Utf8EncodePair(key _dafny.Sequence, value _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_UTF8.Encode(key)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_utf8Key _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_utf8Key
		var _2_valueOrError1 m_Wrappers.Result = m_UTF8.Encode(value)
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_utf8Value _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
			_ = _3_utf8Value
			return m_Wrappers.Companion_Result_.Create_Success_(_dafny.TupleOf(_1_utf8Key, _3_utf8Value))
		}
	}
}
func (_static *CompanionStruct_Default___) Utf8EncodeMap(mapStringString _dafny.Map) m_Wrappers.Result {
	if ((mapStringString).Cardinality()).Sign() == 0 {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.NewMapBuilder().ToMap())
	} else {
		var _0_encodedResults _dafny.Map = func() _dafny.Map {
			var _coll0 = _dafny.NewMapBuilder()
			_ = _coll0
			for _iter3 := _dafny.Iterate((mapStringString).Keys().Elements()); ; {
				_compr_0, _ok3 := _iter3()
				if !_ok3 {
					break
				}
				var _1_key _dafny.Sequence
				_1_key = interface{}(_compr_0).(_dafny.Sequence)
				if (mapStringString).Contains(_1_key) {
					_coll0.Add(_1_key, Companion_Default___.Utf8EncodePair(_1_key, (mapStringString).Get(_1_key).(_dafny.Sequence)))
				}
			}
			return _coll0.ToMap()
		}()
		_ = _0_encodedResults
		var _2_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier(((_0_encodedResults).Values()).Elements(), true, func(_forall_var_0 m_Wrappers.Result) bool {
			var _3_r m_Wrappers.Result
			_3_r = interface{}(_forall_var_0).(m_Wrappers.Result)
			return !(((_0_encodedResults).Values()).Contains(_3_r)) || ((_3_r).Is_Success())
		}), _dafny.SeqOfString("String can not be UTF8 Encoded?"))
		_ = _2_valueOrError0
		if (_2_valueOrError0).IsFailure() {
			return (_2_valueOrError0).PropagateFailure()
		} else {
			return m_Wrappers.Companion_Result_.Create_Success_(func() _dafny.Map {
				var _coll1 = _dafny.NewMapBuilder()
				_ = _coll1
				for _iter4 := _dafny.Iterate(((_0_encodedResults).Values()).Elements()); ; {
					_compr_1, _ok4 := _iter4()
					if !_ok4 {
						break
					}
					var _4_r m_Wrappers.Result
					_4_r = interface{}(_compr_1).(m_Wrappers.Result)
					if ((_0_encodedResults).Values()).Contains(_4_r) {
						_coll1.Add((*((_4_r).Dtor_value().(_dafny.Tuple)).IndexInt(0)).(_dafny.Sequence), (*((_4_r).Dtor_value().(_dafny.Tuple)).IndexInt(1)).(_dafny.Sequence))
					}
				}
				return _coll1.ToMap()
			}())
		}
	}
}
func (_static *CompanionStruct_Default___) Utf8EncodeSeq(seqOfStrings _dafny.Sequence) m_Wrappers.Result {
	var _0_encodedResults _dafny.Sequence = _dafny.SeqCreate((_dafny.IntOfUint32((seqOfStrings).Cardinality())).Uint32(), func(coer4 func(_dafny.Int) m_Wrappers.Result) func(_dafny.Int) interface{} {
		return func(arg4 _dafny.Int) interface{} {
			return coer4(arg4)
		}
	}((func(_1_seqOfStrings _dafny.Sequence) func(_dafny.Int) m_Wrappers.Result {
		return func(_2_i _dafny.Int) m_Wrappers.Result {
			return m_UTF8.Encode((_1_seqOfStrings).Select((_2_i).Uint32()).(_dafny.Sequence))
		}
	})(seqOfStrings)))
	_ = _0_encodedResults
	var _3_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(_dafny.Quantifier((_0_encodedResults).UniqueElements(), true, func(_forall_var_0 m_Wrappers.Result) bool {
		var _4_r m_Wrappers.Result
		_4_r = interface{}(_forall_var_0).(m_Wrappers.Result)
		return !(_dafny.Companion_Sequence_.Contains(_0_encodedResults, _4_r)) || ((_4_r).Is_Success())
	}), _dafny.SeqOfString("String can not be UTF8 Encoded?"))
	_ = _3_valueOrError0
	if (_3_valueOrError0).IsFailure() {
		return (_3_valueOrError0).PropagateFailure()
	} else {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqCreate((_dafny.IntOfUint32((_0_encodedResults).Cardinality())).Uint32(), func(coer5 func(_dafny.Int) _dafny.Sequence) func(_dafny.Int) interface{} {
			return func(arg5 _dafny.Int) interface{} {
				return coer5(arg5)
			}
		}((func(_5_encodedResults _dafny.Sequence) func(_dafny.Int) _dafny.Sequence {
			return func(_6_i _dafny.Int) _dafny.Sequence {
				return ((_5_encodedResults).Select((_6_i).Uint32()).(m_Wrappers.Result)).Dtor_value().(_dafny.Sequence)
			}
		})(_0_encodedResults))))
	}
}

// End of class Default__
