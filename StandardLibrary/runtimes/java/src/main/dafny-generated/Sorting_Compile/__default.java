// Class __default
// Dafny class __default compiled into Java
package Sorting_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean LexicographicByteSeqBelow(dafny.DafnySequence<? extends java.lang.Byte> x, dafny.DafnySequence<? extends java.lang.Byte> y)
  {
    return __default.LexicographicByteSeqBelowAux(x, y, java.math.BigInteger.ZERO);
  }
  public static boolean LexicographicByteSeqBelowAux(dafny.DafnySequence<? extends java.lang.Byte> x, dafny.DafnySequence<? extends java.lang.Byte> y, java.math.BigInteger n)
  {
    return ((java.util.Objects.equals(n, java.math.BigInteger.valueOf((x).length()))) || ((!java.util.Objects.equals(n, java.math.BigInteger.valueOf((y).length()))) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((n))))), ((byte)(java.lang.Object)((y).select(dafny.Helpers.toInt((n)))))) < 0))) || (((!java.util.Objects.equals(n, java.math.BigInteger.valueOf((y).length()))) && ((((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((n)))))) == (((byte)(java.lang.Object)((y).select(dafny.Helpers.toInt((n)))))))) && (__default.LexicographicByteSeqBelowAux(x, y, (n).add(java.math.BigInteger.ONE))));
  }
  public static <__Data> void SelectionSort(dafny.TypeDescriptor<__Data> _td___Data, java.lang.Object a, dafny.Function2<__Data, __Data, Boolean> below)
  {
    java.math.BigInteger _0_m = java.math.BigInteger.ZERO;
    _0_m = java.math.BigInteger.ZERO;
    while ((_0_m).compareTo(java.math.BigInteger.valueOf(java.lang.reflect.Array.getLength((a)))) < 0) {
      java.math.BigInteger _1_mindex = java.math.BigInteger.ZERO;
      java.math.BigInteger _2_n = java.math.BigInteger.ZERO;
      java.math.BigInteger _rhs0 = _0_m;
      java.math.BigInteger _rhs1 = (_0_m).add(java.math.BigInteger.ONE);
      _1_mindex = _rhs0;
      _2_n = _rhs1;
      while ((_2_n).compareTo(java.math.BigInteger.valueOf(java.lang.reflect.Array.getLength((a)))) < 0) {
        if (!(((boolean)(java.lang.Object)((below).apply(_td___Data.getArrayElement((a), (dafny.Helpers.toInt((_1_mindex)))), _td___Data.getArrayElement((a), (dafny.Helpers.toInt((_2_n))))))))) {
          _1_mindex = _2_n;
        }
        _2_n = (_2_n).add(java.math.BigInteger.ONE);
      }
      __Data _rhs2 = _td___Data.getArrayElement((a), (dafny.Helpers.toInt((_1_mindex))));
      __Data _rhs3 = _td___Data.getArrayElement((a), (dafny.Helpers.toInt((_0_m))));
      java.lang.Object _lhs0 = a;
      java.math.BigInteger _lhs1 = _0_m;
      java.lang.Object _lhs2 = a;
      java.math.BigInteger _lhs3 = _1_mindex;
      _td___Data.setArrayElement(_lhs0, dafny.Helpers.toInt((_lhs1).intValue()), _rhs2);
      _td___Data.setArrayElement(_lhs2, dafny.Helpers.toInt((_lhs3).intValue()), _rhs3);
      _0_m = (_0_m).add(java.math.BigInteger.ONE);
    }
  }
  @Override
  public java.lang.String toString() {
    return "Sorting._default";
  }
}
