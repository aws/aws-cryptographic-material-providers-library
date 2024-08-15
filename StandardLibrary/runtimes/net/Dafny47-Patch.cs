using System.Numerics;

namespace String_Compile {

  public partial class __default {
    public static Dafny.ISequence<BigInteger> Int2Digits(BigInteger n, BigInteger @base)
    {
      Dafny.ISequence<BigInteger> _208___accumulator = Dafny.Sequence<BigInteger>.FromElements();
    TAIL_CALL_START: ;
      if ((n).Sign == 0) {
        return Dafny.Sequence<BigInteger>.Concat(Dafny.Sequence<BigInteger>.FromElements(), _208___accumulator);
      } else {
        _208___accumulator = Dafny.Sequence<BigInteger>.Concat(Dafny.Sequence<BigInteger>.FromElements(Dafny.Helpers.EuclideanModulus(n, @base)), _208___accumulator);
        BigInteger _in38 = Dafny.Helpers.EuclideanDivision(n, @base);
        BigInteger _in39 = @base;
        n = _in38;
        @base = _in39;
        goto TAIL_CALL_START;
      }
    }
    public static Dafny.ISequence<char> Digits2String(Dafny.ISequence<BigInteger> digits, Dafny.ISequence<char> chars)
    {
      Dafny.ISequence<char> _209___accumulator = Dafny.Sequence<char>.FromElements();
    TAIL_CALL_START: ;
      if ((digits).Equals(Dafny.Sequence<BigInteger>.FromElements())) {
        return Dafny.Sequence<char>.Concat(_209___accumulator, Dafny.Sequence<char>.FromString(""));
      } else {
        _209___accumulator = Dafny.Sequence<char>.Concat(_209___accumulator, Dafny.Sequence<char>.FromElements((chars).Select((digits).Select(BigInteger.Zero))));
        Dafny.ISequence<BigInteger> _in40 = (digits).Drop(BigInteger.One);
        Dafny.ISequence<char> _in41 = chars;
        digits = _in40;
        chars = _in41;
        goto TAIL_CALL_START;
      }
    }
    public static Dafny.ISequence<char> Int2String(BigInteger n, Dafny.ISequence<char> chars)
    {
      BigInteger _210_base = new BigInteger((chars).Count);
      if ((n).Sign == 0) {
        return Dafny.Sequence<char>.FromString("0");
      } else if ((n).Sign == 1) {
        return String_Compile.__default.Digits2String(String_Compile.__default.Int2Digits(n, _210_base), chars);
      } else {
        return Dafny.Sequence<char>.Concat(Dafny.Sequence<char>.FromString("-"), String_Compile.__default.Digits2String(String_Compile.__default.Int2Digits((BigInteger.Zero) - (n), _210_base), chars));
      }
    }
    public static Dafny.ISequence<char> Base10Int2String(BigInteger n) {
      return String_Compile.__default.Int2String(n, String_Compile.__default.Base10);
    }
    public static Dafny.ISequence<char> Base10 { get {
      return Dafny.Sequence<char>.FromElements('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
    } }
  }
} // end of namespace String_Compile