package StormTrackingCMC

import (
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/StormTracker"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

type StormTrackingCMC struct {
	AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
}

func New_StormTrackingCMC_(stormTracker *StormTracker.StormTracker) *StormTrackingCMC {
	return &StormTrackingCMC{ICryptographicMaterialsCache: stormTracker.Wrapped}
}

func (cmc *StormTrackingCMC) GetCacheEntry(input AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput) Wrappers.Result {
	return cmc.ICryptographicMaterialsCache.GetCacheEntry(input)
}
