// Class AutoScalingPolicyDescription
// Dafny class AutoScalingPolicyDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AutoScalingPolicyDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _PolicyName;
  public Wrappers_Compile.Option<AutoScalingTargetTrackingScalingPolicyConfigurationDescription> _TargetTrackingScalingPolicyConfiguration;
  public AutoScalingPolicyDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, Wrappers_Compile.Option<AutoScalingTargetTrackingScalingPolicyConfigurationDescription> TargetTrackingScalingPolicyConfiguration) {
    this._PolicyName = PolicyName;
    this._TargetTrackingScalingPolicyConfiguration = TargetTrackingScalingPolicyConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AutoScalingPolicyDescription o = (AutoScalingPolicyDescription)other;
    return true && java.util.Objects.equals(this._PolicyName, o._PolicyName) && java.util.Objects.equals(this._TargetTrackingScalingPolicyConfiguration, o._TargetTrackingScalingPolicyConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PolicyName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TargetTrackingScalingPolicyConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AutoScalingPolicyDescription.AutoScalingPolicyDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PolicyName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TargetTrackingScalingPolicyConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AutoScalingPolicyDescription> _TYPE = dafny.TypeDescriptor.<AutoScalingPolicyDescription>referenceWithInitializer(AutoScalingPolicyDescription.class, () -> AutoScalingPolicyDescription.Default());
  public static dafny.TypeDescriptor<AutoScalingPolicyDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<AutoScalingPolicyDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AutoScalingPolicyDescription theDefault = AutoScalingPolicyDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(AutoScalingPolicyName._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingTargetTrackingScalingPolicyConfigurationDescription>Default(AutoScalingTargetTrackingScalingPolicyConfigurationDescription._typeDescriptor()));
  public static AutoScalingPolicyDescription Default() {
    return theDefault;
  }
  public static AutoScalingPolicyDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, Wrappers_Compile.Option<AutoScalingTargetTrackingScalingPolicyConfigurationDescription> TargetTrackingScalingPolicyConfiguration) {
    return new AutoScalingPolicyDescription(PolicyName, TargetTrackingScalingPolicyConfiguration);
  }
  public static AutoScalingPolicyDescription create_AutoScalingPolicyDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, Wrappers_Compile.Option<AutoScalingTargetTrackingScalingPolicyConfigurationDescription> TargetTrackingScalingPolicyConfiguration) {
    return create(PolicyName, TargetTrackingScalingPolicyConfiguration);
  }
  public boolean is_AutoScalingPolicyDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_PolicyName() {
    return this._PolicyName;
  }
  public Wrappers_Compile.Option<AutoScalingTargetTrackingScalingPolicyConfigurationDescription> dtor_TargetTrackingScalingPolicyConfiguration() {
    return this._TargetTrackingScalingPolicyConfiguration;
  }
}
