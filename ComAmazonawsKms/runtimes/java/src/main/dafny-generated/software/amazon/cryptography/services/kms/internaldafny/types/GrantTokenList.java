// Class GrantTokenList
// Dafny class GrantTokenList compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantTokenList {
  public GrantTokenList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> __source) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _10_x = __source;
    return __default.IsValid__GrantTokenList(_10_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(GrantTokenType._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
