// Class ReplicaAutoScalingUpdateList
// Dafny class ReplicaAutoScalingUpdateList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaAutoScalingUpdateList {
  public ReplicaAutoScalingUpdateList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends ReplicaAutoScalingUpdate> __source) {
    dafny.DafnySequence<? extends ReplicaAutoScalingUpdate> _30_x = __source;
    return __default.IsValid__ReplicaAutoScalingUpdateList(_30_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<ReplicaAutoScalingUpdate> empty(ReplicaAutoScalingUpdate._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
