// Class GlobalSecondaryIndexAutoScalingUpdateList
// Dafny class GlobalSecondaryIndexAutoScalingUpdateList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalSecondaryIndexAutoScalingUpdateList {
  public GlobalSecondaryIndexAutoScalingUpdateList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate> __source) {
    dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate> _2_x = __source;
    return __default.IsValid__GlobalSecondaryIndexAutoScalingUpdateList(_2_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<GlobalSecondaryIndexAutoScalingUpdate> empty(GlobalSecondaryIndexAutoScalingUpdate._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
