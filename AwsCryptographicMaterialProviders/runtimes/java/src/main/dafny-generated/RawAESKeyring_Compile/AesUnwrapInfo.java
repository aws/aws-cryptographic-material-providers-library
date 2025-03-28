// Class AesUnwrapInfo
// Dafny class AesUnwrapInfo compiled into Java
package RawAESKeyring_Compile;

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
import EcdhEdkWrapping_Compile.*;
import RawECDHKeyring_Compile.*;
import AwsKmsEcdhKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AesUnwrapInfo {
  public AesUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AesUnwrapInfo o = (AesUnwrapInfo)other;
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
    s.append("RawAESKeyring.AesUnwrapInfo.AesUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AesUnwrapInfo> _TYPE = dafny.TypeDescriptor.<AesUnwrapInfo>referenceWithInitializer(AesUnwrapInfo.class, () -> AesUnwrapInfo.Default());
  public static dafny.TypeDescriptor<AesUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AesUnwrapInfo theDefault = RawAESKeyring_Compile.AesUnwrapInfo.create();
  public static AesUnwrapInfo Default() {
    return theDefault;
  }
  public static AesUnwrapInfo create() {
    return new AesUnwrapInfo();
  }
  public static AesUnwrapInfo create_AesUnwrapInfo() {
    return create();
  }
  public boolean is_AesUnwrapInfo() { return true; }
  public static java.util.ArrayList<AesUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<AesUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new AesUnwrapInfo());
    return singleton_iterator;
  }
}
