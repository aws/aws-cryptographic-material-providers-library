// Interface UnwrapMaterial
// Dafny trait UnwrapMaterial compiled into Java
package MaterialWrapping_Compile;

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
import Constants_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public interface UnwrapMaterial<T> extends Actions_Compile.ActionWithResult<UnwrapInput, UnwrapOutput<T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<UnwrapInput, Wrappers_Compile.Result<UnwrapOutput<T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
}
