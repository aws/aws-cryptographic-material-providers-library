// Code generated by smithy-go-codegen DO NOT EDIT.

package awscryptographymaterialproviderssmithygenerated

import (
	"context"

	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/AwsCryptographyMaterialProvidersTypes"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/MaterialProviders"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

type Client struct {
	DafnyClient AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
}

func NewClient(clientConfig awscryptographymaterialproviderssmithygeneratedtypes.MaterialProvidersConfig) (*Client, error) {
	var dafnyConfig = MaterialProvidersConfig_ToDafny(clientConfig)
	var dafny_response = MaterialProviders.Companion_Default___.MaterialProviders(dafnyConfig)
	if dafny_response.Is_Failure() {
		panic("Client construction failed. This should never happen")
	}
	var dafnyClient = dafny_response.Extract().(AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient)
	client := &Client{dafnyClient}
	return client, nil
}

func (client *Client) CreateAwsKmsKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput = CreateAwsKmsKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsDiscoveryKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsDiscoveryKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryKeyringInput = CreateAwsKmsDiscoveryKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsDiscoveryKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsMultiKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsMultiKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMultiKeyringInput = CreateAwsKmsMultiKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsMultiKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsDiscoveryMultiKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsDiscoveryMultiKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryMultiKeyringInput = CreateAwsKmsDiscoveryMultiKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsDiscoveryMultiKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsMrkKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsMrkKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput = CreateAwsKmsMrkKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsMrkKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsMrkMultiKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsMrkMultiKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkMultiKeyringInput = CreateAwsKmsMrkMultiKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsMrkMultiKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsMrkDiscoveryKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsMrkDiscoveryKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryKeyringInput = CreateAwsKmsMrkDiscoveryKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsMrkDiscoveryKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsMrkDiscoveryMultiKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput = CreateAwsKmsMrkDiscoveryMultiKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsMrkDiscoveryMultiKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsHierarchicalKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsHierarchicalKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput = CreateAwsKmsHierarchicalKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsHierarchicalKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsRsaKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsRsaKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput = CreateAwsKmsRsaKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsRsaKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateAwsKmsEcdhKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateAwsKmsEcdhKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput = CreateAwsKmsEcdhKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateAwsKmsEcdhKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateMultiKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateMultiKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput = CreateMultiKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateMultiKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateRawAesKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateRawAesKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput = CreateRawAesKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateRawAesKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateRawRsaKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateRawRsaKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput = CreateRawRsaKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateRawRsaKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateRawEcdhKeyring(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateRawEcdhKeyringInput) (awscryptographymaterialproviderssmithygeneratedtypes.IKeyring, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput = CreateRawEcdhKeyringInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateRawEcdhKeyring(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IKeyring
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = Keyring_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IKeyring))
	return native_response, nil

}

func (client *Client) CreateDefaultCryptographicMaterialsManager(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateDefaultCryptographicMaterialsManagerInput) (awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsManager, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsManager
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput = CreateDefaultCryptographicMaterialsManagerInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateDefaultCryptographicMaterialsManager(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsManager
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = CryptographicMaterialsManager_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager))
	return native_response, nil

}

func (client *Client) CreateRequiredEncryptionContextCMM(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateRequiredEncryptionContextCMMInput) (awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsManager, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsManager
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateRequiredEncryptionContextCMMInput = CreateRequiredEncryptionContextCMMInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateRequiredEncryptionContextCMM(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsManager
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = CryptographicMaterialsManager_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager))
	return native_response, nil

}

func (client *Client) CreateCryptographicMaterialsCache(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateCryptographicMaterialsCacheInput) (awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsCache, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsCache
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput = CreateCryptographicMaterialsCacheInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateCryptographicMaterialsCache(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.ICryptographicMaterialsCache
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = CryptographicMaterialsCache_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache))
	return native_response, nil

}

func (client *Client) CreateDefaultClientSupplier(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.CreateDefaultClientSupplierInput) (awscryptographymaterialproviderssmithygeneratedtypes.IClientSupplier, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IClientSupplier
		return defaultVal, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput = CreateDefaultClientSupplierInput_ToDafny(params)
	var dafny_response = client.DafnyClient.CreateDefaultClientSupplier(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		var defaultVal awscryptographymaterialproviderssmithygeneratedtypes.IClientSupplier
		return defaultVal, Error_FromDafny(err)
	}
	var native_response = ClientSupplier_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.IClientSupplier))
	return native_response, nil

}

func (client *Client) InitializeEncryptionMaterials(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.InitializeEncryptionMaterialsInput) (*awscryptographymaterialproviderssmithygeneratedtypes.EncryptionMaterials, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return nil, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput = InitializeEncryptionMaterialsInput_ToDafny(params)
	var dafny_response = client.DafnyClient.InitializeEncryptionMaterials(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return nil, Error_FromDafny(err)
	}
	var native_response = EncryptionMaterials_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.EncryptionMaterials))
	return &native_response, nil

}

func (client *Client) InitializeDecryptionMaterials(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.InitializeDecryptionMaterialsInput) (*awscryptographymaterialproviderssmithygeneratedtypes.DecryptionMaterials, error) {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return nil, opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput = InitializeDecryptionMaterialsInput_ToDafny(params)
	var dafny_response = client.DafnyClient.InitializeDecryptionMaterials(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return nil, Error_FromDafny(err)
	}
	var native_response = DecryptionMaterials_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.DecryptionMaterials))
	return &native_response, nil

}

func (client *Client) ValidEncryptionMaterialsTransition(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.ValidEncryptionMaterialsTransitionInput) error {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.ValidEncryptionMaterialsTransitionInput = ValidEncryptionMaterialsTransitionInput_ToDafny(params)
	var dafny_response = client.DafnyClient.ValidEncryptionMaterialsTransition(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return Error_FromDafny(err)
	}
	return nil
}

func (client *Client) ValidDecryptionMaterialsTransition(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.ValidDecryptionMaterialsTransitionInput) error {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.ValidDecryptionMaterialsTransitionInput = ValidDecryptionMaterialsTransitionInput_ToDafny(params)
	var dafny_response = client.DafnyClient.ValidDecryptionMaterialsTransition(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return Error_FromDafny(err)
	}
	return nil
}

func (client *Client) EncryptionMaterialsHasPlaintextDataKey(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.EncryptionMaterials) error {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = EncryptionMaterials_ToDafny(params)
	var dafny_response = client.DafnyClient.EncryptionMaterialsHasPlaintextDataKey(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return Error_FromDafny(err)
	}
	return nil
}

func (client *Client) DecryptionMaterialsWithPlaintextDataKey(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.DecryptionMaterials) error {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = DecryptionMaterials_ToDafny(params)
	var dafny_response = client.DafnyClient.DecryptionMaterialsWithPlaintextDataKey(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return Error_FromDafny(err)
	}
	return nil
}

func (client *Client) GetAlgorithmSuiteInfo(ctx context.Context, params []byte) (*awscryptographymaterialproviderssmithygeneratedtypes.AlgorithmSuiteInfo, error) {

	var dafny_request dafny.Sequence = Aws_cryptography_materialProviders_GetAlgorithmSuiteInfoInput_binaryId_ToDafny(params)
	var dafny_response = client.DafnyClient.GetAlgorithmSuiteInfo(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return nil, Error_FromDafny(err)
	}
	var native_response = AlgorithmSuiteInfo_FromDafny(dafny_response.Dtor_value().(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo))
	return &native_response, nil

}

func (client *Client) ValidAlgorithmSuiteInfo(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.AlgorithmSuiteInfo) error {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = AlgorithmSuiteInfo_ToDafny(params)
	var dafny_response = client.DafnyClient.ValidAlgorithmSuiteInfo(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return Error_FromDafny(err)
	}
	return nil
}

func (client *Client) ValidateCommitmentPolicyOnEncrypt(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.ValidateCommitmentPolicyOnEncryptInput) error {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnEncryptInput = ValidateCommitmentPolicyOnEncryptInput_ToDafny(params)
	var dafny_response = client.DafnyClient.ValidateCommitmentPolicyOnEncrypt(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return Error_FromDafny(err)
	}
	return nil
}

func (client *Client) ValidateCommitmentPolicyOnDecrypt(ctx context.Context, params awscryptographymaterialproviderssmithygeneratedtypes.ValidateCommitmentPolicyOnDecryptInput) error {
	err := params.Validate()
	if err != nil {
		opaqueErr := awscryptographymaterialproviderssmithygeneratedtypes.OpaqueError{
			ErrObject: err,
		}
		return opaqueErr
	}

	var dafny_request AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnDecryptInput = ValidateCommitmentPolicyOnDecryptInput_ToDafny(params)
	var dafny_response = client.DafnyClient.ValidateCommitmentPolicyOnDecrypt(dafny_request)

	if dafny_response.Is_Failure() {
		err := dafny_response.Dtor_error().(AwsCryptographyMaterialProvidersTypes.Error)
		return Error_FromDafny(err)
	}
	return nil
}
