module github.com/dafny-lang/DafnyStandardLibGo/test

go 1.23.0

replace github.com/dafny-lang/DafnyStandardLibGo v0.0.0 => ../ImplementationFromDafny-go

require (
	github.com/dafny-lang/DafnyRuntimeGo/v4 v4.8.0
	github.com/dafny-lang/DafnyStandardLibGo v0.0.0
)

require github.com/google/uuid v1.6.0 // indirect
