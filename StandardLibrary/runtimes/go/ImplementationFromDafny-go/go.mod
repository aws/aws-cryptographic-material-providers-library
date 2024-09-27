module github.com/dafny-lang/DafnyStandardLibGo

go 1.23.0

require github.com/dafny-lang/DafnyRuntimeGo v0.0.0

require github.com/google/uuid v1.6.0 // indirect

replace github.com/dafny-lang/DafnyRuntimeGo => ../../../../../smithy-dafny/DafnyRuntimeGo
