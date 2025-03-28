// Class DescribeContinuousBackupsOutput
// Dafny class DescribeContinuousBackupsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeContinuousBackupsOutput {
  public Wrappers_Compile.Option<ContinuousBackupsDescription> _ContinuousBackupsDescription;
  public DescribeContinuousBackupsOutput (Wrappers_Compile.Option<ContinuousBackupsDescription> ContinuousBackupsDescription) {
    this._ContinuousBackupsDescription = ContinuousBackupsDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeContinuousBackupsOutput o = (DescribeContinuousBackupsOutput)other;
    return true && java.util.Objects.equals(this._ContinuousBackupsDescription, o._ContinuousBackupsDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContinuousBackupsDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeContinuousBackupsOutput.DescribeContinuousBackupsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ContinuousBackupsDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeContinuousBackupsOutput> _TYPE = dafny.TypeDescriptor.<DescribeContinuousBackupsOutput>referenceWithInitializer(DescribeContinuousBackupsOutput.class, () -> DescribeContinuousBackupsOutput.Default());
  public static dafny.TypeDescriptor<DescribeContinuousBackupsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeContinuousBackupsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeContinuousBackupsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeContinuousBackupsOutput.create(Wrappers_Compile.Option.<ContinuousBackupsDescription>Default(ContinuousBackupsDescription._typeDescriptor()));
  public static DescribeContinuousBackupsOutput Default() {
    return theDefault;
  }
  public static DescribeContinuousBackupsOutput create(Wrappers_Compile.Option<ContinuousBackupsDescription> ContinuousBackupsDescription) {
    return new DescribeContinuousBackupsOutput(ContinuousBackupsDescription);
  }
  public static DescribeContinuousBackupsOutput create_DescribeContinuousBackupsOutput(Wrappers_Compile.Option<ContinuousBackupsDescription> ContinuousBackupsDescription) {
    return create(ContinuousBackupsDescription);
  }
  public boolean is_DescribeContinuousBackupsOutput() { return true; }
  public Wrappers_Compile.Option<ContinuousBackupsDescription> dtor_ContinuousBackupsDescription() {
    return this._ContinuousBackupsDescription;
  }
}
