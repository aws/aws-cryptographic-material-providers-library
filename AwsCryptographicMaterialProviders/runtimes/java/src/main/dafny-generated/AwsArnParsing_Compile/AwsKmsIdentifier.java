// Class AwsKmsIdentifier
// Dafny class AwsKmsIdentifier compiled into Java
package AwsArnParsing_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class AwsKmsIdentifier {
  public AwsKmsIdentifier() {
  }
  private static final dafny.TypeDescriptor<AwsKmsIdentifier> _TYPE = dafny.TypeDescriptor.<AwsKmsIdentifier>referenceWithInitializer(AwsKmsIdentifier.class, () -> AwsKmsIdentifier.Default());
  public static dafny.TypeDescriptor<AwsKmsIdentifier> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsIdentifier>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AwsKmsIdentifier theDefault = AwsArnParsing_Compile.AwsKmsIdentifier.create_AwsKmsArnIdentifier(AwsArn.Default());
  public static AwsKmsIdentifier Default() {
    return theDefault;
  }
  public static AwsKmsIdentifier create_AwsKmsArnIdentifier(AwsArn a) {
    return new AwsKmsIdentifier_AwsKmsArnIdentifier(a);
  }
  public static AwsKmsIdentifier create_AwsKmsRawResourceIdentifier(AwsResource r) {
    return new AwsKmsIdentifier_AwsKmsRawResourceIdentifier(r);
  }
  public boolean is_AwsKmsArnIdentifier() { return this instanceof AwsKmsIdentifier_AwsKmsArnIdentifier; }
  public boolean is_AwsKmsRawResourceIdentifier() { return this instanceof AwsKmsIdentifier_AwsKmsRawResourceIdentifier; }
  public AwsArn dtor_a() {
    AwsKmsIdentifier d = this;
    return ((AwsKmsIdentifier_AwsKmsArnIdentifier)d)._a;
  }
  public AwsResource dtor_r() {
    AwsKmsIdentifier d = this;
    return ((AwsKmsIdentifier_AwsKmsRawResourceIdentifier)d)._r;
  }
  public dafny.DafnySequence<? extends Character> ToString() {
    AwsKmsIdentifier _source0 = this;
    if (_source0.is_AwsKmsArnIdentifier()) {
      AwsArn _0___mcc_h0 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsArnIdentifier)_source0)._a;
      AwsArn _1_a = _0___mcc_h0;
      return (_1_a).ToString();
    } else {
      AwsResource _2___mcc_h1 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsRawResourceIdentifier)_source0)._r;
      AwsResource _3_r = _2___mcc_h1;
      return (_3_r).ToString();
    }
  }
}
