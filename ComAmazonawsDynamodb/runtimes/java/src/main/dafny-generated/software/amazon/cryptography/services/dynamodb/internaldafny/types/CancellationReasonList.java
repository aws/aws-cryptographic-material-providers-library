// Class CancellationReasonList
// Dafny class CancellationReasonList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CancellationReasonList {
  public CancellationReasonList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends CancellationReason> __source) {
    dafny.DafnySequence<? extends CancellationReason> _11_x = __source;
    return __default.IsValid__CancellationReasonList(_11_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends CancellationReason>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends CancellationReason>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<CancellationReason> empty(CancellationReason._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends CancellationReason>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends CancellationReason>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
