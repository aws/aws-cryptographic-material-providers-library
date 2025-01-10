module github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/test

go 1.23.0

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.0.0 => ../ImplementationFromDafny-go

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.0.0
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.9.1
)

require github.com/google/uuid v1.6.0 // indirect
