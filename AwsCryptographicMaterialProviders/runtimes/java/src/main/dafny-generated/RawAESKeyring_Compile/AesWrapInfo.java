// Class AesWrapInfo
// Dafny class AesWrapInfo compiled into Java
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
public class AesWrapInfo {
  public dafny.DafnySequence<? extends java.lang.Byte> _iv;
  public AesWrapInfo (dafny.DafnySequence<? extends java.lang.Byte> iv) {
    this._iv = iv;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AesWrapInfo o = (AesWrapInfo)other;
    return true && java.util.Objects.equals(this._iv, o._iv);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._iv);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("RawAESKeyring.AesWrapInfo.AesWrapInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._iv));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AesWrapInfo> _TYPE = dafny.TypeDescriptor.<AesWrapInfo>referenceWithInitializer(AesWrapInfo.class, () -> AesWrapInfo.Default());
  public static dafny.TypeDescriptor<AesWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AesWrapInfo theDefault = RawAESKeyring_Compile.AesWrapInfo.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static AesWrapInfo Default() {
    return theDefault;
  }
  public static AesWrapInfo create(dafny.DafnySequence<? extends java.lang.Byte> iv) {
    return new AesWrapInfo(iv);
  }
  public static AesWrapInfo create_AesWrapInfo(dafny.DafnySequence<? extends java.lang.Byte> iv) {
    return create(iv);
  }
  public boolean is_AesWrapInfo() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_iv() {
    return this._iv;
  }
}
