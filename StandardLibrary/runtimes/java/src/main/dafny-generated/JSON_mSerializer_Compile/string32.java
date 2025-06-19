// Class string32
// Dafny class string32 compiled into Java
package JSON_mSerializer_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class string32 {
  public string32() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends Character> __source) {
    dafny.DafnySequence<? extends Character> _1_s = __source;
    return (java.math.BigInteger.valueOf((_1_s).length())).compareTo(BoundedInts_Compile.__default.TWO__TO__THE__32()) < 0;
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends Character>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
