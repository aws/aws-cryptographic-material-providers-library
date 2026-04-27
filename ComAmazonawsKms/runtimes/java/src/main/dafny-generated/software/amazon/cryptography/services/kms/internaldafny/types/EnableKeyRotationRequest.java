// Class EnableKeyRotationRequest
// Dafny class EnableKeyRotationRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EnableKeyRotationRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<java.lang.Integer> _RotationPeriodInDays;
  public EnableKeyRotationRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> RotationPeriodInDays) {
    this._KeyId = KeyId;
    this._RotationPeriodInDays = RotationPeriodInDays;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EnableKeyRotationRequest o = (EnableKeyRotationRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._RotationPeriodInDays, o._RotationPeriodInDays);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RotationPeriodInDays);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.EnableKeyRotationRequest.EnableKeyRotationRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RotationPeriodInDays));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EnableKeyRotationRequest> _TYPE = dafny.TypeDescriptor.<EnableKeyRotationRequest>referenceWithInitializer(EnableKeyRotationRequest.class, () -> EnableKeyRotationRequest.Default());
  public static dafny.TypeDescriptor<EnableKeyRotationRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<EnableKeyRotationRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EnableKeyRotationRequest theDefault = EnableKeyRotationRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Integer>Default(RotationPeriodInDaysType._typeDescriptor()));
  public static EnableKeyRotationRequest Default() {
    return theDefault;
  }
  public static EnableKeyRotationRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> RotationPeriodInDays) {
    return new EnableKeyRotationRequest(KeyId, RotationPeriodInDays);
  }
  public static EnableKeyRotationRequest create_EnableKeyRotationRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> RotationPeriodInDays) {
    return create(KeyId, RotationPeriodInDays);
  }
  public boolean is_EnableKeyRotationRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_RotationPeriodInDays() {
    return this._RotationPeriodInDays;
  }
}
