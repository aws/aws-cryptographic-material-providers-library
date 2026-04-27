// Class KeyList
// Dafny class KeyList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyList {
  public KeyList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> __source) {
    dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _11_x = __source;
    return __default.IsValid__KeyList(_11_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> empty(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
