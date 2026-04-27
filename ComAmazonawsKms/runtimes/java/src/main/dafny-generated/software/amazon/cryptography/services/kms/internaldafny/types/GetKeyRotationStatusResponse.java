// Class GetKeyRotationStatusResponse
// Dafny class GetKeyRotationStatusResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetKeyRotationStatusResponse {
  public Wrappers_Compile.Option<Boolean> _KeyRotationEnabled;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<java.lang.Integer> _RotationPeriodInDays;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextRotationDate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _OnDemandRotationStartDate;
  public GetKeyRotationStatusResponse (Wrappers_Compile.Option<Boolean> KeyRotationEnabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<java.lang.Integer> RotationPeriodInDays, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextRotationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> OnDemandRotationStartDate) {
    this._KeyRotationEnabled = KeyRotationEnabled;
    this._KeyId = KeyId;
    this._RotationPeriodInDays = RotationPeriodInDays;
    this._NextRotationDate = NextRotationDate;
    this._OnDemandRotationStartDate = OnDemandRotationStartDate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetKeyRotationStatusResponse o = (GetKeyRotationStatusResponse)other;
    return true && java.util.Objects.equals(this._KeyRotationEnabled, o._KeyRotationEnabled) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._RotationPeriodInDays, o._RotationPeriodInDays) && java.util.Objects.equals(this._NextRotationDate, o._NextRotationDate) && java.util.Objects.equals(this._OnDemandRotationStartDate, o._OnDemandRotationStartDate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyRotationEnabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RotationPeriodInDays);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextRotationDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandRotationStartDate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetKeyRotationStatusResponse.GetKeyRotationStatusResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyRotationEnabled));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RotationPeriodInDays));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextRotationDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandRotationStartDate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetKeyRotationStatusResponse> _TYPE = dafny.TypeDescriptor.<GetKeyRotationStatusResponse>referenceWithInitializer(GetKeyRotationStatusResponse.class, () -> GetKeyRotationStatusResponse.Default());
  public static dafny.TypeDescriptor<GetKeyRotationStatusResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetKeyRotationStatusResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetKeyRotationStatusResponse theDefault = GetKeyRotationStatusResponse.create(Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(RotationPeriodInDaysType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static GetKeyRotationStatusResponse Default() {
    return theDefault;
  }
  public static GetKeyRotationStatusResponse create(Wrappers_Compile.Option<Boolean> KeyRotationEnabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<java.lang.Integer> RotationPeriodInDays, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextRotationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> OnDemandRotationStartDate) {
    return new GetKeyRotationStatusResponse(KeyRotationEnabled, KeyId, RotationPeriodInDays, NextRotationDate, OnDemandRotationStartDate);
  }
  public static GetKeyRotationStatusResponse create_GetKeyRotationStatusResponse(Wrappers_Compile.Option<Boolean> KeyRotationEnabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<java.lang.Integer> RotationPeriodInDays, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextRotationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> OnDemandRotationStartDate) {
    return create(KeyRotationEnabled, KeyId, RotationPeriodInDays, NextRotationDate, OnDemandRotationStartDate);
  }
  public boolean is_GetKeyRotationStatusResponse() { return true; }
  public Wrappers_Compile.Option<Boolean> dtor_KeyRotationEnabled() {
    return this._KeyRotationEnabled;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_RotationPeriodInDays() {
    return this._RotationPeriodInDays;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextRotationDate() {
    return this._NextRotationDate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_OnDemandRotationStartDate() {
    return this._OnDemandRotationStartDate;
  }
}
