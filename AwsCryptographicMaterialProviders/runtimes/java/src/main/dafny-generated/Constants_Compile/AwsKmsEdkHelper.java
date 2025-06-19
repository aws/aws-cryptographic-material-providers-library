// Class AwsKmsEdkHelper
// Dafny class AwsKmsEdkHelper compiled into Java
package Constants_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsEdkHelper {
  public software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _edk;
  public AwsArnParsing_Compile.AwsArn _arn;
  public AwsKmsEdkHelper (software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk, AwsArnParsing_Compile.AwsArn arn) {
    this._edk = edk;
    this._arn = arn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AwsKmsEdkHelper o = (AwsKmsEdkHelper)other;
    return true && java.util.Objects.equals(this._edk, o._edk) && java.util.Objects.equals(this._arn, o._arn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._edk);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._arn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Constants.AwsKmsEdkHelper.AwsKmsEdkHelper");
    s.append("(");
    s.append(dafny.Helpers.toString(this._edk));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._arn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AwsKmsEdkHelper> _TYPE = dafny.TypeDescriptor.<AwsKmsEdkHelper>referenceWithInitializer(AwsKmsEdkHelper.class, () -> AwsKmsEdkHelper.Default());
  public static dafny.TypeDescriptor<AwsKmsEdkHelper> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsEdkHelper>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AwsKmsEdkHelper theDefault = AwsKmsEdkHelper.create(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.Default(), AwsArnParsing_Compile.AwsArn.Default());
  public static AwsKmsEdkHelper Default() {
    return theDefault;
  }
  public static AwsKmsEdkHelper create(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk, AwsArnParsing_Compile.AwsArn arn) {
    return new AwsKmsEdkHelper(edk, arn);
  }
  public static AwsKmsEdkHelper create_AwsKmsEdkHelper(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk, AwsArnParsing_Compile.AwsArn arn) {
    return create(edk, arn);
  }
  public boolean is_AwsKmsEdkHelper() { return true; }
  public software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey dtor_edk() {
    return this._edk;
  }
  public AwsArnParsing_Compile.AwsArn dtor_arn() {
    return this._arn;
  }
}
