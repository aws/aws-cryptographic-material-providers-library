from standard_library.internal_generated_dafny.SortedSets import *
import standard_library.internal_generated_dafny.SortedSets
import _dafny

class default__:

  @staticmethod
  def SetToSequence(input_set):
    return _dafny.Seq(input_set.Elements)

standard_library.internal_generated_dafny.SortedSets.default__ = default__