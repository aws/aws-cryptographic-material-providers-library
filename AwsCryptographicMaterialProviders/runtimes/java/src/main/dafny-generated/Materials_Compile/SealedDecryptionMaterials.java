// Class SealedDecryptionMaterials
// Dafny class SealedDecryptionMaterials compiled into Java
package Materials_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class SealedDecryptionMaterials {
  public SealedDecryptionMaterials() {
  }
  public static boolean _Is(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials __source) {
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _1_d = __source;
    return __default.DecryptionMaterialsWithPlaintextDataKey(_1_d);
  }
  private static final dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials> _TYPE = dafny.TypeDescriptor.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>referenceWithInitializer(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials.class, () -> software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials.Default());
  public static dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials> _typeDescriptor() {
    return (dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
