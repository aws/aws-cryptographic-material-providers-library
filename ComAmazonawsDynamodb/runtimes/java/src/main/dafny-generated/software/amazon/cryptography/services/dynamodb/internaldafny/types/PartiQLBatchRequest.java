// Class PartiQLBatchRequest
// Dafny class PartiQLBatchRequest compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PartiQLBatchRequest {
  public PartiQLBatchRequest() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends BatchStatementRequest> __source) {
    dafny.DafnySequence<? extends BatchStatementRequest> _22_x = __source;
    return __default.IsValid__PartiQLBatchRequest(_22_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends BatchStatementRequest>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends BatchStatementRequest>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<BatchStatementRequest> empty(BatchStatementRequest._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends BatchStatementRequest>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends BatchStatementRequest>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
