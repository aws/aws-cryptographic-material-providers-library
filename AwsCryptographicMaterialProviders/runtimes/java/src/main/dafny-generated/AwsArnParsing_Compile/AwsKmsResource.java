// Class AwsKmsResource
// Dafny class AwsKmsResource compiled into Java
package AwsArnParsing_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsResource {
  public AwsKmsResource() {
  }
  public static boolean _Is(AwsResource __source) {
    AwsResource _3_r = __source;
    return __default.ValidAwsKmsResource(_3_r);
  }
  private static final dafny.TypeDescriptor<AwsResource> _TYPE = dafny.TypeDescriptor.<AwsResource>referenceWithInitializer(AwsResource.class, () -> AwsResource.Default());
  public static dafny.TypeDescriptor<AwsResource> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsResource>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
