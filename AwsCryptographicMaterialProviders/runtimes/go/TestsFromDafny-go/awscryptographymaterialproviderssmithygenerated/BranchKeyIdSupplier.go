// Code generated by smithy-go-codegen DO NOT EDIT.

package awscryptographymaterialproviderssmithygenerated

import (
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
)

type BranchKeyIdSupplier struct {
	Impl AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
}

func (this *BranchKeyIdSupplier) GetBranchKeyId(params awscryptographymaterialproviderssmithygeneratedtypes.GetBranchKeyIdInput) (*awscryptographymaterialproviderssmithygeneratedtypes.GetBranchKeyIdOutput, error) {
	var dafny_request AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput = GetBranchKeyIdInput_ToDafny(params)
	var dafny_response = this.Impl.GetBranchKeyId(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return nil, Error_FromDafny(err)
	}
	var native_response = GetBranchKeyIdOutput_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput))
	return &native_response, nil

}