// Class AmazonDynamodbTableName
// Dafny class AmazonDynamodbTableName compiled into Java
package AwsArnParsing_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AmazonDynamodbTableName {
  public AwsArn _a;
  public AmazonDynamodbTableName (AwsArn a) {
    this._a = a;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AmazonDynamodbTableName o = (AmazonDynamodbTableName)other;
    return true && java.util.Objects.equals(this._a, o._a);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._a);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsArnParsing.AmazonDynamodbTableName.AmazonDynamodbTableArn");
    s.append("(");
    s.append(dafny.Helpers.toString(this._a));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AmazonDynamodbTableName> _TYPE = dafny.TypeDescriptor.<AmazonDynamodbTableName>referenceWithInitializer(AmazonDynamodbTableName.class, () -> AmazonDynamodbTableName.Default());
  public static dafny.TypeDescriptor<AmazonDynamodbTableName> _typeDescriptor() {
    return (dafny.TypeDescriptor<AmazonDynamodbTableName>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AmazonDynamodbTableName theDefault = AmazonDynamodbTableName.create(AwsArn.Default());
  public static AmazonDynamodbTableName Default() {
    return theDefault;
  }
  public static AmazonDynamodbTableName create(AwsArn a) {
    return new AmazonDynamodbTableName(a);
  }
  public static AmazonDynamodbTableName create_AmazonDynamodbTableArn(AwsArn a) {
    return create(a);
  }
  public boolean is_AmazonDynamodbTableArn() { return true; }
  public AwsArn dtor_a() {
    return this._a;
  }
  public dafny.DafnySequence<? extends Character> GetTableName() {
    AmazonDynamodbTableName _source0 = this;
    AwsArn _0___mcc_h0 = ((AwsArnParsing_Compile.AmazonDynamodbTableName)_source0)._a;
    AwsArn _1_a = _0___mcc_h0;
    return ((_1_a).dtor_resource()).dtor_value();
  }
}
