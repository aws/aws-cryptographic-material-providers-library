// Class Error
// Dafny class Error compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Error {
  public Error() {
  }
  private static final dafny.TypeDescriptor<Error> _TYPE = dafny.TypeDescriptor.<Error>referenceWithInitializer(Error.class, () -> Error.Default());
  public static dafny.TypeDescriptor<Error> _typeDescriptor() {
    return (dafny.TypeDescriptor<Error>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Error theDefault = software.amazon.cryptography.metrics.internaldafny.types.Error.create_MetricsPublishError(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static Error Default() {
    return theDefault;
  }
  public static Error create_MetricsPublishError(dafny.DafnySequence<? extends Character> message) {
    return new Error_MetricsPublishError(message);
  }
  public static Error create_MetricsPutError(dafny.DafnySequence<? extends Character> message) {
    return new Error_MetricsPutError(message);
  }
  public static Error create_MetricsServiceError(dafny.DafnySequence<? extends Character> message) {
    return new Error_MetricsServiceError(message);
  }
  public static Error create_CollectionOfErrors(dafny.DafnySequence<? extends Error> list, dafny.DafnySequence<? extends Character> message) {
    return new Error_CollectionOfErrors(list, message);
  }
  public static Error create_Opaque(Object obj) {
    return new Error_Opaque(obj);
  }
  public static Error create_OpaqueWithText(Object obj, dafny.DafnySequence<? extends Character> objMessage) {
    return new Error_OpaqueWithText(obj, objMessage);
  }
  public boolean is_MetricsPublishError() { return this instanceof Error_MetricsPublishError; }
  public boolean is_MetricsPutError() { return this instanceof Error_MetricsPutError; }
  public boolean is_MetricsServiceError() { return this instanceof Error_MetricsServiceError; }
  public boolean is_CollectionOfErrors() { return this instanceof Error_CollectionOfErrors; }
  public boolean is_Opaque() { return this instanceof Error_Opaque; }
  public boolean is_OpaqueWithText() { return this instanceof Error_OpaqueWithText; }
  public dafny.DafnySequence<? extends Character> dtor_message() {
    Error d = this;
    if (d instanceof Error_MetricsPublishError) { return ((Error_MetricsPublishError)d)._message; }
    if (d instanceof Error_MetricsPutError) { return ((Error_MetricsPutError)d)._message; }
    if (d instanceof Error_MetricsServiceError) { return ((Error_MetricsServiceError)d)._message; }
    return ((Error_CollectionOfErrors)d)._message;
  }
  public dafny.DafnySequence<? extends Error> dtor_list() {
    Error d = this;
    return ((Error_CollectionOfErrors)d)._list;
  }
  public Object dtor_obj() {
    Error d = this;
    if (d instanceof Error_Opaque) { return ((Error_Opaque)d)._obj; }
    return ((Error_OpaqueWithText)d)._obj;
  }
  public dafny.DafnySequence<? extends Character> dtor_objMessage() {
    Error d = this;
    return ((Error_OpaqueWithText)d)._objMessage;
  }
}
