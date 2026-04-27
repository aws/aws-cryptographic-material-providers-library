// Class AmazonDynamodbTableArn
// Dafny class AmazonDynamodbTableArn compiled into Java
package AwsArnParsing_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AmazonDynamodbTableArn {
  public AmazonDynamodbTableArn() {
  }
  public static boolean _Is(AwsArn __source) {
    AwsArn _4_a = __source;
    return __default.ValidAmazonDynamodbArn(_4_a);
  }
  private static final dafny.TypeDescriptor<AwsArn> _TYPE = dafny.TypeDescriptor.<AwsArn>referenceWithInitializer(AwsArn.class, () -> AwsArn.Default());
  public static dafny.TypeDescriptor<AwsArn> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsArn>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
