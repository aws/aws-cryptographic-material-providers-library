// Class GlobalTableGlobalSecondaryIndexSettingsUpdateList
// Dafny class GlobalTableGlobalSecondaryIndexSettingsUpdateList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalTableGlobalSecondaryIndexSettingsUpdateList {
  public GlobalTableGlobalSecondaryIndexSettingsUpdateList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate> __source) {
    dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate> _3_x = __source;
    return __default.IsValid__GlobalTableGlobalSecondaryIndexSettingsUpdateList(_3_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<GlobalTableGlobalSecondaryIndexSettingsUpdate> empty(GlobalTableGlobalSecondaryIndexSettingsUpdate._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
