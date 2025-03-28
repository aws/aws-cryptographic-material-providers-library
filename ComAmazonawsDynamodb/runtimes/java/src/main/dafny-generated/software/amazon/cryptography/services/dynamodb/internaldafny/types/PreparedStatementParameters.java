// Class PreparedStatementParameters
// Dafny class PreparedStatementParameters compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PreparedStatementParameters {
  public PreparedStatementParameters() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends AttributeValue> __source) {
    dafny.DafnySequence<? extends AttributeValue> _28_x = __source;
    return __default.IsValid__PreparedStatementParameters(_28_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends AttributeValue>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends AttributeValue>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<AttributeValue> empty(AttributeValue._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends AttributeValue>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends AttributeValue>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
