// Class AmazonDynamodbResource
// Dafny class AmazonDynamodbResource compiled into Java
package AwsArnParsing_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AmazonDynamodbResource {
  public AmazonDynamodbResource() {
  }
  public static boolean _Is(AwsResource __source) {
    AwsResource _5_r = __source;
    return __default.ValidAmazonDynamodbResource(_5_r);
  }
  private static final dafny.TypeDescriptor<AwsResource> _TYPE = dafny.TypeDescriptor.<AwsResource>referenceWithInitializer(AwsResource.class, () -> AwsResource.Default());
  public static dafny.TypeDescriptor<AwsResource> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsResource>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
