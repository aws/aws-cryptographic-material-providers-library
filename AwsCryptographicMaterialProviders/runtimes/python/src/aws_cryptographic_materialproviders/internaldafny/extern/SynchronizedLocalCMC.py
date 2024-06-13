import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC
import standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
from . import synchronized

class SynchronizedLocalCMC:

    def __init__(self, wrapped):
        self.wrapped = wrapped

    @synchronized
    def PutCacheEntry(self, input):
        return self.wrapped.PutCacheEntry(input)
    
    @synchronized
    def UpdateUsageMetadata(self, input):
        return self.wrapped.UpdateUsageMetadata(input)
    
    @synchronized
    def GetCacheEntry(self, input):
        return self.wrapped.GetCacheEntry(input)
    
    @synchronized
    def DeleteCacheEntry(self, input):
        return self.wrapped.DeleteCacheEntry(input)
    
    @synchronized
    def PutCacheEntry_k(self, input):
        return self.wrapped.PutCacheEntry(input)
    
    @synchronized
    def UpdateUsageMetadata_k(self, input):
        return self.wrapped.UpdateUsageMetadata(input)
    
    @synchronized
    def GetFromCacheInner(self, input):
        return self.wrapped.GetFromCache(input)
    
    @synchronized
    def GetCacheEntry_k(self, input):
        return self.wrapped.GetCacheEntry(input)

    @synchronized
    def DeleteCacheEntry_k(self, input):
        return self.wrapped.DeleteCacheEntry(input)
    
    def __str__(self):
        return "LocalCMC.StormTrackerCMC"

aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC.SynchronizedLocalCMC = SynchronizedLocalCMC