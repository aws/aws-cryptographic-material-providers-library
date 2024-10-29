// Package MrkAwareStrictMultiKeyring
// Dafny module MrkAwareStrictMultiKeyring compiled into Go

package MrkAwareStrictMultiKeyring

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
	m_MaterialWrapping "github.com/aws/aws-cryptographic-material-providers-library/mpl/MaterialWrapping"
	m_Materials "github.com/aws/aws-cryptographic-material-providers-library/mpl/Materials"
	m_MrkAwareDiscoveryMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MrkAwareDiscoveryMultiKeyring"
	m_MultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/MultiKeyring"
	m_StrictMultiKeyring "github.com/aws/aws-cryptographic-material-providers-library/mpl/StrictMultiKeyring"
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
	return "MrkAwareStrictMultiKeyring.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) MrkAwareStrictMultiKeyring(generator m_Wrappers.Option, awsKmsKeys m_Wrappers.Option, clientSupplier m_AwsCryptographyMaterialProvidersTypes.IClientSupplier, grantTokens m_Wrappers.Option) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Result{}
	_ = output
	var _0_allStrings _dafny.Sequence
	_ = _0_allStrings
	var _source0 m_Wrappers.Option = generator
	_ = _source0
	{
		{
			if _source0.Is_Some() {
				var _1_g _dafny.Sequence = _source0.Get_().(m_Wrappers.Option_Some).Value.(_dafny.Sequence)
				_ = _1_g
				_0_allStrings = _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_1_g), (awsKmsKeys).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence))
				goto Lmatch0
			}
		}
		{
			_0_allStrings = (awsKmsKeys).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence)
		}
		goto Lmatch0
	}
Lmatch0:
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError0
	_2_valueOrError0 = (m_Seq.Companion_Default___.MapWithResult(func(coer71 func(_dafny.Sequence) m_Wrappers.Result) func(interface{}) m_Wrappers.Result {
		return func(arg72 interface{}) m_Wrappers.Result {
			return coer71(arg72.(_dafny.Sequence))
		}
	}(m_AwsArnParsing.Companion_Default___.IsAwsKmsIdentifierString), _0_allStrings)).MapFailure(func(coer72 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error) func(interface{}) interface{} {
		return func(arg73 interface{}) interface{} {
			return coer72(arg73.(_dafny.Sequence))
		}
	}(m_AwsKmsUtils.Companion_Default___.WrapStringToError))
	if (_2_valueOrError0).IsFailure() {
		output = (_2_valueOrError0).PropagateFailure()
		return output
	}
	var _3_allIdentifiers _dafny.Sequence
	_ = _3_allIdentifiers
	_3_allIdentifiers = (_2_valueOrError0).Extract().(_dafny.Sequence)
	var _4_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _4_valueOrError1
	_4_valueOrError1 = m_AwsKmsMrkAreUnique.Companion_Default___.AwsKmsMrkAreUnique(_3_allIdentifiers)
	if (_4_valueOrError1).IsFailure() {
		output = (_4_valueOrError1).PropagateFailure()
		return output
	}
	var _5_generatorKeyring m_Wrappers.Option = m_Wrappers.Companion_Option_.Default()
	_ = _5_generatorKeyring
	var _source1 m_Wrappers.Option = generator
	_ = _source1
	{
		{
			if _source1.Is_Some() {
				var _6_generatorIdentifier _dafny.Sequence = _source1.Get_().(m_Wrappers.Option_Some).Value.(_dafny.Sequence)
				_ = _6_generatorIdentifier
				var _7_valueOrError2 m_Wrappers.Result = m_Wrappers.Result{}
				_ = _7_valueOrError2
				_7_valueOrError2 = (m_AwsArnParsing.Companion_Default___.IsAwsKmsIdentifierString(_6_generatorIdentifier)).MapFailure(func(coer73 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error) func(interface{}) interface{} {
					return func(arg74 interface{}) interface{} {
						return coer73(arg74.(_dafny.Sequence))
					}
				}(m_AwsKmsUtils.Companion_Default___.WrapStringToError))
				if (_7_valueOrError2).IsFailure() {
					output = (_7_valueOrError2).PropagateFailure()
					return output
				}
				var _8_arn m_AwsArnParsing.AwsKmsIdentifier
				_ = _8_arn
				_8_arn = (_7_valueOrError2).Extract().(m_AwsArnParsing.AwsKmsIdentifier)
				var _9_region m_Wrappers.Option
				_ = _9_region
				_9_region = m_AwsArnParsing.Companion_Default___.GetRegion(_8_arn)
				var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Result{}
				_ = _10_valueOrError3
				var _out0 m_Wrappers.Result
				_ = _out0
				_out0 = (clientSupplier).GetClient(m_AwsCryptographyMaterialProvidersTypes.Companion_GetClientInput_.Create_GetClientInput_((_9_region).UnwrapOr(_dafny.SeqOfString("")).(_dafny.Sequence)))
				_10_valueOrError3 = _out0
				if (_10_valueOrError3).IsFailure() {
					output = (_10_valueOrError3).PropagateFailure()
					return output
				}
				var _11_client m_ComAmazonawsKmsTypes.IKMSClient
				_ = _11_client
				_11_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_10_valueOrError3).Extract())
				var _12_g *m_AwsKmsMrkKeyring.AwsKmsMrkKeyring
				_ = _12_g
				var _nw0 *m_AwsKmsMrkKeyring.AwsKmsMrkKeyring = m_AwsKmsMrkKeyring.New_AwsKmsMrkKeyring_()
				_ = _nw0
				_nw0.Ctor__(_11_client, _6_generatorIdentifier, (grantTokens).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence))
				_12_g = _nw0
				_5_generatorKeyring = m_Wrappers.Companion_Option_.Create_Some_(_12_g)
				goto Lmatch1
			}
		}
		{
			_5_generatorKeyring = m_Wrappers.Companion_Option_.Create_None_()
		}
		goto Lmatch1
	}
Lmatch1:
	var _13_children _dafny.Sequence
	_ = _13_children
	_13_children = _dafny.SeqOf()
	var _source2 m_Wrappers.Option = awsKmsKeys
	_ = _source2
	{
		{
			if _source2.Is_Some() {
				var _14_childIdentifiers _dafny.Sequence = _source2.Get_().(m_Wrappers.Option_Some).Value.(_dafny.Sequence)
				_ = _14_childIdentifiers
				var _hi0 _dafny.Int = _dafny.IntOfUint32((_14_childIdentifiers).Cardinality())
				_ = _hi0
				for _15_index := _dafny.Zero; _15_index.Cmp(_hi0) < 0; _15_index = _15_index.Plus(_dafny.One) {
					var _16_childIdentifier _dafny.Sequence
					_ = _16_childIdentifier
					_16_childIdentifier = (_14_childIdentifiers).Select((_15_index).Uint32()).(_dafny.Sequence)
					var _17_valueOrError4 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _17_valueOrError4
					_17_valueOrError4 = (m_AwsArnParsing.Companion_Default___.IsAwsKmsIdentifierString(_16_childIdentifier)).MapFailure(func(coer74 func(_dafny.Sequence) m_AwsCryptographyMaterialProvidersTypes.Error) func(interface{}) interface{} {
						return func(arg75 interface{}) interface{} {
							return coer74(arg75.(_dafny.Sequence))
						}
					}(m_AwsKmsUtils.Companion_Default___.WrapStringToError))
					if (_17_valueOrError4).IsFailure() {
						output = (_17_valueOrError4).PropagateFailure()
						return output
					}
					var _18_info m_AwsArnParsing.AwsKmsIdentifier
					_ = _18_info
					_18_info = (_17_valueOrError4).Extract().(m_AwsArnParsing.AwsKmsIdentifier)
					var _19_region m_Wrappers.Option
					_ = _19_region
					_19_region = m_AwsArnParsing.Companion_Default___.GetRegion(_18_info)
					var _20_valueOrError5 m_Wrappers.Result = m_Wrappers.Result{}
					_ = _20_valueOrError5
					var _out1 m_Wrappers.Result
					_ = _out1
					_out1 = (clientSupplier).GetClient(m_AwsCryptographyMaterialProvidersTypes.Companion_GetClientInput_.Create_GetClientInput_((_19_region).UnwrapOr(_dafny.SeqOfString("")).(_dafny.Sequence)))
					_20_valueOrError5 = _out1
					if (_20_valueOrError5).IsFailure() {
						output = (_20_valueOrError5).PropagateFailure()
						return output
					}
					var _21_client m_ComAmazonawsKmsTypes.IKMSClient
					_ = _21_client
					_21_client = m_ComAmazonawsKmsTypes.Companion_IKMSClient_.CastTo_((_20_valueOrError5).Extract())
					var _22_keyring *m_AwsKmsMrkKeyring.AwsKmsMrkKeyring
					_ = _22_keyring
					var _nw1 *m_AwsKmsMrkKeyring.AwsKmsMrkKeyring = m_AwsKmsMrkKeyring.New_AwsKmsMrkKeyring_()
					_ = _nw1
					_nw1.Ctor__(_21_client, _16_childIdentifier, (grantTokens).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence))
					_22_keyring = _nw1
					_13_children = _dafny.Companion_Sequence_.Concatenate(_13_children, _dafny.SeqOf(_22_keyring))
				}
				goto Lmatch2
			}
		}
		{
			_13_children = _dafny.SeqOf()
		}
		goto Lmatch2
	}
Lmatch2:
	var _23_valueOrError6 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _23_valueOrError6
	_23_valueOrError6 = m_Wrappers.Companion_Default___.Need(((_5_generatorKeyring).Is_Some()) || ((_dafny.IntOfUint32((_13_children).Cardinality())).Sign() == 1), m_AwsCryptographyMaterialProvidersTypes.Companion_Error_.Create_AwsCryptographicMaterialProvidersException_(_dafny.SeqOfString("generatorKeyring or child Keyrings needed to create a multi keyring")))
	if (_23_valueOrError6).IsFailure() {
		output = (_23_valueOrError6).PropagateFailure()
		return output
	}
	var _24_keyring *m_MultiKeyring.MultiKeyring
	_ = _24_keyring
	var _nw2 *m_MultiKeyring.MultiKeyring = m_MultiKeyring.New_MultiKeyring_()
	_ = _nw2
	_nw2.Ctor__(_5_generatorKeyring, _13_children)
	_24_keyring = _nw2
	output = m_Wrappers.Companion_Result_.Create_Success_(_24_keyring)
	return output
	return output
}

// End of class Default__
