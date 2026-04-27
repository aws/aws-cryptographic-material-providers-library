// Class AwsKmsArn
// Dafny class AwsKmsArn compiled into Java
package AwsArnParsing_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsArn {
  public AwsKmsArn() {
  }
  public static boolean _Is(AwsArn __source) {
    AwsArn _2_a = __source;
    return __default.ValidAwsKmsArn(_2_a);
  }
  private static final dafny.TypeDescriptor<AwsArn> _TYPE = dafny.TypeDescriptor.<AwsArn>referenceWithInitializer(AwsArn.class, () -> AwsArn.Default());
  public static dafny.TypeDescriptor<AwsArn> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsArn>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
