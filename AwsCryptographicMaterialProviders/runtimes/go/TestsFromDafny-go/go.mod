module github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/test

go 1.23.0

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl v0.0.0 => ../ImplementationFromDafny-go

replace (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb v0.0.0 => ../../../../ComAmazonawsDynamodb/runtimes/go/ImplementationFromDafny-go/
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms v0.0.0 => ../../../../ComAmazonawsKms/runtimes/go/ImplementationFromDafny-go/
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives v0.0.0 => ../../../../AwsCryptographyPrimitives/runtimes/go/ImplementationFromDafny-go/

)

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library => ../../../../StandardLibrary/runtimes/go/ImplementationFromDafny-go/

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb v0.0.0
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms v0.0.0
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl v0.0.0
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives v0.0.0
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.0.0
	github.com/aws/aws-sdk-go-v2/service/dynamodb v1.35.1
	github.com/aws/aws-sdk-go-v2/service/kms v1.36.0
	github.com/aws/smithy-go v1.21.0
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.9.2
)

require (
	github.com/aws/aws-sdk-go-v2 v1.31.0 // indirect
	github.com/aws/aws-sdk-go-v2/config v1.27.37 // indirect
	github.com/aws/aws-sdk-go-v2/credentials v1.17.35 // indirect
	github.com/aws/aws-sdk-go-v2/feature/ec2/imds v1.16.14 // indirect
	github.com/aws/aws-sdk-go-v2/internal/configsources v1.3.18 // indirect
	github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.6.18 // indirect
	github.com/aws/aws-sdk-go-v2/internal/ini v1.8.1 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.11.5 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/endpoint-discovery v1.9.19 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/presigned-url v1.11.20 // indirect
	github.com/aws/aws-sdk-go-v2/service/sso v1.23.1 // indirect
	github.com/aws/aws-sdk-go-v2/service/ssooidc v1.27.1 // indirect
	github.com/aws/aws-sdk-go-v2/service/sts v1.31.1 // indirect
	github.com/google/uuid v1.6.0 // indirect
	github.com/jmespath/go-jmespath v0.4.0 // indirect
)
