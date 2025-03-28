// Class CacheState
// Dafny class CacheState compiled into Java
package StormTracker_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class CacheState {
  public CacheState() {
  }
  private static final dafny.TypeDescriptor<CacheState> _TYPE = dafny.TypeDescriptor.<CacheState>referenceWithInitializer(CacheState.class, () -> CacheState.Default());
  public static dafny.TypeDescriptor<CacheState> _typeDescriptor() {
    return (dafny.TypeDescriptor<CacheState>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CacheState theDefault = StormTracker_Compile.CacheState.create_EmptyWait();
  public static CacheState Default() {
    return theDefault;
  }
  public static CacheState create_EmptyWait() {
    return new CacheState_EmptyWait();
  }
  public static CacheState create_EmptyFetch() {
    return new CacheState_EmptyFetch();
  }
  public static CacheState create_Full(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput data) {
    return new CacheState_Full(data);
  }
  public boolean is_EmptyWait() { return this instanceof CacheState_EmptyWait; }
  public boolean is_EmptyFetch() { return this instanceof CacheState_EmptyFetch; }
  public boolean is_Full() { return this instanceof CacheState_Full; }
  public software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput dtor_data() {
    CacheState d = this;
    return ((CacheState_Full)d)._data;
  }
}
