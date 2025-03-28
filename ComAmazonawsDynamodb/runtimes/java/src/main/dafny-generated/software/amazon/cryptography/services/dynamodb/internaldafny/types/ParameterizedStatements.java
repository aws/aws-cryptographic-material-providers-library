// Class ParameterizedStatements
// Dafny class ParameterizedStatements compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ParameterizedStatements {
  public ParameterizedStatements() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends ParameterizedStatement> __source) {
    dafny.DafnySequence<? extends ParameterizedStatement> _21_x = __source;
    return __default.IsValid__ParameterizedStatements(_21_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends ParameterizedStatement>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends ParameterizedStatement>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<ParameterizedStatement> empty(ParameterizedStatement._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends ParameterizedStatement>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends ParameterizedStatement>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
