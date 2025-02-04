module github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/test

go 1.23.0

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library => ../ImplementationFromDafny-go

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.1.0
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.9.2
)

require github.com/google/uuid v1.6.0 // indirect
