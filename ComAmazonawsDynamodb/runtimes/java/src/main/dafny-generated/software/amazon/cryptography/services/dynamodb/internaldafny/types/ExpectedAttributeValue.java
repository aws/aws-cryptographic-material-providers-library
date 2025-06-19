// Class ExpectedAttributeValue
// Dafny class ExpectedAttributeValue compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExpectedAttributeValue {
  public Wrappers_Compile.Option<AttributeValue> _Value;
  public Wrappers_Compile.Option<Boolean> _Exists;
  public Wrappers_Compile.Option<ComparisonOperator> _ComparisonOperator;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> _AttributeValueList;
  public ExpectedAttributeValue (Wrappers_Compile.Option<AttributeValue> Value, Wrappers_Compile.Option<Boolean> Exists, Wrappers_Compile.Option<ComparisonOperator> ComparisonOperator, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> AttributeValueList) {
    this._Value = Value;
    this._Exists = Exists;
    this._ComparisonOperator = ComparisonOperator;
    this._AttributeValueList = AttributeValueList;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExpectedAttributeValue o = (ExpectedAttributeValue)other;
    return true && java.util.Objects.equals(this._Value, o._Value) && java.util.Objects.equals(this._Exists, o._Exists) && java.util.Objects.equals(this._ComparisonOperator, o._ComparisonOperator) && java.util.Objects.equals(this._AttributeValueList, o._AttributeValueList);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Value);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Exists);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ComparisonOperator);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeValueList);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExpectedAttributeValue.ExpectedAttributeValue");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Value));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Exists));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ComparisonOperator));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributeValueList));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExpectedAttributeValue> _TYPE = dafny.TypeDescriptor.<ExpectedAttributeValue>referenceWithInitializer(ExpectedAttributeValue.class, () -> ExpectedAttributeValue.Default());
  public static dafny.TypeDescriptor<ExpectedAttributeValue> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExpectedAttributeValue>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExpectedAttributeValue theDefault = ExpectedAttributeValue.create(Wrappers_Compile.Option.<AttributeValue>Default(AttributeValue._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<ComparisonOperator>Default(ComparisonOperator._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends AttributeValue>>Default(dafny.DafnySequence.<AttributeValue>_typeDescriptor(AttributeValue._typeDescriptor())));
  public static ExpectedAttributeValue Default() {
    return theDefault;
  }
  public static ExpectedAttributeValue create(Wrappers_Compile.Option<AttributeValue> Value, Wrappers_Compile.Option<Boolean> Exists, Wrappers_Compile.Option<ComparisonOperator> ComparisonOperator, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> AttributeValueList) {
    return new ExpectedAttributeValue(Value, Exists, ComparisonOperator, AttributeValueList);
  }
  public static ExpectedAttributeValue create_ExpectedAttributeValue(Wrappers_Compile.Option<AttributeValue> Value, Wrappers_Compile.Option<Boolean> Exists, Wrappers_Compile.Option<ComparisonOperator> ComparisonOperator, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> AttributeValueList) {
    return create(Value, Exists, ComparisonOperator, AttributeValueList);
  }
  public boolean is_ExpectedAttributeValue() { return true; }
  public Wrappers_Compile.Option<AttributeValue> dtor_Value() {
    return this._Value;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Exists() {
    return this._Exists;
  }
  public Wrappers_Compile.Option<ComparisonOperator> dtor_ComparisonOperator() {
    return this._ComparisonOperator;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> dtor_AttributeValueList() {
    return this._AttributeValueList;
  }
}
