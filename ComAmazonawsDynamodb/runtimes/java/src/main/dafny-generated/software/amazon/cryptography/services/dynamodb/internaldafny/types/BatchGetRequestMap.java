// Class BatchGetRequestMap
// Dafny class BatchGetRequestMap compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchGetRequestMap {
  public BatchGetRequestMap() {
  }
  public static boolean _Is(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> __source) {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> _8_x = __source;
    return __default.IsValid__BatchGetRequestMap(_8_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>> _TYPE = dafny.TypeDescriptor.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>>referenceWithInitializer(dafny.DafnyMap.class, () -> dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,KeysAndAttributes> empty());
  public static dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
