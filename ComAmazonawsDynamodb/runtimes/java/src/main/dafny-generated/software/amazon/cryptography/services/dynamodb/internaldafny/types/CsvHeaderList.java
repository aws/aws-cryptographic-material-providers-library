// Class CsvHeaderList
// Dafny class CsvHeaderList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CsvHeaderList {
  public CsvHeaderList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> __source) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _17_x = __source;
    return __default.IsValid__CsvHeaderList(_17_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(CsvHeader._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
