import TestWrappedMaterialProvidersMain
import os
import _dafny

def GetTestVectorExecutionDirectory():
    return _dafny.Seq(os.getcwd() + "/../../")

TestWrappedMaterialProvidersMain.default__.GetTestVectorExecutionDirectory = GetTestVectorExecutionDirectory