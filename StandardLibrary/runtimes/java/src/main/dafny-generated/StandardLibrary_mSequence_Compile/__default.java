// Class __default
// Dafny class __default compiled into Java
package StandardLibrary_mSequence_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T, __R, __E> Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> MapWithResult(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R, dafny.TypeDescriptor<__E> _td___E, java.util.function.Function<__T, Wrappers_Compile.Result<__R, __E>> f, dafny.DafnySequence<? extends __T> xs, long pos, dafny.DafnySequence<? extends __R> acc)
  {
    TAIL_CALL_START: while (true) {
      if (((long) (xs).cardinalityInt()) == (pos)) {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>create_Success(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, acc);
      } else {
        Wrappers_Compile.Result<__R, __E> _0_valueOrError0 = ((Wrappers_Compile.Result<__R, __E>)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((xs).select(dafny.Helpers.unsignedToInt(pos)))))));
        if ((_0_valueOrError0).IsFailure(_td___R, _td___E)) {
          return (_0_valueOrError0).<dafny.DafnySequence<? extends __R>>PropagateFailure(_td___R, _td___E, dafny.DafnySequence.<__R>_typeDescriptor(_td___R));
        } else {
          __R _1_head = (_0_valueOrError0).Extract(_td___R, _td___E);
          java.util.function.Function<__T, Wrappers_Compile.Result<__R, __E>> _in0 = f;
          dafny.DafnySequence<? extends __T> _in1 = xs;
          long _in2 = (long) (long) ((pos) + ((long) 1L));
          dafny.DafnySequence<? extends __R> _in3 = dafny.DafnySequence.<__R>concatenate(acc, dafny.DafnySequence.<__R> of(_td___R, _1_head));
          f = _in0;
          xs = _in1;
          pos = _in2;
          acc = _in3;
          continue TAIL_CALL_START;
        }
      }
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Flatten(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> xs, long pos, dafny.DafnySequence<? extends __T> acc)
  {
    TAIL_CALL_START: while (true) {
      if (((long) (xs).cardinalityInt()) == (pos)) {
        return acc;
      } else {
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> _in0 = xs;
        long _in1 = (long) (long) ((pos) + ((long) 1L));
        dafny.DafnySequence<? extends __T> _in2 = dafny.DafnySequence.<__T>concatenate(acc, ((dafny.DafnySequence<? extends __T>)(java.lang.Object)((xs).select(dafny.Helpers.unsignedToInt(pos)))));
        xs = _in0;
        pos = _in1;
        acc = _in2;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> boolean SequenceEqualNat(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> seq1, dafny.DafnySequence<? extends __T> seq2, java.math.BigInteger start1, java.math.BigInteger start2, java.math.BigInteger size)
  {
    return __default.<__T>SequenceEqual(_td___T, seq1, seq2, (start1).longValue(), (start2).longValue(), (size).longValue());
  }
  public static <__T> boolean SequenceEqual(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> seq1, dafny.DafnySequence<? extends __T> seq2, long start1, long start2, long size)
  {
    boolean ret = false;
    long _0_j;
    _0_j = start2;
    long _hi0 = (long) (long) ((start1) + (size));
    for (long _1_i = start1; java.lang.Long.compareUnsigned(_1_i, _hi0) < 0; _1_i++) {
      if (!java.util.Objects.equals(((__T)(java.lang.Object)((seq1).select(dafny.Helpers.unsignedToInt(_1_i)))), ((__T)(java.lang.Object)((seq2).select(dafny.Helpers.unsignedToInt(_0_j)))))) {
        ret = false;
        return ret;
      }
      _0_j = (long) (long) ((_0_j) + ((long) 1L));
    }
    ret = true;
    return ret;
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibrary.Sequence._default";
  }
}
