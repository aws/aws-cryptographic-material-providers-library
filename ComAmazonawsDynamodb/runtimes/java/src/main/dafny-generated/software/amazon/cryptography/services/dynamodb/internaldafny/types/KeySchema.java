// Class KeySchema
// Dafny class KeySchema compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeySchema {
  public KeySchema() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends KeySchemaElement> __source) {
    dafny.DafnySequence<? extends KeySchemaElement> _12_x = __source;
    return __default.IsValid__KeySchema(_12_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends KeySchemaElement>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends KeySchemaElement>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<KeySchemaElement> empty(KeySchemaElement._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends KeySchemaElement>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends KeySchemaElement>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
