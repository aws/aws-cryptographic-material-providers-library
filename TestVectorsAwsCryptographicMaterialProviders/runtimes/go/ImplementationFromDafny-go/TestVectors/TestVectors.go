// Package TestVectors
// Dafny module TestVectors compiled into Go

package TestVectors

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
	m_CmmFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CmmFromKeyDescription"
	m_CreateStaticKeyStores "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyStores"
	m_CreateStaticKeyrings "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyrings"
	m_JSONHelpers "github.com/aws/aws-cryptographic-material-providers-library/testvectors/JSONHelpers"
	m_KeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyDescription"
	m_KeyMaterial "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyMaterial"
	m_KeyVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyVectors"
	m_KeyringFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyringFromKeyDescription"
	m_KeysVectorOperations "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeysVectorOperations"
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
var _ m_KeyMaterial.Dummy__
var _ m_CreateStaticKeyrings.Dummy__
var _ m_CreateStaticKeyStores.Dummy__
var _ m_KeyringFromKeyDescription.Dummy__
var _ m_CmmFromKeyDescription.Dummy__
var _ m_KeysVectorOperations.Dummy__
var _ m_KeyVectors.Dummy__

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
	return "TestVectors.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestGetEncryptionMaterials(test EncryptTest) (bool, m_Wrappers.Option) {
	var testResult bool = false
	_ = testResult
	var materials m_Wrappers.Option = m_Wrappers.Companion_Option_.Default()
	_ = materials
	_dafny.Print((_dafny.SeqOfString("\nTEST===> ")).SetString())
	_dafny.Print((((test).Dtor_vector()).Dtor_name()).SetString())
	_dafny.Print(((func() _dafny.Sequence {
		if (((test).Dtor_vector()).Dtor_description()).Is_Some() {
			return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("\n"), (((test).Dtor_vector()).Dtor_description()).Dtor_value().(_dafny.Sequence))
		}
		return _dafny.SeqOfString("")
	})()).SetString())
	_dafny.Print(((func() _dafny.Sequence {
		if ((test).Dtor_vector()).Is_NegativeEncryptKeyringVector() {

			return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("\n"), ((test).Dtor_vector()).Dtor_errorDescription())
		}
		return _dafny.SeqOfString("")
	})()).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	var _0_result m_Wrappers.Result
	_ = _0_result
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = ((test).Dtor_cmm()).GetEncryptionMaterials((test).Dtor_input())
	// // fmt.Println(_out0)
	_0_result = _out0
	var _source0 EncryptTestVector = (test).Dtor_vector()
	_ = _source0
	{
		{
			if _source0.Is_PositiveEncryptKeyringVector() {
				testResult = (_0_result).Is_Success()
				goto Lmatch0
			}
		}
		{
			if _source0.Is_PositiveEncryptNegativeDecryptKeyringVector() {
				testResult = (_0_result).Is_Success()
				goto Lmatch0
			}
		}
		{
			testResult = !((_0_result).Is_Success())
		}
		goto Lmatch0
	}
Lmatch0:
	if (testResult) && ((_0_result).Is_Success()) {
		materials = m_Wrappers.Companion_Option_.Create_Some_(((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsOutput)).Dtor_encryptionMaterials())
	} else {
		materials = m_Wrappers.Companion_Option_.Create_None_()
	}
	if !(testResult) {
		if (((test).Dtor_vector()).Is_PositiveEncryptKeyringVector()) || (((test).Dtor_vector()).Is_PositiveEncryptNegativeDecryptKeyringVector()) {
			_dafny.Print((_0_result).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error))
		}
		_dafny.Print((_dafny.SeqOfString("\nFAILED! <-----------\n")).SetString())
	}
	return testResult, materials
}
func (_static *CompanionStruct_Default___) TestDecryptMaterials(test DecryptTest) bool {
	var output bool = false
	_ = output
	_dafny.Print((_dafny.SeqOfString("\nTEST===> ")).SetString())
	_dafny.Print((((test).Dtor_vector()).Dtor_name()).SetString())

	_dafny.Print(((func() _dafny.Sequence {
		if (((test).Dtor_vector()).Dtor_description()).Is_Some() {
			return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("\n"), (((test).Dtor_vector()).Dtor_description()).Dtor_value().(_dafny.Sequence))
		}
		return _dafny.SeqOfString("")
	})()).SetString())
	_dafny.Print(((func() _dafny.Sequence {
		if ((test).Dtor_vector()).Is_NegativeDecryptKeyringTest() {
			return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("\n"), ((test).Dtor_vector()).Dtor_errorDescription())
		}
		return _dafny.SeqOfString("\n")
	})()).SetString())
	var _0_result m_Wrappers.Result
	_ = _0_result
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = ((test).Dtor_cmm()).DecryptMaterials((test).Dtor_input())
	_0_result = _out0
	var _source0 DecryptTestVector = (test).Dtor_vector()
	_ = _source0
	{
		{
			if _source0.Is_PositiveDecryptKeyringTest() {
				output = ((((_0_result).Is_Success()) && (((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_plaintextDataKey()).Equals((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_plaintextDataKey()))) && (((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_symmetricSigningKey()).Equals((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_symmetricSigningKey()))) && ((_dafny.MultiSetFromSeq((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_requiredEncryptionContextKeys())).Equals(_dafny.MultiSetFromSeq((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_requiredEncryptionContextKeys())))
				goto Lmatch0
			}
		}
		{
			output = !((_0_result).Is_Success())
		}
		goto Lmatch0
	}
Lmatch0:
	if !(output) {
		if ((test).Dtor_vector()).Is_PositiveDecryptKeyringTest() {
			if (_0_result).Is_Failure() {
				_dafny.Print((_dafny.SeqOfString("Error : ")).SetString())
				_dafny.Print((_0_result).Dtor_error().(m_AwsCryptographyMaterialProvidersTypes.Error).Dtor_list())
				_dafny.Print((_dafny.SeqOfString("\n")).SetString())
			} else {
				if !((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_plaintextDataKey()).Equals((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_plaintextDataKey()) {
					_dafny.Print((_dafny.SeqOfString("Error : plaintextDataKey does not match.\n")).SetString())
					_dafny.Print((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_plaintextDataKey())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_dafny.Print((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_plaintextDataKey())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
				}
				if !((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_symmetricSigningKey()).Equals((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_symmetricSigningKey()) {
					_dafny.Print((_dafny.SeqOfString("Error : symmetricSigningKey does not match.\n")).SetString())
					_dafny.Print((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_symmetricSigningKey())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_dafny.Print((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_symmetricSigningKey())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
				}
				if !(_dafny.MultiSetFromSeq((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_requiredEncryptionContextKeys())).Equals(_dafny.MultiSetFromSeq((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_requiredEncryptionContextKeys())) {
					_dafny.Print((_dafny.SeqOfString("Error : requiredEncryptionContextKeys does not match.\n")).SetString())
					_dafny.Print(_dafny.IntOfUint32(((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_requiredEncryptionContextKeys()).Cardinality()))
					_dafny.Print((_dafny.SeqOfString(" ")).SetString())
					_dafny.Print(_dafny.IntOfUint32(((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_requiredEncryptionContextKeys()).Cardinality()))
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_dafny.Print((((test).Dtor_vector()).Dtor_expectedResult()).Dtor_requiredEncryptionContextKeys())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
					_dafny.Print((((_0_result).Dtor_value().(m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput)).Dtor_decryptionMaterials()).Dtor_requiredEncryptionContextKeys())
					_dafny.Print((_dafny.SeqOfString("\n")).SetString())
				}
			}
		}
		_dafny.Print((_dafny.SeqOfString("\nFAILED! <-----------\n")).SetString())
	}
	return output
}
func (_static *CompanionStruct_Default___) ToEncryptTest(keys *m_KeyVectors.KeyVectorsClient, vector EncryptTestVector) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_input m_AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput
	_ = _0_input
	var _source0 EncryptTestVector = vector
	_ = _source0
	{
		{
			if _source0.Is_PositiveEncryptKeyringVector() {
				_0_input = m_AwsCryptographyMaterialProvidersTypes.Companion_GetEncryptionMaterialsInput_.Create_GetEncryptionMaterialsInput_((vector).Dtor_encryptionContext(), (vector).Dtor_commitmentPolicy(), m_Wrappers.Companion_Option_.Create_Some_(((vector).Dtor_algorithmSuite()).Dtor_id()), (vector).Dtor_maxPlaintextLength(), (vector).Dtor_requiredEncryptionContextKeys())
				goto Lmatch0
			}
		}
		{
			if _source0.Is_NegativeEncryptKeyringVector() {
				_0_input = m_AwsCryptographyMaterialProvidersTypes.Companion_GetEncryptionMaterialsInput_.Create_GetEncryptionMaterialsInput_((vector).Dtor_encryptionContext(), (vector).Dtor_commitmentPolicy(), m_Wrappers.Companion_Option_.Create_Some_(((vector).Dtor_algorithmSuite()).Dtor_id()), (vector).Dtor_maxPlaintextLength(), (vector).Dtor_requiredEncryptionContextKeys())
				goto Lmatch0
			}
		}
		{
			_0_input = m_AwsCryptographyMaterialProvidersTypes.Companion_GetEncryptionMaterialsInput_.Create_GetEncryptionMaterialsInput_((vector).Dtor_encryptionContext(), (vector).Dtor_commitmentPolicy(), m_Wrappers.Companion_Option_.Create_Some_(((vector).Dtor_algorithmSuite()).Dtor_id()), (vector).Dtor_maxPlaintextLength(), (vector).Dtor_requiredEncryptionContextKeys())
		}
		goto Lmatch0
	}
Lmatch0:
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _1_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_WrappedMaterialProviders.Companion_Default___.WrappedMaterialProviders(m_WrappedMaterialProviders.Companion_Default___.WrappedDefaultMaterialProvidersConfig())
	_1_valueOrError0 = _out0
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(151,15): " + (_1_valueOrError0).String())
	}
	var _2_mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
	_ = _2_mpl
	_2_mpl = m_AwsCryptographyMaterialProvidersTypes.Companion_IAwsCryptographicMaterialProvidersClient_.CastTo_((_1_valueOrError0).Extract())
	var _3_cmm_k m_Wrappers.Result
	_ = _3_cmm_k
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (keys).CreateWrappedTestVectorCmm(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_TestVectorCmmInput_.Create_TestVectorCmmInput_((func() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
		if (vector).Is_PositiveEncryptKeyringVector() {
			return (vector).Dtor_encryptDescription()
		}
		return (func() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
			if (vector).Is_PositiveEncryptNegativeDecryptKeyringVector() {
				return (vector).Dtor_encryptDescription()
			}
			return (vector).Dtor_keyDescription()
		})()
	})(), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_CmmOperation_.Create_ENCRYPT_()))
	_3_cmm_k = _out1
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	//// fmt.Println(_3_cmm_k)
	_4_valueOrError1 = (_3_cmm_k).MapFailure(func(coer52 func(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) _dafny.Sequence) func(interface{}) interface{} {
		return func(arg52 interface{}) interface{} {
			return coer52(arg52.(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error))
		}
	}(func(_5_e m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) _dafny.Sequence {
		return func(_pat_let7_0 _dafny.Tuple) _dafny.Sequence {
			return func(_6___v78 _dafny.Tuple) _dafny.Sequence {
				return _dafny.SeqOfString("Cmm failure")
			}(_pat_let7_0)
		}(Companion_Default___.PrintErr(_5_e))
	}))
	if (_4_valueOrError1).IsFailure() {
		output = (_4_valueOrError1).PropagateFailure()
		return output
	}
	var _7_cmm m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
	_ = _7_cmm
	_7_cmm = m_AwsCryptographyMaterialProvidersTypes.Companion_ICryptographicMaterialsManager_.CastTo_((_4_valueOrError1).Extract())
	output = m_Wrappers.Companion_Result_.Create_Success_(Companion_EncryptTest_.Create_EncryptTest_(_0_input, _7_cmm, vector))
	return output
	return output
}
func (_static *CompanionStruct_Default___) EncryptTestToDecryptVector(test EncryptTest, materials m_AwsCryptographyMaterialProvidersTypes.EncryptionMaterials) DecryptTestVector {
	var _0_keysToRemove _dafny.Set = m_Seq.Companion_Default___.ToSet((((test).Dtor_vector()).Dtor_requiredEncryptionContextKeys()).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence))
	_ = _0_keysToRemove
	var _source0 EncryptTestVector = (test).Dtor_vector()
	_ = _source0
	{
		if _source0.Is_PositiveEncryptKeyringVector() {
			return Companion_DecryptTestVector_.Create_PositiveDecryptKeyringTest_(_dafny.Companion_Sequence_.Concatenate(((test).Dtor_vector()).Dtor_name(), _dafny.SeqOfString("->Decryption")), ((test).Dtor_vector()).Dtor_algorithmSuite(), ((test).Dtor_vector()).Dtor_commitmentPolicy(), (materials).Dtor_encryptedDataKeys(), ((materials).Dtor_encryptionContext()).Subtract(_0_keysToRemove), ((test).Dtor_vector()).Dtor_decryptDescription(), Companion_DecryptResult_.Create_DecryptResult_((materials).Dtor_plaintextDataKey(), (func() m_Wrappers.Option {
				if (((materials).Dtor_symmetricSigningKeys()).Is_Some()) && ((_dafny.IntOfUint32((((materials).Dtor_symmetricSigningKeys()).Dtor_value().(_dafny.Sequence)).Cardinality())).Sign() == 1) {
					return m_Wrappers.Companion_Option_.Create_Some_((((materials).Dtor_symmetricSigningKeys()).Dtor_value().(_dafny.Sequence)).Select(0).(_dafny.Sequence))
				}
				return m_Wrappers.Companion_Option_.Create_None_()
			})(), (((test).Dtor_vector()).Dtor_requiredEncryptionContextKeys()).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence)), (func() m_Wrappers.Option {
				if (((test).Dtor_vector()).Dtor_description()).Is_Some() {
					return m_Wrappers.Companion_Option_.Create_Some_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Decryption for "), (((test).Dtor_vector()).Dtor_description()).Dtor_value().(_dafny.Sequence)))
				}
				return m_Wrappers.Companion_Option_.Create_None_()
			})(), ((test).Dtor_vector()).Dtor_reproducedEncryptionContext())
		}
	}
	{
		return Companion_DecryptTestVector_.Create_NegativeDecryptKeyringTest_(_dafny.Companion_Sequence_.Concatenate(((test).Dtor_vector()).Dtor_name(), _dafny.SeqOfString("->Decryption")), ((test).Dtor_vector()).Dtor_algorithmSuite(), ((test).Dtor_vector()).Dtor_commitmentPolicy(), (materials).Dtor_encryptedDataKeys(), (((test).Dtor_vector()).Dtor_encryptionContext()).Subtract(_0_keysToRemove), ((test).Dtor_vector()).Dtor_decryptErrorDescription(), ((test).Dtor_vector()).Dtor_decryptDescription(), ((test).Dtor_vector()).Dtor_reproducedEncryptionContext(), (func() m_Wrappers.Option {
			if (((test).Dtor_vector()).Dtor_description()).Is_Some() {
				return m_Wrappers.Companion_Option_.Create_Some_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Decryption for "), (((test).Dtor_vector()).Dtor_description()).Dtor_value().(_dafny.Sequence)))
			}
			return m_Wrappers.Companion_Option_.Create_None_()
		})())
	}
}
func (_static *CompanionStruct_Default___) DecryptVectorToDecryptTest(keys *m_KeyVectors.KeyVectorsClient, vector DecryptTestVector) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_input m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput
	_ = _0_input
	_0_input = m_AwsCryptographyMaterialProvidersTypes.Companion_DecryptMaterialsInput_.Create_DecryptMaterialsInput_(((vector).Dtor_algorithmSuite()).Dtor_id(), (vector).Dtor_commitmentPolicy(), (vector).Dtor_encryptedDataKeys(), (vector).Dtor_encryptionContext(), (vector).Dtor_reproducedEncryptionContext())
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _1_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_WrappedMaterialProviders.Companion_Default___.WrappedMaterialProviders(m_WrappedMaterialProviders.Companion_Default___.WrappedDefaultMaterialProvidersConfig())
	_1_valueOrError0 = _out0
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(236,15): " + (_1_valueOrError0).String())
	}
	var _2_mpl m_AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
	_ = _2_mpl
	_2_mpl = m_AwsCryptographyMaterialProvidersTypes.Companion_IAwsCryptographicMaterialProvidersClient_.CastTo_((_1_valueOrError0).Extract())
	var _3_cmm_k m_Wrappers.Result
	_ = _3_cmm_k
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (keys).CreateWrappedTestVectorCmm(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_TestVectorCmmInput_.Create_TestVectorCmmInput_((vector).Dtor_keyDescription(), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_CmmOperation_.Create_DECRYPT_()))
	_3_cmm_k = _out1
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _4_valueOrError1
	_4_valueOrError1 = (_3_cmm_k).MapFailure(func(coer53 func(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) _dafny.Sequence) func(interface{}) interface{} {
		return func(arg53 interface{}) interface{} {
			return coer53(arg53.(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error))
		}
	}(Companion_Default___.ErrorToString))
	if (_4_valueOrError1).IsFailure() {
		output = (_4_valueOrError1).PropagateFailure()
		return output
	}
	var _5_cmm m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
	_ = _5_cmm
	_5_cmm = m_AwsCryptographyMaterialProvidersTypes.Companion_ICryptographicMaterialsManager_.CastTo_((_4_valueOrError1).Extract())
	output = m_Wrappers.Companion_Result_.Create_Success_(Companion_DecryptTest_.Create_DecryptTest_(_0_input, _5_cmm, vector))
	return output
	return output
}
func (_static *CompanionStruct_Default___) ErrorToString(e m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) _dafny.Sequence {
	var _source0 m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error = e
	_ = _source0
	{
		if _source0.Is_KeyVectorException() {
			var _0_message _dafny.Sequence = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException).Message
			_ = _0_message
			return _0_message
		}
	}
	{
		if _source0.Is_AwsCryptographyMaterialProviders() {
			var _1_mplError m_AwsCryptographyMaterialProvidersTypes.Error = _source0.Get_().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders).AwsCryptographyMaterialProviders
			_ = _1_mplError
			var _source1 m_AwsCryptographyMaterialProvidersTypes.Error = _1_mplError
			_ = _source1
			{
				if _source1.Is_AwsCryptographicMaterialProvidersException() {
					var _2_message _dafny.Sequence = _source1.Get_().(m_AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException).Message
					_ = _2_message
					return _2_message
				}
			}
			{
				return _dafny.SeqOfString("Unmapped AwsCryptographyMaterialProviders")
			}
		}
	}
	{
		return _dafny.SeqOfString("Unmapped KeyVectorException")
	}
}
func (_static *CompanionStruct_Default___) PrintErr(e m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) _dafny.Tuple {
	var _hresult _dafny.Tuple = _dafny.TupleOf()
	_ = _hresult
	_dafny.Print(e)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_hresult = _dafny.TupleOf()
	return _hresult
	return _hresult
}

// End of class Default__

// Definition of datatype EncryptTest
type EncryptTest struct {
	Data_EncryptTest_
}

func (_this EncryptTest) Get_() Data_EncryptTest_ {
	return _this.Data_EncryptTest_
}

type Data_EncryptTest_ interface {
	isEncryptTest()
}

type CompanionStruct_EncryptTest_ struct {
}

var Companion_EncryptTest_ = CompanionStruct_EncryptTest_{}

type EncryptTest_EncryptTest struct {
	Input  m_AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput
	Cmm    m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
	Vector EncryptTestVector
}

func (EncryptTest_EncryptTest) isEncryptTest() {}

func (CompanionStruct_EncryptTest_) Create_EncryptTest_(Input m_AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput, Cmm m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Vector EncryptTestVector) EncryptTest {
	return EncryptTest{EncryptTest_EncryptTest{Input, Cmm, Vector}}
}

func (_this EncryptTest) Is_EncryptTest() bool {
	_, ok := _this.Get_().(EncryptTest_EncryptTest)
	return ok
}

func (CompanionStruct_EncryptTest_) Default() EncryptTest {
	return Companion_EncryptTest_.Create_EncryptTest_(m_AwsCryptographyMaterialProvidersTypes.Companion_GetEncryptionMaterialsInput_.Default(), (m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager)(nil), Companion_EncryptTestVector_.Default())
}

func (_this EncryptTest) Dtor_input() m_AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput {
	return _this.Get_().(EncryptTest_EncryptTest).Input
}

func (_this EncryptTest) Dtor_cmm() m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager {
	return _this.Get_().(EncryptTest_EncryptTest).Cmm
}

func (_this EncryptTest) Dtor_vector() EncryptTestVector {
	return _this.Get_().(EncryptTest_EncryptTest).Vector
}

func (_this EncryptTest) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case EncryptTest_EncryptTest:
		{
			return "TestVectors.EncryptTest.EncryptTest" + "(" + _dafny.String(data.Input) + ", " + _dafny.String(data.Cmm) + ", " + _dafny.String(data.Vector) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this EncryptTest) Equals(other EncryptTest) bool {
	switch data1 := _this.Get_().(type) {
	case EncryptTest_EncryptTest:
		{
			data2, ok := other.Get_().(EncryptTest_EncryptTest)
			return ok && data1.Input.Equals(data2.Input) && _dafny.AreEqual(data1.Cmm, data2.Cmm) && data1.Vector.Equals(data2.Vector)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this EncryptTest) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(EncryptTest)
	return ok && _this.Equals(typed)
}

func Type_EncryptTest_() _dafny.TypeDescriptor {
	return type_EncryptTest_{}
}

type type_EncryptTest_ struct {
}

func (_this type_EncryptTest_) Default() interface{} {
	return Companion_EncryptTest_.Default()
}

func (_this type_EncryptTest_) String() string {
	return "TestVectors.EncryptTest"
}
func (_this EncryptTest) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = EncryptTest{}

// End of datatype EncryptTest

// Definition of datatype DecryptTest
type DecryptTest struct {
	Data_DecryptTest_
}

func (_this DecryptTest) Get_() Data_DecryptTest_ {
	return _this.Data_DecryptTest_
}

type Data_DecryptTest_ interface {
	isDecryptTest()
}

type CompanionStruct_DecryptTest_ struct {
}

var Companion_DecryptTest_ = CompanionStruct_DecryptTest_{}

type DecryptTest_DecryptTest struct {
	Input  m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput
	Cmm    m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
	Vector DecryptTestVector
}

func (DecryptTest_DecryptTest) isDecryptTest() {}

func (CompanionStruct_DecryptTest_) Create_DecryptTest_(Input m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput, Cmm m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Vector DecryptTestVector) DecryptTest {
	return DecryptTest{DecryptTest_DecryptTest{Input, Cmm, Vector}}
}

func (_this DecryptTest) Is_DecryptTest() bool {
	_, ok := _this.Get_().(DecryptTest_DecryptTest)
	return ok
}

func (CompanionStruct_DecryptTest_) Default() DecryptTest {
	return Companion_DecryptTest_.Create_DecryptTest_(m_AwsCryptographyMaterialProvidersTypes.Companion_DecryptMaterialsInput_.Default(), (m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager)(nil), Companion_DecryptTestVector_.Default())
}

func (_this DecryptTest) Dtor_input() m_AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput {
	return _this.Get_().(DecryptTest_DecryptTest).Input
}

func (_this DecryptTest) Dtor_cmm() m_AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager {
	return _this.Get_().(DecryptTest_DecryptTest).Cmm
}

func (_this DecryptTest) Dtor_vector() DecryptTestVector {
	return _this.Get_().(DecryptTest_DecryptTest).Vector
}

func (_this DecryptTest) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case DecryptTest_DecryptTest:
		{
			return "TestVectors.DecryptTest.DecryptTest" + "(" + _dafny.String(data.Input) + ", " + _dafny.String(data.Cmm) + ", " + _dafny.String(data.Vector) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this DecryptTest) Equals(other DecryptTest) bool {
	switch data1 := _this.Get_().(type) {
	case DecryptTest_DecryptTest:
		{
			data2, ok := other.Get_().(DecryptTest_DecryptTest)
			return ok && data1.Input.Equals(data2.Input) && _dafny.AreEqual(data1.Cmm, data2.Cmm) && data1.Vector.Equals(data2.Vector)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this DecryptTest) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(DecryptTest)
	return ok && _this.Equals(typed)
}

func Type_DecryptTest_() _dafny.TypeDescriptor {
	return type_DecryptTest_{}
}

type type_DecryptTest_ struct {
}

func (_this type_DecryptTest_) Default() interface{} {
	return Companion_DecryptTest_.Default()
}

func (_this type_DecryptTest_) String() string {
	return "TestVectors.DecryptTest"
}
func (_this DecryptTest) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = DecryptTest{}

// End of datatype DecryptTest

// Definition of datatype EncryptTestVector
type EncryptTestVector struct {
	Data_EncryptTestVector_
}

func (_this EncryptTestVector) Get_() Data_EncryptTestVector_ {
	return _this.Data_EncryptTestVector_
}

type Data_EncryptTestVector_ interface {
	isEncryptTestVector()
}

type CompanionStruct_EncryptTestVector_ struct {
}

var Companion_EncryptTestVector_ = CompanionStruct_EncryptTestVector_{}

type EncryptTestVector_PositiveEncryptKeyringVector struct {
	Name                          _dafny.Sequence
	Description                   m_Wrappers.Option
	EncryptionContext             _dafny.Map
	CommitmentPolicy              m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
	AlgorithmSuite                m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	MaxPlaintextLength            m_Wrappers.Option
	RequiredEncryptionContextKeys m_Wrappers.Option
	EncryptDescription            m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
	DecryptDescription            m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
	ReproducedEncryptionContext   m_Wrappers.Option
}

func (EncryptTestVector_PositiveEncryptKeyringVector) isEncryptTestVector() {}

func (CompanionStruct_EncryptTestVector_) Create_PositiveEncryptKeyringVector_(Name _dafny.Sequence, Description m_Wrappers.Option, EncryptionContext _dafny.Map, CommitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, MaxPlaintextLength m_Wrappers.Option, RequiredEncryptionContextKeys m_Wrappers.Option, EncryptDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, DecryptDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, ReproducedEncryptionContext m_Wrappers.Option) EncryptTestVector {
	return EncryptTestVector{EncryptTestVector_PositiveEncryptKeyringVector{Name, Description, EncryptionContext, CommitmentPolicy, AlgorithmSuite, MaxPlaintextLength, RequiredEncryptionContextKeys, EncryptDescription, DecryptDescription, ReproducedEncryptionContext}}
}

func (_this EncryptTestVector) Is_PositiveEncryptKeyringVector() bool {
	_, ok := _this.Get_().(EncryptTestVector_PositiveEncryptKeyringVector)
	return ok
}

type EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector struct {
	Name                          _dafny.Sequence
	Description                   m_Wrappers.Option
	EncryptionContext             _dafny.Map
	CommitmentPolicy              m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
	AlgorithmSuite                m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	MaxPlaintextLength            m_Wrappers.Option
	RequiredEncryptionContextKeys m_Wrappers.Option
	DecryptErrorDescription       _dafny.Sequence
	EncryptDescription            m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
	DecryptDescription            m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
	ReproducedEncryptionContext   m_Wrappers.Option
}

func (EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) isEncryptTestVector() {}

func (CompanionStruct_EncryptTestVector_) Create_PositiveEncryptNegativeDecryptKeyringVector_(Name _dafny.Sequence, Description m_Wrappers.Option, EncryptionContext _dafny.Map, CommitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, MaxPlaintextLength m_Wrappers.Option, RequiredEncryptionContextKeys m_Wrappers.Option, DecryptErrorDescription _dafny.Sequence, EncryptDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, DecryptDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, ReproducedEncryptionContext m_Wrappers.Option) EncryptTestVector {
	return EncryptTestVector{EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector{Name, Description, EncryptionContext, CommitmentPolicy, AlgorithmSuite, MaxPlaintextLength, RequiredEncryptionContextKeys, DecryptErrorDescription, EncryptDescription, DecryptDescription, ReproducedEncryptionContext}}
}

func (_this EncryptTestVector) Is_PositiveEncryptNegativeDecryptKeyringVector() bool {
	_, ok := _this.Get_().(EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)
	return ok
}

type EncryptTestVector_NegativeEncryptKeyringVector struct {
	Name                          _dafny.Sequence
	Description                   m_Wrappers.Option
	EncryptionContext             _dafny.Map
	CommitmentPolicy              m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
	AlgorithmSuite                m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	MaxPlaintextLength            m_Wrappers.Option
	RequiredEncryptionContextKeys m_Wrappers.Option
	ErrorDescription              _dafny.Sequence
	KeyDescription                m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
}

func (EncryptTestVector_NegativeEncryptKeyringVector) isEncryptTestVector() {}

func (CompanionStruct_EncryptTestVector_) Create_NegativeEncryptKeyringVector_(Name _dafny.Sequence, Description m_Wrappers.Option, EncryptionContext _dafny.Map, CommitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, MaxPlaintextLength m_Wrappers.Option, RequiredEncryptionContextKeys m_Wrappers.Option, ErrorDescription _dafny.Sequence, KeyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription) EncryptTestVector {
	return EncryptTestVector{EncryptTestVector_NegativeEncryptKeyringVector{Name, Description, EncryptionContext, CommitmentPolicy, AlgorithmSuite, MaxPlaintextLength, RequiredEncryptionContextKeys, ErrorDescription, KeyDescription}}
}

func (_this EncryptTestVector) Is_NegativeEncryptKeyringVector() bool {
	_, ok := _this.Get_().(EncryptTestVector_NegativeEncryptKeyringVector)
	return ok
}

func (CompanionStruct_EncryptTestVector_) Default() EncryptTestVector {
	return Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.EmptySeq.SetString(), m_Wrappers.Companion_Option_.Default(), _dafny.EmptyMap, m_AwsCryptographyMaterialProvidersTypes.Companion_CommitmentPolicy_.Default(), m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Default(), m_Wrappers.Companion_Option_.Default(), m_Wrappers.Companion_Option_.Default(), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Default(), m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Default(), m_Wrappers.Companion_Option_.Default())
}

func (_this EncryptTestVector) Dtor_name() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.Name
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		return data.Name
	default:
		return data.(EncryptTestVector_NegativeEncryptKeyringVector).Name
	}
}

func (_this EncryptTestVector) Dtor_description() m_Wrappers.Option {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.Description
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		return data.Description
	default:
		return data.(EncryptTestVector_NegativeEncryptKeyringVector).Description
	}
}

func (_this EncryptTestVector) Dtor_encryptionContext() _dafny.Map {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.EncryptionContext
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		return data.EncryptionContext
	default:
		return data.(EncryptTestVector_NegativeEncryptKeyringVector).EncryptionContext
	}
}

func (_this EncryptTestVector) Dtor_commitmentPolicy() m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.CommitmentPolicy
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		return data.CommitmentPolicy
	default:
		return data.(EncryptTestVector_NegativeEncryptKeyringVector).CommitmentPolicy
	}
}

func (_this EncryptTestVector) Dtor_algorithmSuite() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.AlgorithmSuite
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		return data.AlgorithmSuite
	default:
		return data.(EncryptTestVector_NegativeEncryptKeyringVector).AlgorithmSuite
	}
}

func (_this EncryptTestVector) Dtor_maxPlaintextLength() m_Wrappers.Option {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.MaxPlaintextLength
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		return data.MaxPlaintextLength
	default:
		return data.(EncryptTestVector_NegativeEncryptKeyringVector).MaxPlaintextLength
	}
}

func (_this EncryptTestVector) Dtor_requiredEncryptionContextKeys() m_Wrappers.Option {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.RequiredEncryptionContextKeys
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		return data.RequiredEncryptionContextKeys
	default:
		return data.(EncryptTestVector_NegativeEncryptKeyringVector).RequiredEncryptionContextKeys
	}
}

func (_this EncryptTestVector) Dtor_encryptDescription() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.EncryptDescription
	default:
		return data.(EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector).EncryptDescription
	}
}

func (_this EncryptTestVector) Dtor_decryptDescription() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.DecryptDescription
	default:
		return data.(EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector).DecryptDescription
	}
}

func (_this EncryptTestVector) Dtor_reproducedEncryptionContext() m_Wrappers.Option {
	switch data := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		return data.ReproducedEncryptionContext
	default:
		return data.(EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector).ReproducedEncryptionContext
	}
}

func (_this EncryptTestVector) Dtor_decryptErrorDescription() _dafny.Sequence {
	return _this.Get_().(EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector).DecryptErrorDescription
}

func (_this EncryptTestVector) Dtor_errorDescription() _dafny.Sequence {
	return _this.Get_().(EncryptTestVector_NegativeEncryptKeyringVector).ErrorDescription
}

func (_this EncryptTestVector) Dtor_keyDescription() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	return _this.Get_().(EncryptTestVector_NegativeEncryptKeyringVector).KeyDescription
}

func (_this EncryptTestVector) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case EncryptTestVector_PositiveEncryptKeyringVector:
		{
			return "TestVectors.EncryptTestVector.PositiveEncryptKeyringVector" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Description) + ", " + _dafny.String(data.EncryptionContext) + ", " + _dafny.String(data.CommitmentPolicy) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.MaxPlaintextLength) + ", " + _dafny.String(data.RequiredEncryptionContextKeys) + ", " + _dafny.String(data.EncryptDescription) + ", " + _dafny.String(data.DecryptDescription) + ", " + _dafny.String(data.ReproducedEncryptionContext) + ")"
		}
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		{
			return "TestVectors.EncryptTestVector.PositiveEncryptNegativeDecryptKeyringVector" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Description) + ", " + _dafny.String(data.EncryptionContext) + ", " + _dafny.String(data.CommitmentPolicy) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.MaxPlaintextLength) + ", " + _dafny.String(data.RequiredEncryptionContextKeys) + ", " + _dafny.String(data.DecryptErrorDescription) + ", " + _dafny.String(data.EncryptDescription) + ", " + _dafny.String(data.DecryptDescription) + ", " + _dafny.String(data.ReproducedEncryptionContext) + ")"
		}
	case EncryptTestVector_NegativeEncryptKeyringVector:
		{
			return "TestVectors.EncryptTestVector.NegativeEncryptKeyringVector" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.Description) + ", " + _dafny.String(data.EncryptionContext) + ", " + _dafny.String(data.CommitmentPolicy) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.MaxPlaintextLength) + ", " + _dafny.String(data.RequiredEncryptionContextKeys) + ", " + _dafny.String(data.ErrorDescription) + ", " + _dafny.String(data.KeyDescription) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this EncryptTestVector) Equals(other EncryptTestVector) bool {
	switch data1 := _this.Get_().(type) {
	case EncryptTestVector_PositiveEncryptKeyringVector:
		{
			data2, ok := other.Get_().(EncryptTestVector_PositiveEncryptKeyringVector)
			return ok && data1.Name.Equals(data2.Name) && data1.Description.Equals(data2.Description) && data1.EncryptionContext.Equals(data2.EncryptionContext) && data1.CommitmentPolicy.Equals(data2.CommitmentPolicy) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.MaxPlaintextLength.Equals(data2.MaxPlaintextLength) && data1.RequiredEncryptionContextKeys.Equals(data2.RequiredEncryptionContextKeys) && data1.EncryptDescription.Equals(data2.EncryptDescription) && data1.DecryptDescription.Equals(data2.DecryptDescription) && data1.ReproducedEncryptionContext.Equals(data2.ReproducedEncryptionContext)
		}
	case EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector:
		{
			data2, ok := other.Get_().(EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)
			return ok && data1.Name.Equals(data2.Name) && data1.Description.Equals(data2.Description) && data1.EncryptionContext.Equals(data2.EncryptionContext) && data1.CommitmentPolicy.Equals(data2.CommitmentPolicy) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.MaxPlaintextLength.Equals(data2.MaxPlaintextLength) && data1.RequiredEncryptionContextKeys.Equals(data2.RequiredEncryptionContextKeys) && data1.DecryptErrorDescription.Equals(data2.DecryptErrorDescription) && data1.EncryptDescription.Equals(data2.EncryptDescription) && data1.DecryptDescription.Equals(data2.DecryptDescription) && data1.ReproducedEncryptionContext.Equals(data2.ReproducedEncryptionContext)
		}
	case EncryptTestVector_NegativeEncryptKeyringVector:
		{
			data2, ok := other.Get_().(EncryptTestVector_NegativeEncryptKeyringVector)
			return ok && data1.Name.Equals(data2.Name) && data1.Description.Equals(data2.Description) && data1.EncryptionContext.Equals(data2.EncryptionContext) && data1.CommitmentPolicy.Equals(data2.CommitmentPolicy) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.MaxPlaintextLength.Equals(data2.MaxPlaintextLength) && data1.RequiredEncryptionContextKeys.Equals(data2.RequiredEncryptionContextKeys) && data1.ErrorDescription.Equals(data2.ErrorDescription) && data1.KeyDescription.Equals(data2.KeyDescription)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this EncryptTestVector) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(EncryptTestVector)
	return ok && _this.Equals(typed)
}

func Type_EncryptTestVector_() _dafny.TypeDescriptor {
	return type_EncryptTestVector_{}
}

type type_EncryptTestVector_ struct {
}

func (_this type_EncryptTestVector_) Default() interface{} {
	return Companion_EncryptTestVector_.Default()
}

func (_this type_EncryptTestVector_) String() string {
	return "TestVectors.EncryptTestVector"
}
func (_this EncryptTestVector) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = EncryptTestVector{}

// End of datatype EncryptTestVector

// Definition of datatype DecryptTestVector
type DecryptTestVector struct {
	Data_DecryptTestVector_
}

func (_this DecryptTestVector) Get_() Data_DecryptTestVector_ {
	return _this.Data_DecryptTestVector_
}

type Data_DecryptTestVector_ interface {
	isDecryptTestVector()
}

type CompanionStruct_DecryptTestVector_ struct {
}

var Companion_DecryptTestVector_ = CompanionStruct_DecryptTestVector_{}

type DecryptTestVector_PositiveDecryptKeyringTest struct {
	Name                        _dafny.Sequence
	AlgorithmSuite              m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	CommitmentPolicy            m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
	EncryptedDataKeys           _dafny.Sequence
	EncryptionContext           _dafny.Map
	KeyDescription              m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
	ExpectedResult              DecryptResult
	Description                 m_Wrappers.Option
	ReproducedEncryptionContext m_Wrappers.Option
}

func (DecryptTestVector_PositiveDecryptKeyringTest) isDecryptTestVector() {}

func (CompanionStruct_DecryptTestVector_) Create_PositiveDecryptKeyringTest_(Name _dafny.Sequence, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, CommitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy, EncryptedDataKeys _dafny.Sequence, EncryptionContext _dafny.Map, KeyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, ExpectedResult DecryptResult, Description m_Wrappers.Option, ReproducedEncryptionContext m_Wrappers.Option) DecryptTestVector {
	return DecryptTestVector{DecryptTestVector_PositiveDecryptKeyringTest{Name, AlgorithmSuite, CommitmentPolicy, EncryptedDataKeys, EncryptionContext, KeyDescription, ExpectedResult, Description, ReproducedEncryptionContext}}
}

func (_this DecryptTestVector) Is_PositiveDecryptKeyringTest() bool {
	_, ok := _this.Get_().(DecryptTestVector_PositiveDecryptKeyringTest)
	return ok
}

type DecryptTestVector_NegativeDecryptKeyringTest struct {
	Name                        _dafny.Sequence
	AlgorithmSuite              m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
	CommitmentPolicy            m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
	EncryptedDataKeys           _dafny.Sequence
	EncryptionContext           _dafny.Map
	ErrorDescription            _dafny.Sequence
	KeyDescription              m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
	ReproducedEncryptionContext m_Wrappers.Option
	Description                 m_Wrappers.Option
}

func (DecryptTestVector_NegativeDecryptKeyringTest) isDecryptTestVector() {}

func (CompanionStruct_DecryptTestVector_) Create_NegativeDecryptKeyringTest_(Name _dafny.Sequence, AlgorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo, CommitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy, EncryptedDataKeys _dafny.Sequence, EncryptionContext _dafny.Map, ErrorDescription _dafny.Sequence, KeyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription, ReproducedEncryptionContext m_Wrappers.Option, Description m_Wrappers.Option) DecryptTestVector {
	return DecryptTestVector{DecryptTestVector_NegativeDecryptKeyringTest{Name, AlgorithmSuite, CommitmentPolicy, EncryptedDataKeys, EncryptionContext, ErrorDescription, KeyDescription, ReproducedEncryptionContext, Description}}
}

func (_this DecryptTestVector) Is_NegativeDecryptKeyringTest() bool {
	_, ok := _this.Get_().(DecryptTestVector_NegativeDecryptKeyringTest)
	return ok
}

func (CompanionStruct_DecryptTestVector_) Default() DecryptTestVector {
	return Companion_DecryptTestVector_.Create_PositiveDecryptKeyringTest_(_dafny.EmptySeq.SetString(), m_AwsCryptographyMaterialProvidersTypes.Companion_AlgorithmSuiteInfo_.Default(), m_AwsCryptographyMaterialProvidersTypes.Companion_CommitmentPolicy_.Default(), _dafny.EmptySeq, _dafny.EmptyMap, m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Default(), Companion_DecryptResult_.Default(), m_Wrappers.Companion_Option_.Default(), m_Wrappers.Companion_Option_.Default())
}

func (_this DecryptTestVector) Dtor_name() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.Name
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).Name
	}
}

func (_this DecryptTestVector) Dtor_algorithmSuite() m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.AlgorithmSuite
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).AlgorithmSuite
	}
}

func (_this DecryptTestVector) Dtor_commitmentPolicy() m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.CommitmentPolicy
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).CommitmentPolicy
	}
}

func (_this DecryptTestVector) Dtor_encryptedDataKeys() _dafny.Sequence {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.EncryptedDataKeys
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).EncryptedDataKeys
	}
}

func (_this DecryptTestVector) Dtor_encryptionContext() _dafny.Map {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.EncryptionContext
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).EncryptionContext
	}
}

func (_this DecryptTestVector) Dtor_keyDescription() m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.KeyDescription
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).KeyDescription
	}
}

func (_this DecryptTestVector) Dtor_expectedResult() DecryptResult {
	return _this.Get_().(DecryptTestVector_PositiveDecryptKeyringTest).ExpectedResult
}

func (_this DecryptTestVector) Dtor_description() m_Wrappers.Option {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.Description
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).Description
	}
}

func (_this DecryptTestVector) Dtor_reproducedEncryptionContext() m_Wrappers.Option {
	switch data := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		return data.ReproducedEncryptionContext
	default:
		return data.(DecryptTestVector_NegativeDecryptKeyringTest).ReproducedEncryptionContext
	}
}

func (_this DecryptTestVector) Dtor_errorDescription() _dafny.Sequence {
	return _this.Get_().(DecryptTestVector_NegativeDecryptKeyringTest).ErrorDescription
}

func (_this DecryptTestVector) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case DecryptTestVector_PositiveDecryptKeyringTest:
		{
			return "TestVectors.DecryptTestVector.PositiveDecryptKeyringTest" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.CommitmentPolicy) + ", " + _dafny.String(data.EncryptedDataKeys) + ", " + _dafny.String(data.EncryptionContext) + ", " + _dafny.String(data.KeyDescription) + ", " + _dafny.String(data.ExpectedResult) + ", " + _dafny.String(data.Description) + ", " + _dafny.String(data.ReproducedEncryptionContext) + ")"
		}
	case DecryptTestVector_NegativeDecryptKeyringTest:
		{
			return "TestVectors.DecryptTestVector.NegativeDecryptKeyringTest" + "(" + _dafny.String(data.Name) + ", " + _dafny.String(data.AlgorithmSuite) + ", " + _dafny.String(data.CommitmentPolicy) + ", " + _dafny.String(data.EncryptedDataKeys) + ", " + _dafny.String(data.EncryptionContext) + ", " + _dafny.String(data.ErrorDescription) + ", " + _dafny.String(data.KeyDescription) + ", " + _dafny.String(data.ReproducedEncryptionContext) + ", " + _dafny.String(data.Description) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this DecryptTestVector) Equals(other DecryptTestVector) bool {
	switch data1 := _this.Get_().(type) {
	case DecryptTestVector_PositiveDecryptKeyringTest:
		{
			data2, ok := other.Get_().(DecryptTestVector_PositiveDecryptKeyringTest)
			return ok && data1.Name.Equals(data2.Name) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.CommitmentPolicy.Equals(data2.CommitmentPolicy) && data1.EncryptedDataKeys.Equals(data2.EncryptedDataKeys) && data1.EncryptionContext.Equals(data2.EncryptionContext) && data1.KeyDescription.Equals(data2.KeyDescription) && data1.ExpectedResult.Equals(data2.ExpectedResult) && data1.Description.Equals(data2.Description) && data1.ReproducedEncryptionContext.Equals(data2.ReproducedEncryptionContext)
		}
	case DecryptTestVector_NegativeDecryptKeyringTest:
		{
			data2, ok := other.Get_().(DecryptTestVector_NegativeDecryptKeyringTest)
			return ok && data1.Name.Equals(data2.Name) && data1.AlgorithmSuite.Equals(data2.AlgorithmSuite) && data1.CommitmentPolicy.Equals(data2.CommitmentPolicy) && data1.EncryptedDataKeys.Equals(data2.EncryptedDataKeys) && data1.EncryptionContext.Equals(data2.EncryptionContext) && data1.ErrorDescription.Equals(data2.ErrorDescription) && data1.KeyDescription.Equals(data2.KeyDescription) && data1.ReproducedEncryptionContext.Equals(data2.ReproducedEncryptionContext) && data1.Description.Equals(data2.Description)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this DecryptTestVector) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(DecryptTestVector)
	return ok && _this.Equals(typed)
}

func Type_DecryptTestVector_() _dafny.TypeDescriptor {
	return type_DecryptTestVector_{}
}

type type_DecryptTestVector_ struct {
}

func (_this type_DecryptTestVector_) Default() interface{} {
	return Companion_DecryptTestVector_.Default()
}

func (_this type_DecryptTestVector_) String() string {
	return "TestVectors.DecryptTestVector"
}
func (_this DecryptTestVector) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = DecryptTestVector{}

// End of datatype DecryptTestVector

// Definition of datatype DecryptResult
type DecryptResult struct {
	Data_DecryptResult_
}

func (_this DecryptResult) Get_() Data_DecryptResult_ {
	return _this.Data_DecryptResult_
}

type Data_DecryptResult_ interface {
	isDecryptResult()
}

type CompanionStruct_DecryptResult_ struct {
}

var Companion_DecryptResult_ = CompanionStruct_DecryptResult_{}

type DecryptResult_DecryptResult struct {
	PlaintextDataKey              m_Wrappers.Option
	SymmetricSigningKey           m_Wrappers.Option
	RequiredEncryptionContextKeys _dafny.Sequence
}

func (DecryptResult_DecryptResult) isDecryptResult() {}

func (CompanionStruct_DecryptResult_) Create_DecryptResult_(PlaintextDataKey m_Wrappers.Option, SymmetricSigningKey m_Wrappers.Option, RequiredEncryptionContextKeys _dafny.Sequence) DecryptResult {
	return DecryptResult{DecryptResult_DecryptResult{PlaintextDataKey, SymmetricSigningKey, RequiredEncryptionContextKeys}}
}

func (_this DecryptResult) Is_DecryptResult() bool {
	_, ok := _this.Get_().(DecryptResult_DecryptResult)
	return ok
}

func (CompanionStruct_DecryptResult_) Default() DecryptResult {
	return Companion_DecryptResult_.Create_DecryptResult_(m_Wrappers.Companion_Option_.Default(), m_Wrappers.Companion_Option_.Default(), _dafny.EmptySeq)
}

func (_this DecryptResult) Dtor_plaintextDataKey() m_Wrappers.Option {
	return _this.Get_().(DecryptResult_DecryptResult).PlaintextDataKey
}

func (_this DecryptResult) Dtor_symmetricSigningKey() m_Wrappers.Option {
	return _this.Get_().(DecryptResult_DecryptResult).SymmetricSigningKey
}

func (_this DecryptResult) Dtor_requiredEncryptionContextKeys() _dafny.Sequence {
	return _this.Get_().(DecryptResult_DecryptResult).RequiredEncryptionContextKeys
}

func (_this DecryptResult) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case DecryptResult_DecryptResult:
		{
			return "TestVectors.DecryptResult.DecryptResult" + "(" + _dafny.String(data.PlaintextDataKey) + ", " + _dafny.String(data.SymmetricSigningKey) + ", " + _dafny.String(data.RequiredEncryptionContextKeys) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this DecryptResult) Equals(other DecryptResult) bool {
	switch data1 := _this.Get_().(type) {
	case DecryptResult_DecryptResult:
		{
			data2, ok := other.Get_().(DecryptResult_DecryptResult)
			return ok && data1.PlaintextDataKey.Equals(data2.PlaintextDataKey) && data1.SymmetricSigningKey.Equals(data2.SymmetricSigningKey) && data1.RequiredEncryptionContextKeys.Equals(data2.RequiredEncryptionContextKeys)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this DecryptResult) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(DecryptResult)
	return ok && _this.Equals(typed)
}

func Type_DecryptResult_() _dafny.TypeDescriptor {
	return type_DecryptResult_{}
}

type type_DecryptResult_ struct {
}

func (_this type_DecryptResult_) Default() interface{} {
	return Companion_DecryptResult_.Default()
}

func (_this type_DecryptResult_) String() string {
	return "TestVectors.DecryptResult"
}
func (_this DecryptResult) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = DecryptResult{}

// End of datatype DecryptResult
