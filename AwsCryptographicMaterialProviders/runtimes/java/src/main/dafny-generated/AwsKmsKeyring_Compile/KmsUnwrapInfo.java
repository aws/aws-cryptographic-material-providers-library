// Class KmsUnwrapInfo
// Dafny class KmsUnwrapInfo compiled into Java
package AwsKmsKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsUnwrapInfo {
  public KmsUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsUnwrapInfo o = (KmsUnwrapInfo)other;
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
    s.append("AwsKmsKeyring.KmsUnwrapInfo.KmsUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsUnwrapInfo> _TYPE = dafny.TypeDescriptor.<KmsUnwrapInfo>referenceWithInitializer(KmsUnwrapInfo.class, () -> KmsUnwrapInfo.Default());
  public static dafny.TypeDescriptor<KmsUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsUnwrapInfo theDefault = AwsKmsKeyring_Compile.KmsUnwrapInfo.create();
  public static KmsUnwrapInfo Default() {
    return theDefault;
  }
  public static KmsUnwrapInfo create() {
    return new KmsUnwrapInfo();
  }
  public static KmsUnwrapInfo create_KmsUnwrapInfo() {
    return create();
  }
  public boolean is_KmsUnwrapInfo() { return true; }
  public static java.util.ArrayList<KmsUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<KmsUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KmsUnwrapInfo());
    return singleton_iterator;
  }
}
