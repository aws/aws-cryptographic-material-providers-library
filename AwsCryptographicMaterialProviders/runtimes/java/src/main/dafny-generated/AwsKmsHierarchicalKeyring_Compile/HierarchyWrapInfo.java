// Class HierarchyWrapInfo
// Dafny class HierarchyWrapInfo compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class HierarchyWrapInfo {
  public HierarchyWrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HierarchyWrapInfo o = (HierarchyWrapInfo)other;
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
    s.append("AwsKmsHierarchicalKeyring.HierarchyWrapInfo.HierarchyWrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HierarchyWrapInfo> _TYPE = dafny.TypeDescriptor.<HierarchyWrapInfo>referenceWithInitializer(HierarchyWrapInfo.class, () -> HierarchyWrapInfo.Default());
  public static dafny.TypeDescriptor<HierarchyWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<HierarchyWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HierarchyWrapInfo theDefault = AwsKmsHierarchicalKeyring_Compile.HierarchyWrapInfo.create();
  public static HierarchyWrapInfo Default() {
    return theDefault;
  }
  public static HierarchyWrapInfo create() {
    return new HierarchyWrapInfo();
  }
  public static HierarchyWrapInfo create_HierarchyWrapInfo() {
    return create();
  }
  public boolean is_HierarchyWrapInfo() { return true; }
  public static java.util.ArrayList<HierarchyWrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<HierarchyWrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new HierarchyWrapInfo());
    return singleton_iterator;
  }
}
