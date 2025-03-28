// Class EcdhUnwrapInfo
// Dafny class EcdhUnwrapInfo compiled into Java
package EcdhEdkWrapping_Compile;

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
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;
import MrkAwareStrictMultiKeyring_Compile.*;
import LocalCMC_Compile.*;
import StormTracker_Compile.*;
import software.amazon.cryptography.internaldafny.StormTrackingCMC.*;
import CacheConstants_Compile.*;
import AwsKmsHierarchicalKeyring_Compile.*;
import AwsKmsRsaKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class EcdhUnwrapInfo {
  public EcdhUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EcdhUnwrapInfo o = (EcdhUnwrapInfo)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("EcdhEdkWrapping.EcdhUnwrapInfo.EcdhUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EcdhUnwrapInfo> _TYPE = dafny.TypeDescriptor.<EcdhUnwrapInfo>referenceWithInitializer(EcdhUnwrapInfo.class, () -> EcdhUnwrapInfo.Default());
  public static dafny.TypeDescriptor<EcdhUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<EcdhUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EcdhUnwrapInfo theDefault = EcdhEdkWrapping_Compile.EcdhUnwrapInfo.create();
  public static EcdhUnwrapInfo Default() {
    return theDefault;
  }
  public static EcdhUnwrapInfo create() {
    return new EcdhUnwrapInfo();
  }
  public static EcdhUnwrapInfo create_EcdhUnwrapInfo() {
    return create();
  }
  public boolean is_EcdhUnwrapInfo() { return true; }
  public static java.util.ArrayList<EcdhUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<EcdhUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new EcdhUnwrapInfo());
    return singleton_iterator;
  }
}
