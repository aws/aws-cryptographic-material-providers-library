from smithy_dafny_standard_library.internaldafny.generated.SortedSets import *
import smithy_dafny_standard_library.internaldafny.generated.SortedSets
import _dafny

class default__:

  @staticmethod
  def SetToSequence(input_set):
    return _dafny.Seq(input_set.Elements)
  
  @staticmethod
  def SetToOrderedSequence(input_set, is_less_than):
    seq_as_list = list(_dafny.Seq(input_set.Elements).Elements)
    comparer = Comparer(is_less_than)
    from functools import cmp_to_key
    sorted_list = sorted(seq_as_list, key=cmp_to_key(comparer.compare))
    return _dafny.Seq(sorted_list)
  
  @staticmethod
  def SetToOrderedSequence2(input_set, is_less_than):
    return default__.SetToOrderedSequence(input_set, is_less_than)
  
class Comparer:
  is_less_than: Any

  def __init__(self, is_less_than):
    self.is_less_than = is_less_than

  def compare(self, x, y):
    x_list = list(x.Elements)
    y_list = list(y.Elements)
    
    for i in range(0, min(len(x_list), len(y_list))):
      if (self.is_less_than(x_list[i], y_list[i])):
        return -1
      if (self.is_less_than(y_list[i], x_list[i])):
        return 1
    # Reached the end of one array. Either they are equal, or the
    # one which is shorter should be considered "less than"
    if len(x_list) < len(y_list):
      return -1
    elif len(x_list) == len(y_list):
      return 0
    elif len(x_list) > len(y_list):
      return 1

# Export extern
smithy_dafny_standard_library.internaldafny.generated.SortedSets.default__ = default__