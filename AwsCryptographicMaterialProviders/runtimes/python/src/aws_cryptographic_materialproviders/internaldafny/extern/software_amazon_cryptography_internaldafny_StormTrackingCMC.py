import software_amazon_cryptography_internaldafny_StormTrackingCMC
import Wrappers
import software_amazon_cryptography_materialproviders_internaldafny_types
import time
import threading
import functools

# decorator that locks calls to a function
def synchronized(wrapped):
    lock = threading.Lock()
    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)
    return _wrap

class StormTrackingCMC:

    def __init__(self, wrapped):
        self.wrapped = wrapped

    @synchronized
    def PutCacheEntry(self, input):
        return self.wrapped.PutCacheEntry(input)
    
    @synchronized
    def UpdateUsageMetadata(self, input):
        return self.wrapped.UpdateUsageMetadata(input)
    
    # NOT synchronized, as some sleeping might be involved
    def GetCacheEntry(self, input):
        return self.GetCacheEntry_k(input)
    
    @synchronized
    def DeleteCacheEntry(self, input):
        return self.wrapped.DeleteCacheEntry(input)
    
    @synchronized
    def PutCacheEntry_k(self, input):
        return self.wrapped.PutCacheEntry(input)
    
    @synchronized
    def UpdateUsageMetadata_k(self, input):
        return self.wrapped.UpdateUsageMetadata(input)
    
    # This is the synchronization for GetCacheEntry and GetCacheEntry_k
    @synchronized
    def GetFromCacheInner(self, input):
        return self.wrapped.GetFromCache(input)
    
    # NOT synchronized, because we sleep. Calls GetFromCache which IS synchronized.
    def GetCacheEntry_k(self, input):
        while True:
            result = self.GetFromCacheInner(input)
            if result.is_Failure:
                return Wrappers.Result_Failure(result.error)
            elif result.value.is_Full:
                return Wrappers.Result_Success(result.value.data)
            elif result.value.is_EmptyFetch:
                return Wrappers.Result_Failure(
                    software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(
                        "Entry does not exist"
                    )
                ) 
            else:
                try:
                    time.sleep(self.wrapped.sleepMilli)
                except:
                    pass

    @synchronized
    def DeleteCacheEntry_k(self, input):
        return self.wrapped.DeleteCacheEntry(input)
    
    def __str__(self):
        return "StormTracker_Compile.StormTrackerCMC"

software_amazon_cryptography_internaldafny_StormTrackingCMC.StormTrackingCMC = StormTrackingCMC