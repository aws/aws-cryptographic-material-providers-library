module github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives/test

go 1.23.0

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives v0.2.2 => ../ImplementationFromDafny-go

require github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.2.2

require (
	github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives v0.2.2
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.11.1
)

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library => ../../../../StandardLibrary/runtimes/go/ImplementationFromDafny-go/
