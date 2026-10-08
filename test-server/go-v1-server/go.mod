module github.com/aws/aws-cryptographic-material-providers-library/test-server/go-v1-server

go 1.24

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives v0.0.0
	github.com/aws/smithy-go v1.25.1
)

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.4.0 // indirect
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.11.3 // indirect
)

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives => ../../releases/go/primitives

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library => ../../releases/go/smithy-dafny-standard-library
