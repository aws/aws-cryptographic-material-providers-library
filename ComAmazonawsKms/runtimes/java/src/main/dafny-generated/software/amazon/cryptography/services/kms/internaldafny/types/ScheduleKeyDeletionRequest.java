// Class ScheduleKeyDeletionRequest
// Dafny class ScheduleKeyDeletionRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ScheduleKeyDeletionRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<java.lang.Integer> _PendingWindowInDays;
  public ScheduleKeyDeletionRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> PendingWindowInDays) {
    this._KeyId = KeyId;
    this._PendingWindowInDays = PendingWindowInDays;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ScheduleKeyDeletionRequest o = (ScheduleKeyDeletionRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._PendingWindowInDays, o._PendingWindowInDays);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PendingWindowInDays);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ScheduleKeyDeletionRequest.ScheduleKeyDeletionRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PendingWindowInDays));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ScheduleKeyDeletionRequest> _TYPE = dafny.TypeDescriptor.<ScheduleKeyDeletionRequest>referenceWithInitializer(ScheduleKeyDeletionRequest.class, () -> ScheduleKeyDeletionRequest.Default());
  public static dafny.TypeDescriptor<ScheduleKeyDeletionRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<ScheduleKeyDeletionRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ScheduleKeyDeletionRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ScheduleKeyDeletionRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Integer>Default(PendingWindowInDaysType._typeDescriptor()));
  public static ScheduleKeyDeletionRequest Default() {
    return theDefault;
  }
  public static ScheduleKeyDeletionRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> PendingWindowInDays) {
    return new ScheduleKeyDeletionRequest(KeyId, PendingWindowInDays);
  }
  public static ScheduleKeyDeletionRequest create_ScheduleKeyDeletionRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> PendingWindowInDays) {
    return create(KeyId, PendingWindowInDays);
  }
  public boolean is_ScheduleKeyDeletionRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_PendingWindowInDays() {
    return this._PendingWindowInDays;
  }
}
