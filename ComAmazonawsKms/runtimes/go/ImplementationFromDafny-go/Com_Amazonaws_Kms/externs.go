package Com_Amazonaws_Kms

import (
	"context"

	ComAmazonawsKmsTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms/ComAmazonawsKmsTypes"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms/KMSwrapped"
	"github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Wrappers"
	"github.com/aws/aws-sdk-go-v2/aws/middleware"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/kms"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

func (_static *CompanionStruct_Default___) KMSClientForRegion(regionInput _dafny.Sequence) Wrappers.Result {
	region := *toString(regionInput)
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(ComAmazonawsKmsTypes.Companion_Error_.Create_KMSInternalException_(Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfChars([]_dafny.Char(err.Error())...))))
	}
	return Wrappers.Companion_Result_.Create_Success_(&KMSwrapped.Shim{Client: kms.NewFromConfig(cfg, func(o *kms.Options) {
		o.Region = region
		o.APIOptions = append(o.APIOptions, middleware.AddUserAgentKey(_static.UserAgentSuffix()))
	})})
}

func (_static *CompanionStruct_Default___) KMSClient() Wrappers.Result {
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(ComAmazonawsKmsTypes.Companion_Error_.Create_KMSInternalException_(Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfChars([]_dafny.Char(err.Error())...))))
	}
	return Wrappers.Companion_Result_.Create_Success_(&KMSwrapped.Shim{Client: kms.NewFromConfig(cfg, func(o *kms.Options) {
		o.APIOptions = append(o.APIOptions, middleware.AddUserAgentKey(_static.UserAgentSuffix()))
	})})
}

func (_static *CompanionStruct_Default___) RegionMatch(ikmsClient ComAmazonawsKmsTypes.IKMSClient, regionInput _dafny.Sequence) Wrappers.Option {
	region := toString(regionInput)
	var kmsShim = ikmsClient.(*KMSwrapped.Shim).Client
	return Wrappers.Companion_Option_.Create_Some_(kmsShim.Options().Region == *region)
}

func toString(input _dafny.Sequence) *string {
	var s string
	for i := _dafny.Iterate(input); ; {
		val, ok := i()
		if !ok {
			return &[]string{s}[0]
		} else {
			s = s + string(val.(_dafny.Char))
		}
	}
}

func (_static *CompanionStruct_Default___) UserAgentSuffix() string {
	// Create a Dafny sequence with "Go" as the runtime
	runtime := _dafny.SeqOfChars([]_dafny.Char("Go")...)

	// Call the DafnyUserAgentSuffix function and convert the result to a Go string
	dafnyUserAgentSuffix := _static.DafnyUserAgentSuffix(runtime)
	return *toString(dafnyUserAgentSuffix)
}
