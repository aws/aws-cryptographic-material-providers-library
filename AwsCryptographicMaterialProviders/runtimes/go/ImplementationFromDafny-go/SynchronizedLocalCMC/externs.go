package SynchronizedLocalCMC

import (
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/AwsCryptographyMaterialProvidersTypes"
	"github.com/aws/aws-cryptographic-material-providers-library/mpl/LocalCMC"
)

type SynchronizedLocalCMC struct {
	AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
}

func New_SynchronizedLocalCMC_() *SynchronizedLocalCMC {
	return &SynchronizedLocalCMC{LocalCMC.New_LocalCMC_()}
}
