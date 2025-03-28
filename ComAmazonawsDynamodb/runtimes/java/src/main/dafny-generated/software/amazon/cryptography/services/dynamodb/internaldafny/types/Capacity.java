// Class Capacity
// Dafny class Capacity compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class Capacity {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _ReadCapacityUnits;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _WriteCapacityUnits;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CapacityUnits;
  public Capacity (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ReadCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> WriteCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CapacityUnits) {
    this._ReadCapacityUnits = ReadCapacityUnits;
    this._WriteCapacityUnits = WriteCapacityUnits;
    this._CapacityUnits = CapacityUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Capacity o = (Capacity)other;
    return true && java.util.Objects.equals(this._ReadCapacityUnits, o._ReadCapacityUnits) && java.util.Objects.equals(this._WriteCapacityUnits, o._WriteCapacityUnits) && java.util.Objects.equals(this._CapacityUnits, o._CapacityUnits);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._WriteCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CapacityUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Capacity.Capacity");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._WriteCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CapacityUnits));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Capacity> _TYPE = dafny.TypeDescriptor.<Capacity>referenceWithInitializer(Capacity.class, () -> Capacity.Default());
  public static dafny.TypeDescriptor<Capacity> _typeDescriptor() {
    return (dafny.TypeDescriptor<Capacity>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Capacity theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.Capacity.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(ConsumedCapacityUnits._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(ConsumedCapacityUnits._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(ConsumedCapacityUnits._typeDescriptor()));
  public static Capacity Default() {
    return theDefault;
  }
  public static Capacity create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ReadCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> WriteCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CapacityUnits) {
    return new Capacity(ReadCapacityUnits, WriteCapacityUnits, CapacityUnits);
  }
  public static Capacity create_Capacity(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ReadCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> WriteCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CapacityUnits) {
    return create(ReadCapacityUnits, WriteCapacityUnits, CapacityUnits);
  }
  public boolean is_Capacity() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_ReadCapacityUnits() {
    return this._ReadCapacityUnits;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_WriteCapacityUnits() {
    return this._WriteCapacityUnits;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CapacityUnits() {
    return this._CapacityUnits;
  }
}
