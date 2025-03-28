// Class BillingModeSummary
// Dafny class BillingModeSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BillingModeSummary {
  public Wrappers_Compile.Option<BillingMode> _BillingMode;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastUpdateToPayPerRequestDateTime;
  public BillingModeSummary (Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateToPayPerRequestDateTime) {
    this._BillingMode = BillingMode;
    this._LastUpdateToPayPerRequestDateTime = LastUpdateToPayPerRequestDateTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BillingModeSummary o = (BillingModeSummary)other;
    return true && java.util.Objects.equals(this._BillingMode, o._BillingMode) && java.util.Objects.equals(this._LastUpdateToPayPerRequestDateTime, o._LastUpdateToPayPerRequestDateTime);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BillingMode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastUpdateToPayPerRequestDateTime);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BillingModeSummary.BillingModeSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BillingMode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastUpdateToPayPerRequestDateTime));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BillingModeSummary> _TYPE = dafny.TypeDescriptor.<BillingModeSummary>referenceWithInitializer(BillingModeSummary.class, () -> BillingModeSummary.Default());
  public static dafny.TypeDescriptor<BillingModeSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<BillingModeSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BillingModeSummary theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingModeSummary.create(Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static BillingModeSummary Default() {
    return theDefault;
  }
  public static BillingModeSummary create(Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateToPayPerRequestDateTime) {
    return new BillingModeSummary(BillingMode, LastUpdateToPayPerRequestDateTime);
  }
  public static BillingModeSummary create_BillingModeSummary(Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdateToPayPerRequestDateTime) {
    return create(BillingMode, LastUpdateToPayPerRequestDateTime);
  }
  public boolean is_BillingModeSummary() { return true; }
  public Wrappers_Compile.Option<BillingMode> dtor_BillingMode() {
    return this._BillingMode;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastUpdateToPayPerRequestDateTime() {
    return this._LastUpdateToPayPerRequestDateTime;
  }
}
