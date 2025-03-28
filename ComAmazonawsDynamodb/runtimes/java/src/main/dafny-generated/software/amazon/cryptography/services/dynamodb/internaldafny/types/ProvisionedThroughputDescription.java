// Class ProvisionedThroughputDescription
// Dafny class ProvisionedThroughputDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ProvisionedThroughputDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastIncreaseDateTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastDecreaseDateTime;
  public Wrappers_Compile.Option<java.lang.Long> _NumberOfDecreasesToday;
  public Wrappers_Compile.Option<java.lang.Long> _ReadCapacityUnits;
  public Wrappers_Compile.Option<java.lang.Long> _WriteCapacityUnits;
  public ProvisionedThroughputDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastIncreaseDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastDecreaseDateTime, Wrappers_Compile.Option<java.lang.Long> NumberOfDecreasesToday, Wrappers_Compile.Option<java.lang.Long> ReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> WriteCapacityUnits) {
    this._LastIncreaseDateTime = LastIncreaseDateTime;
    this._LastDecreaseDateTime = LastDecreaseDateTime;
    this._NumberOfDecreasesToday = NumberOfDecreasesToday;
    this._ReadCapacityUnits = ReadCapacityUnits;
    this._WriteCapacityUnits = WriteCapacityUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ProvisionedThroughputDescription o = (ProvisionedThroughputDescription)other;
    return true && java.util.Objects.equals(this._LastIncreaseDateTime, o._LastIncreaseDateTime) && java.util.Objects.equals(this._LastDecreaseDateTime, o._LastDecreaseDateTime) && java.util.Objects.equals(this._NumberOfDecreasesToday, o._NumberOfDecreasesToday) && java.util.Objects.equals(this._ReadCapacityUnits, o._ReadCapacityUnits) && java.util.Objects.equals(this._WriteCapacityUnits, o._WriteCapacityUnits);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastIncreaseDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastDecreaseDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NumberOfDecreasesToday);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._WriteCapacityUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ProvisionedThroughputDescription.ProvisionedThroughputDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._LastIncreaseDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastDecreaseDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NumberOfDecreasesToday));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._WriteCapacityUnits));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ProvisionedThroughputDescription> _TYPE = dafny.TypeDescriptor.<ProvisionedThroughputDescription>referenceWithInitializer(ProvisionedThroughputDescription.class, () -> ProvisionedThroughputDescription.Default());
  public static dafny.TypeDescriptor<ProvisionedThroughputDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ProvisionedThroughputDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ProvisionedThroughputDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ProvisionedThroughputDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(NonNegativeLongObject._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(NonNegativeLongObject._typeDescriptor()));
  public static ProvisionedThroughputDescription Default() {
    return theDefault;
  }
  public static ProvisionedThroughputDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastIncreaseDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastDecreaseDateTime, Wrappers_Compile.Option<java.lang.Long> NumberOfDecreasesToday, Wrappers_Compile.Option<java.lang.Long> ReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> WriteCapacityUnits) {
    return new ProvisionedThroughputDescription(LastIncreaseDateTime, LastDecreaseDateTime, NumberOfDecreasesToday, ReadCapacityUnits, WriteCapacityUnits);
  }
  public static ProvisionedThroughputDescription create_ProvisionedThroughputDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastIncreaseDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastDecreaseDateTime, Wrappers_Compile.Option<java.lang.Long> NumberOfDecreasesToday, Wrappers_Compile.Option<java.lang.Long> ReadCapacityUnits, Wrappers_Compile.Option<java.lang.Long> WriteCapacityUnits) {
    return create(LastIncreaseDateTime, LastDecreaseDateTime, NumberOfDecreasesToday, ReadCapacityUnits, WriteCapacityUnits);
  }
  public boolean is_ProvisionedThroughputDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastIncreaseDateTime() {
    return this._LastIncreaseDateTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastDecreaseDateTime() {
    return this._LastDecreaseDateTime;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_NumberOfDecreasesToday() {
    return this._NumberOfDecreasesToday;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ReadCapacityUnits() {
    return this._ReadCapacityUnits;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_WriteCapacityUnits() {
    return this._WriteCapacityUnits;
  }
}
