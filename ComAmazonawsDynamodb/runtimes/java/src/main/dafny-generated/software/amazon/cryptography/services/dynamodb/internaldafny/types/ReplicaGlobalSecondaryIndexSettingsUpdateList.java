// Class ReplicaGlobalSecondaryIndexSettingsUpdateList
// Dafny class ReplicaGlobalSecondaryIndexSettingsUpdateList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaGlobalSecondaryIndexSettingsUpdateList {
  public ReplicaGlobalSecondaryIndexSettingsUpdateList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate> __source) {
    dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate> _32_x = __source;
    return __default.IsValid__ReplicaGlobalSecondaryIndexSettingsUpdateList(_32_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<ReplicaGlobalSecondaryIndexSettingsUpdate> empty(ReplicaGlobalSecondaryIndexSettingsUpdate._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
