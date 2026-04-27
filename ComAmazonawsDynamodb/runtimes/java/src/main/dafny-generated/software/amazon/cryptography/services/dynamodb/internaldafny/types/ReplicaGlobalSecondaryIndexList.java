// Class ReplicaGlobalSecondaryIndexList
// Dafny class ReplicaGlobalSecondaryIndexList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaGlobalSecondaryIndexList {
  public ReplicaGlobalSecondaryIndexList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex> __source) {
    dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex> _31_x = __source;
    return __default.IsValid__ReplicaGlobalSecondaryIndexList(_31_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<ReplicaGlobalSecondaryIndex> empty(ReplicaGlobalSecondaryIndex._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
