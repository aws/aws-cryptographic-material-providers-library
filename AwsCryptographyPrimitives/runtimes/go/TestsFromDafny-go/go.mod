module github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/test

go 1.23.0

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives => ../ImplementationFromDafny-go

require github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.2.0

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives v0.0.0
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.9.2
)

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library => ../../../../StandardLibrary/runtimes/go/ImplementationFromDafny-go/
