// Class AwsKmsEncryptedDataKey
// Dafny class AwsKmsEncryptedDataKey compiled into Java
package Constants_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsEncryptedDataKey {
  public AwsKmsEncryptedDataKey() {
  }
  public static boolean _Is(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey __source) {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _0_edk = __source;
    return (((_0_edk).dtor_keyProviderId()).equals(__default.PROVIDER__ID())) && (UTF8.__default.ValidUTF8Seq((_0_edk).dtor_keyProviderInfo()));
  }
  private static final dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _TYPE = dafny.TypeDescriptor.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>referenceWithInitializer(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.class, () -> software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.Default());
  public static dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
