module github.com/aws/aws-cryptographic-material-providers-library/releases/go/primitives

go 1.23.0

require github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library v0.2.2

require github.com/dafny-lang/DafnyRuntimeGo/v4 v4.11.2

replace github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library => ../../../../StandardLibrary/runtimes/go/ImplementationFromDafny-go/
