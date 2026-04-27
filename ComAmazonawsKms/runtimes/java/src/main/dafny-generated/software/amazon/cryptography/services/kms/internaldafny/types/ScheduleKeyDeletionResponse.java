// Class ScheduleKeyDeletionResponse
// Dafny class ScheduleKeyDeletionResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ScheduleKeyDeletionResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _DeletionDate;
  public Wrappers_Compile.Option<KeyState> _KeyState;
  public Wrappers_Compile.Option<java.lang.Integer> _PendingWindowInDays;
  public ScheduleKeyDeletionResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DeletionDate, Wrappers_Compile.Option<KeyState> KeyState, Wrappers_Compile.Option<java.lang.Integer> PendingWindowInDays) {
    this._KeyId = KeyId;
    this._DeletionDate = DeletionDate;
    this._KeyState = KeyState;
    this._PendingWindowInDays = PendingWindowInDays;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ScheduleKeyDeletionResponse o = (ScheduleKeyDeletionResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._DeletionDate, o._DeletionDate) && java.util.Objects.equals(this._KeyState, o._KeyState) && java.util.Objects.equals(this._PendingWindowInDays, o._PendingWindowInDays);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DeletionDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyState);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PendingWindowInDays);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ScheduleKeyDeletionResponse.ScheduleKeyDeletionResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DeletionDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyState));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PendingWindowInDays));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ScheduleKeyDeletionResponse> _TYPE = dafny.TypeDescriptor.<ScheduleKeyDeletionResponse>referenceWithInitializer(ScheduleKeyDeletionResponse.class, () -> ScheduleKeyDeletionResponse.Default());
  public static dafny.TypeDescriptor<ScheduleKeyDeletionResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ScheduleKeyDeletionResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ScheduleKeyDeletionResponse theDefault = ScheduleKeyDeletionResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<KeyState>Default(KeyState._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(PendingWindowInDaysType._typeDescriptor()));
  public static ScheduleKeyDeletionResponse Default() {
    return theDefault;
  }
  public static ScheduleKeyDeletionResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DeletionDate, Wrappers_Compile.Option<KeyState> KeyState, Wrappers_Compile.Option<java.lang.Integer> PendingWindowInDays) {
    return new ScheduleKeyDeletionResponse(KeyId, DeletionDate, KeyState, PendingWindowInDays);
  }
  public static ScheduleKeyDeletionResponse create_ScheduleKeyDeletionResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DeletionDate, Wrappers_Compile.Option<KeyState> KeyState, Wrappers_Compile.Option<java.lang.Integer> PendingWindowInDays) {
    return create(KeyId, DeletionDate, KeyState, PendingWindowInDays);
  }
  public boolean is_ScheduleKeyDeletionResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_DeletionDate() {
    return this._DeletionDate;
  }
  public Wrappers_Compile.Option<KeyState> dtor_KeyState() {
    return this._KeyState;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_PendingWindowInDays() {
    return this._PendingWindowInDays;
  }
}
