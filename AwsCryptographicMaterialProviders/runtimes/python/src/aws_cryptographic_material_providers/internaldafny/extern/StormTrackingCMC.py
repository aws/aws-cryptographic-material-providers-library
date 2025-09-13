import time
import datetime
import pytz
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
from . import Lock
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import Error_Opaque

class StormTrackingCMC:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.lock = Lock()

    def PutCacheEntry(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.PutCacheEntry(input)
        finally:
            self.lock.Unlock()
        return val
    
    def UpdateUsageMetadata(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.UpdateUsageMetadata(input)
        finally:
            self.lock.Unlock()
        return val
    
    # NOT locked, as some sleeping might be involved
    def GetCacheEntry(self, input):
        return self.GetCacheEntry_k(input)
    
    def DeleteCacheEntry(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.DeleteCacheEntry(input)
        finally:
            self.lock.Unlock()
        return val
    
    def PutCacheEntry_k(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.PutCacheEntry(input)
        finally:
            self.lock.Unlock()
        return val
    
    def UpdateUsageMetadata_k(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.UpdateUsageMetadata(input)
        finally:
            self.lock.Unlock()
        return val
    
    # This is the synchronization for GetCacheEntry and GetCacheEntry_k
    def GetFromCacheInner(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.GetFromCache(input)
        finally:
            self.lock.Unlock()
        return val
    
    # NOT locked, because we sleep. Calls GetFromCache which IS synchronized.
    def GetCacheEntry_k(self, input):
        max_in_flight = round(datetime.datetime.now(tz = pytz.UTC).timestamp() * 1000) + self.wrapped.inFlightTTL;
        sleep_time = self.wrapped.sleepMilli;
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
                if round(datetime.datetime.now(tz = pytz.UTC).timestamp() * 1000) <= max_in_flight:
                    try:
                        time.sleep(self.wrapped.sleepMilli)
                    except Exception as e:
                        return Wrappers.Result_Failure(
                            Error_Opaque(
                                e
                            )
                        )
                else:
                    return Wrappers.Result_Failure(
                        aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InFlightTTLExceeded(
                            "Storm cache inFlightTTL exceeded"
                        )
                    ) 


    def DeleteCacheEntry_k(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.DeleteCacheEntry(input)
        finally:
            self.lock.Unlock()
        return val
    
    def __str__(self):
        return "StormTracker.StormTrackerCMC"

aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC.StormTrackingCMC = StormTrackingCMC