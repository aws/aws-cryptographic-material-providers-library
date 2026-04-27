// Class HexString
// Dafny class HexString compiled into Java
package HexStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class HexString {
  public HexString() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends Character> __source) {
    dafny.DafnySequence<? extends Character> _0_x = __source;
    return __default.IsHexString(_0_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends Character>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
