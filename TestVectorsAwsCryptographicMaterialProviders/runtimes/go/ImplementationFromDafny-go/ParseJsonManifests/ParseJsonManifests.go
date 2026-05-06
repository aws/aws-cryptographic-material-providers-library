// Package ParseJsonManifests
// Dafny module ParseJsonManifests compiled into Go

package ParseJsonManifests

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb/ComAmazonawsDynamodbTypes"
	m_Com_Amazonaws_Dynamodb "github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb/Com_Amazonaws_Dynamodb"
	m_ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms/ComAmazonawsKmsTypes"
	m_Com_Amazonaws_Kms "github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms/Com_Amazonaws_Kms"
	m_AlgorithmSuites "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AlgorithmSuites"
	m_AwsArnParsing "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsArnParsing"
	m_AwsCryptographyKeyStoreOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyKeyStoreOperations"
	m_AwsCryptographyKeyStoreTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyKeyStoreTypes"
	m_AwsCryptographyMaterialProvidersOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyMaterialProvidersOperations"
	m_AwsCryptographyMaterialProvidersTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyMaterialProvidersTypes"
	m_AwsKmsDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsDiscoveryKeyring"
	m_AwsKmsEcdhKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsEcdhKeyring"
	m_AwsKmsHierarchicalKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsHierarchicalKeyring"
	m_AwsKmsKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsKeyring"
	m_AwsKmsMrkAreUnique "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkAreUnique"
	m_AwsKmsMrkDiscoveryKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkDiscoveryKeyring"
	m_AwsKmsMrkKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkKeyring"
	m_AwsKmsMrkMatchForDecrypt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsMrkMatchForDecrypt"
	m_AwsKmsRsaKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsRsaKeyring"
	m_AwsKmsUtils "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsKmsUtils"
	m_CMM "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CMM"
	m_CacheConstants "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CacheConstants"
	m_CanonicalEncryptionContext "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CanonicalEncryptionContext"
	m_Commitment "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Commitment"
	m_Constants "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Constants"
	m_CreateKeyStoreTable "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CreateKeyStoreTable"
	m_CreateKeys "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/CreateKeys"
	m_DDBKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DDBKeystoreOperations"
	m_DefaultCMM "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DefaultCMM"
	m_DefaultClientSupplier "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DefaultClientSupplier"
	m_Defaults "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Defaults"
	m_DiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/DiscoveryMultiKeyring"
	m_EcdhEdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/EcdhEdkWrapping"
	m_EdkWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/EdkWrapping"
	m_ErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/ErrorMessages"
	m_GetKeys "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/GetKeys"
	m_IntermediateKeyWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/IntermediateKeyWrapping"
	m_KMSKeystoreOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KMSKeystoreOperations"
	m_KeyStore "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KeyStore"
	m_KeyStoreErrorMessages "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KeyStoreErrorMessages"
	m_Keyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Keyring"
	m_KmsArn "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/KmsArn"
	m_LocalCMC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/LocalCMC"
	m_MaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MaterialProviders"
	m_MaterialWrapping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MaterialWrapping"
	m_Materials "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Materials"
	m_MrkAwareDiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MrkAwareDiscoveryMultiKeyring"
	m_MrkAwareStrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MrkAwareStrictMultiKeyring"
	m_MultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MultiKeyring"
	m_RawAESKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RawAESKeyring"
	m_RawECDHKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RawECDHKeyring"
	m_RawRSAKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RawRSAKeyring"
	m_RequiredEncryptionContextCMM "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/RequiredEncryptionContextCMM"
	m_StormTracker "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/StormTracker"
	m_StormTrackingCMC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/StormTrackingCMC"
	m_StrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/StrictMultiKeyring"
	m_Structure "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Structure"
	m_SynchronizedLocalCMC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/SynchronizedLocalCMC"
	m_Utils "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/Utils"
	m_AtomicPrimitives "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/AtomicPrimitives"
	m_AwsCryptographyPrimitivesOperations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/AwsCryptographyPrimitivesOperations"
	m_AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/AwsCryptographyPrimitivesTypes"
	m_Digest "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/Digest"
	m_HKDF "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/HKDF"
	m_KdfCtr "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/KdfCtr"
	m_Random "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/Random"
	m_WrappedHKDF "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/WrappedHKDF"
	m_WrappedHMAC "github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/WrappedHMAC"
	m_Actions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Actions"
	m_Base64 "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Base64"
	m_Base64Lemmas "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Base64Lemmas"
	m_BoundedInts "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/BoundedInts"
	m_DivInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternals"
	m_DivInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternalsNonlinear"
	m_DivMod "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivMod"
	m_FileIO "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FileIO"
	m_FloatCompare "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FloatCompare"
	m_Functions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Functions"
	m_GeneralInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GeneralInternals"
	m_GetOpt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GetOpt"
	m_HexStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/HexStrings"
	m_JSON_API "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_API"
	m_JSON_ConcreteSyntax_Spec "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ConcreteSyntax_Spec"
	m_JSON_ConcreteSyntax_SpecProperties "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ConcreteSyntax_SpecProperties"
	m_JSON_Deserializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Deserializer"
	m_JSON_Deserializer_ByteStrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Deserializer_ByteStrConversion"
	m_JSON_Deserializer_Uint16StrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Deserializer_Uint16StrConversion"
	m_JSON_Errors "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Errors"
	m_JSON_Grammar "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Grammar"
	m_JSON_Serializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Serializer"
	m_JSON_Serializer_ByteStrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Serializer_ByteStrConversion"
	m_JSON_Spec "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Spec"
	m_JSON_Utils_Cursors "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Cursors"
	m_JSON_Utils_Lexers_Core "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Lexers_Core"
	m_JSON_Utils_Lexers_Strings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Lexers_Strings"
	m_JSON_Utils_Parsers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Parsers"
	m_JSON_Utils_Seq "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Seq"
	m_JSON_Utils_Str "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Str"
	m_JSON_Utils_Str_CharStrConversion "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Str_CharStrConversion"
	m_JSON_Utils_Str_CharStrEscaping "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Str_CharStrEscaping"
	m_JSON_Utils_Vectors "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Vectors"
	m_JSON_Utils_Views_Core "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Views_Core"
	m_JSON_Utils_Views_Writers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Utils_Views_Writers"
	m_JSON_Values "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_Values"
	m_JSON_ZeroCopy_API "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_API"
	m_JSON_ZeroCopy_Deserializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer"
	m_JSON_ZeroCopy_Deserializer_API "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_API"
	m_JSON_ZeroCopy_Deserializer_ArrayParams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_ArrayParams"
	m_JSON_ZeroCopy_Deserializer_Arrays "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Arrays"
	m_JSON_ZeroCopy_Deserializer_Constants "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Constants"
	m_JSON_ZeroCopy_Deserializer_Core "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Core"
	m_JSON_ZeroCopy_Deserializer_Numbers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Numbers"
	m_JSON_ZeroCopy_Deserializer_ObjectParams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_ObjectParams"
	m_JSON_ZeroCopy_Deserializer_Objects "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Objects"
	m_JSON_ZeroCopy_Deserializer_Strings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Strings"
	m_JSON_ZeroCopy_Deserializer_Values "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Deserializer_Values"
	m_JSON_ZeroCopy_Serializer "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/JSON_ZeroCopy_Serializer"
	m_Logarithm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Logarithm"
	m__Math "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Math_"
	m_ModInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternals"
	m_ModInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternalsNonlinear"
	m_Mul "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Mul"
	m_MulInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternals"
	m_MulInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternalsNonlinear"
	m_Power "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Power"
	m_Relations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Relations"
	m_Seq "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq"
	m_Seq_MergeSort "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq_MergeSort"
	m_Sorting "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Sorting"
	m_StandardLibrary "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary"
	m_StandardLibraryInterop "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibraryInterop"
	m_StandardLibrary_MemoryMath "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_MemoryMath"
	m_StandardLibrary_Sequence "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_Sequence"
	m_StandardLibrary_String "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_UInt"
	m_Streams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Streams"
	m_UTF8 "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/UTF8"
	m_UnicodeStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/UnicodeStrings"
	m__Unicode "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Unicode_"
	m_Utf16EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf8EncodingForm"
	m_Wrappers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Wrappers"
	m_AllAlgorithmSuites "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllAlgorithmSuites"
	m_AllDefaultCmm "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllDefaultCmm"
	m_AllHierarchy "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllHierarchy"
	m_AllKms "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKms"
	m_AllKmsEcdh "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsEcdh"
	m_AllKmsMrkAware "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsMrkAware"
	m_AllKmsMrkAwareDiscovery "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsMrkAwareDiscovery"
	m_AllKmsRsa "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsRsa"
	m_AllMulti "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllMulti"
	m_AllRawAES "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawAES"
	m_AllRawECDH "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawECDH"
	m_AllRawRSA "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRawRSA"
	m_AllRequiredEncryptionContextCmm "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllRequiredEncryptionContextCmm"
	m_AwsCryptographyMaterialProvidersTestVectorKeysTypes "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AwsCryptographyMaterialProvidersTestVectorKeysTypes"
	m_CmmFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CmmFromKeyDescription"
	m_CompleteVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CompleteVectors"
	m_CreateStaticKeyStores "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyStores"
	m_CreateStaticKeyrings "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CreateStaticKeyrings"
	m_EncryptionContextUtils "github.com/aws/aws-cryptographic-material-providers-library/testvectors/EncryptionContextUtils"
	m_JSONHelpers "github.com/aws/aws-cryptographic-material-providers-library/testvectors/JSONHelpers"
	m_KeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyDescription"
	m_KeyMaterial "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyMaterial"
	m_KeyVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyVectors"
	m_KeyringFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeyringFromKeyDescription"
	m_KeysVectorOperations "github.com/aws/aws-cryptographic-material-providers-library/testvectors/KeysVectorOperations"
	m_MplManifestOptions "github.com/aws/aws-cryptographic-material-providers-library/testvectors/MplManifestOptions"
	m_TestVectors "github.com/aws/aws-cryptographic-material-providers-library/testvectors/TestVectors"
	m_WrappedMaterialProviders "github.com/aws/aws-cryptographic-material-providers-library/testvectors/WrappedMaterialProviders"
	m_WriteJsonManifests "github.com/aws/aws-cryptographic-material-providers-library/testvectors/WriteJsonManifests"
	m__System "github.com/dafny-lang/DafnyRuntimeGo/v4/System_"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

var _ = os.Args
var _ _dafny.Dummy__
var _ m__System.Dummy__
var _ m_Wrappers.Dummy__
var _ m_BoundedInts.Dummy__
var _ m_StandardLibrary_UInt.Dummy__
var _ m_StandardLibrary_MemoryMath.Dummy__
var _ m_StandardLibrary_Sequence.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
var _ m_Random.Dummy__
var _ m_Digest.Dummy__
var _ m_WrappedHMAC.Dummy__
var _ m_HKDF.Dummy__
var _ m_WrappedHKDF.Dummy__
var _ m_KdfCtr.Dummy__
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
var _ m_Actions.Dummy__
var _ m_CanonicalEncryptionContext.Dummy__
var _ m_MaterialWrapping.Dummy__
var _ m_IntermediateKeyWrapping.Dummy__
var _ m_EdkWrapping.Dummy__
var _ m_ErrorMessages.Dummy__
var _ m_RawAESKeyring.Dummy__
var _ m_AwsArnParsing.Dummy__
var _ m_Constants.Dummy__
var _ m_EcdhEdkWrapping.Dummy__
var _ m_RawECDHKeyring.Dummy__
var _ m_RawRSAKeyring.Dummy__
var _ m_AwsKmsMrkMatchForDecrypt.Dummy__
var _ m_AwsKmsUtils.Dummy__
var _ m_AwsKmsKeyring.Dummy__
var _ m_AwsKmsDiscoveryKeyring.Dummy__
var _ m_AwsKmsEcdhKeyring.Dummy__
var _ m_FileIO.Dummy__
var _ m_LocalCMC.Dummy__
var _ m_SynchronizedLocalCMC.Dummy__
var _ m_StormTracker.Dummy__
var _ m_StormTrackingCMC.Dummy__
var _ m_CacheConstants.Dummy__
var _ m_AwsKmsHierarchicalKeyring.Dummy__
var _ m_AwsKmsMrkDiscoveryKeyring.Dummy__
var _ m_AwsKmsMrkKeyring.Dummy__
var _ m_AwsKmsRsaKeyring.Dummy__
var _ m_MultiKeyring.Dummy__
var _ m_AwsKmsMrkAreUnique.Dummy__
var _ m_StrictMultiKeyring.Dummy__
var _ m_Com_Amazonaws_Kms.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__
var _ m_DiscoveryMultiKeyring.Dummy__
var _ m_MrkAwareDiscoveryMultiKeyring.Dummy__
var _ m_MrkAwareStrictMultiKeyring.Dummy__
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
var _ m_TestVectors.Dummy__
var _ m_AllHierarchy.Dummy__
var _ m_EncryptionContextUtils.Dummy__
var _ m_AllKms.Dummy__
var _ m_AllKmsMrkAware.Dummy__
var _ m_AllKmsMrkAwareDiscovery.Dummy__
var _ m_AllKmsRsa.Dummy__
var _ m_AllKmsEcdh.Dummy__
var _ m_AllRawAES.Dummy__
var _ m_AllRawRSA.Dummy__
var _ m_AllRawECDH.Dummy__
var _ m_AllDefaultCmm.Dummy__
var _ m_AllRequiredEncryptionContextCmm.Dummy__
var _ m_AllMulti.Dummy__
var _ m_WriteJsonManifests.Dummy__
var _ m_CompleteVectors.Dummy__

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
	return "ParseJsonManifests.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) BuildEncryptTestVector(keys *m_KeyVectors.KeyVectorsClient, obj _dafny.Sequence) m_Wrappers.Result {
	var _hresult m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _hresult
	var _0_i _dafny.Int
	_ = _0_i
	_0_i = _dafny.IntOfUint32((obj).Cardinality())
	var _1_vectors _dafny.Sequence
	_ = _1_vectors
	_1_vectors = _dafny.SeqOf()
	for (_0_i).Sign() != 0 {
		_0_i = (_0_i).Minus(_dafny.One)
		var _2_test m_Wrappers.Result
		_ = _2_test
		_2_test = Companion_Default___.ToEncryptTestVector(keys, (*((obj).Select((_0_i).Uint32()).(_dafny.Tuple)).IndexInt(0)).(_dafny.Sequence), (*((obj).Select((_0_i).Uint32()).(_dafny.Tuple)).IndexInt(1)).(m_JSON_Values.JSON))
		if (_2_test).Is_Failure() {
			_hresult = m_Wrappers.Companion_Result_.Create_Failure_((_2_test).Dtor_error().(_dafny.Sequence))
			return _hresult
		}
		_1_vectors = _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf((_2_test).Dtor_value().(m_TestVectors.EncryptTestVector)), _1_vectors)
	}
	_hresult = m_Wrappers.Companion_Result_.Create_Success_(_1_vectors)
	return _hresult
	return _hresult
}
func (_static *CompanionStruct_Default___) ToEncryptTestVector(keys *m_KeyVectors.KeyVectorsClient, name _dafny.Sequence, obj m_JSON_Values.JSON) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((obj).Is_Object(), _dafny.SeqOfString("EncryptTestVector not an object"))
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
			var _5_description m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("description"), _1_obj)).ToOption()
			_ = _5_description
			var _6_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.SmallObjectToStringStringMap(_dafny.SeqOfString("encryptionContext"), _1_obj)
			_ = _6_valueOrError2
			if (_6_valueOrError2).IsFailure() {
				return (_6_valueOrError2).PropagateFailure()
			} else {
				var _7_encryptionContextStrings _dafny.Map = (_6_valueOrError2).Extract().(_dafny.Map)
				_ = _7_encryptionContextStrings
				var _8_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeMap(_7_encryptionContextStrings)
				_ = _8_valueOrError3
				if (_8_valueOrError3).IsFailure() {
					return (_8_valueOrError3).PropagateFailure()
				} else {
					var _9_encryptionContext _dafny.Map = (_8_valueOrError3).Extract().(_dafny.Map)
					_ = _9_encryptionContext
					var _10_valueOrError4 m_Wrappers.Result = Companion_Default___.GetAlgorithmSuiteInfo(_1_obj)
					_ = _10_valueOrError4
					if (_10_valueOrError4).IsFailure() {
						return (_10_valueOrError4).PropagateFailure()
					} else {
						var _11_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = (_10_valueOrError4).Extract().(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
						_ = _11_algorithmSuite
						var _12_valueOrError5 m_Wrappers.Result = Companion_Default___.GetRequiredEncryptionContextKeys(_1_obj)
						_ = _12_valueOrError5
						if (_12_valueOrError5).IsFailure() {
							return (_12_valueOrError5).PropagateFailure()
						} else {
							var _13_requiredEncryptionContextKeys m_Wrappers.Option = (_12_valueOrError5).Extract().(m_Wrappers.Option)
							_ = _13_requiredEncryptionContextKeys
							var _14_valueOrError6 m_Wrappers.Result = Companion_Default___.GetReproducedEncryptionContext(_1_obj)
							_ = _14_valueOrError6
							if (_14_valueOrError6).IsFailure() {
								return (_14_valueOrError6).PropagateFailure()
							} else {
								var _15_reproducedEncryptionContext m_Wrappers.Option = (_14_valueOrError6).Extract().(m_Wrappers.Option)
								_ = _15_reproducedEncryptionContext
								var _16_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy = m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_11_algorithmSuite)
								_ = _16_commitmentPolicy
								var _17_maxPlaintextLength m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.GetPositiveLong(_dafny.SeqOfString("maxPlaintextLength"), _1_obj)).ToOption()
								_ = _17_maxPlaintextLength
								var _source0 _dafny.Sequence = _4_typ
								_ = _source0
								{
									if (_source0).Equals(_dafny.SeqOfString("positive-keyring")) {
										var _18_valueOrError7 m_Wrappers.Result = Companion_Default___.GetKeyDescription(keys, _dafny.SeqOfString("encryptKeyDescription"), _1_obj)
										_ = _18_valueOrError7
										if (_18_valueOrError7).IsFailure() {
											return (_18_valueOrError7).PropagateFailure()
										} else {
											var _19_encryptKeyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_18_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
											_ = _19_encryptKeyDescription
											var _20_valueOrError8 m_Wrappers.Result = Companion_Default___.GetKeyDescription(keys, _dafny.SeqOfString("decryptKeyDescription"), _1_obj)
											_ = _20_valueOrError8
											if (_20_valueOrError8).IsFailure() {
												return (_20_valueOrError8).PropagateFailure()
											} else {
												var _21_decryptKeyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_20_valueOrError8).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
												_ = _21_decryptKeyDescription
												return m_Wrappers.Companion_Result_.Create_Success_(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(name, _5_description, _9_encryptionContext, _16_commitmentPolicy, _11_algorithmSuite, _17_maxPlaintextLength, _13_requiredEncryptionContextKeys, _19_encryptKeyDescription, _21_decryptKeyDescription, _15_reproducedEncryptionContext))
											}
										}
									}
								}
								{
									if (_source0).Equals(_dafny.SeqOfString("negative-encrypt-keyring")) {
										var _22_valueOrError9 m_Wrappers.Result = Companion_Default___.GetKeyDescription(keys, _dafny.SeqOfString("keyDescription"), _1_obj)
										_ = _22_valueOrError9
										if (_22_valueOrError9).IsFailure() {
											return (_22_valueOrError9).PropagateFailure()
										} else {
											var _23_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_22_valueOrError9).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
											_ = _23_keyDescription
											var _24_valueOrError10 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("errorDescription"), _1_obj)
											_ = _24_valueOrError10
											if (_24_valueOrError10).IsFailure() {
												return (_24_valueOrError10).PropagateFailure()
											} else {
												var _25_errorDescription _dafny.Sequence = (_24_valueOrError10).Extract().(_dafny.Sequence)
												_ = _25_errorDescription
												var _26_valueOrError11 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_15_reproducedEncryptionContext).Is_None(), _dafny.SeqOfString("reproducedEncryptionContext not supported"))
												_ = _26_valueOrError11
												if (_26_valueOrError11).IsFailure() {
													return (_26_valueOrError11).PropagateFailure()
												} else {
													return m_Wrappers.Companion_Result_.Create_Success_(m_TestVectors.Companion_EncryptTestVector_.Create_NegativeEncryptKeyringVector_(name, _5_description, _9_encryptionContext, _16_commitmentPolicy, _11_algorithmSuite, _17_maxPlaintextLength, _13_requiredEncryptionContextKeys, _25_errorDescription, _23_keyDescription))
												}
											}
										}
									}
								}
								{
									if (_source0).Equals(_dafny.SeqOfString("negative-decrypt-keyring")) {
										var _27_valueOrError12 m_Wrappers.Result = Companion_Default___.GetKeyDescription(keys, _dafny.SeqOfString("encryptKeyDescription"), _1_obj)
										_ = _27_valueOrError12
										if (_27_valueOrError12).IsFailure() {
											return (_27_valueOrError12).PropagateFailure()
										} else {
											var _28_encryptKeyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_27_valueOrError12).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
											_ = _28_encryptKeyDescription
											var _29_valueOrError13 m_Wrappers.Result = Companion_Default___.GetKeyDescription(keys, _dafny.SeqOfString("decryptKeyDescription"), _1_obj)
											_ = _29_valueOrError13
											if (_29_valueOrError13).IsFailure() {
												return (_29_valueOrError13).PropagateFailure()
											} else {
												var _30_decryptKeyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_29_valueOrError13).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
												_ = _30_decryptKeyDescription
												var _31_valueOrError14 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("decryptErrorDescription"), _1_obj)
												_ = _31_valueOrError14
												if (_31_valueOrError14).IsFailure() {
													return (_31_valueOrError14).PropagateFailure()
												} else {
													var _32_decryptErrorDescription _dafny.Sequence = (_31_valueOrError14).Extract().(_dafny.Sequence)
													_ = _32_decryptErrorDescription
													return m_Wrappers.Companion_Result_.Create_Success_(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptNegativeDecryptKeyringVector_(name, _5_description, _9_encryptionContext, _16_commitmentPolicy, _11_algorithmSuite, _17_maxPlaintextLength, _13_requiredEncryptionContextKeys, _32_decryptErrorDescription, _28_encryptKeyDescription, _30_decryptKeyDescription, _15_reproducedEncryptionContext))
												}
											}
										}
									}
								}
								{
									return m_Wrappers.Companion_Result_.Create_Failure_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported EncryptTestVector type:"), _4_typ))
								}
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) GetKeyDescription(keyVectorClient *m_KeyVectors.KeyVectorsClient, key _dafny.Sequence, obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Get(key, obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_keyDescriptionObject m_JSON_Values.JSON = (_0_valueOrError0).Extract().(m_JSON_Values.JSON)
		_ = _1_keyDescriptionObject
		var _2_valueOrError1 m_Wrappers.Result = (m_JSON_API.Companion_Default___.Serialize(_1_keyDescriptionObject)).MapFailure(func(coer129 func(m_JSON_Errors.SerializationError) _dafny.Sequence) func(interface{}) interface{} {
			return func(arg200 interface{}) interface{} {
				return coer129(arg200.(m_JSON_Errors.SerializationError))
			}
		}(func(_3_e m_JSON_Errors.SerializationError) _dafny.Sequence {
			return (_3_e).ToString()
		}))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _4_descriptionStr _dafny.Sequence = (_2_valueOrError1).Extract().(_dafny.Sequence)
			_ = _4_descriptionStr
			var _5_valueOrError2 m_Wrappers.Result = ((keyVectorClient).GetKeyDescription(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_GetKeyDescriptionInput_.Create_GetKeyDescriptionInput_(_4_descriptionStr))).MapFailure(func(coer130 func(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error) _dafny.Sequence) func(interface{}) interface{} {
				return func(arg201 interface{}) interface{} {
					return coer130(arg201.(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error))
				}
			}(Companion_Default___.ErrorToString))
			_ = _5_valueOrError2
			if (_5_valueOrError2).IsFailure() {
				return (_5_valueOrError2).PropagateFailure()
			} else {
				var _6_keyDescriptionOutput m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput = (_5_valueOrError2).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput)
				_ = _6_keyDescriptionOutput
				return m_Wrappers.Companion_Result_.Create_Success_((_6_keyDescriptionOutput).Dtor_keyDescription())
			}
		}
	}
}
func (_static *CompanionStruct_Default___) GetAlgorithmSuiteInfo(obj _dafny.Sequence) m_Wrappers.Result {
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
			return (m_AlgorithmSuites.Companion_Default___.GetAlgorithmSuiteInfo(_3_binaryId)).MapFailure(func(coer131 func(m_AwsCryptographyMaterialProvidersTypes.Error) _dafny.Sequence) func(interface{}) interface{} {
				return func(arg202 interface{}) interface{} {
					return coer131(arg202.(m_AwsCryptographyMaterialProvidersTypes.Error))
				}
			}((func(_4_algorithmSuiteHex _dafny.Sequence) func(m_AwsCryptographyMaterialProvidersTypes.Error) _dafny.Sequence {
				return func(_5_e m_AwsCryptographyMaterialProvidersTypes.Error) _dafny.Sequence {
					return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Invalid Suite:"), _4_algorithmSuiteHex)
				}
			})(_1_algorithmSuiteHex)))
		}
	}
}
func (_static *CompanionStruct_Default___) GetRequiredEncryptionContextKeys(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_keysAsStrings m_Wrappers.Option = (m_JSONHelpers.Companion_Default___.GetArrayString(_dafny.SeqOfString("requiredEncryptionContextKeys"), obj)).ToOption()
	_ = _0_keysAsStrings
	var _source0 m_Wrappers.Option = _0_keysAsStrings
	_ = _source0
	{
		if _source0.Is_Some() {
			var _1_s _dafny.Sequence = _source0.Get_().(m_Wrappers.Option_Some).Value.(_dafny.Sequence)
			_ = _1_s
			var _2_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeSeq((_0_keysAsStrings).Dtor_value().(_dafny.Sequence))
			_ = _2_valueOrError0
			if (_2_valueOrError0).IsFailure() {
				return (_2_valueOrError0).PropagateFailure()
			} else {
				var _3_k _dafny.Sequence = (_2_valueOrError0).Extract().(_dafny.Sequence)
				_ = _3_k
				return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(_3_k))
			}
		}
	}
	{
		return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
	}
}
func (_static *CompanionStruct_Default___) GetReproducedEncryptionContext(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalSmallObjectToStringStringMap(_dafny.SeqOfString("reproducedEncryptionContext"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_reproducedEncryptionContextStrings m_Wrappers.Option = (_0_valueOrError0).Extract().(m_Wrappers.Option)
		_ = _1_reproducedEncryptionContextStrings
		var _source0 m_Wrappers.Option = _1_reproducedEncryptionContextStrings
		_ = _source0
		{
			if _source0.Is_Some() {
				var _2_r _dafny.Map = _source0.Get_().(m_Wrappers.Option_Some).Value.(_dafny.Map)
				_ = _2_r
				var _3_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeMap(_2_r)
				_ = _3_valueOrError1
				if (_3_valueOrError1).IsFailure() {
					return (_3_valueOrError1).PropagateFailure()
				} else {
					var _4_e _dafny.Map = (_3_valueOrError1).Extract().(_dafny.Map)
					_ = _4_e
					return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(_4_e))
				}
			}
		}
		{
			return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
		}
	}
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
func (_static *CompanionStruct_Default___) BuildDecryptTestVector(keys *m_KeyVectors.KeyVectorsClient, obj _dafny.Sequence) m_Wrappers.Result {
	var _hresult m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _hresult
	var _0_i _dafny.Int
	_ = _0_i
	_0_i = _dafny.IntOfUint32((obj).Cardinality())
	var _1_vectors _dafny.Sequence
	_ = _1_vectors
	_1_vectors = _dafny.SeqOf()
	for (_0_i).Sign() != 0 {
		_0_i = (_0_i).Minus(_dafny.One)
		var _2_test m_Wrappers.Result
		_ = _2_test
		_2_test = Companion_Default___.ToDecryptTestVector(keys, (*((obj).Select((_0_i).Uint32()).(_dafny.Tuple)).IndexInt(0)).(_dafny.Sequence), (*((obj).Select((_0_i).Uint32()).(_dafny.Tuple)).IndexInt(1)).(m_JSON_Values.JSON))
		if (_2_test).Is_Failure() {
			_hresult = m_Wrappers.Companion_Result_.Create_Failure_((_2_test).Dtor_error().(_dafny.Sequence))
			return _hresult
		}
		_1_vectors = _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf((_2_test).Dtor_value().(m_TestVectors.DecryptTestVector)), _1_vectors)
	}
	_hresult = m_Wrappers.Companion_Result_.Create_Success_(_1_vectors)
	return _hresult
	return _hresult
}
func (_static *CompanionStruct_Default___) PrintJson(j _dafny.Sequence) _dafny.Tuple {
	var _hresult _dafny.Tuple = _dafny.TupleOf()
	_ = _hresult
	_dafny.Print(j)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_hresult = _dafny.TupleOf()
	return _hresult
	return _hresult
}
func (_static *CompanionStruct_Default___) GetEncryptedDataKeys(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetArray(_dafny.SeqOfString("encryptedDataKeys"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_encryptedDataKeysJson _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_encryptedDataKeysJson
		return m_Seq.Companion_Default___.MapWithResult(func(coer132 func(m_JSON_Values.JSON) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
			return func(arg203 interface{}) m_Wrappers.Result {
				return coer132(arg203.(m_JSON_Values.JSON))
			}
		}(Companion_Default___.GetEncryptedDataKey), _1_encryptedDataKeysJson)
	}
}
func (_static *CompanionStruct_Default___) GetEncryptedDataKey(json m_JSON_Values.JSON) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((json).Is_Object(), _dafny.SeqOfString("Encrypted data key is not an object"))
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("keyProviderId"), (json).Dtor_obj())
		_ = _1_valueOrError1
		if (_1_valueOrError1).IsFailure() {
			return (_1_valueOrError1).PropagateFailure()
		} else {
			var _2_keyProviderId _dafny.Sequence = (_1_valueOrError1).Extract().(_dafny.Sequence)
			_ = _2_keyProviderId
			var _3_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("keyProviderInfo"), (json).Dtor_obj())
			_ = _3_valueOrError2
			if (_3_valueOrError2).IsFailure() {
				return (_3_valueOrError2).PropagateFailure()
			} else {
				var _4_keyProviderInfo _dafny.Sequence = (_3_valueOrError2).Extract().(_dafny.Sequence)
				_ = _4_keyProviderInfo
				var _5_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("ciphertext"), (json).Dtor_obj())
				_ = _5_valueOrError3
				if (_5_valueOrError3).IsFailure() {
					return (_5_valueOrError3).PropagateFailure()
				} else {
					var _6_ciphertext _dafny.Sequence = (_5_valueOrError3).Extract().(_dafny.Sequence)
					_ = _6_ciphertext
					var _7_valueOrError4 m_Wrappers.Result = m_UTF8.Encode(_2_keyProviderId)
					_ = _7_valueOrError4
					if (_7_valueOrError4).IsFailure() {
						return (_7_valueOrError4).PropagateFailure()
					} else {
						var _8_keyProviderId _dafny.Sequence = (_7_valueOrError4).Extract().(_dafny.Sequence)
						_ = _8_keyProviderId
						var _9_valueOrError5 m_Wrappers.Result = m_Base64.Companion_Default___.Decode(_4_keyProviderInfo)
						_ = _9_valueOrError5
						if (_9_valueOrError5).IsFailure() {
							return (_9_valueOrError5).PropagateFailure()
						} else {
							var _10_keyProviderInfo _dafny.Sequence = (_9_valueOrError5).Extract().(_dafny.Sequence)
							_ = _10_keyProviderInfo
							var _11_valueOrError6 m_Wrappers.Result = m_Base64.Companion_Default___.Decode(_6_ciphertext)
							_ = _11_valueOrError6
							if (_11_valueOrError6).IsFailure() {
								return (_11_valueOrError6).PropagateFailure()
							} else {
								var _12_ciphertext _dafny.Sequence = (_11_valueOrError6).Extract().(_dafny.Sequence)
								_ = _12_ciphertext
								return m_Wrappers.Companion_Result_.Create_Success_(m_AwsCryptographyMaterialProvidersTypes.Companion_EncryptedDataKey_.Create_EncryptedDataKey_(_8_keyProviderId, _10_keyProviderInfo, _12_ciphertext))
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) GetExpectedResult(obj _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetObject(_dafny.SeqOfString("result"), obj)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_result _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_result
		var _2_valueOrError1 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("plaintextDataKey"), _1_result)
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_plaintextDataKey m_Wrappers.Option = (_2_valueOrError1).Extract().(m_Wrappers.Option)
			_ = _3_plaintextDataKey
			var _4_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("symmetricSigningKey"), _1_result)
			_ = _4_valueOrError2
			if (_4_valueOrError2).IsFailure() {
				return (_4_valueOrError2).PropagateFailure()
			} else {
				var _5_symmetricSigningKey m_Wrappers.Option = (_4_valueOrError2).Extract().(m_Wrappers.Option)
				_ = _5_symmetricSigningKey
				var _6_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetArrayString(_dafny.SeqOfString("requiredEncryptionContextKeys"), _1_result)
				_ = _6_valueOrError3
				if (_6_valueOrError3).IsFailure() {
					return (_6_valueOrError3).PropagateFailure()
				} else {
					var _7_requiredEncryptionContextKeys _dafny.Sequence = (_6_valueOrError3).Extract().(_dafny.Sequence)
					_ = _7_requiredEncryptionContextKeys
					var _8_valueOrError4 m_Wrappers.Result = (func() m_Wrappers.Result {
						if (_3_plaintextDataKey).Is_Some() {
							return func(_pat_let22_0 m_Wrappers.Result) m_Wrappers.Result {
								return func(_9_valueOrError5 m_Wrappers.Result) m_Wrappers.Result {
									return (func() m_Wrappers.Result {
										if (_9_valueOrError5).IsFailure() {
											return (_9_valueOrError5).PropagateFailure()
										}
										return func(_pat_let23_0 _dafny.Sequence) m_Wrappers.Result {
											return func(_10_p _dafny.Sequence) m_Wrappers.Result {
												return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(_10_p))
											}(_pat_let23_0)
										}((_9_valueOrError5).Extract().(_dafny.Sequence))
									})()
								}(_pat_let22_0)
							}(m_Base64.Companion_Default___.Decode((_3_plaintextDataKey).Dtor_value().(_dafny.Sequence)))
						}
						return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
					})()
					_ = _8_valueOrError4
					if (_8_valueOrError4).IsFailure() {
						return (_8_valueOrError4).PropagateFailure()
					} else {
						var _11_plaintextDataKey m_Wrappers.Option = (_8_valueOrError4).Extract().(m_Wrappers.Option)
						_ = _11_plaintextDataKey
						var _12_valueOrError6 m_Wrappers.Result = (func() m_Wrappers.Result {
							if (_5_symmetricSigningKey).Is_Some() {
								return func(_pat_let24_0 m_Wrappers.Result) m_Wrappers.Result {
									return func(_13_valueOrError7 m_Wrappers.Result) m_Wrappers.Result {
										return (func() m_Wrappers.Result {
											if (_13_valueOrError7).IsFailure() {
												return (_13_valueOrError7).PropagateFailure()
											}
											return func(_pat_let25_0 _dafny.Sequence) m_Wrappers.Result {
												return func(_14_p _dafny.Sequence) m_Wrappers.Result {
													return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_Some_(_14_p))
												}(_pat_let25_0)
											}((_13_valueOrError7).Extract().(_dafny.Sequence))
										})()
									}(_pat_let24_0)
								}(m_Base64.Companion_Default___.Decode((_5_symmetricSigningKey).Dtor_value().(_dafny.Sequence)))
							}
							return m_Wrappers.Companion_Result_.Create_Success_(m_Wrappers.Companion_Option_.Create_None_())
						})()
						_ = _12_valueOrError6
						if (_12_valueOrError6).IsFailure() {
							return (_12_valueOrError6).PropagateFailure()
						} else {
							var _15_symmetricSigningKey m_Wrappers.Option = (_12_valueOrError6).Extract().(m_Wrappers.Option)
							_ = _15_symmetricSigningKey
							var _16_valueOrError8 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeSeq(_7_requiredEncryptionContextKeys)
							_ = _16_valueOrError8
							if (_16_valueOrError8).IsFailure() {
								return (_16_valueOrError8).PropagateFailure()
							} else {
								var _17_requiredEncryptionContextKeys _dafny.Sequence = (_16_valueOrError8).Extract().(_dafny.Sequence)
								_ = _17_requiredEncryptionContextKeys
								return m_Wrappers.Companion_Result_.Create_Success_(m_TestVectors.Companion_DecryptResult_.Create_DecryptResult_(_11_plaintextDataKey, _15_symmetricSigningKey, _17_requiredEncryptionContextKeys))
							}
						}
					}
				}
			}
		}
	}
}
func (_static *CompanionStruct_Default___) ToDecryptTestVector(keys *m_KeyVectors.KeyVectorsClient, name _dafny.Sequence, json m_JSON_Values.JSON) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((json).Is_Object(), _dafny.SeqOfString("DecryptTestVector not an object"))
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_obj _dafny.Sequence = (json).Dtor_obj()
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
			var _5_valueOrError2 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetOptionalString(_dafny.SeqOfString("description"), _1_obj)
			_ = _5_valueOrError2
			if (_5_valueOrError2).IsFailure() {
				return (_5_valueOrError2).PropagateFailure()
			} else {
				var _6_description m_Wrappers.Option = (_5_valueOrError2).Extract().(m_Wrappers.Option)
				_ = _6_description
				var _7_valueOrError3 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.SmallObjectToStringStringMap(_dafny.SeqOfString("encryptionContext"), _1_obj)
				_ = _7_valueOrError3
				if (_7_valueOrError3).IsFailure() {
					return (_7_valueOrError3).PropagateFailure()
				} else {
					var _8_encryptionContextStrings _dafny.Map = (_7_valueOrError3).Extract().(_dafny.Map)
					_ = _8_encryptionContextStrings
					var _9_valueOrError4 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.Utf8EncodeMap(_8_encryptionContextStrings)
					_ = _9_valueOrError4
					if (_9_valueOrError4).IsFailure() {
						return (_9_valueOrError4).PropagateFailure()
					} else {
						var _10_encryptionContext _dafny.Map = (_9_valueOrError4).Extract().(_dafny.Map)
						_ = _10_encryptionContext
						var _11_valueOrError5 m_Wrappers.Result = Companion_Default___.GetAlgorithmSuiteInfo(_1_obj)
						_ = _11_valueOrError5
						if (_11_valueOrError5).IsFailure() {
							return (_11_valueOrError5).PropagateFailure()
						} else {
							var _12_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = (_11_valueOrError5).Extract().(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
							_ = _12_algorithmSuite
							var _13_valueOrError6 m_Wrappers.Result = Companion_Default___.GetReproducedEncryptionContext(_1_obj)
							_ = _13_valueOrError6
							if (_13_valueOrError6).IsFailure() {
								return (_13_valueOrError6).PropagateFailure()
							} else {
								var _14_reproducedEncryptionContext m_Wrappers.Option = (_13_valueOrError6).Extract().(m_Wrappers.Option)
								_ = _14_reproducedEncryptionContext
								var _15_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy = m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_12_algorithmSuite)
								_ = _15_commitmentPolicy
								var _16_valueOrError7 m_Wrappers.Result = Companion_Default___.GetKeyDescription(keys, _dafny.SeqOfString("keyDescription"), _1_obj)
								_ = _16_valueOrError7
								if (_16_valueOrError7).IsFailure() {
									return (_16_valueOrError7).PropagateFailure()
								} else {
									var _17_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = (_16_valueOrError7).Extract().(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
									_ = _17_keyDescription
									var _18_valueOrError8 m_Wrappers.Result = Companion_Default___.GetEncryptedDataKeys(_1_obj)
									_ = _18_valueOrError8
									if (_18_valueOrError8).IsFailure() {
										return (_18_valueOrError8).PropagateFailure()
									} else {
										var _19_encryptedDataKeys _dafny.Sequence = (_18_valueOrError8).Extract().(_dafny.Sequence)
										_ = _19_encryptedDataKeys
										var _source0 _dafny.Sequence = _4_typ
										_ = _source0
										{
											if (_source0).Equals(_dafny.SeqOfString("positive-keyring")) {
												var _20_valueOrError9 m_Wrappers.Result = Companion_Default___.GetExpectedResult(_1_obj)
												_ = _20_valueOrError9
												if (_20_valueOrError9).IsFailure() {
													return (_20_valueOrError9).PropagateFailure()
												} else {
													var _21_expectedResult m_TestVectors.DecryptResult = (_20_valueOrError9).Extract().(m_TestVectors.DecryptResult)
													_ = _21_expectedResult
													return m_Wrappers.Companion_Result_.Create_Success_(m_TestVectors.Companion_DecryptTestVector_.Create_PositiveDecryptKeyringTest_(name, _12_algorithmSuite, _15_commitmentPolicy, _19_encryptedDataKeys, _10_encryptionContext, _17_keyDescription, _21_expectedResult, _6_description, _14_reproducedEncryptionContext))
												}
											}
										}
										{
											if (_source0).Equals(_dafny.SeqOfString("negative-keyring")) {
												var _22_valueOrError10 m_Wrappers.Result = m_JSONHelpers.Companion_Default___.GetString(_dafny.SeqOfString("errorDescription"), _1_obj)
												_ = _22_valueOrError10
												if (_22_valueOrError10).IsFailure() {
													return (_22_valueOrError10).PropagateFailure()
												} else {
													var _23_errorDescription _dafny.Sequence = (_22_valueOrError10).Extract().(_dafny.Sequence)
													_ = _23_errorDescription
													return m_Wrappers.Companion_Result_.Create_Success_(m_TestVectors.Companion_DecryptTestVector_.Create_NegativeDecryptKeyringTest_(name, _12_algorithmSuite, _15_commitmentPolicy, _19_encryptedDataKeys, _10_encryptionContext, _23_errorDescription, _17_keyDescription, _14_reproducedEncryptionContext, _6_description))
												}
											}
										}
										{
											return m_Wrappers.Companion_Result_.Create_Failure_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Unsupported DecryptTestVector type:"), _4_typ))
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

// End of class Default__
