# Dafny program the_program compiled into Python
import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_ as module_
import _dafny as _dafny

import WrappedMaterialProvidersMain
try:
    dafnyArgs = [_dafny.Seq(a) for a in sys.argv]
    WrappedMaterialProvidersMain.default__.Main(dafnyArgs)
except _dafny.HaltException as e:
    _dafny.print("[Program halted] " + e.message + "\n")
    sys.exit(1)
