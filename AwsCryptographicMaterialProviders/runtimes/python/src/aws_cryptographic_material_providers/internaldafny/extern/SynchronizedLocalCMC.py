import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
from . import Lock

class SynchronizedLocalCMC:

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
    
    def GetCacheEntry(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.GetCacheEntry(input)
        finally:
            self.lock.Unlock()
        return val
    
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
    
    def GetFromCacheInner(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.GetFromCache(input)
        finally:
            self.lock.Unlock()
        return val
    
    def GetCacheEntry_k(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.GetCacheEntry(input)
        finally:
            self.lock.Unlock()
        return val

    def DeleteCacheEntry_k(self, input):
        self.lock.Lock__()
        try:
            val = self.wrapped.DeleteCacheEntry(input)
        finally:
            self.lock.Unlock()
        return val
    
    def __str__(self):
        return "LocalCMC.SynchronizedLocalCMC"

aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC.SynchronizedLocalCMC = SynchronizedLocalCMC