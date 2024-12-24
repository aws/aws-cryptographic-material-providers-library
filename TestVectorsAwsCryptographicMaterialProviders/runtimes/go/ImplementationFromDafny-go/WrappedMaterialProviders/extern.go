package WrappedMaterialProviders

import (
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/WrappedAwsCryptographyMaterialProvidersService"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

func (_static CompanionStruct_Default___) WrappedMaterialProviders(config AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig) Wrappers.Result {
	return WrappedAwsCryptographyMaterialProvidersService.WrappedMaterialProviders(config)
}
