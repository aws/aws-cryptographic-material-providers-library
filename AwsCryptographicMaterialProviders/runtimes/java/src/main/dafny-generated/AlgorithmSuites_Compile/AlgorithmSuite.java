// Class AlgorithmSuite
// Dafny class AlgorithmSuite compiled into Java
package AlgorithmSuites_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class AlgorithmSuite {
  public AlgorithmSuite() {
  }
  public static boolean _Is(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo __source) {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_a = __source;
    return __default.AlgorithmSuite_q(_0_a);
  }
  private static final dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> _TYPE = dafny.TypeDescriptor.<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>referenceWithInitializer(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.class, () -> software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.Default());
  public static dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
