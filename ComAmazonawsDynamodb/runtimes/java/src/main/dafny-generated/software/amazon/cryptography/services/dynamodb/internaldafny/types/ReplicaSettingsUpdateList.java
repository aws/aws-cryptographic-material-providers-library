// Class ReplicaSettingsUpdateList
// Dafny class ReplicaSettingsUpdateList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaSettingsUpdateList {
  public ReplicaSettingsUpdateList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends ReplicaSettingsUpdate> __source) {
    dafny.DafnySequence<? extends ReplicaSettingsUpdate> _33_x = __source;
    return __default.IsValid__ReplicaSettingsUpdateList(_33_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaSettingsUpdate>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends ReplicaSettingsUpdate>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<ReplicaSettingsUpdate> empty(ReplicaSettingsUpdate._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaSettingsUpdate>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaSettingsUpdate>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
