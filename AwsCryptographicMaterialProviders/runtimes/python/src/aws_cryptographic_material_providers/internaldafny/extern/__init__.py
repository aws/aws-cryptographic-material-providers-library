# This is copy-pasted from DafnyStandardLibraries:
# https://github.com/dafny-lang/dafny/blob/f01af4a4e86a038ed4ea9f81464b2c9bca1955e4/Source/DafnyStandardLibraries/src/Std_Concurrent.py
import threading

# Module: Std_Concurrent

class Lock:
    def ctor__(self):
        pass
        
    def __init__(self) -> None:
        self.lock = threading.Lock()

    def Lock__(self):
        self.lock.acquire()

    def Unlock(self):
        self.lock.release()

# externs depend on the Lock definition;
# import them after defining Lock
from . import (
    StormTrackingCMC,
    SynchronizedLocalCMC,
)