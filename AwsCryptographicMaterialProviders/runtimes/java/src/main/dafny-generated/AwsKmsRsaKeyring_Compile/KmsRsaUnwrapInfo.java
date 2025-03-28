// Class KmsRsaUnwrapInfo
// Dafny class KmsRsaUnwrapInfo compiled into Java
package AwsKmsRsaKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsRsaUnwrapInfo {
  public KmsRsaUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsRsaUnwrapInfo o = (KmsRsaUnwrapInfo)other;
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
    s.append("AwsKmsRsaKeyring.KmsRsaUnwrapInfo.KmsRsaUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsRsaUnwrapInfo> _TYPE = dafny.TypeDescriptor.<KmsRsaUnwrapInfo>referenceWithInitializer(KmsRsaUnwrapInfo.class, () -> KmsRsaUnwrapInfo.Default());
  public static dafny.TypeDescriptor<KmsRsaUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsRsaUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsRsaUnwrapInfo theDefault = AwsKmsRsaKeyring_Compile.KmsRsaUnwrapInfo.create();
  public static KmsRsaUnwrapInfo Default() {
    return theDefault;
  }
  public static KmsRsaUnwrapInfo create() {
    return new KmsRsaUnwrapInfo();
  }
  public static KmsRsaUnwrapInfo create_KmsRsaUnwrapInfo() {
    return create();
  }
  public boolean is_KmsRsaUnwrapInfo() { return true; }
  public static java.util.ArrayList<KmsRsaUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<KmsRsaUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KmsRsaUnwrapInfo());
    return singleton_iterator;
  }
}
