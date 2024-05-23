from multiprocessing import Lock
import functools

def synchronized(wrapped):
    lock = Lock()
    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)
    return _wrap

# externs depend on the synchronized definition;
# import them after defining synchonized
from . import (
    StormTrackingCMC,
    SynchronizedLocalCMC,
    StormTrackerEnforcesOneFanOut,
)