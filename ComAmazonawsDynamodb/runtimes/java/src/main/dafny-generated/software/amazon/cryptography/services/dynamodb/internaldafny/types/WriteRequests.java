// Class WriteRequests
// Dafny class WriteRequests compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class WriteRequests {
  public WriteRequests() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends WriteRequest> __source) {
    dafny.DafnySequence<? extends WriteRequest> _49_x = __source;
    return __default.IsValid__WriteRequests(_49_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends WriteRequest>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends WriteRequest>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<WriteRequest> empty(WriteRequest._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends WriteRequest>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends WriteRequest>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
