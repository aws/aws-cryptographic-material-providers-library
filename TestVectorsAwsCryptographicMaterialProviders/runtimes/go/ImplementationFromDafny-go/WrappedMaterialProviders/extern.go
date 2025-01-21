package WrappedMaterialProviders

import (
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyMaterialProvidersTypes"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/WrappedAwsCryptographyMaterialProvidersService"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Wrappers"
)

func (_static CompanionStruct_Default___) WrappedMaterialProviders(config AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig) Wrappers.Result {
	return WrappedAwsCryptographyMaterialProvidersService.WrappedMaterialProviders(config)
}
