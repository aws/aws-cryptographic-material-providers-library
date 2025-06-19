// Class AwsKmsEncryptedDataKey
// Dafny class AwsKmsEncryptedDataKey compiled into Java
package Constants_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsEncryptedDataKey {
  public AwsKmsEncryptedDataKey() {
  }
  public static boolean _Is(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey __source) {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _1_edk = __source;
    return (((_1_edk).dtor_keyProviderId()).equals(__default.PROVIDER__ID())) && (UTF8.__default.ValidUTF8Seq((_1_edk).dtor_keyProviderInfo()));
  }
  private static final dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _TYPE = dafny.TypeDescriptor.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>referenceWithInitializer(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.class, () -> software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.Default());
  public static dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
