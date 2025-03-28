// Class __default
// Dafny class __default compiled into Java
package CacheConstants_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> NULL__BYTE()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 0);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> RESOURCE__ID__CACHING__CMM()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 1);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> RESOURCE__ID__HIERARCHICAL__KEYRING()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 2);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SCOPE__ID__ENCRYPT()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 1);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SCOPE__ID__DECRYPT()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 2);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SCOPE__ID__SEARCHABLE__ENCRYPTION()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 3);
  }
  @Override
  public java.lang.String toString() {
    return "CacheConstants._default";
  }
}
