// Class BackupName
// Dafny class BackupName compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupName {
  public BackupName() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends Character> __source) {
    dafny.DafnySequence<? extends Character> _5_x = __source;
    return __default.IsValid__BackupName(_5_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends Character>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
