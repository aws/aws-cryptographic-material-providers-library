// Class RsaUnwrapInfo
// Dafny class RsaUnwrapInfo compiled into Java
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
public class RsaUnwrapInfo {
  public RsaUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RsaUnwrapInfo o = (RsaUnwrapInfo)other;
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
    s.append("RawRSAKeyring.RsaUnwrapInfo.RsaUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RsaUnwrapInfo> _TYPE = dafny.TypeDescriptor.<RsaUnwrapInfo>referenceWithInitializer(RsaUnwrapInfo.class, () -> RsaUnwrapInfo.Default());
  public static dafny.TypeDescriptor<RsaUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<RsaUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RsaUnwrapInfo theDefault = RawRSAKeyring_Compile.RsaUnwrapInfo.create();
  public static RsaUnwrapInfo Default() {
    return theDefault;
  }
  public static RsaUnwrapInfo create() {
    return new RsaUnwrapInfo();
  }
  public static RsaUnwrapInfo create_RsaUnwrapInfo() {
    return create();
  }
  public boolean is_RsaUnwrapInfo() { return true; }
  public static java.util.ArrayList<RsaUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<RsaUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new RsaUnwrapInfo());
    return singleton_iterator;
  }
}
