from standard_library.internaldafny.generated.SortedSets import *
import standard_library.internaldafny.generated.SortedSets
import standard_library.internaldafny.extern.UTF8
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
    '''
    Compare bytes of utf-16-be encodings of chars x and y.
    '''
    # x and y are _dafny.Seqs of length 1 (char)
    x_char = x.Elements[0]
    y_char = y.Elements[0]
    
    x_encode = x_char.encode("utf-16-be")
    y_encode = y_char.encode("utf-16-be")

    for i in range(0, min(len(x_encode), len(y_encode))):
      if (self.is_less_than(x_encode[i], y_encode[i])):
        return -1
      if (self.is_less_than(y_encode[i], x_encode[i])):
        return 1
    # Reached the end of one array. Either they are equal, or the
    # one which is shorter should be considered "less than"
    if len(x_encode) < len(y_encode):
      return -1
    elif len(x_encode) == len(y_encode):
      return 0
    elif len(x_encode) > len(y_encode):
      return 1


standard_library.internaldafny.generated.SortedSets.default__ = default__