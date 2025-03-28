// Class __default
// Dafny class __default compiled into Java
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
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput DeserializeEDKCiphertext(dafny.DafnySequence<? extends java.lang.Byte> ciphertext, java.math.BigInteger tagLen)
  {
    java.math.BigInteger _0_encryptedKeyLength = (java.math.BigInteger.valueOf((ciphertext).length())).subtract(tagLen);
    return software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.create((ciphertext).take(_0_encryptedKeyLength), (ciphertext).drop(_0_encryptedKeyLength));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SerializeEDKCiphertext(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput encOutput) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate((encOutput).dtor_cipherText(), (encOutput).dtor_authTag());
  }
  public static java.math.BigInteger AUTH__TAG__LEN__LEN()
  {
    return java.math.BigInteger.valueOf(4L);
  }
  public static java.math.BigInteger IV__LEN__LEN()
  {
    return java.math.BigInteger.valueOf(4L);
  }
  @Override
  public java.lang.String toString() {
    return "RawAESKeyring._default";
  }
}
