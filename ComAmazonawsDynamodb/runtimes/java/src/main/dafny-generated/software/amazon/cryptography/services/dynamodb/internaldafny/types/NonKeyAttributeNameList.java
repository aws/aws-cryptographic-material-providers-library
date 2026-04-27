// Class NonKeyAttributeNameList
// Dafny class NonKeyAttributeNameList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class NonKeyAttributeNameList {
  public NonKeyAttributeNameList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> __source) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _19_x = __source;
    return __default.IsValid__NonKeyAttributeNameList(_19_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(NonKeyAttributeName._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
