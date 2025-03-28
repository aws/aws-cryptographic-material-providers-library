// Class __default
// Dafny class __default compiled into Java
package LocalCMC_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__K, __V> void RemoveValue(dafny.TypeDescriptor<__K> _td___K, dafny.TypeDescriptor<__V> _td___V, __K k0, dafny.DafnyMap<? extends __K, ? extends __V> m)
  {
    dafny.DafnyMap<? extends __K, ? extends __V> _0_m_k;
    _0_m_k = dafny.DafnyMap.<__K, __V>subtract(m, dafny.DafnySet.<__K> of(k0));
  }
  public static Ref<CacheEntry> NULL()
  {
    return LocalCMC_Compile.Ref.<CacheEntry>create_Null(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
  }
  public static int INT32__MAX__VALUE()
  {
    return 2040109465;
  }
  public static long INT64__MAX__VALUE()
  {
    return (long) 8762203435012037017L;
  }
  @Override
  public java.lang.String toString() {
    return "LocalCMC._default";
  }
}
