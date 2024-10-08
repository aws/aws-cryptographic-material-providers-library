import _dafny
from pathlib import Path
import threading

import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries
from smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries import *
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers

# This is copy-pasted from DafnyStandardLibraries:
# https://github.com/dafny-lang/dafny/blob/f01af4a4e86a038ed4ea9f81464b2c9bca1955e4/Source/DafnyStandardLibraries/src/Std_Concurrent.py

class Lock:
    def ctor__(self):
        pass
        
    def __init__(self) -> None:
        self.lock = threading.Lock()

    def Lock__(self):
        self.lock.acquire()

    def Unlock(self):
        self.lock.release()


class MutableMap(smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries.MutableMap):
    def ctor__(self):
        pass
        
    def __init__(self) -> None:
        self.map = dict()
        self.lock = Lock()

    def Keys(self):
        self.lock.Lock__()
        s = self.map.keys()
        self.lock.Unlock()
        return _dafny.Set(s)

    def HasKey(self, k):
        self.lock.Lock__()
        b = k in self.map
        self.lock.Unlock()
        return b

    def Values(self):
        self.lock.Lock__()
        s = self.map.values()
        self.lock.Unlock()
        return _dafny.Set(s)

    def Items(self):
        self.lock.Lock__()
        s = self.map.items()
        self.lock.Unlock()
        return _dafny.Set(s)

    def Put(self, k, v):
        self.lock.Lock__()
        self.map[k] = v
        self.lock.Unlock()

    def Get(self, k):
        self.lock.Lock__()
        try:
            v = self.map.get(k)
        except KeyError:
            self.lock.Unlock()
            return Wrappers.Option_None()
        self.lock.Unlock()
        return Wrappers.Option_Some(v)

    def Remove(self, k):
        self.lock.Lock__()
        self.map.pop(k, None)
        self.lock.Unlock()

    def Size(self):
        self.lock.Lock__()
        l = len(self.map)
        self.lock.Unlock()
        return l
    
    # Added by Crypto Tools.
    # Crypto Tools externs refer a `Select` method
    # that does not exist on the Dafny implementation.
    def Select(self, k):
        return self.Get(k).value

# This is copy-pasted from DafnyStandardLibraries:
# https://github.com/dafny-lang/dafny/blob/f01af4a4e86a038ed4ea9f81464b2c9bca1955e4/Source/DafnyStandardLibraries/src/Std_FileIOInternalExterns.py

import traceback
import os.path
import pathlib

class FileIO:
    @staticmethod
    def INTERNAL_WriteBytesToFile(path, contents):
        path_str = path.VerbatimString(False)
        contents_bytes = bytes(contents)

        try:
            pathlib.Path(path_str).parent.mkdir(parents=True, exist_ok=True)

            with open(path_str, mode="wb") as file:
                contents = file.write(contents_bytes)
                return (False, _dafny.Seq())
        except:
            exc_str = traceback.format_exc()
            exc_seq = _dafny.Seq(exc_str)
            return (True, exc_seq)
        
    @staticmethod
    def INTERNAL_ReadBytesFromFile(path):
        path_str = path.VerbatimString(False)
        try:
            with open(path_str, mode="rb") as file:
                contents = file.read()
                contents_seq = _dafny.Seq(contents)
                return (False, contents_seq, _dafny.Seq())
        except:
            exc_str = traceback.format_exc()
            exc_seq = _dafny.Seq(exc_str)
            return (True, _dafny.Seq(), exc_seq)

# Export externs
smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries.FileIO = FileIO
smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries.MutableMap = MutableMap

import smithy_dafny_standard_library.internaldafny.generated.FileIO
smithy_dafny_standard_library.internaldafny.generated.FileIO.DafnyLibraries = smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries
