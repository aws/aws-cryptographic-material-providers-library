// Class ReplicationGroupUpdateList
// Dafny class ReplicationGroupUpdateList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicationGroupUpdateList {
  public ReplicationGroupUpdateList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends ReplicationGroupUpdate> __source) {
    dafny.DafnySequence<? extends ReplicationGroupUpdate> _34_x = __source;
    return __default.IsValid__ReplicationGroupUpdateList(_34_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicationGroupUpdate>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends ReplicationGroupUpdate>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<ReplicationGroupUpdate> empty(ReplicationGroupUpdate._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicationGroupUpdate>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicationGroupUpdate>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
