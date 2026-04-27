// Class Condition
// Dafny class Condition compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Condition {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> _AttributeValueList;
  public ComparisonOperator _ComparisonOperator;
  public Condition (Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> AttributeValueList, ComparisonOperator ComparisonOperator) {
    this._AttributeValueList = AttributeValueList;
    this._ComparisonOperator = ComparisonOperator;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Condition o = (Condition)other;
    return true && java.util.Objects.equals(this._AttributeValueList, o._AttributeValueList) && java.util.Objects.equals(this._ComparisonOperator, o._ComparisonOperator);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeValueList);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ComparisonOperator);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Condition.Condition");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AttributeValueList));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ComparisonOperator));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Condition> _TYPE = dafny.TypeDescriptor.<Condition>referenceWithInitializer(Condition.class, () -> Condition.Default());
  public static dafny.TypeDescriptor<Condition> _typeDescriptor() {
    return (dafny.TypeDescriptor<Condition>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Condition theDefault = Condition.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends AttributeValue>>Default(dafny.DafnySequence.<AttributeValue>_typeDescriptor(AttributeValue._typeDescriptor())), ComparisonOperator.Default());
  public static Condition Default() {
    return theDefault;
  }
  public static Condition create(Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> AttributeValueList, ComparisonOperator ComparisonOperator) {
    return new Condition(AttributeValueList, ComparisonOperator);
  }
  public static Condition create_Condition(Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> AttributeValueList, ComparisonOperator ComparisonOperator) {
    return create(AttributeValueList, ComparisonOperator);
  }
  public boolean is_Condition() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> dtor_AttributeValueList() {
    return this._AttributeValueList;
  }
  public ComparisonOperator dtor_ComparisonOperator() {
    return this._ComparisonOperator;
  }
}
