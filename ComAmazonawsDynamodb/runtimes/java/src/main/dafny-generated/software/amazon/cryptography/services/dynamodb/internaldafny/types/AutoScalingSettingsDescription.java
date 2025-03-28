// Class AutoScalingSettingsDescription
// Dafny class AutoScalingSettingsDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AutoScalingSettingsDescription {
  public Wrappers_Compile.Option<java.lang.Long> _MinimumUnits;
  public Wrappers_Compile.Option<java.lang.Long> _MaximumUnits;
  public Wrappers_Compile.Option<Boolean> _AutoScalingDisabled;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _AutoScalingRoleArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AutoScalingPolicyDescription>> _ScalingPolicies;
  public AutoScalingSettingsDescription (Wrappers_Compile.Option<java.lang.Long> MinimumUnits, Wrappers_Compile.Option<java.lang.Long> MaximumUnits, Wrappers_Compile.Option<Boolean> AutoScalingDisabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AutoScalingRoleArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends AutoScalingPolicyDescription>> ScalingPolicies) {
    this._MinimumUnits = MinimumUnits;
    this._MaximumUnits = MaximumUnits;
    this._AutoScalingDisabled = AutoScalingDisabled;
    this._AutoScalingRoleArn = AutoScalingRoleArn;
    this._ScalingPolicies = ScalingPolicies;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AutoScalingSettingsDescription o = (AutoScalingSettingsDescription)other;
    return true && java.util.Objects.equals(this._MinimumUnits, o._MinimumUnits) && java.util.Objects.equals(this._MaximumUnits, o._MaximumUnits) && java.util.Objects.equals(this._AutoScalingDisabled, o._AutoScalingDisabled) && java.util.Objects.equals(this._AutoScalingRoleArn, o._AutoScalingRoleArn) && java.util.Objects.equals(this._ScalingPolicies, o._ScalingPolicies);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MinimumUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MaximumUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AutoScalingDisabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AutoScalingRoleArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ScalingPolicies);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AutoScalingSettingsDescription.AutoScalingSettingsDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._MinimumUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MaximumUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AutoScalingDisabled));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AutoScalingRoleArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ScalingPolicies));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AutoScalingSettingsDescription> _TYPE = dafny.TypeDescriptor.<AutoScalingSettingsDescription>referenceWithInitializer(AutoScalingSettingsDescription.class, () -> AutoScalingSettingsDescription.Default());
  public static dafny.TypeDescriptor<AutoScalingSettingsDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<AutoScalingSettingsDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AutoScalingSettingsDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingSettingsDescription.create(Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends AutoScalingPolicyDescription>>Default(dafny.DafnySequence.<AutoScalingPolicyDescription>_typeDescriptor(AutoScalingPolicyDescription._typeDescriptor())));
  public static AutoScalingSettingsDescription Default() {
    return theDefault;
  }
  public static AutoScalingSettingsDescription create(Wrappers_Compile.Option<java.lang.Long> MinimumUnits, Wrappers_Compile.Option<java.lang.Long> MaximumUnits, Wrappers_Compile.Option<Boolean> AutoScalingDisabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AutoScalingRoleArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends AutoScalingPolicyDescription>> ScalingPolicies) {
    return new AutoScalingSettingsDescription(MinimumUnits, MaximumUnits, AutoScalingDisabled, AutoScalingRoleArn, ScalingPolicies);
  }
  public static AutoScalingSettingsDescription create_AutoScalingSettingsDescription(Wrappers_Compile.Option<java.lang.Long> MinimumUnits, Wrappers_Compile.Option<java.lang.Long> MaximumUnits, Wrappers_Compile.Option<Boolean> AutoScalingDisabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AutoScalingRoleArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends AutoScalingPolicyDescription>> ScalingPolicies) {
    return create(MinimumUnits, MaximumUnits, AutoScalingDisabled, AutoScalingRoleArn, ScalingPolicies);
  }
  public boolean is_AutoScalingSettingsDescription() { return true; }
  public Wrappers_Compile.Option<java.lang.Long> dtor_MinimumUnits() {
    return this._MinimumUnits;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_MaximumUnits() {
    return this._MaximumUnits;
  }
  public Wrappers_Compile.Option<Boolean> dtor_AutoScalingDisabled() {
    return this._AutoScalingDisabled;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_AutoScalingRoleArn() {
    return this._AutoScalingRoleArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AutoScalingPolicyDescription>> dtor_ScalingPolicies() {
    return this._ScalingPolicies;
  }
}
