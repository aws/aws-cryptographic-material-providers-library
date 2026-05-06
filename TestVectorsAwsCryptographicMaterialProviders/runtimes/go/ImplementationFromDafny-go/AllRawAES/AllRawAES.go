// Package AllRawAES
// Dafny module AllRawAES compiled into Go

package AllRawAES

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
	m_AllHierarchy "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllHierarchy"
	m_AllKms "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKms"
	m_AllKmsEcdh "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsEcdh"
	m_AllKmsMrkAware "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsMrkAware"
	m_AllKmsMrkAwareDiscovery "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsMrkAwareDiscovery"
	m_AllKmsRsa "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AllKmsRsa"
	m_AwsCryptographyMaterialProvidersTestVectorKeysTypes "github.com/aws/aws-cryptographic-material-providers-library/testvectors/AwsCryptographyMaterialProvidersTestVectorKeysTypes"
	m_CmmFromKeyDescription "github.com/aws/aws-cryptographic-material-providers-library/testvectors/CmmFromKeyDescription"
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
	return "AllRawAES.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) AesPersistentKeyNames() _dafny.Sequence {
	return _dafny.SeqOf(_dafny.SeqOfString("aes-128"), _dafny.SeqOfString("aes-256"), _dafny.SeqOfChars(55349, 57281, 45, 110, 111, 110, 97, 115, 99, 105, 105, 45, 55296, 56322, 45, 97, 101, 115, 45, 50, 53, 54, 45, 55349, 57281, 45, 119, 105, 116, 104, 45, 65533))
}
func (_static *CompanionStruct_Default___) KeyDescriptionsWithPsi() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter62 := _dafny.Iterate((Companion_Default___.AesPersistentKeyNames()).Elements()); ; {
			_compr_0, _ok62 := _iter62()
			if !_ok62 {
				break
			}
			var _0_key _dafny.Sequence
			_0_key = interface{}(_compr_0).(_dafny.Sequence)
			if _dafny.Companion_Sequence_.Contains(Companion_Default___.AesPersistentKeyNames(), _0_key) {
				_coll0.Add(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_AES_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RawAES_.Create_RawAES_(_0_key, _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("aws-raw-vectors-persistent-"), _0_key), _dafny.SeqOfChars(45, 55349, 57281)))))
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) KeyDescriptions() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter63 := _dafny.Iterate((Companion_Default___.AesPersistentKeyNames()).Elements()); ; {
			_compr_0, _ok63 := _iter63()
			if !_ok63 {
				break
			}
			var _0_key _dafny.Sequence
			_0_key = interface{}(_compr_0).(_dafny.Sequence)
			if _dafny.Companion_Sequence_.Contains(Companion_Default___.AesPersistentKeyNames(), _0_key) {
				_coll0.Add(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_KeyDescription_.Create_AES_(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.Companion_RawAES_.Create_RawAES_(_0_key, _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("aws-raw-vectors-persistent-"), _0_key))))
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestsNoEc() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter64 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok64 := _iter64()
			if !_ok64 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter65 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok65 := _iter65()
					if !_ok65 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter66 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok66 := _iter66()
							if !_ok66 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES No Encryption Context "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap(), _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestsWitPsiEc() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter67 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok67 := _iter67()
			if !_ok67 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter68 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok68 := _iter68()
					if !_ok68 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter69 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok69 := _iter69()
							if !_ok69 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								for _iter70 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.EncryptionContextWitPsi()).Elements()); ; {
									_compr_3, _ok70 := _iter70()
									if !_ok70 {
										break
									}
									var _3_encryptionContext _dafny.Map
									_3_encryptionContext = interface{}(_compr_3).(_dafny.Map)
									if (m_EncryptionContextUtils.Companion_Default___.EncryptionContextWitPsi()).Contains(_3_encryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES Encryption Context With Psi "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
									}
								}
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestsWitReplacementCharEc() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter71 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok71 := _iter71()
			if !_ok71 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter72 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok72 := _iter72()
					if !_ok72 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter73 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok73 := _iter73()
							if !_ok73 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								for _iter74 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.EncryptionContextWitReplacementChar()).Elements()); ; {
									_compr_3, _ok74 := _iter74()
									if !_ok74 {
										break
									}
									var _3_encryptionContext _dafny.Map
									_3_encryptionContext = interface{}(_compr_3).(_dafny.Map)
									if (m_EncryptionContextUtils.Companion_Default___.EncryptionContextWitReplacementChar()).Contains(_3_encryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES Encryption Context With Psi "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
									}
								}
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestControlEc() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter75 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok75 := _iter75()
			if !_ok75 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter76 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok76 := _iter76()
					if !_ok76 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter77 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok77 := _iter77()
							if !_ok77 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								for _iter78 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.EncryptionContextControl()).Elements()); ; {
									_compr_3, _ok78 := _iter78()
									if !_ok78 {
										break
									}
									var _3_encryptionContext _dafny.Map
									_3_encryptionContext = interface{}(_compr_3).(_dafny.Map)
									if (m_EncryptionContextUtils.Companion_Default___.EncryptionContextControl()).Contains(_3_encryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES Control Encryption Context "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
									}
								}
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestsBasicEc() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter79 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok79 := _iter79()
			if !_ok79 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter80 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok80 := _iter80()
					if !_ok80 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter81 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok81 := _iter81()
							if !_ok81 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								for _iter82 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.EncryptionContextBasic()).Elements()); ; {
									_compr_3, _ok82 := _iter82()
									if !_ok82 {
										break
									}
									var _3_encryptionContext _dafny.Map
									_3_encryptionContext = interface{}(_compr_3).(_dafny.Map)
									if (m_EncryptionContextUtils.Companion_Default___.EncryptionContextBasic()).Contains(_3_encryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES Basic Encryption Context "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
									}
								}
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestsWithDiffUTF8Ec() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter83 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok83 := _iter83()
			if !_ok83 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter84 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok84 := _iter84()
					if !_ok84 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter85 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok85 := _iter85()
							if !_ok85 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								for _iter86 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.VariedUTF8EncryptionContext()).Elements()); ; {
									_compr_3, _ok86 := _iter86()
									if !_ok86 {
										break
									}
									var _3_encryptionContext _dafny.Map
									_3_encryptionContext = interface{}(_compr_3).(_dafny.Map)
									if (m_EncryptionContextUtils.Companion_Default___.VariedUTF8EncryptionContext()).Contains(_3_encryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES UTF8 Representative values "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
									}
								}
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestsWithOnePairOfHighCodePointUtf8ValuesInEc() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter87 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok87 := _iter87()
			if !_ok87 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter88 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok88 := _iter88()
					if !_ok88 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter89 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok89 := _iter89()
							if !_ok89 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								for _iter90 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.RepresentativeEncryptionContextUtf8Values()).Elements()); ; {
									_compr_3, _ok90 := _iter90()
									if !_ok90 {
										break
									}
									var _3_key _dafny.Sequence
									_3_key = interface{}(_compr_3).(_dafny.Sequence)
									if m_UTF8.Companion_ValidUTF8Bytes_.Is_(_3_key) {
										if (m_EncryptionContextUtils.Companion_Default___.RepresentativeEncryptionContextUtf8Values()).Contains(_3_key) {
											for _iter91 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.RepresentativeEncryptionContextUtf8Values()).Elements()); ; {
												_compr_4, _ok91 := _iter91()
												if !_ok91 {
													break
												}
												var _4_value _dafny.Sequence
												_4_value = interface{}(_compr_4).(_dafny.Sequence)
												if m_UTF8.Companion_ValidUTF8Bytes_.Is_(_4_value) {
													if (m_EncryptionContextUtils.Companion_Default___.RepresentativeEncryptionContextUtf8Values()).Contains(_4_value) {
														_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES Mix and Match UTF8 Key Values "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_3_key, _4_value), _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
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
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) TestsWithMultipleUTF8Ec() _dafny.Set {
	return func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter92 := _dafny.Iterate(((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Elements()); ; {
			_compr_0, _ok92 := _iter92()
			if !_ok92 {
				break
			}
			var _0_keyDescription m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
			_0_keyDescription = interface{}(_compr_0).(m_AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription)
			if ((Companion_Default___.KeyDescriptions()).Union(Companion_Default___.KeyDescriptionsWithPsi())).Contains(_0_keyDescription) {
				for _iter93 := _dafny.Iterate((m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Elements()); ; {
					_compr_1, _ok93 := _iter93()
					if !_ok93 {
						break
					}
					var _1_algorithmSuite m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
					_1_algorithmSuite = interface{}(_compr_1).(m_AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo)
					if (m_AllAlgorithmSuites.Companion_Default___.AllAlgorithmSuites()).Contains(_1_algorithmSuite) {
						for _iter94 := _dafny.Iterate(_dafny.SingleValue(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite))); ; {
							_compr_2, _ok94 := _iter94()
							if !_ok94 {
								break
							}
							var _2_commitmentPolicy m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
							_2_commitmentPolicy = interface{}(_compr_2).(m_AwsCryptographyMaterialProvidersTypes.CommitmentPolicy)
							if (_2_commitmentPolicy).Equals(m_AllAlgorithmSuites.Companion_Default___.GetCompatibleCommitmentPolicy(_1_algorithmSuite)) {
								for _iter95 := _dafny.Iterate((m_EncryptionContextUtils.Companion_Default___.MultipleEntriesUTF8EncryptionContext()).Elements()); ; {
									_compr_3, _ok95 := _iter95()
									if !_ok95 {
										break
									}
									var _3_encryptionContext _dafny.Map
									_3_encryptionContext = interface{}(_compr_3).(_dafny.Map)
									if (m_EncryptionContextUtils.Companion_Default___.MultipleEntriesUTF8EncryptionContext()).Contains(_3_encryptionContext) {
										_coll0.Add(m_TestVectors.Companion_EncryptTestVector_.Create_PositiveEncryptKeyringVector_(_dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("Generated RawAES Multiple UTF8 Entries EC "), ((_0_keyDescription).Dtor_AES()).Dtor_keyId()), m_Wrappers.Companion_Option_.Create_None_(), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), _0_keyDescription, _0_keyDescription, m_Wrappers.Companion_Option_.Create_None_()))
									}
								}
							}
						}
					}
				}
			}
		}
		return _coll0.ToSet()
	}()
}
func (_static *CompanionStruct_Default___) Tests() _dafny.Set {
	return ((((((_dafny.SetOf()).Union(Companion_Default___.TestsNoEc())).Union(Companion_Default___.TestsWitPsiEc())).Union(Companion_Default___.TestsBasicEc())).Union(Companion_Default___.TestControlEc())).Union(Companion_Default___.TestsWitReplacementCharEc())).Union(Companion_Default___.TestsWithMultipleUTF8Ec())
}

// End of class Default__
