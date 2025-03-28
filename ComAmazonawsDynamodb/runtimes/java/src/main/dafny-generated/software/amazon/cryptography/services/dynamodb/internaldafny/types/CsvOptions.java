// Class CsvOptions
// Dafny class CsvOptions compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CsvOptions {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Delimiter;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _HeaderList;
  public CsvOptions (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Delimiter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> HeaderList) {
    this._Delimiter = Delimiter;
    this._HeaderList = HeaderList;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CsvOptions o = (CsvOptions)other;
    return true && java.util.Objects.equals(this._Delimiter, o._Delimiter) && java.util.Objects.equals(this._HeaderList, o._HeaderList);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Delimiter);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._HeaderList);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CsvOptions.CsvOptions");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Delimiter));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._HeaderList));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CsvOptions> _TYPE = dafny.TypeDescriptor.<CsvOptions>referenceWithInitializer(CsvOptions.class, () -> CsvOptions.Default());
  public static dafny.TypeDescriptor<CsvOptions> _typeDescriptor() {
    return (dafny.TypeDescriptor<CsvOptions>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CsvOptions theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.CsvOptions.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CsvDelimiter._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(CsvHeaderList._typeDescriptor()));
  public static CsvOptions Default() {
    return theDefault;
  }
  public static CsvOptions create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Delimiter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> HeaderList) {
    return new CsvOptions(Delimiter, HeaderList);
  }
  public static CsvOptions create_CsvOptions(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Delimiter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> HeaderList) {
    return create(Delimiter, HeaderList);
  }
  public boolean is_CsvOptions() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Delimiter() {
    return this._Delimiter;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_HeaderList() {
    return this._HeaderList;
  }
}
