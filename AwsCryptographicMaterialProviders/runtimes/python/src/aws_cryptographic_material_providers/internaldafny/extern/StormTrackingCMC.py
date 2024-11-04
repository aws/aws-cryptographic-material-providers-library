import time
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
from . import Lock

class StormTrackingCMC:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.lock = Lock()

    def PutCacheEntry(self, input):
        self.lock.Lock__()
        val = self.wrapped.PutCacheEntry(input)
        self.lock.Unlock()
        return val
    
    def UpdateUsageMetadata(self, input):
        self.lock.Lock__()
        val = self.wrapped.UpdateUsageMetadata(input)
        self.lock.Unlock()
        return val
    
    # NOT locked, as some sleeping might be involved
    def GetCacheEntry(self, input):
        return self.GetCacheEntry_k(input)
    
    def DeleteCacheEntry(self, input):
        self.lock.Lock__()
        val = self.wrapped.DeleteCacheEntry(input)
        self.lock.Unlock()
        return val
    
    def PutCacheEntry_k(self, input):
        self.lock.Lock__()
        val = self.wrapped.PutCacheEntry(input)
        self.lock.Unlock()
        return val
    
    def UpdateUsageMetadata_k(self, input):
        self.lock.Lock__()
        val = self.wrapped.UpdateUsageMetadata(input)
        self.lock.Unlock()
        return val
    
    # This is the synchronization for GetCacheEntry and GetCacheEntry_k
    def GetFromCacheInner(self, input):
        self.lock.Lock__()
        val = self.wrapped.GetFromCache(input)
        self.lock.Unlock()
        return val
    
    # NOT locked, because we sleep. Calls GetFromCache which IS synchronized.
    def GetCacheEntry_k(self, input):
        while True:
            result = self.GetFromCacheInner(input)
            if result.is_Failure:
                return Wrappers.Result_Failure(result.error)
            elif result.value.is_Full:
                return Wrappers.Result_Success(result.value.data)
            elif result.value.is_EmptyFetch:
                return Wrappers.Result_Failure(
                    aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_EntryDoesNotExist(
                        "Entry does not exist"
                    )
                ) 
            else:
                try:
                    time.sleep(self.wrapped.sleepMilli)
                except:
                    pass

    def DeleteCacheEntry_k(self, input):
        self.lock.Lock__()
        val = self.wrapped.DeleteCacheEntry(input)
        self.lock.Unlock()
        return val
    
    def __str__(self):
        return "StormTracker.StormTrackerCMC"

aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC.StormTrackingCMC = StormTrackingCMC