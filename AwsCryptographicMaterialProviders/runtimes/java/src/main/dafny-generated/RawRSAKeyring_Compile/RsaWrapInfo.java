// Class RsaWrapInfo
// Dafny class RsaWrapInfo compiled into Java
package RawRSAKeyring_Compile;

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
import RawAESKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class RsaWrapInfo {
  public RsaWrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RsaWrapInfo o = (RsaWrapInfo)other;
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
    s.append("RawRSAKeyring.RsaWrapInfo.RsaWrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RsaWrapInfo> _TYPE = dafny.TypeDescriptor.<RsaWrapInfo>referenceWithInitializer(RsaWrapInfo.class, () -> RsaWrapInfo.Default());
  public static dafny.TypeDescriptor<RsaWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<RsaWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RsaWrapInfo theDefault = RawRSAKeyring_Compile.RsaWrapInfo.create();
  public static RsaWrapInfo Default() {
    return theDefault;
  }
  public static RsaWrapInfo create() {
    return new RsaWrapInfo();
  }
  public static RsaWrapInfo create_RsaWrapInfo() {
    return create();
  }
  public boolean is_RsaWrapInfo() { return true; }
  public static java.util.ArrayList<RsaWrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<RsaWrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new RsaWrapInfo());
    return singleton_iterator;
  }
}
