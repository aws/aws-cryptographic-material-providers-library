// Class AutoScalingTargetTrackingScalingPolicyConfigurationDescription
// Dafny class AutoScalingTargetTrackingScalingPolicyConfigurationDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AutoScalingTargetTrackingScalingPolicyConfigurationDescription {
  public Wrappers_Compile.Option<Boolean> _DisableScaleIn;
  public Wrappers_Compile.Option<java.lang.Integer> _ScaleInCooldown;
  public Wrappers_Compile.Option<java.lang.Integer> _ScaleOutCooldown;
  public dafny.DafnySequence<? extends java.lang.Byte> _TargetValue;
  public AutoScalingTargetTrackingScalingPolicyConfigurationDescription (Wrappers_Compile.Option<Boolean> DisableScaleIn, Wrappers_Compile.Option<java.lang.Integer> ScaleInCooldown, Wrappers_Compile.Option<java.lang.Integer> ScaleOutCooldown, dafny.DafnySequence<? extends java.lang.Byte> TargetValue) {
    this._DisableScaleIn = DisableScaleIn;
    this._ScaleInCooldown = ScaleInCooldown;
    this._ScaleOutCooldown = ScaleOutCooldown;
    this._TargetValue = TargetValue;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AutoScalingTargetTrackingScalingPolicyConfigurationDescription o = (AutoScalingTargetTrackingScalingPolicyConfigurationDescription)other;
    return true && java.util.Objects.equals(this._DisableScaleIn, o._DisableScaleIn) && java.util.Objects.equals(this._ScaleInCooldown, o._ScaleInCooldown) && java.util.Objects.equals(this._ScaleOutCooldown, o._ScaleOutCooldown) && java.util.Objects.equals(this._TargetValue, o._TargetValue);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DisableScaleIn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ScaleInCooldown);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ScaleOutCooldown);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TargetValue);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AutoScalingTargetTrackingScalingPolicyConfigurationDescription.AutoScalingTargetTrackingScalingPolicyConfigurationDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._DisableScaleIn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ScaleInCooldown));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ScaleOutCooldown));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TargetValue));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AutoScalingTargetTrackingScalingPolicyConfigurationDescription> _TYPE = dafny.TypeDescriptor.<AutoScalingTargetTrackingScalingPolicyConfigurationDescription>referenceWithInitializer(AutoScalingTargetTrackingScalingPolicyConfigurationDescription.class, () -> AutoScalingTargetTrackingScalingPolicyConfigurationDescription.Default());
  public static dafny.TypeDescriptor<AutoScalingTargetTrackingScalingPolicyConfigurationDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<AutoScalingTargetTrackingScalingPolicyConfigurationDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AutoScalingTargetTrackingScalingPolicyConfigurationDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingTargetTrackingScalingPolicyConfigurationDescription.create(Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<java.lang.Integer>Default(BoundedInts_Compile.int32._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(BoundedInts_Compile.int32._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static AutoScalingTargetTrackingScalingPolicyConfigurationDescription Default() {
    return theDefault;
  }
  public static AutoScalingTargetTrackingScalingPolicyConfigurationDescription create(Wrappers_Compile.Option<Boolean> DisableScaleIn, Wrappers_Compile.Option<java.lang.Integer> ScaleInCooldown, Wrappers_Compile.Option<java.lang.Integer> ScaleOutCooldown, dafny.DafnySequence<? extends java.lang.Byte> TargetValue) {
    return new AutoScalingTargetTrackingScalingPolicyConfigurationDescription(DisableScaleIn, ScaleInCooldown, ScaleOutCooldown, TargetValue);
  }
  public static AutoScalingTargetTrackingScalingPolicyConfigurationDescription create_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(Wrappers_Compile.Option<Boolean> DisableScaleIn, Wrappers_Compile.Option<java.lang.Integer> ScaleInCooldown, Wrappers_Compile.Option<java.lang.Integer> ScaleOutCooldown, dafny.DafnySequence<? extends java.lang.Byte> TargetValue) {
    return create(DisableScaleIn, ScaleInCooldown, ScaleOutCooldown, TargetValue);
  }
  public boolean is_AutoScalingTargetTrackingScalingPolicyConfigurationDescription() { return true; }
  public Wrappers_Compile.Option<Boolean> dtor_DisableScaleIn() {
    return this._DisableScaleIn;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_ScaleInCooldown() {
    return this._ScaleInCooldown;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_ScaleOutCooldown() {
    return this._ScaleOutCooldown;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_TargetValue() {
    return this._TargetValue;
  }
}
