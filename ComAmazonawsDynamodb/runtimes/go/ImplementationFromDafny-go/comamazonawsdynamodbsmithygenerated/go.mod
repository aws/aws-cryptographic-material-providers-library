module xyz

go 1.23.2

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb => ..

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb v0.0.0-00010101000000-000000000000
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.0.1
	github.com/aws/aws-sdk-go v1.55.6
	github.com/aws/aws-sdk-go-v2/service/dynamodb v1.39.8
	github.com/aws/smithy-go v1.22.2
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.9.2
)

require (
	github.com/aws/aws-sdk-go-v2 v1.36.0 // indirect
	github.com/aws/aws-sdk-go-v2/internal/configsources v1.3.31 // indirect
	github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.6.31 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.12.2 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/endpoint-discovery v1.10.12 // indirect
)
