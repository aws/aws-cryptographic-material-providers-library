// Class __default
// Dafny class __default compiled into Java
package Seq_mMergeSort_Compile;

import Wrappers_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T> dafny.DafnySequence<? extends __T> MergeSortBy(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> a, dafny.Function2<__T, __T, Boolean> lessThanOrEq)
  {
    if ((java.math.BigInteger.valueOf((a).length())).compareTo(java.math.BigInteger.ONE) <= 0) {
      return a;
    } else {
      java.math.BigInteger _0_splitIndex = dafny.DafnyEuclidean.EuclideanDivision(java.math.BigInteger.valueOf((a).length()), java.math.BigInteger.valueOf(2L));
      dafny.DafnySequence<? extends __T> _1_left = (a).take(_0_splitIndex);
      dafny.DafnySequence<? extends __T> _2_right = (a).drop(_0_splitIndex);
      dafny.DafnySequence<? extends __T> _3_leftSorted = __default.<__T>MergeSortBy(_td___T, _1_left, lessThanOrEq);
      dafny.DafnySequence<? extends __T> _4_rightSorted = __default.<__T>MergeSortBy(_td___T, _2_right, lessThanOrEq);
      return __default.<__T>MergeSortedWith(_td___T, _3_leftSorted, _4_rightSorted, lessThanOrEq);
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> MergeSortedWith(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> left, dafny.DafnySequence<? extends __T> right, dafny.Function2<__T, __T, Boolean> lessThanOrEq)
  {
    dafny.DafnySequence<? extends __T> _0___accumulator = dafny.DafnySequence.<__T> empty(_td___T);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((left).length())).signum() == 0) {
        return dafny.DafnySequence.<__T>concatenate(_0___accumulator, right);
      } else if ((java.math.BigInteger.valueOf((right).length())).signum() == 0) {
        return dafny.DafnySequence.<__T>concatenate(_0___accumulator, left);
      } else if (((boolean)(java.lang.Object)((lessThanOrEq).apply(((__T)(java.lang.Object)((left).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), ((__T)(java.lang.Object)((right).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))) {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> of(_td___T, ((__T)(java.lang.Object)((left).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))));
        dafny.DafnySequence<? extends __T> _in0 = (left).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends __T> _in1 = right;
        dafny.Function2<__T, __T, Boolean> _in2 = lessThanOrEq;
        left = _in0;
        right = _in1;
        lessThanOrEq = _in2;
        continue TAIL_CALL_START;
      } else {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> of(_td___T, ((__T)(java.lang.Object)((right).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))));
        dafny.DafnySequence<? extends __T> _in3 = left;
        dafny.DafnySequence<? extends __T> _in4 = (right).drop(java.math.BigInteger.ONE);
        dafny.Function2<__T, __T, Boolean> _in5 = lessThanOrEq;
        left = _in3;
        right = _in4;
        lessThanOrEq = _in5;
        continue TAIL_CALL_START;
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "Seq.MergeSort._default";
  }
}
