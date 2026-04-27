// Class ActiveBranchKeyItem
// Dafny class ActiveBranchKeyItem compiled into Java
package Structure_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class ActiveBranchKeyItem {
  public ActiveBranchKeyItem() {
  }
  public static boolean _Is(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> __source) {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _2_m = __source;
    return __default.ActiveBranchKeyItem_q(_2_m);
  }
  private static final dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>> _TYPE = dafny.TypeDescriptor.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>>referenceWithInitializer(dafny.DafnyMap.class, () -> dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> empty());
  public static dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
