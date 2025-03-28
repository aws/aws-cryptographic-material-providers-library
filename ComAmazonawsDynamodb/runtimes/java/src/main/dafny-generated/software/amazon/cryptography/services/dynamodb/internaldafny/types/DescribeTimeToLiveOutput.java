// Class DescribeTimeToLiveOutput
// Dafny class DescribeTimeToLiveOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeTimeToLiveOutput {
  public Wrappers_Compile.Option<TimeToLiveDescription> _TimeToLiveDescription;
  public DescribeTimeToLiveOutput (Wrappers_Compile.Option<TimeToLiveDescription> TimeToLiveDescription) {
    this._TimeToLiveDescription = TimeToLiveDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeTimeToLiveOutput o = (DescribeTimeToLiveOutput)other;
    return true && java.util.Objects.equals(this._TimeToLiveDescription, o._TimeToLiveDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TimeToLiveDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeTimeToLiveOutput.DescribeTimeToLiveOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TimeToLiveDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeTimeToLiveOutput> _TYPE = dafny.TypeDescriptor.<DescribeTimeToLiveOutput>referenceWithInitializer(DescribeTimeToLiveOutput.class, () -> DescribeTimeToLiveOutput.Default());
  public static dafny.TypeDescriptor<DescribeTimeToLiveOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeTimeToLiveOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeTimeToLiveOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTimeToLiveOutput.create(Wrappers_Compile.Option.<TimeToLiveDescription>Default(TimeToLiveDescription._typeDescriptor()));
  public static DescribeTimeToLiveOutput Default() {
    return theDefault;
  }
  public static DescribeTimeToLiveOutput create(Wrappers_Compile.Option<TimeToLiveDescription> TimeToLiveDescription) {
    return new DescribeTimeToLiveOutput(TimeToLiveDescription);
  }
  public static DescribeTimeToLiveOutput create_DescribeTimeToLiveOutput(Wrappers_Compile.Option<TimeToLiveDescription> TimeToLiveDescription) {
    return create(TimeToLiveDescription);
  }
  public boolean is_DescribeTimeToLiveOutput() { return true; }
  public Wrappers_Compile.Option<TimeToLiveDescription> dtor_TimeToLiveDescription() {
    return this._TimeToLiveDescription;
  }
}
