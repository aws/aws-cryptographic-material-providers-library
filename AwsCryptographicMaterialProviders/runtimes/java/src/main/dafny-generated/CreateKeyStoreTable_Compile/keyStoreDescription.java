// Class keyStoreDescription
// Dafny class keyStoreDescription compiled into Java
package CreateKeyStoreTable_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class keyStoreDescription {
  public keyStoreDescription() {
  }
  public static boolean _Is(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription __source) {
    software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription _0_t = __source;
    return __default.keyStoreHasExpectedConstruction_q(_0_t);
  }
  private static final dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription> _TYPE = dafny.TypeDescriptor.<software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription>referenceWithInitializer(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription.class, () -> software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription.Default());
  public static dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
