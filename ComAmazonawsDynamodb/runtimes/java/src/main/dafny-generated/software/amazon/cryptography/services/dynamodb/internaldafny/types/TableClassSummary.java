// Class TableClassSummary
// Dafny class TableClassSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TableClassSummary {
  public Wrappers_Compile.Option<TableClass> _TableClass;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastUpdateDateTime;
  public TableClassSummary (Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateDateTime) {
    this._TableClass = TableClass;
    this._LastUpdateDateTime = LastUpdateDateTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableClassSummary o = (TableClassSummary)other;
    return true && java.util.Objects.equals(this._TableClass, o._TableClass) && java.util.Objects.equals(this._LastUpdateDateTime, o._LastUpdateDateTime);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableClass);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastUpdateDateTime);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TableClassSummary.TableClassSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableClass));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastUpdateDateTime));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TableClassSummary> _TYPE = dafny.TypeDescriptor.<TableClassSummary>referenceWithInitializer(TableClassSummary.class, () -> TableClassSummary.Default());
  public static dafny.TypeDescriptor<TableClassSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<TableClassSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TableClassSummary theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TableClassSummary.create(Wrappers_Compile.Option.<TableClass>Default(TableClass._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static TableClassSummary Default() {
    return theDefault;
  }
  public static TableClassSummary create(Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateDateTime) {
    return new TableClassSummary(TableClass, LastUpdateDateTime);
  }
  public static TableClassSummary create_TableClassSummary(Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateDateTime) {
    return create(TableClass, LastUpdateDateTime);
  }
  public boolean is_TableClassSummary() { return true; }
  public Wrappers_Compile.Option<TableClass> dtor_TableClass() {
    return this._TableClass;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastUpdateDateTime() {
    return this._LastUpdateDateTime;
  }
}
