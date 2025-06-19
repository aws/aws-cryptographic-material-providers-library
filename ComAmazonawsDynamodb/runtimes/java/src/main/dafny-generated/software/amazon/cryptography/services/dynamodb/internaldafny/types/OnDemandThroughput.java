// Class OnDemandThroughput
// Dafny class OnDemandThroughput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class OnDemandThroughput {
  public Wrappers_Compile.Option<java.lang.Long> _MaxReadRequestUnits;
  public Wrappers_Compile.Option<java.lang.Long> _MaxWriteRequestUnits;
  public OnDemandThroughput (Wrappers_Compile.Option<java.lang.Long> MaxReadRequestUnits, Wrappers_Compile.Option<java.lang.Long> MaxWriteRequestUnits) {
    this._MaxReadRequestUnits = MaxReadRequestUnits;
    this._MaxWriteRequestUnits = MaxWriteRequestUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OnDemandThroughput o = (OnDemandThroughput)other;
    return true && java.util.Objects.equals(this._MaxReadRequestUnits, o._MaxReadRequestUnits) && java.util.Objects.equals(this._MaxWriteRequestUnits, o._MaxWriteRequestUnits);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MaxReadRequestUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MaxWriteRequestUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.OnDemandThroughput.OnDemandThroughput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._MaxReadRequestUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MaxWriteRequestUnits));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<OnDemandThroughput> _TYPE = dafny.TypeDescriptor.<OnDemandThroughput>referenceWithInitializer(OnDemandThroughput.class, () -> OnDemandThroughput.Default());
  public static dafny.TypeDescriptor<OnDemandThroughput> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDemandThroughput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OnDemandThroughput theDefault = OnDemandThroughput.create(Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()));
  public static OnDemandThroughput Default() {
    return theDefault;
  }
  public static OnDemandThroughput create(Wrappers_Compile.Option<java.lang.Long> MaxReadRequestUnits, Wrappers_Compile.Option<java.lang.Long> MaxWriteRequestUnits) {
    return new OnDemandThroughput(MaxReadRequestUnits, MaxWriteRequestUnits);
  }
  public static OnDemandThroughput create_OnDemandThroughput(Wrappers_Compile.Option<java.lang.Long> MaxReadRequestUnits, Wrappers_Compile.Option<java.lang.Long> MaxWriteRequestUnits) {
    return create(MaxReadRequestUnits, MaxWriteRequestUnits);
  }
  public boolean is_OnDemandThroughput() { return true; }
  public Wrappers_Compile.Option<java.lang.Long> dtor_MaxReadRequestUnits() {
    return this._MaxReadRequestUnits;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_MaxWriteRequestUnits() {
    return this._MaxWriteRequestUnits;
  }
}
