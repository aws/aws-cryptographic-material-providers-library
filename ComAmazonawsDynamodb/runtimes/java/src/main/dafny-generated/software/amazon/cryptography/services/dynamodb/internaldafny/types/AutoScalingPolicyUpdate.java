// Class AutoScalingPolicyUpdate
// Dafny class AutoScalingPolicyUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AutoScalingPolicyUpdate {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _PolicyName;
  public AutoScalingTargetTrackingScalingPolicyConfigurationUpdate _TargetTrackingScalingPolicyConfiguration;
  public AutoScalingPolicyUpdate (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, AutoScalingTargetTrackingScalingPolicyConfigurationUpdate TargetTrackingScalingPolicyConfiguration) {
    this._PolicyName = PolicyName;
    this._TargetTrackingScalingPolicyConfiguration = TargetTrackingScalingPolicyConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AutoScalingPolicyUpdate o = (AutoScalingPolicyUpdate)other;
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
    s.append("ComAmazonawsDynamodbTypes.AutoScalingPolicyUpdate.AutoScalingPolicyUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PolicyName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TargetTrackingScalingPolicyConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AutoScalingPolicyUpdate> _TYPE = dafny.TypeDescriptor.<AutoScalingPolicyUpdate>referenceWithInitializer(AutoScalingPolicyUpdate.class, () -> AutoScalingPolicyUpdate.Default());
  public static dafny.TypeDescriptor<AutoScalingPolicyUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<AutoScalingPolicyUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AutoScalingPolicyUpdate theDefault = AutoScalingPolicyUpdate.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(AutoScalingPolicyName._typeDescriptor()), AutoScalingTargetTrackingScalingPolicyConfigurationUpdate.Default());
  public static AutoScalingPolicyUpdate Default() {
    return theDefault;
  }
  public static AutoScalingPolicyUpdate create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, AutoScalingTargetTrackingScalingPolicyConfigurationUpdate TargetTrackingScalingPolicyConfiguration) {
    return new AutoScalingPolicyUpdate(PolicyName, TargetTrackingScalingPolicyConfiguration);
  }
  public static AutoScalingPolicyUpdate create_AutoScalingPolicyUpdate(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, AutoScalingTargetTrackingScalingPolicyConfigurationUpdate TargetTrackingScalingPolicyConfiguration) {
    return create(PolicyName, TargetTrackingScalingPolicyConfiguration);
  }
  public boolean is_AutoScalingPolicyUpdate() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_PolicyName() {
    return this._PolicyName;
  }
  public AutoScalingTargetTrackingScalingPolicyConfigurationUpdate dtor_TargetTrackingScalingPolicyConfiguration() {
    return this._TargetTrackingScalingPolicyConfiguration;
  }
}
